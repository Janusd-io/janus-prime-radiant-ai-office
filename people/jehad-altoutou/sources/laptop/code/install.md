---
type: source
source_type: laptop
title: Janus Puls Onboarding — install
slug: install
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-puls-onboarding/install.sh
original_size: 13211
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# install

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/install.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────────────
# install.sh — Install the /ims-enrolment skill for Claude Desktop
# Janus Digital · IMS / PULS programme
#
# Usage:
#   ./install.sh                    # install / update from local repo or GitHub
#   ./install.sh --check            # verify install only (no changes)
#   ./install.sh --uninstall        # remove the skill (does NOT touch pandoc)
# ──────────────────────────────────────────────────────────────────────────

set -euo pipefail

SKILL_NAME="ims-enrolment"
SKILL_TARGET="$HOME/.claude/skills/$SKILL_NAME"
BACKUP_DIR="$HOME/.claude/.skill-backups"
REPO_URL="https://github.com/Jehada-Janusd/janus-puls-onboarding"
REPO_TARBALL="https://github.com/Jehada-Janusd/janus-puls-onboarding/archive/refs/heads/main.tar.gz"

# Pretty output
g(){ printf "\033[32m%s\033[0m\n" "$*"; }
y(){ printf "\033[33m%s\033[0m\n" "$*"; }
r(){ printf "\033[31m%s\033[0m\n" "$*"; }
b(){ printf "\033[1m%s\033[0m\n" "$*"; }

# ──────────────────────────────────────────────────────────────────────────
# Check mode
# ──────────────────────────────────────────────────────────────────────────
if [[ "${1:-}" == "--check" ]]; then
  b "Checking /ims-enrolment install state..."
  if [[ -d "$SKILL_TARGET" ]] && [[ -f "$SKILL_TARGET/SKILL.md" ]]; then
    file_count=$(find "$SKILL_TARGET" -type f | wc -l | tr -d ' ')
    g "✓ Skill installed at $SKILL_TARGET ($file_count files)"
  else
    r "✗ Skill not installed (no SKILL.md at $SKILL_TARGET)"
    exit 1
  fi
  if command -v pandoc &> /dev/null; then
    g "✓ pandoc available ($(pandoc --version | head -1))"
  else
    y "⚠ pandoc not installed (Phase 5b Word doc export will fail)"
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
    g "✓ Uninstalled. pandoc was not touched."
  else
    y "Nothing to remove — skill not installed."
  fi
  exit 0
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 1 — verify or install pandoc
# ──────────────────────────────────────────────────────────────────────────
b "Step 1/4 — Checking pandoc..."
if command -v pandoc &> /dev/null; then
  g "✓ pandoc already installed"
else
  y "pandoc not found. Attempting install..."
  if command -v brew &> /dev/null; then
    brew install pandoc
    g "✓ pandoc installed via Homebrew"
  elif command -v apt-get &> /dev/null; then
    sudo apt-get update && sudo apt-get install -y pandoc
    g "✓ pandoc installed via apt"
  else
    r "Could not auto-install pandoc."
    r "Install manually: https://pandoc.org/installing.html"
    r "Phase 5b (Word doc export) will fail without it."
    y "Continuing without pandoc..."
  fi
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 2 — find skill source
# ──────────────────────────────────────────────────────────────────────────
b "Step 2/4 — Locating skill source..."

SKILL_SOURCE=""
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Try: run from inside the repo
if [[ -d "$SCRIPT_DIR/skills/$SKILL_NAME" ]]; then
  SKILL_SOURCE="$SCRIPT_DIR/skills/$SKILL_NAME"
  g "✓ Using local repo at $SCRIPT_DIR"

# Try: standard Documents clone
elif [[ -d "$HOME/Documents/janus-puls-onboarding/skills/$SKILL_NAME" ]]; then
  SKILL_SOURCE="$HOME/Documents/janus-puls-onboarding/skills/$SKILL_NAME"
  g "✓ Using local clone at $HOME/Documents/janus-puls-onboarding"

# Fallback: download tarball (requires repo access — private repo will fail here)
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
    r "  Either: 1) clone the repo to ~/Documents/janus-puls-onboarding"
    r "          2) get a zip from Jehad and extract it"
    r "          3) get added as a collaborator on $REPO_URL"
    exit 1
  fi
fi

# ──────────────────────────────────────────────────────────────────────────
# Step 3 — install / update
# ──────────────────────────────────────────────────────────────────────────
b "Step 3/4 — Installing skill..."

mkdir -p "$HOME/.claude/skills"
mkdir -p "$BACKUP_DIR"

if [[ -d "$SKILL_TARGET" ]]; then
  TIMESTAMP=$(date +%Y%m%d-%H%M%S)
  BACKUP_PATH="$BACKUP_DIR/${SKILL_NAME}-${TIMESTAMP}"
  y "Existing install found — backing up to $BACKUP_PATH"
  mv "$SKILL_TARGET" "$BACKUP_PATH"
  # Keep only the 3 most recent backups
  ls -dt "$BACKUP_DIR/${SKILL_NAME}-"* 2>/dev/null | tail -n +4 | xargs -r rm -rf
