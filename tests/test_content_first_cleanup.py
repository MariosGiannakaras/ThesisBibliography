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

    def test_exact_markdown_content_can_merge_orphans(self):
        primary = {"Κωδικός": "SRC-AAAAAAAAAA"}
        duplicate = {"Κωδικός": "SRC-BBBBBBBBBB"}
        text = "same substantive publication content " * 400
        texts = {
            "SRC-AAAAAAAAAA": text,
            "SRC-BBBBBBBBBB": text,
        }
        self.assertTrue(MODULE._content_only_corroboration(primary, duplicate, texts))

    def test_formatting_difference_is_preserved(self):
        primary = {"Κωδικός": "SRC-AAAAAAAAAA"}
        duplicate = {"Κωδικός": "SRC-BBBBBBBBBB"}
        texts = {
            "SRC-AAAAAAAAAA": "# Title\n\nSame scientific words.\n",
            "SRC-BBBBBBBBBB": "# Title\nSame scientific words.\n",
        }
        self.assertFalse(MODULE._content_only_corroboration(primary, duplicate, texts))

    def test_shared_identifier_does_not_merge_different_markdown(self):
        rows = [
            {
                "Κωδικός": "SRC-AAAAAAAAAA",
                "Τίτλος": "Publication A",
                "Συγγραφείς": "Author",
                "Έτος": "2024",
                "Σύνδεσμος": "https://doi.org/10.1234/example",
                "Τύπος": "ακαδημαϊκή εργασία",
                "Θέματα": "χωρίς κατηγορία",
                "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
                "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
                "Προτεραιότητα": "χαμηλή",
                "Σημειώσεις": "",
            },
            {
                "Κωδικός": "SRC-BBBBBBBBBB",
                "Τίτλος": "Publication A chapter/version",
                "Συγγραφείς": "Author",
                "Έτος": "2024",
                "Σύνδεσμος": "https://doi.org/10.1234/example",
                "Τύπος": "βιβλίο ή κεφάλαιο",
                "Θέματα": "χωρίς κατηγορία",
                "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
                "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
                "Προτεραιότητα": "χαμηλή",
                "Σημειώσεις": "",
            },
        ]
        texts = {
            "SRC-AAAAAAAAAA": "full publication content " * 400,
            "SRC-BBBBBBBBBB": "different chapter content " * 400,
        }
        merged = []
        changes = []
        result = MODULE._merge_strong_identities_content_first(
            rows, texts, changes, merged
        )
        self.assertEqual(2, len(result))
        self.assertEqual([], merged)


if __name__ == "__main__":
    unittest.main()
