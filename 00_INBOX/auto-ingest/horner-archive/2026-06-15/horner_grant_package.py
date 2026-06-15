from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 HRFlowable, PageBreak, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = "/mnt/user-data/outputs/horner_archive_grant_package.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1*inch, rightMargin=1*inch,
    topMargin=1*inch, bottomMargin=1*inch,
    title="The Killing of John Spencer Horner — Grant Package",
    author="Daniel Lingar",
    subject="Johnson County Civil War Archive — Grant Readiness Document"
)

styles = getSampleStyleSheet()

# Custom styles
dark = colors.HexColor("#1a0e08")
accent = colors.HexColor("#8b1a1a")
mid = colors.HexColor("#5a3a20")
light = colors.HexColor("#c8b99a")
muted = colors.HexColor("#5a5a5a")

cover_title = ParagraphStyle("cover_title", parent=styles["Normal"],
    fontSize=22, leading=28, textColor=dark, spaceAfter=6, alignment=TA_CENTER, fontName="Times-Bold")
cover_sub = ParagraphStyle("cover_sub", parent=styles["Normal"],
    fontSize=13, leading=18, textColor=mid, spaceAfter=4, alignment=TA_CENTER, fontName="Times-Italic")
cover_meta = ParagraphStyle("cover_meta", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=muted, spaceAfter=3, alignment=TA_CENTER)

section_label = ParagraphStyle("section_label", parent=styles["Normal"],
    fontSize=8, leading=12, textColor=accent, spaceBefore=24, spaceAfter=2,
    fontName="Helvetica-Bold", letterSpacing=2)
h1 = ParagraphStyle("h1", parent=styles["Normal"],
    fontSize=16, leading=20, textColor=dark, spaceBefore=4, spaceAfter=8,
    fontName="Times-Bold", borderPadding=(0,0,4,0))
h2 = ParagraphStyle("h2", parent=styles["Normal"],
    fontSize=13, leading=17, textColor=dark, spaceBefore=14, spaceAfter=4,
    fontName="Times-Bold")
h3 = ParagraphStyle("h3", parent=styles["Normal"],
    fontSize=11, leading=15, textColor=mid, spaceBefore=10, spaceAfter=3,
    fontName="Helvetica-Bold")
body = ParagraphStyle("body", parent=styles["Normal"],
    fontSize=10.5, leading=16, textColor=colors.HexColor("#1a1a1a"),
    spaceAfter=7, alignment=TA_JUSTIFY, fontName="Times-Roman")
body_b = ParagraphStyle("body_b", parent=body, fontName="Times-Bold")
bullet = ParagraphStyle("bullet", parent=body,
    leftIndent=18, firstLineIndent=-10, spaceAfter=4)
note = ParagraphStyle("note", parent=body,
    fontSize=9.5, textColor=muted, fontName="Times-Italic", spaceAfter=5)
box_text = ParagraphStyle("box_text", parent=body,
    fontSize=10, leftIndent=12, rightIndent=12, spaceAfter=4)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=light, spaceAfter=6, spaceBefore=6)

def accent_rule():
    return HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=8, spaceBefore=2)

story = []

# ── COVER PAGE ──────────────────────────────────────────────────────────────
story.append(Spacer(1, 1.2*inch))
story.append(Paragraph("THE KILLING OF JOHN SPENCER HORNER", cover_title))
story.append(Paragraph("Johnson County Civil War Archive", cover_sub))
story.append(Spacer(1, 0.15*inch))
story.append(accent_rule())
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("Grant Readiness Package", ParagraphStyle("grt", parent=cover_sub,
    fontSize=15, textColor=accent, fontName="Times-BoldItalic")))
story.append(Spacer(1, 0.5*inch))

