---
type: source
source_type: laptop
title: Janus Brain Bootstrap — lint-vault
slug: lint-vault
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/lint-vault.py
original_size: 20585
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# lint-vault

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/lint-vault.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
lint-vault.py — Schema + integrity linter for a Prime Radiant vault
(personal or department instance).

Checks
------
ERROR  (must-fix; failing any of these → non-zero exit):
  - frontmatter_present       Every .md page has frontmatter
  - frontmatter_parseable     Frontmatter is well-formed YAML-ish
  - type_set                  `type:` field is present and known
  - required_fields           Type-specific required fields are populated
  - slug_matches_filename     `slug:` equals filename stem
  - folder_type_match         File in /decisions/ has type: decision, etc.
  - audience_valid            `audience:` is one of the allowed forms
  - departments_in_vocab      Every `departments:` entry is in locked list
  - wikilinks_resolve         `[[slug]]` references point at real files

WARN   (should-fix; visible but doesn't fail by default; --strict promotes):
  - slug_discipline           Slug is kebab-case, lowercase, ASCII
  - date_format               created / updated are YYYY-MM-DD
  - sources_resolve           Each item in `sources:` resolves to a source
  - source_immutability       Files in /sources/ have no `updated:` field
  - captured_by_present       Every page has `captured_by:`
  - orphan                    Page has no incoming wikilinks/refs from other
                              pages (excluding /sources/ which are referenced
                              via frontmatter and /inbox/ which is staging)

Output
------
- Default: human-readable, grouped by check, with file:line pointers
- --json: machine-readable for CI
- Exit code = error count (0 = clean), or warning count too if --strict

Scope
-----
Skips: .state/, _archive/, _conflicts/, .obsidian/, .git/, .processed/
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ── Tables ────────────────────────────────────────────────────────────────

LOCKED_DEPTS = {
    "ai-office", "marketing", "hr", "it-ops", "finance",
    "office-of-ceo", "engineering", "training", "iso", "pm",
}

# Required on every page regardless of type
COMMON_REQUIRED = ["type", "title", "slug", "created"]

# Required additionally on content-bearing types (audit chain). Structural
# types like `department` federation stubs don't carry these.
CONTENT_TYPE_REQUIRED = ["captured_by", "audience"]

TYPE_EXTRA_REQUIRED = {
    "decision":  ["status", "owner"],
    "project":   ["status", "owner"],
    "vendor":    ["status", "confidence"],
    "pulse":     ["confidence"],
    "question":  ["status"],
    "source":    ["source_type"],
}

# Content-bearing types (carry audience + captured_by). Per Michael's
# CLAUDE.md vocabulary.
CONTENT_TYPES = {
    "decision", "project", "vendor", "concept", "process",
    "lesson", "pulse", "brief", "question", "source", "person",
}

# Structural types — federation stubs and template scaffolding. Don't
# require captured_by/audience.
STRUCTURAL_TYPES = {"department", "transcript"}

KNOWN_TYPES = CONTENT_TYPES | STRUCTURAL_TYPES

# Folder → expected type. None means "any type is OK in this folder".
# Single-vault layout (rewrite 2026-05-14): everything is one repo, with
# per-person content under `people/<slug>/`.
FOLDER_EXPECTED_TYPE = {
    "decisions":            "decision",
    "projects":             "project",
    "processes":            "process",
    "lessons":              "lesson",
    "pulse":                "pulse",
    "concepts":             "concept",
    "briefs":               "brief",
    "questions":            "question",
    "vendors":              "vendor",
    "people":               None,        # mix of person stubs + per-person subtrees
    # Legacy folder names — deprecated. Lint should still grok the type if a
    # vault still has them, but they emit a deprecation warning below.
    "entities/internal":    "person",
    "entities/external":    "person",
    "entities/vendors":     "vendor",
    "entities/clients":     "vendor",
    "entities/departments": None,
    "sources":              "source",
    "inbox":                None,
}

DEPRECATED_FOLDERS = {"entities/internal", "entities/external", "entities/vendors",
                      "entities/clients", "entities/departments", "inbox"}

VALID_AUDIENCE_SCALAR = {"personal", "department", "org", "ceo-only"}
SKIP_DIRS = {".state", "_archive", "_conflicts", ".obsidian", ".git", ".processed"}

# Vault meta files — not knowledge pages, no frontmatter expected
VAULT_META_FILES = {
    "log.md", "index.md", "CLAUDE.md", "README.md",
    "BOOTSTRAP.md", "CHANGELOG.md", "TEMPLATE-VERSION", "BOOTSTRAPPED-FROM-VERSION",
}

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_RE = re.compile(r"\[\[([^\]|\n]+?)(?:\|[^\]]*)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)


# ── Parsing helpers (no PyYAML dep) ────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """Return (frontmatter_dict, body_text). If no frontmatter, returns (None, text)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    fm_text = m.group(1)
    body = m.group(2)
    fm: dict[str, object] = {}
    for line in fm_text.splitlines():
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
                fm[key] = []
            else:
                fm[key] = [item.strip().strip("\"'") for item in inner.split(",")]
        elif value.startswith('"') and value.endswith('"'):
            fm[key] = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            fm[key] = value[1:-1]
        else:
            fm[key] = value
    return fm, body


def folder_path_for(rel: Path) -> str:
    """Return the longest folder key in FOLDER_EXPECTED_TYPE that prefixes
    this file's directory path (forward-slash form). Returns "" if no match."""
    rel_dir = "/".join(rel.parts[:-1])  # everything but filename
    best = ""
    for key in FOLDER_EXPECTED_TYPE:
        if rel_dir == key or rel_dir.startswith(key + "/"):
            if len(key) > len(best):
                best = key
    return best


def audience_valid(value: object) -> bool:
    """Accept scalar 'personal'/'department'/'org'/'ceo-only',
    list forms like ['department'], or 'departments:x,y' / ['departments:x,y']."""
    if isinstance(value, list):
        return all(audience_valid(v) for v in value)
    if not isinstance(value, str):
        return False
    v = value.strip().strip("[]").strip("\"'")
    if v in VALID_AUDIENCE_SCALAR:
        return True
    if v.startswith("departments:"):
        depts = [d.strip() for d in v.removeprefix("departments:").split(",") if d.strip()]
        return all(d in LOCKED_DEPTS for d in depts)
    return False


def audience_departments(value: object) -> list[str]:
    """Extract the departments referenced inside an audience value, for vocab check."""
    if isinstance(value, list):
        deps: list[str] = []
        for v in value:
            deps.extend(audience_departments(v))
        return deps
    if not isinstance(value, str):
        return []
    v = value.strip().strip("[]").strip("\"'")
    if v.startswith("departments:"):
        return [d.strip() for d in v.removeprefix("departments:").split(",") if d.strip()]
    return []


def list_values(raw: object) -> list[str]:
    """Coerce a frontmatter value to a list of strings."""
    if raw is None or raw == "":
        return []
    if isinstance(raw, list):
        return [str(x).strip() for x in raw if str(x).strip()]
    s = str(raw).strip().strip("[]")
    if not s:
        return []
    return [v.strip().strip("\"'") for v in s.split(",") if v.strip()]


# ── Issue model ───────────────────────────────────────────────────────────

class Issue:
    __slots__ = ("severity", "check", "file", "message")

    def __init__(self, severity: str, check: str, file: str, message: str):
        self.severity = severity
        self.check = check
        self.file = file
        self.message = message

    def to_dict(self) -> dict:
        return {"severity": self.severity, "check": self.check, "file": self.file, "message": self.message}


# ── Main lint pass ────────────────────────────────────────────────────────

def lint(vault: Path) -> list[Issue]:
    issues: list[Issue] = []
    files_by_slug: dict[str, list[Path]] = defaultdict(list)
    fm_by_file: dict[Path, dict] = {}
    body_by_file: dict[Path, str] = {}
    incoming_refs: dict[str, int] = defaultdict(int)

    # ── Pass 1: collect frontmatter + slug index ───────────────────────────
    for md in vault.rglob("*.md"):
        rel = md.relative_to(vault)
        if any(p in SKIP_DIRS for p in rel.parts):
            continue
        if md.name in VAULT_META_FILES:
            continue  # not a knowledge page; lives at vault root, no frontmatter expected
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except (OSError, TimeoutError):
            issues.append(Issue("error", "read_failure", str(rel), "file unreadable"))
            continue

        fm, body = parse_frontmatter(text)
        if fm is None:
            issues.append(Issue("error", "frontmatter_present", str(rel),
                                "no frontmatter (missing leading '---' block)"))
            continue
        fm_by_file[md] = fm
        body_by_file[md] = body
        slug = str(fm.get("slug", "")).strip()
        if slug:
            files_by_slug[slug].append(md)

    # ── Pass 2: per-file checks + build incoming refs ──────────────────────
    for md, fm in fm_by_file.items():
        rel = md.relative_to(vault)
        rel_str = str(rel)
        body = body_by_file[md]
        ftype = str(fm.get("type", "")).strip()
        slug = str(fm.get("slug", "")).strip()

        # type_set + known
        if not ftype:
            issues.append(Issue("error", "type_set", rel_str, "frontmatter missing `type:`"))
        elif ftype not in KNOWN_TYPES:
            issues.append(Issue("error", "type_set", rel_str,
                                f"unknown type `{ftype}` (allowed: {', '.join(sorted(KNOWN_TYPES))})"))

        # required_fields
        required = list(COMMON_REQUIRED)
        if ftype in CONTENT_TYPES:
            required += CONTENT_TYPE_REQUIRED
        if ftype in TYPE_EXTRA_REQUIRED:
            required += TYPE_EXTRA_REQUIRED[ftype]
        for key in required:
            v = fm.get(key)
            if v is None or v == "" or v == []:
                issues.append(Issue("error", "required_fields", rel_str,
                                    f"missing required `{key}:` (for type `{ftype or '<unset>'}`)"))

        # slug_matches_filename
        expected = md.stem
        if slug and slug != expected:
            issues.append(Issue("error", "slug_matches_filename", rel_str,
                                f"slug `{slug}` ≠ filename stem `{expected}`"))

        # slug_discipline
        if slug and not SLUG_RE.match(slug):
            issues.append(Issue("warn", "slug_discipline", rel_str,
                                f"slug `{slug}` not kebab-case ASCII (must match {SLUG_RE.pattern})"))

        # folder_type_match
        folder = folder_path_for(rel)
        if folder:
            expected_type = FOLDER_EXPECTED_TYPE.get(folder)
            if expected_type and ftype and ftype != expected_type:
                issues.append(Issue("error", "folder_type_match", rel_str,
                                    f"file in `{folder}/` has type `{ftype}`, expected `{expected_type}`"))
            if folder in DEPRECATED_FOLDERS:
                issues.append(Issue("warn", "deprecated_folder", rel_str,
                                    f"`{folder}/` is a pre-2026-05-14 layout; "
                                    f"move to the single-vault target (people/, vendors/, etc.)"))

        # audience_valid
        aud = fm.get("audience")
        if aud is not None and aud != "" and not audience_valid(aud):
            issues.append(Issue("error", "audience_valid", rel_str,
                                f"audience `{aud}` not in allowed forms "
                                f"(personal | department | org | ceo-only | departments:X,Y)"))

        # departments_in_vocab — check both `departments:` and audience departments
        for dept in list_values(fm.get("departments")):
            if dept not in LOCKED_DEPTS:
                issues.append(Issue("error", "departments_in_vocab", rel_str,
                                    f"`departments:` entry `{dept}` not in locked vocab "
                                    f"({', '.join(sorted(LOCKED_DEPTS))})"))
        for dept in audience_departments(aud):
            if dept not in LOCKED_DEPTS:
                issues.append(Issue("error", "departments_in_vocab", rel_str,
                                    f"audience references unknown dept `{dept}`"))

        # date_format
        for date_key in ("created", "updated"):
            d = fm.get(date_key)
            if d and not DATE_RE.match(str(d).strip().strip("\"'")):
                issues.append(Issue("warn", "date_format", rel_str,
                                    f"`{date_key}: {d}` not in YYYY-MM-DD form"))

        # source_immutability
        if folder.startswith("sources") and fm.get("updated"):
            issues.append(Issue("warn", "source_immutability", rel_str,
                                f"file in `sources/` has `updated:` — sources should be frozen at capture time"))

        # captured_by_present — only enforced as a warning for content types
        # not already caught by required_fields (i.e., types we don't want to
        # *fail* on but still want to flag for audit-chain hygiene).
        if ftype in CONTENT_TYPES and not str(fm.get("captured_by", "")).strip():
            # required_fields will have caught this as an ERROR already; skip
            # the duplicate WARN to avoid noise.
            pass

        # Collect refs for incoming-links pass
        # 1) wikilinks in body
        for m in WIKILINK_RE.finditer(body):
            target = m.group(1).strip()
            incoming_refs[target] += 1
        # 2) related: and sources: frontmatter entries
        for key in ("related", "sources"):
            for s in list_values(fm.get(key)):
                # External URLs in sources: aren't slug refs
                if s.startswith("http://") or s.startswith("https://"):
                    continue
                incoming_refs[s] += 1

    # ── Pass 3: cross-reference resolution + orphan detection ──────────────
    all_slugs = set(files_by_slug.keys())
    for md, fm in fm_by_file.items():
        rel = md.relative_to(vault)
        rel_str = str(rel)
        body = body_by_file[md]
        slug = str(fm.get("slug", "")).strip()

        # wikilinks_resolve — every [[X]] in body must resolve
        for m in WIKILINK_RE.finditer(body):
            target = m.group(1).strip()
            if target and target not in all_slugs:
                issues.append(Issue("error", "wikilinks_resolve", rel_str,
                                    f"broken wikilink `[[{target}]]` — no file with that slug"))

        # sources_resolve (and related)
        for key, sev in (("sources", "warn"), ("related", "warn")):
            for s in list_values(fm.get(key)):
                if s.startswith("http://") or s.startswith("https://"):
                    continue
                if s not in all_slugs:
                    issues.append(Issue(sev, f"{key}_resolve", rel_str,
                                        f"`{key}:` entry `{s}` does not resolve to any vault file"))

        # orphan — page has no incoming refs and isn't in an entry-point folder
        folder = folder_path_for(rel)
        is_entry_point_folder = folder.startswith("sources") or folder == "" or rel.parts[0] == "inbox"
        # Also skip vault-level fixtures
        skip_orphan_names = {"index.md", "log.md", "CLAUDE.md", "README.md", "BOOTSTRAP.md", "CHANGELOG.md",
                             "TEMPLATE-VERSION", "BOOTSTRAPPED-FROM-VERSION"}
        if (slug and slug not in incoming_refs and not is_entry_point_folder
                and md.name not in skip_orphan_names):
            issues.append(Issue("warn", "orphan", rel_str,
                                f"no incoming wikilinks or references from any other page"))

    # Duplicate slug detection
    for slug, files in files_by_slug.items():
        if len(files) > 1:
            for f in files:
                issues.append(Issue("error", "slug_unique", str(f.relative_to(vault)),
                                    f"slug `{slug}` used in {len(files)} files: " +
                                    ", ".join(str(x.relative_to(vault)) for x in files)))

    return issues


# ── Reporting ─────────────────────────────────────────────────────────────

def render_human(issues: list[Issue]) -> str:
    if not issues:
        return "lint-vault: ✓ clean — no issues found"
    by_check: dict[str, list[Issue]] = defaultdict(list)
    for i in issues:
        by_check[i.check].append(i)
    lines = []
    error_count = sum(1 for i in issues if i.severity == "error")
    warn_count = sum(1 for i in issues if i.severity == "warn")
    lines.append(f"lint-vault: {error_count} error(s), {warn_count} warning(s)\n")
    for check in sorted(by_check):
        items = by_check[check]
        sev = items[0].severity.upper()
        lines.append(f"[{sev}] {check} — {len(items)} issue(s):")
        for it in items[:50]:
            lines.append(f"  {it.file} — {it.message}")
        if len(items) > 50:
            lines.append(f"  …and {len(items) - 50} more")
        lines.append("")
    return "\n".join(lines).rstrip()


# ── Main ──────────────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description="Lint a Prime Radiant vault for schema + integrity issues.")
    p.add_argument("--vault", required=True, help="Vault root (personal or department)")
    p.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of human report")
    p.add_argument("--strict", action="store_true", help="Treat warnings as errors for exit code")
    p.add_argument("--quiet", action="store_true", help="Only print the final summary line")
    args = p.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"vault not found: {vault}", file=sys.stderr)
        return 2

    issues = lint(vault)
    error_count = sum(1 for i in issues if i.severity == "error")
    warn_count = sum(1 for i in issues if i.severity == "warn")

    if args.json:
        report = {
            "vault": str(vault),
            "stats": {"errors": error_count, "warnings": warn_count, "total": len(issues)},
            "issues": [i.to_dict() for i in issues],
        }
        print(json.dumps(report, indent=2))
    elif args.quiet:
        print(f"lint-vault: errors={error_count} warnings={warn_count}")
    else:
        print(render_human(issues))

    exit_code = error_count + (warn_count if args.strict else 0)
    return min(exit_code, 1)  # exit codes >= 1 indicate failure; cap at 1 for shell convenience


if __name__ == "__main__":
    sys.exit(main())

```