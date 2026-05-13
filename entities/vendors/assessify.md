---
type: vendor
title: Assessify
slug: assessify
created: 2026-05-06
updated: 2026-05-06
departments: [hr, ai-office]
status: active
confidence: medium
sources: [aio-2026-05-04, aio-2026-05-05, aio-2026-05-06]
related: [deel, fireflies, claude, 2026-05-04-recruitment-execution-on-hr-dashboard-board, 2026-05-05-recruitment-scoring-as-claude-skill]
---

# Assessify

HR / candidate-assessment platform. At Janus, "Assessify" refers both to the third-party platform and to the broader recruitment-automation pipeline being built around it.

## Janus context

- **Linear AIP-21** "Assessify — Candidate Assessment Platform" was the original capability assessment; status: **Done**. The original scope (assessment platform evaluation) is complete.
- **Expansion underway (2026-05-04 onwards):** Assessify is now the bridge item on the AIO Automations Monday board for the full recruitment-automation pipeline. Execution lives on the dedicated [[monday]] HR Dashboard board (`5095636727`).
- **Conflict open in Linear AIP:** AIP-21 is Done in Linear but the related Monday "Assessify HR platform" item is In Testing for the expansion. Recommend new AIP issue or reopening AIP-21 with revised scope (manual review still required as of 2026-05-06).

## Pipeline scope (as of 2026-05-06)

CV intake form → AI pre-assessment → Slack notifications → interview scheduling → Fireflies transcript pull → post-assessment scoring (a reusable [[claude|Claude]] skill per [[2026-05-05-recruitment-scoring-as-claude-skill]]) → results to recruiter front-end.

## Adjacent vendors

- [[deel]] — used as headless backend; line managers interact only via agentic UIs.
- [[fireflies]] — interview transcripts via centralised webhook (per [[2026-05-04-centralised-fireflies-webhook-for-interviews]]).
- [[claude]] — host of the recruitment scoring skill.

## Watch for

- Resolution of the AIP-21 conflict (new issue vs reopen).
- Whether QBIC scoring metrics are obtained from Bonaventure / Teresa / Mariam (currently a porting blocker).
- Front-end agentic UI maturity once recruiter-facing screens land.
