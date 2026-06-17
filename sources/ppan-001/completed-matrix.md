# OQ-PPAN-001 — Completed Parcel Matrix

**Source:** Arkansas AGISO statewide parcel layer (Johnson County CAMA feed, assessor data current Jun 2026) — equivalent to ARCountyData real estate records.  
**Study anchor:** Patent 19B · T12N R24W · Sec. 19 & 22  
**JSON backup:** `agiso-matrix-2026-06-16.json` · Gate corridor: `gate-corridor-2026-06-17.json`  
**Gate status:** **Primary confirmed** — `001-03571-000` (U.S.A.) @ 35.66075, -93.48564 via GIS corridor scan (17 Jun 2026). ARCountyData map-click screenshot optional.  
**Interactive map:** [`ppan-map.html`](../../ppan-map.html) · embedded in [`index.html` §04](../../index.html#map)

---

## Site feature matrix

| Site Feature | Coordinates | Modern PPAN | Owner / Taxpayer | Acreage | Modern Legal Description | Field Notes / Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Horner Homestead** | 35.6681, -93.4981 | `001-06308-000` | CRAIN RANDA ET AL | 182.66 | SE NW; E2 SW 46.68 ac; W2 SW 15.91 ac; SW SE — S19 T12N R24W | **Primary patent-zone match.** Dominant Sec. 19 block overlapping Patent 19B aliquots. AGISO point-in-polygon returned Sec. 25 YORK (see below) — **use Crain for title work.** |
| **Moore Cemetery** | 35.6666, -93.4955 | `001-06298-001` | DEWBERRY DORIS | 47.73 | PT NE NE — S19 T12N R24W | **No separate cemetery PPAN.** Cemetery sits on Dewberry tract; same surname as GPS surveyor Jimmie Dewberry (2003). Adjacent: `001-06408-000` DEWBERRY DORIS TRUST, 127 ac, S23. |
| **Moore Homestead** | 35.65638, -93.4955 | `001-06512-000` | U S A | 240.0 | NE4 E2 NW — S36 T12N R24W | Approximate KML point; federal/timber hillside tract south of patent block. |
| **Bluff / Cave / Overhang** | 35.6583, -93.4888 | `001-06512-000` | U S A | 240.0 | NE4 E2 NW — S36 T12N R24W | Hillside/timber zone; William Riley cave refuge area per oral history. |
| **Overhang Target A** | 35.65885, -93.4893 | `001-06512-000` | U S A | 240.0 | NE4 E2 NW — S36 T12N R24W | Same polygon as bluff — KML shelter target A. |
| **Overhang Target B** | 35.6579, -93.4885 | `001-06512-000` | U S A | 240.0 | NE4 E2 NW — S36 T12N R24W | Same polygon as bluff — KML shelter target B. |
| **Locked Gate (Jimmie SSE — Primary)** | 35.66075, -93.48564 | `001-03571-000` | U S A | 621.0 | SECTION — S31 T12N R23W | **Confirmed.** Federal timber boundary crossing ≈0.9 mi SSE of cemetery on NW-fork access. South-side parcel at boundary: `001-06435-000` (U.S.A., 240 ac, S25). Matches locked-cable-on-private-spur pattern. |
| **Locked Gate (KML est. — Legacy)** | 35.64768, -93.4955 | `001-06521-000` | GALLOWAY LAND CO LLC | 200.0 | S2 SW NE SE S2 SE — S36 T12N R24W | **Discard for navigation.** Troy-era unverified estimate on -93.4955 meridian; not Jimmie-corrected. |

### Jimmie SSE corridor (primary, cemetery → gate)

| Boundary lat/lon | PPAN | Owner | Acres | Sec | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 35.66660, -93.49550 | `001-06437-000` | YORK EDWARD V & MELISSA K | 40 | 25 | Cemetery cluster (GIS polygon hit) |
| 35.66626, -93.49492 | `001-06441-000` | TAFF ALLISON & AMELIA | 40.26 | 25 | |
| 35.66488, -93.49260 | `001-06435-000` | U S A | 240 | 25 | South parcel at primary gate boundary |
| **35.66075, -93.48564** | **`001-03571-000`** | **U S A** | **621** | **31** | **Primary gate boundary (confirmed)** |

### Legacy meridian corridor (-93.4955, gate → cemetery — do not use)

| Boundary lat | PPAN | Owner | Acres | Sec | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 35.64768 | `001-06521-000` | GALLOWAY LAND CO LLC | 200 | 36 | KML gate estimate |
| 35.65052 | `001-06523-000` | QUALLS LONNIE R | 40 | 36 | |
| 35.65241 | `001-06516-000` | HORNEY PAUL & FRANSHEL | 160 | 36 | |
| 35.65430 | `001-06512-000` | U S A | 240 | 36 | Moore homestead / bluff tract |
| 35.66140 | `001-06435-000` | U S A | 240 | 25 | |
| 35.66518 | `001-06437-000` | YORK EDWARD V & MELISSA K | 40 | 25 | GIS polygon hit at cemetery coords |

### GPS polygon anomaly (do not use for homestead/cemetery)

| Coordinates | AGISO polygon hit | Issue |
| :--- | :--- | :--- |
| 35.6681, -93.4981 (homestead) | `001-06437-000` YORK, Sec. **25** | Outside Patent Sec. 19/22 — coarse rural GIS |
| 35.6666, -93.4955 (cemetery) | `001-06437-000` YORK, Sec. **25** | Same — superseded by Dewberry Sec. 19 assignment above |

---

## Patent 19B aliquot → modern PPAN (full study area)

| Patent 19B aliquot (1857) | Modern PPAN | Owner / Taxpayer | Acreage | Modern Legal Description |
| :--- | :--- | :--- | :--- | :--- |
| **NE¼ SE¼, Sec. 19** | `001-06313-000` | WARREN THOMAS SAMUEL TRUST | 40.0 | NE SE — S19 T12N R24W |
| | `001-06303-000` | WARREN THOMAS SAMUEL TRUST | 19.99 | PT SE NE — S19 T12N R24W |
| | `001-06302-001` | SCHOOL DISTRICT #7 | 7.09 | PT SE NE — S19 T12N R24W |
| **NW¼ SE¼, Sec. 19** | `001-06314-000` | BROWN ALISON TAYLOR | 20.0 | PT NW SE — S19 T12N R24W |
| | `001-06315-000` | WARREN THOMAS SAMUEL TRUST | 24.0 | PT NW SE — S19 T12N R24W |
| | `001-06301-000` | FARMER AUDREY & RISHELLE WILSON | 1.6 | PT SW NE (SW/4 NE/4 per metes) — S19 T12N R24W |
| | `001-06301-001` | WILSON RISHELLE L | 2.3 | PT SW NE — S19 T12N R24W |
| **NW¼ NW¼, Sec. 22** | `001-06393-000` | COOK CATHIE B | 6.79 | 6.79 AC NE NW — S22 T12N R24W |
| | `001-06392-000` | PRICE JAMES C FLP | 83.0 | W2 NW; 3.00 AC SE NW — S22 T12N R24W |
| | `001-06380-000` | KIMBRIEL CHARLOTTE | 0.24 | PT NW NE — S22 T12N R24W |
| **SE¼ NW¼, Sec. 22** | `001-06393-001` | ARBAUGH IMOGENE | 24.9 | PT SE NW — S22 T12N R24W |
| | `001-06393-002` | QUALITY RESTORATION OF ARKANSAS | 0.87 | PT SE NW — S22 T12N R24W |
| | `001-06393-004` | BEAN JIMMY G & BETHANY L | 8.33 | PT SE NW — S22 T12N R24W |

---

## Summary

1. **Patent 19B's 160 acres** are now **many modern PPANs** across Sec. 19 and 22 — not one parcel. Warren Trust, School District #7, Farmer/Wilson, Brown, Arbaugh, Cook/Price, and **Crain (182.66 ac)** hold the overlapping footprint.

2. **Horner homestead** maps best to **`001-06308-000` (Crain Randa et al.)** — the largest Sec. 19 tract covering SE NW and SW aliquots where the 1844 GLO field notes placed **"G. Homers field."**

3. **Moore Cemetery** has **no dedicated PPAN**; it falls on **`001-06298-001` (Dewberry Doris, 47.73 ac, Sec. 19)** with related holding **`001-06408-000` (Dewberry Doris Trust, 127 ac, Sec. 23)**.

4. **Bluff, cave, and overhang targets** share **`001-06512-000` (U.S.A., 240 ac, Sec. 36)** — federal hillside/timber land east of the patent block.

5. **Locked cable gate (primary)** confirmed at **`001-03571-000` (U.S.A., 621 ac, Sec. 31 T12N R23W)** @ 35.66075, -93.48564 — federal boundary on Jimmie SSE corridor. Legacy KML gate on Galloway parcel discarded.

6. **ARCountyData map-click** optional screenshot for chain of custody; AGISO polygons are approximate per state disclaimer.

**Formal correspondence:** continue using Patent 19B legal description, not PPAN alone.