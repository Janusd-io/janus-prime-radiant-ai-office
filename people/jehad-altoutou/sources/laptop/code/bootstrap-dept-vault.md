---
type: source
source_type: laptop
title: bootstrap-dept-vault
slug: bootstrap-dept-vault
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/scripts/bootstrap-dept-vault.sh
original_size: 13178
original_ext: .sh
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: janus-brain-bootstrap

---

# bootstrap-dept-vault

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/scripts/bootstrap-dept-vault.sh` on 2026-05-14._

```bash
#!/usr/bin/env bash
# bootstrap-dept-vault.sh — Stand up a department Prime Radiant on GitHub
# and clone it as the user's SINGLE local vault.
#
# Single-vault model (rewrite 2026-05-14, supersedes the personal/dept split):
#   Every employee's Obsidian vault = one clone of their dept's shared GitHub
#   repo at $VAULT_ROOT (default $HOME/janus/prime-radiant). Per-person content
#   lives at <vault>/people/<slug>/ inside that single repo.
#
# Idempotent on three axes:
#   - remote already exists, local doesn't → clone remote into $VAULT_ROOT
#   - local already exists (with matching remote) → no-op
#   - neither exists → create from template + clone into $VAULT_ROOT
#
# Refuses (exits non-zero) when:
#   - $VAULT_ROOT/.git exists with a DIFFERENT remote URL
#   - $VAULT_ROOT sits inside iCloud / Drive / Dropbox
#
# Usage:
#   bootstrap-dept-vault.sh \
#     --dept-slug marketing \
#     --curator-slug andrew-soane \
#     --curator-name "Andrew Soane" \
#     [--org Janusd-io] \
#     [--template-repo Janusd-io/janus-prime-radiant-template] \
#     [--vault-root "$HOME/janus/prime-radiant"] \
#     [--dry-run]
#
# Outputs the absolute path of the local vault (or planned clone).

set -euo pipefail

ORG_DEFAULT="Janusd-io"
TEMPLATE_REPO_DEFAULT="Janusd-io/janus-prime-radiant-template"
VAULT_ROOT_DEFAULT="$HOME/janus/prime-radiant"

DEPT_SLUG=""
CURATOR_SLUG=""
CURATOR_NAME=""
ORG="$ORG_DEFAULT"
TEMPLATE_REPO="$TEMPLATE_REPO_DEFAULT"
VAULT_ROOT="$VAULT_ROOT_DEFAULT"
DRY_RUN="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dept-slug)     DEPT_SLUG="$2"; shift 2 ;;
    --curator-slug)  CURATOR_SLUG="$2"; shift 2 ;;
    --curator-name)  CURATOR_NAME="$2"; shift 2 ;;
    --org)           ORG="$2"; shift 2 ;;
    --template-repo) TEMPLATE_REPO="$2"; shift 2 ;;
    --vault-root)    VAULT_ROOT="$2"; shift 2 ;;
    --dry-run)       DRY_RUN="true"; shift ;;
    *) echo "bootstrap-dept-vault: unknown arg: $1" >&2; exit 2 ;;
  esac
done

for v in DEPT_SLUG CURATOR_SLUG CURATOR_NAME; do
  if [[ -z "${!v}" ]]; then
    flag=$(echo "$v" | tr '[:upper:]_' '[:lower:]-')
    echo "bootstrap-dept-vault: --${flag} is required" >&2
    exit 2
  fi
done

# Locked dept vocabulary (display names)
case "$DEPT_SLUG" in
  ai-office)     DEPT_DISPLAY="AI Office" ;;
  marketing)     DEPT_DISPLAY="Marketing" ;;
  hr)            DEPT_DISPLAY="HR" ;;
  it-ops)        DEPT_DISPLAY="IT Ops" ;;
  finance)       DEPT_DISPLAY="Finance" ;;
  office-of-ceo) DEPT_DISPLAY="Office of CEO" ;;
  engineering)   DEPT_DISPLAY="Engineering" ;;
  training)      DEPT_DISPLAY="Training" ;;
  iso)           DEPT_DISPLAY="ISO" ;;
  pm)            DEPT_DISPLAY="PM" ;;
  *)
    echo "bootstrap-dept-vault: unknown dept slug: $DEPT_SLUG" >&2
    exit 2
    ;;
