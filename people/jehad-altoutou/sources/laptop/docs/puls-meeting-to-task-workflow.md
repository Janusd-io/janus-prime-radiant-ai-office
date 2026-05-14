---
type: source
source_type: laptop
title: PULS-Meeting-to-Task-Workflow
slug: puls-meeting-to-task-workflow
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/PULS-Meeting-to-Task-Workflow.docx
original_size: 18338
original_ext: .docx
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:43Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Operational process documentation Jehad authored for PULS/IMS — explicitly intended for Simon (ISO Lead) review and dept-wide reference"
project: desktop-captures

---

# PULS-Meeting-to-Task-Workflow

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/PULS-Meeting-to-Task-Workflow.docx` on 2026-05-14._

# [[meeting-to-task-workflow|Meeting → Task → Build Workflow]]

**How requirements become tasks become deployed software at Janus
Digital — AI Operations.**

> This document describes the actual operating procedure for converting
> meetings (internal or with other departments) into tracked tasks,
> logged work, and executed builds. It is the implementation of Activity
> 1 (“Gather requirements”) through Activity 6 (“Handover to IT”) in the
> AI Operations Engineer process schematic.

| Field | Value |
|----|----|
| **Process Owner** | Jehad — AI Operations Engineer |
| **Covers IMS processes** | C1 AI System Design & Development · C2 Software Development & Release · S2 IT Infrastructure & Data Governance |
| **Related ISO clauses** | 9001 §8.1 (operational planning) · 9001 §7.5 (documented information) · 27001 A.5 / A.8 (policies + asset mgmt) · 42001 §6.1 / §8.2 (AI risk + operational planning + AI Systems Register) |
| **Underlying technical skill** | `/standup` v3.11 — invoked from Claude Desktop after every AI Office meeting |
| **Last updated** | 7 May 2026 |

------------------------------------------------------------------------

## 1. The flow at a glance (ISO 9001:2015 Figure 1)

    flowchart LR
        SRC["<b>SOURCES OF INPUTS</b><br/>Internal meetings (departments / teams)<br/>Slack channels<br/>Cross-department requests<br/>Leadership direction ([[michael-bruck|Michael Bruck]])"]

        IN["<b>INPUTS</b><br/>[[fireflies|Fireflies]] meeting transcript (canonical)<br/>Slack thread context<br/>Existing Monday / [[linear|Linear]] / Notion state"]

        subgraph ACT ["<b>ACTIVITIES</b> — 3-phase model: Analyse · Plan · Execute"]
            direction LR
            P1["Phase 1<br/>Analyse<br/>(read-only)"] --> P2["Phase 2<br/>Plan<br/>(read-only)"]
            P2 --> P3["Phase 3<br/>Execute<br/>(writes only)"]
        end

        OUT["<b>OUTPUTS</b><br/>Monday tasks + sub-items + Updates<br/>Linear AIP issues reconciled<br/>Linear AIR entries (via subagent)<br/>Notion journal entry<br/>Final Execution Report"]

        RCV["<b>RECEIVERS OF OUTPUTS</b><br/>Process Owners (assignees)<br/>IT department (handover)<br/>End-users (deployed feature)<br/>Internal Audit (M4) — full trail"]

        CTRL["<b>CONTROLS</b><br/>Notion idempotency check<br/>Subagent Dispatch Gate<br/>Conflict Safety on Linear AIP<br/>No-orphan invariant<br/>Strict Write Safety<br/>Execution Control Mode (large runs)"]

        RES["<b>RESOURCES</b><br/>Fireflies (transcript)<br/>Monday Automations (board 5095012818)<br/>Linear AIP (tasks) + AIR ([[ai-tool-registry|AI tool registry]])<br/>Notion Operations Notebook<br/>Claude Desktop (skill orchestrator)"]

        KPI["<b>MONITORING & MEASUREMENT</b><br/>Notion entries posted per meeting · Subagent failure rate<br/>AIP conflicts unresolved · Owner orphans · Time from meeting end to plan ready"]

        CTRL --> ACT
        SRC --> IN --> ACT --> OUT --> RCV
        RES --> ACT
        ACT -.-> KPI

        classDef ctrl fill:#FFF8D6,stroke:#996600,stroke-width:2px,color:#000
        classDef act fill:#E6F0FF,stroke:#1A4480,stroke-width:2px,color:#000
        classDef res fill:#FFE8E8,stroke:#990000,stroke-width:2px,color:#000
        classDef kpi fill:#E8F5E9,stroke:#1B5E20,stroke-width:2px,color:#000
        classDef neutral fill:#F5F5F5,stroke:#666,stroke-width:1px,color:#000

        class CTRL ctrl
        class ACT,P1,P2,P3 act
        class RES res
        class KPI kpi
        class SRC,IN,OUT,RCV neutral

------------------------------------------------------------------------

## 2. Step-by-step procedure

### Phase 1 — Analyse (read-only)

| \# | Step | What happens | Tool |
|----|----|----|----|
| 1.1 | Retrieve transcript | Fetch the Fireflies recording of the meeting (broad keyword + ±1 day window) | Fireflies API |
| 1.2 | Build Meeting Intelligence Digest | Construct structured summary from raw transcript: attendees · topics · decisions · open questions · action items · blockers · tool mentions · implied next steps. **The Fireflies auto-summary is treated as a weak hint, never canonical.** | Claude (analysis) |
| 1.3 | Notion idempotency check | Look for an existing `## AIO <DD Mon YYYY>` entry. If found, ask user: skip / rerun / abort — **no writes occur until decision is made.** | Notion API |
| 1.4 | Parse Digest into typed items | Convert each action / decision / question into typed records ready for matching | Claude (parsing) |

