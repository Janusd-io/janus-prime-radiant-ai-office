---
type: decision
title: Per-workstream Claude API keys with weekly cost reporting to HR + finance
slug: 2026-05-07-per-workstream-api-keys-cost-monitoring
created: 2026-05-07
updated: 2026-05-13
departments: [ai-office, finance, hr]
status: resolved
owner: jehad-altoutou
sources: [pr-backup-2026-05-11-decision-2026-05-07-per-workstream-api-keys-cost-monitoring]
related: [claude-code, ann-greed, hr-recruitment-pipeline]
audience: [department]
captured_by: jehad-altoutou
---

# Per-workstream Claude API keys + weekly cost reporting

**Decision date:** 2026-05-07. **Decided by:** Michael Bruck, Jehad Altoutou.

## What

Each AI Office workstream gets its own [[claude-code|Claude]] API key. A weekly cost report goes to HR and finance ([[ann-greed]]) showing per-workstream consumption.

## Why

- Granular billing enables accurate cost-allocation per workstream (recruitment, marketing, IT, etc.).
- First production scoring run on the recruitment pipeline measured **$1.12 per CV / 116k tokens** — small per-unit, but at agency-batch scale ($30/batch) it adds up. Without per-workstream visibility, cost surprises arrive unattributed.
- Finance gets a clean cost-attribution surface; HR gets visibility into recruitment automation's running cost.

## Implications

- Implementation queued (per the 2026-05-07 standup — owner: Jehad, due 13 May).
- Pattern generalises: any workstream that goes to production gets its own API key. The recruitment pipeline is first; the Singapore news bot, marketing CRM tooling, and IT helpdesk triage bot follow.
- Sets a baseline for finance-side governance of AI tooling spend, complementing the AI Policy gate.

## Related

- [[hr-recruitment-pipeline]] — first workstream to exercise the pattern.
- [[ann-greed]] — Financial Controller; recipient of the weekly cost report.