esac

REPO="$ORG/janus-prime-radiant-$DEPT_SLUG"
REPO_URL="https://github.com/$REPO.git"
LOCAL="$VAULT_ROOT"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
GITIGNORE_TEMPLATE="$SKILL_ROOT/templates/dept-gitignore"

# ── Tooling preflight ────────────────────────────────────────────────────
for cmd in gh git python3; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "bootstrap-dept-vault: required tool '$cmd' not on PATH" >&2
    exit 4
  fi
done

if ! gh auth status >/dev/null 2>&1; then
  echo "bootstrap-dept-vault: gh CLI not authenticated. Run: gh auth login" >&2
  exit 4
fi

# ── Path hygiene: vault root must not be inside a sync root ─────────────
mkdir -p "$(dirname "$VAULT_ROOT")"
ABS_VAULT_ROOT="$(cd "$(dirname "$VAULT_ROOT")" 2>/dev/null && pwd)/$(basename "$VAULT_ROOT")"
case "$ABS_VAULT_ROOT" in
  *"/Library/CloudStorage/"*|*"/iCloud Drive/"*|*"/Dropbox/"*)
    echo "bootstrap-dept-vault: REFUSED — vault root sits inside another sync root:" >&2
    echo "  $ABS_VAULT_ROOT" >&2
    echo "  Git is the sync layer. Layering iCloud / Drive / Dropbox on top corrupts repos." >&2
    echo "  Move your vault root to a non-synced parent (e.g. \$HOME/janus/prime-radiant)." >&2
    exit 3
    ;;
esac

# ── Determine current state ──────────────────────────────────────────────
remote_exists="false"
local_exists="false"
local_remote_matches="false"

if gh repo view "$REPO" >/dev/null 2>&1; then
  remote_exists="true"
fi

if [[ -d "$LOCAL/.git" ]]; then
  local_exists="true"
  current_remote="$(git -C "$LOCAL" remote get-url origin 2>/dev/null || true)"
  if [[ "$current_remote" == "$REPO_URL" ]] || [[ "$current_remote" == "git@github.com:$REPO.git" ]] || [[ "$current_remote" == "$REPO_URL/" ]]; then
    local_remote_matches="true"
  fi
fi

# ── Refusal: local exists with a DIFFERENT remote ───────────────────────
if [[ "$local_exists" == "true" && "$local_remote_matches" == "false" ]]; then
  echo "bootstrap-dept-vault: REFUSED — $LOCAL is already a git repo with a different remote:" >&2
  echo "    current remote: ${current_remote:-<none>}" >&2
  echo "    expected:        $REPO_URL" >&2
  echo "  This is the single-vault layout: \$VAULT_ROOT must clone exactly one dept repo." >&2
  echo "  Pick a different --vault-root, or move/remove the existing vault first." >&2
  exit 3
fi

# ── Dry-run summary ──────────────────────────────────────────────────────
if [[ "$DRY_RUN" == "true" ]]; then
  echo "bootstrap-dept-vault: dry run for $DEPT_DISPLAY" >&2
  echo "  org:           $ORG" >&2
  echo "  repo:          $REPO  (exists: $remote_exists)" >&2
  echo "  local vault:   $LOCAL  (exists: $local_exists, remote matches: $local_remote_matches)" >&2
  echo "  curator:       $CURATOR_NAME ($CURATOR_SLUG)" >&2
  echo "  template repo: $TEMPLATE_REPO" >&2
  if [[ "$remote_exists" == "true" && "$local_exists" == "true" ]]; then
    echo "  action:        no-op (vault clone present, remote matches)" >&2
  elif [[ "$remote_exists" == "true" ]]; then
    echo "  action:        clone existing remote into \$VAULT_ROOT" >&2
  else
    echo "  action:        create remote from template + clone into \$VAULT_ROOT" >&2
  fi
  echo "$LOCAL"
  exit 0
fi