**Phase 1 control point:** Phase 1 is strictly read-only. If any tool
attempts to write, abort.

### Phase 2 — Plan (read-only)

| \# | Step | What happens |
|----|----|----|
| 2.1 | Confidence-scored matching | Match each parsed item against existing Monday tasks / Linear AIP issues / Notion entries. Score each match: high (≥85%) · medium (60-84%) · low (\<60%) |
| 2.2 | Duplicate detection | Apply keyword rules to flag near-duplicates of work already in flight |
| 2.3 | Parent project routing | Prefer attaching new sub-items to existing parent projects rather than creating new top-level items |
| 2.4 | Subagent Dispatch Gate | For each AI tool mention in the transcript, evaluate whether the mention has enough signal to justify dispatching `/ai-registry` or `/ai-tool-evaluation` subagents. Low-signal mentions are dropped here. |
| 2.5 | Generate execution plan | Compile every proposed write — Monday creates / updates / Updates posts · subagent hand-offs · Linear AIP reconciliation · Notion entry — into one explicit plan. **No writes yet.** |
| 2.6 | Execution Control Mode check | If plan complexity exceeds thresholds (\>15 actions OR \>3 subagent dispatches OR multiple medium-confidence matches OR long/dense transcript), present the plan to the user and **wait for the literal phrase** `Approve execution` before continuing. |

**Phase 2 control point:** Medium-confidence matches always require
human approval. Low-confidence matches never auto-create.

### Phase 3 — Execute (writes only — strict priority order)

