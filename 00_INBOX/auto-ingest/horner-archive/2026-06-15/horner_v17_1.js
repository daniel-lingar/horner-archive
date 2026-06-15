const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageNumber, TabStopType, TabStopPosition
} = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, size: 32, font: "Arial" })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, bold: true, size: 28, font: "Arial" })]
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    children: [new TextRun({ text, bold: true, size: 24, font: "Arial" })]
  });
}
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 },
    children: [new TextRun({ text, font: "Arial", size: 22, ...opts })]
  });
}
function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: [new TextRun({ text, font: "Arial", size: 22 })]
  });
}
function note(text) {
  return new Paragraph({
    spacing: { after: 120 },
    indent: { left: 720 },
    children: [new TextRun({ text, font: "Arial", size: 20, italics: true, color: "555555" })]
  });
}
function spacer() {
  return new Paragraph({ children: [new TextRun("")], spacing: { after: 160 } });
}
function divider() {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "888888", space: 1 } },
    children: [new TextRun("")],
    spacing: { after: 200 }
  });
}

function twoColRow(label, value, valueColor = "000000") {
  return new TableRow({
    children: [
      new TableCell({
        borders,
        width: { size: 2500, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
        children: [new Paragraph({ children: [new TextRun({ text: label, bold: true, font: "Arial", size: 20 })] })]
      }),
      new TableCell({
        borders,
        width: { size: 6860, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: value, font: "Arial", size: 20, color: valueColor })] })]
      })
    ]
  });
}

