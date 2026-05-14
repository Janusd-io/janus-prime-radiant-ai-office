---
type: source
source_type: laptop
title: Janus Brain Bootstrap — lint-vault
slug: lint-vault-2
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/lint-vault.sh
original_size: 988
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# lint-vault

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/lint-vault.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# lint-vault.sh — Run scripts/lint-vault.py against the single dept vault.
#
# Single-vault model (rewrite 2026-05-14): the vault is the user's clone of
# their dept's GitHub repo at $VAULT_ROOT (default $HOME/janus/prime-radiant).
#
# Manual run:
#   ~/.claude/skills/janus-brain/scripts/lint-vault.sh
#   ~/.claude/skills/janus-brain/scripts/lint-vault.sh --strict
#   ~/.claude/skills/janus-brain/scripts/lint-vault.sh --json
#   JB_VAULT=/path/to/vault ~/.claude/skills/janus-brain/scripts/lint-vault.sh

set -uo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

: "${JB_VAULT:=$HOME/janus/prime-radiant}"

if [[ ! -d "$JB_VAULT/.git" ]]; then
  echo "lint-vault: $JB_VAULT is not a git repo." >&2
  echo "  Run /janus-brain to bootstrap your dept vault first." >&2
  exit 2
fi

export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

python3 "$SCRIPT_DIR/lint-vault.py" --vault "$JB_VAULT" "$@"

```