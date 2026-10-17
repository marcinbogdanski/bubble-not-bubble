from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt
from markupsafe import Markup

import transcripts

app = FastAPI(title="Bubble or Not Bubble")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# html=False escapes any raw HTML in transcripts; tables are enabled for readability.
md = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable("table")
templates.env.filters["markdown"] = lambda text: Markup(md.render(text))


def render(request: Request, name: str, **context) -> HTMLResponse:
    context["sessions"] = transcripts.list_sessions()
    context["path"] = request.url.path
    return templates.TemplateResponse(request, name, context)


@app.get("/", response_class=HTMLResponse)
def main_report(request: Request):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return render(request, "report.html", now=now)


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
