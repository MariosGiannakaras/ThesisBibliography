from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CatalogIntegrityTests(unittest.TestCase):
    def test_validation_script_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_bibliography_repository.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_catalog_has_unique_source_ids(self) -> None:
        payload = json.loads((ROOT / "catalog" / "source-catalog.json").read_text(encoding="utf-8"))
        ids = [record["source_id"] for record in payload["sources"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_notebooklm_reports_are_separate_from_sources(self) -> None:
        reports = list((ROOT / "sources" / "group-reports").glob("*"))
        self.assertGreaterEqual(len(reports), 4)
        raw_names = {path.name for path in (ROOT / "sources" / "raw-md").glob("*.md")}
        self.assertFalse(any("notebooklm" in name for name in raw_names))


if __name__ == "__main__":
    unittest.main()
