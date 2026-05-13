---
type: process
title: AI Tool Evaluation Framework
slug: ai-tool-evaluation
created: 2026-05-06
updated: 2026-05-12
departments: [ai-office, it-ops]
related: [linear, claude, anthropic, janus-prime-radiant-build, 2026-05-06-backlog-cleanup-no-return-to-backlog]
---

# AI Tool Evaluation Framework

Janus's gate-based process for assessing whether an AI tool or platform should be adopted. Owned by the AI Office. The canonical implementation is the **`/ai-tool-evaluation` skill** — this wiki page is a short reference for cross-linking and high-level orientation, not a duplicate of the skill.

> **For execution, use the skill.** Do not paraphrase gate criteria from this page when running an actual evaluation; the skill is authoritative and may have moved ahead.

## Tool vs Infrastructure (classify before you evaluate)

The classification determines which Gate 1 criteria apply.

- **Tool** — a user-facing application employees interact with directly (Notion, Gamma, Fireflies). All Gate 1 criteria apply.
- **Infrastructure** — a platform/library/service operating below the user-facing layer (cloud providers, container runtimes, object storage, CI/CD). G1.2 (Slack integration) and G1.4 (Data training exclusion) are N/A for Infrastructure — those evaluate at the Workload layer.
- **Workload** — a specific tool deployed on approved Infrastructure. The Workload's own Gate 1 evaluation **must** assess G1.2 and G1.4 on the Workload vendor's terms; the Infrastructure's pass does not carry forward.

Tiebreak: where does user content first enter the system? Direct → Tool. Only via Workloads on top → Infrastructure.

## The four stages

| Stage | Gate | Linear AIR status on pass | What happens |
|---|---|---|---|
| 1. Intake & Triage | Gate 1 | Evaluating | Rapid desk review against binary integration/data criteria. |
| 2. Technical Qualification | Gate 2 | Sandbox | Deep technical review with Must Have + scored criteria. |
| 3. Sandbox & Domain Expert Evaluation | Gate 3 | (still Sandbox until Stage 4) | Controlled testing with structured domain expert feedback. |
| 4. Approval & Registry Listing | Final | Production | Dossier compilation, Head of AI Office approval, IT handover. |

Failure at any gate → rejection or return to a previous stage.

## Gate 1 criteria (Tool only — infrastructure differs)

| # | Criterion |
|---|---|
| G1.1 | Google Workspace / Cloud Integration |
| G1.2 | Slack Integration |
| G1.3 | Data Portability |
| G1.4 | Data Training Exclusion |
| G1.5 | Documented API |

## Gate 2 — Technical Qualification (summary only)

- **Must Have** criteria: all required.
- **Should Have** criteria: scored 0–5 with a 15/25 threshold.
- **Nice to Have** criteria: scored 0–5, informational only.

## Gate 3 — Sandbox & Domain Expert (qualitative)

- G3.1 — Majority of domain experts recommend Approve or Approve-with-conditions (≥ 50%).
- G3.2 — No critical defects identified during sandbox testing.
- G3.3 — Evaluator confirms viable workflow integration path.

## Stage 4 outputs

- Evaluation dossier (all gate comments + domain expert forms + enriched issue description).
- IT Handover document (auth, provisioning scope, network requirements, data boundary, support ownership, licence/billing).
- Approval recommendation for Head of AI Office.
- AI Hub Slack announcement on go-live.

## Linkage to other surfaces

- The framework runs against [[linear]] AIR — pipeline state lives there, gate comments are posted there, statuses move tools through stages.
- The `/standup` skill (v3.13+) auto-chains `/ai-tool-evaluation` for Gate 1 immediately after `/ai-registry` creates a new AIR-N entry. See the standup skill for the chaining contract.
- Wiki vendor pages (e.g., [[claude]], [[pinecone]], [[google-cloud]]) reference this framework when noting "Stage X candidate" or "Gate 1 viability look."

## Pipeline discipline

**Tools never return to AIR Backlog once evaluation has begun.** See [[2026-05-06-backlog-cleanup-no-return-to-backlog]] — post-evaluation tools move to Sandbox / Production / Monitor / Deprecated / Rejected / Duplicate, never back to Backlog. This preserves the audit trail and prevents re-evaluation churn.

## When to update this page

Whenever the gate criteria change in the skill — keep the wiki summary in sync with the skill version. As of 2026-05-06 the skill version is unspecified in this reference; check the skill file directly for current status.
