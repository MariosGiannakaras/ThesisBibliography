import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "convert_pdf.py"
SPEC = importlib.util.spec_from_file_location("pdf_conversion_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PdfConversionTests(unittest.TestCase):
    def test_quality_accepts_dense_pages(self):
        pages = [MODULE.PageExtraction(1, "word " * 200), MODULE.PageExtraction(2, "text " * 180)]
        quality = MODULE.assess_quality(pages)
        self.assertFalse(quality.further_conversion_required)
        self.assertEqual(2, quality.readable_pages)

    def test_quality_flags_many_empty_pages(self):
        pages = [
            MODULE.PageExtraction(1, "word " * 200),
            MODULE.PageExtraction(2, ""),
            MODULE.PageExtraction(3, ""),
            MODULE.PageExtraction(4, "x"),
        ]
        quality = MODULE.assess_quality(pages)
        self.assertTrue(quality.further_conversion_required)
        self.assertTrue(any("20%" in reason for reason in quality.reasons))

    def test_placeholder_source_can_be_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            path.write_text(
                "# Example\n\n> Η εγγραφή δημιουργήθηκε από πρωτότυπο PDF που δεν υπήρχε ακόμη στον κατάλογο.\n",
                encoding="utf-8",
            )
            self.assertTrue(MODULE.source_is_replaceable(path, {"Κατάσταση": "μόνο μεταδεδομένα"}))

    def test_substantial_markdown_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            path.write_text("# Study\n\n" + ("Detailed scientific content " * 200), encoding="utf-8")
            self.assertFalse(
                MODULE.source_is_replaceable(path, {"Κατάσταση": "διαθέσιμο πλήρες κείμενο"})
            )

    def test_rejected_analysis_marks_conversion_not_required(self):
        with tempfile.TemporaryDirectory() as directory:
            analyses = Path(directory) / "analyses"
            analyses.mkdir()
            source_id = "SRC-ABCDEF1234"
            (analyses / f"{source_id}.md").write_text(
                "---\nκωδικός: SRC-ABCDEF1234\nκατάσταση: απόρριψη\n---\n\n## Απόφαση\nΑπόρριψη.\n",
                encoding="utf-8",
            )
            original_analyses = MODULE.ANALYSES
            try:
                MODULE.ANALYSES = analyses
                self.assertEqual("rejected", MODULE.canonical_decision(source_id))
            finally:
                MODULE.ANALYSES = original_analyses

    def test_not_required_entry_is_not_pending(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "originals" / "SRC-ABCDEF1234.pdf"
            pdf.parent.mkdir(parents=True)
            pdf.write_bytes(b"%PDF-1.4\n")
            original_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                entry = MODULE.not_required_entry(
                    {"Κωδικός": "SRC-ABCDEF1234", "Τίτλος": "Rejected study"},
                    pdf,
                    "a" * 64,
                )
                self.assertEqual("δεν-απαιτείται-λόγω-απόρριψης", entry["Κατάσταση μετατροπής"])
                self.assertEqual("όχι", entry["Χρειάζεται περαιτέρω μετατροπή"])
            finally:
                MODULE.ROOT = original_root

    def test_ocr_missing_is_reported_without_modifying_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.pdf"
            path.write_bytes(b"%PDF-1.4\n")
            with mock.patch.object(MODULE.shutil, "which", return_value=None):
                result = MODULE.run_ocr(path, Path(directory), "eng+ell")
            self.assertEqual("μη-διαθέσιμο", result.status)
            self.assertEqual(path, result.pdf_path)

    def test_lfs_identity_uses_object_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.pdf"
            oid = "a" * 64
            path.write_text(
                "version https://git-lfs.github.com/spec/v1\n"
                f"oid sha256:{oid}\nsize 123\n",
                encoding="utf-8",
            )
            self.assertEqual(oid, MODULE.pdf_identity(path))

    def test_rendered_markdown_records_further_conversion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                pdf = root / "originals" / "SRC-ABCDEF1234.pdf"
                pdf.parent.mkdir(parents=True)
                pdf.write_bytes(b"%PDF-1.4\n")
                pages = [
                    MODULE.PageExtraction(1, "Readable " * 100),
                    MODULE.PageExtraction(2, ""),
                    MODULE.PageExtraction(3, ""),
                ]
                quality = MODULE.assess_quality(pages)
                markdown = MODULE.render_markdown(
                    {"Κωδικός": "SRC-ABCDEF1234", "Τίτλος": "Example"},
                    pdf,
                    "a" * 64,
                    pages,
                    quality,
                    MODULE.OcrResult("ολοκληρώθηκε", pdf),
                    "eng+ell",
                )
                meta = MODULE.parse_front_matter(markdown)
                self.assertEqual("ναι", meta["further_conversion_required"])
                self.assertIn("PDF_PAGE: 2", markdown)
                self.assertIn(MODULE.AUTO_MARKER, markdown)
            finally:
                MODULE.ROOT = original_root


if __name__ == "__main__":
    unittest.main()
