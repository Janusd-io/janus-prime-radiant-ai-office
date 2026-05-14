---
type: source
source_type: laptop
title: apply-meeting-digests
slug: apply-meeting-digests
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/apply-meeting-digests.py
original_size: 30607
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# apply-meeting-digests

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/apply-meeting-digests.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
apply-meeting-digests.py — Deterministic applier for Fireflies meeting digests.

Reads JSON manifests produced by the meeting-parser subagent
(prompts/meeting-parser-subagent.md), each describing one parsed meeting, and
applies them to the **single dept-shared vault** at `<vault>/people/<slug>/`.

  1. Rewrites the meeting note at
     `<vault>/people/<person>/meetings/<date>-<slug>.md`
     with standup-schema digest sections + a `## Transcript` wikilink.
  2. Splits the raw transcript into a sibling
     `<vault>/people/<person>/meetings/<date>-<slug>.transcript.md`
     (with minimal frontmatter; transcript NEVER stays inline in the note).
  3. Writes one `decisions/<slug>.md` per substantive decision (if not already
     present — never overwrites). Decisions live at the vault root.
  4. Creates `people/<slug>.md` stubs for attendees and mentioned people
     (single `people/` namespace, no internal/external split).
  5. Creates `projects/<slug>.md`, `vendors/<slug>.md`, `concepts/<slug>.md`
     stubs for related entities.
  6. Action items in the digest are rendered per the vault owner's
     `task_tracker` config (Linear / Monday / Asana / Notion / none).
  7. Emits a summary report.

Idempotent: a meeting note with matching `parsed_at` + `parser_version` is
skipped. Existing files are never overwritten — collisions are logged.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PARSER_VERSION = 2


# ----- yaml-ish frontmatter helpers (no PyYAML dependency) -----

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_text, body_text). If no frontmatter, returns ("", text)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def parse_simple_yaml(text: str) -> dict:
    """Parse the subset of YAML our frontmatter uses."""
    result: dict = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                result[key] = []
            else:
                result[key] = [
                    item.strip().strip("\"'") for item in inner.split(",")
                ]
        elif value.startswith('"') and value.endswith('"'):
            result[key] = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            result[key] = value[1:-1]
        elif value.lower() in {"true", "false"}:
            result[key] = value.lower() == "true"
        elif value.lstrip("-").isdigit():
            result[key] = int(value)
        else:
            result[key] = value
    return result


def emit_yaml(data: dict) -> str:
    lines = []
    for key, value in data.items():
        if value is None:
            lines.append(f"{key}:")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        elif isinstance(value, list):
            inner = ", ".join(_yaml_scalar(v) for v in value)
            lines.append(f"{key}: [{inner}]")
        else:
            lines.append(f"{key}: {_yaml_scalar(value)}")
    return "\n".join(lines)


def _yaml_scalar(value) -> str:
    if value is None:
        return ""
    s = str(value)
    if any(c in s for c in [":", "#", "[", "]", "{", "}", ",", '"', "'", "\n"]):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return s


# ----- audience normalization -----

VALID_AUDIENCE_SCALARS = {"personal", "department", "org", "ceo-only"}


def normalize_audience(raw, dept_slugs: list[str]) -> str:
    if isinstance(raw, list):
        raw = raw[0] if raw else None
    if raw is None or raw == "":
        return "department"
    s = str(raw).strip().strip("\"'")
    if s in VALID_AUDIENCE_SCALARS:
        return s
    if s == "departments":
        if len(dept_slugs) > 1:
            cleaned = ",".join(d.strip() for d in dept_slugs if d.strip())
            return f"departments:{cleaned}"
        return "department"
    if s.startswith("departments:"):
        inner = s.removeprefix("departments:")
        depts = [d.strip() for d in inner.split(",") if d.strip()]
        if depts:
            return "departments:" + ",".join(depts)
        return "department"
    return "department"


# ----- person config (task tracker) -----

