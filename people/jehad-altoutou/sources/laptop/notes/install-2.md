---
type: source
source_type: laptop
title: INSTALL
slug: install-2
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/INSTALL.md
original_size: 2506
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public install guide shipped in the bootstrap repo."
---

# INSTALL

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/INSTALL.md` on 2026-05-14._

# Install — /janus-brain

## What you need

- macOS 14+ (Linux untested; see REWRITE-SPEC.md out-of-scope notes)
- Python 3.10+
- `gh` CLI authenticated to GitHub (member of the `Janusd-io` org)
- Claude Desktop with the Code or Cowork tab
- Obsidian.app installed
- `graphify` (the installer attempts to install via pipx if missing)

## Install from the repo

```bash
gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap
~/Documents/janus-brain-bootstrap/install.sh
```

The installer:

1. Verifies `python3`, `git`, `gh`, `graphify`, plus the Phase 4.5 toolchain (`pdftotext` / `pandoc` / `tesseract` / `pandas`)
2. Copies `skills/janus-brain/` into `~/.claude/skills/`
3. Backs up any prior install to `~/.claude/skills/janus-brain.bak`
4. Drops `Janus Brain - Start Here.md` on the Desktop

It does **not** create your vault — that happens on the first `/janus-brain` run, which clones your dept's repo and scaffolds your `people/<slug>/` subtree.

## Verify

```bash
~/Documents/janus-brain-bootstrap/install.sh --check
```

Reports installed-files count, `gh` auth, graphify status, and whether the single vault exists at `~/janus/prime-radiant/` (with the remote URL and detected `people/<slug>/` subtrees). Also warns if a pre-2026-05-14 two-vault layout is detected at `~/janus/prime-radiant/personal/` or `~/janus/prime-radiant/ai-office/`.

## First run (interactive)

1. Restart Claude Desktop so the new skill loads.
2. Open a Code or Cowork chat and type `/janus-brain`.
3. Confirm your identity + task tracker; choose laptop scope; let it run.

See `SKILL.md` and `../../ENROLLMENT.md` for the full phase-by-phase description.

## Update

```bash
cd ~/Documents/janus-brain-bootstrap
git pull
./install.sh
```

Existing notes are not touched. The next `/janus-brain sync` picks up any schema changes.

## Uninstall

```bash
~/Documents/janus-brain-bootstrap/install.sh --uninstall
```

Removes the skill. Does **not** delete the Obsidian vault at `~/janus/prime-radiant/` — that's the user's (and dept's) data.

## Auto-sync (optional)

A daily launchd job can open Claude Desktop at a chosen time and trigger `/janus-brain sync`:

```bash
~/Documents/janus-brain-bootstrap/install.sh --install-auto-sync --time 07:30
~/Documents/janus-brain-bootstrap/install.sh --auto-sync-status
~/Documents/janus-brain-bootstrap/install.sh --uninstall-auto-sync
```

On the first fire, macOS will prompt to allow System Events to control Claude Desktop (one-time grant).
