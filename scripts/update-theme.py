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


def run(args, check=True, **kwargs):
    result = subprocess.run(args, **kwargs)
    if check and result.returncode != 0:
        sys.exit(result.returncode)
    return result


def is_git_tracked(path_rel):
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", path_rel],
        cwd=REPO_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def main():
    if THEME_PATH.is_dir() or is_git_tracked(THEME_PATH_REL):
        run(["git", "submodule", "deinit", "-f", THEME_PATH_REL], cwd=REPO_ROOT, check=False)
        if is_git_tracked(THEME_PATH_REL):
            run(["git", "rm", "-f", THEME_PATH_REL], cwd=REPO_ROOT)
        shutil.rmtree(THEME_PATH, ignore_errors=True)
        shutil.rmtree(REPO_ROOT / ".git" / "modules" / THEME_PATH_REL, ignore_errors=True)

    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    run(["git", "submodule", "add", "--force", THEME_URL, THEME_PATH_REL], cwd=REPO_ROOT)


if __name__ == "__main__":
    main()