def read_person_task_tracker(vault: Path, person_slug: str) -> str:
    """Read `task_tracker` from `<vault>/people/<slug>/.config.yaml`.
    Returns the tracker name in lowercase, or 'none' if unset/missing."""
    cfg = vault / "people" / person_slug / ".config.yaml"
    if not cfg.exists():
        return "none"
    try:
        text = cfg.read_text(encoding="utf-8")
    except OSError:
        return "none"
    data = parse_simple_yaml(text)
    tracker = str(data.get("task_tracker", "none")).strip().lower() or "none"
    return tracker


# ----- transcript splitting -----

TRANSCRIPT_HEADING_RE = re.compile(r"(?ms)^##\s+(?:Raw\s+transcript|Transcript)\s*$")


def extract_raw_transcript(body: str) -> str:
    """Find the raw transcript in an existing meeting source body.

    Handles the legacy shape (meta + `---` divider + transcript) and the
    legacy post-digest shape (meta + digest + `---` + `## Raw transcript`).
    Returns the transcript body only (no heading), as a clean newline-
    terminated string.
    """
    # Try to slice from "## Raw transcript" or "## Transcript" heading
    m = TRANSCRIPT_HEADING_RE.search(body)
    if m:
        after = body[m.end():].lstrip("\n")
        # If this contains a wikilink-only stub like "See [[..|full transcript]]"
        # then this body has already been split — no raw text to recover.
        if "transcript|full transcript" in after.splitlines()[0] if after else False:
            return ""
        return after.rstrip() + "\n"
    # Legacy: split on the LAST `---` divider
    parts = body.rsplit("\n---\n", 1)
    if len(parts) == 1:
        return ""
    transcript = parts[1].lstrip("\n")
    return transcript.rstrip() + "\n"


# ----- action item formatting per task tracker -----

def format_action_item(action: dict, task_tracker: str) -> str:
    """Render one action_items[] entry as a markdown checkbox per tracker.

    Trackers supported (v1):
      - linear  → "- [ ] @assignee text (due: X) — file in Linear AIP"
      - monday  → "- [ ] @assignee text (due: X) — Monday"
      - asana   → plain (TODO v2: native Asana-task syntax)
      - notion  → plain (TODO v2: native Notion task DB syntax)
      - none / other → plain "- [ ] @assignee text (due: X)"
    """
    assignee = action.get("assignee_slug") or action.get("assignee_raw") or "unassigned"
    text = (action.get("text") or "").strip()
    due = action.get("due")
    assigned_by = action.get("assigned_by_slug")

    suffix_parts: list[str] = []
    if due:
        suffix_parts.append(f"due: {due}")
    if assigned_by and assigned_by != action.get("assignee_slug"):
        suffix_parts.append(f"raised by @{assigned_by}")
    suffix = f" ({'; '.join(suffix_parts)})" if suffix_parts else ""

    base = f"- [ ] @{assignee} {text}{suffix}"
    tracker = (task_tracker or "none").strip().lower()
    if tracker == "linear":
        return f"{base} — file in Linear AIP"
    if tracker == "monday":
        return f"{base} — Monday"
    # asana / notion / none / other → plain
    # TODO(jehad): v2 — native Asana task syntax (Asana task URL or workspace
    # ref) and native Notion DB row syntax once we wire those trackers up.
    return base


# ----- digest body rendering -----

