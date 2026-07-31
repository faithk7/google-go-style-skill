#!/usr/bin/env python3
"""Check that the Effective Go crosswalk and authority policy stay complete."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / "SKILL.md"
REFERENCE_PATH = ROOT / "references" / "effective-go.md"

SOURCE_SECTIONS = (
    "Introduction",
    "Examples",
    "Formatting",
    "Commentary",
    "Names",
    "Package names",
    "Getters",
    "Interface names",
    "MixedCaps",
    "Semicolons",
    "Control structures",
    "If",
    "Redeclaration and reassignment",
    "For",
    "Switch",
    "Type switch",
    "Functions",
    "Multiple return values",
    "Named result parameters",
    "Defer",
    "Data",
    "Allocation with new",
    "Constructors and composite literals",
    "Allocation with make",
    "Arrays",
    "Slices",
    "Two-dimensional slices",
    "Maps",
    "Printing",
    "Append",
    "Initialization",
    "Constants",
    "Variables",
    "The init function",
    "Methods",
    "Pointers vs. Values",
    "Interfaces and other types",
    "Interfaces",
    "Conversions",
    "Interface conversions and type assertions",
    "Generality",
    "Interfaces and methods",
    "The blank identifier",
    "The blank identifier in multiple assignment",
    "Unused imports and variables",
    "Import for side effect",
    "Interface checks",
    "Embedding",
    "Concurrency",
    "Share by communicating",
    "Goroutines",
    "Channels",
    "Channels of channels",
    "Parallelization",
    "A leaky buffer",
    "Errors",
    "Panic",
    "Recover",
    "A web server",
)

REQUIRED_AUTHORITY_MARKERS = (
    "## Authority and conflicts",
    "current Go specification",
    "current pinned Google Go Style Guide",
    "effective-go.md",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("`", "")).strip().casefold()


def main() -> int:
    skill = SKILL_PATH.read_text(encoding="utf-8")
    reference = REFERENCE_PATH.read_text(encoding="utf-8")
    normalized_reference = normalize(reference)

    missing_sections = [
        section
        for section in SOURCE_SECTIONS
        if normalize(section) not in normalized_reference
    ]
    missing_rules = [
        f"GO-EFFECTIVE-{index:03d}"
        for index in range(1, 20)
        if f"## GO-EFFECTIVE-{index:03d}:" not in reference
    ]
    missing_authority = [
        marker for marker in REQUIRED_AUTHORITY_MARKERS if marker not in skill
    ]

    if missing_sections or missing_rules or missing_authority:
        if missing_sections:
            print("missing Effective Go sections:", file=sys.stderr)
            for section in missing_sections:
                print(f"  - {section}", file=sys.stderr)
        if missing_rules:
            print("missing crosswalk rules:", file=sys.stderr)
            for rule in missing_rules:
                print(f"  - {rule}", file=sys.stderr)
        if missing_authority:
            print("missing authority markers:", file=sys.stderr)
            for marker in missing_authority:
                print(f"  - {marker}", file=sys.stderr)
        return 1

    print(
        f"Effective Go crosswalk covers {len(SOURCE_SECTIONS)} sections "
        "with 19 curated rules"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