# ── Case 1: local matches the right remote → no-op (verify) ─────────────
if [[ "$local_exists" == "true" && "$local_remote_matches" == "true" ]]; then
  echo "$LOCAL"
  echo "bootstrap-dept-vault: $DEPT_DISPLAY vault already cloned at $LOCAL — no-op" >&2
  exit 0
fi

# ── Case 2: remote exists, local doesn't → clone into $VAULT_ROOT ───────
if [[ "$remote_exists" == "true" ]]; then
  echo "bootstrap-dept-vault: remote $REPO exists; cloning to $LOCAL ..." >&2
  # If $LOCAL exists as an empty dir, gh repo clone will fail — refuse rather
  # than clobber.
  if [[ -e "$LOCAL" && -n "$(ls -A "$LOCAL" 2>/dev/null || true)" ]]; then
    echo "bootstrap-dept-vault: REFUSED — $LOCAL exists and is non-empty (and not a matching git repo)." >&2
    exit 3
  fi
  rm -rf "$LOCAL" 2>/dev/null || true
  gh repo clone "$REPO" "$LOCAL"
  echo "$LOCAL"
  echo "bootstrap-dept-vault: ✓ cloned $REPO to $LOCAL" >&2
  exit 0
fi

# ── Case 3: neither exists → create + clone ──────────────────────────────
TEMPDIR=$(mktemp -d /tmp/janus-prime-radiant-template.XXXXXX)
trap 'rm -rf "$TEMPDIR"' EXIT

echo "bootstrap-dept-vault: fetching $TEMPLATE_REPO ..." >&2
if ! gh repo clone "$TEMPLATE_REPO" "$TEMPDIR/template" -- --depth=1 >/dev/null 2>&1; then
  echo "bootstrap-dept-vault: failed to clone $TEMPLATE_REPO" >&2
  echo "  Confirm gh auth has read access to the template repo." >&2
  exit 5
fi

TEMPLATE_VERSION=""
if [[ -f "$TEMPDIR/template/TEMPLATE-VERSION" ]]; then
  TEMPLATE_VERSION=$(head -1 "$TEMPDIR/template/TEMPLATE-VERSION" | tr -d ' \t')
fi

echo "bootstrap-dept-vault: creating private repo $REPO ..." >&2
if ! gh repo create "$REPO" --private --description "Janus Prime Radiant — $DEPT_DISPLAY" --disable-wiki >/dev/null 2>&1; then
  echo "bootstrap-dept-vault: 'gh repo create $REPO' failed" >&2
  echo "  You may lack 'create repo' permission on $ORG. Ask Michael / org admin." >&2
  exit 6
fi

# Refuse to clobber a non-empty $LOCAL
if [[ -e "$LOCAL" && -n "$(ls -A "$LOCAL" 2>/dev/null || true)" ]]; then
  echo "bootstrap-dept-vault: REFUSED — $LOCAL is non-empty but not a matching repo." >&2
  exit 3
fi
mkdir -p "$LOCAL"
echo "bootstrap-dept-vault: staging template into $LOCAL ..." >&2
rsync -a \
  --exclude='.git' \
  --exclude='.github' \
  --exclude='BOOTSTRAP.md' \
  --exclude='LICENSE.md' \
  --exclude='LICENSE' \
  "$TEMPDIR/template/" "$LOCAL/"

# Drop the canonical dept-gitignore at the vault root if one isn't already
# present from the template. This is the single-vault gitignore that keeps
# people/*/private/ and *.confidential.md out of GitHub.
if [[ -f "$GITIGNORE_TEMPLATE" && ! -f "$LOCAL/.gitignore" ]]; then
  cp "$GITIGNORE_TEMPLATE" "$LOCAL/.gitignore"
elif [[ -f "$GITIGNORE_TEMPLATE" && -f "$LOCAL/.gitignore" ]]; then
  # If template carries its own .gitignore, append our entries only if
  # missing (idempotent merge — never duplicate).
  while IFS= read -r line; do
    [[ -z "$line" || "$line" == "#"* ]] && continue
    grep -qxF "$line" "$LOCAL/.gitignore" || echo "$line" >> "$LOCAL/.gitignore"
  done < "$GITIGNORE_TEMPLATE"