def render_digest_body(manifest: dict, task_tracker: str) -> str:
    """Render the standup-schema digest sections. Empty sections are omitted."""
    lines: list[str] = []

    summary = (manifest.get("summary") or "").strip()
    if summary:
        lines += ["## Summary", "", summary, ""]

    decisions = manifest.get("decisions") or []
    if decisions:
        lines += ["## Decisions", ""]
        for d in decisions:
            slug = d.get("slug") or ""
            title = (d.get("title") or "").strip()
            short = title if len(title) <= 100 else title[:97].rstrip() + "..."
            lines.append(f"- [[{slug}]] — {short}" if slug else f"- {short}")
        lines.append("")

    action_items = manifest.get("action_items") or []
    if action_items:
        lines += ["## Action items", ""]
        for a in action_items:
            lines.append(format_action_item(a, task_tracker))
        lines.append("")

    this_week = manifest.get("this_week") or []
    if this_week:
        lines += ["## 🎯 This week", ""]
        for item in this_week:
            assignee = item.get("assignee_slug") or item.get("assignee_raw") or "team"
            text = (item.get("text") or "").strip()
            raised_by = item.get("raised_by_slug")
            suffix = f" (raised by @{raised_by})" if raised_by and raised_by != item.get("assignee_slug") else ""
            lines.append(f"- @{assignee} {text}{suffix}")
        lines.append("")

    long_horizon = manifest.get("long_horizon") or []
    if long_horizon:
        lines += ["## 🏔️ Long horizon", ""]
        for item in long_horizon:
            text = (item.get("text") or "").strip()
            owner = item.get("owner_slug")
            horizon = item.get("horizon") or ""
            bits = []
            if owner:
                bits.append(f"owner: @{owner}")
            if horizon and horizon != "unspecified":
                bits.append(f"horizon: {horizon}")
            suffix = f" ({'; '.join(bits)})" if bits else ""
            lines.append(f"- {text}{suffix}")
        lines.append("")

    findings = manifest.get("findings") or []
    if findings:
        lines += ["## Findings", ""]
        for f in findings:
            text = (f.get("text") or "").strip()
            stated_by = f.get("stated_by_slug")
            confidence = f.get("confidence") or ""
            bits = []
            if stated_by:
                bits.append(f"stated by @{stated_by}")
            if confidence and confidence != "high":
                bits.append(f"confidence: {confidence}")
            suffix = f" ({'; '.join(bits)})" if bits else ""
            lines.append(f"- {text}{suffix}")
        lines.append("")

    open_questions = manifest.get("open_questions") or []
    if open_questions:
        lines += ["## Open questions", ""]
        for q in open_questions:
            text = (q.get("text") or "").strip()
            raised_by = q.get("raised_by_slug")
            suffix = f" (raised by @{raised_by})" if raised_by else ""
            lines.append(f"- {text}{suffix}")
        lines.append("")

    blockers = manifest.get("blockers") or []
    if blockers:
        lines += ["## Blockers", ""]
        for b in blockers:
            text = (b.get("text") or "").strip()
            blocks = b.get("blocks_slug")
            owner = b.get("owner_slug")
            bits = []
            if blocks:
                bits.append(f"blocks: [[{blocks}]]")
            if owner:
                bits.append(f"owner: @{owner}")
            suffix = f" ({'; '.join(bits)})" if bits else ""
            lines.append(f"- {text}{suffix}")
        lines.append("")

    tool_mentions = manifest.get("tool_mentions") or []
    if tool_mentions:
        lines += ["## Tool mentions", ""]
        for t in tool_mentions:
            slug = t.get("slug") or ""
            context = (t.get("context") or "").strip()
            ctx_suffix = f" — {context}" if context else ""
            lines.append(f"- [[{slug}]]{ctx_suffix}" if slug else f"- {context}")
        lines.append("")

    topics = manifest.get("topics") or []
    if topics:
        lines += ["## Topics", ""]
        for t in topics:
            lines.append(f"- {t}")
        lines.append("")

    related = manifest.get("related") or []
    if related:
        lines += ["## Related", ""]
        for r in related:
            kind = (r.get("type") or "").capitalize()
            slug = r.get("slug") or ""
            evidence = (r.get("evidence") or "").strip()
            evidence_suffix = f" — {evidence}" if evidence else ""
            lines.append(f"- {kind}: [[{slug}]]{evidence_suffix}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_meeting_meta_header(manifest: dict, attendee_links: list[str], fireflies_url: str | None) -> str:
    title = (manifest.get("title") or "Untitled meeting").strip()
    date = manifest.get("date") or ""
    duration = manifest.get("duration_min")
    attendee_str = ", ".join(attendee_links) if attendee_links else "(unresolved)"

    lines = [
        f"# {title}",
        "",
        f"**Date:** {date}",
        f"**Attendees:** {attendee_str}",
    ]
    if duration:
        lines.append(f"**Duration:** {duration} min")
    if fireflies_url:
        lines.append(f"**Fireflies:** [original meeting]({fireflies_url})")
    lines.append("")
    return "\n".join(lines)


# ----- file writers -----

def write_transcript_sibling(
    meeting_path: Path,
    raw_transcript: str,
    meeting_slug: str,
    meeting_date: str,
    person_slug: str,
) -> Path:
    """Write the raw transcript to a sibling `<stem>.transcript.md` file
    with minimal frontmatter. Returns the path written."""
    transcript_path = meeting_path.with_name(meeting_path.stem + ".transcript.md")
    fm = {
        "type": "transcript",
        "source": "meeting",
        "meeting_slug": meeting_slug,
        "captured_by": person_slug,
        "created": meeting_date or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    parts = [
        "---",
        emit_yaml(fm),
        "---",
        "",
        f"# Transcript — {meeting_slug}",
        "",
        raw_transcript.rstrip(),
        "",
    ]
    transcript_path.write_text("\n".join(parts), encoding="utf-8")
    return transcript_path


def write_meeting_file(
    meeting_path: Path,
    manifest: dict,
    person_slug: str,
    dept_slugs: list[str],
    task_tracker: str,
) -> str:
    """Rewrite the meeting file as digest + transcript wikilink (NO inline
    transcript). The raw transcript is split out to a sibling file.

    Returns: "wrote" | "skipped_already_parsed" | "skipped_error".
    """
    if not meeting_path.exists():
        return "skipped_error"

    existing = meeting_path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(existing)
    existing_fm = parse_simple_yaml(fm_text)

    # Idempotency check
    if existing_fm.get("parser_version") == PARSER_VERSION and existing_fm.get("parsed_at"):
        return "skipped_already_parsed"

    raw_transcript = extract_raw_transcript(body)
    if not raw_transcript.strip():
        # If a sibling transcript file already exists, that's fine — body was
        # already split in a previous run with an older parser.
        sibling = meeting_path.with_name(meeting_path.stem + ".transcript.md")
        if not sibling.exists():
            return "skipped_error"

    meeting_slug = existing_fm.get("slug") or meeting_path.stem
    meeting_date = manifest.get("date") or existing_fm.get("created") or ""

    # Write the sibling transcript file (if we have transcript text)
    if raw_transcript.strip():
        write_transcript_sibling(meeting_path, raw_transcript, meeting_slug, meeting_date, person_slug)

    attendees_resolved = manifest.get("attendees_resolved") or []
    attendee_slugs = [a["slug"] for a in attendees_resolved if a.get("slug")]
    attendee_links = [f"[[{s}]]" for s in attendee_slugs] or [
        a.get("raw", "") for a in attendees_resolved
    ]

    decisions = manifest.get("decisions") or []
    action_items = manifest.get("action_items") or []
    topics = manifest.get("topics") or []
    audience = normalize_audience(
        manifest.get("audience"),
        manifest.get("departments") or dept_slugs,
    )
    confidence = manifest.get("confidence_overall") or "medium"

    new_fm = {
        "type": "source",
        "source_type": "meeting",
        "title": manifest.get("title") or existing_fm.get("title") or "",
        "slug": meeting_slug,
        "created": meeting_date,
        "captured_by": person_slug,
        "attendees": attendee_slugs or existing_fm.get("attendees") or [],
        "duration_min": manifest.get("duration_min") or existing_fm.get("duration_min") or 0,
        "fireflies_id": manifest.get("fireflies_id") or existing_fm.get("fireflies_id") or "",
        "audience": audience,
        "departments": manifest.get("departments") or dept_slugs,
        "dept_scope": manifest.get("departments") or dept_slugs,
        "sensitivity": existing_fm.get("sensitivity") or "dept",
        "task_tracker": task_tracker,
        "parsed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "parser_version": PARSER_VERSION,
        "summary": (manifest.get("summary") or "").split(". ")[0][:300],
        "topics": topics,
        "decisions": [d.get("slug", "") for d in decisions if d.get("slug")],
        "action_items_count": len(action_items),
        "confidence_overall": confidence,
    }

    ff_id = new_fm.get("fireflies_id") or ""
    fireflies_url = f"https://app.fireflies.ai/view/{ff_id}" if ff_id else None

    meta_header = render_meeting_meta_header(manifest, attendee_links, fireflies_url)
    digest_body = render_digest_body(manifest, task_tracker)

    transcript_wikilink = f"See [[{meeting_slug}.transcript|full transcript]]"

    parts = [
        "---",
        emit_yaml(new_fm),
        "---",
        "",
        meta_header,
        "---",
        "",
        digest_body,
        "---",
        "",
        "## Transcript",
        "",
        transcript_wikilink,
        "",
    ]
    meeting_path.write_text("\n".join(parts), encoding="utf-8")
    return "wrote"


def write_decision_file(
    vault: Path,
    decision: dict,
    meeting_slug: str,
    meeting_date: str,
    person_slug: str,
    dept_slugs: list[str],
) -> str:
    slug = decision.get("slug")
    title = (decision.get("title") or "").strip()
    decision_text = (decision.get("decision_text") or "").strip()
    if not slug or not title or not decision_text:
        return "skipped_invalid"

    target = vault / "decisions" / f"{slug}.md"
    if target.exists():
        return "skipped_exists"
    target.parent.mkdir(parents=True, exist_ok=True)

    rationale = (decision.get("rationale") or "").strip()
    owner_slug = decision.get("owner_slug") or person_slug
    decided_by_slug = decision.get("decided_by_slug") or owner_slug
    evidence_quote = (decision.get("evidence_quote") or "").strip()
    confidence = decision.get("confidence") or "medium"

    fm = {
        "type": "decision",
        "title": title,
        "slug": slug,
        "created": meeting_date,
        "updated": meeting_date,
        "departments": dept_slugs,
        "status": "resolved",
        "owner": owner_slug,
        "decided_by": decided_by_slug,
        "sources": [meeting_slug],
        "related": [],
        "audience": "department",
        "captured_by": person_slug,
        "confidence": confidence,
    }

    parts = [
        "---",
        emit_yaml(fm),
        "---",
        "",
        f"# {title}",
        "",
        "## Decision",
        "",
        decision_text,
        "",
        "## Why",
        "",
        rationale or "(rationale not captured in transcript)",
        "",
    ]
    if evidence_quote:
        parts += ["## Evidence", "", f"> {evidence_quote}", ""]
    when_line = f"{meeting_date} · meeting [[{meeting_slug}]] · decided by [[{decided_by_slug}]]"
    if owner_slug != decided_by_slug:
        when_line += f" · owned by [[{owner_slug}]]"
    parts += [
        "## When",
        "",
        when_line,
        "",
        "## Implications",
        "",
        "- (to be populated by the owner)",
        "",
    ]
    target.write_text("\n".join(parts), encoding="utf-8")
    return "wrote"


def write_related_stub(
    vault: Path,
    related: dict,
    meeting_slug: str,
    meeting_date: str,
    person_slug: str,
) -> str:
    """Create a minimal stub for a `related[]` entry from the manifest if no
    file with that slug exists anywhere in the vault.

    Routing (single-vault layout):
      project  → projects/<slug>.md
      vendor   → vendors/<slug>.md       (NO entities/external split)
      person   → people/<slug>.md        (top-level people/ for stubs)
      concept  → concepts/<slug>.md
    """
    slug = related.get("slug")
    kind = (related.get("type") or "").strip().lower()
    evidence = (related.get("evidence") or "").strip()
    if not slug or not kind:
        return "skipped_invalid"

    # If any file with this slug already exists anywhere in the vault, skip.
    for existing in vault.rglob(f"{slug}.md"):
        if any(p in {"_archive", "_conflicts", ".state"} for p in existing.relative_to(vault).parts):
            continue
        return "skipped_exists"

    if kind == "project":
        target = vault / "projects" / f"{slug}.md"
        fm = {
            "type": "project", "title": slug.replace("-", " ").title(),
            "slug": slug, "created": meeting_date, "updated": meeting_date,
            "status": "active", "owner": person_slug,
            "sources": [meeting_slug], "related": [],
            "audience": "department", "captured_by": person_slug,
            "departments": [],
        }
        kind_label = "Project"
    elif kind == "vendor":
        target = vault / "vendors" / f"{slug}.md"
        fm = {
            "type": "vendor", "title": slug.replace("-", " ").title(),
            "slug": slug, "created": meeting_date, "updated": meeting_date,
            "status": "active", "confidence": "low",
            "sources": [meeting_slug], "related": [],
            "audience": "department", "captured_by": person_slug,
            "departments": [],
        }
        kind_label = "Vendor"
    elif kind == "person":
        target = vault / "people" / f"{slug}.md"
        fm = {
            "type": "person", "title": slug.replace("-", " ").title(),
            "slug": slug, "created": meeting_date, "updated": meeting_date,
            "sources": [meeting_slug], "related": [],
            "audience": "department", "captured_by": person_slug,
            "departments": [],
        }
        kind_label = "Person"
    elif kind == "concept":
        target = vault / "concepts" / f"{slug}.md"
        fm = {
            "type": "concept", "title": slug.replace("-", " ").title(),
            "slug": slug, "created": meeting_date, "updated": meeting_date,
            "sources": [meeting_slug], "related": [],
            "audience": "department", "captured_by": person_slug,
            "departments": [],
        }
        kind_label = "Concept"
    else:
        return "skipped_invalid"

    target.parent.mkdir(parents=True, exist_ok=True)

    body_lines = [
        f"# {fm['title']}",
        "",
        f"{kind_label} stub created from meeting [[{meeting_slug}]] on {meeting_date}.",
    ]
    if evidence:
        body_lines += ["", f"_Mention context:_ {evidence}"]
    body_lines += [
        "",
        "_To populate: replace this stub with real content and remove this notice._",
        "",
    ]

    parts = ["---", emit_yaml(fm), "---", "", "\n".join(body_lines)]
    target.write_text("\n".join(parts), encoding="utf-8")
    return "wrote"


def write_entity_stub(
    vault: Path,
    attendee: dict,
    meeting_slug: str,
    meeting_date: str,
    person_slug: str,
) -> str:
    """Write a `people/<slug>.md` person stub if not present.
    Single namespace — no internal/external split for stubs.

    External companies / vendors land in vendors/ via write_related_stub.
    Here we only create people-stubs (one folder, attendee or mentioned).
    """
    slug = attendee.get("slug")
    raw = (attendee.get("raw") or "").strip()
    if not slug or not raw:
        return "skipped_invalid"

    # Check whether this slug already exists anywhere in the vault
    # (including `people/<other-slug>/` subtree pages).
    for existing in vault.rglob(f"{slug}.md"):
        if any(p in {"_archive", "_conflicts", ".state"} for p in existing.relative_to(vault).parts):
            continue
        return "skipped_exists"

    target = vault / "people" / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    stub_hint = (attendee.get("stub_hint") or "").strip()
    status_marker = attendee.get("status") or "unknown"

    fm = {
        "type": "person",
        "title": raw,
        "slug": slug,
        "created": meeting_date,
        "updated": meeting_date,
        "departments": [],
        "related": [],
        "audience": "department",
        "captured_by": person_slug,
        "status": "stub",
        "confidence": "low",
        "person_status": status_marker,  # internal | external | unknown
    }

    body_lines = [
        f"# {raw}",
        "",
        f"Stub created from meeting [[{meeting_slug}]] on {meeting_date}.",
    ]
    if stub_hint:
        body_lines += ["", stub_hint]
    body_lines += [
        "",
        "_To populate: add role, department, projects worked on, and remove this stub notice._",
        "",
    ]

    parts = ["---", emit_yaml(fm), "---", "", "\n".join(body_lines)]
    target.write_text("\n".join(parts), encoding="utf-8")
    return "wrote"


# ----- main -----

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--vault", required=True, help="Single dept-shared vault root")
    p.add_argument("--person", required=True, help="Owner kebab-case slug")
    p.add_argument("--depts", required=True, help="Comma-separated dept slugs for the owner")
    p.add_argument(
        "--ingest-dir",
        default=None,
        help="Directory of meeting-parser JSON manifests (default: <vault>/.state/meeting-digest)",
    )
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists():
        print(f"vault not found: {vault}", file=sys.stderr)
        return 2

    person_slug = args.person
    dept_slugs = [d.strip() for d in args.depts.split(",") if d.strip()]
    task_tracker = read_person_task_tracker(vault, person_slug)

    ingest_dir = Path(args.ingest_dir).expanduser().resolve() if args.ingest_dir else vault / ".state" / "meeting-digest"
    if not ingest_dir.exists():
        print(f"no manifests at {ingest_dir} — nothing to apply")
        return 0

    manifests = sorted(ingest_dir.glob("*.json"))
    if not manifests:
        print(f"no manifests at {ingest_dir} — nothing to apply")
        return 0

    counts = {
        "meetings_wrote": 0,
        "meetings_skipped_parsed": 0,
        "meetings_skipped_error": 0,
        "meetings_skipped_reason": 0,
        "decisions_wrote": 0,
        "decisions_skipped_exists": 0,
        "decisions_skipped_invalid": 0,
        "stubs_wrote": 0,
        "stubs_skipped_exists": 0,
        "stubs_skipped_invalid": 0,
        "errors": 0,
    }
    errors: list[str] = []

    print(f"apply-meeting-digests: vault={vault} person={person_slug} task_tracker={task_tracker}")

    for mp in manifests:
        try:
            manifest = json.loads(mp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            counts["errors"] += 1
            errors.append(f"{mp.name}: malformed JSON: {e}")
            continue

        if manifest.get("errors"):
            counts["errors"] += 1
            errors.append(f"{mp.name}: subagent errors: {manifest['errors']}")
            continue

        if manifest.get("skipped_reason"):
            counts["meetings_skipped_reason"] += 1
            continue

        meeting_path_str = manifest.get("meeting_file")
        if not meeting_path_str:
            counts["errors"] += 1
            errors.append(f"{mp.name}: missing meeting_file")
            continue
        meeting_path = Path(meeting_path_str).expanduser().resolve()
        meeting_slug = meeting_path.stem
        meeting_date = manifest.get("date") or ""

        if args.dry_run:
            counts["meetings_wrote"] += 1
            for d in manifest.get("decisions") or []:
                if d.get("slug"):
                    counts["decisions_wrote"] += 1
            for a in manifest.get("attendees_resolved") or []:
                if a.get("needs_stub"):
                    counts["stubs_wrote"] += 1
            continue

        action = write_meeting_file(meeting_path, manifest, person_slug, dept_slugs, task_tracker)
        if action == "wrote":
            counts["meetings_wrote"] += 1
        elif action == "skipped_already_parsed":
            counts["meetings_skipped_parsed"] += 1
        else:
            counts["meetings_skipped_error"] += 1
            errors.append(f"{mp.name}: meeting rewrite skipped ({action}) for {meeting_path}")
            continue

        for d in manifest.get("decisions") or []:
            r = write_decision_file(vault, d, meeting_slug, meeting_date, person_slug, dept_slugs)
            counts[f"decisions_{r}"] = counts.get(f"decisions_{r}", 0) + 1

        for a in manifest.get("attendees_resolved") or []:
            r = write_entity_stub(vault, a, meeting_slug, meeting_date, person_slug)
            counts[f"stubs_{r}"] = counts.get(f"stubs_{r}", 0) + 1

        for r_entry in manifest.get("related") or []:
            r = write_related_stub(vault, r_entry, meeting_slug, meeting_date, person_slug)
            counts[f"related_{r}"] = counts.get(f"related_{r}", 0) + 1

    print("apply-meeting-digests complete")
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")
    if errors:
        print("\nerrors:")
        for e in errors[:20]:
            print(f"  - {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

```