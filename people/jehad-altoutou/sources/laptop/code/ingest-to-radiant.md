---
type: source
source_type: laptop
title: ingest-to-radiant
slug: ingest-to-radiant
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/ingest-to-radiant.py
original_size: 11774
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# ingest-to-radiant

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/ingest-to-radiant.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
ingest-to-radiant.py — Validate the ingest subagents' work and update
index.md + log.md for the Personal Prime Radiant.

The subagents themselves write the wiki pages (per AIO §5.1 low-stakes
discipline: writing directly to entity/concept/decision/pulse pages with
correct frontmatter). This script's job is to:

  1. Read each state/ingest/chunk_NN.json manifest produced by a subagent
  2. Validate every page the chunk claims it wrote/updated actually exists
     and has compliant frontmatter
  3. Update index.md with one line per page (per AIO §5.4)
  4. Append a per-chunk batch entry to log.md (per AIO §5.1 batch-ingest)
  5. Surface escalation counts to the user
  6. Move processed inbox markers (legacy two-vault layout) into
     inbox/.processed/<YYYY-MM>/ — no-op under the single-vault layout
     where the inbox/ directory does not exist.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_FRONTMATTER = {
    "type", "title", "slug", "created", "updated", "captured_by",
}
REQUIRED_BY_TYPE = {
    "project":  {"status", "owner", "departments"},
    "decision": {"status", "owner", "departments"},
    "question": {"status", "owner"},
    "lesson":   {"status", "departments"},
    "vendor":   {"confidence"},
    "pulse":    {"confidence", "departments"},
    "brief":    {"confidence", "departments"},
}
VALID_TYPES = {
    "vendor", "concept", "process", "project", "decision", "lesson",
    "question", "pulse", "brief", "person", "client", "department", "source",
}
VALID_AUDIENCE_PREFIXES = ("personal", "department", "departments:", "org", "ceo-only")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm


def validate_page(path: Path) -> list[str]:
    """Return list of validation errors for a page."""
    errors = []
    if not path.exists():
        return [f"page does not exist: {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"no frontmatter: {path}"]
    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing:
        errors.append(f"missing required fields {sorted(missing)}: {path}")
    type_val = fm.get("type", "").strip()
    if type_val not in VALID_TYPES:
        errors.append(f"invalid type {type_val!r}: {path}")
    if type_val in REQUIRED_BY_TYPE:
        type_missing = REQUIRED_BY_TYPE[type_val] - set(fm.keys())
        if type_missing:
            errors.append(f"type={type_val} missing {sorted(type_missing)}: {path}")
    audience = fm.get("audience", "").strip().strip("[]")
    if not audience or not audience.startswith(VALID_AUDIENCE_PREFIXES):
        errors.append(f"missing or invalid audience: {path}")
    return errors


def slug_from_path(path: Path, vault: Path) -> str:
    return path.relative_to(vault).as_posix().removesuffix(".md")


def section_for_path(rel_path: str) -> str:
    """Map a wiki page relative path to its index.md section label.

    Single-vault layout: top-level dirs are `people/`, `vendors/`, `projects/`,
    `concepts/`, `processes/`, `decisions/`, `pulse/`, `briefs/`, `lessons/`,
    `questions/`. Legacy `entities/<sub>/` nesting is still recognized for
    template-inherited content from Michael's dept template.
    """
    parts = rel_path.split("/")
    if not parts:
        return "Other"
    head = parts[0]
    if head == "people":
        # `people/<slug>.md` (top-level person stub) → People
        # `people/<slug>/...` (per-person subtree, sources/meetings/private) is
        # filtered out before this is called.
        return "People"
    if head == "entities":
        if len(parts) > 1:
            sub = parts[1]
            return {
                "vendors": "Vendors",
                "clients": "Clients",
                "external": "People",
                "internal": "People",
                "departments": "Departments",
            }.get(sub, "Entities")
        return "Entities"
    return {
        "vendors": "Vendors",
        "clients": "Clients",
        "concepts": "Concepts",
        "processes": "Processes",
        "projects": "Projects",
        "decisions": "Decisions",
        "lessons": "Lessons",
        "questions": "Questions",
        "pulse": "Pulse",
        "briefs": "Briefs",
        "sources": "Sources",
    }.get(head, "Other")


def render_index(vault: Path) -> str:
    """Walk the vault and produce index.md sorted by section."""
    by_section: dict[str, list[tuple[str, str, str]]] = {}
    skip_dirs = {".obsidian", "inbox", "_Archive", ".state", ".git", ".github"}
    for md in vault.rglob("*.md"):
        rel = md.relative_to(vault)
        if rel.parts[0] in skip_dirs:
            continue
        if rel.parts[0] == "sources":
            continue  # Legacy two-vault path; raw sources are not indexed
        # Single-vault: skip per-person source content (people/<slug>/sources/,
        # people/<slug>/meetings/, people/<slug>/private/). Top-level
        # people/<slug>.md person stubs ARE indexed.
        if rel.parts[0] == "people" and len(rel.parts) >= 3:
            sub = rel.parts[2] if len(rel.parts) >= 3 else ""
            if sub in {"sources", "meetings", "private"} or rel.parts[1] == ".private":
                continue
            # Also skip the per-person CLAUDE.md / self.md / .review-queue.md
            if md.name in {"CLAUDE.md", "self.md", ".review-queue.md"}:
                continue
        if md.name in {"index.md", "log.md", "CLAUDE.md", "README.md"}:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text) or {}
        slug = fm.get("slug", md.stem).strip()
        status = fm.get("status", "").strip()
        confidence = fm.get("confidence", "").strip()
        # First non-empty paragraph after frontmatter, ~12 words
        body = text[FRONTMATTER_RE.match(text).end():] if FRONTMATTER_RE.match(text) else text
        body_lines = [ln.strip() for ln in body.splitlines() if ln.strip() and not ln.startswith("#")]
        snippet = (body_lines[0] if body_lines else "").rstrip(".")
        snippet_words = snippet.split()
        if len(snippet_words) > 18:
            snippet = " ".join(snippet_words[:18]) + "…"
        tags = []
        if status:
            tags.append(status)
        if confidence:
            tags.append(confidence)
        tag_str = f" [{', '.join(tags)}]" if tags else ""
        rel_posix = rel.as_posix()
        section = section_for_path(rel_posix)
        by_section.setdefault(section, []).append((slug, rel_posix, snippet + tag_str))

    order = [
        "Vendors", "Clients", "People (external)", "People (internal)", "Departments",
        "Concepts", "Processes", "Projects", "Decisions", "Lessons",
        "Questions", "Pulse", "Briefs", "Entities", "Other",
    ]
    out = ["# Wiki Index", "", f"_Updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}_", "",
           "> Content catalog. One line per page, grouped by category. See `CLAUDE.md` for the schema.",
           ""]
    for section in order:
        rows = by_section.get(section, [])
        if not rows:
            continue
        rows.sort(key=lambda r: r[0])
        out.append(f"## {section}")
        out.append("")
        for slug, rel_path, snippet in rows:
            out.append(f"- [{slug}]({rel_path}) — {snippet}")
        out.append("")
    return "\n".join(out)


