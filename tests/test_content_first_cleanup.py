import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location(
    "content_first_clean_links_tool", TOOLS / "content_first_clean_links.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ContentFirstCleanupTests(unittest.TestCase):
    def test_same_title_authors_and_year_do_not_merge_different_content(self):
        primary = {
            "Κωδικός": "SRC-AAAAAAAAAA",
            "Τίτλος": "Same publication title",
            "Συγγραφείς": "Same Author",
            "Έτος": "2024",
        }
        duplicate = {
            "Κωδικός": "SRC-BBBBBBBBBB",
            "Τίτλος": "Same publication title",
            "Συγγραφείς": "Same Author",
            "Έτος": "2024",
        }
        texts = {
            "SRC-AAAAAAAAAA": "alpha " * 400,
            "SRC-BBBBBBBBBB": "beta " * 400,
        }
        self.assertFalse(MODULE._content_only_corroboration(primary, duplicate, texts))

    def test_exact_substantive_content_can_merge_orphans(self):
        primary = {"Κωδικός": "SRC-AAAAAAAAAA"}
        duplicate = {"Κωδικός": "SRC-BBBBBBBBBB"}
        text = "same substantive publication content " * 400
        texts = {
            "SRC-AAAAAAAAAA": text,
            "SRC-BBBBBBBBBB": text,
        }
        self.assertTrue(MODULE._content_only_corroboration(primary, duplicate, texts))


if __name__ == "__main__":
    unittest.main()
