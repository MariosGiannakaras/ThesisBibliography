import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("originals_tool", TOOLS / "originals.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules["originals_tool"] = MODULE
SPEC.loader.exec_module(MODULE)


class OriginalsTests(unittest.TestCase):
    def test_arxiv_becomes_pdf_candidate(self):
        row = {
            "Σύνδεσμος": "https://arxiv.org/abs/2203.12117",
            "Τίτλος": "NovGrid",
            "Τύπος": "ακαδημαϊκή εργασία",
        }
        self.assertIn("https://arxiv.org/pdf/2203.12117", MODULE.candidate_urls(row, ""))

    def test_trailing_parenthesis_is_removed_from_candidate_url(self):
        row = {
            "Σύνδεσμος": "https://example.org/report.pdf)",
            "Τίτλος": "Report",
            "Τύπος": "ακαδημαϊκή εργασία",
        }
        self.assertIn("https://example.org/report.pdf", MODULE.candidate_urls(row, ""))
        self.assertNotIn("https://example.org/report.pdf)", MODULE.candidate_urls(row, ""))

    def test_direct_pdf_is_document_candidate_even_with_wrong_type(self):
        row = {
            "Σύνδεσμος": "https://example.org/papers/report.pdf",
            "Τίτλος": "Report",
            "Τύπος": "ιστοσελίδα",
        }
        self.assertTrue(MODULE.is_document_candidate(row))
        self.assertFalse(MODULE.is_url_only(row))

    def test_html_is_not_accepted_as_pdf(self):
        self.assertFalse(MODULE.looks_like_pdf(b"<html>Verifying your browser</html>"))
        self.assertTrue(MODULE.looks_like_pdf(b"%PDF-1.7\n" + b"x" * 2000))

    def test_source_id_in_filename_is_safe_match(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "random_SRC-ABCDEF1234_document.pdf"
            path.write_bytes(b"%PDF-1.4\n" + b"x" * 2000)
            rows = [{"Κωδικός": "SRC-ABCDEF1234", "Τίτλος": "A Paper", "Σύνδεσμος": ""}]
            result = MODULE.match_uploaded(path, rows, {"SRC-ABCDEF1234": ""})
            self.assertEqual("SRC-ABCDEF1234", result.source_id)
            self.assertIn("κωδικός", result.reason)

    def test_multiple_pdf_identifiers_are_not_treated_as_primary_identity(self):
        from originals_common import PdfInfo, strong_pdf_identities

        info = PdfInfo(doi=["10.1000/primary", "10.1000/citation"])
        self.assertEqual(set(), strong_pdf_identities(info))

    def test_suspicious_distribution_is_kept_pending(self):
        from originals_common import PdfInfo, can_create_source_from_pdf

        info = PdfInfo(
            title="A Complete Book About Autonomous Agents",
            authors="Example Author",
            year="2025",
            pages=120,
            text="A Complete Book About Autonomous Agents " + "body " * 100,
        )
        allowed, reason = can_create_source_from_pdf(Path("OceanofPDF_example.pdf"), info)
        self.assertFalse(allowed)
        self.assertIn("προέλευσης", reason)

    def test_incomplete_unidentified_pdf_does_not_create_source(self):
        from originals_common import PdfInfo, can_create_source_from_pdf

        info = PdfInfo(
            title="A Plausible but Unverified Technical Document",
            pages=5,
            text="A Plausible but Unverified Technical Document " + "body " * 100,
        )
        allowed, _ = can_create_source_from_pdf(Path("document.pdf"), info)
        self.assertFalse(allowed)

    def test_linked_alternate_stem_is_recognized(self):
        from originals_common import LINKED_PDF_STEM_RE

        self.assertIsNotNone(LINKED_PDF_STEM_RE.fullmatch("SRC-ABCDEF1234"))
        self.assertIsNotNone(
            LINKED_PDF_STEM_RE.fullmatch("SRC-ABCDEF1234__alternative-1234567890")
        )

    def test_body_citation_is_not_source_identity(self):
        from sources_common import identities

        text = "# Different paper\n\nBody citation https://arxiv.org/abs/2203.12117"
        self.assertNotIn("arxiv:2203.12117", identities("", "Different paper", text))

    def test_homepage_and_channel_are_not_duplicate_identity(self):
        from sources_common import identities

        self.assertEqual(set(), identities("https://openreview.net/", "Unknown", ""))
        self.assertEqual(set(), identities("https://youtube.com/@example", "A lecture", ""))
        self.assertIn(
            "url:https://youtube.com/watch?v=abc123",
            identities("https://youtube.com/watch?v=abc123", "A lecture", ""),
        )

    def test_unmatched_pdf_is_archived_instead_of_deleted(self):
        from originals_files import archive_unmatched

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals = root / "originals"
            unmatched = originals / "unidentified"
            incoming = root / "unknown document.pdf"
            incoming.write_bytes(b"%PDF-1.4\n" + b"unique-content" * 200)

            archived, reason = archive_unmatched(
                incoming,
                originals=originals,
                unmatched=unmatched,
            )

            self.assertIsNotNone(archived)
            assert archived is not None
            self.assertTrue(archived.exists())
            self.assertFalse(incoming.exists())
            self.assertIn("αρχειοθετήθηκε", reason)

    def test_only_exact_duplicate_unmatched_pdf_is_deleted(self):
        from originals_files import archive_unmatched

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals = root / "originals"
            unmatched = originals / "unidentified"
            first = root / "first.pdf"
            second = root / "second.pdf"
            payload = b"%PDF-1.4\n" + b"same-content" * 200
            first.write_bytes(payload)
            second.write_bytes(payload)

            archived, _ = archive_unmatched(first, originals=originals, unmatched=unmatched)
            duplicate, reason = archive_unmatched(second, originals=originals, unmatched=unmatched)

            self.assertIsNotNone(archived)
            self.assertIsNone(duplicate)
            self.assertFalse(second.exists())
            self.assertEqual(1, len(list(unmatched.glob("*.pdf"))))
            self.assertIn("ακριβές διπλότυπο", reason)

    def test_different_pdf_with_same_name_is_preserved(self):
        from originals_files import archive_unmatched

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals = root / "originals"
            unmatched = originals / "unidentified"
            first_dir = root / "a"
            second_dir = root / "b"
            first_dir.mkdir()
            second_dir.mkdir()
            first = first_dir / "paper.pdf"
            second = second_dir / "paper.pdf"
            first.write_bytes(b"%PDF-1.4\n" + b"first" * 300)
            second.write_bytes(b"%PDF-1.4\n" + b"second" * 300)

            first_archived, _ = archive_unmatched(first, originals=originals, unmatched=unmatched)
            second_archived, _ = archive_unmatched(second, originals=originals, unmatched=unmatched)

            self.assertIsNotNone(first_archived)
            self.assertIsNotNone(second_archived)
            self.assertEqual(2, len(list(unmatched.glob("*.pdf"))))


if __name__ == "__main__":
    unittest.main()