def append_log(vault: Path, summary: dict) -> None:
    log = vault / "log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    lines = [
        "",
        f"## [{ts}] batch-ingest | janus-brain | {summary['source_count']} items",
        f"- chunks processed:  {summary['chunks']}",
        f"- pages created:     {summary['created']}",
        f"- pages updated:     {summary['updated']}",
        f"- sources filed:     {summary['sources']}",
        f"- escalations:       {summary['escalations']} (see questions/ingest-*.md)",
        f"- validation errors: {summary['errors']}",
    ]
    with log.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vault", required=True)
    p.add_argument("--person", required=True, help="kebab-case person slug")
    p.add_argument("--ingest-dir", required=True, help="state/ingest dir with chunk_*.json")
    p.add_argument("--templates", required=True)
    args = p.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    ingest_dir = Path(args.ingest_dir).expanduser().resolve()

    if not vault.exists():
        print(f"vault does not exist: {vault}", file=sys.stderr)
        sys.exit(2)

    chunk_files = sorted(ingest_dir.glob("chunk_*.json"))
    summary = {
        "chunks": 0, "created": 0, "updated": 0, "sources": 0,
        "escalations": 0, "errors": 0, "source_count": 0,
    }
    all_errors: list[str] = []

    for chunk_path in chunk_files:
        try:
            manifest = json.loads(chunk_path.read_text())
        except json.JSONDecodeError as e:
            all_errors.append(f"{chunk_path.name}: invalid json: {e}")
            summary["errors"] += 1
            continue

        summary["chunks"] += 1
        summary["source_count"] += len(manifest.get("inbox_processed", []))
        summary["sources"] += len(manifest.get("sources_filed", []))
        summary["created"] += len(manifest.get("pages_created", []))
        summary["updated"] += len(manifest.get("pages_updated", []))
        summary["escalations"] += len(manifest.get("escalations", []))

        for page_rel in manifest.get("pages_created", []) + manifest.get("pages_updated", []):
            page_path = vault / page_rel
            errors = validate_page(page_path)
            if errors:
                all_errors.extend(errors)
                summary["errors"] += len(errors)

        # Move inbox markers to .processed (legacy two-vault layout only —
        # under single-vault, inbox/ does not exist and this is a no-op).
        inbox_processed = manifest.get("inbox_processed", []) or []
        if inbox_processed and (vault / "inbox").exists():
            ym = datetime.now(timezone.utc).strftime("%Y-%m")
            processed_dir = vault / "inbox" / ".processed" / ym
            processed_dir.mkdir(parents=True, exist_ok=True)
            for marker in inbox_processed:
                src = vault / marker
                if src.exists():
                    dest = processed_dir / src.name
                    shutil.move(str(src), str(dest))

    # Update index.md
    index_text = render_index(vault)
    (vault / "index.md").write_text(index_text, encoding="utf-8")

    append_log(vault, summary)

    print(f"ingest validated: {summary['chunks']} chunks")
    print(f"  pages created:  {summary['created']}")
    print(f"  pages updated:  {summary['updated']}")
    print(f"  sources filed:  {summary['sources']}")
    print(f"  escalations:    {summary['escalations']}")
    print(f"  errors:         {summary['errors']}")
    if all_errors:
        print("\nvalidation errors (first 10):")
        for err in all_errors[:10]:
            print(f"  {err}")
        if len(all_errors) > 10:
            print(f"  …and {len(all_errors) - 10} more")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())

```