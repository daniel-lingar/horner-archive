"""Build v21 reviewed pages and seven PDFs from versioned Markdown sources.

Install: python -m pip install markdown weasyprint
Run from any directory: python scripts/build_reviewed_release.py
WeasyPrint also needs its documented system font/rendering dependencies.
"""
from pathlib import Path
import json, re, html, argparse, hashlib
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import markdown
from weasyprint import HTML
R=Path(__file__).resolve().parents[1]
CSS='''
:root{--ink:#20332f;--accent:#8b452e;--paper:#faf7ef;--muted:#59635e}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.65 Georgia,serif}
header{background:#20332f;color:#faf7ef;padding:2.4rem max(5vw,1.2rem)}header p{margin:0;font:13px/1.5 sans-serif;letter-spacing:.13em;text-transform:uppercase}header strong{font-size:1.5rem;font-weight:normal}
nav{padding:.8rem max(5vw,1.2rem);background:#e7e4d9;font:14px/1.9 sans-serif}nav a{margin-right:1.2rem}
main{max-width:1040px;margin:auto;padding:2rem 1.5rem 4rem}h1{font-size:2.5rem;line-height:1.15;font-weight:normal}h2{font-size:1.6rem;border-top:1px solid #bbc1b6;padding-top:1.1rem;margin-top:2.4rem;line-height:1.3}h3{font-size:1.2rem}
a{color:#8b452e;text-underline-offset:.15em}a:focus{outline:3px solid #b87023;outline-offset:3px}p{margin:.8rem 0 1.1rem}li{margin:.4rem 0}img{display:block;max-width:100%;height:auto;margin:1.3rem auto}main>p>img{max-height:850px;object-fit:contain}
table{width:100%;border-collapse:collapse;font:14px/1.5 sans-serif;margin:1.5rem 0;overflow-wrap:anywhere}th{text-align:left;background:#20332f;color:white}td,th{padding:.65rem;border:1px solid #b9c0b6;vertical-align:top}tbody tr:nth-child(even){background:#eeeae0}
.table-wrap{overflow-x:auto}.notice{background:#f1e1bb;padding:1rem 1.2rem;border-left:5px solid #8b452e;font:15px/1.5 sans-serif}.page{break-before:page}.source-image{max-height:8in;max-width:100%;object-fit:contain}footer{padding:1.3rem;text-align:center;font:13px sans-serif;color:#59635e;border-top:1px solid #bbc1b6}
@media(max-width:600px){body{font-size:17px}h1{font-size:2rem}main{padding:1rem}table{min-width:560px}nav a{display:inline-block}}
@media print{
 @page{size:letter;margin:.65in .65in .7in;@bottom-left{content:'Horner Archive · v21.0 · 17 October 2026';font:8px sans-serif;color:#59635e}@bottom-right{content:counter(page);font:8px sans-serif;color:#59635e}}
 body{background:white;font:10.4pt/1.45 Georgia,serif;color:#182b25}main{padding:0;max-width:none}header,nav,footer,.web-only{display:none}h1{font-size:27pt;margin:0 0 16pt}h2{font-size:16pt;margin-top:20pt;padding-top:10pt;break-after:avoid}h3{font-size:12pt;break-after:avoid}p{orphans:3;widows:3;margin:7pt 0}a{color:#653522;text-decoration:none}table{font:8pt/1.35 sans-serif;min-width:0!important;width:100%;table-layout:fixed}td,th{padding:5pt}thead{display:table-header-group}tr{break-inside:avoid}.table-wrap{overflow:visible}img{max-width:100%;max-height:8in;object-fit:contain}.source-image{max-height:7.1in}.notice{font:9pt/1.4 sans-serif;padding:9pt}
.reading{font-size:9.8pt;line-height:1.38}.reading h2{margin-top:16pt}.guide{font-size:9pt;line-height:1.35}.guide h2{font-size:14pt;margin-top:14pt}.guide table{break-inside:avoid;font-size:7.5pt}.guide table.sequence th:first-child{width:14%}.guide table.sequence th:nth-child(2){width:46%}.guide table.sequence th:nth-child(3){width:40%}.worksheet td{height:36pt}.writing-line{height:20pt;border-bottom:1px solid #777}table.budget th:nth-child(1){width:22%}table.budget th:nth-child(2){width:12%}table.budget th:nth-child(3){width:11%}table.budget th:nth-child(4){width:14%}table.budget th:nth-child(5){width:41%}
}
'''
def md(s): return markdown.markdown(s,extensions=['tables','attr_list','sane_lists'])
def wrap(title,body,prefix='',notice=''):
 body=re.sub(r'(<table>.*?</table>)',r'<div class="table-wrap">\1</div>',body,flags=re.S)
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+' | Horner Archive</title><style>'+CSS+'</style></head><body><a class="web-only" href="#main">Skip to content</a><header><p>Horner Civil War Archive · current reading edition · v21.0</p><strong>Records, memory, and the work of history</strong></header><nav aria-label="Main"><a href="'+prefix+'index.html">Archive</a><a href="'+prefix+'dossier.pdf">Dossier PDF</a><a href="'+prefix+'classroom/index.html">Classroom</a><a href="'+prefix+'grant-readiness/index.html">Grant packet</a><a href="'+prefix+'grant-readiness/annotated-bibliography.html">Sources</a></nav><main id="main">'+('<div class="notice">'+notice+'</div>' if notice else '')+body+'</main><footer>Daniel Bret Lingar · Source-specific rights apply · Corrections and research limits documented · 17 October 2026</footer></body></html>'
def write_page(source,target,title,prefix='',notice=''):
 text=(R/source).read_text();doc=wrap(title,md(text),prefix,notice);(R/target).write_text(doc);return doc
