#!/usr/bin/env python3
"""Fetch Readwise Reader bookmarks and create one snippet post per bookmark."""

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
READWISE_BULK_UPDATE_API = "https://readwise.io/api/v3/bulk_update/"
SNIPPETS_DIR = Path("content/snippets")
DEFAULT_OP_REFERENCE = "op://Private/Readwise/token"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create one snippet per Readwise Reader item tagged 'bookmarks'."
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
        help="Maximum number of Reader items to process (default: 25).",
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


def bulk_archive_documents(token: str, document_ids: list[str]) -> tuple[int, int]:
    archived_count = 0
    failed_count = 0

    # Readwise bulk update supports up to 50 documents per request.
    for start in range(0, len(document_ids), 50):
        chunk = document_ids[start : start + 50]
        payload = {
            "updates": [{"id": doc_id, "location": "archive"} for doc_id in chunk]
        }
        req = request.Request(
            READWISE_BULK_UPDATE_API,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Token {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "blog-readwise-bookmarks-script/1.0",
            },
            method="PATCH",
        )

        try:
            with request.urlopen(req, timeout=30) as response:
                body = response.read().decode("utf-8")
        except error.HTTPError as exc:
            message = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"Readwise archive request failed with HTTP {exc.code}: {message.strip()[:200]}"
            ) from exc
        except error.URLError as exc:
            raise RuntimeError(f"Could not connect to Readwise API for archive update: {exc}") from exc

        try:
            data = json.loads(body)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Readwise bulk archive API returned invalid JSON") from exc

        results = data.get("results") if isinstance(data, dict) else None
        if isinstance(results, list):
            for result in results:
                if isinstance(result, dict) and result.get("success") is True:
                    archived_count += 1
                else:
                    failed_count += 1
        else:
            archived_count += len(chunk)

    return archived_count, failed_count


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


def slugify(text: str, fallback: str = "bookmark") -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or fallback


def snippet_filename_for_item(item: dict[str, Any]) -> str:
    created_at = parse_iso_datetime(item.get("created_at"))
    timestamp = (created_at or datetime.now()).strftime("%Y-%m-%d-%H-%M")
    item_id = str(item.get("id", "")).strip()
    if item_id:
        identifier = slugify(item_id, "item")
    else:
        title = safe_text(item.get("title"), "bookmark")
        identifier = slugify(title)
    return f"{timestamp}-{identifier}.md"


def snippet_output_path_for_item(item: dict[str, Any]) -> Path:
    created_at = parse_iso_datetime(item.get("created_at"))
    year = (created_at or datetime.now()).strftime("%Y")
    return SNIPPETS_DIR / year / snippet_filename_for_item(item)


def build_front_matter(date_value: str, tag: str) -> str:
    return "\n".join(
        [
            "---",
            'author: "liamjbennett"',
            f'date: "{date_value}"',
            f'tags: ["{tag}"]',
            "ShowToc: false",
            "ShowBreadCrumbs: false",
            'thumbnail: "/img/main/profile.jpg"',
            'mastodon_link: ""',
            'bluesky_link: ""',
            "---",
            "",
        ]
    )


def date_for_item(item: dict[str, Any]) -> str:
    created_at = parse_iso_datetime(item.get("created_at"))
    if created_at:
        return created_at.strftime("%Y-%m-%d")
    return datetime.now().strftime("%Y-%m-%d")


def bookmark_url(item: dict[str, Any]) -> str:
    # Prefer the original/source URL when available; fall back to Reader URL.
    for key in ("source_url", "original_url", "canonical_url", "url"):
        value = safe_text(item.get(key), "")
        if value:
            return value
    return ""


def bookmark_preview_image_url(item: dict[str, Any]) -> str:
    # Readwise often exposes page preview images using one of these fields.
    for key in ("image_url", "cover_image_url", "summary_image_url", "thumbnail_url"):
        value = safe_text(item.get(key), "")
        if value:
            return value
    return ""


def render_snippet_body(item: dict[str, Any]) -> str:
    title = safe_text(item.get("title"), "Untitled")
    url = bookmark_url(item)
    image_url = bookmark_preview_image_url(item)
    author = safe_text(item.get("author"), "")

    lines: list[str] = []
    if image_url:
        if url:
            lines.append(
                f'{{{{< figure src="{image_url}" width="350px" link="{url}" >}}}}'
            )
            lines.extend(["", f"[{title}]({url})"])
        else:
            lines.append(f'{{{{< figure src="{image_url}" width="350px" >}}}}')
    elif url:
        lines.append(f"[{title}]({url})")
    else:
        lines.append(title)

    if author:
        lines.extend(["", f"Author: {author}"])

    return "\n".join(lines).rstrip() + "\n"


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

    created_count = 0
    skipped_count = 0
    created_item_ids: list[str] = []

    for item in items:
        output_path = snippet_output_path_for_item(item)
        if output_path.exists():
            skipped_count += 1
            continue

        output_path.parent.mkdir(parents=True, exist_ok=True)
        content = build_front_matter(date_for_item(item), args.tag) + render_snippet_body(item)
        output_path.write_text(content, encoding="utf-8")
        created_count += 1
        item_id = safe_text(item.get("id"), "")
        if item_id:
            created_item_ids.append(item_id)
        print(f"Created snippet: {output_path}")

    archived_count = 0
    archive_failed_count = 0
    if created_item_ids:
        try:
            archived_count, archive_failed_count = bulk_archive_documents(token, created_item_ids)
        except RuntimeError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1

    print(
        f"Processed {len(items)} item(s): created {created_count}, skipped {skipped_count} existing file(s)."
    )
    if created_item_ids:
        print(
            f"Archived {archived_count} created item(s) in Readwise"
            + (f"; {archive_failed_count} failed." if archive_failed_count else ".")
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
