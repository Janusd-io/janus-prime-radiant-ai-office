---
type: source
source_type: laptop
title: discover
slug: discover
created: 2026-05-13
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/discover.sh
original_size: 8022
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# discover

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/discover.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# discover.sh — scaffold a Personal Prime Radiant vault for one employee.
#
# Usage:
#   discover.sh --scaffold-radiant <vault-path> <person-slug> <person-name> <dept-slugs>
#     where <dept-slugs> is a comma-separated list, e.g. "ai-office" or "hr,it-ops"
#
#   discover.sh --detect-drive             # print the Google Drive mount root
#   discover.sh --check <vault-path>       # verify a vault looks Prime-Radiant-shaped
#   discover.sh --find-aio-self <person-slug>   # print path to entities/internal/<slug>.md in AIO if it exists

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATES_DIR="$SKILL_DIR/templates"

# ──────────────────────────────────────────────────────────────────────────
# AIO instance detection (Git substrate)
#
# AIO Prime Radiant now lives in a GitHub repo (per 2026-05-13 brief), cloned
# locally to ~/janus/prime-radiant/ai-office/. The (legacy) Drive path is
# checked as a fallback so this script still works on machines mid-migration.
# ──────────────────────────────────────────────────────────────────────────
VAULT_ROOT_DEFAULT="${JB_VAULT_ROOT:-$HOME/janus/prime-radiant}"

aio_instance_path() {
  local primary="$VAULT_ROOT_DEFAULT/ai-office"
  if [[ -d "$primary/.git" ]] || [[ -f "$primary/CLAUDE.md" ]]; then
    echo "$primary"
    return 0
  fi
  # Legacy Drive fallback — temporary, while migration is in flight
  for d in "$HOME/Library/CloudStorage/"GoogleDrive-*/; do
    if [[ -d "$d" ]]; then
      local legacy="$d/Shared drives/Janus AI Office/Janus Prime Radiant — AI Office"
      if [[ -d "$legacy" ]]; then
        echo "$legacy"
        return 0
      fi
    fi
  done
  return 1
}

# Kept for backward compat; emits a warning that the substrate has moved.
detect_drive_root() {
  for d in "$HOME/Library/CloudStorage/"GoogleDrive-*/; do
    if [[ -d "$d" ]]; then
      echo "$d"
      return 0
    fi
  done
  return 1
}

# ──────────────────────────────────────────────────────────────────────────
# Modes
# ──────────────────────────────────────────────────────────────────────────
case "${1:-}" in
  --detect-drive)
    if drive=$(detect_drive_root); then
      echo "$drive"
      exit 0
    fi
    echo "no Google Drive mount found" >&2
    exit 1
    ;;
  --check)
    vault="${2:-}"
    if [[ -z "$vault" ]]; then
      echo "usage: $0 --check <vault-path>" >&2
      exit 2
    fi
    missing=0
    for required in CLAUDE.md index.md log.md inbox sources entities concepts decisions lessons questions pulse briefs; do
      if [[ ! -e "$vault/$required" ]]; then
        echo "missing: $required"
        missing=$((missing+1))
      fi
    done
    if [[ $missing -eq 0 ]]; then
      echo "vault looks Prime-Radiant-shaped: $vault"
      exit 0
    fi
    exit 1
    ;;
  --find-aio-self)
    slug="${2:-}"
    [[ -z "$slug" ]] && { echo "usage: $0 --find-aio-self <person-slug>" >&2; exit 2; }
    if aio=$(aio_instance_path); then
      candidate="$aio/entities/internal/${slug}.md"
      if [[ -f "$candidate" ]]; then
        echo "$candidate"
        exit 0
      fi
    fi
    exit 1
    ;;
  --scaffold-radiant)
    vault="${2:-}"
    person_slug="${3:-}"
    person_name="${4:-}"
    dept_slugs="${5:-ai-office}"
    if [[ -z "$vault" || -z "$person_slug" || -z "$person_name" ]]; then
      echo "usage: $0 --scaffold-radiant <vault-path> <person-slug> <person-name> [<dept-slugs>]" >&2
      exit 2
    fi

    mkdir -p "$vault"

    # Top-level folders
    for d in inbox inbox/.processed sources sources/laptop sources/meetings sources/articles \
             sources/linear sources/notion sources/slack sources/monday sources/misc \
             entities entities/internal entities/vendors entities/clients entities/external entities/departments \
             concepts processes projects decisions lessons questions pulse briefs; do
      mkdir -p "$vault/$d"
    done

    today=$(date -u +"%Y-%m-%d")
    timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # CLAUDE.md — substitute placeholders
    sed -e "s|{{PERSON}}|${person_name}|g" \
        -e "s|{{PERSON_SLUG}}|${person_slug}|g" \
        -e "s|{{DATE}}|${today}|g" \
        "$TEMPLATES_DIR/personal-claude-md.md" > "$vault/CLAUDE.md"

    # index.md stub
    cat > "$vault/index.md" <<EOF