cover_items = [
    ("Researcher", "Daniel Bret Lingar"),
    ("Location", "Clarksville, Johnson County, Arkansas"),
    ("Contact", "lingardaniel1@gmail.com"),
    ("Archive URL", "https://daniel-lingar.github.io/horner-archive/"),
    ("Dossier Version", "19.0 · June 2026"),
    ("Subject", "Guerrilla violence, Civil War Arkansas, Choctaw land dispossession"),
    ("Period", "1830–1866 (primary focus: August 2, 1864)"),
]
for label, val in cover_items:
    story.append(Paragraph(f"<b>{label}:</b>  {val}", ParagraphStyle("ci", parent=body,
        spaceAfter=3, alignment=TA_LEFT)))

story.append(Spacer(1, 0.5*inch))
story.append(rule())
story.append(Paragraph(
    "This document contains: project overview · interpretive thesis · evidentiary summary · "
    "primary sources inventory · open questions register · NARA retrieval queue · "
    "grant narrative draft · institutional affiliation guidance · budget framework",
    note))
story.append(PageBreak())

# ── SECTION 1: PROJECT OVERVIEW ─────────────────────────────────────────────
story.append(Paragraph("§ 01", section_label))
story.append(Paragraph("Project Overview", h1))
story.append(accent_rule())

story.append(Paragraph(
    "On August 2, 1864, a group of approximately twenty Confederate-aligned bushwhackers rode "
    "to the homestead of John Spencer Horner in Floyd Township, Johnson County, Arkansas. They "
    "shot Spencer where he stood in his potato patch, beat his son William Riley Horner with "
    "pistols and left him for dead, ransacked the farm for hidden gold, and rode away. Eight days "
    "later William died of his wounds in a cave on the mountainside where his wife had carried him. "
    "No one was ever charged.", body))
story.append(Paragraph(
    "The men who did it were known to the family. The county sheriff — John Fry Hill — was "
    "simultaneously a colonel in the Confederate Army, commanding a regiment whose Johnson County "
    "companies overlapped with the social network of the attackers. His regiment was documented "
    "across the river in Dardanelle the following day. He never investigated.", body))
story.append(Paragraph(
    "Spencer's son, Dr. John Turner Horner, led a reprisal squad that allegedly killed seventeen "
    "of the twenty men responsible. The official record is entirely silent on this — which is "
    "itself a form of evidence about what the community chose not to see.", body))
story.append(Paragraph(
    "This archive documents that case. It is built on primary sources: federal land patents, "
    "military service records, pension files, a Confederate pension record, an amnesty petition, "
    "GPS coordinates, and a 1942 family oral history transcript. The researcher is a direct "
    "descendant — fifth great-grandson of Spencer Horner, second great-grandson of John Samuel "
    "Acord, the seven-year-old boy who witnessed the murder.", body))
story.append(Spacer(1, 0.1*inch))

# ── SECTION 2: INTERPRETIVE THESIS ──────────────────────────────────────────
story.append(Paragraph("§ 02", section_label))
story.append(Paragraph("Interpretive Thesis", h1))
story.append(accent_rule())

story.append(Paragraph(
    "The killing of Spencer Horner is a documented case study in three intersecting "
    "histories that are rarely examined together at the local level:", body))

theses = [
    ("Civil War guerrilla violence in the Arkansas Ozarks",
     "Floyd Township in 1864 was not a battlefield — it was an ungoverned space where "
     "the absence of institutional authority enabled targeted political murder. The Horner "
     "case puts a specific family, a specific date, and a specific social network on a pattern "
     "of violence that the historical record usually describes only in aggregate."),
    ("The failure of Reconstruction justice at the county level",
     "The sheriff who did not investigate was also a Confederate colonel. The men who killed "
     "Spencer were never charged. The reprisal was extra-judicial and apparently successful — "
     "seventeen killings that left no official record. The archive documents how complete "
     "impunity operated in one Arkansas county in 1864–1866."),
    ("Choctaw land dispossession and the secondary scrip market",
     "Spencer Horner's title to the land he died for derived from a Choctaw child's "
     "displacement under the Treaty of Dancing Rabbit Creek. Certificate 19B traces a 160-acre "
     "child allotment from Mississippi through the speculator market to a Union-aligned farmer "
     "in the Arkansas Ozarks — a chain that connects Indian removal in 1830 to Civil War "
     "violence in 1864 on the same parcel of ground."),
]
for title, text in theses:
    story.append(Paragraph(f"<b>{title}.</b>  {text}", bullet))

