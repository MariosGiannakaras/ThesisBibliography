#!/usr/bin/env python3
"""Validate enriched bibliography outputs against the base catalog."""
from __future__ import annotations
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'verified-arxiv-api','verified-crossref-api','probable-openalex-match','recorded-source-url','unresolved'}
def main()->int:
 errors=[]; catalog=json.loads((ROOT/'catalog'/'source_catalog.json').read_text()); ids={r['source_id'] for r in catalog}
 overlay=json.loads((ROOT/'catalog'/'verified_source_metadata.json').read_text())
 oids=[r['source_id'] for r in overlay]
 if len(oids)!=len(set(oids)) or set(oids)!=ids: errors.append('metadata overlay IDs do not exactly match catalog IDs')
 for row in overlay:
  status=row.get('verification_status'); provider=row.get('provider') or ''
  if status not in ALLOWED: errors.append(f"{row.get('source_id')}: invalid verification status {status}")
  if status=='verified-arxiv-api' and (not row.get('arxiv_id') or provider!='arXiv API'): errors.append(f"{row.get('source_id')}: arXiv verification lacks matching ID/provider")
  if status=='verified-crossref-api' and (not row.get('doi') or provider!='Crossref API'): errors.append(f"{row.get('source_id')}: Crossref verification lacks matching DOI/provider")
  if status=='probable-openalex-match' and (provider!='OpenAlex API' or not row.get('verified_title') or float(row.get('match_score') or 0)<0.92): errors.append(f"{row.get('source_id')}: OpenAlex match lacks evidence")
  if status in {'recorded-source-url','unresolved'} and provider: errors.append(f"{row.get('source_id')}: unverified status has provider claim")
 q=ROOT/'queues'/'REFERENCES_TO_SCREEN.csv'
 if not q.exists(): errors.append('missing reference queue')
 else:
  rows=list(csv.DictReader(q.open(encoding='utf-8',newline='')))
  required={'candidate_key','candidate_text','candidate_url','origin_count','origin_ids','already_cataloged','screening_status','decision','notes'}
  if not required.issubset(rows[0].keys() if rows else required): errors.append('reference queue schema mismatch')
  allowed_status={'pending','pending-text-verification','already-present'}
  for row in rows:
   if row.get('screening_status') not in allowed_status: errors.append(f"invalid reference status: {row.get('candidate_key')}")
   if not row.get('candidate_url') and not row.get('candidate_text'): errors.append(f"empty reference candidate: {row.get('candidate_key')}")
 for p in ['catalog/VERIFIED_SOURCE_METADATA.csv','catalog/VERIFIED_SOURCE_METADATA.md','catalog/MALFORMED_OR_MISSING_DATA.md','catalog/ENRICHMENT_REPORT.md','catalog/ENRICHMENT_METHOD.md','queues/NEXT_SOURCES.md','curation/EXCERPT_INDEX.md','incoming/README.md','notes/by-source/NOTE_TEMPLATE.md']:
  if not (ROOT/p).exists(): errors.append(f'missing {p}')
 for p in (ROOT/'curation'/'excerpts'/'by-source').glob('*.md'):
  sid=p.name.split('__',1)[0].upper()
  if sid not in ids: errors.append(f'excerpt references unknown source ID {sid}')
 if errors:
  print('Enriched bibliography validation failed:'); [print('-',e) for e in errors]; return 1
 print(f'Enriched bibliography validation passed for {len(catalog)} sources.'); return 0
if __name__=='__main__': raise SystemExit(main())
