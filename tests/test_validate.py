from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATE_PATH = REPO_ROOT / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("skill_validate", VALIDATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {VALIDATE_PATH}")
validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate)


class ValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name) / "skill"
        shutil.copytree(
            REPO_ROOT,
            self.root,
            ignore=shutil.ignore_patterns(".git", ".github", "__pycache__"),
        )

    def test_current_package_passes_structural_checks(self) -> None:
        validate.validate_skill_size(self.root)
        validate.validate_rule_headings(self.root)
        validate.validate_rule_sources(self.root)
        validate.validate_reference_registration(self.root)
        validate.validate_manifest(self.root)

    def test_rule_bearing_reference_requires_source_declaration(self) -> None:
        reference = self.root / "references" / "generated-code-and-contracts.md"
        text = reference.read_text(encoding="utf-8")
        reference.write_text(text.replace("Sources:", "Provenance:", 1), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "must declare sources"):
            validate.validate_rule_sources(self.root)

    def test_rule_bearing_reference_must_be_registered(self) -> None:
        skill_path = self.root / "SKILL.md"
        lines = skill_path.read_text(encoding="utf-8").splitlines()
        lines = [
            line
            for line in lines
            if not line.startswith("- [`generated-code-and-contracts.md`](references/")
        ]
        skill_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "missing from Reference map"):
            validate.validate_reference_registration(self.root)

    def test_reference_registration_uses_markdown_headings(self) -> None:
        skill_path = self.root / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        text = text.replace("Treat focus as a boundary", "Keep the selected focus as a boundary")
        skill_path.write_text(text, encoding="utf-8")

        validate.validate_reference_registration(self.root)

    def test_manifest_requires_full_commit_sha(self) -> None:
        manifest_path = self.root / "references" / "source-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["commit"] = "1809c76"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "full 40-character lowercase SHA"):
            validate.validate_manifest(self.root)

    def test_manifest_source_entries_require_provenance_fields(self) -> None:
        manifest_path = self.root / "references" / "source-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["tooling_documents"] = [{"name": "Go command documentation"}]
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, r"tooling_documents\[0\]\.url"):
            validate.validate_manifest(self.root)

    def test_duplicate_rule_id_is_rejected(self) -> None:
        reference = self.root / "references" / "generated-code-and-contracts.md"
        with reference.open("a", encoding="utf-8") as reference_file:
            reference_file.write("\n## GO-GEN-001: Duplicate rule\n")

        with self.assertRaisesRegex(ValueError, "duplicate rule GO-GEN-001"):
            validate.validate_rule_headings(self.root)

    def test_skill_body_has_line_limit(self) -> None:
        skill_path = self.root / "SKILL.md"
        with skill_path.open("a", encoding="utf-8") as skill_file:
            skill_file.write("\n".join(["padding"] * validate.MAX_SKILL_LINES) + "\n")

        with self.assertRaisesRegex(ValueError, "exceeds the 500-line limit"):
            validate.validate_skill_size(self.root)


if __name__ == "__main__":
    unittest.main()