story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(
    "<b>One-sentence grant thesis:</b>  The killing of John Spencer Horner on August 2, 1864 "
    "offers a fully documented, multi-generational case study — anchored in primary sources and "
    "direct researcher descent — of how Civil War guerrilla violence, the failure of Reconstruction "
    "justice, and Choctaw land dispossession converged on a single 160-acre farm in the Arkansas Ozarks.",
    ParagraphStyle("thesis_box", parent=body,
        leftIndent=18, rightIndent=18, spaceBefore=8, spaceAfter=8,
        borderPadding=10, backColor=colors.HexColor("#f0ebe0"),
        borderWidth=0, leading=17)))
story.append(PageBreak())

# ── SECTION 3: EVIDENTIARY SUMMARY ──────────────────────────────────────────
story.append(Paragraph("§ 03", section_label))
story.append(Paragraph("Evidentiary Summary", h1))
story.append(accent_rule())

story.append(Paragraph(
    "The archive is built on primary sources. The following table summarizes the documentary "
    "base and its current status.", body))
story.append(Spacer(1, 0.1*inch))

source_data = [
    ["Document", "Date", "Status"],
    ["Federal Land Patent 19B (Choctaw scrip) — BLM GLO AR2690__.426", "April 1, 1857", "Imaged"],
    ["Federal Land Patent 4706 (cash entry) — Fayetteville Land Office", "1848", "Documented"],
    ["Northern Neck Proprietary Grant — George Horner / George Washington survey", "March 9, 1752", "Documented"],
    ["CMSR — William Riley Horner, Co. K, 2nd Arkansas Infantry (US)", "1864", "Reviewed"],
    ["CMSR — Francis Marion Acord, Co. K, 2nd Arkansas Infantry (US)", "1864", "Reviewed"],
    ["CMSR — John Fry Hill, 7th Arkansas Cavalry (CSA)", "1864", "Reviewed"],
    ["CMSR — Hiram Boen, Co. E, 2nd Arkansas Infantry (US)", "1864", "Reviewed"],
    ["CMSR — James Mitchell Wilson, 2nd Arkansas Cavalry (CSA)", "1864", "Reviewed"],
    ["John Fry Hill Amnesty Petition to President Andrew Johnson", "1866", "Reviewed"],
    ["Widow's Pension — Permelia Turner Horner", "Aug 17, 1865", "Reviewed"],
    ["Minor Pension — Dr. John Turner Horner (Acord orphans)", "Sept 7, 1865", "Reviewed"],
    ["Rejected Pension — Dr. John Turner Horner, RG 15 App. 1,143,763", "1894", "NARA — not yet retrieved"],
    ["Arkansas Ex-Confederate Pension Record — Henry Stewart", "1910–1915", "Imaged"],
    ["1942 Horner Family Oral History Transcript (Eva Horner)", "1942", "Held by researcher"],
    ["Dewberry GPS Site Survey — Moore Cemetery, homestead, cave", "2003", "GPS-verified"],
    ["1850 Federal Census — Johnson County, Mulberry Township", "1850", "Reviewed"],
    ["1860 Federal Census — Johnson County, Floyd Township (partial)", "1860", "Reviewed (partial)"],
    ["Goodspeed's History of Barry County, MO — Hill biography", "1888", "Reviewed"],
    ["Colton's Railroad & Township Map of Arkansas", "1860", "Documented"],
]

col_widths = [3.2*inch, 1.1*inch, 1.7*inch]
t = Table(source_data, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), dark),
    ("TEXTCOLOR", (0,0), (-1,0), colors.HexColor("#e8d8b8")),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 8.5),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 8),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f8f5ef"), colors.HexColor("#f0ebe0")]),
    ("GRID", (0,0), (-1,-1), 0.3, light),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TEXTCOLOR", (2,1), (2,-1), muted),
]))
story.append(t)
story.append(PageBreak())

