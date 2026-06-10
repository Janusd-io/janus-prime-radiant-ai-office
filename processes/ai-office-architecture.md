---
type: process
title: AI Office Architecture
slug: ai-office-architecture
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
confidence: medium
migrated_from: personal-obsidian-vault (AI Office Brain)
related: [platform-development-process, meeting-to-task-workflow, ai-registry, standup, organisational-digital-twin]
---

# AI Office Architecture

_How the AI Office's knowledge & systems are architected. Migrated 2026-06-09 from the personal-vault 'AI Office Brain' base (an earlier parallel knowledge base); canonical detail also lives across the vault's vendor/process pages._

# Architecture — Skills + Systems of Record

How the four Janus operational skills connect, what flows where, and which system owns each piece of state.

## Source-of-truth table

| Domain | Owning system | Owning skill |
|---|---|---|
| Daily standup transcripts | Fireflies | n/a (read-only by skills) |
| Standup logs, decisions, next-step plans | [[notion]] | [[standup]] |
| Tasks / projects / automations / action tracking | [[monday]] (board `5095012818`) | [[standup]] |
| Recruitment + leave management dashboard | [[monday]] (board `5095636727`) | HR team (operational) |
| AI tool registry — descriptions, cost, tier, departments, evaluations | [[ai-registry]] | [[ai-registry]] |
| AI tool gate evaluations (Gate 1–4 comments) | [[ai-registry]] (comments) | [[ai-tool-evaluation]] |
| AI Projects (implementation initiatives) | [[linear]] | reconciled by [[standup]] each run |
| Assessify platform state (assessments, questions, invites) | Assessify SaaS | [[assessify]] |
| AI Tools Registry on Monday (deprecated) | [[monday]] | none — historical reference |

## Daily flow (the [[standup]] orchestration)

```
Fireflies raw transcript  ◄── canonical
        │
        ▼
  Meeting Intelligence Digest (Phase 1, read-only)
        │
        ▼
  Notion idempotency check ─── ask user if today's entry exists
        │
        ▼
  Match + duplicate-detect + parent-route ── confidence scoring ──┐
        │                                                         │
        ▼                                                         ▼
  Subagent Dispatch Gate (drop low-signal mentions)      Ask user (60–84%)
        │
        ▼
  Execution Plan (Phase 2, read-only)
        │
        ▼
  Execution Control Mode check ── if large/ambiguous → wait for "Approve execution"
        │
        ▼
  Phase 3 — strict priority order
        ├── (1) Monday Automations writes
        ├── (2) No-orphan next-step pass
        ├── (3) Subagent dispatch ─►  /ai-registry, /ai-tool-evaluation
        │                              (forked context, JSON I/O)
        ├── (4) Linear AIP reconciliation (with Conflict Safety)
        ├── (5) Notion journal entry (size-checked, archival-triggered if needed)
        └── (6) Final Execution Report (incl. Subagent Failures + AIP Conflicts)
```

## Skill orchestration rules

[[standup]] is the only skill that runs against the daily transcript. It never invokes sibling skills via the `Skill` tool from within its own context (that would cause instruction collisions). Instead, it dispatches **isolated subagents** via the Task/Agent tool — each subagent forks a clean context, loads the relevant sibling skill, executes, and returns one structured JSON object.

```
                  ┌──────────────────────┐
                  │      /standup        │
                  │  (orchestrator only) │
                  └────────┬─────────────┘
                           │ Task/Agent dispatch
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌──────────────┐ ┌────────────┐ ┌────────────┐
     │ /ai-registry │ │ /ai-tool-  │ │ /assessify │
     │              │ │ evaluation │ │  -hr       │
     └──────┬───────┘ └─────┬──────┘ └─────┬──────┘
            │               │              │
            ▼               ▼              ▼
       Linear AIR      Linear AIR      Assessify
       (writes)        (comments)      SaaS
```

[[assessify]] is **not** orchestrated by [[standup]] — it's a peer skill the user invokes directly when working on the Assessify platform. The standup might *trigger* assessify work via a Monday task, but it doesn't dispatch the skill.

## Subagent dispatch contract (between [[standup]] and [[ai-registry]] / [[ai-tool-evaluation]])

