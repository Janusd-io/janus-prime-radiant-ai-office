---
type: skill-reference
title: IMS Enrolment Skill
slug: ims-enrolment
created: 2026-05-11
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, skill, enrolment, claude-desktop]
skill_path: ~/.claude/skills/ims-enrolment/
repo_path: ~/Documents/janus-puls-onboarding/skills/ims-enrolment/
version: 1.0
---
# `/ims-enrolment` — Department Onboarding Skill

> Claude Desktop skill that walks any Janus department through documenting their work in ISO 9001:2015 Figure 1 shape. Produces parent process + sub-processes + First Voice + handover bundle for Simon (ISO Lead).

## Why this skill exists

The IMS programme needs **every department at Janus** to enrol — not just AI. Each department lead is going to face the same blank-page problem we faced: *"Where do I start? What does Simon want? What's an ISO 9001 Figure 1 schematic?"*

This skill is the answer. It bundles:

- **Foundation** — Plain English overview · jargon decoder · ISO 9001 Figure 1 schematic · the 7-section template · Simon's IMS-PRC-AI-001 v0.4 summary
- **Templates** — Blank parent-process · blank sub-process · blank First Voice · handover-to-Simon cover note
- **Interview prompts** — Guided question scripts for the department head (Phase 2) and each activity owner (Phase 3)
- **Worked example** — The Janus AI Department fully documented (parent + 3 sub-processes) as the reference any department can pattern-match against

## How it works (5 phases)

1. **Foundation** — Department head reads the references (15 min if new to ISO, skip if seasoned)
2. **Parent process interview** — 30-45 min with the department head → produces `parent-process.md`
3. **Sub-process interviews** — 20-30 min per activity from the parent's list → produces one `sub-process-*.md` per activity
4. **First Voice** — Each department member fills the 6-question form for their role
5. **Handover bundle** — split in two:
   - **5a — Diagram prompts:** one ChatGPT prompt per process document (parametric `diagram-prompt.md` template, filled in from the answered process doc). Department pastes each into ChatGPT to generate polished PNG/SVG diagrams. Mermaid backup ships in every process doc as the guaranteed-text fallback.
   - **5b — Word doc bundle:** all process docs + diagram prompts + generated images + First Voice forms → single Word doc for Simon, plus a cover note (`handover-to-simon.md`).

## Output location — Desktop folder (v1.3+)

Every department that uses the skill produces a folder **on the Desktop**, not buried in `~/.claude/` or `~/Documents/`:

```
~/Desktop/<Department> - IMS Enrolment/
├── README.md                    ← Manifest of what's in the folder
├── parent-process.md
├── sub-process-*.md
├── diagram-prompt-*.md          ← Paste into ChatGPT for polished diagrams
├── first-voice-*.md
├── handover-to-simon.md
├── diagrams/                    ← Generated PNGs/SVGs
└── exports/
    └── HANDOVER-BUNDLE.docx     ← For Simon
```

Folder name convention: title case + space-dash-space separator (e.g., `HR - IMS Enrolment`, `Finance - IMS Enrolment`). This means any team member can locate a department's IMS bundle by opening Finder/Explorer and looking at the Desktop — no need to know internal file paths.

After install, the skill also drops a `~/Desktop/IMS Enrolment - Start Here.md` quickstart file (just one file, easily deleted) explaining how to use the skill.

## Tools register (Linear AIR) clarification

