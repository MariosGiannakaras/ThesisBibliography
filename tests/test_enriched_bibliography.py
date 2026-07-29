from __future__ import annotations
import csv,importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('enrich_bibliography',ROOT/'scripts'/'enrich_bibliography.py')
enrich=importlib.util.module_from_spec(spec); spec.loader.exec_module(enrich)
class EnrichedBibliographyTests(unittest.TestCase):
 def test_overlay_matches_catalog(self):
  catalog=json.loads((ROOT/'catalog'/'source_catalog.json').read_text())
  overlay=json.loads((ROOT/'catalog'/'verified_source_metadata.json').read_text())
  self.assertEqual({r['source_id'] for r in catalog},{r['source_id'] for r in overlay})
  self.assertEqual(len(overlay),len({r['source_id'] for r in overlay}))
 def test_reference_queue_status(self):
  with (ROOT/'queues'/'REFERENCES_TO_SCREEN.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
  self.assertTrue(all(r['screening_status'] in {'pending','pending-text-verification','already-present'} for r in rows))
 def test_excerpt_ids_exist(self):
  ids={r['source_id'] for r in json.loads((ROOT/'catalog'/'source_catalog.json').read_text())}
  for path in (ROOT/'curation'/'excerpts'/'by-source').glob('*.md'):
   self.assertIn(path.name.split('__',1)[0].upper(),ids)
 def test_youtube_identity_parameters_are_preserved(self):
  self.assertEqual(enrich.canon('https://www.youtube.com/watch?v=abc123&list=PL9&utm_source=x'),'https://www.youtube.com/watch?v=abc123&list=PL9')
 def test_cited_identifier_is_not_source_identifier(self):
  doi,arxiv_id=enrich.ids({'url':'https://en.wikipedia.org/wiki/Reinforcement_learning','title':'Reinforcement learning'},'This article cites arXiv:2503.16586 and doi:10.1000/example.')
  self.assertEqual((doi,arxiv_id),('',''))
 def test_unicode_title_normalization_is_nonempty(self):
  self.assertEqual(enrich.norm('Ανθεκτική Ενισχυτική Μάθηση'),'ανθεκτική ενισχυτική μάθηση')
 def test_manual_reference_decisions_survive_regeneration(self):
  old_queue,old_import=enrich.QUE,enrich.IMP
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp); enrich.QUE=root/'queues'; enrich.IMP=root/'imports'; enrich.QUE.mkdir(); (enrich.IMP/'g').mkdir(parents=True)
   url='https://example.org/paper'; key='url:'+url
   fields=['candidate_key','candidate_text','candidate_url','origin_count','origin_ids','already_cataloged','screening_status','decision','notes']
   with (enrich.QUE/'REFERENCES_TO_SCREEN.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerow({'candidate_key':key,'candidate_url':url,'decision':'include','notes':'reviewed'})
   with (enrich.IMP/'g'/'table.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['Link']); w.writeheader(); w.writerow({'Link':url})
   row=enrich.refs([],[])[0]
   self.assertEqual((row['decision'],row['notes']),('include','reviewed'))
  enrich.QUE, enrich.IMP = old_queue, old_import
 def test_textual_reference_without_url_is_queued(self):
  old_root,old_import,old_queue=enrich.ROOT,enrich.IMP,enrich.QUE
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp); (root/'sources').mkdir(); enrich.ROOT=root; enrich.IMP=root/'imports'; enrich.QUE=root/'queues'; enrich.IMP.mkdir(); enrich.QUE.mkdir()
   source=root/'sources'/'s.md'; source.write_text('# Paper\n\n## References\nBrynjolfsson, E. and McAfee, A. (2017). Machine, Platform, Crowd. Norton.\n')
   rows=enrich.refs([{'source_id':'SRC-TEST00000','normalized_path':'sources/s.md','url':''}],[])
   self.assertTrue(any(r['screening_status']=='pending-text-verification' and 'brynjolfsson' in r['candidate_text'] for r in rows))
  enrich.ROOT,enrich.IMP,enrich.QUE=old_root,old_import,old_queue
if __name__=='__main__': unittest.main()
