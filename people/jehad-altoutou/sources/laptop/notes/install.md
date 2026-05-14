---
type: source
source_type: laptop
title: Janus Puls Onboarding — INSTALL
slug: install
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/INSTALL.md
original_size: 5418
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.85
sensitivity_reason: "Installer/runbook for the /ims-enrolment skill — distributable to other Janus depts; work content"
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# INSTALL

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/INSTALL.md` on 2026-05-14._

# `/ims-enrolment` — Installation

> Pick the path that matches your situation. All three end with the same state: the skill installed at `~/.claude/skills/ims-enrolment/` and Claude Desktop ready to use it.

---

## Path 1 — Easiest (via Claude Desktop)

Open Claude Desktop and type:

> *"Install the [[ims-enrolment|IMS enrolment]] skill from the Janus PULS repo."*

Claude will propose running the install script. Approve the Bash tool call. Restart Claude Desktop when it finishes. Done.

**Requires:** You must have access to the [[github|GitHub]] repo `Jehada-Janusd/janus-puls-onboarding` (ask Jehad), OR a local clone at `~/Documents/janus-puls-onboarding`, OR a zip from Jehad.

---

## Path 2 — One terminal command (if you already have the repo cloned)

```bash
~/Documents/janus-puls-onboarding/install.sh
```

That's it. The script will:

1. Check pandoc · install via `brew` (Mac) or `apt` (Linux) if missing
2. Locate the skill source (local repo OR download from GitHub)
3. Copy to `~/.claude/skills/ims-enrolment/`
4. Verify all required files are present

Then restart Claude Desktop.

---

## Path 3 — Fresh machine, no repo yet

```bash
# Clone the repo (you need access)
git clone https://github.com/Jehada-Janusd/janus-puls-onboarding.git ~/Documents/janus-puls-onboarding

# Run the installer
~/Documents/janus-puls-onboarding/install.sh
```

Restart Claude Desktop.

---

## Path 4 — Manual install (if scripts fail or for inspection)

```bash
# Mac/Linux
mkdir -p ~/.claude/skills
cp -r ~/Documents/janus-puls-onboarding/skills/ims-enrolment ~/.claude/skills/

# Install pandoc separately
brew install pandoc       # macOS
sudo apt install pandoc   # Linux
# Windows: download from https://pandoc.org/installing.html
```

Restart Claude Desktop.

---

## Verify the install

```bash
~/Documents/janus-puls-onboarding/install.sh --check
```

Or in Claude Desktop:

> *"Verify the IMS enrolment skill is installed correctly."*

Or `/skill-list` and look for `ims-enrolment` in the list.

---

## Updating to a newer version

```bash
cd ~/Documents/janus-puls-onboarding
git pull
./install.sh
```

The installer backs up your previous copy to `~/.claude/skills/ims-enrolment.bak` before replacing — so updates are reversible.

---

## Uninstalling

```bash
~/Documents/janus-puls-onboarding/install.sh --uninstall
```

This removes `~/.claude/skills/ims-enrolment/`. Pandoc is not touched (it has other uses on your machine).

## Windows users

Use the PowerShell installer instead:

```powershell
# Open PowerShell, navigate to the repo clone, then:
.\install.ps1               # install / update
.\install.ps1 -Check        # verify only
.\install.ps1 -Uninstall    # remove
```

Same behaviour as `install.sh`: copies skill to `%USERPROFILE%\.claude\skills\ims-enrolment\`, installs pandoc via winget if missing, backs up existing installs to `%USERPROFILE%\.claude\.skill-backups\` (timestamped, last 3 kept), drops `Desktop\IMS Enrolment - Start Here.md`.

## Backup retention

The installer (Mac/Linux/Windows) automatically backs up existing installs to `~/.claude/.skill-backups/ims-enrolment-<timestamp>/` (or `%USERPROFILE%\.claude\.skill-backups\` on Windows). The 3 most recent backups are kept; older ones are auto-pruned.

This location is **outside** `~/.claude/skills/`, so backups don't get loaded as duplicate skills by Claude Desktop.

---

## What gets installed

```
~/.claude/skills/ims-enrolment/   (21 files, ~3500 lines)
├── SKILL.md                          ← Orchestrator (5 phases)
├── INSTALL.md                        ← This file
├── references/   (5 files)
│   ├── iso-9001-figure-1.md
│   ├── seven-section-template.md
│   ├── plain-english-overview.md
│   ├── jargon-decoder.md
│   └── simon-ims-prc-ai-001-v0.4.md
├── templates/    (5 files)
│   ├── parent-department-process.md
│   ├── sub-process.md
│   ├── first-voice-questionnaire.md
│   ├── diagram-prompt.md
│   └── handover-to-simon.md
├── examples/ai-department/   (8 files — 4 process docs + 4 diagram prompts)
└── prompts/      (2 files)
    ├── interview-department-head.md
    └── interview-activity-owner.md
```

Plus `pandoc` available on your `PATH` (separately installed, used by Phase 5b for Word doc exports).

---

## Distribution to other Janus departments

If you're Jehad sending this to another department head, the lowest-friction options:

| Friction | Method |
|---|---|
| Lowest | Add them as a GitHub repo collaborator → they run Path 3 |
| Low | Zip `skills/ims-enrolment` + `install.sh` → send via Slack → they unzip and run `./install.sh` |
| Medium | Keep the skill on a shared drive → they copy + run install.sh from the shared location |

The skill itself is self-contained — no other dependencies beyond pandoc.

---

## Troubleshooting

**`/ims-enrolment` doesn't appear after install**
→ Restart Claude Desktop. Skills load at startup.

**`pandoc: command not found` during Phase 5b**
→ Install pandoc: `brew install pandoc` on Mac. Phase 5b regenerates the Word docs — re-run that phase after install.

**`install.sh: Permission denied`**
→ `chmod +x ~/Documents/janus-puls-onboarding/install.sh` then re-run.

**"Repo is private — you need access"**
→ Ask Jehad to add your GitHub username as a collaborator, or to send you a zip.