| \# | Step | What happens | Output |
|----|----|----|----|
| 3.1 | Monday Automations writes | Create new tasks · update existing · post Updates · attach sub-items. **Strict Write Safety Rules** apply throughout. | Monday item IDs |
| 3.2 | No-orphan next-step pass | Verify every action item from the Digest has a corresponding Monday assignee. Owner orphans block the run. | Owner-completeness audit |
| 3.3 | Context Updates on creates (v3.11) | Every newly created Monday parent and sub-item gets a Context Update — Source / Why / Definition of done / Cross-links — posted to its Updates timeline. Idempotent: skip if a Context block already exists. | Updates posted |
| 3.4 | Subagent dispatch | For surviving AI tool mentions, dispatch `/ai-registry` and `/ai-tool-evaluation` subagents via the Task/Agent tool — gated, validated, volume-controlled. **For new-tool registry creates, Gate 1 evaluation is auto-chained** (no extra confirmation). | Linear AIR entry · evaluation comment |
| 3.5 | Linear AIP reconciliation | Build the AIP-N → Monday-item-id map. Apply status changes only when the transcript or completed Monday work authorises it. **Conflict Safety:** never overwrite Linear when transcript and Monday disagree. | AIP status updates |
| 3.6 | Notion journal entry | Append `## AIO <DD Mon YYYY>` to the Operations Notebook — Clean Meeting Summary · 🎯 Next steps by next standup · 📅 This week · 🏔️ Longer horizon · Decisions · Findings · Monday items touched · AIP reconciliation · AI Registry / Evaluation outcomes. **Output compression** rules cap entry size; Notion size hygiene auto-archives at thresholds. | Notion entry URL |
| 3.7 | Final Execution Report | Emit a structured report — items updated · created · sub-items · Updates · subagent outcomes · failures · conflicts · missing owners · warnings. | Final report shown to user |

**Phase 3 control points:** - Confidence ≥85% → execute automatically
(subject to Strict Write Safety) - Confidence 60-84% → already paused
for approval in Phase 2 - Confidence \<60% → never auto-creates

------------------------------------------------------------------------

## 3. Where this connects to the build (Activities 2-6)

Once a Monday task or Linear AIP issue exists from this workflow, it
enters the rest of my AI Ops flow:

    This document (Activity 1)        AI Ops process (Activities 2-6)
    ══════════════════════════        ═══════════════════════════════
    Meeting → Monday/Linear task ──▶  Build in sandbox
                                  ──▶ Stress test (functionality / UI / sec / API / stability)
                                  ──▶ Fix and enrol
                                  ──▶ Document (SOP / README / implementation plan)
                                  ──▶ Handover to IT

Audit traceability runs end-to-end: every deployed feature can be traced
backward to a Monday task → a Linear AIP → a Notion journal entry → a
Fireflies transcript → the original meeting.

------------------------------------------------------------------------

## 4. Controls & check points (full list)

| Control | Where it fires | Why it exists |
|----|----|----|
| **Notion idempotency check** | Phase 1, before any writes | Prevents duplicate journal entries when re-running the workflow |
| **Subagent Dispatch Gate** | Phase 2.4 | Stops over-triggering of `/ai-registry` and `/ai-tool-evaluation` on low-signal mentions |
| **Execution Control Mode** | Phase 2.6 | Forces explicit user approval (`Approve execution`) on large or ambiguous runs |
| **Strict Write Safety Rules** | Phase 3.1 | Guards Monday writes — no destructive ops, idempotent updates only |
| **No-orphan invariant** | Phase 3.2 | Every action must have an owner — no untrackable work |
| **Mandatory Context Updates** | Phase 3.3 | Every new task gets traceability back to its source meeting (v3.11) |
| **Conflict Safety on Linear AIP** | Phase 3.5 | Never overwrites Linear when transcript and Monday execution disagree |
| **Output compression + Notion size hygiene** | Phase 3.6 | Keeps the Notion journal readable and auto-archives oversized pages |
| **Final Execution Report** | Phase 3.7 | Surfaces all failures, conflicts, missing owners — nothing fails silently |

------------------------------------------------------------------------

## 5. Resources

| Resource | Detail |
|----|----|
| **Process Owner** | Jehad — AI Operations Engineer (accountable) |
| **Orchestrator** | Claude Desktop (skill `/standup` v3.11) |
| **Transcript source** | Fireflies (canonical — auto-summary disregarded) |
| **Task surface** | Monday Automations board `5095012818` |
| **Issue tracker** | Linear AIP team (project tasks) |
| **AI tool registry** | Linear AIR team — sole source of truth, written only via `/ai-registry` subagent |
| **Journal** | Notion Operations Notebook (`https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a`) |
| **Sibling skills** | `/ai-registry` (registry CRUD + related-tools check) · `/ai-tool-evaluation` (Gate 1-4 methodology) |

