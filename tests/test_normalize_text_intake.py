import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "normalize_text_intake.py"
SPEC = importlib.util.spec_from_file_location("normalize_text_intake_tool", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

JATS = """<?xml version="1.0" encoding="UTF-8"?>
<article article-type="review-article">
  <front>
    <article-meta>
      <article-id pub-id-type="doi">10.1234/example.2026.1</article-id>
      <title-group><article-title>Resilient AI Systems</article-title></title-group>
      <contrib-group>
        <contrib contrib-type="author"><name><surname>Doe</surname><given-names>Jane</given-names></name></contrib>
        <contrib contrib-type="author"><name><surname>Roe</surname><given-names>John</given-names></name></contrib>
      </contrib-group>
      <pub-date pub-type="epub"><year>2026</year></pub-date>
      <abstract><p>Abstract about resilience and adaptation.</p></abstract>
    </article-meta>
  </front>
  <body>
    <sec><title>1. Introduction</title><p>Useful source text.</p>
      <sec><title>1.1. Recovery</title><p>Recovery is measured after change.</p></sec>
    </sec>
  </body>
  <back><ref-list><ref id="r1"><mixed-citation>Reference One, 2020.</mixed-citation></ref></ref-list></back>
</article>
"""


class NormalizeTextIntakeTests(unittest.TestCase):
    def test_jats_to_markdown_extracts_scientific_metadata_and_body(self):
        markdown = MODULE.jats_to_markdown(JATS)
        self.assertIn("# Resilient AI Systems", markdown)
        self.assertIn("> Source: https://doi.org/10.1234/example.2026.1", markdown)
        self.assertIn("Authors: Jane Doe; John Roe", markdown)
        self.assertIn("Year: 2026", markdown)
        self.assertIn("## Abstract", markdown)
        self.assertIn("## 1. Introduction", markdown)
        self.assertIn("### 1.1. Recovery", markdown)
        self.assertIn("Recovery is measured after change.", markdown)
        self.assertIn("## References", markdown)
        self.assertIn("1. Reference One, 2020.", markdown)

    def test_raw_jats_markdown_and_original_xml_converge_without_data_loss(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "new-sources").mkdir(parents=True)
            (root / "new-originals").mkdir(parents=True)
            source = root / "new-sources" / "paper.md"
            original = root / "new-originals" / "paper.xml"
            source.write_text("\ufeff" + JATS.replace("><", ">\n<"), encoding="utf-8")
            original.write_text(JATS, encoding="utf-8")

            counts = MODULE.normalize(root)

            self.assertFalse(original.exists())
            normalized = source.read_text(encoding="utf-8")
            self.assertTrue(normalized.startswith("# Resilient AI Systems\n"))
            self.assertNotIn("<article", normalized)
            archived = list((root / "structured-originals").glob("ORIGINAL-*.xml"))
            self.assertEqual(1, len(archived))
            self.assertEqual(JATS, archived[0].read_text(encoding="utf-8"))
            self.assertEqual(1, counts["jats_markdown"])
            self.assertEqual(1, counts["jats_xml"])
            self.assertEqual(1, counts["archived_originals"])

            with (root / "structured-originals" / "index.csv").open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(1, len(rows))
            self.assertEqual("new-originals/paper.xml", rows[0]["Original intake path"])
            self.assertEqual("new-sources/paper.md", rows[0]["Derived path"])

            second = MODULE.normalize(root)
            self.assertEqual(0, second["jats_markdown"])
            self.assertEqual(0, second["jats_xml"])
            with (root / "structured-originals" / "index.csv").open(encoding="utf-8", newline="") as handle:
                self.assertEqual(1, len(list(csv.DictReader(handle))))

    def test_direct_jats_xml_in_new_sources_generates_markdown_and_archives_xml(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            incoming = root / "new-sources"
            (root / "new-originals").mkdir(parents=True)
            incoming.mkdir(parents=True)
            xml = incoming / "article.xml"
            xml.write_text(JATS, encoding="utf-8")

            counts = MODULE.normalize(root)

            self.assertFalse(xml.exists())
            markdown = incoming / "article.md"
            self.assertTrue(markdown.exists())
            self.assertIn("# Resilient AI Systems", markdown.read_text(encoding="utf-8"))
            self.assertEqual(1, counts["jats_xml"])
            self.assertEqual(1, len(list((root / "structured-originals").glob("ORIGINAL-*.xml"))))

    def test_auxiliary_text_is_preserved_as_searchable_note_and_original(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            incoming = root / "new-sources"
            (root / "new-originals").mkdir(parents=True)
            incoming.mkdir(parents=True)
            note = incoming / "my-definition.txt"
            note.write_text("Artificial intelligence is discussed here.\n", encoding="utf-8")

            counts = MODULE.normalize(root)

            self.assertFalse(note.exists())
            notes = list((root / "research-notes" / "intake").glob("NOTE-*.md"))
            self.assertEqual(1, len(notes))
            text = notes[0].read_text(encoding="utf-8")
            self.assertIn("Artificial intelligence is discussed here.", text)
            self.assertIn("not citation-ready", text)
            self.assertEqual(1, len(list((root / "structured-originals").glob("ORIGINAL-*.txt"))))
            self.assertEqual(1, counts["notes"])

    def test_non_jats_xml_original_is_preserved_as_note_not_fake_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "new-sources").mkdir(parents=True)
            originals = root / "new-originals"
            originals.mkdir(parents=True)
            xml = originals / "metadata.xml"
            xml.write_text("<metadata><value>Useful fragment</value></metadata>", encoding="utf-8")

            counts = MODULE.normalize(root)

            self.assertFalse(xml.exists())
            self.assertEqual([], list((root / "new-sources").glob("*.md")))
            notes = list((root / "research-notes" / "intake").glob("NOTE-*.md"))
            self.assertEqual(1, len(notes))
            self.assertIn("Useful fragment", notes[0].read_text(encoding="utf-8"))
            self.assertEqual(1, counts["notes"])


if __name__ == "__main__":
    unittest.main()
