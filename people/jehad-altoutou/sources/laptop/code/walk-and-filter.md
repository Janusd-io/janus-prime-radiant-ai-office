---
type: source
source_type: laptop
title: walk-and-filter
slug: walk-and-filter
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/walk-and-filter.py
original_size: 11682
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# walk-and-filter

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/walk-and-filter.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
walk-and-filter.py — Walk $HOME, apply the privacy filter, classify files,
and emit a manifest.json that the rest of /janus-brain consumes.

Reads:
  config/exclude-patterns.txt  (basename globs, never edited by users)
  config/exclude-paths.txt     ($HOME-relative path prefixes)
  config/include-extensions.txt
  config/user-exclude.txt      (user-added basename globs)
  state/manifest.json          (previous manifest, for delta computation)

Writes:
  state/manifest.json
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────
# File classification — maps extension → vault section + category
# Routing aligns with references/vault-structure.md
# ─────────────────────────────────────────────────────────────────────────
CATEGORY_BY_EXT = {
    # Notes / docs
    **{ext: "notes" for ext in [".md", ".markdown", ".txt", ".rst", ".org", ".adoc", ".asciidoc", ".rtf"]},
    # Office / portable
    **{ext: "docs" for ext in [".docx", ".doc", ".odt", ".html", ".htm", ".epub", ".tex"]},
    ".pdf": "pdfs",
    # Slides
    **{ext: "slides" for ext in [".pptx", ".ppt", ".odp"]},
    # Sheets
    **{ext: "sheets" for ext in [".xlsx", ".xls", ".ods", ".csv", ".tsv"]},
    # Code (lightly enriched)
    **{ext: "code" for ext in [
        ".py", ".ipynb", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
        ".go", ".rs", ".java", ".kt", ".swift", ".c", ".h", ".cpp", ".hpp",
        ".cc", ".cs", ".rb", ".php", ".scala", ".sh", ".bash", ".zsh",
        ".fish", ".lua", ".r", ".jl", ".dart", ".vue", ".svelte", ".astro",
    ]},
    # Config
    **{ext: "config" for ext in [
        ".json", ".yaml", ".yml", ".toml", ".ini", ".conf", ".sql",
        ".graphql", ".proto",
    ]},
    # Images
    **{ext: "images" for ext in [
        ".png", ".jpg", ".jpeg", ".heic", ".heif", ".webp", ".tiff",
        ".bmp", ".gif",
    ]},
}

# Vault section per category — these align with references/vault-structure.md
SECTION_BY_CATEGORY = {
    "notes":  "10 Knowledge",
    "docs":   "10 Knowledge",
    "pdfs":   "10 Knowledge",
    "slides": "10 Knowledge",
    "sheets": "10 Knowledge",
    "code":   "10 Knowledge/Code",
    "config": "10 Knowledge/Config",
    "images": "10 Knowledge/Images",
}

OVERSIZE_BYTES = 2 * 1024 * 1024  # 2 MB text cap before warning

# Hard skip — any path containing one of these segments is out, even if
# the user has cleared the exclude paths. Defence in depth.
HARD_SKIP_SEGMENTS = {
    ".ssh", ".aws", ".gnupg", ".gcp", ".azure", ".kube", ".docker",
    ".password-store", ".config/gcloud", ".config/gh",
    "Library/Keychains", "Library/Mail", "Library/Messages",
}


