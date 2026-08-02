#!/usr/bin/env python3
"""Validate the skill package without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"[a-z0-9-]{1,64}")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path.name}: missing opening frontmatter delimiter")

    try:
        end = lines.index("---", 1)
    except ValueError as err:
        raise ValueError(f"{path.name}: missing closing frontmatter delimiter") from err

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        key, separator, value = line.partition(":")
        if not separator or not key or not value.strip():
            raise ValueError(f"{path.name}:{line_number}: invalid frontmatter field")
        if key in fields:
            raise ValueError(f"{path.name}:{line_number}: duplicate field {key!r}")
        fields[key] = value.strip().strip('"\'')
    return fields


def validate_frontmatter() -> str:
    fields = parse_frontmatter(ROOT / "SKILL.md")
    if set(fields) != {"name", "description"}:
        raise ValueError("SKILL.md: frontmatter must contain only name and description")
    if not NAME_PATTERN.fullmatch(fields["name"]):
        raise ValueError("SKILL.md: name must use lowercase letters, digits, and hyphens")
    if not fields["description"]:
        raise ValueError("SKILL.md: description must not be empty")
    return fields["name"]


def validate_metadata(skill_name: str) -> None:
    metadata = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if not re.search(r'^\s*display_name:\s*"[^"\n]+"\s*$', metadata, re.MULTILINE):
        raise ValueError("agents/openai.yaml: missing quoted display_name")
    if not re.search(r'^\s*short_description:\s*"[^"\n]{25,64}"\s*$', metadata, re.MULTILINE):
        raise ValueError("agents/openai.yaml: short_description must be 25-64 characters")
    prompt = re.search(r'^\s*default_prompt:\s*"([^"\n]+)"\s*$', metadata, re.MULTILINE)
    if prompt is None or f"${skill_name}" not in prompt.group(1):
        raise ValueError(f"agents/openai.yaml: default_prompt must mention ${skill_name}")


def validate_markdown_links() -> None:
    for markdown_path in [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]:
        text = markdown_path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (markdown_path.parent / target).resolve()
            if not resolved.exists():
                relative_path = markdown_path.relative_to(ROOT)
                raise ValueError(f"{relative_path}: broken local link {raw_target!r}")


def validate_manifest() -> None:
    manifest_path = ROOT / "references" / "source-manifest.json"
    with manifest_path.open(encoding="utf-8") as manifest_file:
        json.load(manifest_file)


def run_script(script_name: str, *arguments: str) -> None:
    command = [sys.executable, str(ROOT / "scripts" / script_name), *arguments]
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-upstream",
        action="store_true",
        help="also compare the pinned Google Go Style sources with upstream",
    )
    args = parser.parse_args()

    try:
        skill_name = validate_frontmatter()
        validate_metadata(skill_name)
        validate_markdown_links()
        validate_manifest()
        run_script("check-effective-go-crosswalk.py")
        if args.check_upstream:
            run_script("update-source-manifest.py", "--check")
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as err:
        print(f"validation failed: {err}", file=sys.stderr)
        return 1

    print("skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
