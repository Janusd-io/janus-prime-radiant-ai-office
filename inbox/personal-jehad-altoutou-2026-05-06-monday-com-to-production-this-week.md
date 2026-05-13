---
type: decision
title: Push Monday.com from sandbox to production this week (CRM lock-in same window)
slug: 2026-05-06-monday-com-to-production-this-week
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, it-ops, marketing]
status: resolved
owner: michael-bruck
sources: [pr-backup-2026-05-11-decision-2026-05-06-monday-com-to-production-this-week]
related: [monday-com, crm-evaluation, ai-tool-evaluation-framework]
audience: [department]
captured_by: jehad-altoutou
---

# Push Monday.com to production this week; CRM lock-in same window

**Decision date:** 2026-05-06. **Decided by:** Michael Bruck, Jehad Altoutou.

## What

Two paired actions for this week (target 2026-05-08), while Bonaventure is away:
1. Promote [[monday-com]] from sandbox to production — the first concrete sandbox→production promotion in the new IT hand-off process.
2. Lock CRM direction with Euclid + Andrew + Bonaventure before Bonaventure's departure.

## Why

- The Monday.com sandbox status has been blocking downstream rollouts (e.g., the standup skill rollout to non-AIO users). Promotion unblocks it.
- CRM lock-in is time-critical: Bonaventure is away soon, and the CRM choice has to be made with him in the room. The window is now or post-return; now is operationally easier.
- Both actions exercise the IT hand-off template that's currently being drafted — they're the first real test of that template.

## Implications

- IT hand-off template gets validated against a live promotion this week (sandbox→production checklist: usability, security, webhook).
- Password / user-ID issuance workflow via Euclid + Andre is a downstream task in the same template.
- CRM direction will be reflected in Linear AIR once locked — likely a Stage 1 or Stage 2 [[ai-tool-evaluation-framework]] outcome.

## Reversal / failure modes

- If the promotion exposes a hand-off-template gap, capture as a `lessons/` page rather than rolling back. The point is to learn the template by using it.