# ── SECTION 4: OPEN QUESTIONS ────────────────────────────────────────────────
story.append(Paragraph("§ 04", section_label))
story.append(Paragraph("Open Questions Register", h1))
story.append(accent_rule())
story.append(Paragraph(
    "Questions are classified by what action is required to close them. "
    "Priority items are marked.", body))

oqs = [
    ("CLOSE THIS WEEK — online retrieval", [
        ("OQ-21", "Spencer Horner 1860 census property values",
         "Page 981–982, Floyd Township, Johnson County. Ancestry or FamilySearch. "
         "Real estate and personal property columns are on the same line as the household head. "
         "Closes the question of what Spencer was financially worth in 1864."),
        ("OQ-22", "GLO field notes T12N R24W",
         "glorecords.blm.gov or history.cosl.org → Louisiana Purchase → Transcribed Field Notes → T12N R24W. "
         "Field notes describe terrain, timber, and water features section by section — may independently "
         "document the bluff and cave corridor."),
        ("OQ-12", "William Gordon Acord CMSR",
         "NARA M317, card #44903963. Check Fold3 first. Resolves the unit designation conflict "
         "between the tombstone ('CO K 2ND AR INF VOL') and claimed Confederate service."),
        ("OQ-13", "Henry Stewart CMSR",
         "NARA M317. Check Fold3 first. Would confirm whether Stewart served in a Johnson County "
         "Confederate command (10th Arkansas Militia or 7th Arkansas Cavalry)."),
        ("OQ-18", "Co-cha-tubbee on Armstrong Roll",
         "Armstrong Roll (1831) digitized on Ancestry and FamilySearch. Search phonetic variants. "
         "If found, may show family structure explaining the 160-acre child certificate and identify "
         "the parent household claim from which 19B derives."),
    ]),
    ("NARA ORDER — paid, weeks turnaround", [
        ("OQ-15 ★ PRIORITY", "John Turner Horner rejected pension file",
         "RG 15, Application 1,143,763. Filed March 2, 1894; rejected October 5, 1894. Not digitized. "
         "Expected to contain sworn service statements and witness affidavits — the most important "
         "unretrieved document in the archive. NARA request email drafted; send to inquire@nara.gov."),
        ("OQ-16", "Special Order Bo-276-66 — Hiram Boen desertion clearance",
         "NARA RG 94. The War Department cleared Boen's desertion charge in 1866 without stating a reason. "
         "The order itself may explain why he was absent during the murders."),
        ("OQ-17 + OQ-19", "Fayetteville Land Office register + GLO case file for 19B",
         "NARA RG 49. The Land Office register would document Spencer's filing date, witnesses, and "
         "residence. The case file may contain his original application and the Choctaw scrip certificate text. "
         "Bundle with OQ-15 order to save turnaround time."),
    ]),
    ("ARCHIVE / LIBRARY — Arkansas History Commission", [
        ("OQ-23", "Masonic lodge records — Stewart family and Lodges #272 and #118",
         "Yale Cemetery records confirm Thomas Stewart's tombstone was erected by Mulberry Lodge #272; "
         "he was a member of Springhill Lodge #118. Grand Lodge records burned 1864 and 1876. "
         "Any surviving local records would be at the Arkansas History Commission, Little Rock."),
        ("OQ-5", "Dr. John Turner Horner's 10th Arkansas Militia enrollment",
         "His 27-day Confederate muster (Feb–Mar 1862) is confirmed. The 10th Arkansas Militia "
         "muster rolls at the Arkansas State Archives may document this original enrollment."),
    ]),
    ("LONG-TERM — chain completion", [
        ("OQ-24", "Parent Choctaw household for Certificate 19B",
         "Certificate 19B (160 acres) indicates Canne Chubbee was an under-ten child in 1831. "
         "The head-of-household claimant who registered with agent William Ward has not been identified. "
         "Sources: NARA RG 75, Ward's Register (1831), and 1842–1845 commission records."),
        ("OQ-20", "Post-1864 deed transfer for the Floyd Township 160 acres",
         "Permelia sold the farm for a horse and wagon after the murders. The actual deed — buyer, "
         "date, price — has not been located. Johnson County deed records 1865–1870 not yet examined."),
    ]),
]

