---
type: source
source_type: laptop
title: install
slug: install-2
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/install.sh
original_size: 24754
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# install

_Extracted from `Documents/janus-brain-bootstrap/install.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────────────
# install.sh — Install the /janus-brain skill for Claude Desktop
# Janus Digital · Personal Prime Radiant programme
#
# Usage:
#   ./install.sh                    # install / update from local repo or GitHub
#   ./install.sh --check            # verify install only (no changes)
#   ./install.sh --uninstall        # remove the skill (keeps the vaults)
#   ./install.sh --uninstall-cron   # remove any legacy Drive-era cron entries
#                                   # (sync now runs via the Obsidian Git plugin)
#   ./install.sh --install-auto-sync [--time HH:MM]
#                                   # schedule daily auto /janus-brain sync
#                                   # via launchd (default 07:30)
#   ./install.sh --uninstall-auto-sync
#                                   # remove the scheduled job
#   ./install.sh --auto-sync-status # show schedule + recent log entries
# ──────────────────────────────────────────────────────────────────────────

set -euo pipefail

SKILL_NAME="janus-brain"
SKILL_TARGET="$HOME/.claude/skills/$SKILL_NAME"
REPO_URL="https://github.com/Janusd-io/janus-brain-bootstrap"
REPO_TARBALL="https://github.com/Janusd-io/janus-brain-bootstrap/archive/refs/heads/main.tar.gz"

g(){ printf "\033[32m%s\033[0m\n" "$*"; }
y(){ printf "\033[33m%s\033[0m\n" "$*"; }
r(){ printf "\033[31m%s\033[0m\n" "$*"; }
b(){ printf "\033[1m%s\033[0m\n" "$*"; }

# ──────────────────────────────────────────────────────────────────────────
# Check mode
# ──────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--check" ]]; then
  b "Checking /janus-brain install state..."
  if [[ -d "$SKILL_TARGET" ]] && [[ -f "$SKILL_TARGET/SKILL.md" ]]; then
    file_count=$(find "$SKILL_TARGET" -type f | wc -l | tr -d ' ')
    g "✓ /janus-brain installed at $SKILL_TARGET ($file_count files)"
  else
    r "✗ /janus-brain not installed (no SKILL.md at $SKILL_TARGET)"
    exit 1
  fi
  if command -v gh &> /dev/null; then
    if gh auth status >/dev/null 2>&1; then
      g "✓ gh CLI authenticated"
    else
      y "⚠ gh CLI present but not authenticated — run: gh auth login"
    fi
  else
    r "✗ gh CLI missing — install with: brew install gh && gh auth login"
  fi
  if command -v git &> /dev/null; then
    g "✓ git available"
  else
    r "✗ git missing — install with: xcode-select --install"
  fi
  if command -v graphify &> /dev/null; then
    g "✓ graphify available"
  else
    y "⚠ graphify not on PATH — skill will install it via pipx on first run"
  fi
  # Legacy cron entries (Drive era). Detect and offer cleanup.
  if crontab -l 2>/dev/null | grep -qE "janus-brain/scripts/(refresh-from-aio|federate-to-department|sync-to-drive)\.sh"; then
    y "⚠ Legacy Drive-era cron entries detected — run: $0 --uninstall-cron"
    y "   (sync is now continuous via the Obsidian Git plugin; no cron needed)"
  else
    g "✓ no legacy cron entries"
  fi
  # Auto-sync state
  if [[ -f "$HOME/Library/LaunchAgents/com.janus.brain-sync.plist" ]]; then
    g "✓ auto-sync scheduled (see: $0 --auto-sync-status)"
  else
    y "⚠ auto-sync not scheduled (optional). Run: $0 --install-auto-sync [--time HH:MM]"
  fi
  # Single-vault layout check (rewrite 2026-05-14)
  VAULT="$HOME/janus/prime-radiant"
  if [[ -d "$VAULT/.git" ]]; then
    remote_url="$(git -C "$VAULT" remote get-url origin 2>/dev/null || echo '<unset>')"
    g "✓ vault present at $VAULT"
    g "  remote: $remote_url"
    # Per-person subtrees inside the single vault
    if compgen -G "$VAULT/people/*/.config.yaml" >/dev/null; then
      for cfg in "$VAULT"/people/*/.config.yaml; do
        slug="$(basename "$(dirname "$cfg")")"
        g "  person subtree: people/$slug/"
      done
    else
      y "  ⚠ no people/<slug>/.config.yaml found — run /janus-brain to scaffold"
    fi
    # Legacy two-vault layout detection
    if [[ -d "$HOME/janus/prime-radiant/personal/.git" ]] || [[ -d "$HOME/janus/prime-radiant/ai-office/.git" ]]; then
      y "  ⚠ legacy two-vault layout detected at \$HOME/janus/prime-radiant/{personal,ai-office}"
      y "    The 2026-05-14 rewrite collapses these into a single vault at \$HOME/janus/prime-radiant"
      y "    Migration: archive the personal repo, delete both clones, re-run /janus-brain"
    fi
  else
    y "⚠ no vault at $VAULT — run /janus-brain to bootstrap"
  fi
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────
# Uninstall mode
# ──────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--uninstall" ]]; then
  if [[ -d "$SKILL_TARGET" ]]; then
    b "Removing $SKILL_TARGET ..."
    rm -rf "$SKILL_TARGET"
    g "✓ /janus-brain removed."
  else
    y "/janus-brain not installed — nothing to remove."
  fi
  if crontab -l 2>/dev/null | grep -qE "janus-brain/scripts/" ; then
    b "Removing janus-brain cron entries ..."
    ( crontab -l 2>/dev/null | grep -vE "janus-brain/scripts/" ) | crontab -
    g "✓ Cron entries removed."
  fi
  y "Note: your Obsidian vault was NOT touched. Delete it manually if you want."
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────
# Cron-only mode
# ──────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--uninstall-cron" ]] || [[ "${1:-}" == "--install-cron" ]]; then
  if [[ "${1:-}" == "--install-cron" ]]; then
    y "⚠ --install-cron has been retired. Sync now runs continuously via the"
    y "  Obsidian Git plugin (auto-pull/push every 5 min, per vault). For daily"
    y "  ingestion of new Fireflies/Notion/laptop content, use --install-auto-sync"
    y "  which schedules a launchd job that opens Claude Desktop and triggers"
    y "  /janus-brain sync via AppleScript. Cleaning up legacy entries now."
    echo ""
  fi
  if crontab -l 2>/dev/null | grep -qE "janus-brain/scripts/(refresh-from-aio|federate-to-department|sync-to-drive)\.sh"; then
    b "Removing legacy janus-brain cron entries..."
    ( crontab -l 2>/dev/null | grep -vE "janus-brain/scripts/(refresh-from-aio|federate-to-department|sync-to-drive)\.sh" ) | crontab -
    g "✓ Legacy cron entries removed."
  else
    g "✓ No legacy janus-brain cron entries present."
  fi
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────
# Auto-sync mode (daily launchd job that opens Claude Desktop and triggers
# /janus-brain sync via AppleScript). No API keys; relies on Claude Desktop's
# MCP setup.
# ──────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--install-auto-sync" ]] || [[ "${1:-}" == "--uninstall-auto-sync" ]] || [[ "${1:-}" == "--auto-sync-status" ]]; then
  LAUNCH_AGENT_DIR="$HOME/Library/LaunchAgents"
  PLIST_NAME="com.janus.brain-sync.plist"
  PLIST_PATH="$LAUNCH_AGENT_DIR/$PLIST_NAME"
  PLIST_TEMPLATE="$SKILL_TARGET/scripts/com.janus.brain-sync.plist.template"
  AUTO_SYNC_PATH="$SKILL_TARGET/scripts/auto-sync.sh"
  LOG_DIR="$HOME/.config/janus-brain"

  if [[ "${1:-}" == "--uninstall-auto-sync" ]]; then
    if [[ -f "$PLIST_PATH" ]]; then
      launchctl bootout "gui/$UID/com.janus.brain-sync" 2>/dev/null || true
      rm -f "$PLIST_PATH"
      g "✓ auto-sync uninstalled (LaunchAgent removed)."
    else
      y "auto-sync was not installed."
    fi
    exit 0
  fi

  if [[ "${1:-}" == "--auto-sync-status" ]]; then
    b "auto-sync status:"
    if [[ -f "$PLIST_PATH" ]]; then
      g "  ✓ LaunchAgent installed at $PLIST_PATH"
      hour=$(grep -A1 "<key>Hour</key>" "$PLIST_PATH" | tail -1 | sed -E 's/.*<integer>([0-9]+)<\/integer>.*/\1/')
      minute=$(grep -A1 "<key>Minute</key>" "$PLIST_PATH" | tail -1 | sed -E 's/.*<integer>([0-9]+)<\/integer>.*/\1/')
      printf "  ✓ scheduled time: %02d:%02d daily\n" "$hour" "$minute"
      if launchctl list | grep -q "com.janus.brain-sync"; then
        g "  ✓ loaded in launchctl"
      else
        y "  ⚠ not currently loaded — run: launchctl bootstrap gui/\$UID $PLIST_PATH"
      fi
    else
      y "  not installed. Run: $0 --install-auto-sync [--time HH:MM]"
    fi
    if [[ -f "$LOG_DIR/auto-sync.log" ]]; then
      echo ""
      echo "  Last 5 log entries:"
      tail -5 "$LOG_DIR/auto-sync.log" | sed 's/^/    /'
    fi
    exit 0
  fi

  # --install-auto-sync
  HOUR="7"
  MINUTE="30"
  shift   # consume the --install-auto-sync arg
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --time)
        if [[ "$2" =~ ^([0-9]{1,2}):([0-9]{2})$ ]]; then
          HOUR="${BASH_REMATCH[1]}"
          MINUTE="${BASH_REMATCH[2]}"
        else
          r "✗ --time expects HH:MM (e.g. 07:30 or 23:00). Got: $2"
          exit 2
        fi
        shift 2
        ;;
      *) r "✗ unknown arg: $1"; exit 2 ;;
    esac
  done

  if [[ ! -f "$AUTO_SYNC_PATH" ]] || [[ ! -f "$PLIST_TEMPLATE" ]]; then
    r "✗ Skill not installed yet. Run $0 first."
    exit 1
  fi

  mkdir -p "$LAUNCH_AGENT_DIR" "$LOG_DIR"

  # Render the template into the plist
  sed \
    -e "s|{{AUTO_SYNC_PATH}}|$AUTO_SYNC_PATH|g" \
    -e "s|{{HOUR}}|$HOUR|g" \
    -e "s|{{MINUTE}}|$MINUTE|g" \
    -e "s|{{LOG_DIR}}|$LOG_DIR|g" \
    -e "s|{{USER_HOME}}|$HOME|g" \
    "$PLIST_TEMPLATE" > "$PLIST_PATH"

  # Unload any prior version first (so changes take effect)
  launchctl bootout "gui/$UID/com.janus.brain-sync" 2>/dev/null || true
  if launchctl bootstrap "gui/$UID" "$PLIST_PATH" 2>/dev/null; then
    g "✓ auto-sync installed and loaded."
  else
    y "⚠ Plist written but launchctl bootstrap failed. To activate manually:"
    echo "    launchctl bootstrap gui/$UID $PLIST_PATH"
  fi

  printf "  scheduled time: %02d:%02d daily\n" "$HOUR" "$MINUTE"
  echo "  log file: $LOG_DIR/auto-sync.log"
  echo ""
  y "⚠ FIRST-RUN PERMISSION REQUIRED"
  y "  On the first fire, macOS will prompt to allow 'System Events' to control"
  y "  Claude Desktop (for the keystroke-typing). You'll only see this prompt once."
  y "  If you want to grant permission proactively, run the script manually:"
  echo "    $AUTO_SYNC_PATH --force"
  echo ""
  echo "  Test the script anytime (without waiting for the scheduled time):"
  echo "    $AUTO_SYNC_PATH --force                      # full run"
  echo "    $AUTO_SYNC_PATH --dry-run --force            # log-only, no actions"
  echo ""
  echo "  Check status / view recent logs:"
  echo "    $0 --auto-sync-status"
  echo ""
  echo "  Uninstall:"
  echo "    $0 --uninstall-auto-sync"
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 1 — locate source
# ──────────────────────────────────────────────────────────────────────────
b "Step 1/5 — Locating skill source..."

SKILL_SOURCE=""
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [[ -d "$SCRIPT_DIR/skills/$SKILL_NAME" ]]; then
  SKILL_SOURCE="$SCRIPT_DIR/skills/$SKILL_NAME"
  g "✓ Using local repo at $SCRIPT_DIR"
elif [[ -d "$HOME/Documents/janus-brain-bootstrap/skills/$SKILL_NAME" ]]; then
  SKILL_SOURCE="$HOME/Documents/janus-brain-bootstrap/skills/$SKILL_NAME"
  g "✓ Using local clone at $HOME/Documents/janus-brain-bootstrap"
else
  y "No local repo found. Attempting download from GitHub..."
  TEMP=$(mktemp -d)
  if curl -fsSL "$REPO_TARBALL" -o "$TEMP/repo.tar.gz" 2>/dev/null; then
    tar -xzf "$TEMP/repo.tar.gz" -C "$TEMP"
    SKILL_SOURCE=$(find "$TEMP" -type d -name "$SKILL_NAME" -path "*/skills/*" | head -1)
    if [[ -z "$SKILL_SOURCE" ]]; then
      r "✗ Could not locate skill in downloaded archive"
      exit 1
    fi
    g "✓ Downloaded from GitHub to $TEMP"
  else
    r "✗ Download failed (repo is private — you need access)"
    r "  Either: 1) gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap"
    r "          2) get a zip from Jehad"
    r "          3) get added as a Janusd-io org member"
    exit 1
  fi
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 2 — preflight: python3 + git + gh + graphify
# ──────────────────────────────────────────────────────────────────────────
b "Step 2/5 — Preflight checks..."

if command -v python3 &> /dev/null; then
  g "✓ python3 present ($(python3 --version))"
else
  r "✗ python3 missing — install Python 3.10+ first"
  exit 1
fi

if command -v git &> /dev/null; then
  g "✓ git present ($(git --version))"
else
  r "✗ git missing — run: xcode-select --install"
  exit 1
fi

if command -v gh &> /dev/null; then
  g "✓ gh CLI present ($(gh --version | head -1))"
  if gh auth status >/dev/null 2>&1; then
    g "✓ gh authenticated"
  else
    y "⚠ gh present but not authenticated"
    y "  Run: gh auth login   (choose GitHub.com, HTTPS, web browser)"
  fi
else
  r "✗ gh CLI missing"
  r "  Run: brew install gh && gh auth login"
  exit 1
fi

if command -v graphify &> /dev/null; then
  g "✓ graphify present"
else
  y "graphify missing — attempting install via pipx"
  if command -v pipx &> /dev/null; then
    pipx install graphify && g "✓ graphify installed via pipx" || y "⚠ pipx install failed — skill will retry on first run"
  elif command -v brew &> /dev/null; then
    brew install pipx 2>/dev/null || true
    pipx install graphify 2>/dev/null && g "✓ graphify installed via pipx" || y "⚠ install failed — skill will retry on first run"
  else
    y "⚠ pipx not available — install graphify manually before first bootstrap"
  fi
fi

# Content extraction toolchain (Phase 4.5): pdftotext (poppler), pandoc,
# tesseract (OCR), pandas+openpyxl. Each is best-effort — extract-content.py
# falls back gracefully when any of these are missing.
b "  Content-extraction toolchain (Phase 4.5):"

install_with_brew() {
  local pkg="$1"
  local bin="${2:-$1}"
  if command -v "$bin" &> /dev/null; then
    g "  ✓ $bin present"
    return 0
  fi
  if command -v brew &> /dev/null; then
    brew install "$pkg" 2>&1 | tail -3
    if command -v "$bin" &> /dev/null; then
      g "  ✓ $bin installed via brew"
    else
      y "  ⚠ $bin install failed — extract-content.py will skip $bin-dependent files"
    fi
  else
    y "  ⚠ Homebrew not present; install $pkg manually for full extraction"
  fi
}

install_with_brew poppler pdftotext
install_with_brew pandoc pandoc
install_with_brew tesseract tesseract

# pandas + openpyxl for xlsx/xls extraction (CSV/TSV use stdlib)
if python3 -c "import pandas" 2>/dev/null; then
  g "  ✓ pandas present"
else
  y "  pandas missing — attempting: pip3 install --user pandas openpyxl"
  pip3 install --user pandas openpyxl 2>&1 | tail -2
  if python3 -c "import pandas" 2>/dev/null; then
    g "  ✓ pandas installed"
  else
    y "  ⚠ pandas install failed — extract-content.py will skip xlsx/xls files (CSV/TSV still work)"
  fi
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 3 — install / update skill
# ──────────────────────────────────────────────────────────────────────────
b "Step 3/5 — Installing skill..."

mkdir -p "$HOME/.claude/skills"

if [[ -d "$SKILL_TARGET" ]]; then
  y "Existing /janus-brain found — backing up to ${SKILL_TARGET}.bak"
  rm -rf "${SKILL_TARGET}.bak"
  mv "$SKILL_TARGET" "${SKILL_TARGET}.bak"
fi

cp -r "$SKILL_SOURCE" "$SKILL_TARGET"
chmod +x "$SKILL_TARGET"/scripts/*.sh 2>/dev/null || true
chmod +x "$SKILL_TARGET"/scripts/*.py 2>/dev/null || true
file_count=$(find "$SKILL_TARGET" -type f | wc -l | tr -d ' ')
g "✓ Installed $file_count files to $SKILL_TARGET"

# ──────────────────────────────────────────────────────────────────────────
# Step 4 — verify
# ──────────────────────────────────────────────────────────────────────────
b "Step 4/5 — Verifying install..."

required=(
  "SKILL.md"
  "README.md"
  "INSTALL.md"
  "config/exclude-patterns.txt"
  "config/exclude-paths.txt"
  "config/include-extensions.txt"
  "config/departments.yaml"
  "scripts/discover.sh"
  "scripts/walk-and-filter.py"
  "scripts/ingest-to-radiant.py"
  "scripts/fetch-fireflies.py"
  "scripts/apply-meeting-digests.py"
  "scripts/extract-content.py"
  "scripts/extract-content.sh"
  "scripts/auto-sync.sh"
  "scripts/com.janus.brain-sync.plist.template"
  "scripts/bootstrap-dept-vault.sh"
  "scripts/scaffold-person-subtree.sh"
  "scripts/lint-vault.py"
  "scripts/lint-vault.sh"
  "scripts/nightly-sync.sh"
  "scripts/install-cron.sh"
  "templates/personal-claude-md.md"
  "templates/personal-self-page.md"
  "templates/entity-internal.md"
  "templates/entity-vendor.md"
  "templates/decision.md"
  "templates/lesson.md"
  "templates/pulse.md"
  "templates/meeting-source.md"
  "templates/dept-gitignore"
  "references/privacy-filter.md"
  "references/prime-radiant-personal.md"
  "prompts/enrichment-subagent.md"
  "prompts/meeting-parser-subagent.md"
  "briefs/personal-prime-radiant-proposal.md"
)

missing=0
for f in "${required[@]}"; do
  if [[ ! -f "$SKILL_TARGET/$f" ]]; then
    r "✗ Missing: $f"
    missing=$((missing+1))
  fi
done

if [[ $missing -eq 0 ]]; then
  g "✓ All required files present"
else
  r "✗ $missing files missing — install incomplete"
  exit 1
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 5 — Drop a Start-Here on the Desktop
# ──────────────────────────────────────────────────────────────────────────
b "Step 5/5 — Dropping Start-Here on Desktop..."

START_HERE="$HOME/Desktop/Janus Brain - Start Here.md"
if [[ ! -f "$START_HERE" ]]; then
  cat > "$START_HERE" <<'EOF'
# Janus Brain — Start Here

The `/janus-brain` skill is now installed in your Claude Desktop (Code / Cowork tab).

## What it does

Creates your private GitHub-backed Personal Prime Radiant repo at
`Janusd-io/janus-prime-radiant-personal-<your-slug>` (cloned locally to
`~/janus/prime-radiant/personal/`), scaffolds the canonical folder layout,
pulls your Notion + Fireflies meetings via Claude Desktop's MCP connectors,
walks your laptop documents, and runs parallel Claude subagents to extract
decisions, action items, and structured pulse pages.

It then clones (or creates from template) your department's vault repo at
`Janusd-io/janus-prime-radiant-<your-dept>` and the AIO vault, runs the
first federation push (items tagged `audience: department` go into the
dept clone's inbox/), and tells you how to enable the Obsidian Git plugin
for transparent ongoing sync.

## How to use it

1. Open Claude Desktop → **Code tab** (or **Cowork** if you have it)
2. Make sure Fireflies + Notion connectors are signed in (Settings → Connectors)
3. Make sure `gh auth status` shows you're signed in to GitHub
4. Type `/janus-brain` — autopilots through 8 phases
5. After it finishes, open Obsidian and enable the Git plugin in each vault

## Subcommands

- `/janus-brain sync` — pull yesterday's Notion + Fireflies, re-enrich, re-federate
- `/janus-brain status` — health check (clone status, lint count, federation queue)
- `/janus-brain federate` — re-run department federation only
- `/janus-brain lint` — run schema + integrity check across the vault
- `/janus-brain reset` — wipe local state metadata (keeps the vault repo)

## Substrate (per 2026-05-13 brief)

Prime Radiant lives on Git, not Drive. Each vault is a private GitHub repo
under the Janusd-io org. Sync runs continuously via the Obsidian Git
community plugin (auto-pull/push every 5 min while Obsidian is open).
**No cron jobs.**

## Verify, update, uninstall

| What | Command |
| --- | --- |
| Verify install | `~/Documents/janus-brain-bootstrap/install.sh --check` |
| Clean legacy crons | `~/Documents/janus-brain-bootstrap/install.sh --uninstall-cron` |
| Update to latest | `cd ~/Documents/janus-brain-bootstrap && git pull && ./install.sh` |
| Uninstall | `~/Documents/janus-brain-bootstrap/install.sh --uninstall` |

## Owner / contact

Jehad — AI Operations Engineer · jehada@janusd.io
EOF
  g "✓ Dropped 'Janus Brain - Start Here.md' on your Desktop"
else
  y "→ 'Janus Brain - Start Here.md' already on Desktop (not overwritten)"
fi

# ──────────────────────────────────────────────────────────────────────────
# Done
# ──────────────────────────────────────────────────────────────────────────
echo ""
b "──────────────────────────────────────────────────────────────────────────"
g "✓ /janus-brain skill installed successfully"
b "──────────────────────────────────────────────────────────────────────────"
echo ""
echo "Next steps:"
echo "  1. Restart Claude Desktop"
echo "  2. Make sure gh is authenticated: gh auth status   (gh auth login if not)"
echo "  3. Make sure Fireflies + Notion connectors are signed in"
echo "     (Claude Desktop → Settings → Connectors)"
echo "  4. In Claude Desktop → Code (or Cowork) tab → New chat → type /janus-brain"
echo "     The skill autopilots through everything."
echo ""
echo "Sync runs continuously via the Obsidian Git plugin (auto-pull/push every"
echo "5 min while Obsidian is open). No cron required."
echo ""
echo "Verify anytime with:  $0 --check"
echo "Uninstall with:       $0 --uninstall"
echo ""

```