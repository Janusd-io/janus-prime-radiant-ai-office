---
type: process
title: Prime Radiant — instance setup (curator side)
slug: prime-radiant-instance-setup
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
related: [janus-prime-radiant-build, prime-radiant-storage-substrate, marketing-prime-radiant, peer-to-peer-mesh-federation-pattern]
---

# Prime Radiant — instance setup (curator side)

How to stand up a new Janus Prime Radiant instance end-to-end: GitHub repo, local vault, initial commit, curator's local tooling. One run per new department. Companion to a forthcoming `prime-radiant-member-setup.md` (per-joining-member runbook, to be extracted from [[prime-radiant-storage-substrate]] Appendix A after Jehad's first run).

This page captures the empirical sequence Michael ran on 2026-05-13 to migrate the AIO instance off Google Drive to Git, distilled for reuse with the Marketing instance and every department instance that follows. The reasoning behind the substrate choice lives in [[prime-radiant-storage-substrate]]; this page is the operational handoff.

## When to use

- **Migration case:** moving an existing Drive-hosted vault to Git (AIO, 2026-05-13).
- **Fresh case:** standing up a brand-new vault for a new department (Marketing, queued; HR/Finance/IT-Ops/ISO/Office-of-CEO/Engineering/Training to follow).

The two cases differ only in step 4 below — migration copies an existing tree; fresh setup clones from the [[janus-prime-radiant-build|janus-prime-radiant-template]] repo. Everything else is identical.

## Prerequisites on the curator's Mac

- `gh` CLI installed and authenticated: `brew install gh && gh auth login`
- Obsidian installed
- Cowork installed
- Admin or write access to the `Janusd-io` GitHub Organization
- Local path `~/janus/prime-radiant/<instance-slug>/` does not yet exist (script will fail safe if it does)

## Inputs

- `INSTANCE_SLUG` — kebab-case department slug. Must match the corresponding `entities/departments/<slug>.md` slug. Examples: `ai-office`, `marketing`, `hr`, `finance`, `it-ops`, `office-of-ceo`, `engineering`, `training`, `iso`.
- `SOURCE_PATH` — optional. Absolute path to an existing Drive-hosted vault folder. Pass for migration; omit for fresh setup.

## The script

Saves about an hour of typing per instance and prevents the kind of slips that cost a debugging session. Handles every step that can be done safely without GUI interaction: GitHub repo creation, Drive-to-local file move (with stream-on-demand materialization), git init, initial commit, push, and a sanity-check summary at the end.

Copy this to `~/janus/scripts/prime-radiant-instance-setup.sh`, `chmod +x` it, then run.