for category, items in oqs:
    story.append(Paragraph(category, h3))
    for oq_id, title, desc in items:
        story.append(Paragraph(f"<b>{oq_id} — {title}</b>", ParagraphStyle("oqt", parent=body,
            spaceAfter=1, leftIndent=12)))
        story.append(Paragraph(desc, ParagraphStyle("oqd", parent=body,
            leftIndent=12, fontSize=9.5, textColor=muted, spaceAfter=7)))
    story.append(Spacer(1, 0.05*inch))

story.append(PageBreak())

# ── SECTION 5: GRANT NARRATIVE ───────────────────────────────────────────────
story.append(Paragraph("§ 05", section_label))
story.append(Paragraph("Grant Narrative Draft", h1))
story.append(accent_rule())
story.append(Paragraph(
    "The following narrative is suitable for adaptation to NEH Preservation and Access grants, "
    "Arkansas Humanities Council project grants, or local history foundation applications. "
    "Adjust word count and emphasis to match the specific funder's priorities.", note))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Project Description", h2))
story.append(Paragraph(
    "On the morning of August 2, 1864, a group of approximately twenty Confederate-aligned "
    "bushwhackers rode to the homestead of John Spencer Horner in Floyd Township, Johnson County, "
    "Arkansas. They shot him in his potato patch, beat his son near to death, and ransacked the "
    "farm for hidden gold. Eight days later the son died in a cave. No one was ever charged. The "
    "county sheriff was simultaneously a Confederate colonel whose regiment had been camped across "
    "the river the previous day.", body))
story.append(Paragraph(
    "The Killing of John Spencer Horner is a documentary archive built on primary sources — "
    "federal land patents, compiled military service records, pension files, a Confederate pension "
    "record, an amnesty petition, GPS-verified site coordinates, and a 1942 family oral history "
    "transcript — that reconstructs this case with a level of evidentiary specificity rarely "
    "achieved for ordinary civilian violence during the Civil War.", body))
story.append(Paragraph(
    "The project is the work of Daniel Lingar of Clarksville, Arkansas, who is a direct descendant "
    "of the family. He is the fifth great-grandson of John Spencer Horner and the second "
    "great-grandson of John Samuel Acord — the seven-year-old boy who was present when his "
    "grandfather was shot. The archive exists because that child survived and because someone "
    "was eventually willing to write it down.", body))

story.append(Paragraph("Significance", h2))
story.append(Paragraph(
    "The archive addresses three intersecting historical questions that are typically examined "
    "separately and rarely at the granular local level:", body))
story.append(Paragraph(
    "<b>Guerrilla violence in the Arkansas Ozarks.</b>  The Horner case is among the most "
    "thoroughly documented instances of civilian murder by Confederate irregulars in northwest "
    "Arkansas. It names perpetrators, victims, witnesses, a site, a date, and a motive — and "
    "it documents the subsequent extra-judicial reprisal that killed seventeen of the twenty men "
    "responsible, leaving no official record of either the crime or its consequence.", bullet))
story.append(Paragraph(
    "<b>The failure of Reconstruction justice.</b>  Sheriff John Fry Hill was a Confederate "
    "colonel. His regiment's Johnson County companies — five of twelve — drew from the same "
    "social network as the attackers. He made no investigation. After the war he was re-elected "
    "sheriff and served in the Arkansas Senate. The archive documents how complete impunity "
    "operated in one county in 1864–1866.", bullet))
