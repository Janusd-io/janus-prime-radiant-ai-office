---
type: source
source_type: laptop
title: auto-sync
slug: auto-sync
created: 2026-05-13
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/auto-sync.sh
original_size: 5756
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# auto-sync

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/auto-sync.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# auto-sync.sh — Daily auto-trigger for /janus-brain sync.
#
# Fires from launchd at a user-chosen time. Launches Claude Desktop and
# uses AppleScript (System Events) to open a new chat and type "/janus-brain
# sync" — which then autopilots through Phases 3 → 7. No API keys, no REST
# calls, no MCP duplication — relies entirely on the user's existing
# Claude Desktop MCP connections.
#
# Manual invocation:
#   ~/.claude/skills/janus-brain/scripts/auto-sync.sh
#   ~/.claude/skills/janus-brain/scripts/auto-sync.sh --dry-run
#   ~/.claude/skills/janus-brain/scripts/auto-sync.sh --force   # skip idle check
#
# Prereqs (one-time):
#   - Claude Desktop installed at /Applications/Claude.app
#   - Accessibility permission granted to "System Events" so it can send
#     keystrokes to Claude (macOS prompts on first run; user clicks Allow)
#   - User's default Claude Desktop landing tab is Code or Cowork (NOT Chat)
#     since /janus-brain only loads in Code/Cowork

set -uo pipefail

# ── Tunables ─────────────────────────────────────────────────────────────
IDLE_THRESHOLD_SECONDS=${IDLE_THRESHOLD_SECONDS:-3600}   # 1 hour idle = OK to interrupt
LAUNCH_WAIT_SECONDS=${LAUNCH_WAIT_SECONDS:-4}            # time for Claude to be ready after open
NEW_CHAT_WAIT_SECONDS=${NEW_CHAT_WAIT_SECONDS:-1}        # time after Cmd+N for input to be focused

LOG_DIR="$HOME/.config/janus-brain"
LOG="$LOG_DIR/auto-sync.log"
mkdir -p "$LOG_DIR"

ts() { date "+%Y-%m-%d %H:%M:%S"; }
log() { printf "[%s] %s\n" "$(ts)" "$*" >> "$LOG"; }

# ── Args ─────────────────────────────────────────────────────────────────
DRY_RUN="false"
FORCE="false"
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN="true" ;;
    --force)   FORCE="true" ;;
    *) echo "auto-sync: unknown arg: $arg" >&2; exit 2 ;;
  esac
done

log "start: auto-sync (dry-run=$DRY_RUN, force=$FORCE)"

# ── Preflight ────────────────────────────────────────────────────────────
if [[ ! -d "/Applications/Claude.app" ]]; then
  log "ERROR: Claude Desktop not found at /Applications/Claude.app"
  echo "auto-sync: Claude Desktop is not installed. Install from https://claude.ai/download" >&2
  exit 2
fi

# ── Idle check (skip if user is actively using the computer) ─────────────
if [[ "$FORCE" != "true" ]]; then
  idle_ns=$(ioreg -c IOHIDSystem 2>/dev/null | awk '/HIDIdleTime/ {print $NF; exit}' || echo 0)
  idle_seconds=$(( idle_ns / 1000000000 ))
  if [[ $idle_seconds -lt $IDLE_THRESHOLD_SECONDS ]]; then
    log "skip: user active (idle ${idle_seconds}s < threshold ${IDLE_THRESHOLD_SECONDS}s)"
    echo "auto-sync: user is active (idle ${idle_seconds}s < ${IDLE_THRESHOLD_SECONDS}s threshold)." >&2
    echo "  Run manually with --force to override, or run /janus-brain sync yourself." >&2
    exit 0
  fi
  log "  idle check passed: ${idle_seconds}s since last input"
fi

# ── Dry run? bail before touching Claude ─────────────────────────────────
if [[ "$DRY_RUN" == "true" ]]; then
  log "dry-run: would launch Claude + send /janus-brain sync"
  echo "auto-sync: dry run. Would launch Claude Desktop and type '/janus-brain sync'."
  exit 0
fi

# ── Launch Claude Desktop ────────────────────────────────────────────────
log "  launching Claude Desktop"
open -a "Claude" 2>>"$LOG"
sleep "$LAUNCH_WAIT_SECONDS"

# ── Drive Claude via AppleScript ─────────────────────────────────────────
# Strategy:
#   1. Activate Claude (bring to foreground; will steal focus)
#   2. Cmd+N to open a new chat (standard macOS shortcut; Claude Desktop honors it)
#   3. Wait briefly for the input field to be focused
#   4. Type "/janus-brain sync"
#   5. Press Return to submit
#
# Fragility notes:
#   - Cmd+N might not open a new chat in older Claude Desktop versions; in that
#     case the keystroke lands in whatever chat is currently open (which is
#     still acceptable behavior)
#   - If Claude Desktop's default tab is Chat (not Code), the /janus-brain skill
#     won't be available; user should set Code or Cowork as their default.
#   - If Accessibility permission has not been granted, AppleScript silently
#     fails. Check macOS System Settings → Privacy & Security → Accessibility.

log "  driving Claude via AppleScript"
osascript <<'APPLESCRIPT' 2>>"$LOG"
tell application "Claude" to activate
delay 1
tell application "System Events"
    tell process "Claude"
        -- New chat
        keystroke "n" using {command down}
        delay 1
        -- Type the slash command
        keystroke "/janus-brain sync"
        delay 0.5
        keystroke return
    end tell
end tell
APPLESCRIPT
status=$?

if [[ $status -eq 0 ]]; then
  log "end: ok (Claude triggered; skill autopilots from here)"
else
  log "end: AppleScript exited $status"
  echo "auto-sync: AppleScript failed with status $status." >&2
  echo "  Most likely cause: macOS hasn't granted Accessibility permission yet." >&2
  echo "  Open System Settings → Privacy & Security → Accessibility and enable" >&2
  echo "  the parent process (Terminal / launchd / whatever invoked this script)." >&2
fi

exit $status

```