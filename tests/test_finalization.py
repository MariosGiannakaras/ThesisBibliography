import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("finalization_tool", TOOLS / "finalize.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class FinalizationTests(unittest.TestCase):
    def test_meaningful_markdown_is_preserved_without_pdf_or_url(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            path.write_text(
                "# Useful source\n\n"
                + "This source explains robust reinforcement learning under uncertainty, "
                + "including assumptions, methods, evaluation metrics, limitations, and experimental findings. " * 8,
                encoding="utf-8",
            )
            self.assertTrue(MODULE.meaningful_text(path))

    def test_metadata_only_markdown_is_not_treated_as_useful(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            path.write_text(
                "# Unknown source\n\n- Συγγραφείς: άγνωστο\n- Έτος: άγνωστο\n- Σύνδεσμος: \n"
                "- Χρειάζεται έλεγχο μεταδεδομένων.\n",
                encoding="utf-8",
            )
            self.assertFalse(MODULE.meaningful_text(path))

    def test_missing_file_has_no_meaningful_content(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertFalse(MODULE.meaningful_text(Path(directory) / "missing.md"))

    def test_useful_analysis_protects_source_without_pdf_or_url(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = (MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS)
            try:
                MODULE.SOURCES = root / "sources"
                MODULE.ANALYSES = root / "analyses"
                MODULE.EXCERPTS = root / "evidence"
                for folder in (MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS):
                    folder.mkdir()
                (MODULE.SOURCES / "SRC-TEST000001.md").write_text(
                    "# Metadata only\n\n- Έτος: άγνωστο\n",
                    encoding="utf-8",
                )
                (MODULE.ANALYSES / "SRC-TEST000001.md").write_text(
                    "# Analysis\n\n"
                    + "The analysis documents the method, assumptions, experimental design, metrics, "
                    + "results, limitations, validity threats, and relevance to robust agents. " * 16,
                    encoding="utf-8",
                )
                self.assertTrue(MODULE.has_useful_content("SRC-TEST000001"))
            finally:
                MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS = original

    def test_empty_analysis_template_does_not_protect_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = (MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS)
            try:
                MODULE.SOURCES = root / "sources"
                MODULE.ANALYSES = root / "analyses"
                MODULE.EXCERPTS = root / "evidence"
                for folder in (MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS):
                    folder.mkdir()
                (MODULE.SOURCES / "SRC-TEST000001.md").write_text(
                    "# Metadata only\n\n- Έτος: άγνωστο\n",
                    encoding="utf-8",
                )
                template = (ROOT / "templates" / "source-analysis.md").read_text(encoding="utf-8")
                (MODULE.ANALYSES / "SRC-TEST000001.md").write_text(template, encoding="utf-8")
                self.assertFalse(MODULE.has_useful_content("SRC-TEST000001"))
            finally:
                MODULE.SOURCES, MODULE.ANALYSES, MODULE.EXCERPTS = original

    def test_finalization_archives_unmatched_and_removes_only_exact_duplicate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = (MODULE.INCOMING, MODULE.ORIGINALS, MODULE.UNMATCHED)
            try:
                MODULE.INCOMING = root / "new-originals"
                MODULE.ORIGINALS = root / "originals"
                MODULE.UNMATCHED = MODULE.ORIGINALS / "unidentified"
                MODULE.INCOMING.mkdir(parents=True)
                first = MODULE.INCOMING / "first.pdf"
                duplicate = MODULE.INCOMING / "duplicate.pdf"
                distinct = MODULE.INCOMING / "distinct.pdf"
                payload = b"%PDF-1.4\n" + b"same" * 300
                first.write_bytes(payload)
                duplicate.write_bytes(payload)
                distinct.write_bytes(b"%PDF-1.4\n" + b"different" * 300)

                archived, duplicates = MODULE.preserve_unmatched_uploads()

                self.assertEqual(2, archived)
                self.assertEqual(1, duplicates)
                self.assertEqual(2, len(list(MODULE.UNMATCHED.glob("*.pdf"))))
                self.assertEqual([], list(MODULE.INCOMING.glob("*.pdf")))
            finally:
                MODULE.INCOMING, MODULE.ORIGINALS, MODULE.UNMATCHED = original


if __name__ == "__main__":
    unittest.main()
