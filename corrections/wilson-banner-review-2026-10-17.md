# Wilson and banner follow-up, 17 October 2026

**Prepublication review snapshot.** The local/unpublished status and unchecked boxes below describe the review stage. The complete release includes these changes; see [release history](../CHANGELOG.md) and the [current reader](../index.html). Classroom and historical verification limits remain in force.

Prepared locally for review. These changes have not been pushed or published. The public main branch checked was `4fe2aa4592b3c0b0bff1dfc9218ef2e2dc47d3e1`; the reader branch checked was `cba7866`. That reader is v21.2, so the draft links and notice use v21.2 rather than the older v21.1 label. The Library PDFs checked separately still identify themselves as v21.0; they were not replaced.

## Item 17

Approved reader wording:

> The published excerpt states: “One time they left Jess Wilson to hold their horses when they went to fight” [S04]. The surrounding published passage does not identify “they” or specify which fight is meant.

Register status: *original transcript unchecked; antecedent of "they" unresolved.* Closed only at the published-excerpt level.

The preceding published sentence is “Dad said Jess Wilson was a brave man too.” The two earlier website excerpt blocks describe a road killing and dance-house raid and name Wash Middleton. A more distant excerpt names Wash Middleton and Fate Arnold. These arranged excerpts do not establish the original manuscript's consecutive sentences; “too” does not identify its own referent.

The earlier website attributes the narrator to Prof. John Turner Horner, “Dad” to his father Dr. John Turner Horner, and recording to Eva Horner, the professor's daughter. This is an attributed transmission chain; it has not been independently checked against the manuscript. The new source note states those roles and limits. The legacy transcript page replaces the “Squad Members” heading with a neutral editorial heading. No claim is made that the original manuscript lacks that heading.

The reader, C20 correction row, research register, S04 catalog and annotated bibliography are aligned on the reader review branch. The Confederate-prisoner identification, original-attacker claim and reprisal-victim claim are retained only as unresolved research distinctions in the register.

## Item 18

The live page, transcript, old dossier, principal KML, map-data script and map withdrawal page were freshly downloaded and matched the checked main branch. Both existing banner links returned HTTP 200. The six downloaded gallery files were inspected and all are census scans.

The revised banner calls the page a partly corrected version of v20.13 and says the earlier census figures are unverified. It does not declare those figures false. The inline census label refers to the page examined in the v21.2 draft and leaves its original metadata unresolved. The patent label points to classroom source pack p. 4, which gives the first tract reading and leaves remaining readings under review.

The legacy PDF's notice page uses the revised banner text. Its other 57 pages retain identical extracted text and rendered pixels. The reader remains six pages. The core classroom pack was inspected for the p. 4 reference and was not changed.

## Targeted privacy checklist

- [x] Principal `horner-sites.kml`: already served a withdrawal notice with no placemarks.
- [x] `js/horner-site-map-data.js` and `ppan-map.html`: already withdrawn on the live site.
- [x] Current cadastral extracts and assignments under `sources/ppan-001/`: already replaced with withdrawal notices on main.
- [x] Main-page birthdate: already removed by the earlier fix; the preceding PDF redactions are preserved.
- [x] Main-page share image: already uses the patent image rather than the marker photograph.
- [ ] Publish the prepared withdrawal of the four duplicate KML files in `00_INBOX/auto-ingest/horner-archive/2026-06-15/`. Each freshly fetched live copy still returned HTTP 200 with 11 placemarks. The local drafts replace their coordinate payloads with the same withdrawal notice as the principal KML.
- [ ] Publish the revised banner, inline labels, source notes, register and PDFs if these drafts are adopted.
- [ ] After publication, re-fetch the changed URLs and verify the deployed content; working files are not proof of deployment.

This targeted check does not certify every historic inbox attachment, PDF, image or metadata field as free of personal or location information. Older Git commits and third-party copies remain outside the current-file withdrawal.

## Validation

The reader branch's release validator passed 756 checks with no failures. Both worktrees passed `git diff --check`. Additional checks confirmed the banner is the first visible body element, no active scripts or gallery images remain in the legacy page, all five local KML files have no placemarks or coordinates, and the two revised legacy PDF copies are identical. The reader's six pages and replacement PDF notice were rendered and visually checked. These are technical and source-consistency checks, not authentication of the original family manuscript or a classroom pilot.

## Review locations

- Legacy page draft: `review/wilson-banner-20261017` in `horner-release-review`.
- Reader/source draft: `review/wilson-sources-20261017` in `horner-reader-review`.

The two branches keep the live-page repair separate from the unpublished reader release. No remote branch, public page, Library PDF or Git history was overwritten.
