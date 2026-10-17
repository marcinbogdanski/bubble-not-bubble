"""Markdown content of the report: report/, research/, forecasts/, signals/.

Every .md file in those folders is a page. The first H1 is its title. Pages are
served rendered (HTML) and raw (text/markdown, for agents), see main.py.
"""

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Section slug -> (folder, nav label). Order is the sidebar order.
SECTIONS = {
    "report": "Report",
    "forecasts": "Forecasts",
    "signals": "Signals",
    "research": "Research",
}

# Report pages in reading order; anything else in report/ follows alphabetically.
REPORT_ORDER = ["index", "theory", "stack", "methodology"]

# Reachable by URL, but not listed in the sidebar or llms.txt.
HIDDEN = {"README", "TEMPLATE"}

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Page:
    section: str
    rel: str  # path inside the section, no extension, e.g. "stack/nvidia"
    path: Path
    title: str

    @property
    def url(self) -> str:
        return "/" if (self.section, self.rel) == ("report", "index") else f"/{self.section}/{self.rel}"

    @property
    def raw_url(self) -> str:
        return f"/raw/{self.section}/{self.rel}.md"

    @property
    def group(self) -> str:
        return self.rel.rsplit("/", 1)[0] if "/" in self.rel else ""

    @property
    def updated(self) -> datetime:
        return datetime.fromtimestamp(self.path.stat().st_mtime, tz=timezone.utc)

    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")


def _title(path: Path) -> str:
    try:
        m = H1_RE.search(path.read_text(encoding="utf-8"))
    except OSError:
        m = None
    return m.group(1) if m else path.stem.replace("-", " ").title()


def _sort_key(page: Page):
    if page.section == "report":
        i = REPORT_ORDER.index(page.rel) if page.rel in REPORT_ORDER else len(REPORT_ORDER)
        return (i, page.rel)
    if page.section == "signals":
        return (0, "")  # sorted separately, newest first
    return (0, page.rel)


def list_pages(section: str) -> list[Page]:
    folder = ROOT / section
    if section not in SECTIONS or not folder.is_dir():
        return []
    pages = [
        Page(section, p.relative_to(folder).with_suffix("").as_posix(), p, _title(p))
        for p in folder.rglob("*.md")
        if not any(part.startswith(".") for part in p.relative_to(folder).parts)
        and p.stem not in HIDDEN
    ]
    if section == "signals":
        return sorted(pages, key=lambda p: p.rel, reverse=True)
    return sorted(pages, key=_sort_key)


def get_page(section: str, rel: str) -> Page | None:
    if section not in SECTIONS:
        return None
    rel = rel.removesuffix(".md").strip("/")
    if not rel or ".." in rel.split("/"):
        return None
    folder = (ROOT / section).resolve()
    path = (folder / f"{rel}.md").resolve()
    if not path.is_file() or folder not in path.parents:
        return None
    return Page(section, rel, path, _title(path))


def nav() -> dict[str, list[Page]]:
    return {section: list_pages(section) for section in SECTIONS}
