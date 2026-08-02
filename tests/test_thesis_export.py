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
SPEC = importlib.util.spec_from_file_location("thesis_export_tool", EXPORTER)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class ThesisExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.originals = {
            "ROOT": MODULE.ROOT,
            "CATALOG_DIR": MODULE.CATALOG_DIR,
            "CATALOG": MODULE.CATALOG,
            "SELECTION": MODULE.SELECTION,
            "SOURCES": MODULE.SOURCES,
            "ANALYSES": MODULE.ANALYSES,
            "EXCERPTS": MODULE.EXCERPTS,
            "DEFAULT_OUTPUT": MODULE.DEFAULT_OUTPUT,
        }
        MODULE.ROOT = root
        MODULE.CATALOG_DIR = root / "catalog"
        MODULE.CATALOG = root / "catalog" / "sources.csv"
        MODULE.SELECTION = root / "catalog" / "thesis-selection.csv"
        MODULE.SOURCES = root / "sources"
        MODULE.ANALYSES = root / "analyses"
        MODULE.EXCERPTS = root / "evidence"
        MODULE.DEFAULT_OUTPUT = root / "thesis-package"
        MODULE.CATALOG_DIR.mkdir(parents=True)
        MODULE.SOURCES.mkdir()
        MODULE.ANALYSES.mkdir()
        MODULE.EXCERPTS.mkdir()
        self.write_catalog()
        self.write_source_english()

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

    def write_source_english(self):
        payload = (
            "This original source discusses reinforcement learning under environmental uncertainty, "
            "evaluation methodology, adaptation after distribution shift, robust decision making, "
            "limitations, experimental controls, and reproducible evidence from the reported study. " * 6
        )
        (MODULE.SOURCES / "SRC-TEST000001.md").write_text(payload, encoding="utf-8")

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

    def write_analysis(self, checked="ναι"):
        analysis_payload = (
            "The study defines its research question, assumptions, experimental environment, algorithms, "
            "baselines, evaluation metrics, quantitative findings, limitations, validity threats, and the exact "
            "way each result may support a narrowly scoped claim about robust agents under uncertainty. " * 12
        )
        (MODULE.ANALYSES / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένη\n"
            f"ελεγχθέν-πρωτότυπο: {checked}\n"
            "---\n\n"
            "## Bibliographic identity\n\n"
            "Test Author (2026). Verified test source.\n\n"
            "## Limitations\n\n"
            "The result is limited to the stated environment and protocol.\n\n"
            "## Thesis use\n\n"
            "Use only for the explicitly supported methodological claim.\n\n"
            + analysis_payload,
            encoding="utf-8",
        )

    def write_evidence_english(self, checked="ναι"):
        excerpt_payload = (
            "The verified evidence is interpreted in its original context and linked to a narrowly stated claim. "
            "The surrounding assumptions, scope conditions, measurement procedure, and limitations are recorded "
            "so the thesis cannot overgeneralize the reported result. " * 10
        )
        (MODULE.EXCERPTS / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένο\n"
            f"ελεγχθέν-πρωτότυπο: {checked}\n"
            "source-language: en\n"
            "---\n\n"
            "# Evidence — Verified test source\n\n"
            "## E1 — Controlled result\n\n"
            "- **Type:** faithful paraphrase\n"
            "- **Location:** page 4, Section 2.1, Table 1\n"
            "- **Claim:** The result supports only the stated experimental claim.\n"
            "- **Status:** verified\n\n"
            "### Faithful paraphrase\n\n"
            + excerpt_payload,
            encoding="utf-8",
        )

    def write_evidence_greek_mismatch(self):
        excerpt_payload = (
            "Το επαληθευμένο τεκμήριο ερμηνεύεται μέσα στα αρχικά συμφραζόμενα και συνδέεται μόνο με έναν "
            "στενά διατυπωμένο ισχυρισμό. Οι παραδοχές, οι συνθήκες εφαρμογής, η διαδικασία μέτρησης και οι "
            "περιορισμοί καταγράφονται ώστε η διπλωματική να μην υπεργενικεύει το αναφερόμενο αποτέλεσμα. " * 10
        )
        (MODULE.EXCERPTS / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένο\n"
            "ελεγχθέν-πρωτότυπο: ναι\n"
            "---\n\n"
            "## Τεκμήριο E1\n\n"
            "- **Θέση:** σελίδα 4, ενότητα 2.1, πίνακας 1\n"
            "- **Ισχυρισμός:** Το αποτέλεσμα υποστηρίζει μόνο τον συγκεκριμένο πειραματικό ισχυρισμό.\n\n"
            + excerpt_payload,
            encoding="utf-8",
        )

    def write_template_only_files(self):
        self.write_analysis()
        (MODULE.EXCERPTS / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένο\n"
            "ελεγχθέν-πρωτότυπο: ναι\n"
            "---\n\n"
            "## Τεκμήριο E1\n\n"
            "- **Θέση:** σελίδα, ενότητα, πίνακας, σχήμα ή χρονική σήμανση\n"
            "- **Ισχυρισμός:** ποια ακριβώς πρόταση της διπλωματικής υποστηρίζει\n",
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

    def test_template_only_files_cannot_be_exported(self):
        self.write_selection()
        self.write_template_only_files()
        errors, _, _, _ = MODULE.validate()
        self.assertTrue(any("αρκετό ουσιαστικό περιεχόμενο" in error for error in errors))
        self.assertTrue(any("πραγματική ακριβής θέση" in error for error in errors))
        self.assertTrue(any("πραγματικός ισχυρισμός" in error for error in errors))

    def test_unchecked_original_cannot_be_exported(self):
        self.write_selection()
        self.write_analysis(checked="όχι")
        self.write_evidence_english(checked="όχι")
        errors, _, _, _ = MODULE.validate()
        self.assertTrue(any("ελέγχθηκε το πρωτότυπο" in error for error in errors))

    def test_english_structured_source_language_evidence_is_accepted(self):
        self.write_selection()
        self.write_analysis()
        self.write_evidence_english()
        errors, exported, _, _ = MODULE.validate()
        self.assertEqual(errors, [])
        self.assertEqual(len(exported), 1)

    def test_cross_language_evidence_is_rejected(self):
        self.write_selection()
        self.write_analysis()
        self.write_evidence_greek_mismatch()
        errors, _, _, _ = MODULE.validate()
        self.assertTrue(any("δεν διατηρεί τη γλώσσα της πηγής" in error for error in errors))

    def test_verified_source_builds_english_path_package(self):
        self.write_selection()
        self.write_analysis()
        self.write_evidence_english()
        errors, exported, catalog, fields = MODULE.validate()
        self.assertEqual(errors, [])
        output = MODULE.ROOT / "output"
        MODULE.write_package(output, exported, catalog, fields)
        self.assertTrue((output / "manifest.csv").exists())
        self.assertTrue((output / "analyses" / "SRC-TEST000001.md").exists())
        self.assertTrue((output / "evidence" / "SRC-TEST000001.md").exists())
        self.assertTrue((output / "catalog" / "sources.csv").exists())


if __name__ == "__main__":
    unittest.main()