story.append(Paragraph(
    "<b>Choctaw land dispossession and the secondary scrip market.</b>  Spencer Horner's title "
    "to the land he died for derived from a Choctaw child's allotment under the Treaty of Dancing "
    "Rabbit Creek (1830). Certificate 19B — now imaged — names Spencer as assignee of "
    "Co-cha-tubbee, representative of Canne Chubbee, deceased. The 160-acre allotment indicates "
    "Canne Chubbee was a child under ten in 1831. Spencer was almost certainly a speculator "
    "intermediary, not a Choctaw kinsman — a participant in the secondary market through which "
    "Choctaw removal entitlements became white Arkansas farmland. Indian removal in 1830 and "
    "Civil War murder in 1864 are connected by the same 160 acres.", bullet))

story.append(Paragraph("Methods and Deliverables", h2))
story.append(Paragraph(
    "The archive is currently published as a public website at "
    "daniel-lingar.github.io/horner-archive. It is a working document, updated as new "
    "research is completed. The current version (19.0, June 2026) integrates the Patent 19B "
    "image, expanded Choctaw scrip analysis, the 7th Arkansas Cavalry company composition, "
    "the Masonic-Stewart connection, and twenty-four open research questions with specific "
    "retrieval paths.", body))
story.append(Paragraph(
    "Proposed grant deliverables include: (1) retrieval of the John Turner Horner rejected "
    "pension file (NARA RG 15, the highest-priority unretrieved document); (2) retrieval of "
    "the Fayetteville Land Office register entry and GLO case file for Patent 19B (NARA RG 49); "
    "(3) first-pass search of the Armstrong Roll and NARA RG 75 for Co-cha-tubbee and the "
    "parent Choctaw household; (4) a revised and expanded public archive incorporating all "
    "new findings; and (5) a research paper suitable for submission to the Arkansas Historical "
    "Quarterly or a comparable peer-reviewed publication.", body))

story.append(Paragraph("Researcher Qualifications", h2))
story.append(Paragraph(
    "Daniel Lingar is a self-trained genealogical researcher with direct descent from the "
    "Horner and Acord families of Johnson County, Arkansas. He has independently located, "
    "retrieved, and analyzed federal land patents, compiled military service records, pension "
    "files, census records, and Confederate pension records. The archive represents several "
    "years of sustained primary source research on a single documented event. He resides in "
    "Clarksville, Arkansas — the county seat of Johnson County, eight miles from the murder site.", body))
story.append(PageBreak())

# ── SECTION 6: INSTITUTIONAL AFFILIATION ────────────────────────────────────
story.append(Paragraph("§ 06", section_label))
story.append(Paragraph("Institutional Affiliation", h1))
story.append(accent_rule())
story.append(Paragraph(
    "Most grants from NEH, the Arkansas Humanities Council, and private foundations require "
    "an institutional host or fiscal agent. As an independent researcher, Daniel Lingar will "
    "need to partner with a qualifying institution before applying to most funders. The following "
    "are the strongest candidates.", body))

institutions = [
    ("Butler Center for Arkansas Studies",
     "Central Arkansas Library System, Little Rock",
     "The Butler Center is the state's primary repository for Arkansas history and regularly "
     "partners with independent researchers. Their mission directly aligns with the Horner "
     "archive's focus on Civil War Arkansas. Contact: butlercenter.org"),
    ("Arkansas Historical Association",
     "University of Arkansas, Fayetteville",
     "The AHA publishes the Arkansas Historical Quarterly and supports local history research. "
     "A relationship here would also open a publication pathway for the research paper deliverable."),
    ("Johnson County Historical Society & Heritage Center",
     "Clarksville, Arkansas",
     "The local society is the most natural fit given the archive's geographic and community focus. "
     "A local institutional home strengthens the case for Arkansas Humanities Council funding "
     "specifically, which prioritizes community-based projects."),
    ("Arkansas History Commission",
     "Little Rock (State Archives)",
     "The Commission holds the state's archival collections and may be able to facilitate access "
     "to records relevant to the open questions, including Masonic lodge records and Arkansas "
     "militia muster rolls."),
]

for name, location, desc in institutions:
    story.append(Paragraph(f"<b>{name}</b>", ParagraphStyle("iname", parent=body,
        spaceAfter=1, spaceBefore=8)))
    story.append(Paragraph(location, ParagraphStyle("iloc", parent=body,
        fontSize=9.5, textColor=muted, spaceAfter=3, fontName="Times-Italic")))
    story.append(Paragraph(desc, ParagraphStyle("idesc", parent=body,
        leftIndent=12, fontSize=9.5, spaceAfter=4)))

