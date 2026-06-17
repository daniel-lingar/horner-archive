"""Scan local images for 1860 Johnson County Floyd census pages."""
from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

INBOX = Path(
    r"C:\Users\linga\repo-auto-ingest\repos\horner-archive"
    r"\00_INBOX\auto-ingest\horner-archive\2026-06-15"
)
OUT = Path(r"C:\Users\linga\AppData\Local\Temp\census_scan")
OUT.mkdir(parents=True, exist_ok=True)

KEYWORDS = re.compile(
    r"981|982|johnson|floyd|homer|horne|arkansas|mulberry",
    re.I,
)


def thumb(path: Path, max_side: int = 1400) -> Path:
    dest = OUT / f"{path.stem}_thumb.jpg"
    if dest.exists():
        return dest
    img = Image.open(path)
    img.thumbnail((max_side, max_side))
    img.convert("RGB").save(dest, quality=85)
    return dest


def ocr(path: Path) -> str:
    try:
        import pytesseract
    except ImportError:
        return ""
    return pytesseract.image_to_string(Image.open(path))


def scan_folder(folder: Path, pattern: str = "*.jpg") -> None:
    files = sorted(folder.glob(pattern))
    print(f"Scanning {len(files)} files in {folder}")
    for f in files:
        if "_1." in f.name:
            continue
        t = thumb(f)
        text = ocr(t)
        if KEYWORDS.search(text):
            hits = sorted(set(KEYWORDS.findall(text)), key=str.lower)
            print(f"MATCH {f.name}: {hits}")
            snippet = " ".join(text.split())[:200]
            print(f"  {snippet}")


if __name__ == "__main__":
    scan_folder(INBOX)