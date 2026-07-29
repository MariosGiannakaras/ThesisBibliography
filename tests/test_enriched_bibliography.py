from __future__ import annotations
import csv,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class EnrichedBibliographyTests(unittest.TestCase):
 def test_overlay_matches_catalog(self):
  catalog=json.loads((ROOT/'catalog'/'source_catalog.json').read_text())
  overlay=json.loads((ROOT/'catalog'/'verified_source_metadata.json').read_text())
  self.assertEqual({r['source_id'] for r in catalog},{r['source_id'] for r in overlay})
  self.assertEqual(len(overlay),len({r['source_id'] for r in overlay}))
 def test_reference_queue_status(self):
  with (ROOT/'queues'/'REFERENCES_TO_SCREEN.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
  self.assertTrue(all(r['screening_status'] in {'pending','already-present'} for r in rows))
 def test_excerpt_ids_exist(self):
  ids={r['source_id'] for r in json.loads((ROOT/'catalog'/'source_catalog.json').read_text())}
  for path in (ROOT/'curation'/'excerpts'/'by-source').glob('*.md'):
   self.assertIn(path.name.split('__',1)[0].upper(),ids)
if __name__=='__main__': unittest.main()
