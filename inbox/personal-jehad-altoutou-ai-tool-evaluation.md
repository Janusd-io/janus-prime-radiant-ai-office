---
type: process
title: AI Tool Evaluation Framework
slug: ai-tool-evaluation
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, it-ops]
sources: [pr-backup-2026-05-11-process-ai-tool-evaluation]
related: [linear, claude-code, anthropic, ai-tool-evaluation-framework, ai-tool-evaluation-iso-procedure, gate-based-evaluation]
audience: [department]
captured_by: jehad-altoutou
---

# AI Tool Evaluation Framework

Janus's gate-based process for assessing whether an AI tool or platform should be adopted. Owned by the AI Office. The canonical implementation is the **`/ai-tool-evaluation` skill** — this wiki page is a short reference for cross-linking and high-level orientation, not a duplicate of the skill.

> Dedupe note: closely related to the canonical project pages [[ai-tool-evaluation-framework]] and [[ai-tool-evaluation-iso-procedure]]. This is the process-level reference (the framework as a documented procedure) restored from PR backup.

> **For execution, use the skill.** Do not paraphrase gate criteria from this page when running an actual evaluation; the skill is authoritative.

## Tool vs Infrastructure (classify before you evaluate)

- **Tool** — a user-facing application employees interact with directly (Notion, Gamma, Fireflies). All Gate 1 criteria apply.
- **Infrastructure** — a platform/library/service operating below the user-facing layer (cloud providers, container runtimes, object storage, CI/CD). G1.2 (Slack integration) and G1.4 (Data training exclusion) are N/A for Infrastructure.
- **Workload** — a specific tool deployed on approved Infrastructure. The Workload's own Gate 1 evaluation **must** assess G1.2 and G1.4 on the Workload vendor's terms.

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

- Evaluation dossier.
- IT Handover document (auth, provisioning scope, network requirements, data boundary, support ownership, licence/billing).
- Approval recommendation for Head of AI Office.
- AI Hub Slack announcement on go-live.

## Linkage to other surfaces

- The framework runs against [[linear]] AIR — pipeline state lives there.
- The `/standup` skill (v3.13+) auto-chains `/ai-tool-evaluation` for Gate 1 immediately after `/ai-registry` creates a new AIR-N entry.
- Wiki vendor pages reference this framework.

## When to update this page

Whenever the gate criteria change in the skill — keep the wiki summary in sync with the skill version.
