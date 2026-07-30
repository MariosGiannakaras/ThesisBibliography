import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "εργαλεία"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("originals_tool", TOOLS / "πρωτότυπα.py")
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

    def test_html_is_not_accepted_as_pdf(self):
        self.assertFalse(MODULE.looks_like_pdf(b"<html>Verifying your browser</html>"))
        self.assertTrue(MODULE.looks_like_pdf(b"%PDF-1.7\n" + b"x" * 2000))

    def test_source_id_in_filename_is_safe_match(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "random_SRC-ABCDEF1234_document.pdf"
            path.write_bytes(b"%PDF-1.4\n" + b"x" * 2000)
            rows = [{"Κωδικός": "SRC-ABCDEF1234", "Τίτλος": "A Paper", "Σύνδεσμος": ""}]
            source_id, reason = MODULE.match_uploaded(path, rows, {"SRC-ABCDEF1234": ""})
            self.assertEqual("SRC-ABCDEF1234", source_id)
            self.assertIn("κωδικός", reason)

    def test_body_citation_is_not_source_identity(self):
        from κοινά_πηγών import identities

        text = "# Different paper\n\nBody citation https://arxiv.org/abs/2203.12117"
        self.assertNotIn("arxiv:2203.12117", identities("", "Different paper", text))

    def test_homepage_and_channel_are_not_duplicate_identity(self):
        from κοινά_πηγών import identities

        self.assertEqual(set(), identities("https://openreview.net/", "Unknown", ""))
        self.assertEqual(set(), identities("https://youtube.com/@example", "A lecture", ""))
        self.assertIn(
            "url:https://youtube.com/watch?v=abc123",
            identities("https://youtube.com/watch?v=abc123", "A lecture", ""),
        )


if __name__ == "__main__":
    unittest.main()