fi

cp -r "$SKILL_SOURCE" "$SKILL_TARGET"
file_count=$(find "$SKILL_TARGET" -type f | wc -l | tr -d ' ')
g "✓ Installed $file_count files to $SKILL_TARGET"

# ──────────────────────────────────────────────────────────────────────────
# Step 4 — verify
# ──────────────────────────────────────────────────────────────────────────
b "Step 4/4 — Verifying install..."

required=(
  "SKILL.md"
  "INSTALL.md"
  "references/iso-9001-figure-1.md"
  "references/seven-section-template.md"
  "references/plain-english-overview.md"
  "references/jargon-decoder.md"
  "references/simon-ims-prc-ai-001-v0.4.md"
  "templates/parent-department-process.md"
  "templates/sub-process.md"
  "templates/first-voice-questionnaire.md"
  "templates/diagram-prompt.md"
  "templates/handover-to-simon.md"
  "prompts/interview-department-head.md"
  "prompts/interview-activity-owner.md"
  "prompts/interview-first-voice.md"
  "examples/ai-department/parent-process.md"
  "examples/ai-department/sub-process-meeting-to-task.md"
  "examples/ai-department/sub-process-tool-evaluation.md"
  "examples/ai-department/sub-process-platform-development.md"
  "examples/ai-department/diagram-prompt-parent-process.md"
  "examples/ai-department/diagram-prompt-meeting-to-task.md"
  "examples/ai-department/diagram-prompt-tool-evaluation.md"
  "examples/ai-department/diagram-prompt-platform-development.md"
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
# Step 5 — Drop a "Start Here" file on the Desktop
# ──────────────────────────────────────────────────────────────────────────
START_HERE="$HOME/Desktop/IMS Enrolment - Start Here.md"
if [[ ! -f "$START_HERE" ]]; then
  cat > "$START_HERE" <<'EOF'
# IMS Enrolment — Start Here

The `/ims-enrolment` skill is now installed in your Claude Desktop.

## How to use it

1. Open Claude Desktop
2. Type one of these trigger phrases:
   - `/ims-enrolment`
   - *"Enrol [my department] into the IMS"*
   - *"Help [my team] document our processes for ISO"*
3. Claude walks you through a guided interview (Phases 1-5)

## What you'll end up with

A folder on your Desktop called **`<Your Department> - IMS Enrolment`** containing:

- Process documents (parent + sub-processes) in the ISO 9001 Figure 1 shape
- ChatGPT prompts you can paste to generate polished diagrams
- First Voice questionnaire for each person in your department
- A `HANDOVER-BUNDLE.docx` ready to send to Simon (ISO Lead)
- All Word doc exports for sharing outside Claude

## What you need

- **Claude Desktop** (already installed, you're reading this)
- **pandoc** (for Word doc export — install via `brew install pandoc` on Mac if missing)
- **30-60 min per department head interview** (Phase 2), **20-30 min per sub-process** (Phase 3)
- **A folder of patience** — the first run feels long because the skill is teaching you the structure. The second department goes 3× faster.

## Help, verify, update

| What | Command |
|---|---|
| Verify the skill is installed | `~/Documents/janus-puls-onboarding/install.sh --check` |
| Update to latest version | `cd ~/Documents/janus-puls-onboarding && git pull && ./install.sh` |
| Uninstall the skill | `~/Documents/janus-puls-onboarding/install.sh --uninstall` |
| Read the full install docs | `~/.claude/skills/ims-enrolment/INSTALL.md` |

## Worked example

If you get stuck during the interview, the skill ships with the **AI Department fully documented** as a reference:

`~/.claude/skills/ims-enrolment/examples/ai-department/`

That's a complete enrolment showing what every section should look like.

## Owner / contact

Jehad — AI Operations Engineer · jehada@janusd.io

---

*This file is dropped here once by `install.sh`. Feel free to delete it after reading — the skill itself doesn't need it. Re-running the installer won't overwrite it.*
EOF
  g "✓ Dropped 'IMS Enrolment - Start Here.md' on your Desktop"
else
  y "→ 'IMS Enrolment - Start Here.md' already on Desktop (not overwritten)"
fi

# ──────────────────────────────────────────────────────────────────────────
# Done
# ──────────────────────────────────────────────────────────────────────────
echo ""
b "──────────────────────────────────────────────────────────────────────────"
g "✓ /ims-enrolment skill installed successfully (v1.4)"
b "──────────────────────────────────────────────────────────────────────────"
echo ""
echo "Next steps:"
echo "  1. Restart Claude Desktop"
echo "  2. Type /ims-enrolment to invoke the skill"
echo "  3. Or use a trigger phrase like 'enrol [department] into the IMS'"
echo ""
echo "Outputs from the skill land on your Desktop:"
echo "  ~/Desktop/<Department> - IMS Enrolment/"
echo ""
echo "Verify anytime with:  $0 --check"
echo "Uninstall with:       $0 --uninstall"
echo ""

```