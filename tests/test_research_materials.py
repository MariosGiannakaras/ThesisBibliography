from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


rm = load_module("research_materials_test", ROOT / "tools" / "research_materials.py")
erc = load_module("export_research_corpus_test", ROOT / "tools" / "export_research_corpus.py")


class ResearchMaterialTests(unittest.TestCase):
    def make_pdf(self, path: Path, title: str = "Useful draft material") -> None:
        writer = PdfWriter()
        writer.add_blank_page(width=612, height=792)
        writer.add_metadata({"/Title": title, "/Author": "Test Author", "/CreationDate": "D:20240101000000"})
        with path.open("wb") as handle:
            writer.write(handle)

    def test_unidentified_pdf_is_preserved_as_material(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf_dir = root / "originals" / "unidentified"
            pdf_dir.mkdir(parents=True)
            self.make_pdf(pdf_dir / "original.pdf")
            rm.build(root)
            self.assertEqual(rm.validate(root), [])
            rows = rm.read_csv(root / "catalog" / "research-materials.csv")
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["title_candidate"], "Useful draft material")
            material = root / "materials" / f"{rows[0]['material_id']}.md"
            self.assertIn("not-citation-ready", material.read_text(encoding="utf-8"))

    def test_substantive_linked_source_is_not_duplicated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            originals = root / "originals"
            sources = root / "sources"
            originals.mkdir()
            sources.mkdir()
            self.make_pdf(originals / "SRC-1234567890.pdf")
            sources.joinpath("SRC-1234567890.md").write_text("word " * 200, encoding="utf-8")
            rm.build(root)
            self.assertEqual(rm.read_csv(root / "catalog" / "research-materials.csv"), [])
            self.assertEqual(rm.validate(root), [])

    def test_review_fields_survive_rebuild(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf_dir = root / "originals" / "unidentified"
            pdf_dir.mkdir(parents=True)
            self.make_pdf(pdf_dir / "original.pdf")
            rm.build(root)
            rows = rm.read_csv(root / "catalog" / "research-material-review.csv")
            rows[0]["canonical_title"] = "Reviewed title"
            rows[0]["identification_status"] = "identified"
            rm.write_csv(root / "catalog" / "research-material-review.csv", rm.REVIEW_FIELDS, rows)
            rm.build(root)
            rebuilt = rm.read_csv(root / "catalog" / "research-material-review.csv")
            self.assertEqual(rebuilt[0]["canonical_title"], "Reviewed title")
            self.assertEqual(rebuilt[0]["identification_status"], "identified")


class ResearchCorpusTests(unittest.TestCase):
    def test_build_and_validate_complete_corpus(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for directory in ("sources", "analyses", "evidence", "materials", "notes", "catalog"):
                (root / directory).mkdir(parents=True, exist_ok=True)
            (root / "notes" / "README.md").write_text("notes\n", encoding="utf-8")
            (root / "sources" / "SRC-1234567890.md").write_text("source text\n", encoding="utf-8")
            (root / "analyses" / "SRC-1234567890.md").write_text("analysis\n", encoding="utf-8")
            with (root / "catalog" / "sources.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Κωδικός"], lineterminator="\n")
                writer.writeheader()
                writer.writerow({"Κωδικός": "SRC-1234567890"})
            rm.write_csv(root / "catalog" / "research-materials.csv", rm.INVENTORY_FIELDS, [])
            rm.write_csv(root / "catalog" / "research-material-review.csv", rm.REVIEW_FIELDS, [])
            package = root / "thesis-package"
            (package / "catalog").mkdir(parents=True)
            (package / "manifest.csv").write_text("source_id\n", encoding="utf-8")
            (package / "catalog" / "package-metadata.json").write_text(
                json.dumps({"schema_version": 1}), encoding="utf-8"
            )
            output = root / "research-corpus"
            erc.build(root, output)
            self.assertEqual(erc.validate(root, output), [])
            (output / "README.md").write_text("tampered", encoding="utf-8")
            self.assertTrue(any("checksum mismatch" in error for error in erc.validate(root, output)))


if __name__ == "__main__":
    unittest.main()
