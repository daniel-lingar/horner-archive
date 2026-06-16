#!/usr/bin/env python3
"""Query Arkansas statewide parcel GIS for OQ-PPAN-001 sites."""
import json
import urllib.parse
import urllib.request

BASE = (
    "https://gis.arkansas.gov/arcgis/rest/services/"
    "FEATURESERVICES/Planning_Cadastre/FeatureServer/6/query"
)
FIELDS = "parcelid,ownername,parcellgl,section,township,range,str,taxarea,totalvalue,adrlabel"


def query(**params):
    params["f"] = "json"
    url = BASE + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def main():
    data = query(
        where="countyfips='05071' AND township='12' AND range='24'",
        outFields=FIELDS,
        returnGeometry="false",
        resultRecordCount=200,
    )
    feats = data.get("features", [])
    print(f"=== T12N R24W Johnson — {len(feats)} parcels ===")
    for f in sorted(
        feats,
        key=lambda x: (
            x["attributes"].get("section") or 0,
            x["attributes"].get("parcelid") or "",
        ),
    ):
        a = f["attributes"]
        owner = (a.get("ownername") or "")[:42]
        lgl = (a.get("parcellgl") or "")[:70]
        print(
            f"{a.get('parcelid','?'):18} Sec {str(a.get('section','?')):>2}  "
            f"{a.get('taxarea','?')} ac  {owner:42}  {lgl}"
        )

    sites = [
        ("Horner homestead", 35.6681, -93.4981),
        ("Moore Cemetery", 35.6666, -93.4955),
        ("Moore Cemetery KML", 35.66217, -93.4955),
        ("Moore homestead", 35.65638, -93.4955),
        ("Bluff cave", 35.6583, -93.4888),
        ("Overhang A", 35.65885, -93.4893),
        ("Overhang B", 35.6579, -93.4885),
        ("Locked gate", 35.64768, -93.4955),
    ]
    print()
    for name, lat, lon in sites:
        geom = json.dumps(
            {"x": lon, "y": lat, "spatialReference": {"wkid": 4326}}
        )
        d = query(
            geometry=geom,
            geometryType="esriGeometryPoint",
            inSR=4326,
            spatialRel="esriSpatialRelIntersects",
            outFields=FIELDS,
            returnGeometry="false",
        )
        print(f"=== {name} ({lat}, {lon}) ===")
        if not d.get("features"):
            print("  NO PARCEL POLYGON")
        for f in d["features"]:
            a = f["attributes"]
            print(f"  {a.get('parcelid')} | {a.get('ownername')}")
            print(f"    Sec {a.get('section')} T{a.get('township')}N R{a.get('range')}W | {a.get('taxarea')} ac")
            print(f"    {a.get('parcellgl')}")


if __name__ == "__main__":
    main()