**Hand-off package** (sent to subagent):
```json
{
  "target_skill": "/ai-registry | /ai-tool-evaluation",
  "tool_name": "",
  "air_id": "AIR-N or new",
  "standup_date": "AIO DD Mon YYYY",
  "transcript_evidence": [{"speaker": "", "excerpt": ""}],
  "decision_or_action_required": "",
  "owner": "",
  "urgency": "by-next-standup | this-week | longer",
  "expected_output": ""
}
```

**Return contract** (subagent → standup):
```json
{
  "action_completed": "",
  "linear_air_issue": "AIR-N",
  "final_status_or_result": "",
  "monday_task_required": {"required": true|false, "task_title": "", "reason": ""},
  "notion_journal_addition": "",
  "unresolved_questions_or_blockers": []
}
```

`monday_task_required.required` MUST be a real boolean (`true` or `false`). `/standup` validates the JSON, retries once with stricter instruction on failure, falls back to logging under Subagent Failures if the retry also fails.

## Read-vs-write matrix

|  | Fireflies | Monday Automations | Monday HR Dashboard | Monday Tools Registry | Linear AIR | Linear AIP | Notion | Assessify |
|---|---|---|---|---|---|---|---|---|
| [[standup]] | read | read + write | read only | — (deprecated) | — (subagent) | read + write (reconcile) | read + write | — |
| [[ai-registry]] | — | — | — | — | read + write | — | — | — |
| [[ai-tool-evaluation]] | — | — | — | — | comment | — | — | — |
| [[assessify]] | — | — | — | — | — | — | — | read + write |

## Why Linear AIR (not Monday) for tool registry?

Resolved during the AIO 1 May 2026 standup. Linear AIR is the source of truth because:
- The registry has a complex lifecycle (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected) that maps natively to Linear states.
- [[ai-registry]] and [[ai-tool-evaluation]] already invest in Linear-side conventions (description schema, label taxonomy, gate-comment patterns).
- Mirroring on Monday created Monday/Linear duplication-sync issues that were hard to keep clean.
- The Monday AI Tools Registry board is retained for historical reference only — see [[monday]].

## Notion size hygiene (v3.9)

Notion's Operations Notebook is bounded:
- Master page kept under 80KB
- Recent 14 days of standup entries at full content
- Older entries auto-archive to monthly child pages (`Standup Log Archive — <Month YYYY>`)
- Notion API failures fall back to file outputs; never block successful Monday writes

See Step 5A.1 / 5F in the [[standup]] SKILL.md for the algorithm.

## Recurring-blocker pattern

If the same action item appears in two consecutive standups (e.g., "Get ISO references from Simon" across 22 Apr → 1 May → 4 May), the standup skill currently posts fresh stubs on the linked Monday item but doesn't auto-detect recurrence. **Manual escalation to the blocker's owner** is the current workaround. Future enhancement under consideration.

---

## Original overview (ex-AI Office Brain MOC)

# AI Office — Map of Content

Entry point for the AI Office brain. Click any link to dive in.

## The orchestrator

[[standup]] — the central skill. Runs daily after the AIO standup meeting. Pulls the Fireflies transcript, matches what was said to existing work on Monday, dispatches subagents to specialist skills, reconciles Linear AIP, writes the journal entry to Notion, emits a Final Execution Report. **Source of truth for the daily AI Office workflow.**

## The specialist skills (orchestrated by [[standup]])

- [[ai-registry]] — manages Linear AIR (the registry of every AI/SaaS tool the company uses). Adds new tools, enriches metadata, moves tools through the lifecycle, regenerates derivative views (Slack Canvas, Excel workbook).
- [[ai-tool-evaluation]] — runs the formal Gate 1–4 evaluation framework on individual tools. Posts gate-decision comments on Linear AIR issues. Complements [[ai-registry]].
- [[assessify]] — drives the Assessify HR platform: assessments, questions, candidate invites, departments, competencies, job roles.

## Systems of record (where the data actually lives)

- [[monday]] — board `5095012818`. Tasks, automations, projects, action items, sub-items. **Where day-to-day work runs.**
- [[monday]] — board `5095636727`. Recruitment pipeline + leave management.
- [[monday]] — board `5095577150`. **Deprecated.** Historical reference only.
- [[ai-registry]] — AI Registry team. Source of truth for AI tool descriptions, costs, tier, evaluations.
- [[linear]] — AI Projects team. Implementation initiatives. Reconciled against [[monday]] in every standup.
- [[notion]] — standup journal, decisions, next-step plans.
- [[fireflies]] — transcripts. Canonical source for everything — the [[standup]] skill builds its Meeting Intelligence Digest from raw transcripts.

