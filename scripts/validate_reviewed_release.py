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
for term in ['Mulberry Township','Choctaw','1 June 1860','20 June 1860','working date, source not located',"Who's who",'A short timeline','reopened']:
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
# Classroom content checks complement technical link/PDF checks; they are not a pilot.
from PIL import Image,ImageChops
for x in json.loads((R/'sources/reviewed/lesson-derivatives.json').read_text()):
 original=R/x['source'];derivative=R/x['path']
 check(hashlib.sha256(original.read_bytes()).hexdigest()==x['source_sha256'],'Derivative original hash changed '+x['path'])
 check(hashlib.sha256(derivative.read_bytes()).hexdigest()==x['sha256'],'Derivative hash changed '+x['path'])
 a=Image.open(original).crop(x['box']).convert('RGB');b=Image.open(derivative).convert('RGB')
 check(a.size==b.size and ImageChops.difference(a,b).getbbox() is None,'Derivative is not exact source crop '+x['path'])
 check(x['human_review']=='pending','Human sign-off must not be invented')
worksheet=(R/'classroom/student-worksheet.md').read_text();guide=(R/'classroom/teacher-guide.md').read_text();sheets=(R/'classroom/source-sheets.md').read_text();evaluation=(R/'classroom/evaluation-form.md').read_text()
model=guide.split('## Model label (100–150 words)')[1].split('## Label rubric')[0].strip()
check(100<=len(model.split())<=150,'Model violates required word count')
check('[A]' in model and '[B]' in model,'Model lacks source references')
check('assignment' in model and 'consideration' in model,'Model lacks specific next record/question')
for item in ['P1','P2','P3']:
 check(worksheet.count('| '+item+' |')==2,'Baseline/exit not paired for '+item)
 check(item in evaluation,'Evaluation lacks '+item)
check('P1 D; P2 I; P3 N' in guide and 'P1 D; P2 I; P3 N' in evaluation,'Teacher/form matched answer key')
check('2 August' not in worksheet and '10 August' not in worksheet,'Core assessment depends on optional death/attack dates')
check('22–30' in guide and 'all five' in guide,'Classification task absent from timed lesson')
check('Anonymous feedback' in worksheet,'Promised student feedback absent')
check('Partial transcription' in sheets and 'Column key' in sheets,'In-pack reading aids absent')
check('1 June 1860' in sheets and '20 June 1860' in sheets,'Census reference/enumeration dates absent')
check('Not part of the 50-minute core lesson' in (R/'classroom/memory-extension.md').read_text(),'Optional memory material not clearly separated')
# Correction notice and current spatial-data withdrawal checks.
import xml.etree.ElementTree as ET
legacy=BeautifulSoup((R/'superseded-v20.html').read_text(),'html.parser')
check(legacy.body.find(True,recursive=False).get('id')=='correction-notice','Correction notice is not first visible legacy body element')
check(not legacy.find_all('script'),'Legacy map/popup scripts still active')
check(not legacy.select('img[src^="field-docs/"]'),'Withdrawn gallery image still displayed')
check('James Mitchell' not in BeautifulSoup((R/'index.html').read_text(),'html.parser').get_text(),'Reader plants Wilson prisoner association')
check('which party or which fight' in (R/'editions/v21/current-reading.md').read_text(),'Wilson antecedent uncertainty absent')
check('reprisal group' not in (R/'editions/v21/current-reading.md').read_text().split('The excerpt quoted')[1].split('## A short timeline')[0],'Wilson party assumption reintroduced')
check(not ET.parse(R/'horner-sites.kml').findall('.//{http://www.opengis.net/kml/2.2}Placemark'),'Withdrawn KML retains locations')
for f in (R/'sources/ppan-001').glob('*.json'):
 check(json.loads(f.read_text()).get('status')=='withdrawn','Cadastral extract not withdrawn '+f.name)
legacy_pdf=fitz.open(R/'legacy-research-edition.pdf')
check('Correction notice' in legacy_pdf[0].get_text(),'Legacy PDF lacks notice at front')
check(len(legacy_pdf)==58,'Unexpected legacy PDF page preservation')
print(f'{checks} checks; {len(errors)} failures')
for e in errors:print('FAIL:',e)
raise SystemExit(bool(errors))
