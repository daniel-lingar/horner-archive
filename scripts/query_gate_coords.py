#!/usr/bin/env python3
"""Query gate coordinate candidates for OQ-PPAN-001."""
import json
import urllib.parse
import urllib.request

BASE = (
    "https://gis.arkansas.gov/arcgis/rest/services/"
    "FEATURESERVICES/Planning_Cadastre/FeatureServer/6/query"
)
FIELDS = "parcelid,ownername,parcellgl,section,township,range,taxarea,str"


def hit(name, lat, lon):
    geom = json.dumps({"x": lon, "y": lat, "spatialReference": {"wkid": 4326}})
    params = {
        "geometry": geom,
        "geometryType": "esriGeometryPoint",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": FIELDS,
        "returnGeometry": "false",
        "where": "countyfips='05071'",
        "f": "json",
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)
    print(f"=== {name} ({lat}, {lon}) ===")
    if not d.get("features"):
        print("  NO HIT")
    for f in d["features"]:
        a = f["attributes"]
        print(f"  PPAN: {a.get('parcelid')}")
        print(f"  Owner: {a.get('ownername')}")
        print(f"  Acres: {a.get('taxarea')}")
        print(f"  Legal: {a.get('parcellgl')}")
        print(
            f"  Sec {a.get('section')} T{a.get('township')}N "
            f"R{a.get('range')}W  STR={a.get('str')}"
        )
    print()


def main():
    sites = [
        ("Gate Jimmie estimate (walkthrough)", 35.658, -93.481),
        ("Gate KML locked cable (archive)", 35.64768, -93.4955),
        ("Cemetery cluster", 35.6666, -93.4955),
        ("Moore homestead", 35.65638, -93.4955),
        ("Y-junction area approx", 35.648, -93.471),
        ("Ozone reference", 35.6353, -93.445),
        ("Bluff overhang", 35.6583, -93.4888),
    ]
    for s in sites:
        hit(*s)


if __name__ == "__main__":
    main()