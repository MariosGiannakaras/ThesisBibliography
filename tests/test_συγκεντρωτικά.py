from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "εργαλεία" / "συγκεντρωτικά.py"
SPEC = importlib.util.spec_from_file_location("consolidated_views", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ConsolidatedViewsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "κατάλογος").mkdir()
        (self.root / "πηγές").mkdir()
        (self.root / "αποσπάσματα").mkdir()

        rows = [
            {
                "Κωδικός": "SRC-AAAAAAAAAA",
                "Τίτλος": "Verified source",
                "Συγγραφείς": "Ada Author",
                "Έτος": "2024",
                "Σύνδεσμος": "https://example.org/verified",
                "Τύπος": "ακαδημαϊκή εργασία",
                "Θέματα": "GridWorld; ανθεκτικότητα",
                "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
                "Επιβεβαίωση": "επιβεβαιωμένη",
                "Προτεραιότητα": "υψηλή",
                "Σημειώσεις": "Χρήσιμη | βασική",
            },
            {
                "Κωδικός": "SRC-BBBBBBBBBB",
                "Τίτλος": "Draft source",
                "Συγγραφείς": "Beta Author",
                "Έτος": "2023",
                "Σύνδεσμος": "https://example.org/draft",
                "Τύπος": "τεχνική αναφορά",
                "Θέματα": "μετρικές",
                "Κατάσταση": "μόνο μεταδεδομένα",
                "Επιβεβαίωση": "εκκρεμεί",
                "Προτεραιότητα": "μεσαία",
                "Σημειώσεις": "",
            },
        ]
        with (self.root / "κατάλογος" / "πηγές.csv").open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=MODULE.REQUIRED_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)

        for code in ("SRC-AAAAAAAAAA", "SRC-BBBBBBBBBB"):
            (self.root / "πηγές" / f"{code}.md").write_text(
                f"# {code}\n\nFull source text.\n", encoding="utf-8"
            )

        (self.root / "αποσπάσματα" / "SRC-AAAAAAAAAA.md").write_text(
            """---
κωδικός: SRC-AAAAAAAAAA
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Verified source

## Τεκμήριο E1

- **Ισχυρισμός:** Verified evidence.
""",
            encoding="utf-8",
        )
        (self.root / "αποσπάσματα" / "SRC-BBBBBBBBBB.md").write_text(
            """---
κωδικός: SRC-BBBBBBBBBB
κατάσταση: πρόχειρο
ελεγχθέν-πρωτότυπο: όχι
---

# Draft evidence

This must not be exported.
""",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_generates_complete_archive_and_verified_excerpt_view(self) -> None:
        outputs = MODULE.generate_outputs(self.root)
        archive = outputs[self.root / MODULE.ARCHIVE_FILENAME]
        excerpts = outputs[self.root / MODULE.EXCERPTS_FILENAME]

        self.assertIn("Συνολικές ενεργές πηγές:** 2", archive)
        self.assertIn("SRC-AAAAAAAAAA", archive)
        self.assertIn("SRC-BBBBBBBBBB", archive)
        self.assertIn("GridWorld", archive)
        self.assertIn("Χρήσιμη \\| βασική", archive)

        self.assertIn("SRC-AAAAAAAAAA", excerpts)
        self.assertIn("Verified evidence", excerpts)
        self.assertNotIn("SRC-BBBBBBBBBB", excerpts)
        self.assertNotIn("This must not be exported", excerpts)

    def test_write_and_check_are_deterministic(self) -> None:
        outputs = MODULE.generate_outputs(self.root)
        MODULE.write_outputs(outputs)
        self.assertTrue(MODULE.check_outputs(MODULE.generate_outputs(self.root)))

        archive_path = self.root / MODULE.ARCHIVE_FILENAME
        archive_path.write_text("stale", encoding="utf-8")
        self.assertFalse(MODULE.check_outputs(MODULE.generate_outputs(self.root)))

    def test_rejects_excerpt_code_mismatch(self) -> None:
        path = self.root / "αποσπάσματα" / "SRC-AAAAAAAAAA.md"
        text = path.read_text(encoding="utf-8").replace(
            "κωδικός: SRC-AAAAAAAAAA", "κωδικός: SRC-CCCCCCCCCC"
        )
        path.write_text(text, encoding="utf-8")

        with self.assertRaises(ValueError):
            MODULE.generate_outputs(self.root)


if __name__ == "__main__":
    unittest.main()
