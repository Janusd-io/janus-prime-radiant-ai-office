---
type: source
source_type: laptop
title: scaffold-person-subtree
slug: scaffold-person-subtree
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/scaffold-person-subtree.sh
original_size: 5775
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# scaffold-person-subtree

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/scaffold-person-subtree.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# scaffold-person-subtree.sh — Create `<vault>/people/<slug>/` inside the
# single dept-shared vault. Idempotent: existing files are not overwritten.
#
# Usage:
#   scaffold-person-subtree.sh \
#     --vault-root "$HOME/janus/prime-radiant" \
#     --person-slug jehad-altoutou \
#     --person-name "Jehad Altoutou" \
#     --primary-dept ai-office \
#     --task-tracker linear      # linear | monday | asana | notion | none | other
#
# Creates:
#   people/<slug>/.config.yaml      ← task_tracker, primary_dept, person_name, captured_by
#   people/<slug>/CLAUDE.md          ← from templates/personal-claude-md.md (placeholders substituted)
#   people/<slug>/self.md             ← from templates/personal-self-page.md
#   people/<slug>/sources/             (dept-visible)
#   people/<slug>/meetings/            (dept-visible)
#   people/<slug>/private/             (gitignored — sensitivity=self|confidential)
#   people/<slug>/.review-queue.md     (header only; low-confidence items)

set -euo pipefail

VAULT_ROOT=""
PERSON_SLUG=""
PERSON_NAME=""
PRIMARY_DEPT=""
TASK_TRACKER="none"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --vault-root)    VAULT_ROOT="$2"; shift 2 ;;
    --person-slug)   PERSON_SLUG="$2"; shift 2 ;;
    --person-name)   PERSON_NAME="$2"; shift 2 ;;
    --primary-dept)  PRIMARY_DEPT="$2"; shift 2 ;;
    --task-tracker)  TASK_TRACKER="$2"; shift 2 ;;
    *) echo "scaffold-person-subtree: unknown arg: $1" >&2; exit 2 ;;
  esac
done

for v in VAULT_ROOT PERSON_SLUG PERSON_NAME PRIMARY_DEPT; do
  if [[ -z "${!v}" ]]; then
    flag=$(echo "$v" | tr '[:upper:]_' '[:lower:]-')
    echo "scaffold-person-subtree: --${flag} is required" >&2
    exit 2
  fi
done

case "$TASK_TRACKER" in
  linear|monday|asana|notion|none|other) ;;
  *) echo "scaffold-person-subtree: --task-tracker must be one of: linear monday asana notion none other (got: $TASK_TRACKER)" >&2; exit 2 ;;
esac

if [[ ! -d "$VAULT_ROOT" ]]; then
  echo "scaffold-person-subtree: vault root not found: $VAULT_ROOT" >&2
  exit 3
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
TEMPLATES="$SKILL_ROOT/templates"

PERSON_ROOT="$VAULT_ROOT/people/$PERSON_SLUG"
mkdir -p \
  "$PERSON_ROOT/sources" \
  "$PERSON_ROOT/meetings" \
  "$PERSON_ROOT/private"

TODAY="$(date -u +%Y-%m-%d)"

# .config.yaml
CONFIG="$PERSON_ROOT/.config.yaml"
if [[ ! -f "$CONFIG" ]]; then
  cat > "$CONFIG" <<EOF
# Janus brain — per-person config for $PERSON_NAME ($PERSON_SLUG)
# Lives inside the shared dept vault. Read by apply-meeting-digests.py and
# the enrichment subagent. Edit freely; one key per line, simple YAML.

person_slug: $PERSON_SLUG
person_name: "$PERSON_NAME"
primary_dept: $PRIMARY_DEPT
task_tracker: $TASK_TRACKER
captured_by: $PERSON_SLUG
created: $TODAY
EOF
  echo "scaffold-person-subtree: wrote $CONFIG" >&2
