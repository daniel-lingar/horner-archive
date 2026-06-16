"""Compress Moore Cemetery field photos for GitHub Pages."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "00_INBOX" / "auto-ingest" / "horner-archive" / "2026-06-15"
OUT = ROOT / "field-docs"

PHOTOS = [
    ("image (49).jpg", "moore-cemetery-stones-row-01.jpg", "Four Horner family stones in situ — Moore Cemetery"),
    ("image (50).jpg", "moore-cemetery-stones-row-02.jpg", "Permelia, Spencer, and William Riley Horner markers"),
    ("image (53).jpg", "moore-cemetery-overview.jpg", "Moore Cemetery overview — wooded hilltop burial ground"),
    ("image (62).jpg", "moore-cemetery-panorama.jpg", "Panoramic view of Moore Cemetery clearing"),
    ("image (66).jpg", "moore-cemetery-permelia-stone.jpg", "Permelia Turner Horner tombstone — d. Aug 9, 1892"),
    ("image (68).jpg", "moore-cemetery-stone-detail.jpg", "Horner family marker detail — Moore Cemetery"),
]

MAX_WIDTH = 1400
JPEG_QUALITY = 82


def optimize(src: Path, dest: Path) -> None:
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > MAX_WIDTH:
            ratio = MAX_WIDTH / im.width
            im = im.resize((MAX_WIDTH, int(im.height * ratio)), Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for src_name, dest_name, caption in PHOTOS:
        src = INBOX / src_name
        if not src.exists():
            raise FileNotFoundError(src)
        dest = OUT / dest_name
        optimize(src, dest)
        size_kb = dest.stat().st_size // 1024
        manifest.append((dest_name, caption, size_kb))
        print(f"Wrote {dest_name} ({size_kb} KB)")

    index_path = OUT / "manifest.txt"
    lines = [f"{name}\t{caption}\t{size_kb} KB" for name, caption, size_kb in manifest]
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()