---
type: decision
title: Notion accounts restricted to AIO — no broad rollout
slug: 2026-05-11-notion-restricted-to-aio-no-broad-rollout
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office, it-ops, office-of-ceo]
status: resolved
owner: bonaventure-wong
decided_by: bonaventure-wong
sources: [2026-05-11-aio-standup-with-jehad]
related: [bonaventure-wong, michael-bruck, jehad-altoutou, euclid-wong, notion, 2026-05-06-notion-role-shift-journal-not-knowledge-base, janus-prime-radiant-build]
---

# Notion accounts restricted to AIO — no broad rollout

## Decision

[[bonaventure-wong|Bonaventure]] has ruled that Janus will not add additional [[notion|Notion]] accounts beyond the AI Office's existing paid seats. The AIO's Operations Notebook stays in Notion (where it's load-bearing for the [[standup|/standup]] skill journal); other departments and individuals should not be onboarded to Notion. Non-AIO users who need shared-document collaboration should use Google Drive shared folders and — increasingly — the [[janus-prime-radiant-build|Prime Radiant]] wiki pattern instead.

Restated in the 11 May 2026 AIO standup, with the reasoning attributed to Bonaventure. Verbatim from the meeting (speaker unattributed): *"I'm not adding anybody after Bonaventure said nobody gets — we don't have a Notion at janusdigital.io. In fact, I just had to pay our Notion bill."*

## Why

- **Tool sprawl restraint.** Janus is in active tool consolidation mode (per [[2026-04-23-monday-hostinger-notion-stack-adopted|the Monday + Hostinger + Notion stack decision]]); Notion's role has been narrowed to the AIO journal surface ([[2026-05-06-notion-role-shift-journal-not-knowledge-base]]). Spreading Notion to additional departments cuts against that consolidation.
- **Cost.** Notion seats add up; the existing paid plan covers AIO's needs and no more.
- **IT support boundary.** Per the standup discussion, [[euclid-wong|Euclid]] does not support Notion for company-wide use. Adding more accounts would push support burden onto IT without a clear consumer of the value.
- **Substitution path is real.** For shared-document collaboration, Google Drive shared folders are already in use (the Prime Radiant vault itself sits on a Shared Drive). For durable institutional knowledge, the Prime Radiant Markdown pattern is the explicit successor surface.

## Scope

Affects:
- New Notion seats for non-AIO individuals → not added.
- Departments asking to use Notion as a workspace → routed to Drive + Prime Radiant.
- [[andrey-timokhov|Andre]] is observed to have a Notion account (per the meeting, believed to be personal); not part of the company account.

Does not affect:
- The AIO Operations Notebook itself — stays in Notion; load-bearing for `/standup`.
- The AIO's paid Notion subscription — continues.
- Future re-evaluation — if the AIO's wiki-vs-Notion balance shifts further (durable knowledge migrates fully to wiki; Notion role narrows further), Notion subscription scope may shrink, but that's a separate decision.

## Implications for the Prime Radiant rollout

This decision is upstream of the [[janus-prime-radiant-build|Prime Radiant rollout]]: as departments grow institutional-knowledge needs, the wiki pattern is the only blessed substrate. Marketing's instance ([[marketing-prime-radiant]]) is already a Prime Radiant; the queued HR / Finance / IT-Ops / Office-of-CEO instances will be Prime Radiants, not Notion workspaces. Validates the rollout strategy.

## Related

[[notion]] · [[2026-05-06-notion-role-shift-journal-not-knowledge-base]] · [[2026-04-23-monday-hostinger-notion-stack-adopted]] · [[janus-prime-radiant-build]]
