import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = (
    ROOT / "tools" / "export_thesis.py"
    if (ROOT / "tools" / "export_thesis.py").exists()
    else ROOT / "tools" / "export_thesis.py"
)
if str(EXPORTER.parent) not in sys.path:
    sys.path.insert(0, str(EXPORTER.parent))
SPEC = importlib.util.spec_from_file_location("theory_only_export_tool", EXPORTER)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class TheoryOnlyExportTests(unittest.TestCase):
    def test_final_theory_only_row_is_valid_but_not_exported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            catalog_dir = root / "catalog"
            catalog_dir.mkdir()
            catalog = catalog_dir / "sources.csv"
            selection = catalog_dir / "thesis-selection.csv"

            with catalog.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Κωδικός", "Τίτλος", "Σύνδεσμος"])
                writer.writeheader()
                writer.writerow({"Κωδικός": "SRC-THEORY0001", "Τίτλος": "Seminar transcript", "Σύνδεσμος": ""})

            with selection.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=MODULE.SELECTION_FIELDS)
                writer.writeheader()
                writer.writerow(
                    {
                        "Κωδικός": "SRC-THEORY0001",
                        "Ρόλος": "θεωρητικό υλικό",
                        "Κατάσταση": "ελεγμένο-μη-παραπομπή",
                        "Κεφάλαια": "",
                        "Θέματα": "seminar transcript",
                        "Εξαγωγή": "όχι",
                        "Σημείωση": "Useful for synthesis; primary papers preferred for citation.",
                    }
                )

            originals = (MODULE.ROOT, MODULE.CATALOG_DIR, MODULE.CATALOG, MODULE.SELECTION)
            try:
                MODULE.ROOT = root
                MODULE.CATALOG_DIR = catalog_dir
                MODULE.CATALOG = catalog
                MODULE.SELECTION = selection
                errors, exported, _, _ = MODULE.validate()
            finally:
                MODULE.ROOT, MODULE.CATALOG_DIR, MODULE.CATALOG, MODULE.SELECTION = originals

            self.assertEqual(errors, [])
            self.assertEqual(exported, [])

    def test_theory_only_role_cannot_be_exported(self):
        self.assertNotIn("θεωρητικό υλικό", MODULE.EXPORTABLE_ROLES)
        self.assertIn("θεωρητικό υλικό", MODULE.ALLOWED_ROLES)


if __name__ == "__main__":
    unittest.main()