story.append(PageBreak())

# ── SECTION 7: BUDGET FRAMEWORK ─────────────────────────────────────────────
story.append(Paragraph("§ 07", section_label))
story.append(Paragraph("Budget Framework", h1))
story.append(accent_rule())
story.append(Paragraph(
    "The following is a framework for a modest grant application targeting NARA retrieval, "
    "digitization, and publication. Adjust line items to match specific funder guidelines.", body))

budget_data = [
    ["Line Item", "Estimated Cost", "Notes"],
    ["NARA record retrieval — RG 15 (Horner pension file)", "$25–75", "Per-page copy fees; ~20–50 pages expected"],
    ["NARA record retrieval — RG 49 (Land Office register + GLO case file)", "$50–150", "Two record groups; bundle request"],
    ["NARA record retrieval — RG 94 (Special Order Bo-276-66)", "$15–40", "Single order document"],
    ["Armstrong Roll / RG 75 research — subscription or archive visit", "$0–200", "Ancestry subscription or research trip to NARA"],
    ["Travel — NARA College Park (if physical retrieval required)", "$400–800", "Flights + 1–2 nights; or hire a NARA researcher ($50–75/hr)"],
    ["Fold3 subscription — CMSR retrieval OQ-12, OQ-13", "$0–50", "Annual subscription; may already have access"],
    ["Website hosting and domain (ongoing)", "$0–50/yr", "Currently GitHub Pages (free)"],
    ["Publication preparation — Arkansas Historical Quarterly submission", "$0", "Open submission; no fee"],
    ["Researcher time (if compensated)", "$3,000–8,000", "Based on funder norms; some grants exclude independent researchers"],
    ["Indirect / overhead (institutional)", "10–15%", "Varies by host institution"],
    ["TOTAL (excluding researcher time)", "~$550–1,350", ""],
]

col_widths_b = [3.0*inch, 1.2*inch, 1.8*inch]
bt = Table(budget_data, colWidths=col_widths_b, repeatRows=1)
bt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), dark),
    ("TEXTCOLOR", (0,0), (-1,0), colors.HexColor("#e8d8b8")),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 8.5),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 8),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f8f5ef"), colors.HexColor("#f0ebe0")]),
    ("GRID", (0,0), (-1,-1), 0.3, light),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("FONTNAME", (0,-1), (-1,-1), "Helvetica-Bold"),
    ("TEXTCOLOR", (0,-1), (-1,-1), dark),
]))
story.append(bt)
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph(
    "For a small grant (&lt;$5,000) through the Arkansas Humanities Council or a local foundation, "
    "the NARA retrieval costs plus researcher time (if allowed) and a modest digitization budget "
    "is a defensible and fundable scope. The archive's existing evidentiary base is unusually "
    "strong and reduces the risk profile of the project for funders.", note))
story.append(PageBreak())

# ── SECTION 8: GRANT TARGETS ─────────────────────────────────────────────────
story.append(Paragraph("§ 08", section_label))
story.append(Paragraph("Recommended Grant Targets", h1))
story.append(accent_rule())

