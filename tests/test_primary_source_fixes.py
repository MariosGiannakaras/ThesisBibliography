import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "primary_source_fixes.py"
SPEC = importlib.util.spec_from_file_location("primary_source_fixes_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PrimarySourceFixTests(unittest.TestCase):
    def row(self) -> dict[str, str]:
        return {
            "Κωδικός": MODULE.RANE_SOURCE_ID,
            "Τίτλος": "Nitin Liladhar Rane1, *, Saurabh P. Choudhary1,2, Jayesh Rane3",
            "Συγγραφείς": "Markus Richter",
            "Έτος": "2024",
            "Σύνδεσμος": f"https://doi.org/{MODULE.RANE_DOI}",
            "Τύπος": "ακαδημαϊκή εργασία",
            "Θέματα": "χωρίς κατηγορία",
            "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
            "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
            "Προτεραιότητα": "χρειάζεται διόρθωση",
            "Σημειώσεις": "Αυτόματη πλήρης μετατροπή PDF με OCR· τεχνικά πλήρης, προς ανθρώπινο έλεγχο",
        }

    def write_source(
        self,
        directory: Path,
        original_sha: str | None = None,
        *,
        quoted: bool = True,
    ) -> Path:
        source = directory / f"{MODULE.RANE_SOURCE_ID}.md"
        original_sha = original_sha or MODULE.RANE_ORIGINAL_SHA256
        sha_value = f'"{original_sha}"' if quoted else original_sha
        source.write_text(
            "---\n"
            f'source_id: "{MODULE.RANE_SOURCE_ID}"\n'
            f"original_sha256: {sha_value}\n"
            "---\n\n"
            "# Nitin Liladhar Rane1, *, Saurabh P. Choudhary1,2, Jayesh Rane3\n\n"
            "<!-- page: 1 -->\n"
            "Artificial intelligence for enhancing resilience\n"
            "Nitin Liladhar Rane, Saurabh P. Choudhary, Jayesh Rane\n",
            encoding="utf-8",
        )
        return source

    def test_verified_quoted_original_overrides_bad_metadata_without_rewriting_body(self):
        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory)
            source = self.write_source(sources, quoted=True)
            rows, changes = MODULE.apply([self.row()], sources)

            self.assertEqual(1, len(changes))
            row = rows[0]
            self.assertEqual(MODULE.RANE_TITLE, row["Τίτλος"])
            self.assertEqual(MODULE.RANE_AUTHORS, row["Συγγραφείς"])
            self.assertEqual(MODULE.RANE_PRIMARY_URL, row["Σύνδεσμος"])
            self.assertEqual("υψηλή", row["Προτεραιότητα"])
            self.assertIn("ανθεκτικότητα και ανάκαμψη", row["Θέματα"])
            self.assertIn("DOI-only", row["Σημειώσεις"])

            text = source.read_text(encoding="utf-8")
            self.assertIn(f'original_sha256: "{MODULE.RANE_ORIGINAL_SHA256}"', text)
            self.assertIn(f"# {MODULE.RANE_TITLE}", text)
            self.assertIn(f"> Source: {MODULE.RANE_PRIMARY_URL}", text)
            self.assertIn(f"> DOI as printed by publisher: https://doi.org/{MODULE.RANE_DOI}", text)
            self.assertIn("<!-- page: 1 -->", text)
            self.assertIn("Nitin Liladhar Rane, Saurabh P. Choudhary, Jayesh Rane", text)

    def test_unquoted_expected_hash_is_also_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory)
            source = self.write_source(sources, quoted=False)
            self.assertTrue(MODULE.source_has_expected_original(source))

    def test_wrong_original_hash_fails_closed_even_when_quoted(self):
        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory)
            self.write_source(sources, "0" * 64, quoted=True)
            with self.assertRaisesRegex(RuntimeError, "refusing primary metadata override"):
                MODULE.apply([self.row()], sources)

    def test_absent_target_is_a_noop(self):
        rows = [{**self.row(), "Κωδικός": "SRC-0000000000"}]
        result, changes = MODULE.apply(rows, Path("does-not-exist"))
        self.assertEqual(rows, result)
        self.assertEqual([], changes)


if __name__ == "__main__":
    unittest.main()