fi

# Record template version
if [[ -n "$TEMPLATE_VERSION" ]]; then
  echo "$TEMPLATE_VERSION" > "$LOCAL/BOOTSTRAPPED-FROM-VERSION"
fi

# Auto-normalize Michael's authored content (add captured_by + audience)
python3 - "$LOCAL" <<'PY'
import sys, re
from pathlib import Path

vault = Path(sys.argv[1])
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)

TEMPLATE_AUTHORED = [
    "concepts", "lessons", "processes",
    "sources/articles",
    "entities/people", "entities/clients",
]

fixed = 0
for sub in TEMPLATE_AUTHORED:
    sub_path = vault / sub
    if not sub_path.is_dir():
        continue
    for md in sub_path.rglob("*.md"):
        if md.name == "README.md":
            continue
        text = md.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        fm_text = m.group(1)
        body = m.group(2)
        additions = []
        if not re.search(r"^\s*captured_by\s*:", fm_text, re.MULTILINE):
            additions.append("captured_by: michael-bruck")
        if not re.search(r"^\s*audience\s*:", fm_text, re.MULTILINE):
            additions.append("audience: org")
        if additions:
            new_fm = fm_text + "\n" + "\n".join(additions)
            md.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
            fixed += 1

if fixed:
    print(f"  normalized {fixed} template-authored files", file=sys.stderr)
PY

# Adapt §1 of CLAUDE.md to name the instance + append Instance metadata footer
CLAUDE_MD="$LOCAL/CLAUDE.md"
if [[ -f "$CLAUDE_MD" ]]; then
  python3 - "$CLAUDE_MD" "$DEPT_DISPLAY" "$CURATOR_NAME" "$CURATOR_SLUG" <<'PY'
import sys, re, datetime
path, dept, curator_name, curator_slug = sys.argv[1:]
text = open(path, encoding="utf-8").read()

patterns = [
    (r"(# Janus Prime Radiant — )(AI Office|<Department>|<Dept>)", fr"\1{dept}"),
    (r"(This is the )(AI Office|<Department>|<Dept>)( Prime Radiant)", fr"\1{dept}\3"),
]
for pat, repl in patterns:
    new_text, n = re.subn(pat, repl, text, count=1)
    if n:
        text = new_text
        break

stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d")
footer = f"""

---

## Instance metadata

- Instance: **{dept} Prime Radiant**
- Curator: **{curator_name}** (`{curator_slug}`)
- Bootstrapped from `Janusd-io/janus-prime-radiant-template`
- Bootstrapped on: {stamp}
- Substrate: Git (per Janus 2026-05-13 brief)
- Single-vault model (rewrite 2026-05-14): one dept repo per employee.

(Appended by bootstrap-dept-vault.sh; edit freely.)
"""
if "## Instance metadata" not in text:
    text = text.rstrip() + footer

open(path, "w", encoding="utf-8").write(text)
PY
fi

# Init git, commit, push
echo "bootstrap-dept-vault: initialising local git repo and pushing initial commit ..." >&2
cd "$LOCAL"
git init -b main >/dev/null 2>&1
git remote add origin "$REPO_URL"
git add -A
git commit -m "Initial commit from janus-prime-radiant-template${TEMPLATE_VERSION:+ ($TEMPLATE_VERSION)}" >/dev/null
git push -u origin main >/dev/null 2>&1

echo "$LOCAL"
echo "bootstrap-dept-vault: ✓ bootstrapped $DEPT_DISPLAY" >&2
echo "  repo:   https://github.com/$REPO" >&2
echo "  local:  $LOCAL" >&2
echo "  template version: ${TEMPLATE_VERSION:-unknown}" >&2
echo "  curator: $CURATOR_NAME ($CURATOR_SLUG)" >&2
echo "" >&2
echo "  Next: grant the dept's GitHub Team write access on $REPO via:" >&2
echo "    gh api -X PUT repos/$REPO/collaborators/<team-slug> -F permission=push" >&2
echo "  (or via the GitHub UI: Settings → Manage access → Add teams)" >&2

```