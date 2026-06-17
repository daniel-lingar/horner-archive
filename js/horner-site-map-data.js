/* OQ-PPAN-001 site map data — Johnson County, Jun 2026 assessor feed */
window.HORNER_MAP_DATA = {
  studyAnchor: "Patent 19B · T12N R24W · Sec. 19 & 22",
  source: "Arkansas AGISO CAMA / Johnson County assessor (Jun 2026)",
  markers: [
    {
      id: "gate-primary",
      name: "Locked Gate (Primary — Confirmed)",
      lat: 35.66075,
      lng: -93.48564,
      group: "access",
      color: "#e67e22",
      radius: 9,
      ppan: "001-03571-000",
      owner: "U S A",
      acres: 621.0,
      legal: "SECTION — S31 T12N R23W",
      note: "Federal timber boundary ≈0.9 mi SSE of cemetery. South parcel: 001-06435-000 (U.S.A., 240 ac, S25)."
    },
    {
      id: "gate-legacy",
      name: "Locked Gate (Legacy — Discard)",
      lat: 35.64768,
      lng: -93.4955,
      group: "access",
      color: "#999999",
      radius: 6,
      ppan: "001-06521-000",
      owner: "GALLOWAY LAND CO LLC",
      acres: 200.0,
      legal: "S2 SW NE SE S2 SE — S36 T12N R24W",
      note: "Troy-era estimate. Not Jimmie-corrected — do not use for navigation."
    },
    {
      id: "cemetery",
      name: "Moore Cemetery",
      lat: 35.6666,
      lng: -93.4955,
      group: "sites",
      color: "#8b1a1a",
      radius: 9,
      ppan: "001-06298-001",
      owner: "DEWBERRY DORIS",
      acres: 47.73,
      legal: "PT NE NE — S19 T12N R24W",
      note: "Spencer, William, Permelia Horner. No separate cemetery PPAN."
    },
    {
      id: "horner-homestead",
      name: "Spencer Horner Homestead",
      lat: 35.6681,
      lng: -93.4981,
      group: "sites",
      color: "#6b3a2a",
      radius: 9,
      ppan: "001-06308-000",
      owner: "CRAIN RANDA ET AL",
      acres: 182.66,
      legal: "SE NW; E2 SW; W2 SW; SW SE — S19 T12N R24W",
      note: "Attack site — Aug 2, 1864. GLO field notes: G. Homers field."
    },
    {
      id: "moore-homestead",
      name: "Moore Homestead / Old Moore Place",
      lat: 35.65638,
      lng: -93.4955,
      group: "sites",
      color: "#2d6a4f",
      radius: 7,
      ppan: "001-06512-000",
      owner: "U S A",
      acres: 240.0,
      legal: "NE4 E2 NW — S36 T12N R24W",
      note: "Approximate KML point — field-check."
    },
    {
      id: "bluff",
      name: "Bluff / Cave Refuge",
      lat: 35.6583,
      lng: -93.4888,
      group: "sites",
      color: "#3d5a80",
      radius: 8,
      ppan: "001-06512-000",
      owner: "U S A",
      acres: 240.0,
      legal: "NE4 E2 NW — S36 T12N R24W",
      note: "William Riley Horner — died Aug 10, 1864."
    },
    {
      id: "overhang-a",
      name: "Overhang Target A",
      lat: 35.65885,
      lng: -93.4893,
      group: "sites",
      color: "#5c7aea",
      radius: 6,
      ppan: "001-06512-000",
      owner: "U S A",
      acres: 240.0,
      legal: "NE4 E2 NW — S36 T12N R24W",
      note: "KML shelter investigation target A."
    },
    {
      id: "overhang-b",
      name: "Overhang Target B",
      lat: 35.6579,
      lng: -93.4885,
      group: "sites",
      color: "#5c7aea",
      radius: 6,
      ppan: "001-06512-000",
      owner: "U S A",
      acres: 240.0,
      legal: "NE4 E2 NW — S36 T12N R24W",
      note: "KML shelter investigation target B."
    },
    {
      id: "ozone",
      name: "Ozone, AR",
      lat: 35.6353,
      lng: -93.445,
      group: "reference",
      color: "#7a6a5a",
      radius: 6,
      note: "Nearest community. Hwy 86 / Low Gap Road west ~2.3 mi to Y-junction."
    },
    {
      id: "y-junction",
      name: "Y-Junction (approx.)",
      lat: 35.648,
      lng: -93.471,
      group: "reference",
      color: "#7a6a5a",
      radius: 5,
      note: "Low Gap Rd west of Ozone — NW fork toward Moore cluster."
    }
  ],
  corridors: [
    {
      id: "jimmie-sse",
      name: "Primary access (Jimmie SSE)",
      group: "access",
      color: "#e67e22",
      weight: 4,
      dash: null,
      opacity: 0.9,
      coords: [
        [35.66075, -93.48564],
        [35.66488, -93.4926],
        [35.66626, -93.49492],
        [35.6666, -93.4955]
      ]
    },
    {
      id: "legacy-meridian",
      name: "Legacy meridian (discard)",
      group: "access",
      color: "#999999",
      weight: 2,
      dash: "8 6",
      opacity: 0.45,
      coords: [
        [35.64768, -93.4955],
        [35.65052, -93.4955],
        [35.65241, -93.4955],
        [35.6543, -93.4955],
        [35.6614, -93.4955],
        [35.66518, -93.4955],
        [35.6666, -93.4955]
      ]
    },
    {
      id: "low-gap-approach",
      name: "Low Gap approach (Ozone → Y)",
      group: "reference",
      color: "#7a6a5a",
      weight: 2,
      dash: "4 6",
      opacity: 0.55,
      coords: [
        [35.6353, -93.445],
        [35.648, -93.471]
      ]
    }
  ],
  legend: [
    { label: "Primary gate (confirmed)", color: "#e67e22", shape: "circle" },
    { label: "Moore Cemetery", color: "#8b1a1a", shape: "circle" },
    { label: "Horner homestead", color: "#6b3a2a", shape: "circle" },
    { label: "Federal / timber (U.S.A.)", color: "#3d5a80", shape: "circle" },
    { label: "Primary access corridor", color: "#e67e22", shape: "line" },
    { label: "Legacy corridor (discard)", color: "#999999", shape: "dashed" }
  ]
};