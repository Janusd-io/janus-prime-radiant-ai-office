---
type: decision
title: HR Rubric scoring rebuilt as a reusable Claude skill (Claude API direct; MCP for low-volume only)
slug: 2026-05-07-rubric-scoring-as-claude-skill
created: 2026-05-07
updated: 2026-05-13
departments: [hr, ai-office]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [aio-2026-05-07, jehad-vault-2026-05-07-rubric-scoring-as-claude-skill]
related: [claude, recruitment-automation-pipeline, agent-skills, 2026-05-05-recruitment-scoring-as-claude-skill]
---

# HR Rubric scoring rebuilt as a reusable Claude skill

**Decision date:** 2026-05-07
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-07]]

## What

Jehad rebuilt the HR Rubric (recruitment) scoring system *without source access* — pre-interview report taking JD + CV and producing dimensions, score, gaps, red flags, and interview questions. Output matches Bonaventure's original prompt-engineered scoring. The system is now packaged as a reusable [[claude]] skill rather than living in a shared chat thread.

Architecture:

- **Production scoring** — Claude API direct (high volume, low latency).
- **Low-volume rubric creation flows** — MCP retained as the surface where rubrics get authored.

## Why

- Refines and extends [[2026-05-05-recruitment-scoring-as-claude-skill]] — that decision said "rebuild as a skill"; this decision picks the API surface and rationalises why MCP and direct API coexist.
- The Bonaventure prompt-engineered version was project-mode-locked to a shared account; the skill version is reproducible across users without that friction.
- Skills (per [[agent-skills]]) replaced prompt engineering as the right packaging once the workflow stabilised.

## Cost economics

First production scoring run: **$1.12 per CV / 116k tokens.** Agency batches of 10–20 CVs cost ~$30. Cheaper *and* faster than human-only triage even at the upper bound. See [[recruitment-automation-pipeline]] for the full operational context.

## Implications

- Bonaventure's existing prompt history is the next extraction target — Jehad to derive any remaining undiscovered methodology nuances on Bonaventure's return.
- Per-workstream Claude API keys + weekly cost report to HR + finance ([[2026-05-07-per-workstream-api-keys-cost-monitoring]]) are the billing-discipline complement.
- Deel sandbox account acquisition is queued ([[recruitment-automation-pipeline]]).

## Related

- [[2026-05-05-recruitment-scoring-as-claude-skill]] — original "rebuild as skill" decision.
- [[recruitment-automation-pipeline]] — project hub.
- [[claude]] — host platform.