else
  echo "scaffold-person-subtree: $CONFIG exists — leaving as-is" >&2
fi

# CLAUDE.md (substituted from templates/personal-claude-md.md)
PERSON_CLAUDE="$PERSON_ROOT/CLAUDE.md"
if [[ ! -f "$PERSON_CLAUDE" ]]; then
  if [[ -f "$TEMPLATES/personal-claude-md.md" ]]; then
    python3 - "$TEMPLATES/personal-claude-md.md" "$PERSON_CLAUDE" \
      "$PERSON_NAME" "$PERSON_SLUG" "$PRIMARY_DEPT" "$TASK_TRACKER" "$TODAY" <<'PY'
import sys
src, dst, person, slug, dept, tracker, today = sys.argv[1:]
text = open(src, encoding="utf-8").read()
subs = {
    "{{PERSON}}": person,
    "{{PERSON_SLUG}}": slug,
    "{{PRIMARY_DEPT}}": dept,
    "{{TASK_TRACKER}}": tracker,
    "{{DATE}}": today,
}
for k, v in subs.items():
    text = text.replace(k, v)
open(dst, "w", encoding="utf-8").write(text)
PY
    echo "scaffold-person-subtree: wrote $PERSON_CLAUDE" >&2
  else
    echo "scaffold-person-subtree: template personal-claude-md.md missing — skipping CLAUDE.md" >&2
  fi
else
  echo "scaffold-person-subtree: $PERSON_CLAUDE exists — leaving as-is" >&2
fi

# self.md
SELF_MD="$PERSON_ROOT/self.md"
if [[ ! -f "$SELF_MD" ]]; then
  if [[ -f "$TEMPLATES/personal-self-page.md" ]]; then
    python3 - "$TEMPLATES/personal-self-page.md" "$SELF_MD" \
      "$PERSON_NAME" "$PERSON_SLUG" "$PRIMARY_DEPT" "$TODAY" <<'PY'
import sys
src, dst, person, slug, dept, today = sys.argv[1:]
text = open(src, encoding="utf-8").read()
subs = {
    "{{PERSON}}": person,
    "{{PERSON_SLUG}}": slug,
    "{{PRIMARY_DEPT}}": dept,
    "{{DATE}}": today,
}
for k, v in subs.items():
    text = text.replace(k, v)
open(dst, "w", encoding="utf-8").write(text)
PY
    echo "scaffold-person-subtree: wrote $SELF_MD" >&2
  else
    echo "scaffold-person-subtree: template personal-self-page.md missing — skipping self.md" >&2
  fi
fi

# .review-queue.md
REVIEW_Q="$PERSON_ROOT/.review-queue.md"
if [[ ! -f "$REVIEW_Q" ]]; then
  cat > "$REVIEW_Q" <<EOF
# Review queue — $PERSON_NAME

Items the enrichment subagent flagged at low sensitivity confidence
(<0.7) get appended here for human review. Each entry: file path,
proposed sensitivity, confidence, one-line reason.

Once you've moved the file (or confirmed it's fine where it is), strike
the line through or delete it.

---

EOF
  echo "scaffold-person-subtree: wrote $REVIEW_Q" >&2
fi

# Ensure private/ is gitignored even if the vault's .gitignore got stripped.
# (Belt + braces — bootstrap-dept-vault.sh also drops the canonical ignore.)
GITIGNORE="$VAULT_ROOT/.gitignore"
if [[ -f "$GITIGNORE" ]]; then
  if ! grep -qxF "people/*/private/" "$GITIGNORE"; then
    {
      echo ""
      echo "# Added by scaffold-person-subtree.sh"
      echo "people/*/private/"
      echo "people/*/.review-queue.md"
    } >> "$GITIGNORE"
  fi
fi

echo "scaffold-person-subtree: ✓ $PERSON_NAME ($PERSON_SLUG) scaffolded at $PERSON_ROOT" >&2
echo "$PERSON_ROOT"

```