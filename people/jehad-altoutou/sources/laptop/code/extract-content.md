---
type: source
source_type: laptop
title: extract-content
slug: extract-content
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/extract-content.py
original_size: 18534
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# extract-content

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/extract-content.py` on 2026-05-14._

```python
#!/usr/bin/env python3
"""
extract-content.py — Convert every laptop file in the walker's manifest into a
markdown file with full content (not summaries) under
people/<slug>/sources/laptop/ in the shared dept vault.

Per Jehad's 2026-05-13 request: PDFs, docs, slides, sheets, images, code, and
plain text all get FULL extraction into the personal vault, so federation
and search work on real content rather than filenames.

Tools used (all local, free; fail gracefully if missing):
  - pdftotext   (poppler-utils)   for .pdf
  - pandoc                          for .docx / .doc / .rtf / .odt / .html / .epub / .tex / .pptx / .ppt / .odp
  - pandas (or csv stdlib)          for .xlsx / .xls / .csv / .tsv
  - tesseract                       for .png / .jpg / .jpeg / .heic / .webp / .gif / .bmp / .tiff
  - direct copy                     for .md / .txt / .markdown / .rst / .org / .adoc / .asciidoc

Output: one markdown file per source file at
  <vault>/people/<captured_by>/sources/laptop/<category>/<slug>.md

Each output carries frontmatter (type, source_type, title, slug, created,
captured_by, audience=personal by default, original_path, original_size,
original_ext, extracted_with, extracted_at) followed by the extracted body.

Image markdown carries OCR text. If OCR finds little text, the file is flagged
`needs_vision_description: true` so the Phase 5 enrichment subagent supplements
with a vision-model description.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ── Tooling availability checks ──────────────────────────────────────────

def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


HAS_PDFTOTEXT = have("pdftotext")
HAS_PANDOC = have("pandoc")
HAS_TESSERACT = have("tesseract")

try:
    import pandas as pd  # type: ignore
    HAS_PANDAS = True
except Exception:
    HAS_PANDAS = False

# ── File-type handling ───────────────────────────────────────────────────

# Extensions handled by each tool
EXTS_PDFTOTEXT = {".pdf"}
EXTS_PANDOC = {".docx", ".doc", ".rtf", ".odt", ".html", ".htm", ".epub", ".tex",
               ".pptx", ".ppt", ".odp"}
EXTS_SHEETS = {".xlsx", ".xls", ".ods", ".csv", ".tsv"}
EXTS_IMAGES = {".png", ".jpg", ".jpeg", ".heic", ".webp", ".gif", ".bmp", ".tiff"}
EXTS_TEXT = {".md", ".markdown", ".txt", ".rst", ".org", ".adoc", ".asciidoc"}
EXTS_CODE = {".py", ".ipynb", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
             ".go", ".rs", ".java", ".kt", ".swift", ".c", ".h", ".cpp", ".hpp",
             ".cc", ".cs", ".rb", ".php", ".scala", ".sh", ".bash", ".zsh",
             ".fish", ".lua", ".r", ".jl", ".dart", ".vue", ".svelte", ".astro"}
EXTS_CONFIG = {".json", ".yaml", ".yml", ".toml", ".ini", ".conf", ".sql",
               ".graphql", ".proto"}

# Max bytes to embed in markdown body. Files larger get truncated with a marker.
MAX_BODY_CHARS = 500_000   # ~125k tokens worst case; reasonable cap

# Tesseract OCR confidence threshold (chars). Below this, flag for vision.
OCR_MIN_CHARS = 50


# ── Helpers ──────────────────────────────────────────────────────────────

SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_len: int = 80) -> str:
    s = SLUG_RE.sub("-", text.lower()).strip("-")
    return s[:max_len].rstrip("-") or "untitled"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")


def date_from_mtime(p: Path) -> str:
    try:
        ts = p.stat().st_mtime
        return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d")
    except OSError:
        return today_str()


def safe_run(cmd: list[str], stdin: bytes | None = None, timeout: int = 120) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            cmd,
            input=stdin,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return (
            result.returncode,
            result.stdout.decode("utf-8", errors="replace"),
            result.stderr.decode("utf-8", errors="replace"),
        )
    except subprocess.TimeoutExpired:
        return (124, "", f"timeout after {timeout}s")
    except FileNotFoundError as e:
        return (127, "", str(e))


def truncate_with_marker(text: str) -> tuple[str, bool]:
    """Truncate to MAX_BODY_CHARS, return (text, was_truncated)."""
    if len(text) <= MAX_BODY_CHARS:
        return text, False
    head = text[:MAX_BODY_CHARS - 100]
    tail_note = f"\n\n…[truncated at {MAX_BODY_CHARS:,} chars; original file is larger]…\n"
    return head + tail_note, True


# ── Extractors (one per family) ──────────────────────────────────────────

def extract_pdf(path: Path) -> tuple[str, str | None]:
    """Return (body, error). body is markdown-ish plain text."""
    if not HAS_PDFTOTEXT:
        return "", "pdftotext not installed (brew install poppler)"
    rc, out, err = safe_run(["pdftotext", "-nopgbrk", str(path), "-"])
    if rc != 0:
        return "", f"pdftotext exited {rc}: {err.strip()[:200]}"
    return out, None


def extract_pandoc(path: Path) -> tuple[str, str | None]:
    if not HAS_PANDOC:
        return "", "pandoc not installed (brew install pandoc)"
    # Pandoc autodetects most input formats from extension.
    # gfm (GitHub-flavored Markdown) is the cleanest output for Obsidian.
    rc, out, err = safe_run(["pandoc", "-t", "gfm", str(path)])
    if rc != 0:
        return "", f"pandoc exited {rc}: {err.strip()[:200]}"
    return out, None


def extract_sheet(path: Path) -> tuple[str, str | None]:
    """Convert spreadsheet to markdown table(s)."""
    ext = path.suffix.lower()

    if ext in {".csv", ".tsv"}:
        # Use stdlib csv to avoid pandas dependency for the common case
        import csv
        sep = "\t" if ext == ".tsv" else ","
        rows: list[list[str]] = []
        try:
            with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
                reader = csv.reader(f, delimiter=sep)
                for i, row in enumerate(reader):
                    if i > 1000:  # cap for huge CSVs
                        rows.append(["…"])
                        break
                    rows.append([(cell or "").replace("|", "\\|") for cell in row])
        except Exception as e:
            return "", f"csv read failed: {e}"
        if not rows:
            return "(empty)", None
        return rows_to_markdown(rows), None

    # Excel / ODS — need pandas
    if not HAS_PANDAS:
        return "", f"pandas not installed (pip3 install pandas openpyxl) — skipping {ext}"
    try:
        engine = "openpyxl" if ext == ".xlsx" else None
        all_sheets = pd.read_excel(path, sheet_name=None, engine=engine)  # type: ignore
    except Exception as e:
        return "", f"excel read failed: {e}"

    parts = []
    for sheet_name, df in all_sheets.items():
        rows = [list(df.columns)] + df.head(1000).astype(str).values.tolist()
        parts.append(f"### Sheet: {sheet_name}\n\n{rows_to_markdown(rows)}")
        if len(df) > 1000:
            parts.append(f"\n_…and {len(df) - 1000:,} more rows_\n")
    return "\n\n".join(parts), None


def rows_to_markdown(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    n_cols = max(len(r) for r in rows)
    # Pad short rows
    padded = [r + [""] * (n_cols - len(r)) for r in rows]
    header = padded[0]
    sep = ["---"] * n_cols
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]
    for row in padded[1:]:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(out)


def extract_image(path: Path) -> tuple[str, dict, str | None]:
    """Return (body, extra_frontmatter_fields, error).

    Body is the OCR'd text (markdown-wrapped). Extra fields include
    `needs_vision_description: true` if OCR yielded < OCR_MIN_CHARS.
    """
    if not HAS_TESSERACT:
        return "", {"needs_vision_description": True}, "tesseract not installed (brew install tesseract)"
    rc, out, err = safe_run(["tesseract", str(path), "-", "-l", "eng", "--psm", "3"])
    if rc != 0:
        return "", {"needs_vision_description": True}, f"tesseract exited {rc}: {err.strip()[:200]}"
    text = out.strip()
    extra = {
        "ocr_char_count": len(text),
        "needs_vision_description": len(text) < OCR_MIN_CHARS,
    }
    if not text:
        text = "_(no text extracted by OCR — image may be visual-only; the Phase 5 enrichment subagent should describe it via vision)_"
    return text, extra, None


def extract_text(path: Path) -> tuple[str, str | None]:
    try:
        return path.read_text(encoding="utf-8", errors="replace"), None
    except OSError as e:
        return "", str(e)


def extract_code(path: Path) -> tuple[str, str | None]:
    """For code, embed as a fenced block with the language hint."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return "", str(e)
    ext = path.suffix.lower().lstrip(".")
    lang = {"py": "python", "ts": "typescript", "tsx": "tsx", "js": "javascript",
            "jsx": "jsx", "go": "go", "rs": "rust", "java": "java", "kt": "kotlin",
            "swift": "swift", "rb": "ruby", "php": "php", "sh": "bash", "bash": "bash",
            "zsh": "bash", "fish": "fish", "lua": "lua", "r": "r", "jl": "julia",
            "scala": "scala", "cs": "csharp", "cpp": "cpp", "c": "c", "h": "c",
            "sql": "sql"}.get(ext, ext)
    return f"```{lang}\n{text}\n```", None


