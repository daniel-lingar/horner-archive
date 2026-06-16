# Patent 19B → Modern PPAN Map (AGISO GIS pull)

**Source:** Arkansas GIS Office statewide parcel layer (`Planning_Cadastre` FeatureServer layer 6)  
**Query date:** 16 Jun 2026 · Johnson County FIPS `05071` · `T12N R24W`  
**Script:** `scripts/query_ppan_001.py` · Full log: `agiso-query-2026-06-16.txt`

**Caveat:** AGISO publishes that cadastral polygons are approximate and not legal boundaries. Point-in-polygon at GPS coordinates can return unexpected sections when rural coverage is coarse. **Verify on ARCountyData** before citing in correspondence.

---

## Patent 19B aliquot → best modern PPAN matches

| Patent aliquot (1857) | Modern PPAN | Owner (2026) | Acres | Modern legal (abbrev.) |
| --- | --- | --- | --- | --- |
| **NE¼ SE¼, Sec. 19** | `001-06302-001` | OARK SD #7 | 7.09 | PT SE NE |
| | `001-06303-000` | WARREN THOMAS SAMUEL TRUST | 19.99 | PT SE NE |
| | `001-06313-000` | WARREN THOMAS SAMUEL TRUST | 40.0 | NE SE |
| **NW¼ SE¼, Sec. 19** | `001-06301-000` | FARMER AUDREY & RISHELLE WILSON | 1.6 | PT SW NE |
| | `001-06301-001` | WILSON RISHELLE L | 2.3 | PT SW NE |
| **NW¼ NW¼, Sec. 22** | `001-06380-000` | KIMBRIEL CHARLOTTE | 0.24 | PT NW NE |
| | `001-06393-000` | COOK CATHIE B | 6.79 | NE NW |
| **SE¼ NW¼, Sec. 22** | `001-06393-001` | ARBAUGH IMOGENE | 24.9 | PT SE NW |
| | `001-06393-002` | QUALITY RESTORATION OF ARKANSAS | 0.87 | PT SE NW |

### Large surrounding tract (Sec. 19 — may cover homestead area)

| PPAN | Owner | Acres | Legal | Notes |
| --- | --- | --- | --- | --- |
| `001-06308-000` | CRAIN RANDA ET AL | 182.66 | SE NW, E2 SW, W2 SW, SW SE | Dominant Sec. 19 block west of patent aliquots |

### Dewberry corridor (Sec. 23 — cemetery access context)

| PPAN | Owner | Acres | Legal | Notes |
| --- | --- | --- | --- | --- |
| `001-06408-000` | **DEWBERRY DORIS TRUST** | 127.0 | S2 SW, PT SE SE SW SE | Same surname as GPS surveyor Jimmie Dewberry (2003) |

---

## GPS point-in-polygon (AGISO — verify in field)

| Site | Coordinates | AGISO hit PPAN | Owner | Sec | Caveat |
| --- | --- | --- | --- | --- | --- |
| Horner homestead | 35.6681, -93.4981 | `001-06437-000` | YORK EDWARD V & MELISSA K | 25 | **Conflicts with Patent Sec. 19** — GIS imprecision likely |
| Moore Cemetery | 35.6666, -93.4955 | `001-06437-000` | YORK EDWARD V & MELISSA K | 25 | Same polygon as homestead hit |
| Moore Cemetery (KML) | 35.66217, -93.4955 | `001-06435-000` | U S A | 25 | Federal tract |
| Moore homestead | 35.65638, -93.4955 | `001-06512-000` | U S A | 36 | Approximate point |
| Bluff / cave | 35.6583, -93.4888 | `001-06512-000` | U S A | 36 | Large federal parcel |
| Overhang A / B | 35.65885, -93.4893 / 35.6579, -93.4885 | `001-06512-000` | U S A | 36 | Same |
| Locked gate | 35.64768, -93.4955 | `001-06521-000` | GALLOWAY LAND CO LLC | 36 | 200 ac |

**Interpretation:** GPS points for homestead/cemetery did not fall inside Sec. 19/22 polygons in AGISO. Use **Patent 19B PPAN table above** for land-title work; use **GPS hits** only after ARCountyData map confirmation.