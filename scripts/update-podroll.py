#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


POCKETCASTS_API = "https://api.pocketcasts.com"
DEFAULT_OUTPUT = Path("static/podroll.xml")
OP_TITLE = "OPML file of all the podcasts I'm subscribed to:"


@dataclass(frozen=True)
class Folder:
    uuid: str
    name: str
    sort_position: int


@dataclass(frozen=True)
class Podcast:
    title: str
    description: str
    feed_url: str
    folder_uuid: str | None
    sort_position: int


def parse_json_response(response: requests.Response, action: str) -> dict:
    """Parse JSON responses and fail with useful diagnostics if the API changes."""
    content_type = response.headers.get("Content-Type", "")
    if "json" not in content_type.lower():
        body_preview = response.text.strip().replace("\n", " ")[:200]
        raise RuntimeError(
            f"Pocket Casts returned unexpected content for {action}: "
            f"HTTP {response.status_code}, Content-Type '{content_type or 'unknown'}', body '{body_preview}'"
        )

    try:
        return response.json()
    except ValueError as error:
        raise RuntimeError(f"Pocket Casts returned invalid JSON for {action}: {error}") from error


def get_credentials() -> tuple[str, str]:
    """Get Pocket Casts credentials from 1Password vault."""
    try:
        username = subprocess.check_output(
            ["op", "read", "op://Personal/pocketcasts/username"],
            text=True,
        ).strip()
        password = subprocess.check_output(
            ["op", "read", "op://Personal/pocketcasts/password"],
            text=True,
        ).strip()

        if not username or not password:
            raise RuntimeError("Empty credentials retrieved from 1Password")

        return username, password
    except FileNotFoundError as error:
        raise RuntimeError(
            "1Password CLI (op) not found. Install from https://1password.com/downloads/command-line/"
        ) from error
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            "Failed to retrieve Pocket Casts credentials from 1Password. "
            "Ensure the item exists at op://Personal/pocketcasts with 'username' and 'password' fields."
        ) from error


def authenticate(username: str, password: str) -> str:
    """Authenticate against Pocket Casts and return a bearer token."""
    response = requests.post(
        f"{POCKETCASTS_API}/user/login",
        json={"email": username, "password": password, "scope": "webplayer"},
        timeout=30,
    )
    data = parse_json_response(response, "authentication")
    if not response.ok:
        message = data.get("errorMessage") or data.get("message") or response.reason
        raise RuntimeError(f"Pocket Casts authentication failed: {message}")

    token = data.get("token") or data.get("access_token") or data.get("jwt")
    if not token:
        raise RuntimeError(
            "Pocket Casts authentication succeeded but no token was returned. "
            f"Response keys: {', '.join(sorted(data.keys())) or 'none'}"
        )
    return token


def to_int(value: object, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def normalize_description(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())


def fetch_subscriptions(token: str) -> tuple[list[Folder], list[Podcast]]:
    """Fetch folders and subscribed podcasts from Pocket Casts."""
    response = requests.post(
        f"{POCKETCASTS_API}/user/podcast/list",
        headers={"Authorization": f"Bearer {token}"},
        json={"v": 1},
        timeout=30,
    )
    data = parse_json_response(response, "podcast list lookup")
    if not response.ok:
        message = data.get("errorMessage") or data.get("message") or response.reason
        raise RuntimeError(f"Pocket Casts podcast list lookup failed: {message}")

    folders = [
        Folder(
            uuid=str(item.get("folderUuid", "")).strip(),
            name=str(item.get("name", "")).strip() or "Untitled Folder",
            sort_position=to_int(item.get("sortPosition"), 0),
        )
        for item in data.get("folders", [])
        if item.get("folderUuid")
    ]

    podcasts: list[Podcast] = []
    for item in data.get("podcasts", []):
        feed_url = str(item.get("url", "")).strip()
        if not feed_url:
            continue

        title = str(item.get("title", "")).strip() or "Untitled Podcast"
        description = normalize_description(item.get("description"))
        folder_uuid_raw = str(item.get("folderUuid", "")).strip()
        folder_uuid = folder_uuid_raw or None

        podcasts.append(
            Podcast(
                title=title,
                description=description,
                feed_url=feed_url,
                folder_uuid=folder_uuid,
                sort_position=to_int(item.get("sortPosition"), 0),
            )
        )

    return folders, podcasts


def xml_attr(name: str, value: str) -> str:
    return f'{name}="{escape(value, {"\"": "&quot;"})}"'


def build_outline_lines(title: str, podcasts: list[Podcast]) -> list[str]:
    count = len(podcasts)
    label = "podcast" if count == 1 else "podcasts"
    lines = [
        f"        <outline {xml_attr('title', title)} {xml_attr('text', f'{title} ({count} {label})')}>",
    ]

    for podcast in sorted(podcasts, key=lambda item: (item.sort_position, item.title.lower())):
        attrs = [
            xml_attr("text", podcast.title),
            xml_attr("description", podcast.description or "No description"),
            xml_attr("type", "rss"),
            xml_attr("xmlUrl", podcast.feed_url),
        ]
        lines.append(f"            <outline {' '.join(attrs)}/>")

    lines.append("        </outline>")
    return lines


def build_opml(folders: list[Folder], podcasts: list[Podcast]) -> str:
    grouped: dict[str | None, list[Podcast]] = defaultdict(list)
    for podcast in podcasts:
        grouped[podcast.folder_uuid].append(podcast)

    lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<?xml-stylesheet type=\"text/xsl\" href=\"podroll.xsl\"?>",
        "<opml version=\"1.0\">",
        "    <head>",
        f"        <title>{escape(OP_TITLE)}</title>",
        "    </head>",
        "    <body>",
    ]

    for folder in sorted(folders, key=lambda item: (item.sort_position, item.name.lower())):
        folder_podcasts = grouped.pop(folder.uuid, [])
        lines.extend(build_outline_lines(folder.name, folder_podcasts))

    unassigned = grouped.pop(None, [])
    if unassigned:
        lines.extend(build_outline_lines("Unfiled", unassigned))

    # If unknown folder UUIDs appear, keep their podcasts grouped rather than dropping them.
    for folder_uuid in sorted([key for key in grouped.keys() if key], key=str.lower):
        lines.extend(build_outline_lines(f"Folder {folder_uuid}", grouped[folder_uuid]))

    lines.extend([
        "    </body>",
        "</opml>",
        "",
    ])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch Pocket Casts subscriptions and regenerate podroll OPML."
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output path for generated OPML (default: static/podroll.xml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated OPML to stdout without writing a file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = Path(args.output)

    try:
        username, password = get_credentials()
        print("Authenticating with Pocket Casts...")
        token = authenticate(username, password)

        print("Fetching folders and podcasts...")
        folders, podcasts = fetch_subscriptions(token)
        opml = build_opml(folders, podcasts)

        if args.dry_run:
            print(opml)
            print(f"Dry run complete: {len(podcasts)} podcasts across {len(folders)} folders.")
            return 0

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(opml, encoding="utf-8")
        print(f"Updated {output_path} with {len(podcasts)} podcasts across {len(folders)} folders.")
        return 0
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except requests.RequestException as error:
        print(f"API Error: {error}", file=sys.stderr)
        return 1
    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
