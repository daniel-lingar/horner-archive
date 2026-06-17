# OQ-PPAN-001 — Modern Parcel / PPAN Identification for Horner–Moore Sites

| Metadata | Value |
| --- | --- |
| **Status** | **Closed v20.13** — Matrix + **primary gate confirmed** (`001-03571-000` U.S.A. @ 35.66075, -93.48564) |
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
| Locked gate / cable (Jimmie SSE — **primary**) | 35.66075°N | 93.48564°W | **Confirmed** — `001-03571-000` U.S.A., Sec. 31 T12N R23W |
| Locked gate / cable (KML est. — legacy) | 35.64768°N | 93.4955°W | Discard — Galloway `001-06521-000`, Troy-era estimate |

**Map assets:** [**`ppan-map.html`**](../ppan-map.html) (full-screen interactive) · `horner-sites.kml` · §04 map table · [Regrid Johnson County](https://app.regrid.com/us/ar/johnson) · [Acres plat map](https://www.acres.com/plat-map/map/ar/johnson-county-ar)

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

See **[`ppan-001/completed-matrix.md`](ppan-001/completed-matrix.md)** for full table + Patent 19B aliquot map.

| Site | Coordinates | Modern PPAN | Owner | Acres | Notes |
| --- | --- | --- | --- | --- | --- |
| Horner Homestead | 35.6681, -93.4981 | `001-06308-000` | CRAIN RANDA ET AL | 182.66 | Sec. 19 — patent overlap |
| Moore Cemetery | 35.6666, -93.4955 | `001-06298-001` | DEWBERRY DORIS | 47.73 | No separate cemetery PPAN |
| Moore Homestead | 35.65638, -93.4955 | `001-06512-000` | U S A | 240 | Sec. 36 |
| Bluff / cave / overhang | 35.6583, -93.4888 | `001-06512-000` | U S A | 240 | Sec. 36 timber/federal |
| Overhang A / B | see matrix | `001-06512-000` | U S A | 240 | Same tract |
| Locked gate (primary) | 35.66075, -93.48564 | `001-03571-000` | U S A | 621 | Sec. 31 T12N R23W — **confirmed** |

**Data:** `agiso-matrix-2026-06-16.json` · `gate-corridor-2026-06-17.json` · Scripts: `scripts/scan_access_corridor.py`

---

## Cross-references

- OQ-20 estate/deed search — use **Patent 19B legal description**, not PPAN, in clerk letters
- `grant-readiness/estate-request-oq20.md`
- `index.html` §04 land description · §04b coordinate table

## On completion

- [x] AGISO GIS query — Patent 19B PPAN map + GPS point hits (16 Jun 2026)
- [x] Gate corridor scan — primary `001-03571-000` confirmed (17 Jun 2026)
- [ ] ARCountyData screenshot of gate boundary (optional chain-of-custody)
- [ ] Deposit screenshots in `sources/ppan-001/`
- [ ] Update §13 / §16 on site
- [ ] Log in `sources/INGEST_LOG.md`
- [ ] Optional: add PPAN layer note to `horner-sites.kml`