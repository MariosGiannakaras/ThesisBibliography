import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "package_integrity.py"
SPEC = importlib.util.spec_from_file_location("package_integrity_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class PackageIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.package = Path(self.temp.name) / "thesis-package"
        (self.package / "catalog").mkdir(parents=True)
        (self.package / "analyses").mkdir()
        (self.package / "evidence").mkdir()
        (self.package / "README.md").write_text("verified package\n", encoding="utf-8")
        (self.package / "SOURCE_COMMIT").write_text("a" * 40 + "\n", encoding="utf-8")
        with (self.package / "manifest.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["Κωδικός"], lineterminator="\n")
            writer.writeheader()
            writer.writerow({"Κωδικός": "SRC-AAAAAAAAAA"})
        (self.package / "catalog" / "sources.csv").write_text("Κωδικός\nSRC-AAAAAAAAAA\n", encoding="utf-8")
        (self.package / "analyses" / "SRC-AAAAAAAAAA.md").write_text("analysis\n", encoding="utf-8")
        (self.package / "evidence" / "SRC-AAAAAAAAAA.md").write_text("evidence\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_write_and_validate_integrity(self):
        MODULE.write_integrity(self.package)
        self.assertEqual(MODULE.validate_integrity(self.package), [])
        metadata = json.loads(
            (self.package / MODULE.METADATA_REL).read_text(encoding="utf-8")
        )
        self.assertEqual(metadata["schema_version"], 1)
        self.assertEqual(metadata["source_commit"], "a" * 40)
        self.assertEqual(metadata["selected_sources"], 1)
        self.assertGreater(metadata["file_count"], 0)

    def test_tampered_file_is_rejected(self):
        MODULE.write_integrity(self.package)
        (self.package / "evidence" / "SRC-AAAAAAAAAA.md").write_text("tampered\n", encoding="utf-8")
        errors = MODULE.validate_integrity(self.package)
        self.assertTrue(any("checksum mismatch" in error for error in errors))

    def test_new_unhashed_file_is_rejected(self):
        MODULE.write_integrity(self.package)
        (self.package / "analyses" / "SRC-BBBBBBBBBB.md").write_text("unexpected\n", encoding="utf-8")
        errors = MODULE.validate_integrity(self.package)
        self.assertTrue(any("checksums missing package files" in error for error in errors))

    def test_missing_hashed_file_is_rejected(self):
        MODULE.write_integrity(self.package)
        (self.package / "analyses" / "SRC-AAAAAAAAAA.md").unlink()
        errors = MODULE.validate_integrity(self.package)
        self.assertTrue(any("checksums reference missing package files" in error for error in errors))

    def test_metadata_source_commit_must_match(self):
        MODULE.write_integrity(self.package)
        metadata_path = self.package / MODULE.METADATA_REL
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["source_commit"] = "b" * 40
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        errors = MODULE.validate_integrity(self.package)
        self.assertTrue(any("source_commit differs" in error for error in errors))

    def test_integrity_files_are_not_self_hashed(self):
        MODULE.write_integrity(self.package)
        sums = (self.package / MODULE.CHECKSUMS_REL).read_text(encoding="utf-8")
        self.assertNotIn(MODULE.METADATA_REL.as_posix(), sums)
        self.assertNotIn(MODULE.CHECKSUMS_REL.as_posix(), sums)


if __name__ == "__main__":
    unittest.main()
