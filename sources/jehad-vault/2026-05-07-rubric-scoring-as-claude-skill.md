---
type: decision
title: HR Rubric scoring rebuilt as a reusable Claude skill (API direct; MCP for low-volume only)
slug: 2026-05-07-rubric-scoring-as-claude-skill
created: 2026-05-07
updated: 2026-05-13
departments: [hr, ai-office]
status: resolved
owner: jehad-altoutou
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [claude, hr-recruitment-pipeline, claude-skills]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/2026-05-07-rubric-scoring-as-claude-skill.md` — this file is preserved as a source for divergent framing / additional context._

# HR Rubric scoring rebuilt as a reusable Claude skill

**Decision date:** 2026-05-07. **Decided by:** [[michael-bruck]], [[jehad-altoutou]]. Source: AIO 2026-05-07 standup.

## What

[[jehad-altoutou]] rebuilt the HR Rubric (recruitment) scoring system *without source access* — pre-interview report taking JD + CV and producing dimensions, score, gaps, red flags, and interview questions. Output matches [[bonaventure-wong]]'s original prompt-engineered scoring. Now packaged as a reusable [[claude]] skill rather than living in a shared chat thread.

Architecture:
- **Production scoring** — Claude API direct (high volume, low latency).
- **Low-volume rubric creation flows** — MCP retained as the surface where rubrics get authored.

## Why

- Refines and extends `2026-05-05-recruitment-scoring-as-claude-skill` — that decision said "rebuild as a skill"; this picks the API surface and rationalises why MCP and direct API coexist.
- Bonaventure prompt-engineered version was project-mode-locked to a shared account; the skill version is reproducible across users.
- Skills replaced prompt engineering once the workflow stabilised.

## Cost economics

First production scoring run: **$1.12 per CV / 116k tokens.** Agency batches of 10–20 CVs cost ~$30. Cheaper *and* faster than human-only triage even at the upper bound.

## Implications

- Bonaventure's existing prompt history is the next extraction target — Jehad to derive any remaining undiscovered methodology nuances on Bonaventure's return.
- Per-workstream Claude API keys + weekly cost report to HR + finance is the billing-discipline complement.
- Deel sandbox account acquisition is queued.
