---
type: source
source_type: laptop
title: SKILL
slug: skill-2
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/SKILL.md
original_size: 20980
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Skill source code for /ims-enrolment — distributable internal tooling; work content"
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# SKILL

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/SKILL.md` on 2026-05-14._

---
name: ims-enrolment
description: "Enrol a Janus Digital department or team into the IMS (Integrated Management System) for ISO 9001 / 27001 / 42001 certification. Guides any department head through documenting their work in the [[iso-9001-figure-1|ISO 9001 Figure 1]] schematic — parent process first (how the department functions as a whole), then sub-processes (one per activity). Produces ISO-grade artefacts: parent process document, sub-process documents, First Voice questionnaire, and a handover bundle for Simon (ISO Lead). Use when a department needs to onboard into the IMS programme and has no idea where to start. Trigger phrases: 'enrol [department] into IMS', 'help [team] document their processes for ISO', 'IMS onboarding for [department]'. Two purposes: (1) provide complete understanding of the IMS programme, (2) guide the department through documentation. AI Department is the worked example shipped with the skill."
---

# Skill: [[ims-enrolment|IMS Enrolment]] — Department Onboarding into ISO Programme

**Version:** 1.4
**Owner:** Jehad — AI Operations Engineer, Janus Digital
**Last Updated:** 2026-05-11
**Scope:** End-to-end onboarding of any Janus department into the IMS for ISO 9001:2015 / ISO/IEC 27001:2022 / ISO/IEC 42001:2023 certification under the PULS programme. Produces ISO 9001 Figure 1-compliant documentation for one department: parent process + sub-processes + First Voice + handover bundle.

---

## Core Principle

```
Department-level enrolment runs top-down:
1. PARENT process   — how the department functions as a whole
2. SUB-processes    — one document per activity from the parent
3. FIRST VOICE      — the 6-question form for each person in the department
4. HANDOVER         — Word doc bundle ready for Simon (ISO Lead) to review