funders = [
    ("Arkansas Humanities Council",
     "ahc.edu — annual project grants, typically $1,000–$10,000",
     "Best fit. AHC specifically funds community-based Arkansas history projects. "
     "Independent researchers can apply with an institutional co-applicant. Deadlines vary; "
     "check current cycle. The Horner archive's community connection (Johnson County, "
     "Clarksville-based researcher, documented local history) is a strong match."),
    ("NEH Preservation and Access — Digitizing Hidden Collections",
     "neh.gov — grants typically $50,000–$350,000; requires institutional host",
     "Longer-term target. Would require partnership with the Butler Center or Arkansas "
     "History Commission. Scope would need to expand beyond a single family archive to a "
     "broader collection of Johnson County Civil War materials."),
    ("NEH Public Scholar Program",
     "neh.gov — $60,000 stipend for public-facing research; requires institutional affiliation",
     "Competitive but well-suited to the archive's combination of rigorous primary source "
     "work and public accessibility. The interpretive framework (three intersecting histories) "
     "is exactly the kind of argument the program funds."),
    ("Daughters of the American Revolution — Local Chapter Grants",
     "dar.org — small grants for genealogical and historical preservation",
     "The Northern Neck Proprietary Grant (1752) and William Horner Sr.'s Revolutionary War "
     "service (DAR #462142) establish DAR eligibility. Local chapter grants are small but "
     "achievable without institutional affiliation."),
    ("Arkansas State Library — LSTA Grants",
     "library.arkansas.gov — Library Services and Technology Act grants",
     "If the archive is formally deposited with a library system, LSTA digitization grants "
     "become available. The Butler Center or Johnson County Public Library would be the host."),
]

for name, details, desc in funders:
    story.append(Paragraph(f"<b>{name}</b>", ParagraphStyle("fname", parent=body,
        spaceAfter=1, spaceBefore=10)))
    story.append(Paragraph(details, ParagraphStyle("fdet", parent=body,
        fontSize=9, textColor=muted, spaceAfter=3, fontName="Helvetica-Oblique")))
    story.append(Paragraph(desc, ParagraphStyle("fdesc", parent=body,
        leftIndent=12, fontSize=9.5, spaceAfter=4)))

story.append(PageBreak())

# ── SECTION 9: IMMEDIATE NEXT STEPS ─────────────────────────────────────────
story.append(Paragraph("§ 09", section_label))
story.append(Paragraph("Immediate Next Steps", h1))
story.append(accent_rule())

steps = [
    ("This week", [
        "Send the NARA request email (drafted) to inquire@nara.gov for RG 15, Application 1,143,763.",
        "Pull 1860 census image pages 981–982, Floyd Township, Johnson County on Ancestry or FamilySearch. "
        "Read the real estate and personal property values for W.R. Horne and John T. Homer.",
        "Go to glorecords.blm.gov or history.cosl.org and retrieve the field notes for T12N R24W.",
        "Search Fold3 for Henry Stewart and William Gordon Acord CMSRs before ordering physical copies.",
        "Search Armstrong Roll on Ancestry or FamilySearch for Co-cha-tubbee (and phonetic variants).",
    ]),
    ("Next 30 days", [
        "Contact the Johnson County Historical Society in Clarksville and the Butler Center in Little Rock "
        "about potential institutional partnership for grant applications.",
        "Review the Arkansas Humanities Council's current grant cycle and deadlines at ahc.edu.",
        "Bundle NARA orders for RG 49 (Land Office register + GLO case file) with the RG 15 request "
        "to reduce turnaround trips.",
        "Update archive with 1860 census values and GLO field note findings once retrieved.",
    ]),
    ("Grant application window", [
        "Draft full AHC application with institutional co-applicant once a host is identified.",
        "Write the Arkansas Historical Quarterly article as a standalone deliverable — this strengthens "
        "any future grant application and is achievable from the existing research base.",
        "Consider a DAR chapter grant application as a no-institutional-affiliation option for immediate funding.",
    ]),
]

for timeframe, items in steps:
    story.append(Paragraph(timeframe, h3))
    for item in items:
        story.append(Paragraph(f"• {item}", bullet))
    story.append(Spacer(1, 0.05*inch))

story.append(Spacer(1, 0.3*inch))
story.append(rule())
story.append(Paragraph(
    "The Killing of John Spencer Horner — Johnson County Civil War Archive · "
    "Research by Daniel Lingar · Clarksville, Arkansas · lingardaniel1@gmail.com · "
    "daniel-lingar.github.io/horner-archive · Dossier v. 19.0 · June 2026",
    ParagraphStyle("footer", parent=note, alignment=TA_CENTER, fontSize=8.5)))

doc.build(story)
print("PDF written to", OUTPUT)