```bash
#!/usr/bin/env bash
# Prime Radiant — instance setup (curator side)
# Documented at: processes/prime-radiant-instance-setup.md

set -euo pipefail

# ---------- inputs ----------
INSTANCE_SLUG="${1:?usage: $0 <instance-slug> [source-path]}"
SOURCE_PATH="${2:-}"
ORG="Janusd-io"
TEMPLATE_REPO="${ORG}/janus-prime-radiant-template"
REPO_NAME="janus-prime-radiant-${INSTANCE_SLUG}"
LOCAL_PATH="${HOME}/janus/prime-radiant/${INSTANCE_SLUG}"

echo "▸ Instance:    ${INSTANCE_SLUG}"
echo "▸ Repo:        ${ORG}/${REPO_NAME}"
echo "▸ Local path:  ${LOCAL_PATH}"
if [ -n "${SOURCE_PATH}" ]; then
    echo "▸ Source:      ${SOURCE_PATH} (migration mode)"
else
    echo "▸ Source:      template (fresh mode)"
fi
echo ""

# ---------- prerequisites ----------
echo "▸ Checking prerequisites..."
command -v gh >/dev/null 2>&1 \
    || { echo "✗ gh CLI not found. Install: brew install gh"; exit 1; }
gh auth status >/dev/null 2>&1 \
    || { echo "✗ gh not authenticated. Run: gh auth login"; exit 1; }
[ ! -e "${LOCAL_PATH}" ] \
    || { echo "✗ Target path already exists: ${LOCAL_PATH}"; exit 1; }
if [ -n "${SOURCE_PATH}" ]; then
    [ -d "${SOURCE_PATH}" ] \
        || { echo "✗ Source path not a directory: ${SOURCE_PATH}"; exit 1; }
fi
echo "  ok."

# ---------- create the GitHub repo (empty, no auto-init) ----------
echo "▸ Creating ${ORG}/${REPO_NAME}..."
gh repo create "${ORG}/${REPO_NAME}" \
    --private \
    --description "Janus Prime Radiant instance for ${INSTANCE_SLUG}" \
    --disable-wiki >/dev/null
echo "  created."

# ---------- prepare the local vault ----------
mkdir -p "$(dirname "${LOCAL_PATH}")"

if [ -n "${SOURCE_PATH}" ]; then
    echo "▸ Materializing Drive files (in case of stream-on-demand placeholders)..."
    # Force-read every file so Drive for Desktop materializes bytes locally
    # before we copy. Suppresses errors on unreadable files (rare).
    find "${SOURCE_PATH}" -type f -exec cat {} > /dev/null \; 2>/dev/null || true
    echo "  done."

    echo "▸ Copying ${SOURCE_PATH} → ${LOCAL_PATH}..."
    cp -R "${SOURCE_PATH}" "${LOCAL_PATH}"
    echo "  copied."
else
    echo "▸ Cloning from template repo ${TEMPLATE_REPO}..."
    gh repo clone "${TEMPLATE_REPO}" "${LOCAL_PATH}" >/dev/null
    # Drop the template's git history; we start a fresh history for the new instance
    rm -rf "${LOCAL_PATH}/.git"
    echo "  cloned (template history discarded)."
fi

cd "${LOCAL_PATH}"

# ---------- .gitignore ----------
if [ ! -f .gitignore ]; then
    echo "▸ Writing .gitignore..."
    cat > .gitignore <<'EOF'
.DS_Store
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
EOF
    echo "  done."
else
    echo "▸ .gitignore already present, leaving as-is."
fi

# ---------- git init + initial commit + push ----------
echo "▸ Initializing git and pushing initial commit..."
git init --initial-branch=main >/dev/null
git add -A
git commit -m "Initial import for ${INSTANCE_SLUG} ($(date +%Y-%m-%d))" >/dev/null
git remote add origin "git@github.com:${ORG}/${REPO_NAME}.git"
git push -u origin main >/dev/null
echo "  pushed."

# ---------- summary ----------
FILE_COUNT=$(find . -type f -not -path './.git/*' | wc -l | tr -d ' ')

cat <<EOF

============================================================
Instance scaffold complete.

  Repo URL:    https://github.com/${ORG}/${REPO_NAME}
  Local path:  ${LOCAL_PATH}
  Branch:      main (default)
  Files:       ${FILE_COUNT}

Next steps (GUI work — see runbook for details):

  1. GitHub web: Settings → Collaborators and teams →
     - Add the department Team with Write role
     - Add curator(s) directly with Admin role
  2. GitHub web: Settings → Branches → Add branch protection rule for 'main'
     (rule is created but only enforced on Team/Enterprise tier;
     defer the upgrade if AIO-only and no non-curator contributors yet)
  3. Obsidian: Manage Vaults → Open folder as vault → ${LOCAL_PATH}
  4. Obsidian: Settings → Community plugins → Turn on →
     Browse → install 'Git' by vinzent03 → Enable
  5. Obsidian Git plugin settings:
     - Auto pull interval: 5 minutes
     - Auto pull on startup: on
     - Auto commit-and-sync interval: 5 minutes
     - Sync method: merge
     - Pull before push: on
     - Commit message: vault backup: {{date}} {{hostname}}
     Then: git add .obsidian/community-plugins.json .obsidian/plugins/obsidian-git/data.json
           git commit -m "Enable Obsidian Git plugin with auto-commit-and-sync at 5min"
           git push
  6. Cowork: create/repoint project at ${LOCAL_PATH}
  7. Sanity check: edit a file in Obsidian → wait 5 min → verify a
     commit lands on GitHub with the curator's identity.

============================================================
EOF
```

## Running the script

For a fresh new-department setup (Marketing case, no Drive migration):

```
./prime-radiant-instance-setup.sh marketing
```

For migrating an existing Drive-based vault (AIO case):

```
./prime-radiant-instance-setup.sh ai-office \
    "/Users/<you>/Library/CloudStorage/GoogleDrive-michaelb@janusd.io/Shared drives/Janus AI Office/Janus Prime Radiant — AI Office"
```

The script prints what it's about to do, runs each step with a status line, and finishes with a numbered next-step guide for the GUI work. If anything fails (`set -e` is on), it halts at the failing step and prints the underlying error.

## The GUI sequence (steps that can't be safely scripted)

The script handles the bash-automatable 70%; these are the remaining 30%.

### 1 — Repo collaborators and teams (GitHub web)

`https://github.com/Janusd-io/janus-prime-radiant-<INSTANCE_SLUG>/settings/access`

Add the department Team (e.g., `marketing`, `hr`, `finance`) with **Write** role — this is the role new joiners pick up automatically when they're added to the team. Add the curator(s) directly with **Admin** role — direct entry rather than via team membership, so they retain access to repo-level settings like branch rules.

The AIO repo uses this pattern: AI-office team has Write; curators (Michael, Jehad) have direct Admin.

### 2 — Branch protection (GitHub web)

`https://github.com/Janusd-io/janus-prime-radiant-<INSTANCE_SLUG>/settings/branches`

Add branch protection rule:
- Branch name pattern: `main`
- ☑ Require linear history
- ☐ Allow force pushes
- ☐ Allow deletions
- ☐ Do not allow bypassing the above settings (leave unchecked so admins can override in emergencies)

Click Create.

On the `Janusd-io` Org's current Free tier, the rule is created but won't be enforced. Two paths:

- **Upgrade to GitHub Team** (~$4/user/month) for enforcement. Right answer once non-curator contributors are touching the system (Marketing onboarding being the natural trigger point).
- **Defer the upgrade** until enforcement value justifies the cost. Acceptable for a curator-only instance with admin-level trust.

See [[prime-radiant-storage-substrate]] for the cost framing.

### 3 — Register the vault in Obsidian

Obsidian → Manage Vaults → Open folder as vault → select `~/janus/prime-radiant/<INSTANCE_SLUG>/`.

The `.obsidian/` folder that came with the migration (or with the template clone) preserves the curator's view state. For a brand-new fresh instance, Obsidian will populate a default `.obsidian/` on first open.

### 4 — Install the Obsidian Git plugin

In the new vault: Settings → Community plugins → Turn on → accept the third-party-code disclaimer (one-time per vault) → Browse → search "Git" → install **Git** by **vinzent03** (the entry with ~2.5M+ downloads, repository `github.com/Vinzent03/obsidian-git`) → Enable.

### 5 — Configure the Git plugin

Settings → Git, set:
- Auto pull interval (minutes): `5`
- Auto pull on startup: on
- Auto commit-and-sync interval (minutes): `5` (the plugin's combined commit+push setting)
- Sync method: `merge`
- Pull before push: on
- Commit message template: `vault backup: {{date}} {{hostname}}`
- Split timers for automatic commit and sync: off

Then commit the plugin enablement so future joiners pick up the same config when they clone:

```
git add .obsidian/community-plugins.json .obsidian/plugins/obsidian-git/data.json
git commit -m "Enable Obsidian Git plugin with auto-commit-and-sync at 5min"
git push
```

Alternative: just edit any file in Obsidian; the plugin's first auto-cycle (≤5 min) will pick everything up and push with its auto-generated commit message. Functionally identical; less descriptive message.

### 6 — Point Cowork at the local vault

In Cowork, create a new project for this instance OR repoint an existing project's working folder at `~/janus/prime-radiant/<INSTANCE_SLUG>/`. Verify the project mounts cleanly: file count and folder structure visible in Cowork's project panel.

### 7 — Sanity-check the round-trip

Two-way verification before declaring the instance live:

- Edit any file in Obsidian, save, wait ≤5 min, refresh the repo's GitHub page → confirm a commit appears with the curator's identity.
- Make a small change via Cowork (e.g., add a placeholder file to `inbox/.testing/`), then `git add`, `git commit`, `git push` from the vault directory → confirm it appears on GitHub.

The instance is now live and ready for member onboarding.

## Migration-specific final step (Drive → Git only)

After the new Git substrate is running, leave the Drive folder in place for one week as a hot backup. After a week of clean Git operation with no missed writes, rename the Drive folder to `<original-name> (ARCHIVED YYYY-MM-DD)` to signal it's no longer the source of truth. Don't delete the Drive copy for at least another month.

## Member onboarding (next-step pointer)

Once the instance is scaffolded, each joining member runs the per-member setup separately. The first execution of that flow is [[prime-radiant-storage-substrate]] Appendix A (Jehad on AIO, 2026-05-13). After Jehad's setup runs successfully, the generalised `processes/prime-radiant-member-setup.md` will be extracted from it for reuse with subsequent members.

## Empirical record

- **2026-05-13** — AIO instance migrated from Drive to Git. First execution of this flow, before this runbook existed; the runbook captures the lessons. See [[prime-radiant-storage-substrate]] for substrate rationale and [[2026-05-12-prime-radiant-marketing-setup-debug]] for the precipitating Drive failure.
- **Marketing** (next, ~week of 2026-05-13) — first scripted execution using this runbook. Fresh-mode (no source path); the Marketing vault contents from the failed 2026-05-12 attempt get re-created on the new substrate. Expected outcome: instance scaffold complete in ≤10 minutes vs. the ~2 hours the AIO migration took unscripted.
- **IT-Ops** (queued per [[janus-prime-radiant-build]]) — Euclid's project-management team first pilot.
- **HR / Finance / ISO / Office-of-CEO / Engineering / Training** — sequenced after Marketing and IT-Ops prove the runbook.

## Open issues to fold back into the runbook as they surface

- **Concurrent Cowork sessions** touching the same vault — not yet a real problem with one curator per instance; revisit if Marketing introduces simultaneous-write patterns.
- **Mobile editing** — Obsidian Git plugin is unstable on mobile per its own documentation. Mobile path is Web Clipper-to-desktop-inbox, not direct mobile editing. Revisit if/when a contributor pushes for mobile.
- **Cross-instance federation tooling** — sibling-clone layout supports [[peer-to-peer-mesh-federation-pattern]] mechanically; programmatic cross-vault search/citation tooling is a future increment.
- **Lint workflow as GitHub Actions** — once GitHub Team is on, the wiki's lint pass can become a CI status check on `main`. Worth adding to step 2 of the GUI sequence at that point.