function contraRow(issue, vA, vB) {
  return new TableRow({
    children: [
      new TableCell({
        borders,
        width: { size: 3120, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: issue, font: "Arial", size: 20, bold: true })] })]
      }),
      new TableCell({
        borders,
        width: { size: 3120, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: vA, font: "Arial", size: 20 })] })]
      }),
      new TableCell({
        borders,
        width: { size: 3120, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: vB, font: "Arial", size: 20 })] })]
      })
    ]
  });
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      }
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: "1A1A2E" },
        paragraph: { spacing: { before: 320, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "2C3E6B" },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "4A4A4A" },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [

      // TITLE BLOCK
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "HORNER FAMILY RESEARCH DOSSIER", bold: true, size: 40, font: "Arial", color: "1A1A2E" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "Johnson County, Arkansas — Civil War Era", size: 28, font: "Arial", color: "444444", italics: true })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "Version 17  |  June 2026", size: 22, font: "Arial", color: "888888" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "Compiled by Daniel Bret Lingar  |  Capitol Contracts LLC", size: 20, font: "Arial", color: "888888" })]
      }),
      divider(),

      // SECTION 1: JOHN SPENCER HORNER
      h1("1. John Spencer Horner — Primary Subject"),
      spacer(),

      h2("1.1 Vital Statistics"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2500, 6860],
        rows: [
          twoColRow("Born", "1807 or 1808, Hickman County, Tennessee (year conflict — see contradictions)"),
          twoColRow("Died", "2 August 1864, Johnson County, Arkansas — killed by bushwhackers"),
          twoColRow("Married", "1828, Perry County, Tennessee — to Permelia Turner"),
          twoColRow("Heritage", "Irish and Cherokee descent (per Goodspeed Barry County, MO History — secondary source only, unverified genealogically)"),
          twoColRow("Religion / Politics", "Union sympathizer; slave owner. Opposed secession strongly."),
        ]
      }),
      spacer(),

      h2("1.2 Residences — Documented Sequence"),
      bullet("Pre-1828: Hickman County, Tennessee"),
      bullet("1828–1835: Perry County, Tennessee (post-marriage)"),
      bullet("1835–1836: Last documented Perry County activity (Howard's Store account, March 1835; 4.5-acre Buffalo River purchase granted)"),
      bullet("1836–1849: Franklin County, Arkansas (arrived ~1836; confirmed at Cass, Franklin County, 1843; squatter on 80 acres, W½ SE¼ Range 24 Township 12 Section 27)"),
      bullet("1840: Note — Pleasant Horner made a round-trip to Arkansas per Howard's Store: 'Time you started to Arkansas and returned back.' Indicates the family was scouting Arkansas before the full move."),
      bullet("1849–1864: Johnson County, Arkansas — 18 miles north of Clarksville, near Ozone/Catalpa area"),
      spacer(),

      h2("1.3 Land Holdings — Federal Documentation"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2500, 6860],
        rows: [
          twoColRow("1848 Patent", "40 acres. NESE, Section 19, T12N R24W. Fayetteville Land Office, Doc #4706, signed July 10, 1848. Accession AR0940__.121."),
          twoColRow("1857 Patent — Parcel 1", "NWSE, Section 19, T12N R24W. Doc #19B, signed April 1, 1857. Accession AR2690__.426. NOTE: Assignee of Co-Cha-Tubbee representing deceased Cunne-Chubbee (Choctaw names — unexplained acquisition mechanism)."),
          twoColRow("1857 Patent — Parcel 2", "160 acres. SENW, Section 22, T12N R24W. Same doc/date as Parcel 1. Same Choctaw assignee notation."),
          twoColRow("Total Documented", "At least 200 acres. Spencer himself stated 120 acres prior to the rebellion — discrepancy unresolved."),
          twoColRow("1837 Benton County", "Spencer appears as assignee on a $55 promissory note, Dec 6 1837, due Dec 25 1838 (per History of Benton County, p.605). Minor — confirms legal/financial activity in AR that year."),
          twoColRow("Pre-AR Purchase", "1835: 4.5-acre purchase on Buffalo River, Perry County, TN Court Records 1834–35."),
        ]
      }),
      spacer(),

      h2("1.4 Military / Civil Service"),
      bullet("July 1861: Member of Home Guard Minute Men, Mulberry Township, Johnson County, Arkansas"),
      bullet("Conscripted by Confederates at some point during the war — remained a Union man"),
      bullet("Permelia applied for pension at age 66 based on Spencer's Civil War service — application outcome unknown"),
      spacer(),

      h2("1.5 The Killing — August 2, 1864"),
      p("The following account draws from multiple FamilySearch sources including the Civil War Life note, the HeatherAcord note, the Larry Kraus/Annie Everette files, and William's tombstone inscription. Where sources conflict, both versions are noted."),
      spacer(),
      bullet("The family had gathered at Spencer's house including recently orphaned grandsons John Samuel Acord and Christopher Columbus Acord"),
      bullet("William R. Horner had come home — listed as AWOL from Union 2nd Arkansas Infantry (one source says 'leave or scouting mission')"),
      bullet("Family was eating a fried chicken dinner but were already concerned about bushwhackers — children were posted as road lookouts"),
      bullet("Several men appeared coming off the mountain; children ran in yelling 'Here they come Grandpap!'"),
      bullet("William bolted out the back door toward the potato field"),
      bullet("Spencer recognized the men as neighbors and walked into the yard to speak with them — he did not believe he was in danger"),
      bullet("They shot Spencer where he stood. Location: the yard (primary FamilySearch account) / the potato patch (HeatherAcord note — minor conflict)"),
      bullet("They chased William, caught him in the potato field, pistol-whipped him, and — per Spencer's daughter Sarah — 'crushed his privates'"),
      bullet("They left William for dead and departed"),
      bullet("The women feared taking William back to the house would alert the bushwhackers that he survived, so they carried him into the woods and hid him in a cave or rock overhang"),
      bullet("To disguise their daily supply runs, the women wrapped food bundles to resemble a baby"),
      bullet("William died eight days later on August 10, 1864"),
      spacer(),
      p("William's tombstone inscription (verbatim, confirmed from two sources):"),
      note('"Wm. R. Horner Born Aug. 1, 1834 Killed Aug. 10, 1864 by parties known to his family."'),
      spacer(),
      p("NOTE: Spencer and William were both buried somewhere on the farm. The graves are reported as unmarked. However, the cemetery record (see Section 4) includes GPS coordinates that Jimmie Dewberry reported having visited."),
      spacer(),

      h2("1.6 Suspected Killers"),
      bullet("Family belief: one of the Stewarts from Yale participated — probably Henry Stewart, buried in Yale Cemetery"),
      note("Source: FamilySearch Civil War Life note. This is family oral tradition, not a court record. No criminal proceedings were ever found. Treat as lead, not established fact."),
      bullet("HeatherAcord note states: 'The bushwhackers were after Spencer's money but they did not get it, and the money was never found after his death.' — family lore, unverified"),
      spacer(),

      divider(),

      // SECTION 2: PERMELIA TURNER HORNER
      h1("2. Permelia Turner Horner — Widow"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2500, 6860],
        rows: [
          twoColRow("Born", "November 11, 1810 (per Jimmie Dewberry / cemetery record) OR 1815, Virginia (per HeatherAcord note) — CONFLICT, see Section 6"),
          twoColRow("Died", "9 August 1892, Johnson County, Arkansas (one day before the 28th anniversary of William's death)"),
          twoColRow("Parents", "Turner family — came from St. Clair County, Alabama; Calhoun County, Arkansas; and Mulgrave, Oklahoma"),
          twoColRow("After the War", "Sold property for 'a chunk of a mare and an old wagon'; loaded up and left — possibly to Webster County, Missouri to join family"),
          twoColRow("Return", "Permelia and some Horners returned to Arkansas after the war"),
          twoColRow("Burial", "Horner family cemetery with Spencer and William Riley — see Section 4 for GPS coordinates"),
        ]
      }),
      spacer(),

      divider(),

      // SECTION 3: CHILDREN
      h1("3. Children of Spencer and Permelia Horner"),
      p("Ten children born, all lived to adulthood per HeatherAcord note. Seven died in 1864 or close to it."),
      spacer(),

      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2600, 1500, 1500, 3760],
        rows: [
          new TableRow({
            children: [
              new TableCell({ borders, width: { size: 2600, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Name", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 1500, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Born", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 1500, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Died", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 3760, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Notes", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
            ]
          }),
          ...[
            ["Dr. John Turner Horner", "1829", "1911", "Eldest son. Conscripted by Confederates. Later organized (or assisted) Union wagon train moving Horner family to Webster County, MO. Became a physician."],
            ["Zilpha Horner", "1833", "1910", "Married Boen, later Mooney. Moved to Webster County, MO. Estate heir listed with husband James Boen; James died 1872 leaving 5 children."],
            ["William R. Horner", "Aug 1, 1834", "Aug 10, 1864", "AWOL from 2nd AR Infantry. Beaten and left to die by bushwhackers Aug 2; died in the cave/overhang Aug 10. Tombstone inscription confirmed verbatim."],
            ["Elizabeth Horner Acord", "1835", "Mar 1, 1864", "Died pneumonia/measles. Married Francis Marion Acord. Sons John Samuel and Christopher Columbus Acord were orphaned and at Spencer's house the day of the killing."],
            ["Andrew Jackson Horner", "?", "Jul 31, 1864", "Died of measles in camp at Lewisburg Ridge, 2nd Arkansas Infantry."],
            ["Pleasant Horner", "?", "Aug 12, 1864", "Died of measles in camp at Lewisburg Ridge, 2nd Arkansas Infantry. Two days after Spencer's killing."],
            ["Oma Horner (Bowen)", "?", "After 1865", "One source says died before 1864. BUT the 1865 estate record lists her as a living heir: 'Oma Bowen, husband John J., Johnson Co., Ark.' — CONTRADICTION. Estate record is primary; pre-1864 death claim appears incorrect."],
            ["Keziah Horner James", "?", "?", "Estate listed as 'Keziah James, A.J. James, Webster Co., Mo.'"],
            ["Polly Horner Bowen", "?", "?", "Estate: 'Polly Bowen, Jesse Bowen, Webster Co., Mo.'"],
            ["James Spencer 'Jim' Horner", "1849", "1924", "Too young to serve. Survived."],
            ["Sarah Ann Horner Vaught", "1853", "1929", "Eyewitness to the attack. Reported bushwhackers 'crushed his privates.' Estate: Webster Co., MO."],
          ].map(([name, born, died, notes]) =>
            new TableRow({
              children: [
                new TableCell({ borders, width: { size: 2600, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: name, font: "Arial", size: 20, bold: true })] })] }),
                new TableCell({ borders, width: { size: 1500, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: born, font: "Arial", size: 20 })] })] }),
                new TableCell({ borders, width: { size: 1500, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: died, font: "Arial", size: 20 })] })] }),
                new TableCell({ borders, width: { size: 3760, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: notes, font: "Arial", size: 20 })] })] }),
              ]
            })
          )
        ]
      }),
      spacer(),

      divider(),

      // SECTION 4: CEMETERY / GPS
      h1("4. Cemetery and GPS Coordinates"),
      p("Coordinates provided by Jimmie Dewberry (researcher) via email to Thomas Troy Graham, 2003. Jimmie states he has personally visited the cemetery."),
      spacer(),

      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2500, 6860],
        rows: [
          twoColRow("Cemetery Location", "Lat. 35°, Long. 093°W, 29.73 min."),
          twoColRow("Spencer's House Site", "Lat. 35° 40.09', Long. 093°W 29.89'"),
          twoColRow("William's Bluff/Cave", "Lat. 35° 39.5', Long. 093° 29.33' — WHERE WILLIAM DIED"),
          twoColRow("Access Route", "From Ozone: take Hwy 86 (Low Gap Road) west ~2 miles. Locked cable gate blocks trail. Old Moore home place is ~0.4 miles past cable. Cemetery is in the edge of the Moore property, less than 0.5 miles from Moore house."),
          twoColRow("Access Note", "Junior Moore (key holder to cable gate) is deceased as of 2003 correspondence. Current access status unknown."),
        ]
      }),
      spacer(),
      p("Confirmed burials per Jimmie Dewberry:"),
      bullet("Spencer Horner 1807 – 2 Aug 1864"),
      bullet("William Riley Horner 1834 – 10 Aug 1864"),
      bullet("Mealey (Permelia) Horner 11 Nov 1810 – 9 Aug 1892"),
      bullet("Permelia Narcissa Cowan 6 Nov 1860 – 24 Apr 1884"),
      bullet("Tinna A. Boen (dates unknown — child of Mary Ann and Thomas Franklin Boen, William Riley's widow's second marriage)"),
      bullet("Sarah E. Boen (dates unknown — same parentage)"),
      spacer(),

      divider(),

      // SECTION 5: ESTATE RECORDS
      h1("5. Estate Records — 1865, Johnson County, Arkansas"),
      p("Source: Johnson County Courthouse. Physical papers listed in index as pigeon hole 6 — search in October 1973 failed to locate them. The following is from court records index only."),
      spacer(),

      h2("Spencer Horner Estate, 1865"),
      bullet("Administrator: John Turner Horner"),
      bullet("Dr. John Turner Horner — Johnson Co., AR"),
      bullet("Zilpha Bowen and husband John Bowen — Webster Co., MO — children: William, Sarah Ann, Nancy, Emaline, Columbus"),
      bullet("William R. Horner — deceased (heirs listed in separate estate below)"),
      bullet("Elizabeth Acord — deceased; heirs: John and Columbus"),
      bullet("Oma Bowen, husband John J. — Johnson Co., AR [NOTE: ALIVE in 1865 — contradicts 'died before 1864' claim]"),
      bullet("Polly Bowen, Jesse Bowen — Webster Co., MO"),
      bullet("Keziah James, A.J. James — Webster Co., MO"),
      bullet("Sarah Horner — Webster Co., MO"),
      spacer(),

      h2("William R. Horner Estate, 1865"),
      bullet("Administrator: Mary Ann Horner (widow)"),
      bullet("Heirs: Zilpha, John, Permelia, and William"),
      spacer(),

      h2("James Boen Estate, 1872"),
      bullet("Zilpha Boen — widow"),
      bullet("Five children; William S. made guardian of 3 minor children"),
      bullet("Sarah Oma (age 16, later married ___ Wharton), C.C. Boen (age 13), Emaline Boen (age 12), Nancy Boen (wife of James A. Willsford)"),
      spacer(),

      divider(),

      // SECTION 6: CONTRADICTIONS
      h1("6. Active Contradictions — Unresolved"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [3120, 3120, 3120],
        rows: [
          new TableRow({
            children: [
              new TableCell({ borders, width: { size: 3120, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Issue", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 3120, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Version A", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 3120, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Version B", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
            ]
          }),
          contraRow("Spencer killed where", "In the yard (FamilySearch Civil War Life note)", "In the potato patch (HeatherAcord note)"),
          contraRow("Oma Horner's fate", "Died before 1864 (HeatherAcord note)", "ALIVE — listed as heir in 1865 estate record (court document — stronger source)"),
          contraRow("Spencer birth year", "1808 (most sources)", "1807 (Jimmie Dewberry / cemetery record)"),
          contraRow("Permelia birth year", "1815, Virginia (HeatherAcord)", "Nov 11, 1810 (Jimmie Dewberry / cemetery)"),
          contraRow("John Turner Horner — war role", "Conscripted by Confederates (HeatherAcord)", "Organized Union wagon train (Civil War Life note) — NOT necessarily contradictory; may be sequential"),
          contraRow("Spencer's acreage", "120 acres (Spencer's own statement)", "200+ acres documented in federal patents — likely additional parcels not in patent record"),
        ]
      }),
      spacer(),

      divider(),

      // SECTION 7: TENNESSEE BACKGROUND
      h1("7. Tennessee Background — Howard's Store Account Books"),
      p("Cedar Creek, Perry County, Tennessee. Store account books 1833–1840, compiled by researcher Betty Horner and Thomas Troy Graham. Key Horner-related entries:"),
      spacer(),
      bullet("March 1835: Spencer Horner charged $3.75 for breakfast for five men and their horses — and also for a prisoner's supper and board. NOTE: Spencer had a prisoner in custody. No explanation in the record."),
      bullet("March 1835: Spencer purchased half-pint whiskey ($0.12) and tobacco"),
      bullet("July 1833: Spencer Horner — 1 cake $0.06"),
      bullet("1835: Spencer and George Horner — joint entries"),
      bullet("April 1835: Mrs. Jemima Horner — fabric, dyes (indigo, madder, copperas, calico) — noted as 'taken by Spencer Horner'"),
      bullet("March 1840: Pleasant Horner — 2 passengers, round trip, foot ferriage. Noted explicitly: 'Time you started to Arkansas and returned back.' This is documented proof Pleasant scouted Arkansas before the family's permanent move."),
      bullet("Other Horner family members in the books: George, William Sr., William Jr., Thomas, Isaac, Lewis, Jesse, Caleb — extended family network confirmed"),
      spacer(),

      divider(),

      // SECTION 8: SOURCES
      h1("8. Sources and Confidence Ratings"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [4680, 2340, 2340],
        rows: [
          new TableRow({
            children: [
              new TableCell({ borders, width: { size: 4680, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Source", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 2340, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Type", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 2340, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Confidence", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
            ]
          }),
          ...[
            ["BLM Federal Land Patents (1848, 1857)", "Government — PRIMARY", "HIGH"],
            ["Johnson County Estate Records, 1865", "Court — PRIMARY", "HIGH"],
            ["William R. Horner tombstone inscription", "Physical monument — PRIMARY", "HIGH"],
            ["Jimmie Dewberry GPS coordinates (via email 2003)", "Eyewitness researcher", "MEDIUM-HIGH"],
            ["Howard's Store Account Books 1833–1840", "Contemporary commercial record — PRIMARY", "HIGH"],
            ["FamilySearch Civil War Life note (HeatherAcord, 2013)", "Family researcher — secondary", "MEDIUM"],
            ["Larry Kraus / Annie Everette files (pre-2000)", "Family researcher — secondary", "MEDIUM"],
            ["Thomas Troy Graham emails (2003)", "Family researcher — secondary", "MEDIUM"],
            ["Goodspeed Barry County, MO History (Irish/Cherokee claim)", "Published secondary", "LOW — unverified genealogically"],
            ["Henry Stewart suspect (family belief)", "Oral tradition", "LOW — no court record"],
            ["Spencer's hidden money story", "Oral tradition", "LOW — unverified"],
          ].map(([src, type, conf]) =>
            new TableRow({
              children: [
                new TableCell({ borders, width: { size: 4680, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: src, font: "Arial", size: 20 })] })] }),
                new TableCell({ borders, width: { size: 2340, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: type, font: "Arial", size: 20 })] })] }),
                new TableCell({ borders, width: { size: 2340, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: conf, font: "Arial", size: 20 })] })] }),
              ]
            })
          )
        ]
      }),
      spacer(),

      divider(),

      // SECTION 9: OPEN LEADS
      h1("9. Open Research Leads"),
      bullet("Henry Stewart, Yale Cemetery (Johnson County) — obtain death record, census records, any criminal history"),
      bullet("Yale Cemetery — physical visit to locate Henry Stewart grave"),
      bullet("Verify Oma Horner / Oma Bowen identity: estate record 1865 says alive with husband John J. Bowen, Johnson County. Cross-reference against 1870 census."),
      bullet("Permelia's pension application — VA/NARA search for widow's pension filing. Application outcome unknown."),
      bullet("2nd Arkansas Infantry regimental records — confirm William R. Horner AWOL status; confirm Andrew Jackson and Pleasant Horner deaths at Lewisburg Ridge"),
      bullet("John Turner Horner CMSR — was he conscripted Confederate or did he serve Union? What is his actual military record?"),
      bullet("Choctaw land assignment (Co-Cha-Tubbee / Cunne-Chubbee) — research how Spencer acquired these patents as assignee; may connect to broader Native American land grant history"),
      bullet("1940/1942 oral history — already integrated in prior versions but not fully cited here; re-verify content"),
      bullet("Junior Moore's heirs — current owner of Moore property is unknown; access to cemetery requires resolution"),
      bullet("Cherokee ancestry claim — requires genealogical work through Russell family line (the Irish/Cherokee reportedly came through the Russells per HeatherAcord note)"),
      spacer(),

      divider(),

      // VERSION HISTORY
      h1("10. Version History"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [1440, 2000, 5920],
        rows: [
          new TableRow({
            children: [
              new TableCell({ borders, width: { size: 1440, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Version", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 2000, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Date", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
              new TableCell({ borders, width: { size: 5920, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                shading: { fill: "2C3E6B", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: "Changes", bold: true, font: "Arial", size: 20, color: "FFFFFF" })] })] }),
            ]
          }),
          ...[
            ["v16", "March–April 2026", "BLM land records, NARA CMSRs, widow's pension filings, GPS coordinates integrated, 1942 oral history added. Dual descendancy confirmed (Horner + Hill lines)."],
            ["v17", "June 2026", "FamilySearch document integrated: Henry Stewart suspect named, baby-bundle detail added, tombstone inscription verbatim confirmed, full estate heir list with Oma contradiction identified, Howard's Store account book entries added, contradictions table formalized, source confidence ratings added."],
          ].map(([ver, date, changes]) =>
            new TableRow({
              children: [
                new TableCell({ borders, width: { size: 1440, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: ver, font: "Arial", size: 20, bold: true })] })] }),
                new TableCell({ borders, width: { size: 2000, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: date, font: "Arial", size: 20 })] })] }),
                new TableCell({ borders, width: { size: 5920, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
                  children: [new Paragraph({ children: [new TextRun({ text: changes, font: "Arial", size: 20 })] })] }),
              ]
            })
          )
        ]
      }),
      spacer(),

      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 400 },
        children: [new TextRun({ text: "— END OF DOSSIER v17 —", font: "Arial", size: 20, color: "888888", italics: true })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/Horner_Dossier_v17.docx', buffer);
  console.log('Done.');
});
