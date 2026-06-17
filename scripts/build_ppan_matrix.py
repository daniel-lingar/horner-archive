#!/usr/bin/env python3
"""Build OQ-PPAN-001 matrix from Arkansas AGISO assessor CAMA layer."""
import json
import urllib.parse
import urllib.request

BASE = (
    "https://gis.arkansas.gov/arcgis/rest/services/"
    "FEATURESERVICES/Planning_Cadastre/FeatureServer/6/query"
)
FIELDS = (
    "parcelid,ownername,parcellgl,section,township,range,str,taxarea,"
    "totalvalue,adrlabel,assessvalue,landvalue,countyfips"
)
COUNTY = "countyfips='05071' AND township='12' AND range='24'"


def query(**params):
    params["f"] = "json"
    url = BASE + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=90) as resp:
        return json.load(resp)


def parcel_rows(section: int) -> list[dict]:
    data = query(
        where=f"{COUNTY} AND section={section}",
        outFields=FIELDS,
        returnGeometry="false",
        resultRecordCount=200,
    )
    rows = []
    for f in data.get("features", []):
        a = f["attributes"]
        rows.append(
            {
                "ppan": a.get("parcelid"),
                "owner": a.get("ownername"),
                "acres": a.get("taxarea"),
                "legal": a.get("parcellgl"),
                "section": a.get("section"),
                "str": a.get("str"),
            }
        )
    return sorted(rows, key=lambda r: r["ppan"] or "")


def point_hit(name: str, lat: float, lon: float) -> list[dict]:
    geom = json.dumps({"x": lon, "y": lat, "spatialReference": {"wkid": 4326}})
    data = query(
        geometry=geom,
        geometryType="esriGeometryPoint",
        inSR=4326,
        spatialRel="esriSpatialRelIntersects",
        outFields=FIELDS,
        returnGeometry="false",
    )
    hits = []
    for f in data.get("features", []):
        a = f["attributes"]
        if a.get("countyfips") != "05071":
            continue
        hits.append(
            {
                "site": name,
                "ppan": a.get("parcelid"),
                "owner": a.get("ownername"),
                "acres": a.get("taxarea"),
                "legal": a.get("parcellgl"),
                "section": a.get("section"),
                "township": a.get("township"),
                "range": a.get("range"),
            }
        )
    return hits


def main():
    sec19 = parcel_rows(19)
    sec22 = parcel_rows(22)
    sec23 = parcel_rows(23)

    sites = [
        ("Horner Homestead", 35.6681, -93.4981),
        ("Moore Cemetery", 35.6666, -93.4955),
        ("Moore Homestead", 35.65638, -93.4955),
        ("Bluff / Cave / Overhang", 35.6583, -93.4888),
        ("Overhang Target A", 35.65885, -93.4893),
        ("Overhang Target B", 35.6579, -93.4885),
    ]
    points = []
    for name, lat, lon in sites:
        points.extend(point_hit(name, lat, lon))

    out = {
        "source": "Arkansas AGISO Planning_Cadastre layer 6 (CAMA Jun 2026)",
        "study_area": "T12N R24W Sec 19 & 22 — Patent 19B",
        "section_19_parcels": sec19,
        "section_22_parcels": sec22,
        "section_23_nearby": sec23,
        "gps_point_hits": points,
    }
    path = "sources/ppan-001/agiso-matrix-2026-06-16.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()