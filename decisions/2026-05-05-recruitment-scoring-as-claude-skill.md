---
type: decision
title: Recruitment scoring moves from a Bonaventure project + thread to a reusable Claude skill
slug: 2026-05-05-recruitment-scoring-as-claude-skill
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, hr]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [aio-2026-05-05]
related: [agent-skills, claude]
---

# Recruitment scoring moves to a reusable Claude skill

**Decision date:** 2026-05-05
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-05]]

## What

The existing recruitment scoring workflow — currently a project + chat thread shared between Bonaventure and Marianne — will be rebuilt as a reusable Claude skill. Same inputs (CV, JD, interview transcript), same scoring contract, same output structure, but invocable repeatably by anyone who needs it.

## Why

- Project + thread mode forces two users to share an account; reproducing scoring across different recruiters is friction-heavy.
- Skills are first-class in the Claude product family ([[claude]], [[agent-skills]]). They package condensed expertise and load on demand without polluting general context.
- Once the scoring skill exists, the [[2026-05-04-centralised-fireflies-webhook-for-interviews|Fireflies webhook]] can trigger it automatically post-interview.

## Blockers

- Marianne does not hold the formal QBIC scoring metrics — Jehad to obtain from Bonaventure / Teresa / Mariam before the skill can be ported with full fidelity.
- Sample CVs / JDs / interview outputs needed from Teresa / Mariam to validate the skill against existing scoring outputs.

## Implications

- Recruitment scoring becomes shareable and auditable — multiple recruiters get the same contract.
- The skill is a candidate to expose to the HR Dashboard board front-end agentic UIs.
- Same pattern likely generalises to other scoring/evaluation workflows currently locked in chat threads.
