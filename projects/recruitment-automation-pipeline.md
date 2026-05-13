---
type: project
title: Recruitment Automation Pipeline
slug: recruitment-automation-pipeline
created: 2026-05-07
updated: 2026-05-13
departments: [hr, ai-office]
status: active
owner: jehad-altoutou
sources: [aio-2026-05-04, aio-2026-05-05, automations-2881310536, jehad-vault-recruitment-automation-pipeline]
related: [assessify, deel, fireflies, claude, jehad-altoutou, andrew-soane, bonaventure-wong, theresa-wong, mariam-mahmood, 2026-05-04-recruitment-execution-on-hr-dashboard-board, 2026-05-04-centralised-fireflies-webhook-for-interviews, 2026-05-05-recruitment-scoring-as-claude-skill]
---

# Recruitment Automation Pipeline

Hub for the full CV-to-hire automation pipeline being built across the Janus AI Office and HR. Bridge item on the AIO Automations board: [[assessify|Assessify HR platform]] (Monday `2881310536`); execution lives on the dedicated HR Dashboard Monday board (`5095636727`, 28 items, P0–P3 prioritised).

## Scope

End-to-end recruitment flow:

1. **CV intake** — recruiter form on the HR Dashboard board.
2. **AI pre-assessment** — CV parse and initial match scoring against the JD.
3. **Slack notification** — recruiter and hiring-manager notifications via [[slack]].
4. **Interview scheduling** — calendar integration with [[fireflies]] auto-recording invitee on every meeting.
5. **Post-interview scoring** — webhook-triggered [[claude|Claude]] skill ([[2026-05-05-recruitment-scoring-as-claude-skill]]) running QBIC/Rubric scoring against CV + JD + interview transcript.
6. **Candidate dashboard** — front-end agentic UI for line managers; [[deel]] sits headless underneath.

## Architecture decisions

- [[2026-05-04-recruitment-execution-on-hr-dashboard-board]] — execution lives on dedicated HR Dashboard board; Assessify on Automations is the bridge.
- [[2026-05-04-centralised-fireflies-webhook-for-interviews]] — single Fireflies invitee email + webhook for transcript capture.
- [[2026-05-05-recruitment-scoring-as-claude-skill]] — scoring rebuilt as a reusable Claude skill instead of a shared-account project + thread.
- [[2026-05-07-rubric-scoring-as-claude-skill]] — Rubric scoring rebuilt without source access, matching Bonaventure's original output. Architecture: Claude API direct for production; MCP for low-volume rubric creation. **Cost economics: $1.12/CV / 116k tokens; agency batches ≈ $30.**
- [[2026-05-07-per-workstream-api-keys-cost-monitoring]] — per-workstream Claude API keys + weekly cost reports to HR + finance.

## Newly queued (as of 2026-05-07)

- Set up **Deel sandbox account** for HR platform integration testing — owner: both, due 13 May. Bonaventure overrode the standard evaluation pipeline for Deel as an executive call.
- Extract rubric scoring methodology from Bonaventure's prompt history into the reusable skill — owner: Jehad, due 13 May (sync with Bonaventure on his return).

## Status (as of 2026-05-07)

- HR Dashboard board (`5095636727`) populated with 28 items.
- Bridge item Assessify HR platform — In Testing.
- Linear AIP-21 conflict outstanding: original Assessify scope is Done in Linear but the recruitment-pipeline expansion is In Testing in Monday. Manual review required (recommend new AIP issue or reopening AIP-21 with revised scope).
- Linear AIP-15 (Deel API & Developer Platform — Capability Assessment): Planned in Linear; should be advanced now that Deel is operationally critical as headless backend.

## Active dependencies / blockers

- **Sample CVs + JDs + interview outputs** from [[theresa-wong|Theresa]] / [[mariam-mahmood|Mariam]] needed to validate the scoring skill against existing outputs.
- **QBIC scoring metrics** from [[bonaventure-wong|Bonaventure]] / Marianne — porting blocker; Marianne does not hold the formal metrics.
- **Claude API key** generation for the SSFI/Assessify AI agent.
- **Centralised Fireflies setup** with webhook for interview transcripts — design phase.

## Owners

- Engineering: [[jehad-altoutou]]
- HR sponsor / decision-maker: [[theresa-wong]] (head of HR)
- HR operations: [[mariam-mahmood]]
- Stakeholder coordination: [[michael-bruck]] (AIO), [[andrew-soane]] (Marketing — career-page integration), [[bonaventure-wong]] (origin scoring workflow)
- External (still unresolved): Marianne (existing scoring workflow co-author with Bonaventure; Janus-internal status not yet confirmed)

## Watch for

- Resolution of the AIP-21 conflict.
- AIP-15 advancement to In Progress.
- First end-to-end run of the pipeline on a sample candidate.
