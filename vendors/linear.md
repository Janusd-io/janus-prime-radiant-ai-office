---
type: vendor
title: Linear
slug: linear
air_id: AIR-36
status: Sandbox
labels: [AI Policy, Technology, Functional]
departments: [ai-office, engineering]
url: https://linear.app/janusd/issue/AIR-36/linear
created: 2026-02-25
updated: 2026-06-09
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
confidence: high
sources: [2026-05-11-aio-standup-with-jehad]
related: [michael-bruck, jehad-altoutou, janus-prime-radiant-build, aio-skills-sor-architecture-jehad, ai-tool-evaluation, 2026-05-06-backlog-cleanup-no-return-to-backlog]
migrated_from: entities/vendors/linear.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Linear

> AI Registry entry [AIR-36](https://linear.app/janusd/issue/AIR-36/linear) — status **Sandbox** as of 2026-04-06. Departments: —.

**Category:** Product Management / Issue Tracking
**Cost per User/Month:** Free (individual); $8 (Standard, per seat); Custom (Plus/Enterprise)
**Departments:** Technology, AI Policy

## Overview

Modern PM/issue tracking platform for software teams. Emphasises speed, keyboard-first navigation, streamlined workflow. PM backbone for AI Office — hosts AI Registry (tool tracking) and AI Projects (internal initiatives). Also Technology team's primary issue tracker.

## Capabilities

* Issue tracking with statuses, priorities, labels, due dates
* Projects, milestones, cycles, roadmaps
* Customisable status workflows per team (Backlog → Evaluating → Sandbox → Production)
* Views and filters
* Keyboard-first design
* GraphQL API + webhooks
* MCP integration for [[claude|Claude]]
* Built-in documents

## Security & Compliance

* SOC 2 Type II, GDPR
* SSO/SAML on Plus and Enterprise
* AES-256 at rest, TLS in transit
* Role-based access control
* Audit logging, full data export

## Relevance

Central to AI Office operations. AI Registry project (one issue per tool, custom workflow statuses) tracks every AI tool. AI Projects tracks internal initiatives. MCP integration means programmatic management through Claude.

*Sandbox. Functional tier. Core tool for AI Office and Technology.*

## Merged from `entities/vendors/linear.md`

# Linear

Issue tracker. At Janus, two teams are in active use:

- **Linear AIR** (AI Registry team) — sole source of truth for the **AI Tools Registry**. Tools move through Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected/Duplicate stages here. Managed *only* via the `/ai-registry` and `/ai-tool-evaluation` skills via subagent dispatch — never written to from `/standup` or directly from this wiki.
- **Linear AIP** (AI Projects team) — status surface for AI Projects, reconciled from Monday execution. Lower-priority for wiki ingest.

## Scope at Janus

Currently scoped to the AI Tools Registry (AIR) and AI Projects status (AIP). Broader project management has migrated to [[notion]] (Operations Notebook journal) plus Monday Automations board (execution surface). The `ai-registry` and `ai-tool-evaluation` skills both operate against Linear AIR directly.

## Relationship to this wiki

Linear AIR holds **pipeline state** (which stage a tool is in, who's evaluating it, when it changed). This wiki holds the **narrative**: what the tool is, why we're evaluating it, what we've learned, how it compares to alternatives. The two are complementary — wiki entries link out to their Linear AIR issue; Linear comments may surface back as decision/lesson pages here.

Closed Linear issues with substantive resolution comments are an ingest source per `CLAUDE.md` §5.1.

## Pipeline discipline

The AIR pipeline is governed by the [[ai-tool-evaluation]] framework. Once a tool enters evaluation, it never returns to Backlog — see [[2026-05-06-backlog-cleanup-no-return-to-backlog]] for the decision. Post-evaluation states are Sandbox / Production / Monitor / Deprecated / Rejected / Duplicate; returning to Backlog would break the audit trail and invite re-evaluation churn.

## Team identifiers and AIP status UUIDs

From Jehad's federated view ([[aio-skills-sor-architecture-jehad]], 2026-05-11) — operationally load-bearing for any `/standup` or wiki-driven Linear API work:

- **AI Registry (AIR) team UUID:** `598dd614-dce5-4ede-98ef-207f3bdff33c`. Issue prefix `AIR-N`. The team was originally created with the name "AI Office" but issues are prefixed `AIR-N` — the prefix is what matters.
- **AI Projects (AIP) team UUID:** `2d1b5c04-94fd-4087-8e95-a5a7aa244a16`. Issue prefix `AIP-N`.

### AIP status UUIDs

| Status | UUID |
|---|---|
| Backlog | `57d6d704-7a3b-41f9-b936-a7d64252d00a` |
| Planned | `d5ccd469-37b4-4b5b-92d6-21be9f27dc90` |
| In Progress | `210b719c-eb51-4d5f-88fb-dcde85ae9939` |
| Done | `661dd6ca-5d5b-4378-8cb4-f1b0384975dc` |
| Cancelled | `ebfcf4e3-f40e-4599-a2b2-827656299627` |

### AIR pipeline

`Backlog → Evaluating → Sandbox → Production` (or `→ Monitor`); also `→ Deprecated / Rejected / Duplicate`.

### Snapshot of recent AIP issues (May 2026)

- AIP-1 Finance Department API Integration (Planned)
- AIP-13 Speaker diarisation for Fireflies (Backlog)
- AIP-15 Deel API & Developer Platform — Capability Assessment (Planned)
- AIP-16 Town Hall Transcript Processing — Pilot (Planned)
- AIP-17 CEO Dashboard — Global Operations View (Backlog)
- AIP-18 Cross-Department Action Routing (Backlog)
- AIP-19 Invoice Bot v3/v4 (Done)
- AIP-20 HR Employee Form Replacement (Done)
- AIP-21 Assessify — Candidate Assessment Platform (Done — expansion underway, conflict logged)
- AIP-22 Decide n8n hosting (Done)

### AIR snapshot stats (May 2026)

74 active issues. Most recent: **AIR-92 Wispr Flow (Whisper Flow)** — added 1 May 2026 standup; Backlog; Functional + Technology + AI Policy.

## Merged from `entities/vendors/linear.md`

# Linear

Issue tracker. At Janus, two teams are in active use:

- **Linear AIR** (AI Registry team) — sole source of truth for the **AI Tools Registry**. Tools move through Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected/Duplicate stages here. Managed *only* via the `/ai-registry` and `/ai-tool-evaluation` skills via subagent dispatch — never written to from `/standup` or directly from this wiki.
- **Linear AIP** (AI Projects team) — status surface for AI Projects, reconciled from Monday execution. Lower-priority for wiki ingest.

## Scope at Janus

Currently scoped to the AI Tools Registry (AIR) and AI Projects status (AIP). Broader project management has migrated to [[notion]] (Operations Notebook journal) plus Monday Automations board (execution surface). The `ai-registry` and `ai-tool-evaluation` skills both operate against Linear AIR directly.

## Relationship to this wiki

Linear AIR holds **pipeline state** (which stage a tool is in, who's evaluating it, when it changed). This wiki holds the **narrative**: what the tool is, why we're evaluating it, what we've learned, how it compares to alternatives. The two are complementary — wiki entries link out to their Linear AIR issue; Linear comments may surface back as decision/lesson pages here.

Closed Linear issues with substantive resolution comments are an ingest source per `CLAUDE.md` §5.1.

## Pipeline discipline

The AIR pipeline is governed by the [[ai-tool-evaluation]] framework. Once a tool enters evaluation, it never returns to Backlog — see [[2026-05-06-backlog-cleanup-no-return-to-backlog]] for the decision. Post-evaluation states are Sandbox / Production / Monitor / Deprecated / Rejected / Duplicate; returning to Backlog would break the audit trail and invite re-evaluation churn.

## Team identifiers and AIP status UUIDs

From Jehad's federated view ([[aio-skills-sor-architecture-jehad]], 2026-05-11) — operationally load-bearing for any `/standup` or wiki-driven Linear API work:

- **AI Registry (AIR) team UUID:** `598dd614-dce5-4ede-98ef-207f3bdff33c`. Issue prefix `AIR-N`. The team was originally created with the name "AI Office" but issues are prefixed `AIR-N` — the prefix is what matters.
- **AI Projects (AIP) team UUID:** `2d1b5c04-94fd-4087-8e95-a5a7aa244a16`. Issue prefix `AIP-N`.

### AIP status UUIDs

| Status | UUID |
|---|---|
| Backlog | `57d6d704-7a3b-41f9-b936-a7d64252d00a` |
| Planned | `d5ccd469-37b4-4b5b-92d6-21be9f27dc90` |
| In Progress | `210b719c-eb51-4d5f-88fb-dcde85ae9939` |
| Done | `661dd6ca-5d5b-4378-8cb4-f1b0384975dc` |
| Cancelled | `ebfcf4e3-f40e-4599-a2b2-827656299627` |

### AIR pipeline

`Backlog → Evaluating → Sandbox → Production` (or `→ Monitor`); also `→ Deprecated / Rejected / Duplicate`.

### Snapshot of recent AIP issues (May 2026)

- AIP-1 Finance Department API Integration (Planned)
- AIP-13 Speaker diarisation for Fireflies (Backlog)
- AIP-15 Deel API & Developer Platform — Capability Assessment (Planned)
- AIP-16 Town Hall Transcript Processing — Pilot (Planned)
- AIP-17 CEO Dashboard — Global Operations View (Backlog)
- AIP-18 Cross-Department Action Routing (Backlog)
- AIP-19 Invoice Bot v3/v4 (Done)
- AIP-20 HR Employee Form Replacement (Done)
- AIP-21 Assessify — Candidate Assessment Platform (Done — expansion underway, conflict logged)
- AIP-22 Decide n8n hosting (Done)

### AIR snapshot stats (May 2026)

74 active issues. Most recent: **AIR-92 Wispr Flow (Whisper Flow)** — added 1 May 2026 standup; Backlog; Functional + Technology + AI Policy.

---

## Operational notes — Linear AIP (AI Projects)

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Linear — AI Projects (AIP)

Team UUID: `2d1b5c04-94fd-4087-8e95-a5a7aa244a16`
Issue prefix: `AIP-N` (e.g. AIP-15, AIP-21)

Tracks **implementation initiatives** — the actual work projects that come out of approved tools or AI strategy decisions. Reconciled against [[monday]] in every standup run.

## Workflow

Simpler than [[ai-registry]]:

```
Backlog → Planned → In Progress → Done
                              ↘ Cancelled
```

## AIP Status UUIDs (used by [[standup]] reconciliation)

| Status | UUID |
|---|---|
| Backlog | `57d6d704-7a3b-41f9-b936-a7d64252d00a` |
| Planned | `d5ccd469-37b4-4b5b-92d6-21be9f27dc90` |
| In Progress | `210b719c-eb51-4d5f-88fb-dcde85ae9939` |
| Done | `661dd6ca-5d5b-4378-8cb4-f1b0384975dc` |
| Cancelled | `ebfcf4e3-f40e-4599-a2b2-827656299627` |

## Reconciliation by [[standup]]

Step 4 of every [[standup]] run cross-checks AIP status against [[monday]] using a two-source mapping algorithm:

1. **Source 1 (canonical):** Monday item's `link_mm2xexj3` Link column → matches `https://linear.app/janusd/issue/AIP-N`
2. **Source 2 (incidental):** regex `/AIP-(\d+)/g` over Monday Updates body
3. **Fallback:** name similarity ≥ 85%

Source 1 wins on conflict.

## Monday → AIP status mapping

| Monday Automations Status | Linear AIP Status |
|---|---|
| Backlog | Backlog |
| In Definition | Planned |
| In Development | In Progress |
| In Testing | In Progress |
| In Production | Done |
| Postponed | Backlog |
| Deprecated | Cancelled |

## Conflict Safety (Step 4C)

[[standup]] **never silently reconciles** AIP drift. If a mismatch exists between Linear and Monday but the transcript doesn't authorise the change AND the Monday execution doesn't clearly justify it, the conflict is logged under **AIP Conflicts Unresolved** in the Final Execution Report — manual review required.

Live example (4 May 2026):
- **AIP-21** "Assessify — Candidate Assessment Platform" — Linear says Done; Monday Assessify is In Testing with active expansion. Logged as conflict because the original AIP-21 scope IS done; new work is beyond it. Recommendation: open a new AIP issue.
- **AIP-15** "Deel API & Developer Platform — Capability Assessment" — Linear says Planned; transcript discussed using Deel as backend (operational use). Logged because no explicit transcript evidence of status change.

## Snapshot of recent AIP issues (May 2026)

- AIP-1 Finance Department API Integration (Planned)
- AIP-15 Deel API & Developer Platform — Capability Assessment (Planned)
- AIP-16 Town Hall Transcript Processing — Pilot (Planned)
- AIP-17 CEO Dashboard — Global Operations View (Backlog)
- AIP-18 Cross-Department Action Routing (Backlog)
- AIP-21 Assessify — Candidate Assessment Platform (Done — but expansion beyond)
- AIP-22 Decide n8n hosting (Done)
- AIP-19 Invoice Bot v3/v4 (Done)
- AIP-20 HR Employee Form Replacement (Done)

## Read-vs-write

- **[[standup]]** writes (only AIP status changes from reconciliation, only when authorised by transcript or completed Monday execution)
- **[[ai-registry]] / [[ai-tool-evaluation]]** never write here (they're AIR-side)

## Related

- Reconciled by: [[standup]] (Step 4)
- Linked from: [[monday]] Link column
- Sibling: [[ai-registry]] (different team, different lifecycle)