## How they fit together

See [[ai-office-architecture]] for the full diagram, the source-of-truth table, and the orchestration flow. Short version: [[standup]] is the only skill that runs against the daily transcript; everything else is invoked as a subagent or operates on its own surface.

## Common workflows

See [[ai-office-playbooks]] for step-by-step playbooks:
- Post-standup processing (the daily flow)
- Adding a new AI tool to the registry
- Running a Gate 1 evaluation on a tool
- Inviting a candidate via Assessify
- Reconciling Linear AIP drift
- Cleaning up the Notion notebook when it gets too large

## Quick links

- [Monday — Automations](https://janusd-company.monday.com/boards/5095012818)
- [Monday — HR Dashboard](https://janusd-company.monday.com/boards/5095636727)
- [Notion — Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a)
- [Linear](https://linear.app/janusd)
- [Fireflies](https://app.fireflies.ai)

## Skill ownership

| Skill | Owner | Domain |
|---|---|---|
| [[standup]] | Jehad Altoutou | Orchestrator + standup workflow |
| [[ai-registry]] | AI Office | Linear AIR CRUD + derivative views |
| [[ai-tool-evaluation]] | AI Office | Gate 1–4 evaluation methodology |
| [[assessify]] | HR + AI Office | Assessify platform driver |

---

## README (ex-AI Office Brain)

# AI Office Brain — README

This folder is an Obsidian-compatible knowledge base for Janus Digital's AI Office team. It documents the four operational skills (`/standup`, `/ai-registry`, `/ai-tool-evaluation`, `/assessify-hr`), the systems they touch (Monday, Linear, Notion, Fireflies, Assessify), and the playbooks for the work that runs through them.

## How to import into Obsidian

1. Drag this `AI-Office-Brain/` folder into your Obsidian vault root, or copy it to an existing sub-folder.
2. Open Obsidian → switch to this vault → start at [[ai-office-architecture]].
3. Internal `wiki-links` resolve automatically. External URLs (Monday, Linear, Notion, Fireflies) are plain markdown links and will open in a browser.

## Folder structure

```
AI-Office-Brain/
├── 00 — MOC.md                          ← Map of Content (start here)
├── 01 — Architecture.md                 ← How skills connect; source-of-truth table; system diagram
├── 02 — Playbooks.md                    ← Common workflows step-by-step
├── Skills/
│   ├── standup.md                       ← /standup orchestrator
│   ├── ai-registry.md                   ← /ai-registry registry engine
│   ├── ai-tool-evaluation.md            ← /ai-tool-evaluation Gate 1–4 framework
│   └── assessify-hr.md                  ← /assessify-hr platform driver
└── Systems-of-Record/
    ├── Monday-Automations.md            ← Board 5095012818 (tasks/projects)
    ├── Monday-AI-Tools-Registry.md      ← Board 5095577150 (deprecated)
    ├── Monday-HR-Dashboard.md           ← Board 5095636727 (recruitment + leave)
    ├── Linear-AIR.md                    ← AI Registry team (tools)
    ├── Linear-AIP.md                    ← AI Projects team (delivery)
    ├── Notion-Operations-Notebook.md    ← Standup journal
    └── Fireflies.md                     ← Transcripts (canonical source)
```

## Conventions

- **Wiki-links** (`note name`) for cross-references within this brain.
- **External links** in standard markdown — Monday board URLs, Linear issue URLs, Notion page URLs, Fireflies transcript URLs.
- **Tags** at the top of each note (`#skill`, `#system-of-record`, `#playbook`) for Obsidian's tag pane.
- British English. USD costs. `DD Mon YYYY` dates.
- This brain is generated and maintained as part of `/standup` workflow updates; it should be regenerated whenever any of the source SKILL.md files change materially.

## Last regenerated

2026-05-04 — covers standup skill v3.9.

Sources:
- [SKILL.md v3.9](file:./outputs/SKILL.md) (in your outputs folder)
- [Monday — Automations](https://janusd-company.monday.com/boards/5095012818)
- [Monday — AI Tools Registry (deprecated)](https://janusd-company.monday.com/boards/5095577150)
- [Monday — HR Dashboard](https://janusd-company.monday.com/boards/5095636727)
- [Notion Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a)
