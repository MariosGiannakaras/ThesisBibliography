import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import export_thesis
import validate_thesis_package


class CommittedThesisPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.originals = {
            "ROOT": export_thesis.ROOT,
            "CATALOG_DIR": export_thesis.CATALOG_DIR,
            "CATALOG": export_thesis.CATALOG,
            "SELECTION": export_thesis.SELECTION,
            "SOURCES": export_thesis.SOURCES,
            "ANALYSES": export_thesis.ANALYSES,
            "EXCERPTS": export_thesis.EXCERPTS,
            "DEFAULT_OUTPUT": export_thesis.DEFAULT_OUTPUT,
            "repository_commit": export_thesis.repository_commit,
        }
        export_thesis.ROOT = root
        export_thesis.CATALOG_DIR = root / "catalog"
        export_thesis.CATALOG = root / "catalog" / "sources.csv"
        export_thesis.SELECTION = root / "catalog" / "thesis-selection.csv"
        export_thesis.SOURCES = root / "sources"
        export_thesis.ANALYSES = root / "analyses"
        export_thesis.EXCERPTS = root / "evidence"
        export_thesis.DEFAULT_OUTPUT = root / "thesis-package"
        export_thesis.repository_commit = lambda: "a" * 40

        export_thesis.CATALOG_DIR.mkdir(parents=True)
        export_thesis.SOURCES.mkdir()
        export_thesis.ANALYSES.mkdir()
        export_thesis.EXCERPTS.mkdir()
        self.write_catalog()
        self.write_selection()
        self.write_source()
        self.write_analysis()
        self.write_evidence()
        self.build_package()

    def tearDown(self):
        for name, value in self.originals.items():
            setattr(export_thesis, name, value)
        self.temp.cleanup()

    def write_catalog(self):
        with export_thesis.CATALOG.open("w", encoding="utf-8", newline="") as handle:
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

    def write_selection(self):
        with export_thesis.SELECTION.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=export_thesis.SELECTION_FIELDS,
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerow(
                {
                    "Κωδικός": "SRC-TEST000001",
                    "Ρόλος": "κύρια",
                    "Κατάσταση": "επαληθευμένη",
                    "Κεφάλαια": "2; 4",
                    "Θέματα": "robustness",
                    "Εξαγωγή": "ναι",
                    "Σημείωση": "",
                }
            )

    def write_source(self):
        payload = (
            "This source reports reinforcement learning experiments under environmental uncertainty, "
            "including evaluation methodology, adaptation after distribution shift, robust decision making, "
            "experimental controls, limitations, and reproducible evidence from the reported study. " * 8
        )
        (export_thesis.SOURCES / "SRC-TEST000001.md").write_text(payload, encoding="utf-8")

    def write_analysis(self):
        payload = (
            "The study defines its research question, assumptions, environment, algorithms, baselines, metrics, "
            "quantitative findings, limitations, validity threats, and the exact narrow way each result may support "
            "a claim about robust agents under uncertainty. " * 14
        )
        (export_thesis.ANALYSES / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένη\n"
            "ελεγχθέν-πρωτότυπο: ναι\n"
            "---\n\n"
            "## Bibliographic identity\n\nTest Author (2026). Verified test source.\n\n"
            "## Limitations\n\nThe result is limited to the stated environment and protocol.\n\n"
            "## Thesis use\n\nUse only for the explicitly supported methodological claim.\n\n"
            + payload,
            encoding="utf-8",
        )

    def write_evidence(self):
        payload = (
            "The verified evidence is interpreted in its original context and linked to a narrowly stated claim. "
            "The assumptions, scope conditions, measurement procedure, and limitations are recorded so the thesis "
            "cannot overgeneralize the reported result. " * 12
        )
        (export_thesis.EXCERPTS / "SRC-TEST000001.md").write_text(
            "---\n"
            "κατάσταση: επαληθευμένο\n"
            "ελεγχθέν-πρωτότυπο: ναι\n"
            "source-language: en\n"
            "---\n\n"
            "## E1 — Controlled result\n\n"
            "- **Location:** page 4, Section 2.1, Table 1\n"
            "- **Claim:** The result supports only the stated experimental claim.\n"
            "- **Status:** verified\n\n"
            + payload,
            encoding="utf-8",
        )

    def build_package(self):
        errors, exported, catalog, fields = export_thesis.validate()
        self.assertEqual(errors, [])
        export_thesis.write_package(export_thesis.DEFAULT_OUTPUT, exported, catalog, fields)

    def test_current_committed_package_is_accepted(self):
        self.assertEqual(
            validate_thesis_package.validate_package(export_thesis.DEFAULT_OUTPUT),
            [],
        )

    def test_canonical_evidence_change_marks_package_stale(self):
        evidence = export_thesis.EXCERPTS / "SRC-TEST000001.md"
        evidence.write_text(evidence.read_text(encoding="utf-8") + "\nNew verified detail.\n", encoding="utf-8")
        errors = validate_thesis_package.validate_package(export_thesis.DEFAULT_OUTPUT)
        self.assertTrue(any("evidence differs from canonical evidence" in error for error in errors))

    def test_readme_count_must_match_current_selection(self):
        readme = export_thesis.DEFAULT_OUTPUT / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace("Επιλεγμένες πηγές: **1**", "Επιλεγμένες πηγές: **0**"),
            encoding="utf-8",
        )
        errors = validate_thesis_package.validate_package(export_thesis.DEFAULT_OUTPUT)
        self.assertTrue(any("selected-source count is stale" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
