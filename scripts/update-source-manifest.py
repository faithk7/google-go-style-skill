#!/usr/bin/env python3
"""Check or update the pinned Google Go Style Guide source commit."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPOSITORY = "https://github.com/google/styleguide.git"
BRANCH = "gh-pages"
MANIFEST_PATH = Path(__file__).resolve().parent.parent / "references" / "source-manifest.json"


def current_commit() -> str:
    result = subprocess.run(
        ["git", "ls-remote", REPOSITORY, f"refs/heads/{BRANCH}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or "git ls-remote failed"
        raise RuntimeError(detail)

    line = result.stdout.strip().splitlines()
    if not line:
        raise RuntimeError(f"no {BRANCH} ref returned by {REPOSITORY}")
    return line[0].split()[0]


def load_manifest() -> dict[str, object]:
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"read {MANIFEST_PATH}: {exc}") from exc


def write_manifest(manifest: dict[str, object]) -> None:
    try:
        MANIFEST_PATH.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        raise RuntimeError(f"write {MANIFEST_PATH}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="check the pinned commit without changing files (the default)",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="update the manifest to the current upstream commit",
    )
    args = parser.parse_args()
    if args.check and args.update:
        parser.error("--check and --update cannot be used together")

    try:
        manifest = load_manifest()
        pinned = str(manifest.get("commit", ""))
        current = current_commit()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"pinned:  {pinned}")
    print(f"current: {current}")
    if pinned == current:
        print("source manifest is current")
        return 0

    if args.update:
        manifest["commit"] = current
        write_manifest(manifest)
        print(f"updated {MANIFEST_PATH}")
        return 0

    print("source manifest is stale; review references, then rerun with --update", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
