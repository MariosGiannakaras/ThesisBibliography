#!/usr/bin/env python3
"""Validate enriched bibliography outputs against the base catalog."""
from __future__ import annotations
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main()->int:
 errors=[]; catalog=json.loads((ROOT/'catalog'/'source_catalog.json').read_text()); ids={r['source_id'] for r in catalog}
 overlay=json.loads((ROOT/'catalog'/'verified_source_metadata.json').read_text())
 oids=[r['source_id'] for r in overlay]
 if len(oids)!=len(set(oids)) or set(oids)!=ids: errors.append('metadata overlay IDs do not exactly match catalog IDs')
 q=ROOT/'queues'/'REFERENCES_TO_SCREEN.csv'
 if not q.exists(): errors.append('missing reference queue')
 else:
  rows=list(csv.DictReader(q.open(encoding='utf-8',newline='')))
  required={'candidate_url','origin_count','origin_ids','already_cataloged','screening_status','decision','notes'}
  if not required.issubset(rows[0].keys() if rows else required): errors.append('reference queue schema mismatch')
 for p in ['catalog/VERIFIED_SOURCE_METADATA.csv','catalog/VERIFIED_SOURCE_METADATA.md','catalog/MALFORMED_OR_MISSING_DATA.md','catalog/ENRICHMENT_REPORT.md','queues/NEXT_SOURCES.md','curation/EXCERPT_INDEX.md','incoming/README.md','notes/by-source/NOTE_TEMPLATE.md']:
  if not (ROOT/p).exists(): errors.append(f'missing {p}')
 for p in (ROOT/'curation'/'excerpts'/'by-source').glob('*.md'):
  sid=p.name.split('__',1)[0].upper()
  if sid not in ids: errors.append(f'excerpt references unknown source ID {sid}')
 if errors:
  print('Enriched bibliography validation failed:'); [print('-',e) for e in errors]; return 1
 print(f'Enriched bibliography validation passed for {len(catalog)} sources.'); return 0
if __name__=='__main__': raise SystemExit(main())
