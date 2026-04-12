#!/usr/bin/env python3
"""Update the hugo-PaperMod theme submodule."""

import os
import shutil
import subprocess
import sys

THEME_PATH = "themes/hugo-PaperMod"
THEME_URL = "https://github.com/adityatelange/hugo-PaperMod"


def run(args, **kwargs):
    result = subprocess.run(args, **kwargs)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    if os.path.isdir(THEME_PATH):
        run(["git", "submodule", "deinit", "-f", THEME_PATH])
        run(["git", "rm", "-f", THEME_PATH])
        shutil.rmtree(THEME_PATH, ignore_errors=True)
        shutil.rmtree(f".git/modules/{THEME_PATH}", ignore_errors=True)
    else:
        run(["git", "submodule", "add", "--force", THEME_URL], cwd="themes")


if __name__ == "__main__":
    main()
