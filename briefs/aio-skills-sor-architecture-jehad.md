---
type: brief
title: AIO Skills + Systems-of-Record architecture (Jehad's view)
slug: aio-skills-sor-architecture-jehad
created: 2026-05-04
updated: 2026-05-12
departments: [ai-office]
confidence: medium
status: active
sources: [2026-05-11-aio-standup-with-jehad]
related: [standup, ai-registry, ai-tool-evaluation, linear, monday, notion, fireflies, jehad-altoutou, aio-playbooks-jehad, peer-to-peer-mesh-federation-pattern]
audience: [department]
captured_by: jehad-altoutou
---

# AIO Skills + Systems-of-Record architecture (Jehad's view)

Federated from Jehad's personal vault as a synthesis-level reference. Captures how the four Janus operational skills connect, what flows where, and which system owns each piece of state — written from the perspective of the skill's owner.

## Source-of-truth table

| Domain | Owning system | Owning skill |
|---|---|---|
| Daily standup transcripts | [[fireflies]] | n/a (read-only by skills) |
| Standup logs, decisions, next-step plans | [[notion]] (Operations Notebook) | [[standup|/standup]] |
| Tasks / projects / automations / action tracking | [[monday]] (Automations board `5095012818`) | [[standup|/standup]] |
| Recruitment + leave management dashboard | [[monday]] (HR Dashboard `5095636727`) | HR team (operational) |
| AI tool registry — descriptions, cost, tier, departments, evaluations | [[linear]] (AI Registry team) | [[ai-registry|/ai-registry]] |
| AI tool gate evaluations (Gate 1–4 comments) | [[linear]] (AIR comments) | [[ai-tool-evaluation|/ai-tool-evaluation]] |
| AI Projects (implementation initiatives) | [[linear]] (AIP team) | reconciled by [[standup|/standup]] each run |
| Assessify platform state (assessments, questions, invites) | Assessify SaaS | `/assessify-hr` |
| AI Tools Registry on [[monday]] (deprecated) | [[monday]] (board `5095577150`) | none — historical reference |

## Daily flow (the [[standup|/standup]] orchestration)

```
Fireflies raw transcript  ◄── canonical (Fireflies' own summary is unreliable)
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

[[standup|/standup]] is the only skill that runs against the daily transcript. It never invokes sibling skills via the Skill tool from within its own context (that would cause instruction collisions). Instead, it dispatches **isolated subagents** via the Task/Agent tool — each subagent forks a clean context, loads the relevant sibling skill, executes, and returns one structured JSON object.

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

`/assessify-hr` is **not** orchestrated by [[standup|/standup]] — it's a peer skill the user invokes directly when working on the Assessify platform. The standup might trigger assessify work via a Monday task, but it doesn't dispatch the skill.

## Subagent dispatch contract (between [[standup|/standup]] and [[ai-registry|/ai-registry]] / [[ai-tool-evaluation|/ai-tool-evaluation]])

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

`monday_task_required.required` MUST be a real boolean. `/standup` validates the JSON, retries once with stricter instruction on failure, falls back to logging under Subagent Failures if the retry also fails.

## Read-vs-write matrix

|  | Fireflies | Monday Automations | Monday HR Dashboard | Linear AIR | Linear AIP | Notion | Assessify |
|---|---|---|---|---|---|---|---|
| [[standup|/standup]] | read | read + write | read only | — (subagent) | read + write (reconcile) | read + write | — |
| [[ai-registry|/ai-registry]] | — | — | — | read + write | — | — | — |
| [[ai-tool-evaluation|/ai-tool-evaluation]] | — | — | — | comment | — | — | — |
| `/assessify-hr` | — | — | — | — | — | — | read + write |

## Why Linear AIR (not Monday) for tool registry

Resolved during the AIO 1 May 2026 standup. Linear AIR is the source of truth because:

- The registry has a complex lifecycle (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected) that maps natively to Linear states.
- [[ai-registry|/ai-registry]] and [[ai-tool-evaluation|/ai-tool-evaluation]] already invest in Linear-side conventions (description schema, label taxonomy, gate-comment patterns).
- Mirroring on Monday created Monday/Linear duplication-sync issues that were hard to keep clean.
- The Monday AI Tools Registry board is retained for historical reference only.

## Notion size hygiene (v3.9)

Notion's Operations Notebook is bounded:

- Master page kept under 80 KB
- Recent 14 days of standup entries at full content
- Older entries auto-archive to monthly child pages (`Standup Log Archive — <Month YYYY>`)
- Notion API failures fall back to file outputs; never block successful Monday writes

See Step 5A.1 / 5F in the [[standup|/standup]] SKILL.md for the algorithm.

## Recurring-blocker pattern

If the same action item appears in two consecutive standups (e.g., "Get ISO references from Simon" across 22 Apr → 1 May → 4 May), the standup skill currently posts fresh stubs on the linked Monday item but doesn't auto-detect recurrence. **Manual escalation to the blocker's owner** is the current workaround. Future enhancement under consideration.
