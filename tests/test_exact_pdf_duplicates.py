import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "exact_duplicates.py"
SPEC = importlib.util.spec_from_file_location("exact_pdf_duplicates_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ExactPdfDuplicateTests(unittest.TestCase):
    def layout(self, root: Path):
        originals = root / "originals"
        sources = root / "sources"
        analyses = root / "analyses"
        evidence = root / "evidence"
        report = root / "catalog" / "exact-pdf-duplicates.csv"
        for path in (originals, sources, analyses, evidence, report.parent):
            path.mkdir(parents=True, exist_ok=True)
        return originals, sources, analyses, evidence, report

    def test_exact_pdf_removes_only_redundant_file_and_keeps_source_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals, sources, analyses, evidence, report = self.layout(root)
            old_id = "SRC-AAAAAAAAAA"
            new_id = "SRC-BBBBBBBBBB"
            (sources / f"{old_id}.md").write_text("canonical reviewed source", encoding="utf-8")
            (sources / f"{new_id}.md").write_text("different export text", encoding="utf-8")
            (analyses / f"{old_id}.md").write_text("reviewed analysis", encoding="utf-8")
            (evidence / f"{old_id}.md").write_text("verified evidence", encoding="utf-8")
            payload = b"%PDF-1.4\nidentical scientific paper bytes\n%%EOF\n"
            old_pdf = originals / f"{old_id}.pdf"
            new_pdf = originals / f"{new_id}.pdf"
            old_pdf.write_bytes(payload)
            new_pdf.write_bytes(payload)

            removed = MODULE.prune_exact_duplicates(
                originals=originals,
                sources=sources,
                analyses=analyses,
                evidence=evidence,
                report=report,
            )

            self.assertEqual(1, len(removed))
            self.assertTrue(old_pdf.exists())
            self.assertFalse(new_pdf.exists())
            self.assertTrue((sources / f"{old_id}.md").exists())
            self.assertTrue((sources / f"{new_id}.md").exists())
            self.assertIn("source record preserved", report.read_text(encoding="utf-8"))

    def test_different_pdf_bytes_are_never_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals, sources, analyses, evidence, report = self.layout(root)
            for source_id, payload in (
                ("SRC-AAAAAAAAAA", b"%PDF-1.4\nversion A\n%%EOF\n"),
                ("SRC-BBBBBBBBBB", b"%PDF-1.4\nversion B\n%%EOF\n"),
            ):
                (sources / f"{source_id}.md").write_text("source", encoding="utf-8")
                (originals / f"{source_id}.pdf").write_bytes(payload)

            removed = MODULE.prune_exact_duplicates(
                originals=originals,
                sources=sources,
                analyses=analyses,
                evidence=evidence,
                report=report,
            )

            self.assertEqual([], removed)
            self.assertEqual(2, len(list(originals.glob("*.pdf"))))

    def test_lfs_object_identity_is_used_for_exact_duplicate_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            originals, sources, analyses, evidence, report = self.layout(root)
            oid = "a" * 64
            pointer = (
                "version https://git-lfs.github.com/spec/v1\n"
                f"oid sha256:{oid}\n"
                "size 12345\n"
            ).encode("ascii")
            for source_id in ("SRC-AAAAAAAAAA", "SRC-BBBBBBBBBB"):
                (sources / f"{source_id}.md").write_text("source", encoding="utf-8")
                (originals / f"{source_id}.pdf").write_bytes(pointer)

            removed = MODULE.prune_exact_duplicates(
                originals=originals,
                sources=sources,
                analyses=analyses,
                evidence=evidence,
                report=report,
            )

            self.assertEqual(1, len(removed))
            self.assertEqual(1, len(list(originals.glob("*.pdf"))))
            self.assertEqual(oid, removed[0][2])


if __name__ == "__main__":
    unittest.main()
