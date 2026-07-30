import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "εργαλεία"
SPEC = importlib.util.spec_from_file_location("finalization_tool", TOOLS / "οριστικοποίηση.py")
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


if __name__ == "__main__":
    unittest.main()
