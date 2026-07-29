#!/usr/bin/env python3
"""Process one or more complete NotebookLM groups staged under incoming/."""
from __future__ import annotations
import argparse,re,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; IN=ROOT/'incoming'; GROUP=re.compile(r'Group\d+',re.I)
def run(*args:str)->None:
 subprocess.run([sys.executable,*args],cwd=ROOT,check=True)
def main()->int:
 ap=argparse.ArgumentParser(); ap.add_argument('--online',action='store_true'); a=ap.parse_args()
 groups=sorted(p for p in IN.iterdir() if p.is_dir() and GROUP.fullmatch(p.name)) if IN.exists() else []
 if not groups: print('No incoming GroupN folders found.'); return 0
 for group in groups:
  source_dirs=[p for p in group.iterdir() if p.is_dir() and re.fullmatch(r'Group\d+Files',p.name,re.I)]
  helpers_md=list(group.glob('*.md')); helpers_csv=list(group.glob('*.csv'))
  if len(source_dirs)!=1 or not helpers_md or not helpers_csv: raise RuntimeError(f'{group}: expected one GroupNFiles folder plus helper Markdown and CSV')
  target=ROOT/group.name
  if target.exists() or (ROOT/'imports'/'notebooklm'/f"group-{int(re.search(r'\d+',group.name).group()):02d}").exists(): raise RuntimeError(f'Group collision: {group.name}')
  shutil.move(str(group),str(target))
 run('scripts/organize_sources.py')
 enrich=['scripts/enrich_bibliography.py']
 if a.online: enrich.append('--online')
 run(*enrich)
 print(f'Processed {len(groups)} incoming group(s).'); return 0
if __name__=='__main__': raise SystemExit(main())
