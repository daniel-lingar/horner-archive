"""Validate reviewed release provenance, local links, budget and PDF constraints."""
from pathlib import Path
import hashlib,json,re
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import fitz
R=Path(__file__).resolve().parents[1]
errors=[];checks=0
def check(ok,msg):
 global checks
 checks+=1
 if not ok:errors.append(msg)
pages=[R/'index.html',R/'transcript-1942.html',R/'ppan-map.html',*R.glob('classroom/*.html'),*R.glob('grant-readiness/*.html'),R/'grant-readiness/neh-planning/submission-gates.html']
for p in pages:
 s=BeautifulSoup(p.read_text(),'html.parser')
 check(s.html.get('lang')=='en',str(p)+' missing language')
 for el in s.select('[href], img[src]'):
  u=urlsplit(el.get('href',el.get('src','')))
  if u.scheme or u.netloc:continue
  dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
  check(dest.is_file(),str(p.relative_to(R))+' missing local target '+str(u))
  if u.fragment and dest.is_file() and dest.suffix=='.html':
   check(BeautifulSoup(dest.read_text(),'html.parser').find(id=unquote(u.fragment)) is not None,'Missing anchor '+str(u))
 for im in s.find_all('img'):check(bool(im.get('alt')),str(p)+' missing alt text')
 if p.name!='superseded-v20.html':check(not s.select('img[src^="field-docs/"]'),'Withdrawn gallery used in current page')
data=json.loads((R/'sources/reviewed/source-catalog.json').read_text())
check(len(data['sources'])==7,'Expected seven source groups')
for s in data['sources']:
 p=R/s['path'];check(p.is_file(),'Missing source '+s['id'])
 check(s.get('sha256')==hashlib.sha256(p.read_bytes()).hexdigest(),'Source hash mismatch '+s['id'])
 for field in ['provenance','supports','limits','rights']:check(bool(s.get(field)),'Missing '+field+' '+s['id'])
b=json.loads((R/'grant-readiness/neh-planning/budget.json').read_text())
for row in b['rows']:check(row['quantity']*row['rate']==row['total'],'Budget row arithmetic '+row['role'])
check(sum(x['total'] for x in b['rows'])==b['direct_total']==25920,'Budget total')
check(b['indirect_total']==0,'Unexpected indirect total')
core=(R/'index.html').read_text()
for term in ['Mulberry Township','SE 1/4 NE 1/4','1,143,763','WC75885','fourth great-grandparent','164 elapsed','reopened']:
 check(term in core,'Missing correction '+term)
register=(R/'corrections/v21-claim-reconciliation.md').read_text()
check(len(re.findall(r'^\| C\d+ ',register,re.M))==40,'Missing audit findings')
for f in [R/'dossier.pdf',R/'classroom/source-pack.pdf',*R.glob('grant-readiness/neh-planning/*.pdf'),R/'sources/1860-floyd-township-census-analysis.pdf']:
 d=fitz.open(f);check(len(d)>0,'Empty PDF '+str(f))
 for i,page in enumerate(d):
  for line in page.get_text('dict')['blocks']:
   if line['type']!=0:continue
   x0,y0,x1,y1=line['bbox'];check(x0>=-1 and y0>=-1 and x1<=page.rect.width+1 and y1<=page.rect.height+1,f'{f.name} page {i+1} text outside page')
 if f.name=='narrative.pdf':
  check(len(d)<=15,'Narrative page limit');text=''.join(p.get_text() for p in d)
  check('AI-generated' in text,'Missing NEH AI acknowledgment')
  check(not text.lstrip().startswith('Exhibition planning discussion packet'),'Narrative has forbidden packet cover')
 if f.name in ['workplan.pdf','bibliography.pdf']:check(len(d)<=2,'Suggested attachment length exceeded '+f.name)
check(not json.loads((R/'sources/glo-field-notes-t12n-r24w/manifest.json').read_text())['oq_status'].lower().startswith('oq-22 closed'),'GLO question falsely closed')
print(f'{checks} checks; {len(errors)} failures')
for e in errors:print('FAIL:',e)
raise SystemExit(bool(errors))