def load_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [
        line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def is_hidden(path: Path, root: Path) -> bool:
    """A path is 'hidden' if any segment relative to $HOME starts with a dot."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    return any(part.startswith(".") for part in rel.parts)


def matches_basename(name: str, patterns: list[str]) -> bool:
    name_lower = name.lower()
    return any(fnmatch.fnmatch(name_lower, p.lower()) for p in patterns)


def under_excluded_path(path: Path, home: Path, excluded_prefixes: list[Path]) -> bool:
    try:
        rel = path.relative_to(home)
    except ValueError:
        return False
    rel_posix = rel.as_posix()
    return any(rel_posix == p.as_posix() or rel_posix.startswith(p.as_posix() + "/") for p in excluded_prefixes)


def hard_skip(path: Path) -> bool:
    posix = path.as_posix()
    return any(seg in posix for seg in HARD_SKIP_SEGMENTS)


def classify(ext: str) -> tuple[str, str] | None:
    ext = ext.lower()
    cat = CATEGORY_BY_EXT.get(ext)
    if not cat:
        return None
    return cat, SECTION_BY_CATEGORY.get(cat, "10 Knowledge")


def word_estimate(size_bytes: int, ext: str) -> int:
    """Rough word count estimate without reading the file."""
    if ext in {".pdf", ".docx", ".pptx", ".xlsx"}:
        return size_bytes // 12      # binary-encoded, ~12 bytes per word
    if ext in {".png", ".jpg", ".jpeg", ".heic", ".webp", ".gif", ".bmp", ".tiff"}:
        return 0                     # OCR happens later, words unknown
    return size_bytes // 6           # plain text, ~6 bytes per word


def file_signature(path: Path) -> str:
    """Cheap fingerprint: size + mtime. Avoids hashing huge files."""
    try:
        st = path.stat()
        return f"{st.st_size}:{int(st.st_mtime)}"
    except OSError:
        return ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Root to walk (usually $HOME)")
    parser.add_argument("--vault", required=True, help="Obsidian vault path (skipped during walk)")
    parser.add_argument("--config", required=True, help="Config dir with exclude/include lists")
    parser.add_argument("--out", required=True, help="Path to manifest.json")
    parser.add_argument("--prev", default=None, help="Previous manifest.json for delta (optional)")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    vault = Path(args.vault).expanduser().resolve()
    config_dir = Path(args.config).expanduser().resolve()
    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    exclude_patterns = load_lines(config_dir / "exclude-patterns.txt")
    user_exclude = load_lines(config_dir / "user-exclude.txt")
    exclude_path_lines = load_lines(config_dir / "exclude-paths.txt")
    include_exts = {e.lower() for e in load_lines(config_dir / "include-extensions.txt")}

    # Resolve excluded paths to absolute Path objects under $HOME
    excluded_prefixes = []
    for line in exclude_path_lines:
        p = Path(line)
        if p.is_absolute():
            excluded_prefixes.append(p)
        else:
            excluded_prefixes.append(root / p)
    # Skip the vault itself so we don't recursively scan our own output
    excluded_prefixes.append(vault)

    all_patterns = exclude_patterns + user_exclude

    prev_signatures: dict[str, str] = {}
    if args.prev and Path(args.prev).exists():
        try:
            prev = json.loads(Path(args.prev).read_text())
            prev_signatures = {item["path"]: item.get("signature", "") for item in prev.get("included", [])}
        except (OSError, json.JSONDecodeError):
            pass

    included: list[dict] = []
    excluded_summary = {
        "hidden_path": 0,
        "library_or_excluded_path": 0,
        "privacy_pattern": 0,
        "binary_skip": 0,
        "oversized": 0,
        "hard_skip": 0,
    }
    by_category: dict[str, int] = {}
    total_words = 0

    for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        cur_dir = Path(dirpath)

        # Prune directories in-place so we never descend into them.
        new_dirnames = []
        for d in dirnames:
            full = cur_dir / d
            if is_hidden(full, root):
                excluded_summary["hidden_path"] += 1
                continue
            if hard_skip(full):
                excluded_summary["hard_skip"] += 1
                continue
            if under_excluded_path(full, root, excluded_prefixes):
                excluded_summary["library_or_excluded_path"] += 1
                continue
            if matches_basename(d, all_patterns):
                excluded_summary["privacy_pattern"] += 1
                continue
            new_dirnames.append(d)
        dirnames[:] = new_dirnames

        for fname in filenames:
            full = cur_dir / fname
            if is_hidden(full, root):
                excluded_summary["hidden_path"] += 1
                continue
            if hard_skip(full):
                excluded_summary["hard_skip"] += 1
                continue
            if under_excluded_path(full, root, excluded_prefixes):
                excluded_summary["library_or_excluded_path"] += 1
                continue
            if matches_basename(fname, all_patterns):
                excluded_summary["privacy_pattern"] += 1
                continue

            ext = full.suffix.lower()
            if ext not in include_exts:
                excluded_summary["binary_skip"] += 1
                continue

            cls = classify(ext)
            if cls is None:
                excluded_summary["binary_skip"] += 1
                continue
            category, section = cls

            try:
                size = full.stat().st_size
            except OSError:
                continue

            words = word_estimate(size, ext)
            oversized = size > OVERSIZE_BYTES and category not in {"images"}
            if oversized:
                excluded_summary["oversized"] += 1

            rel = full.relative_to(root).as_posix()
            sig = file_signature(full)

            included.append({
                "path": str(full),
                "rel": rel,
                "ext": ext,
                "size": size,
                "words": words,
                "category": category,
                "section": section,
                "oversized": oversized,
                "signature": sig,
                "status": "modified" if rel in prev_signatures and prev_signatures.get(str(full)) != sig else (
                    "unchanged" if str(full) in prev_signatures else "added"
                ),
            })
            by_category[category] = by_category.get(category, 0) + 1
            total_words += words

    # Delta: anything in prev but not in current = deleted
    current_paths = {item["path"] for item in included}
    deleted = [p for p in prev_signatures if p not in current_paths]
    added = [item for item in included if item["status"] == "added"]
    modified = [item for item in included if item["status"] == "modified"]

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "vault": str(vault),
        "summary": {
            "total_included": len(included),
            "total_words": total_words,
            "by_category": by_category,
            "excluded": excluded_summary,
            "delta": {
                "added": len(added),
                "modified": len(modified),
                "deleted": len(deleted),
            },
        },
        "included": included,
        "deleted": deleted,
    }

    out_path.write_text(json.dumps(manifest, indent=2))

    print(f"manifest written: {out_path}")
    print(f"included:        {len(included)}")
    print(f"total words:     ~{total_words:,}")
    print("by category:")
    for cat, n in sorted(by_category.items(), key=lambda kv: -kv[1]):
        print(f"  {cat:8s} {n}")
    print("excluded:")
    for reason, n in excluded_summary.items():
        print(f"  {reason:25s} {n}")
    print(f"delta:           +{len(added)} ~{len(modified)} -{len(deleted)}")


if __name__ == "__main__":
    sys.exit(main())

```