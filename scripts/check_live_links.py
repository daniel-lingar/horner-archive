"""Check internal GitHub Pages links for horner-archive."""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://daniel-lingar.github.io/horner-archive/"
ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = list(ROOT.rglob("*.html"))


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag == "a" and attr_map.get("href"):
            self.links.append(("href", attr_map["href"]))
        elif tag in {"img", "script", "link"}:
            key = "src" if tag != "link" else "href"
            if attr_map.get(key):
                self.links.append((key, attr_map[key]))


def normalize(url: str, page_url: str) -> str | None:
    url = url.strip()
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/"):
        return urllib.parse.urljoin("https://daniel-lingar.github.io/", url.lstrip("/"))
    return urllib.parse.urljoin(page_url, url)


def check(url: str) -> tuple[int | str, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "horner-link-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.geturl()
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405}:
            req = urllib.request.Request(url, headers={"User-Agent": "horner-link-check/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    return resp.status, resp.geturl()
            except urllib.error.HTTPError as exc2:
                return exc2.code, str(exc2.reason)
        return exc.code, str(exc.reason)
    except Exception as exc:  # noqa: BLE001
        return "ERR", str(exc)


def main() -> int:
    seen: set[str] = set()
    internal: list[tuple[str, str, str]] = []
    external: list[tuple[str, str, str]] = []

    for html_file in HTML_FILES:
        rel = html_file.relative_to(ROOT).as_posix()
        page_url = urllib.parse.urljoin(BASE, rel)
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        for kind, raw in parser.links:
            resolved = normalize(raw, page_url)
            if not resolved or resolved in seen:
                continue
            seen.add(resolved)
            bucket = internal if "daniel-lingar.github.io/horner-archive" in resolved else external
            bucket.append((rel, kind, resolved))

    print(f"Checking {len(internal)} internal + {len(external)} external links...\n")
    broken_internal: list[tuple[str, str, str, object]] = []
    broken_external: list[tuple[str, str, str, object]] = []

    for source, kind, url in sorted(internal):
        status, detail = check(url)
        mark = "OK" if isinstance(status, int) and status < 400 else "FAIL"
        print(f"[{mark}] {status} {kind} {url}\n    from {source}")
        if mark == "FAIL":
            broken_internal.append((source, kind, url, status))

    print("\n--- External (sample failures only) ---")
    for source, kind, url in sorted(external):
        status, detail = check(url)
        if not (isinstance(status, int) and status < 400):
            print(f"[FAIL] {status} {kind} {url}\n    from {source}")
            broken_external.append((source, kind, url, status))

    print("\n=== Summary ===")
    print(f"Internal: {len(internal) - len(broken_internal)}/{len(internal)} OK")
    print(f"External failures: {len(broken_external)}")
    if broken_internal:
        print("\nBroken internal links:")
        for item in broken_internal:
            print(f"  - {item[2]} ({item[3]}) in {item[0]}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())