------------------------------------------------------------------------

## 6. Outputs and records (audit-ready)

| Output | Where it lives | Retention |
|----|----|----|
| Fireflies transcript | Fireflies | Per Fireflies retention policy |
| Meeting Intelligence Digest | Notion journal entry (compressed) | Permanent, in journal |
| Monday tasks / sub-items / Context Updates | Monday board `5095012818` | Permanent |
| Linear AIP status changes | Linear AIP team | Permanent |
| Linear AIR entries (when new AI tools mentioned) | Linear AIR team (via subagent) | Permanent |
| Notion journal entry | Operations Notebook | Auto-archived per size hygiene rules |
| Final Execution Report | Shown to user; can be saved to Notion if needed | On request |

------------------------------------------------------------------------

## 7. KPIs (proposed for PULS dashboard)

| KPI | Target | Source |
|----|----|----|
| Notion entries posted per AI Office meeting | 100% | Notion |
| Subagent failure rate | \<5% | Final Execution Report log |
| AIP conflicts unresolved per week | 0 | Linear AIP |
| Owner orphans detected per run | 0 | Final Execution Report |
| Time from meeting end to execution plan ready | \<30 min | Run timestamps |
| New AI tools registered in AIR per quarter | tracked | Linear AIR |
| Auto-chained Gate 1 evaluations completed within 24h | 100% | Linear AIR comments |

------------------------------------------------------------------------

## 8. ISO clause mapping

| Clause | How this workflow satisfies it |
|----|----|
| **ISO 9001:2015 §8.1** Operational planning and control | Defined process · documented controls · planned outputs · explicit phase boundaries |
| **ISO 9001:2015 §7.5** Documented information | Notion entries + Final Execution Reports retained as objective evidence |
| **ISO 9001:2015 §8.5.6** Control of changes | Conflict Safety + Strict Write Safety prevent uncontrolled changes |
| **ISO/IEC 27001:2022 §A.5** Information security policies | Subagent Dispatch Gate + Strict Write Safety enforce policy at write time |
| **ISO/IEC 27001:2022 §A.8** Asset management | Linear AIR maintains the [[ai-tools-registry|AI Tools Registry]] as a managed asset register |
| **ISO/IEC 42001:2023 §6.1** AI risk management | Auto-chained Gate 1 evaluation on every new AI tool registered |
| **ISO/IEC 42001:2023 §8.2** AI System Impact Assessment | Sibling `/ai-tool-evaluation` skill performs formal Gate 1-4 evaluations stored as Linear AIR comments |

------------------------------------------------------------------------

## 9. How this is invoked in practice

After any AI Office meeting:

    User says: "Process today's standup"
      or:      "Log the standup from <date>"

In Claude Desktop, the `/standup` skill orchestrates the entire flow
described above.

For meetings outside the AI Office (cross-department, vendor calls,
etc.), the same workflow applies but Fireflies search keywords change
and the parent-project routing targets different Monday groups (see
[[standup-skill|standup skill]]’s Department Group Routing reference).

------------------------------------------------------------------------

## 10. Open items for Simon (ISO Lead)

- Confirm this workflow satisfies the operational planning evidence
  requirement for **C1 / C2 / S2** — or specify additional documentation
  needed.
- Confirm the Linear AIR entries (with Gate 1 evaluation comments) are
  sufficient as the **AI Systems Register** required by ISO 42001, or
  whether a separate Notion-side mirror is needed.
- Decide whether the Notion idempotency check + Final Execution Report
  constitute sufficient **§7.5 documented information** retention, or if
  additional archival to a dedicated audit folder is required.
- Confirm whether non-AI-Office meetings (vendor calls,
  cross-department) should follow this same workflow with different
  routing rules, or have a separate documented procedure.

------------------------------------------------------------------------

← Back to [README](./README.md) · See also:
[04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md) ·
[06-FIRST-VOICE-FINAL.md](./06-FIRST-VOICE-FINAL.md)
