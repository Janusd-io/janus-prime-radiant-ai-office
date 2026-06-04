#!/usr/bin/env python3
"""Build the Prime Radiant daily-snapshot JSON from the local AI-Office vault.

Reads frontmatter across questions/, inbox/, projects/ and pulse/ and emits a
single JSON object on stdout. Consumed by the Prime Radiant morning dashboard
(live artifact, via a Notion page) and refreshed each morning by a scheduled
task. Pure stdlib; safe to run repeatedly.
"""
import json
import os
import re
import sys
from datetime import datetime, date
from zoneinfo import ZoneInfo

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TZ = ZoneInfo("Asia/Dubai")
TODAY = datetime.now(TZ).date()
AGING_DAYS = 14
OWNER_ME = "michael-bruck"


def parse_frontmatter(path):
    """Return dict of simple `key: value` frontmatter, or {} if none."""
    fm = {}
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return fm, ""
    if not text.startswith("---"):
        return fm, text
    end = text.find("\n---", 3)
    if end == -1:
        return fm, text
    block = text[3:end]
    body = text[end + 4:]
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            val = val.strip('"').strip("'")
            fm[key] = val
    return fm, body


def to_date(s):
    if not s:
        return None
    s = s.strip().strip('"').strip("'")
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return None


def age_days(created):
    d = to_date(created)
    if not d:
        return None
    return (TODAY - d).days


def md_files(subdir, recursive=False):
    root = os.path.join(VAULT, subdir)
    out = []
    if not os.path.isdir(root):
        return out
    if recursive:
        for dp, _, files in os.walk(root):
            if "/." in dp or os.path.basename(dp).startswith("."):
                continue
            for fn in files:
                if fn.endswith(".md"):
                    out.append(os.path.join(dp, fn))
    else:
        for fn in os.listdir(root):
            p = os.path.join(root, fn)
            if fn.endswith(".md") and os.path.isfile(p):
                out.append(p)
    return out


# ---- Questions (open = status: active) -----------------------------------
open_questions, aging = [], []
for p in md_files("questions"):
    fm, _ = parse_frontmatter(p)
    if fm.get("status", "").lower() != "active":
        continue
    a = age_days(fm.get("created"))
    rec = {
        "title": fm.get("title") or os.path.basename(p)[:-3],
        "slug": fm.get("slug", ""),
        "owner": fm.get("owner", ""),
        "created": fm.get("created", ""),
        "ageDays": a,
        "file": os.path.relpath(p, VAULT),
    }
    open_questions.append(rec)
    if a is not None and a > AGING_DAYS:
        aging.append(rec)
open_questions.sort(key=lambda r: (r["ageDays"] is None, -(r["ageDays"] or 0)))
aging.sort(key=lambda r: -(r["ageDays"] or 0))

# ---- Inbox (top-level clippings to triage) -------------------------------
inbox = []
for p in md_files("inbox"):
    fm, _ = parse_frontmatter(p)
    inbox.append({
        "title": fm.get("title") or os.path.basename(p)[:-3],
        "source": fm.get("source", ""),
        "created": fm.get("created", ""),
        "published": fm.get("published", ""),
        "file": os.path.relpath(p, VAULT),
    })
inbox.sort(key=lambda r: r["created"], reverse=True)

# ---- Projects (active / live) --------------------------------------------
projects = []
for p in md_files("projects"):
    fm, _ = parse_frontmatter(p)
    st = fm.get("status", "").lower()
    if st not in ("active", "live"):
        continue
    projects.append({
        "title": fm.get("title") or os.path.basename(p)[:-3],
        "slug": fm.get("slug", ""),
        "status": st,
        "owner": fm.get("owner", ""),
        "updated": fm.get("updated", ""),
        "mine": fm.get("owner", "") == OWNER_ME,
        "file": os.path.relpath(p, VAULT),
    })
# most recently updated first, then mine to the top
projects.sort(key=lambda r: r["updated"], reverse=True)
projects.sort(key=lambda r: not r["mine"])

# ---- Latest pulse ---------------------------------------------------------
latest_pulse = None
pulse_files = md_files("pulse")
dated = []
for p in pulse_files:
    base = os.path.basename(p)
    m = re.match(r"(\d{4}-\d{2}-\d{2})", base)
    if m:
        dated.append((m.group(1), p))
dated.sort(reverse=True)
if dated:
    pdate, ppath = dated[0]
    fm, body = parse_frontmatter(ppath)
    headline = ""
    hm = re.search(r"##\s*Headline\s*\n+([^\n]+)", body)
    if hm:
        headline = re.sub(r"\*\*", "", hm.group(1)).strip()
    else:
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith("#"):
                headline = re.sub(r"\*\*", "", s).strip()
                break
    latest_pulse = {
        "title": fm.get("title") or os.path.basename(ppath)[:-3],
        "date": pdate,
        "slug": fm.get("slug", ""),
        "headline": headline[:400],
        "file": os.path.relpath(ppath, VAULT),
    }

snapshot = {
    "generatedAt": datetime.now(TZ).isoformat(timespec="minutes"),
    "today": TODAY.isoformat(),
    "counts": {
        "openQuestions": len(open_questions),
        "aging": len(aging),
        "inbox": len(inbox),
        "activeProjects": len(projects),
        "myProjects": sum(1 for p in projects if p["mine"]),
    },
    "openQuestions": open_questions,
    "agingEscalations": aging,
    "inbox": inbox,
    "activeProjects": projects,
    "latestPulse": latest_pulse,
}

json.dump(snapshot, sys.stdout, ensure_ascii=False, indent=2)
sys.stdout.write("\n")
