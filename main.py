from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt
from markupsafe import Markup

import content
import transcripts

ROOT = Path(__file__).resolve().parent
SITE = "https://bubble.bogdanski.ai"

app = FastAPI(title="Bubble or Not Bubble")
templates = Jinja2Templates(directory=ROOT / "templates")

# html=False escapes any raw HTML in transcripts; tables are enabled for readability.
md = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable("table")
templates.env.filters["markdown"] = lambda text: Markup(md.render(text))
templates.env.globals["sections"] = content.SECTIONS


@app.middleware("http")
async def noindex(request: Request, call_next):
    # Public, but kept out of search results. AI crawlers follow robots.txt instead.
    response = await call_next(request)
    response.headers["X-Robots-Tag"] = "noindex"
    return response


@app.get("/robots.txt", response_class=PlainTextResponse)
def robots_txt() -> str:
    return "User-agent: *\nAllow: /\n"


@app.get("/llms.txt", response_class=PlainTextResponse)
def llms_txt() -> str:
    """Index for AI agents: every page as raw markdown, plus the data folder."""
    lines = [
        "# Bubble or Not Bubble",
        "",
        "A live, evidence-backed research report on the economics of AI: is the current",
        "AI investment boom a bubble or not? Built by AI agents steered by a human.",
        f"Source: https://github.com/marcinbogdanski/bubble-not-bubble . Data files: {SITE}/data/",
        "",
    ]
    for section, label in content.SECTIONS.items():
        pages = content.list_pages(section)
        if not pages:
            continue
        lines += [f"## {label}", ""]
        lines += [f"- [{p.title}]({SITE}{p.raw_url}) (html: {SITE}{p.url})" for p in pages]
        lines.append("")
    return "\n".join(lines)


def render(request: Request, name: str, **context) -> HTMLResponse:
    context["nav"] = content.nav()
    context["sessions"] = transcripts.list_sessions()
    context["path"] = request.url.path
    return templates.TemplateResponse(request, name, context)


def render_page(request: Request, page: content.Page) -> HTMLResponse:
    return render(request, "page.html", page=page, body=page.text())


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    page = content.get_page("report", "index")
    if not page:
        raise HTTPException(404, "report/index.md is missing")
    return render_page(request, page)


@app.get("/claude", response_class=HTMLResponse)
def claude_index(request: Request):
    return render(request, "claude_index.html")


@app.get("/claude/{session_id}.json")
def claude_session_json(session_id: str) -> dict:
    session = transcripts.get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    return {
        "id": session.id,
        "title": session.title,
        "started": session.started,
        "messages": [
            {"role": m.role, "timestamp": m.timestamp, "text": m.text, "images": m.images}
            for m in session.messages
        ],
    }


@app.get("/claude/{session_id}", response_class=HTMLResponse)
def claude_session(request: Request, session_id: str):
    session = transcripts.get_session(session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    return render(request, "claude_session.html", session=session)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# Mounted before the catch-all markdown route so /data/* is served as files.
app.mount("/data", StaticFiles(directory=ROOT / "data"), name="data")


@app.get("/raw/{section}/{rel:path}")
def raw_page(section: str, rel: str):
    page = content.get_page(section, rel)
    if not page:
        raise HTTPException(404, "Page not found")
    return Response(page.text(), media_type="text/markdown; charset=utf-8")


@app.get("/{section}/{rel:path}", response_class=HTMLResponse)
def markdown_page(request: Request, section: str, rel: str):
    """Rendered page. Both /research/stack/nvidia and /research/stack/nvidia.md work,
    so relative links written in markdown resolve in the browser too."""
    page = content.get_page(section, rel)
    if not page:
        raise HTTPException(404, "Page not found")
    return render_page(request, page)

