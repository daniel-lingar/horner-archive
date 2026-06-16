"""Publish 1860 Floyd Township census images from inbox to sources/census-1860/."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "00_INBOX" / "census-1860"
OUT = ROOT / "sources" / "census-1860"

# Google Doc PDF export page 7 = Johnson Co. Floyd Township sheets 981-982 (Horner cluster)
SOURCE = INBOX / "google-doc-export-page-07.png"
DEST = OUT / "floyd-township-pages-981-982-horner-cluster.jpg"
MAX_WIDTH = 1600
JPEG_QUALITY = 85


def optimize(src: Path, dest: Path) -> int:
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > MAX_WIDTH:
            ratio = MAX_WIDTH / im.width
            im = im.resize((MAX_WIDTH, int(im.height * ratio)), Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)
    return dest.stat().st_size // 1024


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Missing {SOURCE}. Export 1860 census.pdf page 7 to 00_INBOX/census-1860/ first."
        )
    OUT.mkdir(parents=True, exist_ok=True)
    size_kb = optimize(SOURCE, DEST)
    manifest = OUT / "manifest.txt"
    lines = [
        f"{DEST.name}\tFloyd Township pp. 981-982 — W.R. Horne (l.35-38) and John T. Homer (l.1-7)\t{size_kb} KB",
        "Source: Google Doc export of 1860 census.pdf (Johnson County, Floyd Township)",
        "NARA M653 roll 44 · Enumerator A.M. Marshall · June 1860",
    ]
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {DEST} ({size_kb} KB)")
    print(f"Wrote {manifest}")


if __name__ == "__main__":
    main()