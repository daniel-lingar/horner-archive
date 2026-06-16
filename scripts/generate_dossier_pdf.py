"""Generate dossier.pdf from the live archive HTML using headless Edge."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
OUTPUT = ROOT / "dossier.pdf"

EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
]


def find_browser() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No Edge or Chrome executable found for PDF export")


def main() -> None:
    if not HTML.exists():
        raise FileNotFoundError(HTML)

    browser = find_browser()
    file_url = HTML.resolve().as_uri()
    if OUTPUT.exists():
        OUTPUT.unlink()

    cmd = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT}",
        file_url,
    ]
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        raise SystemExit(result.returncode)

    if not OUTPUT.exists() or OUTPUT.stat().st_size < 10000:
        raise RuntimeError(f"PDF generation failed or produced tiny file: {OUTPUT}")

    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()