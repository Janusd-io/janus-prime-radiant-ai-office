---
type: vendor
title: Viktor
slug: viktor
created: 2026-05-07
updated: 2026-05-13
departments: [ai-office]
status: archived
confidence: medium
sources: [air-38, jehad-vault-viktor]
related: [ai-tool-evaluation, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms]
---

# Viktor

AI agent / integration platform evaluated at Janus and **rejected** in Linear AIR-38 on 2026-04-22. Page retained because the rejection drove a durable evaluation policy — see [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]].

## Why it was rejected

The evaluation surfaced that Viktor's access model did not enforce per-user, source-platform-faithful data access — a hard requirement for any agent or integration platform that touches user-scoped enterprise data. This rejection became the precedent for a Gate 1 / Gate 2 policy line in [[ai-tool-evaluation]]: agent platforms that flatten or escalate user-level access privileges are out before deeper review.

## Status

Rejected. Not under reconsideration as of 2026-05-07. If Viktor revises its access model, this page would be the place to track the change.

## Watch for

- Any product update from Viktor specifically addressing per-user access scoping.
- Other agent platforms surfacing the same access-model gap during evaluation — Viktor is the precedent case.

## Funding update — 2026-05-20

Viktor raised a $75M Series A led by Accel (largest Series A ever by a Polish tech company). Angel checks from Stewart Butterfield & Cal Henderson (Slack co-founders), Victor Riparbelli (Synthesia), Guillermo Rauch (Vercel), Mati Staniszewski (ElevenLabs), Nat Friedman (former GitHub). Reached $15M ARR in 10 weeks post-broader-access; 12,000+ corporate teams currently on platform.

Use case framing: "first true AI employee" — autonomous Slack/Teams teammate that produces completed work products rather than conversational responses. Connecting to 3,000+ workplace tools.

**Status stays `archived` for Janus.** The funding round does not change the underlying [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms|per-user data control gap]] that drove the original rejection. The release notes for the funding round explicitly call out "stricter role-based access controls, per-user data isolation, and localized data residency measures" as **future** ("later this year") roadmap items — confirming the gap is real and still unaddressed.

If those roadmap items ship and are verified, that would be the reconsideration trigger. Until then, the rejection holds.

Sources: [[2026-05-20-ventureburn-viktor-series-a-75m]], [[2026-05-20-forbes-viktor-series-a-75m]]
