#!/usr/bin/env python3
"""Enrich the staged bibliography without modifying archived Markdown bytes."""
from __future__ import annotations
import argparse,csv,json,re,time,unicodedata,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/'catalog'/'source_catalog.json'; SRC=ROOT/'sources'/'markdown'; IMP=ROOT/'imports'/'notebooklm'
OUT=ROOT/'catalog'; QUE=ROOT/'queues'; CUR=ROOT/'curation'; EX=CUR/'excerpts'/'by-source'
OVER=OUT/'verified_source_metadata.json'; UA='ThesisBibliography/1.0 metadata-curation'
ARX=re.compile(r'(?:arxiv:|arxiv\.org/(?:abs|pdf|html)/)(\d{4}\.\d{4,5})(?:v\d+)?',re.I)
DOI=re.compile(r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b',re.I); URL=re.compile(r'https?://[^\s<>\]\[\)\(\"\']+')
REFH=re.compile(r'^#{1,6}\s*(references|bibliography|works cited|βιβλιογραφ.*?)\s*$',re.I|re.M)
EXH=re.compile(r'^##\s+(SRC-[A-F0-9]{10})\s+—\s+(.+?)\s*$',re.M)
ACADEMIC={'academic-paper','thesis-or-dissertation','book-or-chapter','standard-or-institutional-report'}
TARGETS=[
('AI Safety Gridworlds','https://arxiv.org/abs/1711.09883','benchmark'),
('NovGrid: A Flexible Grid World for Evaluating Agent Response to Novelty','https://arxiv.org/abs/2203.12117','benchmark-and-metrics'),
('CARL: A Benchmark for Contextual and Adaptive Reinforcement Learning','https://arxiv.org/abs/2110.02102','benchmark'),
('Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning','https://openreview.net/forum?id=2uQBSa2X4R','benchmark-and-taxonomy'),
('Deep Reinforcement Learning at the Edge of the Statistical Precipice','https://arxiv.org/abs/2108.13264','evaluation-statistics'),
('Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks','https://arxiv.org/abs/2306.13831','environment'),
('Action Robust Reinforcement Learning and Applications in Continuous Control','https://arxiv.org/abs/1901.09184','action-uncertainty'),
('Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations','https://arxiv.org/abs/2003.08938','observation-uncertainty'),
('Restarted Bayesian Online Change-point Detection for Non-Stationary Markov Decision Processes','https://proceedings.mlr.press/v232/alami23a.html','nonstationarity'),
('Deep Reinforcement Learning in Non-Stationary Environments','https://opus.lib.uts.edu.au/handle/10453/186408','comparable-thesis'),
('Efficient Adaptation of Reinforcement Learning Agents to Sudden Environmental Change','https://hdl.handle.net/1853/76967','comparable-thesis')]

def norm(s:str)->str:
 s=unicodedata.normalize('NFKC',s).casefold(); return re.sub(r'\s+',' ',''.join(c if c.isalnum() or c.isspace() else ' ' for c in s)).strip()
def canon(u:str)->str:
 if not u:return ''
 u=u.strip().rstrip('.,;:)>]}"'); p=urllib.parse.urlparse(u); h=p.netloc.lower().removeprefix('www.'); a=ARX.search(u)
 if a:return f'https://arxiv.org/abs/{a.group(1)}'
 if h=='doi.org':return f"https://doi.org/{p.path.lstrip('/').lower()}"
 if h in {'youtube.com','m.youtube.com'}:
  q=urllib.parse.parse_qs(p.query); keep=[]
  for key in ('v','list'):
   if q.get(key):keep.append((key,q[key][0]))
  return 'https://www.youtube.com'+p.path+('?' + urllib.parse.urlencode(keep) if keep else '')
 if h=='youtu.be':return 'https://www.youtube.com/watch?v='+p.path.lstrip('/')
 query=[(k,v) for k,vals in urllib.parse.parse_qs(p.query).items() if not k.lower().startswith(('utm_','fbclid','gclid')) for v in vals]
 return f'{p.scheme or "https"}://{h}{p.path.rstrip("/")}' + ('?' + urllib.parse.urlencode(query) if query else '') if h else u
def ids(r:dict[str,Any],text:str)->tuple[str,str]:
 region='\n'.join([str(r.get('url') or ''),str(r.get('title') or '')]); d=DOI.search(region); a=ARX.search(region)
 return (d.group(0).rstrip('.,;)').lower() if d else '',a.group(1) if a else '')
def get_json(url:str)->dict[str,Any]|None:
 for i in range(3):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
   with urllib.request.urlopen(req,timeout=35) as res:return json.loads(res.read().decode())
  except Exception:
   if i<2:time.sleep(i+1)
 return None
def arxiv(ids_:list[str])->dict[str,dict[str,str]]:
 out={}; ns={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom'}; failures=[]
 for i in range(0,len(ids_),25):
  batch=ids_[i:i+25]; last=None
  for attempt in range(3):
   try:
    req=urllib.request.Request('https://export.arxiv.org/api/query?id_list='+','.join(batch),headers={'User-Agent':UA})
    with urllib.request.urlopen(req,timeout=40) as res:root=ET.fromstring(res.read())
    for e in root.findall('a:entry',ns):
     aid=re.sub(r'v\d+$','',e.findtext('a:id','',ns).split('/')[-1]); out[aid]={'title':' '.join(e.findtext('a:title','',ns).split()),'authors':'; '.join(x.findtext('a:name','',ns) for x in e.findall('a:author',ns)),'year':e.findtext('a:published','',ns)[:4],'doi':e.findtext('x:doi','',ns) or '', 'provider':'arXiv API'}
    last=None; break
   except Exception as exc:
    last=exc; time.sleep(attempt+1)
  if last is not None:failures.append({'ids':batch,'error':str(last)})
 if failures:raise RuntimeError('arXiv metadata lookup failed: '+json.dumps(failures))
 return out
def crossref(doi:str)->dict[str,str]|None:
 p=get_json('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))
 if not p or not isinstance(p.get('message'),dict):return None
 m=p['message']; au=[' '.join(filter(None,(a.get('given'),a.get('family')))) for a in m.get('author',[])]; dp=((m.get('published') or m.get('issued') or {}).get('date-parts') or [[]])[0]
 return {'title':(m.get('title') or [''])[0],'authors':'; '.join(x for x in au if x),'year':str(dp[0]) if dp else '','doi':str(m.get('DOI') or doi).lower(),'provider':'Crossref API'}
def openalex(title:str)->tuple[dict[str,str]|None,float]:
 target=norm(title)
 if not target:return None,0.0
 p=get_json('https://api.openalex.org/works?'+urllib.parse.urlencode({'search':title,'per-page':3})); best=None; score=0.0
 for m in (p or {}).get('results',[]):
  t=str(m.get('display_name') or ''); candidate=norm(t)
  if not candidate:continue
  s=SequenceMatcher(None,target,candidate).ratio()
  if s>score:
   au=[(x.get('author') or {}).get('display_name') for x in m.get('authorships',[])]; loc=m.get('primary_location') or {}
   best={'title':t,'authors':'; '.join(x for x in au if x),'year':str(m.get('publication_year') or ''),'doi':str(m.get('doi') or '').removeprefix('https://doi.org/'),'official_url':str(loc.get('landing_page_url') or ''),'provider':'OpenAlex API'}; score=s
 return best,score
def write_csv(path:Path,rows:list[dict[str,Any]],fields:list[str]):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader()
  for r in rows:w.writerow({k:'; '.join(map(str,v)) if isinstance(v,list) else v for k,v in r.items()})
def build_overlay(records:list[dict[str,Any]],online:bool)->list[dict[str,Any]]:
 old={r['source_id']:r for r in json.loads(OVER.read_text())} if OVER.exists() else {}
 prepared=[]
 for r in records:
  text=(ROOT/r['normalized_path']).read_text(encoding='utf-8',errors='replace'); d,a=ids(r,text); prepared.append((r,d,a))
 amap=arxiv(sorted({a for _,_,a in prepared if a})) if online else {}
 rows=[]
 for r,d,a in prepared:
  row={'source_id':r['source_id'],'catalog_title':r.get('title',''),'verified_title':'','authors':'','year':'','doi':d,'arxiv_id':a,'official_url':canon(r.get('url','')),'verification_status':'recorded-source-url' if r.get('url') else 'unresolved','provider':'','match_score':''}
  meta=None; score=1.0
  if online and a and a in amap:meta=amap[a]; row['verification_status']='verified-arxiv-api'
  elif online and d:meta=crossref(d); row['verification_status']='verified-crossref-api' if meta else row['verification_status']; time.sleep(.1)
  elif online and r.get('source_type') in ACADEMIC and r.get('title'):
   meta,score=openalex(str(r['title'])); time.sleep(.1)
   if score>=.92:row['verification_status']='probable-openalex-match'
   else:meta=None
  elif not online and r['source_id'] in old:return_old=old[r['source_id']]; rows.append(return_old); continue
  if meta:
   row.update({'verified_title':meta.get('title',''),'authors':meta.get('authors',''),'year':meta.get('year',''),'doi':meta.get('doi') or d,'official_url':canon(meta.get('official_url') or row['official_url']),'provider':meta.get('provider',''),'match_score':round(score,4)})
  rows.append(row)
 return rows
def refs(records:list[dict[str,Any]],overlay:list[dict[str,Any]])->list[dict[str,Any]]:
 existing={}
 queue_path=QUE/'REFERENCES_TO_SCREEN.csv'
 if queue_path.exists():
  try:existing={r.get('candidate_key') or r.get('candidate_url'):r for r in csv.DictReader(queue_path.open(encoding='utf-8',newline=''))}
  except Exception:existing={}
 present={canon(r.get('url','')) for r in records if r.get('url')}; present|={canon(r.get('official_url','')) for r in overlay if r.get('official_url')}; found=defaultdict(set); text_found=defaultdict(set)
 for r in records:
  text=(ROOT/r['normalized_path']).read_text(encoding='utf-8',errors='replace'); m=list(REFH.finditer(text)); region=text[m[-1].start():] if m else ''
  if not region:continue
  for u in URL.findall(region):
   c=canon(u)
   if c:found[c].add(r['source_id'])
  for d in DOI.findall(region):found['https://doi.org/'+d.rstrip('.,;)').lower()].add(r['source_id'])
  for a in ARX.findall(region):found['https://arxiv.org/abs/'+a].add(r['source_id'])
  for line in region.splitlines()[1:]:
   item=re.sub(r'^[\s*+\-\d.\[\]()]+','',line).strip()
   if 30<=len(item)<=700 and re.search(r'\b(?:19|20)\d{2}\b',item) and not URL.search(item) and not DOI.search(item) and not ARX.search(item):text_found[norm(item)].add(r['source_id'])
 for table in IMP.rglob('*.csv'):
  try:
   for row in csv.DictReader(table.open(encoding='utf-8-sig',errors='replace')):
    u=canon(str(row.get('Link') or ''))
    if u:found[u].add('notebooklm:'+table.parent.name)
  except Exception:pass
 rows=[]
 for u,orig in sorted(found.items(),key=lambda x:(-len(x[1]),x[0])):
  key='url:'+u; old=existing.get(key) or existing.get(u) or {}
  rows.append({'candidate_key':key,'candidate_text':'','candidate_url':u,'origin_count':len(orig),'origin_ids':sorted(orig),'already_cataloged':u in present,'screening_status':'already-present' if u in present else 'pending','decision':old.get('decision',''),'notes':old.get('notes','')})
 for item,orig in sorted(text_found.items(),key=lambda x:(-len(x[1]),x[0])):
  key='text:'+item; old=existing.get(key,{})
  rows.append({'candidate_key':key,'candidate_text':item,'candidate_url':'','origin_count':len(orig),'origin_ids':sorted(orig),'already_cataloged':False,'screening_status':'pending-text-verification','decision':old.get('decision',''),'notes':old.get('notes','')})
 return rows
def esc(value:Any)->str:return str(value or '—').replace('|','\\|')
def outputs(records:list[dict[str,Any]],overlay:list[dict[str,Any]],reference_rows:list[dict[str,Any]]):
 OVER.write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); fields=['source_id','catalog_title','verified_title','authors','year','doi','arxiv_id','official_url','verification_status','provider','match_score']; write_csv(OUT/'VERIFIED_SOURCE_METADATA.csv',overlay,fields)
 lines=['# Verified Source Metadata','','This overlay supplements the intake catalog without changing archived Markdown. API verification does not mean the full source was read.','','| ID | Catalog title | Verified title | Authors | Year | Link | Status |','|---|---|---|---|---:|---|---|']
 for r in overlay:lines.append(f"| `{r['source_id']}` | {esc(r['catalog_title'])} | {esc(r['verified_title'])} | {esc(r['authors'])} | {esc(r['year'])} | {esc(r['official_url'])} | {r['verification_status']} |")
 (OUT/'VERIFIED_SOURCE_METADATA.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 write_csv(QUE/'REFERENCES_TO_SCREEN.csv',reference_rows,['candidate_key','candidate_text','candidate_url','origin_count','origin_ids','already_cataloged','screening_status','decision','notes'])
 known={norm(r.get('title','')) for r in records}; nxt=['# Next Sources to Add or Verify','','This is a screening queue, not an approved bibliography.','','## Known priority targets','']
 for t,u,c in TARGETS:nxt.append(f"- [{'x' if norm(t) in known else ' '}] **{t}** — {c} — {u}")
 pending=[r for r in reference_rows if r['screening_status'] in {'pending','pending-text-verification'}]; nxt+=['','## Reference-mining queue','',f'Pending candidates: **{len(pending)}**. See `REFERENCES_TO_SCREEN.csv`; prioritize candidates cited by several high-relevance sources.']
 (QUE/'NEXT_SOURCES.md').write_text('\n'.join(nxt)+'\n',encoding='utf-8')
 bad=[]; ov={r['source_id']:r for r in overlay}
 for r in records:
  p=[]
  if r.get('content_status') in {'failed-load','metadata-only','partial'}:p.append(str(r['content_status']))
  if r.get('source_type')=='unknown':p.append('unknown-source-type')
  if r.get('source_type') in ACADEMIC and ov[r['source_id']]['verification_status'] not in {'verified-arxiv-api','verified-crossref-api'}:p.append('metadata-not-identifier-verified')
  if not r.get('url') and not ov[r['source_id']].get('official_url'):p.append('missing-source-link')
  if p:bad.append((r,p))
 b=['# Malformed, Missing or Unverified Source Data','','Records remain archived; this lists repair or verification work.','','| ID | Title | Problems | Markdown |','|---|---|---|---|']
 for r,p in bad:b.append(f"| `{r['source_id']}` | {esc(r['title'])} | {', '.join(p)} | `{r['normalized_path']}` |")
 (OUT/'MALFORMED_OR_MISSING_DATA.md').write_text('\n'.join(b)+'\n',encoding='utf-8')
 return len(bad),len(pending)
def split_excerpts()->int:
 EX.mkdir(parents=True,exist_ok=True)
 for p in EX.glob('*.md'):p.unlink()
 src=CUR/'USEFUL_EXCERPTS.md'
 if not src.exists():return 0
 text=src.read_text(); ms=list(EXH.finditer(text)); idx=['# Candidate Excerpt Index','','Machine-selected review candidates; verify before citation.','']
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(text); fn=f'{m.group(1).lower()}__candidate-excerpt.md'; (EX/fn).write_text(text[m.start():end].strip()+'\n'); idx.append(f"- [`{m.group(1)}` — {m.group(2)}](excerpts/by-source/{fn})")
 (CUR/'EXCERPT_INDEX.md').write_text('\n'.join(idx)+'\n'); (CUR/'excerpts'/'README.md').write_text('# Candidate Excerpts\n\nVerify against source Markdown and original PDF where needed. Reviewed interpretation belongs in `notes/by-source/`.\n')
 return len(ms)
def main()->int:
 ap=argparse.ArgumentParser(); ap.add_argument('--online',action='store_true'); a=ap.parse_args(); records=json.loads(CAT.read_text())
 OUT.mkdir(exist_ok=True); QUE.mkdir(exist_ok=True); CUR.mkdir(exist_ok=True); overlay=build_overlay(records,a.online); rr=refs(records,overlay); bad,pending=outputs(records,overlay,rr); ex=split_excerpts(); statuses=defaultdict(int)
 for r in overlay:statuses[r['verification_status']]+=1
 (OUT/'ENRICHMENT_REPORT.md').write_text('\n'.join(['# Bibliography Enrichment Report','',f'- Source records: **{len(records)}**',f"- Explicit arXiv/Crossref metadata: **{statuses['verified-arxiv-api']+statuses['verified-crossref-api']}**",f"- Probable OpenAlex matches: **{statuses['probable-openalex-match']}**",f"- Recorded URLs only: **{statuses['recorded-source-url']}**",f"- Unresolved identities: **{statuses['unresolved']}**",f'- Malformed/incomplete/unverified: **{bad}**',f'- Candidate excerpt files: **{ex}**',f'- Reference candidates: **{len(rr)}**',f'- Pending new references: **{pending}**','','These are curation states, not final bibliography approval.'])+'\n')
 print(json.dumps({'sources':len(records),'verified_identifier_metadata':statuses['verified-arxiv-api']+statuses['verified-crossref-api'],'references':len(rr),'candidate_excerpts':ex,'malformed':bad},indent=2)); return 0
if __name__=='__main__':raise SystemExit(main())
