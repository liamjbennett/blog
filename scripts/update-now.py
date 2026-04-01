#!/usr/bin/env python3

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
import re
import sys


WEEKNOTE_DIR = Path("content/weeknotes")
NOW_FILE = Path("content/now.md")
READING_HEADING = "## Reading"
WATCHING_HEADING = "## Watching"
BOOK_PAGES_PATTERN = re.compile(r"^\* \d+ book pages read \((.+?) - p\d+-p\d+\)(?: - Finished)?$")
WEEKNOTE_WATCHING_HEADING = "📺 - This weeks background entertainment:"


def find_latest_weeknote(today: date) -> Path:
    latest_path: Path | None = None
    latest_date: date | None = None

    for path in sorted(WEEKNOTE_DIR.rglob("*.md")):
        try:
            note_date = datetime.strptime(path.name[:10], "%Y-%m-%d").date()
        except ValueError:
            continue

        if note_date > today:
            continue

        if latest_date is None or (note_date, path.name) > (latest_date, latest_path.name):
            latest_date = note_date
            latest_path = path

    if latest_path is None:
        raise RuntimeError(f"No weeknote found on or before {today:%Y-%m-%d}")

    return latest_path


def extract_watching_items(weeknote_path: Path) -> list[str]:
    lines = weeknote_path.read_text().splitlines()
    items: list[str] = []
    in_block = False

    for line in lines:
        stripped = line.strip()

        if stripped == WEEKNOTE_WATCHING_HEADING:
            in_block = True
            continue

        if in_block and stripped == "<!-- vale on -->":
            break

        if in_block and stripped.startswith("* ") and stripped not in {"*", "* "}:
            items.append(line)

    if not items:
        raise RuntimeError(f"No watching items found in {weeknote_path}")

    return items


def extract_reading_items(weeknote_path: Path) -> list[str]:
    lines = weeknote_path.read_text().splitlines()

    for line in lines:
        match = BOOK_PAGES_PATTERN.match(line.strip())
        if match:
            return [f"* {match.group(1)}"]

    raise RuntimeError(f"No reading item found in {weeknote_path}")


def replace_section(now_lines: list[str], heading: str, items: list[str]) -> list[str]:
    section_start: int | None = None
    section_end: int | None = None

    for index, line in enumerate(now_lines):
        stripped = line.strip()

        if section_start is None and stripped == heading:
            section_start = index
            continue

        if section_start is not None and index > section_start and (stripped.startswith("## ") or stripped == "---"):
            section_end = index
            break

    if section_start is None:
        raise RuntimeError(f"Could not find '{heading}' in {NOW_FILE}")

    if section_end is None:
        section_end = len(now_lines)

    return [
        *now_lines[:section_start],
        now_lines[section_start],
        "",
        *items,
        "",
        *now_lines[section_end:],
    ]


def update_last_updated(now_lines: list[str], updated_on: str) -> list[str]:
    for index, line in enumerate(now_lines):
        if line.startswith("Last Updated: "):
            now_lines[index] = f"Last Updated: {updated_on}"
            break

    return now_lines


def main() -> int:
    today = date.today()
    updated_on = today.strftime("%d-%b-%Y")

    latest_weeknote = find_latest_weeknote(today)
    reading_items = extract_reading_items(latest_weeknote)
    watching_items = extract_watching_items(latest_weeknote)

    now_lines = NOW_FILE.read_text().splitlines()
    updated_lines = replace_section(now_lines, READING_HEADING, reading_items)
    updated_lines = replace_section(updated_lines, WATCHING_HEADING, watching_items)
    updated_lines = update_last_updated(updated_lines, updated_on)

    NOW_FILE.write_text("\n".join(updated_lines) + "\n")
    print(f"Updated {NOW_FILE} from {latest_weeknote}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)