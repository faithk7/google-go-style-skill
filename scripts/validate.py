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
MAX_SKILL_LINES = 500
NAME_PATTERN = re.compile(r"[a-z0-9-]{1,64}")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKILL_REFERENCE_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(references/([^#)]+\.md)(?:#[^)]+)?\)")
RULE_HEADING_CANDIDATE_PATTERN = re.compile(r"^#{1,6}\s+GO-")
RULE_HEADING_PATTERN = re.compile(r"^## (GO-[A-Z]+(?:-[A-Z]+)*-[0-9]{3}): \S.*$")
SOURCE_DECLARATION_PATTERN = re.compile(r"^(?:Google )?Sources?:\s+\S", re.IGNORECASE)
COMMIT_PATTERN = re.compile(r"[0-9a-f]{40}")
REVIEW_DATE_PATTERN = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


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


def validate_frontmatter(root: Path = ROOT) -> str:
    fields = parse_frontmatter(root / "SKILL.md")
    if set(fields) != {"name", "description"}:
        raise ValueError("SKILL.md: frontmatter must contain only name and description")
    if not NAME_PATTERN.fullmatch(fields["name"]):
        raise ValueError("SKILL.md: name must use lowercase letters, digits, and hyphens")
    if not fields["description"]:
        raise ValueError("SKILL.md: description must not be empty")
    return fields["name"]


def validate_metadata(skill_name: str, root: Path = ROOT) -> None:
    metadata = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if not re.search(r'^\s*display_name:\s*"[^"\n]+"\s*$', metadata, re.MULTILINE):
        raise ValueError("agents/openai.yaml: missing quoted display_name")
    if not re.search(r'^\s*short_description:\s*"[^"\n]{25,64}"\s*$', metadata, re.MULTILINE):
        raise ValueError("agents/openai.yaml: short_description must be 25-64 characters")
    prompt = re.search(r'^\s*default_prompt:\s*"([^"\n]+)"\s*$', metadata, re.MULTILINE)
    if prompt is None or f"${skill_name}" not in prompt.group(1):
        raise ValueError(f"agents/openai.yaml: default_prompt must mention ${skill_name}")


def validate_markdown_links(root: Path = ROOT) -> None:
    for markdown_path in [root / "SKILL.md", *sorted((root / "references").glob("*.md"))]:
        text = markdown_path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (markdown_path.parent / target).resolve()
            if not resolved.exists():
                relative_path = markdown_path.relative_to(root)
                raise ValueError(f"{relative_path}: broken local link {raw_target!r}")


def rule_bearing_references(root: Path = ROOT) -> list[Path]:
    return [
        markdown_path
        for markdown_path in sorted((root / "references").glob("*.md"))
        if any(
            RULE_HEADING_CANDIDATE_PATTERN.match(line)
            for line in markdown_path.read_text(encoding="utf-8").splitlines()
        )
    ]


def validate_rule_headings(root: Path = ROOT) -> None:
    seen: dict[str, tuple[Path, int]] = {}
    for markdown_path in sorted((root / "references").glob("*.md")):
        for line_number, line in enumerate(
            markdown_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if RULE_HEADING_CANDIDATE_PATTERN.match(line) is None:
                continue
            match = RULE_HEADING_PATTERN.fullmatch(line)
            relative_path = markdown_path.relative_to(root)
            if match is None:
                raise ValueError(f"{relative_path}:{line_number}: malformed rule heading")

            rule_id = match.group(1)
            if rule_id in seen:
                first_path, first_line = seen[rule_id]
                raise ValueError(
                    f"{relative_path}:{line_number}: duplicate rule {rule_id}; "
                    f"first defined at {first_path}:{first_line}"
                )
            seen[rule_id] = (relative_path, line_number)

    if not seen:
        raise ValueError("references: no GO rule headings found")


def validate_rule_sources(root: Path = ROOT) -> None:
    for markdown_path in rule_bearing_references(root):
        opening_lines = markdown_path.read_text(encoding="utf-8").splitlines()[:6]
        if not any(SOURCE_DECLARATION_PATTERN.match(line) for line in opening_lines):
            relative_path = markdown_path.relative_to(root)
            raise ValueError(f"{relative_path}: rule-bearing reference must declare sources near the top")


def markdown_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    marker = f"## {heading}"
    try:
        start = lines.index(marker) + 1
    except ValueError as err:
        raise ValueError(f"SKILL.md: missing section {marker!r}") from err

    end = next(
        (line_number for line_number in range(start, len(lines)) if lines[line_number].startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start:end])


def validate_reference_registration(root: Path = ROOT) -> None:
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    reference_map = markdown_section(skill_text, "Reference map")
    focused_requests = markdown_section(skill_text, "Focused requests")

    registered = set(SKILL_REFERENCE_LINK_PATTERN.findall(reference_map))
    focused = set(SKILL_REFERENCE_LINK_PATTERN.findall(focused_requests))
    rule_bearing = {path.name for path in rule_bearing_references(root)}

    missing_topics = sorted(rule_bearing - registered)
    if missing_topics:
        raise ValueError(
            "SKILL.md: rule-bearing references missing from Reference map: "
            + ", ".join(missing_topics)
        )

    unregistered_focused = sorted(focused - registered)
    if unregistered_focused:
        raise ValueError(
            "SKILL.md: focused references missing from Reference map: "
            + ", ".join(unregistered_focused)
        )


def validate_skill_size(root: Path = ROOT) -> None:
    line_count = len((root / "SKILL.md").read_text(encoding="utf-8").splitlines())
    if line_count > MAX_SKILL_LINES:
        raise ValueError(f"SKILL.md: {line_count} lines exceeds the {MAX_SKILL_LINES}-line limit")


def validate_source_entries(manifest_path: Path, field: str, entries: object) -> None:
    if not isinstance(entries, list) or not entries:
        raise ValueError(f"{manifest_path.name}: {field} must be a non-empty list")

    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"{manifest_path.name}: {field}[{index}] must be an object")
        for required_field in ("name", "url", "reviewed"):
            value = entry.get(required_field)
            if not isinstance(value, str) or not value:
                raise ValueError(
                    f"{manifest_path.name}: {field}[{index}].{required_field} "
                    "must be a non-empty string"
                )
        if not REVIEW_DATE_PATTERN.fullmatch(entry["reviewed"]):
            raise ValueError(
                f"{manifest_path.name}: {field}[{index}].reviewed must use YYYY-MM-DD"
            )


def validate_manifest(root: Path = ROOT) -> None:
    manifest_path = root / "references" / "source-manifest.json"
    with manifest_path.open(encoding="utf-8") as manifest_file:
        manifest = json.load(manifest_file)

    required_fields = {
        "repository",
        "branch",
        "commit",
        "documents",
        "tooling_documents",
        "supplementary_documents",
    }
    missing_fields = sorted(required_fields - set(manifest))
    if missing_fields:
        raise ValueError(f"{manifest_path.name}: missing fields: {', '.join(missing_fields)}")
    if not isinstance(manifest["repository"], str) or not manifest["repository"]:
        raise ValueError(f"{manifest_path.name}: repository must be a non-empty string")
    if not isinstance(manifest["branch"], str) or not manifest["branch"]:
        raise ValueError(f"{manifest_path.name}: branch must be a non-empty string")
    if not isinstance(manifest["commit"], str) or not COMMIT_PATTERN.fullmatch(manifest["commit"]):
        raise ValueError(f"{manifest_path.name}: commit must be a full 40-character lowercase SHA")
    if not isinstance(manifest["documents"], list) or not manifest["documents"] or not all(
        isinstance(document, str) and document for document in manifest["documents"]
    ):
        raise ValueError(f"{manifest_path.name}: documents must be a non-empty list of paths")
    validate_source_entries(manifest_path, "tooling_documents", manifest["tooling_documents"])
    validate_source_entries(
        manifest_path,
        "supplementary_documents",
        manifest["supplementary_documents"],
    )


def run_script(script_name: str, *arguments: str, root: Path = ROOT) -> None:
    command = [sys.executable, str(root / "scripts" / script_name), *arguments]
    subprocess.run(command, cwd=root, check=True)


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
        validate_skill_size()
        validate_markdown_links()
        validate_rule_headings()
        validate_rule_sources()
        validate_reference_registration()
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
