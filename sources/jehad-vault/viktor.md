---
type: vendor
title: Viktor
slug: viktor
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: archived
confidence: medium
sources: [jehad-vault-import-2026-05-13]
related: [ai-tool-evaluation, victor]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `entities/vendors/viktor.md` — this file is preserved as a source for divergent framing / additional context._

# Viktor

AI agent / integration platform evaluated at Janus and **rejected** in Linear AIR-38 on 2026-04-22. Page retained because the rejection drove a durable evaluation policy. Existing vault page `victor.md` is the same vendor under a misspelled slug; flagged for dedup.

## Why it was rejected

The evaluation surfaced that Viktor's access model did not enforce per-user, source-platform-faithful data access — a hard requirement for any agent or integration platform that touches user-scoped enterprise data. This rejection became the precedent for a Gate 1 / Gate 2 policy line in [[ai-tool-evaluation]]: agent platforms that flatten or escalate user-level access privileges are out before deeper review.

## Status

Rejected. Not under reconsideration as of 2026-05-07. If Viktor revises its access model, this page would be the place to track the change.

## Watch for

- Any product update from Viktor specifically addressing per-user access scoping.
- Other agent platforms surfacing the same access-model gap during evaluation — Viktor is the precedent case.
