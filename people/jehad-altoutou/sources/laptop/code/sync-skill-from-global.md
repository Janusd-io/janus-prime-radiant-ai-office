---
type: source
source_type: laptop
title: sync-skill-from-global
slug: sync-skill-from-global
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-puls-onboarding/scripts/sync-skill-from-global.sh
original_size: 1623
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# sync-skill-from-global

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/scripts/sync-skill-from-global.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# Sync the locally-edited /ims-enrolment skill from ~/.claude/skills/
# into this repo (so the repo stays canonical for distribution).
#
# Run this AFTER editing files in ~/.claude/skills/ims-enrolment/
# but BEFORE running ./install.sh or committing.

set -euo pipefail

REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." &> /dev/null && pwd )"
GLOBAL_SKILL="$HOME/.claude/skills/ims-enrolment"
REPO_SKILL="$REPO_DIR/skills/ims-enrolment"

g(){ printf "\033[32m%s\033[0m\n" "$*"; }
y(){ printf "\033[33m%s\033[0m\n" "$*"; }
r(){ printf "\033[31m%s\033[0m\n" "$*"; }
b(){ printf "\033[1m%s\033[0m\n" "$*"; }

if [[ ! -d "$GLOBAL_SKILL" ]]; then
  r "✗ Global skill not found at $GLOBAL_SKILL"
  r "  Nothing to sync. Install first: $REPO_DIR/install.sh"
  exit 1
fi

if [[ ! -d "$REPO_SKILL" ]]; then
  mkdir -p "$REPO_SKILL"
fi

b "Syncing $GLOBAL_SKILL → $REPO_SKILL"
rsync -a --delete "$GLOBAL_SKILL/" "$REPO_SKILL/"

# Show diff against last commit
cd "$REPO_DIR"
if git diff --quiet HEAD -- skills/ims-enrolment/; then
  y "No changes vs last commit. Skill is already up to date in the repo."
else
  g "✓ Synced. Changes detected:"
  git diff --stat HEAD -- skills/ims-enrolment/
  echo ""
  b "Next steps:"
  echo "  1. Review the diff: git diff HEAD -- skills/ims-enrolment/"
  echo "  2. Commit:          git add skills/ && git commit -m '...'"
  echo "  3. Push:            git push"
  echo ""
  echo "DO NOT run ./install.sh until you've committed — the installer copies repo→global,"
  echo "so re-running it before sync would overwrite your edits with the OLD repo content."
fi

```