---
type: reference
title: Janus PULS Onboarding (external repo)
slug: janus-puls-onboarding
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, github, repo]
repo: https://github.com/Jehada-Janusd/janus-puls-onboarding
local_path: /Users/jehad/Documents/janus-puls-onboarding
---
# External Repo — Janus PULS Onboarding

> All procedural deliverables for the IMS / PULS programme live in a private GitHub repo. This note is the bridge — Obsidian for context and navigation, the repo for the actual ISO-grade documents.

---

## 🔗 Repo

**[github.com/Jehada-Janusd/janus-puls-onboarding](https://github.com/Jehada-Janusd/janus-puls-onboarding)** (private)

Local clone: `/Users/jehad/Documents/janus-puls-onboarding`

---

## Why GitHub and not just Obsidian

- GitHub renders Mermaid diagrams natively (so Simon can see them properly)
- GitHub renders tables, code blocks, and ISO clause maps cleanly
- Markdown linter visible in IDE
- One source of truth for procedural docs · auditors can be given a read-only repo link
- Obsidian stays the navigation + concept layer; repo is the deliverable layer

---

## The 11 documents in the repo

| # | File | What it is | Status |
|---|---|---|---|
| 0 | [README.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/README.md) | Navigation hub + 60-second TL;DR | ✅ |
| 1 | [01-START-HERE.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/01-START-HERE.md) | Plain English: what's happening, the 20 docs, the 7 sections inside each | ✅ |
| 2 | [02-DO-THIS-TODAY.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/02-DO-THIS-TODAY.md) | The 3-sentence email to Simon | ✅ Sent |
| 3 | [03-YOUR-5-TASKS.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/03-YOUR-5-TASKS.md) | Full task breakdown with order of operations | ✅ |
| 4 | [04-FORMAL-RESPONSE.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/04-FORMAL-RESPONSE.md) | ISO 9001 Figure-1 schematic for the AI Ops Engineer role (covers C1, C2, S2 at activity level) | ✅ |
| 5 | [05-JARGON-DECODER.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/05-JARGON-DECODER.md) | Every buzzword and acronym translated | ✅ |
| 6 | [06-FIRST-VOICE-FINAL.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/06-FIRST-VOICE-FINAL.md) | **Send-ready** First Voice answers addressed to Simon | ✅ Ready |
| 7 | [07-MEETING-TO-TASK-WORKFLOW.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/07-MEETING-TO-TASK-WORKFLOW.md) | The actual SOP for "meeting → task → build" — implements Activity 1 of the AI Ops process. Underlying skill: [[standup|/standup v3.11]] | ✅ |
| 8 | [08-TOOL-EVALUATION-PROCEDURE.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/08-TOOL-EVALUATION-PROCEDURE.md) | AI Tool Evaluation & Onboarding · two intake paths (meeting + Slack) → registry check → Gates 1-4 → sandbox → IT handover | ✅ v0.4 — needs v0.5 alignment to Simon's IMS-PRC-AI-001 |
| 9 | [09-PLATFORM-DEVELOPMENT-PROCESS.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/09-PLATFORM-DEVELOPMENT-PROCESS.md) | Platform & Tool Development Process — 9 stages from pain point to live. Worked example: [[assessify|Assessify]] | ✅ |
| 10 | [10-GAP-ANALYSIS-vs-SIMON.md](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/10-GAP-ANALYSIS-vs-SIMON.md) | Gap analysis: our docs vs Simon's IMS-PRC-AI-001 v0.4 · 10 specific gaps · ~3 dev-days to align · plus HR architecture recommendation | ✅ Living doc |

---

## Word doc exports

For sharing with Simon (or other non-technical recipients), each markdown is converted via pandoc:

```bash
cd ~/Documents/janus-puls-onboarding
pandoc 06-FIRST-VOICE-FINAL.md -o ~/Desktop/PULS-First-Voice-Jehad.docx
```

Generated Word docs on Desktop:

- `PULS-First-Voice-Jehad.docx` — already addressed to Simon, send-ready
- `PULS-Meeting-to-Task-Workflow.docx`
- `PULS-Tool-Evaluation-Procedure.docx`
- `PULS-Platform-Development-Process.docx`
- `PULS-Gap-Analysis-vs-Simon.docx`

---

## How to add a new doc

```bash
cd ~/Documents/janus-puls-onboarding
# create the new file, e.g. 11-IMS-PRC-AI-001-v0.5.md

git add 11-IMS-PRC-AI-001-v0.5.md
git -c user.email="jehada@janusd.io" -c user.name="Jehad" commit -m "Add IMS-PRC-AI-001 v0.5 aligned to Simon's structure"
git push
```

Then update the README.md in the repo to add it to the navigation table, and update this Obsidian note to reflect the new file.

---

## Update discipline

When the repo state changes:

1. Commit and push to GitHub
2. Update the table above with new docs / status changes
3. Update [[iso-ims-puls]] status snapshot
4. If a new doc maps to a specific IMS process, update [[ims-process-documents]]

---

## Related

- [[iso-ims-puls]] — entry point
- [[ims-process-documents]] — what each repo file maps to
- [[ims-open-questions-for-simon]] — what's pending before docs can be finalised

← Back to [[iso-ims-puls]]
