---
type: source
source_type: laptop
title: README
slug: readme-10
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/README.md
original_size: 10222
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Repo README for janus-puls-onboarding — distributable internal tooling; work content"
---

# README

_Extracted from `Documents/janus-puls-onboarding/README.md` on 2026-05-14._

# Janus PULS — Onboarding & Task Plan

> Personal working notes for navigating the IMS / PULS programme at Janus Digital.
> The ISO lead sent a deck. This repo translates the deck into "what do I actually have to do, and in what order."

---

## How to use this repo

Read in order. Each file builds on the previous.

| # | File | When to read |
|---|---|---|
| 1 | [01-START-HERE.md](./01-START-HERE.md) | **Read first.** What's actually happening. The 20 process documents. What goes inside each one. |
| 2 | [02-DO-THIS-TODAY.md](./02-DO-THIS-TODAY.md) | **Read second.** The single email to send the ISO lead today. Three sentences. Unblocks everything. |
| 3 | [03-YOUR-5-TASKS.md](./03-YOUR-5-TASKS.md) | After the ISO lead replies. The 5 tasks in priority order. |
| 4 | [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md) | After Task 1 + Task 2 are scheduled. The ISO 9001 Figure-1 schematic response (with diagrams) — what to send when you submit your First Voice form properly. |
| 5 | [05-JARGON-DECODER.md](./05-JARGON-DECODER.md) | Reference. What every buzzword in the deck actually means. |
| 6 | [06-FIRST-VOICE-FINAL.md](./06-FIRST-VOICE-FINAL.md) | **Send-ready.** First Voice answers addressed to Simon. Send when he asks for the form. |
| 7 | [07-MEETING-TO-TASK-WORKFLOW.md](./07-MEETING-TO-TASK-WORKFLOW.md) | The actual SOP for "meeting → task → build" — implements Activity 1 of your AI Ops process. Becomes part of the C1 / C2 / S2 process documents. ISO clause map included. |
| 8 | [08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md) | AI Tool Evaluation & Onboarding — two intake paths (meeting + Slack) → registry check → Gates 1-4 → sandbox → IT handover. Includes the implementation gap for the Slack-webhook path. Maps directly to ISO 42001 §8.2. |
| 9 | [09-PLATFORM-DEVELOPMENT-PROCESS.md](./09-PLATFORM-DEVELOPMENT-PROCESS.md) | [[platform-development-process|Platform & Tool Development Process]] — how a whole platform (e.g. [[assessify|Assessify]]) goes from pain point to live, with [[obsidian|Obsidian]] as the living source of truth. Worked example: Assessify, end to end. Becomes the Activities section of the C2 IMS process document. |
| 10 | [10-GAP-ANALYSIS-vs-SIMON.md](./10-GAP-ANALYSIS-vs-SIMON.md) | Gap analysis: our docs vs. Simon's IMS-PRC-AI-001 v0.4. ~70% overlap. 10 specific gaps with effort estimates (~3 dev-days total). Plus the HR architecture question (Option 1 vs Option 2) with a recommendation. Living doc — close items as resolved. |

---

## Distributable skill — `/ims-enrolment` (v1.4)

A Claude Desktop skill that walks **any Janus department** through ISO documentation. Lives in [`skills/ims-enrolment/`](./skills/ims-enrolment/). 23 files · references + templates + examples + prompts + interview scripts.

---

### What you get

After running the skill, every department ends up with a folder on their Desktop:

```text
~/Desktop/<Department> - IMS Enrolment/
├── README.md                        Auto-generated manifest
├── parent-process.md                Department in ISO 9001 Figure 1 shape
├── sub-process-*.md                 One per major activity
├── diagram-prompt-*.md              ChatGPT prompts → polished diagrams
├── first-voice-*.md                 One per department member
├── handover-to-simon.md             Cover note to Simon (ISO Lead)
├── diagrams/                        Generated PNGs/SVGs
└── exports/
    └── HANDOVER-BUNDLE.docx         Single Word doc — send to Simon
```

Anyone on the team can find it on the Desktop. No internal paths to navigate.

---

### Install — pick one path

#### Path A — From inside Claude Desktop (easiest, no Terminal)

Open Claude Desktop. Say:

> *"Install the [[ims-enrolment|IMS enrolment]] skill from the Janus PULS repo."*

Claude proposes the install command. Approve the Bash tool call. Restart Claude Desktop when it finishes.

**Requires:** access to this [[github|GitHub]] repo (ask Jehad to add you as a collaborator) or a zip from Jehad.

#### Path B — Terminal (macOS / Linux)

```bash
git clone https://github.com/Jehada-Janusd/janus-puls-onboarding.git ~/Documents/janus-puls-onboarding
~/Documents/janus-puls-onboarding/install.sh
```

Restart Claude Desktop. Done.

The installer:

1. Checks `pandoc` is installed (`brew install pandoc` if not — handled automatically)
2. Copies the skill to `~/.claude/skills/ims-enrolment/` (23 files)
3. Backs up any existing install to `~/.claude/.skill-backups/` (timestamped, last 3 kept)
4. Drops a `~/Desktop/IMS Enrolment - Start Here.md` quickstart on your Desktop
5. Verifies all required files are present

#### Path C — Terminal (Windows / PowerShell)

```powershell
git clone https://github.com/Jehada-Janusd/janus-puls-onboarding.git $env:USERPROFILE\Documents\janus-puls-onboarding
& "$env:USERPROFILE\Documents\janus-puls-onboarding\install.ps1"
```

