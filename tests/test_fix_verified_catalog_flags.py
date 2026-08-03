from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from tools import fix_verified_catalog_flags as fix


class VerifiedCatalogFlagTests(unittest.TestCase):
    def make_repo(self, *, verified: bool = True) -> Path:
        root = Path(tempfile.mkdtemp())
        (root / "catalog").mkdir()
        (root / "analyses").mkdir()
        (root / "evidence").mkdir()

        catalog_fields = [
            "Κωδικός",
            "Τίτλος",
            "Συγγραφείς",
            "Έτος",
            "Σύνδεσμος",
            "Τύπος",
            "Θέματα",
            "Κατάσταση",
            "Επιβεβαίωση",
            "Προτεραιότητα",
            "Σημειώσεις",
        ]
        with (root / "catalog" / "sources.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=catalog_fields, lineterminator="\n")
            writer.writeheader()
            for source_id in sorted(fix.TARGETS):
                writer.writerow(
                    {
                        "Κωδικός": source_id,
                        "Τίτλος": source_id,
                        "Προτεραιότητα": fix.STALE_PRIORITY,
                        "Σημειώσεις": fix.STALE_NOTE,
                    }
                )

        with (root / "catalog" / "thesis-selection.csv").open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["Κωδικός", "Κατάσταση", "Εξαγωγή"],
                lineterminator="\n",
            )
            writer.writeheader()
            for source_id in sorted(fix.TARGETS):
                writer.writerow(
                    {"Κωδικός": source_id, "Κατάσταση": "επαληθευμένη", "Εξαγωγή": "ναι"}
                )

        for source_id in fix.TARGETS:
            analysis_status = "επαληθευμένη" if verified else "πρόχειρη"
            (root / "analyses" / f"{source_id}.md").write_text(
                "---\n"
                f"κατάσταση: {analysis_status}\n"
                "ελεγχθέν-πρωτότυπο: ναι\n"
                'ημερομηνία-ελέγχου: "2026-08-03"\n'
                "---\n",
                encoding="utf-8",
            )
            (root / "evidence" / f"{source_id}.md").write_text(
                "---\n"
                "κατάσταση: επαληθευμένο\n"
                "ελεγχθέν-πρωτότυπο: ναι\n"
                'ημερομηνία-ελέγχου: "2026-08-03"\n'
                "---\n",
                encoding="utf-8",
            )
        return root

    def test_check_detects_stale_flags(self) -> None:
        root = self.make_repo()
        errors = fix.normalize(root=root, apply=False)
        self.assertEqual(errors, ["6 stale verified catalog fields require normalization"])

    def test_apply_normalizes_only_verified_targets(self) -> None:
        root = self.make_repo()
        self.assertEqual(fix.normalize(root=root, apply=True), [])
        self.assertEqual(fix.normalize(root=root, apply=False), [])

        with (root / "catalog" / "sources.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual({row["Προτεραιότητα"] for row in rows}, {fix.READY_PRIORITY})
        self.assertTrue(all(fix.READY_NOTE in row["Σημειώσεις"] for row in rows))
        self.assertTrue(all("προς ανθρώπινο έλεγχο" not in row["Σημειώσεις"] for row in rows))

    def test_apply_refuses_unverified_analysis(self) -> None:
        root = self.make_repo(verified=False)
        errors = fix.normalize(root=root, apply=True)
        self.assertEqual(len(errors), len(fix.TARGETS))
        self.assertTrue(all("verified analysis" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