def extract_config(path: Path) -> tuple[str, str | None]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return "", str(e)
    ext = path.suffix.lower().lstrip(".")
    lang = {"yml": "yaml", "yaml": "yaml", "json": "json", "toml": "toml",
            "sql": "sql", "graphql": "graphql"}.get(ext, ext)
    return f"```{lang}\n{text}\n```", None


# ── Frontmatter + output writing ─────────────────────────────────────────

def emit_yaml_value(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    s = str(value)
    if any(c in s for c in [":", "#", "[", "]", "{", "}", ",", '"', "'", "\n"]):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def write_extraction(
    vault: Path,
    category: str,
    item: dict,
    body: str,
    extra_fm: dict,
    captured_by: str,
    extracted_with: str,
    truncated: bool,
) -> Path:
    source_path = Path(item["path"])
    slug_base = slugify(source_path.stem) or slugify(item.get("rel", "untitled"))
    target_dir = vault / "people" / captured_by / "sources" / "laptop" / category
    target_dir.mkdir(parents=True, exist_ok=True)

    # Conflict handling: append numeric suffix if needed
    target = target_dir / f"{slug_base}.md"
    n = 2
    while target.exists():
        target = target_dir / f"{slug_base}-{n}.md"
        n += 1

    final_slug = target.stem
    title = source_path.stem.strip() or final_slug

    fm = {
        "type": "source",
        "source_type": "laptop",
        "title": title,
        "slug": final_slug,
        "created": date_from_mtime(source_path),
        "captured_by": captured_by,
        "audience": "personal",
        "sensitivity": "dept",
        "sensitivity_confidence": 0.5,
        "original_path": str(source_path),
        "original_size": item.get("size", 0),
        "original_ext": item.get("ext", ""),
        "category": category,
        "extracted_with": extracted_with,
        "extracted_at": now_iso(),
    }
    if truncated:
        fm["extraction_truncated"] = True
    fm.update(extra_fm)

    fm_lines = []
    for k, v in fm.items():
        fm_lines.append(f"{k}: {emit_yaml_value(v)}")
    fm_block = "---\n" + "\n".join(fm_lines) + "\n---\n\n"

    header = f"# {title}\n\n_Extracted from `{item['rel']}` on {today_str()}._\n\n"
    target.write_text(fm_block + header + body, encoding="utf-8")
    return target


# ── Main ─────────────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", required=True, help="walk-and-filter.py output JSON")
    p.add_argument("--vault", required=True, help="Personal Prime Radiant path")
    p.add_argument("--captured-by", required=True, help="kebab-case slug of vault owner")
    p.add_argument("--report", default=None, help="Write JSON report (default: <vault>/.state/extract-content.json)")
    p.add_argument("--limit", type=int, default=None, help="Stop after N files (testing)")
    p.add_argument("--only-categories", default=None, help="Comma-separated categories to extract (default: all)")
    p.add_argument("--skip-unchanged", action="store_true", help="Skip manifest items with status=unchanged")
    args = p.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"vault not found: {vault}", file=sys.stderr)
        return 2

    manifest_path = Path(args.manifest).expanduser().resolve()
    if not manifest_path.exists():
        print(f"manifest not found: {manifest_path}", file=sys.stderr)
        return 2

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    items: list[dict] = manifest.get("included", [])

    only_cats = None
    if args.only_categories:
        only_cats = {c.strip() for c in args.only_categories.split(",") if c.strip()}

    # Print tool availability up front
    print("extract-content: tooling check")
    print(f"  pdftotext: {'✓' if HAS_PDFTOTEXT else '✗ (install: brew install poppler)'}")
    print(f"  pandoc:    {'✓' if HAS_PANDOC else '✗ (install: brew install pandoc)'}")
    print(f"  tesseract: {'✓' if HAS_TESSERACT else '✗ (install: brew install tesseract)'}")
    print(f"  pandas:    {'✓' if HAS_PANDAS else '✗ (install: pip3 install pandas openpyxl)'}")
    print()

    counts: dict[str, int] = {}
    errors: list[dict] = []
    written: list[str] = []
    processed = 0

    for item in items:
        if args.limit and processed >= args.limit:
            break
        if args.skip_unchanged and item.get("status") == "unchanged":
            counts["skipped_unchanged"] = counts.get("skipped_unchanged", 0) + 1
            continue
        category = item.get("category", "")
        ext = (item.get("ext") or "").lower()
        if only_cats and category not in only_cats:
            counts["skipped_filter"] = counts.get("skipped_filter", 0) + 1
            continue

        src = Path(item["path"])
        if not src.is_file():
            errors.append({"path": str(src), "category": category, "error": "source missing"})
            continue

        body, extra_fm, err, tool = "", {}, None, ""
        if ext in EXTS_PDFTOTEXT:
            body, err = extract_pdf(src); tool = "pdftotext"
        elif ext in EXTS_PANDOC:
            body, err = extract_pandoc(src); tool = "pandoc"
        elif ext in EXTS_SHEETS:
            body, err = extract_sheet(src); tool = "sheets"
        elif ext in EXTS_IMAGES:
            body, extra_fm, err = extract_image(src); tool = "tesseract"
        elif ext in EXTS_TEXT:
            body, err = extract_text(src); tool = "text-copy"
        elif ext in EXTS_CODE:
            body, err = extract_code(src); tool = "code-fenced"
        elif ext in EXTS_CONFIG:
            body, err = extract_config(src); tool = "config-fenced"
        else:
            counts["skipped_unknown_ext"] = counts.get("skipped_unknown_ext", 0) + 1
            continue

        if err:
            errors.append({"path": str(src), "category": category, "tool": tool, "error": err})
            counts[f"failed_{category}"] = counts.get(f"failed_{category}", 0) + 1
            continue

        body_clean, truncated = truncate_with_marker(body)
        try:
            target = write_extraction(
                vault=vault,
                category=category,
                item=item,
                body=body_clean,
                extra_fm=extra_fm,
                captured_by=args.captured_by,
                extracted_with=tool,
                truncated=truncated,
            )
            written.append(str(target.relative_to(vault)))
            counts[f"wrote_{category}"] = counts.get(f"wrote_{category}", 0) + 1
            processed += 1
        except OSError as e:
            errors.append({"path": str(src), "category": category, "error": f"write failed: {e}"})

    # Write report
    report_path = Path(args.report).expanduser().resolve() if args.report else vault / ".state" / "extract-content.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "ran_at": now_iso(),
        "manifest": str(manifest_path),
        "vault": str(vault),
        "tooling": {
            "pdftotext": HAS_PDFTOTEXT,
            "pandoc": HAS_PANDOC,
            "tesseract": HAS_TESSERACT,
            "pandas": HAS_PANDAS,
        },
        "counts": counts,
        "errors": errors[:200],   # cap so the report stays readable
        "error_count": len(errors),
        "files_written": len(written),
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"extract-content: complete")
    print(f"  files written: {len(written)}")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    if errors:
        print(f"  errors: {len(errors)} (see {report_path})")
        for e in errors[:5]:
            print(f"    {e.get('path', '?')}: {e.get('error', '')[:120]}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

```