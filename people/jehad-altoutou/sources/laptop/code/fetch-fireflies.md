---
type: source
source_type: laptop
title: fetch-fireflies
slug: fetch-fireflies
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/fetch-fireflies.py
original_size: 8527
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# fetch-[[fireflies|fireflies]]

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/fetch-fireflies.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
fetch-fireflies.py — Pull yesterday's meetings (or a custom date range) from
Fireflies via the user's personal API key, drop each as an inbox marker for
the next ingest pass.

Authentication:
  Reads FIREFLIES_API_KEY from --env (default ~/.config/janus-brain/.env).
  Each employee has their own key (per user preference 2026-05-11). The key
  authorises access to only the meetings they were in.

Output:
  For each meeting, writes a raw-transcript markdown file into <vault>/inbox/
  named YYYY-MM-DD-<meeting-slug>.md. The ingest subagent treats these as
  source markers and files them into sources/meetings/ per AIO §5.1.

Skip rules (matching AIO §5.1):
  - Recurring 1:1s with the same attendee count week-over-week (probably
    standup-like). Override with --no-skip-recurring.
  - Meetings flagged as standups by Fireflies metadata.
  - Meetings older than --since unless explicitly given a date.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


FIREFLIES_GRAPHQL = "https://api.fireflies.ai/graphql"

LIST_QUERY = """
query Transcripts($fromDate: DateTime, $toDate: DateTime) {
  transcripts(fromDate: $fromDate, toDate: $toDate, limit: 50) {
    id
    title
    date
    duration
    participants
    organizer_email
    summary { keywords }
    sentences { index speaker_name text start_time }
  }
}
"""


def load_api_key(env_path: Path) -> str | None:
    if not env_path.exists():
        return None
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k.strip() == "FIREFLIES_API_KEY":
            return v.strip().strip("\"'")
    return None


