---
type: vendor
title: Viktor
slug: viktor
air_id: AIR-38
status: Rejected
labels: [Functional]
departments: [ai-office]
url: https://linear.app/janusd/issue/AIR-38/viktor
created: 2026-02-25
updated: 2026-05-13
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
sources: [air-38, jehad-vault-viktor, 2026-04-22-it-team-meeting]
confidence: medium
related: [ai-tool-evaluation, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms]
migrated_from: entities/vendors/viktor.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Viktor

> AI Registry entry [AIR-38](https://linear.app/janusd/issue/AIR-38/viktor) — status **Rejected** as of 2026-05-04. Departments: —.

**Category:** AI Agent Platform (In-Slack Coworker)
**Status:** REJECTED (2026-04-22) → account deleted 2026-05-04
**Cost:** Free Tier; $50 Pro; ~$250 Enterprise
**Departments:** Technology, AI Policy, Commercial

## Evaluation Summary

* **Gate 1 (Baseline):** PASS (G1.1-G1.5)
* **Gate 2 (Technical):** PASS (Score 23/25)
* **Gate 3 (Sandbox):** Initiated; **failed on per-user data-control architecture**

## Rejection — Per-user data control failure

Sandbox evaluation in #viktor-evaluation Slack channel (2026-04-03, with Michael Bruck, Jehad Altoutou, Andrey Timokhov) surfaced **structural data-control issue:**

* **Integrations connected per-user but used workspace-wide.** Michael connects Drive/Notion/[[linear|Linear]]; once connected, EVERY authorised channel member can invoke those integrations
* **Integration runs under connecting user's permissions, not requesting user's.** Viktor explicitly does NOT enforce source-platform access boundaries. If User C is in channel but has no Notion account, they can still pull Notion data via Viktor.
* **First-line defence is workspace allow-list, not per-tool ACLs.** Per-call approval doesn't scale and doesn't enforce source platform's access model.

Viktor's own direct response: *"Short answer: yes, User C could access Notion data through me."*

This is the **wrong shape of access control** for multi-user, multi-jurisdiction consultancy where Notion/Drive/Linear access boundaries are deliberately differentiated by team and project.

## Account Deletion (2026-05-04)

Triggered by $50 Pro tier payment coming due. Reasons stated:
* Does not fit Janus requirements
* Requires more role-based account controls to data sources

## Lessons Captured (Future Evaluations)

Per-user, source-platform-faithful access control is a **HARD REQUIREMENT** for any AI agent/integration platform at Janus:

1. Integration must run under REQUESTING user's permissions, not connecting user's
2. Source-platform access boundaries (Notion page permissions, Drive ACLs, Linear team membership) must be honoured in full
3. Workspace allow-list + per-tool approval are NOT substitutes for proper per-user data-source ACLs

**Now a Gate 1 / Gate 2 criterion for all future agent platform evaluations.**

*Rejected.*

## Merged from `entities/vendors/viktor.md`

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

## Merged from `entities/vendors/viktor.md`

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
