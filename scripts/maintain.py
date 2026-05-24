#!/usr/bin/env python3
"""Run all blog maintenance update scripts."""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent

UPDATE_SCRIPTS = [
    "update-now.py",
    "update-pocketcasts.py",
    "update-podroll.py",
    "update-theme.py",
]


def main():
    failed = []
    for script in UPDATE_SCRIPTS:
        path = SCRIPTS_DIR / script
        print(f"Running {script}...")
        result = subprocess.run([sys.executable, str(path)])
        if result.returncode != 0:
            print(f"  FAILED (exit code {result.returncode})")
            failed.append(script)
        else:
            print(f"  OK")

    if failed:
        print(f"\n{len(failed)} script(s) failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
