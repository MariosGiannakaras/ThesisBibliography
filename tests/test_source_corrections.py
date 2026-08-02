import hashlib
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))


def load_script(module_name: str, filename: str):
    spec = importlib.util.spec_from_file_location(module_name, TOOLS / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


DUPLICATES = load_script("exact_pdf_duplicates_test", "exact_duplicates.py")
CORRECTIONS = load_script("known_source_corrections_test", "known_fixes.py")


class SourceCorrectionTests(unittest.TestCase):
    def test_internal_session_and_degree_project_titles_are_generic(self):
        from originals_common import GENERIC_TITLE

        self.assertIsNotNone(GENERIC_TITLE.search("Degree Project, 30 Credits, Spring 2024"))
        self.assertIsNotNone(
            GENERIC_TITLE.search(
                "• LTRCRT-3100 - Building Python Applications for DevNet Candidates"
            )
        )
        self.assertIsNone(GENERIC_TITLE.search("Deep reinforcement learning in non-stationary environments"))

    def test_generic_title_cannot_create_source(self):
        from originals_common import PdfInfo, can_create_source_from_pdf

        info = PdfInfo(
            title="Degree Project, 30 Credits, Spring 2024",
            authors="David Skog",
            year="2024",
            pages=40,
            text="Degree Project, 30 Credits, Spring 2024 " + "body " * 100,
        )
        allowed, _ = can_create_source_from_pdf(Path("FULLTEXT02.pdf"), info)
        self.assertFalse(allowed)

    def test_combined_notes_are_idempotent_across_existing_delimited_text(self):
        existing = "πρώτη σημείωση | επαναλαμβανόμενη σημείωση | επαναλαμβανόμενη σημείωση"
        self.assertEqual(
            "πρώτη σημείωση | επαναλαμβανόμενη σημείωση | νέα σημείωση",
            CORRECTIONS.combine_notes(existing, "επαναλαμβανόμενη σημείωση", "νέα σημείωση"),
        )

    def test_lfs_pointer_uses_object_oid(self):
        oid = "a" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.pdf"
            path.write_text(
                "version https://git-lfs.github.com/spec/v1\n"
                f"oid sha256:{oid}\n"
                "size 12345\n",
                encoding="utf-8",
            )
            self.assertEqual(oid, DUPLICATES.pdf_object_identity(path))

    def test_regular_file_uses_sha256(self):
        payload = b"%PDF-1.7\n" + b"x" * 2048
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.pdf"
            path.write_bytes(payload)
            self.assertEqual(
                hashlib.sha256(payload).hexdigest(),
                DUPLICATES.pdf_object_identity(path),
            )


if __name__ == "__main__":
    unittest.main()
