#!/usr/bin/env python3
"""Scan access corridor for parcel boundary crossings (gate candidates)."""
import json
import math
import urllib.parse
import urllib.request

BASE = (
    "https://gis.arkansas.gov/arcgis/rest/services/"
    "FEATURESERVICES/Planning_Cadastre/FeatureServer/6/query"
)
FIELDS = "parcelid,ownername,parcellgl,section,township,range,taxarea"


def parcel_at(lat, lon):
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
    if not d.get("features"):
        return None
    a = d["features"][0]["attributes"]
    return {
        "ppan": a.get("parcelid"),
        "owner": a.get("ownername"),
        "acres": a.get("taxarea"),
        "legal": a.get("parcellgl"),
        "sec": a.get("section"),
        "twp": a.get("township"),
        "rng": a.get("range"),
    }


def scan_line(name, lat1, lon1, lat2, lon2, steps=30):
    print(f"\n=== Corridor: {name} ===")
    prev = None
    for i in range(steps + 1):
        t = i / steps
        lat = lat1 + (lat2 - lat1) * t
        lon = lon1 + (lon2 - lon1) * t
        p = parcel_at(lat, lon)
        key = p["ppan"] if p else "NONE"
        if key != (prev["ppan"] if prev else None):
            if p:
                print(
                    f"  BOUNDARY @ {lat:.5f}, {lon:.5f} -> "
                    f"{p['ppan']} | {p['owner']} | {p['acres']} ac | "
                    f"Sec {p['sec']} T{p['twp']}N R{p['rng']}W | {p['legal']}"
                )
            else:
                print(f"  GAP @ {lat:.5f}, {lon:.5f}")
            prev = p


def main():
    # KML access line: gate -> homestead -> cemetery (same meridian)
    scan_line(
        "KML meridian -93.4955 (gate to cemetery)",
        35.64768, -93.4955,
        35.6666, -93.4955,
        steps=40,
    )
    # Jimmie bearing: cemetery SSE ~1 mi to gate estimate
    scan_line(
        "Cemetery to Jimmie gate estimate (SSE)",
        35.6666, -93.4955,
        35.658, -93.481,
        steps=25,
    )
    # Low Gap approach: Ozone area toward Y-junction
    scan_line(
        "Hwy 86 / Low Gap approach (Ozone toward Y)",
        35.6353, -93.445,
        35.648, -93.471,
        steps=20,
    )


if __name__ == "__main__":
    main()