# Wiki Index

_Updated: ${today}_

> Content catalog for **Janus Prime Radiant · ${person_name} (Personal)**. One line per page, grouped by category. See \`CLAUDE.md\` for the schema. This file is regenerated by \`ingest-to-radiant.py\` after each ingest pass.

_(no entries yet — run a bootstrap ingest to populate)_
EOF

    # log.md first entry
    log_ts=$(date -u +"%Y-%m-%d %H:%M")
    cat > "$vault/log.md" <<EOF
## [${log_ts}] scaffold | /janus-brain | initial scaffold for ${person_name}
- person: ${person_slug}
- departments: ${dept_slugs}
- vault: ${vault}
- derived from: AI Office Prime Radiant CLAUDE.md v0.8
EOF

    # Self-page — try to seed from AIO entities/internal/<slug>.md if it exists
    self_target="$vault/entities/internal/${person_slug}.md"
    if aio_self=$("$0" --find-aio-self "$person_slug" 2>/dev/null); then
      cp "$aio_self" "$self_target"
      # Force audience to department-level for the personal copy
      python3 - "$self_target" <<'PY'
import re, sys, pathlib
p = pathlib.Path(sys.argv[1])
t = p.read_text(encoding="utf-8")
# Add audience and captured_by if missing
fm_match = re.match(r"^---\n(.*?)\n---", t, re.DOTALL)
if fm_match:
    fm = fm_match.group(1)
    if "audience:" not in fm:
        fm += "\naudience: [department]"
    if "captured_by:" not in fm:
        slug = next((l.split(":", 1)[1].strip() for l in fm.splitlines() if l.startswith("slug:")), "")
        fm += f"\ncaptured_by: {slug}"
    t = f"---\n{fm}\n---" + t[fm_match.end():]
    p.write_text(t, encoding="utf-8")
PY
    else
      # Use the template
      sed -e "s|{{PERSON_NAME}}|${person_name}|g" \
          -e "s|{{PERSON_SLUG}}|${person_slug}|g" \
          -e "s|{{DATE}}|${today}|g" \
          -e "s|{{DEPT_SLUGS}}|${dept_slugs}|g" \
          "$TEMPLATES_DIR/personal-self-page.md" > "$self_target"
    fi

    # Department stubs — one per dept the person belongs to (federation layer)
    IFS=',' read -ra DEPTS <<< "$dept_slugs"
    for dept in "${DEPTS[@]}"; do
      dept_trim=$(echo "$dept" | tr -d ' ')
      [[ -z "$dept_trim" ]] && continue
      dept_target="$vault/entities/departments/${dept_trim}.md"
      if [[ ! -f "$dept_target" ]]; then
        cat > "$dept_target" <<EOF
---
type: department
title: ${dept_trim}
slug: ${dept_trim}
created: ${today}
updated: ${today}
status: active
audience: [department]
captured_by: ${person_slug}
---

# ${dept_trim}

Federation stub. The canonical Prime Radiant for this department is the authoritative source. This page exists in ${person_name}'s personal vault to make \`departments: [${dept_trim}]\` frontmatter resolve cleanly via \`[[${dept_trim}]]\` wikilinks.
EOF
      fi
    done

    echo "$vault"
    ;;
  *)
    echo "discover.sh — scaffold or inspect Personal Prime Radiant vaults" >&2
    echo "" >&2
    echo "usage:" >&2
    echo "  $0 --scaffold-radiant <vault-path> <person-slug> <person-name> [<dept-slugs>]" >&2
    echo "  $0 --detect-drive" >&2
    echo "  $0 --check <vault-path>" >&2
    echo "  $0 --find-aio-self <person-slug>" >&2
    exit 2
    ;;
esac

```