The skill is explicit that **departments do NOT enrol AI tools into Linear AIR themselves**. The AI department maintains the register and runs Gate 1-4 evaluation on every AI tool before it reaches other departments via the [Tool Evaluation Procedure](https://github.com/Jehada-Janusd/janus-puls-onboarding/blob/main/08-TOOL-EVALUATION-PROCEDURE.md). Other departments just list the tools they use; the AI department cross-checks AIR coverage independently. This wording was clarified in v1.1 of the skill after early confusion.

## Trigger phrases

- "Enrol [department] into the IMS"
- "Help [team] document their processes for ISO"
- "I'm a department head, where do I start with this ISO thing?"

## Where it lives

| Location | Path | Purpose |
|---|---|---|
| **Global skill (Jehad's machine)** | `~/.claude/skills/ims-enrolment/` | Auto-loaded into every Claude Desktop session |
| **Repo export** | `~/Documents/janus-puls-onboarding/skills/ims-enrolment/` | Portable copy for other employees to install on their machines |

## Skill bundle contents

```
ims-enrolment/
├── SKILL.md                                          ← Orchestrator
├── references/
│   ├── iso-9001-figure-1.md                          ← The schematic shape
│   ├── seven-section-template.md                     ← What goes in each section
│   ├── plain-english-overview.md                     ← Non-technical IMS intro
│   ├── jargon-decoder.md                             ← Buzzword translator
│   └── simon-ims-prc-ai-001-v0.4.md                  ← Summary of Simon's formal template
├── templates/
│   ├── parent-department-process.md                  ← Blank parent
│   ├── sub-process.md                                ← Blank sub
│   ├── first-voice-questionnaire.md                  ← Blank First Voice
│   ├── diagram-prompt.md                             ← Parametric ChatGPT prompt (new in v1.1)
│   └── handover-to-simon.md                          ← Cover note
├── examples/ai-department/
│   ├── parent-process.md                             ← The Janus AI Dept as a whole
│   ├── sub-process-meeting-to-task.md                ← Meeting → Task → Build
│   ├── sub-process-tool-evaluation.md                ← AI Tool Evaluation
│   ├── sub-process-platform-development.md           ← Platform Development
│   ├── diagram-prompt-parent-process.md              ← Filled-in diagram prompt for parent (new v1.1)
│   ├── diagram-prompt-meeting-to-task.md             ← (new v1.1)
│   ├── diagram-prompt-tool-evaluation.md             ← (new v1.1)
│   └── diagram-prompt-platform-development.md        ← (new v1.1)
└── prompts/
    ├── interview-department-head.md                  ← Phase 2 script
    └── interview-activity-owner.md                   ← Phase 3 script
```

**20 files. ~3500 lines total. v1.1.**

## Distribution

For other department heads to install on their own machines:

```bash
# Option A — clone the repo and install from there
cd ~
git clone https://github.com/Jehada-Janusd/janus-puls-onboarding.git
cp -r janus-puls-onboarding/skills/ims-enrolment ~/.claude/skills/
# Restart Claude Desktop → /ims-enrolment now available

# Option B — download the skill folder only (zip from GitHub)
# Place at ~/.claude/skills/ims-enrolment/
```

After install, in Claude Desktop the skill appears in the skill list and responds to the trigger phrases above.

## Maintenance discipline

Update this skill when:

- Simon publishes a new version of IMS-PRC-AI-001 (or any IMS template change) → update `references/simon-ims-prc-ai-001-v0.4.md`
- A new ISO clause requirement emerges → update `references/seven-section-template.md`
- The AI Department adds a new sub-process → add example to `examples/ai-department/`
- A department completes enrolment and finds a gap in the templates or prompts → update the relevant template/prompt

Use `/skill-create` (if updating structure) or direct edits (for content). After edits, re-export to the repo:

```bash
cp -r ~/.claude/skills/ims-enrolment/. ~/Documents/janus-puls-onboarding/skills/ims-enrolment/
cd ~/Documents/janus-puls-onboarding
git add skills/ims-enrolment/
git commit -m "skill: update ims-enrolment …"
git push
```

## What replaced the stale files

The two files previously in `03 Projects/` (`PULS-plain-english-tasks.md` and `PULS-response-to-ISO-lead.md`) have been **repurposed** into this skill:

- `PULS-plain-english-tasks.md` → became `references/plain-english-overview.md`
- `PULS-response-to-ISO-lead.md` → was the seed for `examples/ai-department/parent-process.md` (canonical version now lives in the GitHub repo as file 04, copied here for the worked example)

The originals have been deleted from `03 Projects/` — they were stale drafts and the skill bundle now contains the current versions.

## Related

- [[iso-ims-puls]] — entry point for the ISO section
- [[janus-puls-onboarding]] — GitHub repo with the canonical 11 procedural docs (+ now this skill in `skills/`)
- [[ims-process-documents]] — the full list of documents this skill helps produce
- [[ims-process-owners-map]] — who owns what, which departments need to enrol

← Back to [[iso-ims-puls]]
