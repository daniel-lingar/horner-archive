"""Extract 1942 transcript and census references from dossier v9 docx."""
import html
import re
import zipfile
from pathlib import Path

DOCX = Path(
    r"C:\Users\linga\Documents\Lingar-Archive\03-Horner-Hill-Archive\Horner"
    r"\Horner_Research_Dossier_v9 (1).docx"
)
OUT = Path(__file__).resolve().parents[1] / "sources" / "1942_transcript_excerpts.txt"

KEYWORDS = (
    "1942",
    "Eva Horner",
    "From the 1942",
    "seventeen",
    "1860 census",
    "page 982",
    "page 981",
    "Real Estate",
    "Personal Estate",
    "Homer",
    "Joseph Hill",
)


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
    xml = re.sub(r"<w:tab[^/]*/>", "\t", xml)
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    return html.unescape(xml)


def main() -> None:
    text = docx_text(DOCX)
    hits = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if any(k.lower() in stripped.lower() for k in KEYWORDS):
            hits.append(stripped)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n\n".join(hits), encoding="utf-8")
    print(f"Wrote {len(hits)} lines to {OUT}")
    for line in hits[:40]:
        print(line[:280])


if __name__ == "__main__":
    main()