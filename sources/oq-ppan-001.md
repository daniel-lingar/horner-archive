# OQ-PPAN-001 — Modern Parcel / PPAN Identification for Horner–Moore Sites

| Metadata | Value |
| --- | --- |
| **Status** | **Partial** — Patent 19B PPANs identified via AGISO GIS (16 Jun 2026); GPS hits need ARCountyData verify |
| **Priority** | **High** |
| **Source verification** | [ARCountyData — Johnson County](https://www.arcountydata.com/county.asp?county=Johnson) |
| **Data recency** | Assessor: 15 Jun 2026 · Collector: 16 Jun 2026 |
| **Key capability** | Free public search via PPAN / Parcel Number field |

## Purpose

Identify the modern Johnson County PPAN (parcel number) and assessor records covering the Horner homestead, Moore Cemetery, Moore homestead, bluff/cave/overhang area, and related hillside targets.

---

## Reference framework

### Historic legal anchor (controlling reference)

**Rule:** Use this description in formal clerk, assessor, estate, and land-record correspondence. Modern PPANs may not match the 1857 patent boundaries one-to-one. Do not anchor formal letters on a PPAN until current surface parcel boundaries are mapped to the historic patent.

| Field | Value |
| --- | --- |
| Tract size | 160 acres |
| Source document | Federal Land Patent / Certificate **19B** |
| Township / Range | **T12N R24W** |
| Aliquot parts | NE¼ SE¼, Sec. 19 · NW¼ SE¼, Sec. 19 · NW¼ NW¼, Sec. 22 · SE¼ NW¼, Sec. 22 |

**Related:** 1848 cash entry (Document **4706**, Fayetteville Land Office) — additional acreage; section breakdown not yet pinned on site.

### GPS coordinates to cross-check

| Site | Latitude | Longitude | Confidence |
| --- | --- | --- | --- |
| Spencer Horner homestead (attack site) | 35.6681°N | 93.4981°W | GPS-verified (Dewberry 2003) |
| Moore Cemetery | 35.6666°N | 93.4955°W | GPS-verified |
| Moore Cemetery (KML label) | 35.66217°N | 93.4955°W | KML waypoint — reconcile in field |
| Moore homestead / old Moore place | 35.65638°N | 93.4955°W | Approximate — field-check |
| Bluff / cave refuge | 35.6583°N | 93.4888°W | GPS-verified |
| Overhang target A (KML) | 35.65885°N | 93.4893°W | KML shelter target |
| Overhang target B (KML) | 35.6579°N | 93.4885°W | KML shelter target |
| Locked gate / cable (KML) | 35.64768°N | 93.4955°W | Approximate access point |

**Map assets:** `horner-sites.kml` · §04 map table · [Regrid Johnson County](https://app.regrid.com/us/ar/johnson) · [Acres plat map](https://www.acres.com/plat-map/map/ar/johnson-county-ar)

---

## Lookup workflow

1. **ARCountyData:** Johnson County → Search Real Estate Records. Search by legal description (T12N R24W, Sec. 19 & 22) and by PPAN if returned from map click.
2. **Spatial cross-check:** Plot coordinates on Regrid or Acres; note which parcel polygon contains each point.
3. **Extract:** PPAN, owner/taxpayer, acreage, modern legal description, school district.
4. **Feature verification:** Confirm which sites fall inside each parcel (homestead, cemetery, bluff, gate/access corridor).
5. **Archive deposit:** Screenshot parcel cards + map views → `sources/ppan-001/` (create on completion).

---

## Deliverable matrix

*The historic 160-acre tract may now be split, merged, or absorbed into larger rural farm, timber, or pasture tracts. Cemetery and bluff areas may not have separate PPANs.*

| Site | Coordinates | Modern PPAN | Owner / taxpayer | Acreage | Legal description | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **Patent 19B block** | T12N R24W Sec 19 & 22 | See map | Multiple | 160 (1857) | NE¼ SE¼, NW¼ SE¼, NW¼ NW¼, SE¼ NW¼ | [`patent-19b-parcel-map.md`](ppan-001/patent-19b-parcel-map.md) |
| Horner homestead | 35.6681, -93.4981 | `001-06437-000` * | YORK EDWARD V & MELISSA K | 40 | NE SW, **Sec. 25** | *AGISO GIS hit — verify; also see `001-06308-000` CRAIN Sec. 19 |
| Moore Cemetery | 35.6666, -93.4955 | `001-06437-000` * | YORK (same hit) | 40 | Sec. 25 | *Verify on ARCountyData; nearby `001-06408-000` DEWBERRY Sec. 23 |
| Moore homestead | 35.65638, -93.4955 | `001-06512-000` | U S A | 240 | Sec. 36 NE4 E2 NW | Approximate point |
| Bluff / cave / overhang | 35.6583, -93.4888 | `001-06512-000` | U S A | 240 | Sec. 36 | AGISO hit |
| Overhang target A | 35.65885, -93.4893 | `001-06512-000` | U S A | 240 | Sec. 36 | Same polygon as bluff |
| Overhang target B | 35.6579, -93.4885 | `001-06512-000` | U S A | 240 | Sec. 36 | Same polygon as bluff |
| Locked gate / access | 35.64768, -93.4955 | `001-06521-000` | GALLOWAY LAND CO LLC | 200 | Sec. 36 S2 SW NE SE S2 SE | Access corridor |

**AGISO pull:** `sources/ppan-001/agiso-query-2026-06-16.txt` · Query script: `scripts/query_ppan_001.py`

---

## Cross-references

- OQ-20 estate/deed search — use **Patent 19B legal description**, not PPAN, in clerk letters
- `grant-readiness/estate-request-oq20.md`
- `index.html` §04 land description · §04b coordinate table

## On completion

- [x] AGISO GIS query — Patent 19B PPAN map + GPS point hits (16 Jun 2026)
- [ ] ARCountyData screenshots to confirm GPS → PPAN
- [ ] Deposit screenshots in `sources/ppan-001/`
- [ ] Update §13 / §16 on site
- [ ] Log in `sources/INGEST_LOG.md`
- [ ] Optional: add PPAN layer note to `horner-sites.kml`