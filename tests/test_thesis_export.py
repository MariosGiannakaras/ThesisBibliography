import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "thesis_export_tool", ROOT / "εργαλεία" / "εξαγωγή-διπλωματικής.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class ThesisExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.originals = {
            "ROOT": MODULE.ROOT,
            "CATALOG": MODULE.CATALOG,
            "SELECTION": MODULE.SELECTION,
            "ANALYSES": MODULE.ANALYSES,
            "EXCERPTS": MODULE.EXCERPTS,
            "DEFAULT_OUTPUT": MODULE.DEFAULT_OUTPUT,
        }
        MODULE.ROOT = root
        MODULE.CATALOG = root / "κατάλογος" / "πηγές.csv"
        MODULE.SELECTION = root / "κατάλογος" / "επιλογή-διπλωματικής.csv"
        MODULE.ANALYSES = root / "αναλύσεις"
        MODULE.EXCERPTS = root / "αποσπάσματα"
        MODULE.DEFAULT_OUTPUT = root / "πακέτο-διπλωματικής"
        MODULE.CATALOG.parent.mkdir(parents=True)
        MODULE.ANALYSES.mkdir()
        MODULE.EXCERPTS.mkdir()
        self.write_catalog()

    def tearDown(self):
        for name, value in self.originals.items():
            setattr(MODULE, name, value)
        self.temp.cleanup()

    def write_catalog(self):
        with MODULE.CATALOG.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["Κωδικός", "Τίτλος", "Σύνδεσμος"],
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerow(
                {
                    "Κωδικός": "SRC-TEST000001",
                    "Τίτλος": "Verified test source",
                    "Σύνδεσμος": "https://example.com/source",
                }
            )

    def write_selection(self, status="επαληθευμένη", export="ναι"):
        with MODULE.SELECTION.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=MODULE.SELECTION_FIELDS,
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerow(
                {
                    "Κωδικός": "SRC-TEST000001",
                    "Ρόλος": "κύρια",
                    "Κατάσταση": status,
                    "Κεφάλαια": "2; 4",
                    "Θέματα": "robustness",
                    "Εξαγωγή": export,
                    "Σημείωση": "",
                }
            )

    def write_verified_files(self):
        headings = "\n\n".join(MODULE.REQUIRED_ANALYSIS_HEADINGS)
        (MODULE.ANALYSES / "SRC-TEST000001.md").write_text(
            "---\nκατάσταση: επαληθευμένη\n---\n\n" + headings + "\n",
            encoding="utf-8",
        )
        (MODULE.EXCERPTS / "SRC-TEST000001.md").write_text(
            "---\nκατάσταση: επαληθευμένο\n---\n\n"
            "- **Θέση:** σελίδα 4\n"
            "- **Ισχυρισμός:** Το εύρημα υποστηρίζει τον δοκιμαστικό ισχυρισμό.\n",
            encoding="utf-8",
        )

    def test_empty_selection_is_valid(self):
        with MODULE.SELECTION.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=MODULE.SELECTION_FIELDS)
            writer.writeheader()
        errors, exported, _, _ = MODULE.validate()
        self.assertEqual(errors, [])
        self.assertEqual(exported, [])

    def test_unverified_source_cannot_be_exported(self):
        self.write_selection(status="πρόχειρη", export="ναι")
        errors, _, _, _ = MODULE.validate()
        self.assertTrue(any("μόνο με κατάσταση" in error for error in errors))

    def test_verified_source_builds_package(self):
        self.write_selection()
        self.write_verified_files()
        errors, exported, catalog, fields = MODULE.validate()
        self.assertEqual(errors, [])
        output = MODULE.ROOT / "output"
        MODULE.write_package(output, exported, catalog, fields)
        self.assertTrue((output / "manifest.csv").exists())
        self.assertTrue((output / "αναλύσεις" / "SRC-TEST000001.md").exists())
        self.assertTrue((output / "αποσπάσματα" / "SRC-TEST000001.md").exists())


if __name__ == "__main__":
    unittest.main()
