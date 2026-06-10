---
type: process
title: AI Tool Evaluation Framework
slug: ai-tool-evaluation
created: 2026-05-06
updated: 2026-06-09
sources: [jehad-vault-ai-tool-evaluation]
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

---

## Notes — ai-tool-evaluation skill

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# /ai-tool-evaluation — Gate 1–4 evaluation framework

Janus Digital's formal multi-stage evaluation process for AI tools and platforms. Companion to [[ai-registry]] — where [[ai-registry]] manages Linear issues and derivative views, this skill handles the **structured assessment methodology**: research, gate criteria, scored assessments, formal evaluation records.

## When to use

Trigger phrases:
- *"Do a Stage 1 on AIR-N"* / *"Triage [tool name]"*
- *"Run Gate 1 / Gate 2 / Gate 3 / Gate 4"*
- *"Score [tool] against the framework"*
- *"Prepare an approval dossier for [tool]"*
- *"Domain expert evaluation"* / *"Sandbox evaluation write-up"*

Also dispatched as a subagent by [[standup]] when transcripts contain explicit gate evaluation requests (e.g. "we should run Gate 1 on Stitch", "evaluate Harvey AI for security").

## The four-stage process

| Stage | Gate | Linear status (on PASS) | What happens |
|---|---|---|---|
| Stage 1: Intake & Triage | Gate 1 | Evaluating | Rapid desk review against 5 binary integration/data criteria |
| Stage 2: Technical Qualification | Gate 2 | Sandbox | Deep technical review with Must Have + scored criteria |
| Stage 3: Sandbox & Domain Expert | Gate 3 | (remains Sandbox until Stage 4) | Controlled testing with structured domain expert feedback |
| Stage 4: Approval & Registry Listing | Final approval | Production | Dossier compilation, Head of AI Office approval, IT handover |

A failure at any gate results in **Rejected** (or return to a previous stage for re-evaluation).

## Stage 1 — Intake & Triage (most common)

**Five binary criteria** — all must PASS to proceed:
- **G1.1** — Google Workspace / Cloud integration or export
- **G1.2** — Slack integration (app, webhook, or MCP connector)
- **G1.3** — Data portability (standard export formats)
- **G1.4** — Data training exclusion (contractual guarantee)
- **G1.5** — Documented API

Each evaluated as PASS / FAIL / CONDITIONAL PASS with specific evidence (URL, page section, ToS clause).

Gate 1 outcome:
- All PASS → **GATE 1 PASS** → tool proceeds to Stage 2
- Any FAIL with no viable path → **GATE 1 FAIL** → tool rejected
- Conditional / uncertain → **GATE 1 BLOCKED** → flagged for clarification

## Stage 2 — Technical Qualification

Three categories of criteria:
- **Must Have** (binary pass/fail, all required) — MCP/AI orchestration, enterprise auth, vendor viability
- **Should Have** (scored 0–5, threshold 15/25) — efficiency gain, ease of adoption, multi-platform, audit trail, Gemini integration
- **Nice to Have** (scored 0–5, informational only) — automation support, competitive differentiation, cost efficiency

Outcome:
- All Must Haves pass + Should Have ≥ 15/25 → **PASS** → Sandbox
- Should Have 10–14/25 → **CONDITIONAL** → Head of AI Office decides
- Any Must Have fails OR Should Have < 10/25 → **FAIL** → Rejected

## Stage 3 — Sandbox & Domain Expert

Human-driven. This skill **structures and documents** rather than conducts the evaluation:
- Generates the test brief (representative tasks for domain experts)
- Generates blank evaluation forms
- Summarises domain expert feedback
- Posts the Gate 3 Assessment comment with aggregated findings

Gate 3 criteria (qualitative):
- **G3.1** — Majority of domain experts recommend Approve / Approve-with-conditions (≥ 50%)
- **G3.2** — No critical defects identified during sandbox testing
- **G3.3** — Evaluator confirms viable workflow integration path

## Stage 4 — Approval & Registry Listing

Administrative. This skill:
- Compiles the evaluation dossier (Gates 1, 2, 3 + domain expert forms + enriched description)
- Drafts the IT handover document (auth, provisioning, network, data boundary, support ownership)
- Prepares the approval recommendation for Head of AI Office
- On approval — moves the AIR issue to Production, drafts the Slack #ai-internal-hub announcement

## Where the evaluation lives

Each gate posts a structured **comment** on the corresponding Linear AIR issue (created/managed by [[ai-registry]]). Comments form the audit trail of the evaluation history.

## Subagent invocation contract

Same as [[ai-registry]] — JSON hand-off + JSON return per [[ai-office-architecture]]. The `notion_journal_addition` field surfaces the gate decision (e.g. "Gate 1 PASS — proceed to Stage 2") in [[standup]]'s Notion entry.

## Conventions

- British English
- USD costs
- Cite specific evidence source (URL, page section, ToS clause) for every criterion
- Conditional criteria flagged explicitly (not converted to PASS/FAIL)
- Reference framework section numbers when relevant

## Related

- Companion: [[ai-registry]] (Linear issue management + description schema)
- Orchestrator: [[standup]] (dispatches via subagent)
- System of record: [[ai-registry]] (gate comments)
- Reference docs (in plugin): `references/gate-criteria.md`, `references/scoring-matrix.md`, `references/evaluation-form.md`
