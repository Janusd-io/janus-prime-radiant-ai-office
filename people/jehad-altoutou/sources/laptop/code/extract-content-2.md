---
type: source
source_type: laptop
title: extract-content
slug: extract-content-2
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/extract-content.sh
original_size: 2233
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---

# extract-content

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/extract-content.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# extract-content.sh — Wrapper for extract-content.py.
# Single-vault model (rewrite 2026-05-14): vault = $HOME/janus/prime-radiant
# by default. Set JB_VAULT to override. JB_PERSON_SLUG identifies whose
# subtree (people/<slug>/) is the target for laptop sources.
#
# Manual run:
#   ~/.claude/skills/janus-brain/scripts/extract-content.sh
#   ~/.claude/skills/janus-brain/scripts/extract-content.sh --only-categories pdfs,docs
#   ~/.claude/skills/janus-brain/scripts/extract-content.sh --limit 10   # testing

set -uo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

: "${JB_VAULT:=$HOME/janus/prime-radiant}"

if [[ ! -d "$JB_VAULT/.git" ]]; then
  echo "extract-content: vault not found (or not a git repo) at $JB_VAULT" >&2
  echo "  Run /janus-brain to bootstrap your dept vault first." >&2
  exit 2
fi

if [[ -z "${JB_PERSON_SLUG:-}" ]]; then
  # Best-effort: pick the only people/<slug>/ subdir, if exactly one exists.
  candidates=()
  for d in "$JB_VAULT"/people/*/; do
    [[ -d "$d" && -f "$d/.config.yaml" ]] || continue
    candidates+=("$(basename "$d")")
  done
  if [[ ${#candidates[@]} -eq 1 ]]; then
    JB_PERSON_SLUG="${candidates[0]}"
  else
    echo "extract-content: set JB_PERSON_SLUG (found ${#candidates[@]} candidate people/<slug>/ subtrees)" >&2
    exit 2
  fi
fi

MANIFEST="$JB_VAULT/.state/manifest.json"
if [[ ! -f "$MANIFEST" ]]; then
  echo "extract-content: no manifest at $MANIFEST" >&2
  echo "  Run walk-and-filter.py first (handled by /janus-brain Phase 4)." >&2
  exit 2
fi

LOG="$JB_VAULT/.state/extract-content.log"
mkdir -p "$(dirname "$LOG")"

ts() { date "+%Y-%m-%d %H:%M:%S"; }
log() { printf "[%s] %s\n" "$(ts)" "$*" >> "$LOG"; }

log "start: extract-content"
log "  manifest:    $MANIFEST"
log "  vault:       $JB_VAULT"
log "  captured_by: $JB_PERSON_SLUG"

export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

out=$(python3 "$SCRIPT_DIR/extract-content.py" \
  --manifest "$MANIFEST" \
  --vault "$JB_VAULT" \
  --captured-by "$JB_PERSON_SLUG" \
  "$@" 2>&1)
status=$?

log "$out"
echo "$out"

if [[ $status -eq 0 ]]; then
  log "end: ok"
else
  log "end: status=$status"
fi

exit $status

```