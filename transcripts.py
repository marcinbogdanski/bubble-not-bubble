"""Read Claude Code chat transcripts for this project from ~/.claude/projects.

Only the human-visible conversation is kept: user prompts (with pasted images)
and the assistant's text replies. Tool calls, tool results, thinking, subagents
and harness metadata are skipped.
"""

import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
CLAUDE_DIR = Path(os.environ.get("CLAUDE_CONFIG_DIR", Path.home() / ".claude"))
SESSION_ID_RE = re.compile(r"^[0-9a-f-]{36}$")


@dataclass
class Message:
    role: str  # "user" or "assistant"
    timestamp: datetime | None
    text: str
    images: list[str] = field(default_factory=list)  # data: URIs


@dataclass
class Session:
    id: str
    path: Path
    title: str
    started: datetime | None
    messages: list[Message] = field(default_factory=list)


def _project_dirs() -> list[Path]:
    """This project's transcript dir, plus dirs of Claude worktrees inside it."""
    encoded = re.sub(r"[^A-Za-z0-9]", "-", str(PROJECT_DIR))
    root = CLAUDE_DIR / "projects"
    return sorted(
        d for d in root.glob(f"{encoded}*")
        if d.is_dir() and (d.name == encoded or d.name.startswith(f"{encoded}--claude-worktrees-"))
    )


def _parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone()
    except ValueError:
        return None


def _user_message(record: dict) -> Message | None:
    if record.get("isMeta"):
        return None
    content = record.get("message", {}).get("content")
    if isinstance(content, str):
        text, images = content, []
    elif isinstance(content, list):
        if any(b.get("type") == "tool_result" for b in content):
            return None
        text = "\n\n".join(b.get("text", "") for b in content if b.get("type") == "text")
        images = [
            f"data:{b['source']['media_type']};base64,{b['source']['data']}"
            for b in content
            if b.get("type") == "image" and b.get("source", {}).get("type") == "base64"
        ]
    else:
        return None
    if not text.strip() and not images:
        return None
    return Message("user", _parse_time(record.get("timestamp")), text, images)


def _assistant_text(record: dict) -> str:
    message = record.get("message", {})
    if message.get("model") == "<synthetic>":
        return ""
    parts = []
    for b in message.get("content", []):
        if b.get("type") == "text":
            parts.append(b.get("text", ""))
        elif b.get("type") == "tool_use" and b.get("name", "").endswith("__wrap_up"):
            # The desktop app's end-of-turn box: shown to the user, so keep it.
            inp = b.get("input", {})
            parts.extend(f"> {inp[k]}" for k in ("recap", "ask") if inp.get(k))
    return "\n\n".join(parts).strip()


def load_session(path: Path) -> Session:
    title = None
    started = None
    messages: list[Message] = []

    with path.open(encoding="utf-8") as f:
        for line in f:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            kind = record.get("type")
            if kind == "custom-title":
                title = record.get("customTitle") or title
                continue
            if record.get("isSidechain"):
                continue
            started = started or _parse_time(record.get("timestamp"))

            msg = None
            if kind == "user":
                msg = _user_message(record)
            elif kind == "attachment":
                # Messages typed while Claude was mid-turn arrive as queued commands.
                att = record.get("attachment", {})
                if att.get("type") == "queued_command" and att.get("origin", {}).get("kind") == "human":
                    msg = Message("user", _parse_time(att.get("timestamp")), att.get("prompt", ""))
            elif kind == "assistant":
                text = _assistant_text(record)
                if text:
                    # One reply is split across many records; merge consecutive text.
                    if messages and messages[-1].role == "assistant":
                        messages[-1].text += "\n\n" + text
                        continue
                    msg = Message("assistant", _parse_time(record.get("timestamp")), text)
            if msg:
                messages.append(msg)

    if not title:
        first = next((m.text for m in messages if m.role == "user" and m.text.strip()), "")
        title = (first[:60] + "…") if len(first) > 60 else (first or path.stem)
    return Session(path.stem, path, title, started, messages)


def list_sessions() -> list[Session]:
    """All sessions for this project, newest first (messages loaded)."""
    sessions = [
        load_session(p)
        for d in _project_dirs()
        for p in d.glob("*.jsonl")
        if SESSION_ID_RE.match(p.stem)
    ]
    sessions = [s for s in sessions if s.messages]
    return sorted(sessions, key=lambda s: s.path.stat().st_mtime, reverse=True)


def get_session(session_id: str) -> Session | None:
    if not SESSION_ID_RE.match(session_id):
        return None
    for d in _project_dirs():
        path = d / f"{session_id}.jsonl"
        if path.is_file():
            return load_session(path)
    return None
