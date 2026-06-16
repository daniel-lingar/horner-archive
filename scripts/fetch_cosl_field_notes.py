"""Fetch COSL transcribed GLO field notes for a township/range."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "glo-field-notes-t12n-r24w"

BUNDLES = [
    {"quarter": "NW", "township": "12", "range": "24", "book": "225A", "bundle": "BD0078"},
    {"quarter": "NW", "township": "12", "range": "24", "book": "913A", "bundle": "BD0164"},
]


def get_json(url: str) -> object:
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.loads(resp.read().decode())


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as resp:
        dest.write_bytes(resp.read())


def fetch_bundle(book: str, bundle: str) -> list[dict]:
    api = (
        "https://cosl.org/History/LouisianaPurchase/"
        f"GetTranscribedThumbnailsByBookBundle?bundle={bundle}&book={urllib.parse.quote(book)}"
    )
    pages = get_json(api)
    manifest: list[dict] = []
    slug = f"{book}-{bundle}".replace("/", "-")
    for page in pages:
        seq = int(page["seq"])
        # Full-resolution transcribed pages (LPSFNT); thumbnails use TLPSFNT prefix.
        path = page.get("path", "")
        img_url = f"https://coslstorage.blob.core.windows.net/history-docs/{path}"
        fname = f"{slug}-page-{seq:03d}.jpg"
        dest = OUT / fname
        if not dest.exists() or dest.stat().st_size < 1000:
            download(img_url, dest)
        manifest.append(
            {
                "book": book,
                "bundle": bundle,
                "seq": seq,
                "file": fname,
                "url": img_url,
                "path": page.get("path"),
                "viewer": f"https://cosl.org/History/LouisianaPurchase/Viewer?PT={page.get('path', '').replace('/', chr(92))}&BD={bundle}&BK={book}&SQ={seq}",
            }
        )
        print(f"  {fname} ({dest.stat().st_size // 1024} KB)")
    return manifest


def main() -> None:
    all_manifest: list[dict] = []
    for item in BUNDLES:
        print(f"Fetching Book {item['book']} / {item['bundle']} (T{item['township']}N R{item['range']}W, {item['quarter']} quarter)...")
        all_manifest.extend(fetch_bundle(item["book"], item["bundle"]))

    meta = {
        "township": "12N",
        "range": "24W",
        "meridian": "Fifth Principal (Louisiana Purchase)",
        "county": "Johnson County, Arkansas",
        "patent_sections": [19, 22],
        "source": "Arkansas Commissioner of State Lands — Transcribed Field Notes",
        "search_url": "https://cosl.org/History/LouisianaPurchase/TranscribedFieldNotesTownshipRange",
        "bundles": BUNDLES,
        "pages": all_manifest,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manifest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote {len(all_manifest)} pages to {OUT}")


if __name__ == "__main__":
    main()