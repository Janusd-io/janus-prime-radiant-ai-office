---
type: vendor
title: Mailchimp
slug: mailchimp
created: 2026-05-15
updated: 2026-05-19
departments: [marketing]
status: active
confidence: medium
sources: [AIO-100, AIR-111, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting]
related: [resend, agentic-lean-marketing-stack, marketing-prime-radiant]
migrated_from: entities/vendors/mailchimp.md
---
Mailchimp is an all-in-one email marketing platform owned by Intuit, offering email campaign builder, audience segmentation, automation workflows, A/B testing, and analytics. It serves over 13 million users and is widely used for newsletter marketing, drip campaigns, and customer lifecycle communications.

## Status (as of 2026-05-19)

**Hold open.** Linear AIR-111 status moved Rejected → Backlog at Andrew's request. Andrew has not yet decided whether Mailchimp is needed for the broadcast / campaign email layer of the [[agentic-lean-marketing-stack|marketing stack]] — the question is whether [[resend|Resend's]] new Broadcasts feature is enough to obviate the need for a dedicated marketing email tool. Decision deferred to after the Singapore launch settles, when Andrew can evaluate operational ergonomics with real campaigns.

## Boundary with Resend

Per the [[2026-05-19-aio-mktg-meeting]]:

- [[resend|Resend]] = programmatic / transactional.
- Mailchimp (if adopted) = broadcast / marketing campaigns.

If Mailchimp is dropped, Resend Broadcasts covers the broadcast layer. If Mailchimp is adopted, the two are complementary, not redundant.

## Registry

- Linear AIR: AIR-111 — Backlog (status reverted from Rejected on 2026-05-19 at Andrew's request).
- Prior entry: AIO-100 (superseded).

## Watch for

- Andrew's post-Singapore-launch evaluation: does he prefer Mailchimp's UI for the 6-email nurture series, or operate via Resend Broadcasts directly?
- If Mailchimp comes back into scope, re-run Gate 1 (the earlier evaluation flagged G1.4 ToS training exclusion gap and G1.1 Google Workspace integration confirmation needed).
