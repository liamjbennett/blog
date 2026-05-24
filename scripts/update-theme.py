#!/usr/bin/env python3
"""Update the hugo-PaperMod theme submodule."""

from pathlib import Path
import shutil
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
THEME_PATH = REPO_ROOT / "themes" / "hugo-PaperMod"
THEME_PATH_REL = "themes/hugo-PaperMod"
THEMES_DIR = REPO_ROOT / "themes"
THEME_URL = "https://github.com/adityatelange/hugo-PaperMod"


def run(args, **kwargs):
    result = subprocess.run(args, **kwargs)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    if THEME_PATH.is_dir():
        run(["git", "submodule", "deinit", "-f", THEME_PATH_REL], cwd=REPO_ROOT)
        run(["git", "rm", "-f", THEME_PATH_REL], cwd=REPO_ROOT)
        shutil.rmtree(THEME_PATH, ignore_errors=True)
        shutil.rmtree(REPO_ROOT / ".git" / "modules" / THEME_PATH_REL, ignore_errors=True)

    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    run(["git", "submodule", "add", "--force", THEME_URL, THEME_PATH_REL], cwd=REPO_ROOT)


if __name__ == "__main__":
    main()