Same ISO 9001 Figure 1 schematic at both levels.
Same 7 sections (per slide 9 of Simon's deck) in every document.
AI Department is the worked example — use it when others say "I don't get it".
```

This skill **never writes to [[linear|Linear]] AIR or the Monday [[ai-tools-registry|AI Tools Registry]]**. Output artefacts are markdown + Word docs handed to Simon and the department head.

---

## When to use

Trigger phrases:

- *"Enrol [Department name] into the IMS"*
- *"Help [team] document their processes for ISO"*
- *"IMS onboarding for [Department]"*
- *"I'm a department head, where do I start with this ISO thing?"*

Do **not** use this skill for:
- Documenting a single tool or feature (use the standard development workflow instead)
- AI tool evaluation specifically (use `/ai-registry` + `/ai-tool-evaluation`)
- Updating an already-enrolled department's process (use `/brain update` for incremental changes)

---

## Two purposes

| Purpose | What the skill does |
|---|---|
| **Foundation** | Gives the department head a complete understanding of the IMS / PULS / ISO programme before they touch any document. Pulls from `references/` |
| **Guidance** | Walks the department through producing ISO-grade documentation by interview, using the templates in `templates/` and the AI Department worked example in `examples/ai-department/` |

The skill assumes the department head **has not read Simon's deck** and may have **no compliance background**. It explains everything in plain English first, then escalates to ISO vocabulary as needed.

---

## Skill boundaries

This skill is **not**:

- The IMS itself (that's the 20 process documents in Notion, written collectively)
- A replacement for Simon's authority (he is the ISO Lead — this skill produces drafts for his review)
- An audit-readiness tool (PULS handles that)
- A general project-management skill (use `/standup` for that)

This skill **produces drafts** that Simon then formalises into the official IMS-PRC-XXX-NNN process documents.

---

## Execution Model — 5 Phases

The skill runs in five strict phases. Each phase has clear entry/exit criteria.

### Phase 0 — Self-verify (runs automatically on every invocation)

**EXECUTE THIS FIRST, before any other phase. Use the Bash tool.**

Run the install verifier:

```bash
bash ~/Documents/janus-puls-onboarding/install.sh --check 2>&1
```

Parse the output:

- If output contains both `✓ Skill installed` AND `✓ pandoc available` → **verification passed, proceed silently to Phase 1**
- If output contains `✗ Skill not installed` → offer to run `bash ~/Documents/janus-puls-onboarding/install.sh` (full install) before continuing. Do NOT proceed to Phase 1 until install succeeds.
- If output contains `⚠ pandoc not installed` → warn the user that Phase 5c (Word doc export) will fail, propose `brew install pandoc` (macOS) or `sudo apt install pandoc` (Linux), but allow Phases 1-5b to continue.
- If the Bash command fails (script not found) → tell the user the install script is missing, propose cloning the repo: `git clone https://[[github|github]].com/Jehada-Janusd/janus-puls-onboarding.git ~/Documents/janus-puls-onboarding` then re-run Phase 0.

**Resume detection:** also check for an existing enrolment in progress:

```bash
ls ~/Desktop/*\ -\ IMS\ Enrolment/ 2>/dev/null | head
```

If a department folder with a `state.json` file is found, ask the user whether they want to **resume** that enrolment (skip back to the relevant phase) or **start fresh** (overwrite or create a new folder with `-v2` suffix). See "Resume mechanism" below.

**Required files manifest:** the install verifier checks all 22 required files (`SKILL.md`, `INSTALL.md`, 5 references, 5 templates, 2 prompts, 8 AI Dept examples, 1 first-voice prompt). The script is the source of truth — do not duplicate the list here.

#### Slug generation rule

When generating filenames for sub-processes, diagram prompts, or output folders, derive the slug deterministically from the human-readable name:

1. Lowercase
2. Replace spaces with `-`
3. Strip all characters except `a-z`, `0-9`, `-`
4. Collapse multiple consecutive `-` into one
5. Trim leading/trailing `-`
6. Truncate to 40 chars

Examples:

| Activity name | Slug |
|---|---|
| Talent Acquisition | `talent-acquisition` |
| Meeting → Task → Build | `meeting-task-build` |
| Approve & Release | `approve-release` |
| New Hire Onboarding (US/UK) | `new-hire-onboarding-us-uk` |

Use the slug consistently across all output filenames (`sub-process-<slug>.md`, `diagram-prompt-<slug>.md`, `diagrams/<slug>.png`).

#### Resume mechanism

Each Desktop output folder contains `state.json` capturing progress:

```json
{
  "department_name": "HR",
  "department_slug": "hr",
  "phase_completed": 2,
  "parent_activities": [
    {"name": "Talent Acquisition", "slug": "talent-acquisition", "sub_process_done": true},
    {"name": "Onboarding", "slug": "onboarding", "sub_process_done": false}
  ],
  "people_filled_first_voice": ["jane-doe"],
  "last_updated": "2026-05-11T15:30:00Z"
}
```

Write `state.json` at the end of each phase. On Phase 0 resume detection, read `state.json` and skip to the first incomplete phase.

---

### Phase 1 — Foundation (read-only)

- Confirm the department head's prior context: have they read Simon's deck? Have they seen the IMS / PULS overview?
- If not: walk them through `references/plain-english-overview.md` (5 minutes), then `references/iso-9001-figure-1.md` (2 minutes), then `references/seven-section-template.md` (3 minutes)
- Show them `examples/ai-department/parent-process.md` as the worked example
- **Exit criterion:** Department head can answer in their own words: "What is PULS? What goes inside each IMS process document? Why does my department need to do this?"

### Phase 2 — Parent process definition (interview)

- Run the parent-process interview from `prompts/interview-department-head.md`
- The interview elicits the 7 ISO 9001 Figure 1 sections for the department as a whole:
  1. Sources of inputs (who/what triggers your department's work)
  2. Inputs (data, requests, scheduled events)
  3. Activities (the major things your department does — this list seeds Phase 3)
  4. Outputs (what your department produces)
  5. Receivers of outputs (who consumes your outputs)
  6. Controls and check points (quality gates)
  7. Resources (people, tools, knowledge, budget)
- Populate `templates/parent-department-process.md` with the answers
- **Exit criterion:** Parent process document is complete and the department head signs off on it. The Activities list is the input to Phase 3.

### Phase 3 — Sub-process definition (one per activity, interview each)

- For each activity from Phase 2's list, run the sub-process interview from `prompts/interview-activity-owner.md`
- Same 7-section structure — but scoped to **one activity within the department**
- Populate one copy of `templates/sub-process.md` per activity
- **Exit criterion:** One sub-process document per activity exists, each signed off by the activity owner (who may or may not be the department head)

### Phase 4 — First Voice (per person)

Run the First Voice interview from `prompts/interview-first-voice.md`. Two delivery modes:

**Mode A — Live interview** (default for departments ≤ 5 people):

- Open `prompts/interview-first-voice.md` and follow the 6-question script with each person individually
- Pre-populate `[PERSON NAME]`, `[ROLE]`, `[DEPARTMENT]`, `[MANAGER]` from the parent process Resources section
- Save each completed form as `first-voice-<person-slug>.md` in the Desktop folder
- Time: ~15-20 min per person

**Mode B — Async distribution** (for departments > 5 people):

- Generate one blank form per person on the parent process people list
- Save all forms to the Desktop folder
- Generate a cover note for the department head to distribute via Slack/email (template in `prompts/interview-first-voice.md`)
- Department head paste-collects responses asynchronously, then re-engages the skill at Phase 5

**Tooling note:** During Q3 (Tools & systems), remind every person they do **NOT** add anything to Linear AIR themselves. The AI department maintains AIR; departments only list the tools they use.

**Exit criterion:** One First Voice form per department member, all saved in the Desktop folder.

### Phase 5 — Handover (Desktop bundle + diagram prompts + Word docs)

**5a — Create the Desktop output folder:**

- Output base: `~/Desktop/<Department> - IMS Enrolment/` (e.g., `~/Desktop/HR - IMS Enrolment/`)
- The folder name uses title case + space-dash-space separator so any team member can find it on the Desktop without knowing internal paths
- Inside the folder: create `diagrams/` and `exports/` subdirectories
- Move all process documents from any temp working location into this folder
- **Auto-generate a `README.md` inside the folder** that lists what each file is and what to do with it

**5b — Generate diagram prompts (one per process doc):**

For each `parent-process.md` and every `sub-process-*.md`:

1. Read the answered process document from the Desktop folder
2. Open `templates/diagram-prompt.md`
3. **Fill in each `[PLACEHOLDER]` verbatim from the source document:**
   - `[PROCESS TITLE]` ← from the document title at the top
   - `[SUBTITLE]` ← derived (e.g., *"ISO 9001 Figure 1 schematic · [N] activities"*)
   - `[CONTROLS LIST]` ← Section 7 bullets, one per line
   - `[SOURCES LIST]` ← Section 2 bullets
   - `[INPUTS LIST]` ← Section 3 bullets
   - `[ACTIVITIES LIST]` ← Section 4 numbered list, each with its 1-line description
   - `[OUTPUTS LIST]` ← Section 5 bullets
   - `[RECEIVERS LIST]` ← Section 6 bullets
   - `[RESOURCES LIST]` ← Section 8 bullets (split by category if structured)
   - `[KPI LIST]` ← Section 9 KPIs (use proposed KPIs if no formal ones defined)
   - `[PROCESS OWNER NAME]` ← from document header
   - `[ISO CLAUSE FOOTER]` ← from header's "Related ISO clauses" line, formatted as: `"ISO 9001 §X.X · ISO 27001 §X.X · ISO 42001 §X.X — [one-sentence relevance]"`
4. Save as `diagram-prompt-parent-process.md` or `diagram-prompt-<activity-slug>.md` in the Desktop folder
5. **Verify no `[PLACEHOLDER]` markers remain** in the saved file — if any do, you missed filling something in
6. The department then pastes the resulting prompt into ChatGPT (GPT-5 or GPT-4o with image gen) to generate a polished PNG/SVG
7. Generated images are saved to `diagrams/<activity-slug>.png` (or `parent-process.png` for the parent)

See `examples/ai-department/diagram-prompt-*.md` for four worked examples of fully-filled prompts.

**5c — Generate Word doc bundle:**

- Generate a Word doc bundle using `templates/handover-to-simon.md` as the cover note
- Include: parent process + all sub-process documents + all First Voice forms + all diagram prompts + generated PNG/SVG images if available
- Use pandoc: `pandoc <file>.md -o exports/<file>.docx`
- The single combined doc lives at `exports/HANDOVER-BUNDLE.docx`
- Department head sends to Simon for IMS-PRC-XXX-NNN code assignment and integration
- **Exit criterion:** Simon acknowledges receipt; the bundle enters Simon's formal IMS document pipeline

#### Auto-generated README manifest (Phase 5a)

The skill writes a `README.md` at the root of the Desktop folder explaining the contents so any team member can navigate it without context:

```markdown
# <Department> - IMS Enrolment

Generated by /ims-enrolment skill on <YYYY-MM-DD>.

## What's here
- `parent-process.md` — Your whole department in the ISO 9001 Figure 1 shape
- `sub-process-*.md` — One per major activity from the parent (you produced [N] of these)
- `diagram-prompt-*.md` — Paste into ChatGPT for polished diagrams → save to `diagrams/`
- `first-voice-*.md` — One per person in the department
- `handover-to-simon.md` — Cover note when you send this bundle to Simon (ISO Lead)
- `diagrams/` — PNG/SVG images generated from the ChatGPT prompts
- `exports/` — Word doc versions + single `HANDOVER-BUNDLE.docx` for Simon

## What to do next
1. Open each diagram-prompt-*.md, paste prompt into ChatGPT, save image to `diagrams/`
2. Finalise `handover-to-simon.md`
3. Run pandoc to produce `exports/*.docx`
4. Email `exports/HANDOVER-BUNDLE.docx` (with embedded diagrams) to Simon
5. Wait for Simon's review, iterate, ship to formal IMS document set
```

---

## Quick-start (compact mode)

For experienced department heads who have read the deck and know what they're doing:

1. Skip Phase 1
2. Direct interview through Phases 2 + 3 (no example walkthrough)
3. Skip Phase 4 if the department is one person
4. Generate handover bundle and exit

Trigger: department head says *"I've read the deck, just walk me through the documentation"*

---

## References (in `references/`)

| File | Purpose | When to read it |
|---|---|---|
| `plain-english-overview.md` | What the IMS / PULS / ISO programme is, in non-technical language | Phase 1 if department head is new to ISO |
| `iso-9001-figure-1.md` | The schematic shape every process document follows | Phase 1, before Phase 2 starts |
| `seven-section-template.md` | What goes inside each of the 7 sections of a process document | Phase 1 + Phase 2 reference |
| `jargon-decoder.md` | Every buzzword in Simon's deck translated | Anytime during the run |
| `simon-ims-prc-ai-001-v0.4.md` | Simon's IMS-PRC-AI-001 v0.4 in summary form (formal template structure) | Phase 5 alignment if Simon's vocabulary is needed |

---

## Templates (in `templates/`)

| File | Purpose |
|---|---|
| `parent-department-process.md` | Blank parent-process document — fill in during Phase 2 |
| `sub-process.md` | Blank sub-process document — one copy per activity, fill in during Phase 3 |
| `first-voice-questionnaire.md` | The 6-question form — one copy per person, fill in during Phase 4 |
| `diagram-prompt.md` | Parametric ChatGPT prompt — one copy per process doc, fill in during Phase 5a from the answered process doc. Department pastes into ChatGPT for a polished diagram image. |
| `handover-to-simon.md` | Cover note for the handover bundle — used in Phase 5b |

---

## Examples (in `examples/`)

| Example department | Files |
|---|---|
| `ai-department/` | Fully documented Janus AI Department — parent process + 3 sub-processes (Meeting → Task → Build, Tool Evaluation, Platform Development), each with its own filled-in diagram prompt. Use as the reference when other departments say *"I don't get it."* |

---

## Prompts (in `prompts/`)

| File | Purpose |
|---|---|
| `interview-department-head.md` | Guided question script for Phase 2 — extract the 7 sections of the parent process |
| `interview-activity-owner.md` | Guided question script for Phase 3 — extract the 7 sections of one sub-process |
| `interview-first-voice.md` | Guided question script for Phase 4 — 6-question First Voice interview, supports Mode A (live) and Mode B (async distribution) |

---

## Output artefacts (per department enrolment)

After a successful run, the department has a folder on the **Desktop** so anyone can find it without digging through file paths:

```
~/Desktop/<Department> - IMS Enrolment/
├── README.md                                  ← Auto-generated manifest explaining the folder
├── parent-process.md                          ← The whole department in ISO 9001 Figure 1 shape
├── sub-process-<activity-1>.md                ← One per activity
├── sub-process-<activity-N>.md
├── diagram-prompt-parent-process.md           ← ChatGPT prompt for the parent diagram
├── diagram-prompt-<activity-1>.md             ← ChatGPT prompt per sub-process diagram
├── diagram-prompt-<activity-N>.md
├── first-voice-<person-1>.md                  ← One per department member
├── first-voice-<person-N>.md
├── handover-to-simon.md                       ← Cover note to Simon
├── diagrams/                                  ← Generated PNG/SVG images (after pasting prompts into ChatGPT)
│   ├── parent-process.png
│   └── <activity>.png (×N)
└── exports/                                   ← Word doc bundle (after pandoc)
    ├── parent-process.docx
    ├── sub-process-<activity>.docx (×N)
    ├── first-voice-<person>.docx (×N)
    └── HANDOVER-BUNDLE.docx                    ← Single combined doc for Simon (embeds diagrams if generated)
```

**Where to find it:** the folder appears on the Desktop with a clear, self-explanatory name (`HR - IMS Enrolment`, `Finance - IMS Enrolment`, etc.). Other team members can locate it without needing to know any file paths.

**Department-name convention:** title case with a space-dash-space separator. Examples:

- `AI Department - IMS Enrolment`
- `HR - IMS Enrolment`
- `Talent Acquisition - IMS Enrolment`
- `Finance - IMS Enrolment`

**Optional secondary copies:**

- Backup in `~/Documents/janus-puls-onboarding/department-enrolments/<department>/` (for version control via git)
- [[obsidian|Obsidian]] mirror at `07 [[iso-ims-puls|ISO IMS PULS]]/Department Enrolments/<department>/` (for in-vault navigation)

These are optional — the Desktop folder is the canonical user-facing location.

---

## How a department head invokes this skill

```
User opens Claude Desktop, types:
  /ims-enrolment

Or:
  Help the HR team enrol into the IMS

Or:
  I'm the Finance lead, I need to document our processes for ISO

The skill responds with Phase 1 — Foundation, beginning with:
  "Welcome. Let's enrol the [Department] into the IMS.
   Before we start, three quick questions to set the right pace:
   1. Have you read Simon's IMS Development Programme deck?
   2. Have you seen the ISO 9001 Figure 1 schematic (slide 8)?
   3. How many sub-activities does your department have, roughly?

   Whatever your answers, I'll meet you where you are."
```

The skill then proceeds through Phases 1-5 in order, pausing at each phase boundary for the department head to review and confirm.

---

## Connection to the rest of Janus's IMS programme

- **Source of truth for IMS structure:** Simon's IMS-PRC-AI-001 v0.4 (in `references/`)
- **Source of truth for what's been built:** GitHub repo at `https://github.com/Jehada-Janusd/janus-puls-onboarding`
- **Conceptual navigation:** Obsidian Vault `07 ISO IMS PULS/`
- **Related skills:**
  - `/standup` v3.11 — used inside the AI Department's Meeting → Task → Build sub-process
  - `/ai-registry` + `/ai-tool-evaluation` — used inside the Tool Evaluation sub-process
  - `/brain` — used to maintain Obsidian project notes through the enrolment

---

## Maintenance

Update this skill when:

- Simon publishes a new version of IMS-PRC-AI-001 (or any IMS template change)
- A new ISO clause requirement emerges
- A department completes enrolment and identifies a gap in the templates or prompts
- The seven-section schema changes (it shouldn't, but if Simon updates it, update `seven-section-template.md`)

---

## British English

All artefacts produced by this skill use British English spelling (`enrolment`, `behaviour`, `organisation`, `centralise`, etc.) — consistent with Janus's conventions and Simon's documents.
