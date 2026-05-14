---
type: source
source_type: laptop
title: DEVELOPING
slug: developing
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/DEVELOPING.md
original_size: 6145
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.88
sensitivity_reason: "Developer notes on /ims-enrolment skill maintenance; dept-shareable."
---

# DEVELOPING

_Extracted from `Documents/janus-puls-onboarding/DEVELOPING.md` on 2026-05-14._

# Developing — Editing the `/ims-enrolment` skill

> If you're the only person editing the skill, you can mostly ignore this. But there's one race condition that will bite anyone who edits global → runs installer → loses changes, and the fix is one rule.

## Two surfaces, one source of truth

The skill exists in two places at any time:

| Location | Purpose |
|---|---|
| `~/.claude/skills/ims-enrolment/` | **Runtime** — what Claude Desktop loads and runs |
| `~/Documents/janus-puls-onboarding/skills/ims-enrolment/` | **Source** — what the installer copies from, and what [[github|GitHub]] serves to other employees |

`install.sh` copies **repo → global** (one-way). The repo is the source of truth for distribution.

## The race condition

If you:

1. Edit something in `~/.claude/skills/ims-enrolment/` (the runtime location)
2. Run `./install.sh` to test it
3. **Your edits get destroyed** — the installer copies the OLD content from the repo over your edits

This bit us during v1.3 development. To avoid it:

## The rule — sync before install

```
Edit global → sync to repo → commit → push → install.sh is safe again
```

Use the sync helper:

```bash
./scripts/sync-skill-from-global.sh
```

It rsyncs the global skill into the repo, shows you the diff, and reminds you to commit before running the installer.

## Recommended dev workflow

```bash
# 1. Edit files in ~/.claude/skills/ims-enrolment/
#    (this is what Claude Desktop sees while you iterate)

# 2. Test with Claude Desktop — invoke /ims-enrolment, see how it behaves

# 3. When happy, sync to repo
./scripts/sync-skill-from-global.sh

# 4. Review the diff
git diff HEAD -- skills/ims-enrolment/

# 5. Bump version in skills/ims-enrolment/SKILL.md (`**Version:**` field)
#    Use semver: patch for bug fix, minor for new files/templates, major for breaking changes

# 6. Commit + push
git add .
git commit -m "ims-enrolment vX.Y: <what changed>"
git push

# 7. (Optional) Re-run installer to confirm clean install matches your dev state
./install.sh
```

## When to edit the repo directly instead

Edit `skills/ims-enrolment/` in the repo directly (and run `./install.sh` after) when:

- Onboarding a new machine
- Reviewing a teammate's PR
- You don't want runtime updates until you're done editing
- You're not iterating live with Claude Desktop

## File map

```
janus-puls-onboarding/
├── install.sh                  # Bash installer (Mac/Linux)
├── install.ps1                 # PowerShell installer (Windows)
├── README.md                   # Public-facing overview + install instructions
├── DEVELOPING.md               # This file
├── 01-START-HERE.md…10-…       # The 11 procedural PULS onboarding docs (separate from the skill)
├── scripts/
│   └── sync-skill-from-global.sh
└── skills/ims-enrolment/       # The skill bundle (source of truth)
    ├── SKILL.md
    ├── INSTALL.md
    ├── references/
    ├── templates/
    ├── prompts/
    └── examples/ai-department/
```

The **11 procedural docs at the repo root** (`04-FORMAL-RESPONSE.md`, etc.) and the **skill examples** (`skills/ims-enrolment/examples/ai-department/parent-process.md`, etc.) contain similar content but serve different audiences:

- Root docs = for Jehad and Simon's collaboration (working docs)
- Skill examples = for any department head pattern-matching against the AI Department's work

Both should stay roughly aligned. If you make a substantive change to one, propagate to the other.

## Versioning

Use semver in `skills/ims-enrolment/SKILL.md` `**Version:**` field:

- `1.x` patches → bug fixes, typos, small clarifications
- `1.x` minor bumps → new files/templates, new phases, new examples
- `2.0` major bump → breaking changes (renamed phases, removed templates, schema breaks)

Tag in git after each version: `git tag v1.4 && git push --tags`.

## Releasing a new version

1. Sync from global if you've been iterating locally: `./scripts/sync-skill-from-global.sh`
2. Bump `SKILL.md` `**Version:**` field
3. Update `~/.claude/skills/ims-enrolment/SKILL.md` to match (or re-sync if needed)
4. Update `scripts/sync-skill-from-global.sh`'s required-files check if you added new mandatory files
5. Update `install.sh` and `install.ps1` `required=()` lists if you added new mandatory files
6. Update `INSTALL.md` if the install steps changed
7. Update [[obsidian|Obsidian]] `07 [[iso-ims-puls|ISO IMS PULS]]/[[ims-enrolment|IMS Enrolment]] Skill.md` with the new version info
8. Update `~/.claude/projects/-Users-jehad/memory/reference_iso_ims_puls.md`
9. Commit + push
10. Optionally tag in git

## Testing checklist

Before shipping a version:

- [ ] `install.sh --check` passes
- [ ] `install.sh --uninstall && install.sh` produces a clean install
- [ ] All 22+ required files present (`install.sh --check` validates)
- [ ] No `[PLACEHOLDER]` markers leaked into example files
- [ ] Mermaid diagrams in example process docs render on GitHub (paste a sample into <https://mermaid.live>)
- [ ] Restart Claude Desktop and confirm `/ims-enrolment` invokes Phase 0 self-verify
- [ ] Pandoc converts at least one of the example process docs cleanly: `pandoc skills/ims-enrolment/examples/ai-department/parent-process.md -o /tmp/test.docx && open /tmp/test.docx`

## When things break

| Symptom | Most likely cause | Fix |
|---|---|---|
| Two skills with same name in `/skill-list` | Backup directory inside `~/.claude/skills/` (e.g., `ims-enrolment.bak`) — v1.1-1.3 bug | Should be auto-fixed in v1.4+ (backups now go to `~/.claude/.skill-backups/`). If you have an old `.bak`: `rm -rf ~/.claude/skills/*.bak` |
| Skill changes don't show up | Edited repo but didn't run installer; OR edited global, ran installer (which reverted) | Re-sync: `./scripts/sync-skill-from-global.sh` then re-run installer |
| `install.sh: Permission denied` | Script not executable | `chmod +x install.sh` |
| `pandoc: command not found` | pandoc missing | `brew install pandoc` (Mac) · `sudo apt install pandoc` (Linux) · `winget install JohnMacFarlane.Pandoc` (Win) |

## Owner

Jehad — AI Operations Engineer · jehada@janusd.io
