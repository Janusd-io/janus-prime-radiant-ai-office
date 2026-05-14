---
type: source
source_type: laptop
title: install-cron
slug: install-cron
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/install-cron.sh
original_size: 1105
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---

# install-cron

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/install-cron.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# install-cron.sh — Register the nightly sync as a user cron job.
#
# Default schedule: 0 3 * * *  (3 AM local time)
# Override with: CRON_SCHEDULE="30 2 * * *" ./install-cron.sh

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
NIGHTLY="$SCRIPT_DIR/nightly-sync.sh"
SCHEDULE="${CRON_SCHEDULE:-0 3 * * *}"
TAG="# janus-brain nightly sync"

if [[ ! -x "$NIGHTLY" ]]; then
  chmod +x "$NIGHTLY"
fi

# Remove any prior entry pointing at the same script
existing=$(crontab -l 2>/dev/null || true)
filtered=$(echo "$existing" | grep -v "janus-brain/scripts/nightly-sync.sh" || true)

new_entry="$SCHEDULE $NIGHTLY >> $HOME/.claude/skills/janus-brain/state/nightly.log 2>&1 $TAG"

# Replace crontab
{
  if [[ -n "$filtered" ]]; then
    echo "$filtered"
  fi
  echo "$new_entry"
} | crontab -

printf "\033[32m✓ Registered nightly cron: %s\033[0m\n" "$SCHEDULE"
echo "Script:  $NIGHTLY"
echo "Log:     $HOME/.claude/skills/janus-brain/state/nightly.log"
echo ""
echo "Verify with: crontab -l | grep janus-brain"
echo "Force run:   $NIGHTLY"

```