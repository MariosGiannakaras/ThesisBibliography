#!/usr/bin/env python3
"""Process complete NotebookLM groups staged under incoming/."""
from __future__ import annotations
import argparse,re,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; IN=ROOT/'incoming'; GROUP=re.compile(r'Group\d+',re.I)
def run(*args:str)->None: subprocess.run([sys.executable,*args],cwd=ROOT,check=True)
def main()->int:
 ap=argparse.ArgumentParser(); ap.add_argument('--offline',action='store_true',help='Skip official metadata services; output remains incomplete.'); a=ap.parse_args()
 groups=sorted(p for p in IN.iterdir() if p.is_dir() and GROUP.fullmatch(p.name)) if IN.exists() else []
 if not groups: print('No incoming GroupN folders found.'); return 0
 plans=[]
 for group in groups:
  source_dirs=[p for p in group.iterdir() if p.is_dir() and re.fullmatch(r'Group\d+Files',p.name,re.I)]
  helpers_md=list(group.glob('*.md')); helpers_csv=list(group.glob('*.csv'))
  if len(source_dirs)!=1 or not helpers_md or not helpers_csv: raise RuntimeError(f'{group}: expected one GroupNFiles folder plus helper Markdown and CSV')
  unexpected=[p for p in source_dirs[0].rglob('*') if p.is_file() and p.suffix.lower()!='.md']
  if unexpected: raise RuntimeError(f'{group}: non-Markdown source files must be archived separately before intake: '+', '.join(str(p.relative_to(ROOT)) for p in unexpected[:10]))
  target=ROOT/group.name; number=int(re.search(r'\d+',group.name).group()); imported=ROOT/'imports'/'notebooklm'/f'group-{number:02d}'
  if target.exists() or imported.exists(): raise RuntimeError(f'Group collision: {group.name}')
  plans.append((group,target))
 for source,target in plans: shutil.move(str(source),str(target))
 run('scripts/organize_sources.py')
 args=['scripts/enrich_bibliography.py']
 if not a.offline: args.append('--online')
 run(*args)
 print(f'Processed {len(groups)} incoming group(s); metadata mode: {"offline-incomplete" if a.offline else "online-verified"}.'); return 0
if __name__=='__main__': raise SystemExit(main())