def graphql(query: str, variables: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        FIREFLIES_GRAPHQL,
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def slugify(text: str, max_len: int = 80) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    return text[:max_len].rstrip("-") or "untitled"


def looks_like_standup(meeting: dict) -> bool:
    title = (meeting.get("title") or "").lower()
    if any(k in title for k in ("standup", "stand-up", "stand up", "daily ", "1:1", "1-1", "one on one")):
        return True
    return False


def render_marker(vault: Path, meeting: dict, person_slug: str) -> Path:
    title = meeting.get("title") or "Untitled meeting"
    date_raw = meeting.get("date") or ""
    # Fireflies returns ms-since-epoch or ISO depending on plan; handle both
    try:
        if isinstance(date_raw, (int, float)) or (isinstance(date_raw, str) and date_raw.isdigit()):
            dt = datetime.fromtimestamp(int(date_raw) / 1000, tz=timezone.utc)
        else:
            dt = datetime.fromisoformat(str(date_raw).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        dt = datetime.now(timezone.utc)
    date_str = dt.strftime("%Y-%m-%d")

    slug = slugify(title)
    fname = f"{date_str}-{slug}.md"
    target = vault / "inbox" / fname
    target.parent.mkdir(parents=True, exist_ok=True)

    participants = meeting.get("participants") or []
    duration = meeting.get("duration") or 0
    fireflies_id = meeting.get("id") or ""

    # Build transcript body
    sentences = meeting.get("sentences") or []
    body_lines = [f"# {title}", "", f"**Meeting date:** {dt.strftime('%Y-%m-%d %H:%M UTC')}", ""]
    body_lines.append(f"**Duration:** {duration} min")
    body_lines.append(f"**Participants:** {', '.join(participants)}")
    body_lines.append("")
    body_lines.append("---")
    body_lines.append("")
    for s in sentences:
        speaker = s.get("speaker_name") or "Unknown"
        ts = s.get("start_time") or 0
        try:
            ts_str = f"[{int(ts) // 60:02d}:{int(ts) % 60:02d}]"
        except (TypeError, ValueError):
            ts_str = ""
        body_lines.append(f"**{speaker}** {ts_str}: {s.get('text', '').strip()}")
        body_lines.append("")

    frontmatter = (
        "---\n"
        "type: source\n"
        "source_type: meeting\n"
        f"slug: {date_str}-{slug}\n"
        f"title: {title}\n"
        f"created: {date_str}\n"
        f"captured_by: {person_slug}\n"
        f"fireflies_id: {fireflies_id}\n"
        f"attendees: {json.dumps(participants)}\n"
        f"duration_min: {duration}\n"
        "audience: [department]\n"
        "---\n\n"
    )
    target.write_text(frontmatter + "\n".join(body_lines), encoding="utf-8")
    return target


def parse_since(since: str) -> datetime:
    s = since.strip().lower()
    now = datetime.now(timezone.utc)
    if s == "yesterday":
        d = (now - timedelta(days=1)).date()
        return datetime(d.year, d.month, d.day, tzinfo=timezone.utc)
    if s == "today":
        return datetime(now.year, now.month, now.day, tzinfo=timezone.utc)
    if s.endswith("d"):
        try:
            n = int(s[:-1])
            return now - timedelta(days=n)
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except ValueError:
        raise SystemExit(f"--since: cannot parse {since!r}; use 'yesterday', 'today', '7d', or YYYY-MM-DD")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vault", required=True)
    p.add_argument("--person", required=True, help="kebab-case person slug")
    p.add_argument("--env", default=str(Path.home() / ".config" / "janus-brain" / ".env"))
    p.add_argument("--since", default="yesterday")
    p.add_argument("--until", default=None, help="ISO date; default = now")
    p.add_argument("--no-skip-recurring", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    env_path = Path(args.env).expanduser().resolve()

    api_key = os.environ.get("FIREFLIES_API_KEY") or load_api_key(env_path)
    if not api_key:
        print(f"FIREFLIES_API_KEY missing — set in env or in {env_path}", file=sys.stderr)
        print("To create:", file=sys.stderr)
        print(f"  mkdir -p {env_path.parent} && touch {env_path} && chmod 600 {env_path}", file=sys.stderr)
        print(f"  echo 'FIREFLIES_API_KEY=<your-key>' > {env_path}", file=sys.stderr)
        sys.exit(2)

    since_dt = parse_since(args.since)
    until_dt = datetime.fromisoformat(args.until).replace(tzinfo=timezone.utc) if args.until else datetime.now(timezone.utc)

    try:
        result = graphql(LIST_QUERY, {
            "fromDate": since_dt.isoformat(),
            "toDate": until_dt.isoformat(),
        }, api_key)
    except urllib.error.HTTPError as e:
        print(f"Fireflies API error: {e.code} {e.reason}", file=sys.stderr)
        print(e.read().decode(errors="replace")[:500], file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Fireflies API network error: {e}", file=sys.stderr)
        sys.exit(1)

    if "errors" in result:
        print("Fireflies GraphQL errors:", file=sys.stderr)
        for err in result["errors"]:
            print(f"  {err.get('message')}", file=sys.stderr)
        sys.exit(1)

    transcripts = result.get("data", {}).get("transcripts", []) or []
    written: list[str] = []
    skipped: list[tuple[str, str]] = []

    for meeting in transcripts:
        if not args.no_skip_recurring and looks_like_standup(meeting):
            skipped.append((meeting.get("title", ""), "looks like standup/1:1 (use --no-skip-recurring to override)"))
            continue
        if args.dry_run:
            written.append(meeting.get("title", ""))
            continue
        target = render_marker(vault, meeting, args.person)
        written.append(str(target.relative_to(vault)))

    print(f"fireflies: {len(written)} meetings staged in inbox/, {len(skipped)} skipped")
    for s in skipped[:5]:
        print(f"  skipped: {s[0]} — {s[1]}")
    if args.dry_run:
        print("(dry run)")


if __name__ == "__main__":
    sys.exit(main())

```