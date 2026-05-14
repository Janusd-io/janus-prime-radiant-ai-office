---
type: source
source_type: laptop
title: nightly-sync
slug: nightly-sync
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/nightly-sync.sh
original_size: 1593
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# nightly-sync

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/nightly-sync.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# nightly-sync.sh — Cron entrypoint. Calls the claude CLI non-interactively
# with /janus-brain sync so the skill's own logic runs against the delta.
#
# Logs everything to state/nightly.log (cron stdout/stderr also redirected
# there by install-cron.sh).

set -uo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
STATE_DIR="$SKILL_DIR/state"
LOG="$STATE_DIR/nightly.log"
LOCK="$STATE_DIR/nightly.lock"

mkdir -p "$STATE_DIR"

ts() { date "+%Y-%m-%d %H:%M:%S"; }

log() { printf "[%s] %s\n" "$(ts)" "$*" >> "$LOG"; }

# Prevent overlap if a previous run is still going
if [[ -f "$LOCK" ]]; then
  pid=$(cat "$LOCK" 2>/dev/null || echo "")
  if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
    log "skip: previous run pid=$pid still alive"
    exit 0
  fi
  rm -f "$LOCK"
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT

log "start: nightly-sync.sh pid=$$"

# Require claude CLI on PATH. Cron has a minimal PATH — augment it.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

if ! command -v claude >/dev/null 2>&1; then
  log "error: claude CLI not on PATH. install it then re-run."
  exit 1
fi

# Non-interactive invocation. The -p flag passes a prompt and exits when done.
# The skill's `sync` subcommand handles the rest (walk → enrich → render →
# graphify --update → sync-to-company --mode delta).
claude -p "/janus-brain sync" \
  --output-format text \
  >> "$LOG" 2>&1

status=$?
log "end: claude exited with status=$status"
exit $status

```