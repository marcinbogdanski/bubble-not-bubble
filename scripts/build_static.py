"""Build the whole site as static files in site/, for Cloudflare Pages.

Every page is fetched from the FastAPI app in-process, so the static site is
exactly what the dev server shows. Run on the VM, where the Claude chats live:

    uv run python scripts/build_static.py

URL -> file mapping (Cloudflare Pages serves /foo from foo.html):
    /                      index.html
    /claude, /claude/<id>  claude.html, claude/<id>.html (+ <id>.json)
    /<section>/<rel>       <section>/<rel>.html
    /raw/<section>/<rel>.md, /data/*, robots.txt, llms.txt   copied as-is
"""

import shutil
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import content  # noqa: E402
import transcripts  # noqa: E402
from main import app  # noqa: E402

OUT = ROOT / "site"
MAX_FILES = 20_000  # Cloudflare Pages limits
MAX_FILE_BYTES = 25 * 1024 * 1024

# Cloudflare Pages reads this file for response headers.
HEADERS = """\
/*
  X-Robots-Tag: noindex
/raw/*
  Content-Type: text/markdown; charset=utf-8
"""


def main() -> None:
    client = TestClient(app)

    def save(url: str, dest: str) -> None:
        response = client.get(url)
        if response.status_code != 200:
            sys.exit(f"{url} -> HTTP {response.status_code}")
        path = OUT / dest
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    save("/", "index.html")
    save("/robots.txt", "robots.txt")
    save("/llms.txt", "llms.txt")

    save("/claude", "claude.html")
    for session in transcripts.list_sessions():
        save(f"/claude/{session.id}", f"claude/{session.id}.html")
        save(f"/claude/{session.id}.json", f"claude/{session.id}.json")

    # Every .md is a page, including ones hidden from the sidebar (README, TEMPLATE).
    for section in content.SECTIONS:
        folder = ROOT / section
        for md in sorted(folder.rglob("*.md")):
            rel = md.relative_to(folder).with_suffix("").as_posix()
            if any(part.startswith(".") for part in rel.split("/")):
                continue
            save(f"/{section}/{rel}", f"{section}/{rel}.html")
            save(f"/raw/{section}/{rel}.md", f"raw/{section}/{rel}.md")

    shutil.copytree(ROOT / "data", OUT / "data")

    response = client.get("/__missing__")
    (OUT / "404.html").write_bytes(response.content)
    (OUT / "_headers").write_text(HEADERS)

    files = [p for p in OUT.rglob("*") if p.is_file()]
    total = sum(p.stat().st_size for p in files)
    largest = max(files, key=lambda p: p.stat().st_size)
    print(f"Built {len(files)} files, {total / 1e6:.1f} MB, in {OUT.relative_to(ROOT)}/")
    print(f"Largest: {largest.relative_to(OUT)} ({largest.stat().st_size / 1e6:.1f} MB)")
    if len(files) > MAX_FILES or largest.stat().st_size > MAX_FILE_BYTES:
        sys.exit("Over Cloudflare Pages limits (20,000 files, 25 MiB per file)")


if __name__ == "__main__":
    main()
