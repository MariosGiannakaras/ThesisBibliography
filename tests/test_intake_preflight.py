import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "intake_preflight.py"
SPEC = importlib.util.spec_from_file_location("intake_preflight_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class IntakePreflightTests(unittest.TestCase):
    def test_blank_markdown_is_archived_without_collapsing_distinct_filenames(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            incoming = root / "new-sources"
            unresolved = root / "unresolved-intake"
            report = root / "catalog" / "unresolved-intake.csv"
            incoming.mkdir(parents=True)

            first = incoming / "different-source-a.md"
            second = incoming / "διαφορετική-πηγή-b.md"
            first.write_text("", encoding="utf-8")
            second.write_text("\n\t", encoding="utf-8")

            rows = MODULE.process_blank_markdown(incoming, unresolved, report)

            self.assertEqual(2, len(rows))
            self.assertFalse(first.exists())
            self.assertFalse(second.exists())
            archived = list(unresolved.glob("UNRESOLVED-*.md"))
            self.assertEqual(2, len(archived))
            self.assertNotEqual(archived[0].name, archived[1].name)
            self.assertTrue(all(path.name.isascii() for path in archived))

            with report.open(encoding="utf-8", newline="") as handle:
                report_rows = list(csv.DictReader(handle))
            self.assertEqual(2, len(report_rows))
            originals = {row["Original path"] for row in report_rows}
            self.assertEqual({"different-source-a.md", "διαφορετική-πηγή-b.md"}, originals)

    def test_nonblank_markdown_is_left_for_normal_import(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            incoming = root / "new-sources"
            unresolved = root / "unresolved-intake"
            report = root / "catalog" / "unresolved-intake.csv"
            incoming.mkdir(parents=True)
            source = incoming / "paper.md"
            source.write_text("# Paper\n\nSubstantive content.", encoding="utf-8")

            rows = MODULE.process_blank_markdown(incoming, unresolved, report)

            self.assertEqual([], rows)
            self.assertTrue(source.exists())
            self.assertEqual([], list(unresolved.glob("UNRESOLVED-*")))

    def test_later_run_preserves_previous_unresolved_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            incoming = root / "new-sources"
            unresolved = root / "unresolved-intake"
            report = root / "catalog" / "unresolved-intake.csv"
            incoming.mkdir(parents=True)

            first = incoming / "first-original-name.md"
            first.write_text("", encoding="utf-8")
            MODULE.process_blank_markdown(incoming, unresolved, report)

            second = incoming / "second-original-name.md"
            second.write_text("", encoding="utf-8")
            MODULE.process_blank_markdown(incoming, unresolved, report)

            with report.open(encoding="utf-8", newline="") as handle:
                report_rows = list(csv.DictReader(handle))
            self.assertEqual(2, len(report_rows))
            self.assertEqual(
                {"first-original-name.md", "second-original-name.md"},
                {row["Original path"] for row in report_rows},
            )
            self.assertEqual(2, len(list(unresolved.glob("UNRESOLVED-*.md"))))


if __name__ == "__main__":
    unittest.main()