def pdf(doc,path,base=R):
 parsed=BeautifulSoup(doc,'html.parser')
 for a in parsed.select('a[href]'):
  href=a['href'];u=urlsplit(href)
  if u.scheme or u.netloc or not u.path:continue
  dest=(base/u.path).resolve()
  if dest.is_relative_to(R):a['href']='https://daniel-lingar.github.io/horner-archive/'+str(dest.relative_to(R))+('#'+u.fragment if u.fragment else '')
 HTML(string=str(parsed),base_url=str(base)+'/').write_pdf(R/path);print('PDF',path)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--html-only',action='store_true');a=ap.parse_args()
 core=write_page('editions/v21/current-reading.md','index.html','The Horner family in Civil War Johnson County',notice='Current concise reading edition. The earlier detailed narrative is preserved separately as superseded; unresolved evidence remains marked.')
 write_page('grant-readiness/annotated-bibliography.md','grant-readiness/annotated-bibliography.html','Annotated sources','../')
 write_page('classroom/teacher-guide.md','grant-readiness/teacher-guide.html','Teacher guide','../')
 write_page('transcript-1942.md','transcript-1942.html','Later family testimony',notice='Published family-account excerpts are not a complete authenticated original. Source S04.')
 write_page('ppan-map.md','ppan-map.html','Landscape research',notice='Parcel and coordinate identification reopened. This page is not access guidance.')
 for n in ['fiscal-sponsor-one-page','fiscal-sponsor-request-letter']:
  write_page('grant-readiness/'+n+'.md','grant-readiness/'+n+'.html','Institutional partnership draft','../')
 write_page('grant-readiness/README.md','grant-readiness/index.html','Grant readiness packet','../',notice='Discussion drafts only. No eligible applicant, signed commitments, award or approved rates are represented.')
 # Add useful HTML links to the packet alongside the editable source files.
 g=R/'grant-readiness/index.html';d=g.read_text();d=d.replace('</main>','<h2>Printable planning packet</h2><p><a href="neh-planning/discussion-packet.pdf">Combined discussion packet (not an application attachment)</a> · <a href="neh-planning/submission-gates.html">Submission gates</a> · <a href="startup-budget.html">Priced budget</a></p></main>');g.write_text(d)
 write_page('grant-readiness/startup-budget.md','grant-readiness/startup-budget.html','Planning budget','../')
 write_page('grant-readiness/neh-planning/submission-gates.md','grant-readiness/neh-planning/submission-gates.html','Submission gates','../../')
 for n in ['teacher-guide','student-worksheet','evaluation-form']:
  write_page('classroom/'+n+'.md','classroom/'+n+'.html',n.replace('-',' ').title(),'../')
 classroom_intro='''# Classroom materials

**v21.0 | Grades 9–12 and adult learners | Unpiloted prototype**

[Print source pack with source sheets, worksheet, teacher key and evaluation form](source-pack.pdf).

[Teacher guide and answer key](teacher-guide.html) · [Student worksheet](student-worksheet.html) · [Pilot evaluation form](evaluation-form.html)

The pack works offline. It includes a corrected census image and patent facsimile, reading aids, and short attributed summaries of memorial and family testimony. It avoids graphic injury descriptions. A land/census alternative supports the same learning goals. No classroom results, state standards certification or special grant page requirement are claimed.
'''
 (R/'classroom/index.html').write_text(wrap('Classroom materials',md(classroom_intro),'../'))
 # Historic page: prominently mark it and disable the old gallery/map rendering.
 old=R/'superseded-v20.html';t=old.read_text()
 if 'SUPERSEDED v20' not in t:
  t=t.replace('<body>','<body><aside style="padding:25px;background:#ffe6a6;color:#171717;border:5px solid #8b452e"><strong>SUPERSEDED v20: research history, not the current reading edition.</strong> This page contains known incorrect images, transcriptions and unsupported claims. <a href="index.html">Read v21 and its correction register.</a> The old 57-page PDF is preserved in Git history, not at the current dossier link.</aside>')
  t=re.sub(r'<img\b[^>]*field-docs/[^>]*>', '<p>[Mislabeled census image withdrawn from the former cemetery gallery.]</p>',t)
  t=re.sub(r'<script\b[^>]*>.*?</script>','',t,flags=re.S)
  t=t.replace('<head>','<head><meta name="robots" content="noindex">');old.write_text(t)
 if a.html_only:return
 # Keep full facsimiles in a labeled appendix, avoiding isolated text between full-page images.
 soup=BeautifulSoup(core,'html.parser');soup.main['class']='reading';appendix=[]
 for image in soup.select('main p > img'):
  image_src=image.get('src');label=image.get('alt','Record image')
  appendix.append('<section class="page"><h2>'+html.escape(label)+'</h2><img class="source-image" src="'+image_src+'" alt="'+html.escape(label)+'"></section>')
  image.parent.replace_with(BeautifulSoup('<p>Full record image appears in the source appendix.</p>','html.parser'))
 soup.main.append(BeautifulSoup(''.join(appendix),'html.parser'))
 pdf(str(soup),'dossier.pdf')
 # Put sources on their own pages; image-only pages follow reading aids.
 atext='''# Source sheets

**Reading records, remembering violence | v21.0**

Use these sheets with the student worksheet. A historical record establishes some claims and leaves others open. Page-image readings may be provisional. You are not required to infer motives, name perpetrators or disclose family experiences.

## A · 1860 census, Spencer Horner household (S01)

Government population schedule; Mulberry Township, Johnson County, Arkansas; Clarksville post office; heading 20 June 1860. Dwelling 698, family 699, lines 1–7. Extracted unaltered from page 1 of the owner-supplied “1860 census” export. Original series/roll and provider image identifier remain to be reconciled. The page heading has differing handwritten page numbers and stamped 1029.

Reading aid: Spencer Horner, 52, farmer, Tennessee; real estate $1,500, personal estate $1,500. Permelia is listed on line 2. Other names and ages are provisional; the full cautious transcription is in the source catalog. This schedule does not explicitly state household relationships. It does not establish motives, cash hidden, or acreage. The next page is the full record image, so you can check rather than rely only on this aid.

## B · Federal land patent (S02)

Patent 19B, 1 April 1857, Fayetteville Land Office; repository image, original accession pending. Spencer Horner appears as assignee of Co-cha-tubbee, representative of Canne Chubbee, deceased. Total 160 acres: SE 1/4 NE 1/4 and NW 1/4 SE 1/4 of section 19; NW 1/4 NW 1/4 and SE 1/4 NW 1/4 of section 22; T12N R24W. It does not establish Horner ancestry, a transfer price, an attacker’s motive, or a modern house site. Facsimile follows the census page.
'''
 sheet=md(atext)+f'<section class="page"><h2>A · Full census page</h2><p>Source S01 · top household, lines 1–7 · Reading aid on preceding sheet.</p><img class="source-image" src="{json.loads((R/"sources/reviewed/source-catalog.json").read_text())["sources"][0]["path"]}" alt="1860 Mulberry census page; Spencer Horner household appears at the top"></section>'
 sheet+='<section class="page"><h2>B · Patent 19B</h2><p>Source S02 · 1 April 1857 · Read the tract descriptions, not a modern map.</p><img class="source-image" src="Patent_19B_AR2690___426.jpg" alt="Federal patent naming Spencer Horner as assignee for four tracts totaling 160 acres"></section>'
 sheet+='<section class="page">'+md('''# C and D · Commemoration and memory

## C · William Riley Horner marker (S03)

Reading of the visible repository photograph: William Riley’s marker gives a death date of **10 August 1864** and says he was killed by parties known to his family. The installation date, photographer, photograph date and reproduction permission are unknown. The photograph is not reproduced in this pack. This is a reading aid, not a facsimile or certified diplomatic transcription. The repository image can be consulted separately if appropriate.

The wording records a memorial accusation. It does not name the killers or establish whether officials investigated. It does not prove a 2 August attack date. What could a court docket, inquest, or dated military record add?

## D · Family account attributed to 1942 (S04)

Attributed paraphrase of published excerpts: the account describes Spencer surrendering and being shot, William receiving a head wound, and a later reprisal group associated with Dr. John Turner Horner. It reports seventeen of twenty attackers killed in reprisals. The published excerpt describes Jess Wilson holding the group’s horses.

These are statements attributed to a later family account. The complete manuscript, date/authorship and transmission chain have not been verified. The casualty count, identities and chronology are not independently corroborated here. This short paraphrase avoids graphic detail and is not presented as the original transcript. What would you need before treating two retellings as independent testimony?

## Comparison prompt

Mark the event date, source date and unknown date for each sheet. Explain which claim each source can establish. Compare an attributed memory to an administrative record without assuming either answers every question.
''')+'</section>'
 for n in ['student-worksheet','teacher-guide','evaluation-form']:
  body=md((R/('classroom/'+n+'.md')).read_text())
  if n=='teacher-guide':body=body.replace('<table>','<table class="sequence">',1)
  if n=='student-worksheet':
   body=body.replace('<h2>3. Write a museum label</h2>','<h2 class="page">3. Write a museum label</h2>')
   body=re.sub(r'<p>_{20,}</p>','<div class="writing-line"></div>',body)
   body=body.replace('<h2>Exit response</h2>','<div class="writing-line"></div>'*6+'<h2>Exit response</h2>')
  sheet+='<section class="'+('page guide' if n=='teacher-guide' else 'page worksheet' if n=='student-worksheet' else '')+'">'+body+'</section>'
 pdf(wrap('Classroom source pack',sheet),'classroom/source-pack.pdf')
 N=R/'grant-readiness/neh-planning'
 docs={n:md((N/(n+'.md')).read_text()) for n in ['narrative','workplan','bibliography','submission-gates','commitment-templates']}
 for n in ['narrative','workplan','bibliography']:
  pdf(wrap(n.title(),docs[n],'../../'),'grant-readiness/neh-planning/'+n+'.pdf',N)
 budget=md((R/'grant-readiness/startup-budget.md').read_text()).replace('<table>','<table class="budget">',1)
 pdf(wrap('Budget justification',budget,'../../'),'grant-readiness/neh-planning/budget-justification.pdf',R/'grant-readiness')
 combined=md('# Exhibition planning discussion packet\n\n**17 October 2026 | v21.0 | Not a submission package**\n\nThe following pages are prepared drafts. Actual eligible institution, appointments, signed letters, original-source identifiers, rights and approved costs remain required. Do not attach this combined file to an NEH application.')
 for body in [docs['submission-gates'],docs['narrative'],docs['workplan'],docs['bibliography'],budget,docs['commitment-templates']]:combined+='<section class="page">'+body+'</section>'
 pdf(wrap('Institutional planning discussion packet',combined,'../../'),'grant-readiness/neh-planning/discussion-packet.pdf',N)
 # The legacy analysis URL returns a withdrawal notice instead of the unsupported old finding.
 pdf(wrap('Census analysis superseded',md('# Earlier census analysis withdrawn\n\n**17 October 2026 | v21.0**\n\nThe earlier Floyd 981–982 analysis was not supported by its displayed image. Its household identification and valuation comparison are withdrawn. A Spencer/Permelia entry has now been recovered under Mulberry Township. See the current dossier, S01 source catalog, and sources/reviewed/census-transcription.md. William Riley’s household and original census metadata remain under review. The original analysis remains in Git history.')),'sources/1860-floyd-township-census-analysis.pdf')
 catalog=R/'sources/reviewed/source-catalog.json';data=json.loads(catalog.read_text())
 for s in data['sources']:
  p=R/s['path']
  if p.is_file():s['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
 catalog.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()