Restart Claude Desktop. Done.

PowerShell installer behaves the same: installs pandoc via `winget` if missing, backs up to `%USERPROFILE%\.claude\.skill-backups\`, drops the Start Here file.

---

### Verify, update, uninstall

| Action | macOS / Linux | Windows |
|---|---|---|
| **Verify install** | `~/Documents/janus-puls-onboarding/install.sh --check` | `.\install.ps1 -Check` |
| **Update to latest** | `cd ~/Documents/janus-puls-onboarding && git pull && ./install.sh` | `cd $env:USERPROFILE\Documents\janus-puls-onboarding; git pull; .\install.ps1` |
| **Uninstall** | `~/Documents/janus-puls-onboarding/install.sh --uninstall` | `.\install.ps1 -Uninstall` |
| **List skills** | (in Claude Desktop) `/skill-list` | same |

Phase 0 of the skill runs verification automatically every time you invoke `/ims-enrolment`. If anything is missing or stale, it tells you exactly what to do.

---

### What the skill does

Drives a **5-phase interview** that produces ISO 9001:2015 Figure 1-compliant documentation for one department:

| Phase | Tool | Output |
|---|---|---|
| 0. Self-verify | Bash | (silent) Confirms 23 required files + pandoc on PATH; offers fixes if not |
| 1. Foundation | Reading | Department head reads IMS overview + Figure 1 schematic + 7-section template |
| 2. Parent process interview | Interview | `parent-process.md` (whole department in Figure 1 shape) |
| 3. Sub-process interviews | Interview | One `sub-process-*.md` per activity from the parent |
| 4. First Voice | Interview (Mode A) or Async distribute (Mode B) | One `first-voice-*.md` per department member |
| 5a. Desktop folder + diagrams | Auto | Output folder on Desktop · one ChatGPT prompt per process doc |
| 5b. Diagram generation | Manual ChatGPT | Paste each prompt → polished PNG/SVG → save to `diagrams/` |
| 5c. Word doc bundle | Pandoc | `exports/HANDOVER-BUNDLE.docx` — single doc to send Simon |

**AI Department ships as the fully-worked example** — 4 process docs + 4 filled-in diagram prompts inside `examples/ai-department/`. When other departments enrol and feel lost, the skill points them at this example.

**Trigger phrases:**

- *"Enrol [department] into the IMS"*
- *"Help [team] document their processes for ISO"*
- *"I'm a department head, where do I start with this ISO thing?"*

---

### Distribution to other Janus departments

| Friction | Method | When to use |
|---|---|---|
| Lowest | Add them as a GitHub repo collaborator → they run Path B/C | Trusted internal use |
| Low | Zip `skills/ims-enrolment` + `install.sh` + `install.ps1` → send via Slack | They lack GitHub access |
| Medium | Park the zip on a shared drive · they `cp` + `install.sh` from the shared location | Multiple installers at once |

---

### For maintainers

If you're editing the skill (not just installing), read [DEVELOPING.md](./DEVELOPING.md). It documents the source-of-truth model (`~/.claude/skills/` is runtime, `skills/ims-enrolment/` in repo is canonical) and the one race condition that bites if you edit global then re-run the installer without syncing first. There's a helper at [`scripts/sync-skill-from-global.sh`](./scripts/sync-skill-from-global.sh) for that.

---

### Skill changelog

| Version | Date | Highlights |
|---|---|---|
| v1.4 | 2026-05-11 | Phase 0 explicit Bash check · `install.ps1` for Windows · backups moved to `~/.claude/.skill-backups/` (no more duplicate-skill collision) · `prompts/interview-first-voice.md` (Mode A + Mode B) · `scripts/sync-skill-from-global.sh` · `DEVELOPING.md` · slug rule + resume mechanism documented · explicit diagram parameterisation |
| v1.3 | 2026-05-11 | Outputs land on `~/Desktop/<Department> - IMS Enrolment/` · Start Here quickstart file on Desktop |
| v1.2 | 2026-05-11 | Self-installable via `install.sh` · self-verifying via Phase 0 · `INSTALL.md` with 4 install paths · CLAUDE.md auto-offer rule |
| v1.1 | 2026-05-11 | Diagram prompts per process doc · AIR ownership clarified (AI department maintains, other departments only list tools) |
| v1.0 | 2026-05-11 | Initial release — 5-phase orchestrator · AI Department worked example |

---

## TL;DR (60 seconds)

Janus wants three ISO certifications (Quality 9001 + Security 27001 + AI Governance 42001) on **one** certificate covering Dubai + Singapore + UK + future branches. To pull this off, the company needs:

1. **20 process documents** (one per area of the business) written in **Notion**
2. **A live dashboard called PULS** showing real-time status of each process
3. The whole thing **deployable as a template** to every new branch (10 this year, 20/yr from 2027)

That's the entire deck. Everything else — "Predictive Unified Live System," "Live · Visible · Trusted," the heartbeat metaphor — is branding around that core idea.

## Your job, briefly

1. Fill the **[[puls-first-voice|PULS First Voice]]** form for your role (15 min). Pre-filled in [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md).
2. Lead the **AI/IT tooling discussion** (Step 4 on slide 17). Recommendation drafted.
3. Find out from Michael whether you own **C1 / C2 / S2** as Process Owner.
4. If yes → write those process documents using the 7-section ISO 9001 template.
5. Eventually → build the actual PULS dashboard.

## Today

Send three sentences to the ISO lead. See [02-DO-THIS-TODAY.md](./02-DO-THIS-TODAY.md).
