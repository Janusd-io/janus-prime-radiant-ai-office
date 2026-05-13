---
type: decision
title: Per-workstream Claude API keys with weekly cost reporting to HR + finance
slug: 2026-05-07-per-workstream-api-keys-cost-monitoring
created: 2026-05-07
updated: 2026-05-07
departments: [ai-office, finance, hr]
status: resolved
owner: jehad-altoutou
sources: [aio-2026-05-07]
related: [claude, ann-greed, recruitment-automation-pipeline]
---

# Per-workstream Claude API keys + weekly cost reporting

**Decision date:** 2026-05-07
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-07]]

## What

Each AI Office workstream gets its own [[claude|Claude]] API key. A weekly cost report goes to HR and finance ([[ann-greed]]) showing per-workstream consumption.

## Why

- Granular billing enables accurate cost-allocation per workstream (recruitment, marketing, IT, etc.).
- First production scoring run on the recruitment pipeline measured **$1.12 per CV / 116k tokens** — small enough per-unit, but at agency-batch scale ($30/batch) it adds up. Without per-workstream visibility, cost surprises arrive unattributed.
- Finance gets a clean cost-attribution surface; HR gets visibility into recruitment automation's running cost.

## Implications

- Implementation queued this week (per the 2026-05-07 standup — owner: Jehad, due 13 May).
- Pattern generalises: any workstream that goes to production gets its own API key. The recruitment pipeline is the first; the Singapore news bot, the marketing CRM tooling, and the IT helpdesk triage bot will follow as they go live.
- Sets a baseline for finance-side governance of AI tooling spend, complementing [[ai-policy-gate-approval]].

## Related

- [[recruitment-automation-pipeline]] — first workstream to exercise the pattern.
- [[2026-05-07-rubric-scoring-as-claude-skill]] — sibling decision; the workload that produced the cost-economics data.
- [[ann-greed]] — Financial Controller; recipient of the weekly cost report.
