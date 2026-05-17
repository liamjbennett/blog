#!/usr/bin/env python3
"""Fetch Readwise Reader bookmarks and create a new snippet post."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib import error, parse, request


READWISE_API = "https://readwise.io/api/v3/list/"
SNIPPETS_DIR = Path("content/snippets")
DEFAULT_OP_REFERENCE = "op://Personal/readwise/token"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a snippet from Readwise Reader items tagged 'bookmarks'."
    )
    parser.add_argument(
        "--tag",
        default="bookmarks",
        help="Readwise Reader tag to filter by (default: bookmarks).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Maximum number of Reader items to include in the snippet (default: 25).",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Readwise API token. If omitted, token is read from 1Password.",
    )
    parser.add_argument(
        "--op-reference",
        default=os.getenv("READWISE_OP_REFERENCE") or DEFAULT_OP_REFERENCE,
        help=(
            "1Password secret reference for Readwise token "
            f"(default: {DEFAULT_OP_REFERENCE})."
        ),
    )
    return parser.parse_args()


def get_token_from_1password(op_reference: str) -> str:
    """Get Readwise token from 1Password vault using `op read`."""
    try:
        token = subprocess.check_output(["op", "read", op_reference], text=True).strip()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "1Password CLI (op) not found. Install from https://1password.com/downloads/command-line/"
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            "Failed to retrieve Readwise token from 1Password. "
            f"Ensure the item exists at {op_reference}. Error: {exc}"
        ) from exc

    if not token:
        raise RuntimeError(
            f"Empty token retrieved from 1Password reference {op_reference}."
        )

    return token


def resolve_token(args: argparse.Namespace) -> str:
    if args.token:
        return args.token

    env_token = os.getenv("READWISE_READER_TOKEN") or os.getenv("READWISE_TOKEN")
    if env_token:
        return env_token

    return get_token_from_1password(args.op_reference)


def fetch_page(token: str, params: dict[str, Any]) -> dict[str, Any]:
    query = parse.urlencode(params)
    url = f"{READWISE_API}?{query}"
    req = request.Request(
        url,
        headers={
            "Authorization": f"Token {token}",
            "Accept": "application/json",
            "User-Agent": "blog-readwise-bookmarks-script/1.0",
        },
    )

    try:
        with request.urlopen(req, timeout=30) as response:
            payload = response.read().decode("utf-8")
    except error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Readwise API request failed with HTTP {exc.code}: {message.strip()[:200]}"
        ) from exc
    except error.URLError as exc:
        raise RuntimeError(f"Could not connect to Readwise API: {exc}") from exc

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Readwise API returned invalid JSON") from exc

    if not isinstance(data, dict) or "results" not in data:
        raise RuntimeError("Readwise API response format was unexpected")

    return data


def fetch_bookmarks(token: str, tag: str, limit: int) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    next_page_cursor: str | None = None

    while len(items) < limit:
        params: dict[str, Any] = {
            "tag": tag,
            "withHtmlContent": "false",
        }
        if next_page_cursor:
            params["pageCursor"] = next_page_cursor

        data = fetch_page(token, params)
        results = data.get("results", [])
        if not isinstance(results, list):
            raise RuntimeError("Readwise API returned an invalid 'results' value")

        for item in results:
            if not isinstance(item, dict):
                continue
            items.append(item)
            if len(items) >= limit:
                break

        next_page_cursor = data.get("nextPageCursor")
        if not next_page_cursor:
            break

    return items[:limit]


def parse_iso_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def safe_text(value: Any, fallback: str) -> str:
    if isinstance(value, str):
        text = value.strip()
        if text:
            return text
    return fallback


def render_snippet_body(items: list[dict[str, Any]], tag: str) -> str:
    lines = [
        f"Pulled {len(items)} Readwise Reader item(s) tagged '{tag}'.",
        "",
    ]

    for item in items:
        title = safe_text(item.get("title"), "Untitled")
        url = safe_text(item.get("url"), "")
        author = safe_text(item.get("author"), "")
        created_at = parse_iso_datetime(item.get("created_at"))
        created_on = created_at.strftime("%Y-%m-%d") if created_at else ""

        line = f"- [{title}]({url})" if url else f"- {title}"
        details: list[str] = []
        if author:
            details.append(author)
        if created_on:
            details.append(created_on)
        if details:
            line += f" ({', '.join(details)})"

        lines.append(line)

    return "\n".join(lines) + "\n"


def snippet_filename(items: list[dict[str, Any]]) -> str:
    first = items[0] if items else {}
    created_at = parse_iso_datetime(first.get("created_at") if isinstance(first, dict) else None)
    timestamp = created_at or datetime.now()
    return timestamp.strftime("%Y-%m-%d-%H-%M") + ".md"


def unique_snippet_path(filename: str) -> Path:
    target = SNIPPETS_DIR / filename
    if not target.exists():
        return target

    stem = target.stem
    suffix = target.suffix
    counter = 2
    while True:
        candidate = SNIPPETS_DIR / f"{stem}-{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def build_front_matter(date_value: str) -> str:
    return "\n".join(
        [
            "---",
            'author: "liamjbennett"',
            f'date: "{date_value}"',
            'tags: ["bookmarks"]',
            "ShowToc: false",
            "ShowBreadCrumbs: false",
            'thumbnail: "/img/main/profile.jpg"',
            'mastodon_link: ""',
            'bluesky_link: ""',
            "---",
            "",
        ]
    )


def extract_date_from_filename(filename: str) -> str:
    match = re.match(r"^(\d{4}-\d{2}-\d{2})-\d{2}-\d{2}.*\\.md$", filename)
    if match:
        return match.group(1)
    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    args = parse_args()

    try:
        token = resolve_token(args)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.limit < 1:
        print("Error: --limit must be at least 1.", file=sys.stderr)
        return 1

    try:
        print(f"Fetching Readwise Reader items tagged '{args.tag}'...")
        items = fetch_bookmarks(token, args.tag, args.limit)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not items:
        print(f"No Reader items found for tag '{args.tag}'.")
        return 0

    filename = snippet_filename(items)
    output_path = unique_snippet_path(filename)
    date_value = extract_date_from_filename(output_path.name)

    content = build_front_matter(date_value) + render_snippet_body(items, args.tag)
    SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"Created snippet: {output_path}")
    print(f"Included {len(items)} item(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())