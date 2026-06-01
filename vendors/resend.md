---
type: vendor
title: Resend
slug: resend
created: 2026-05-15
updated: 2026-05-19
departments: [it-ops, marketing]
status: active
confidence: high
sources: [AIO-101, AIR-118, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting]
related: [mailchimp, agentic-lean-marketing-stack, stack-composition-framework, singapore-launch, marketing-prime-radiant]
migrated_from: entities/vendors/resend.md
---
Resend is a developer-focused transactional email API platform offering high deliverability, React-based email templating, domain authentication, and detailed analytics. It targets engineering teams building product-triggered emails and has grown rapidly as an alternative to SendGrid and Mailgun.

## Status (as of 2026-05-19)

Confirmed for transactional email in the [[agentic-lean-marketing-stack|marketing stack]]. Already in place for the Singapore campaign. Scores 3/3 on the [[stack-composition-framework]] (REST-first API, mature CLI, agent-operable). AIR-118 in Linear (AI Registry) — comment added 2026-05-19 on transactional vs broadcast boundary with MailChimp.

## Transactional vs broadcast — boundary

Per [[2026-05-19-aio-mktg-meeting]]:

- **Resend = programmatic / transactional.** Already integrated for Singapore campaign auto-reply (white paper attachment delivery).
- **[[mailchimp|MailChimp]] = broadcast / marketing campaigns.** Status held open (Rejected → Backlog) pending Andrew's decision.
- The two are complementary if both adopted. But: Resend now also has **Broadcasts** for marketing campaigns — meaning Janus may not need to add Mailchimp at all. To revisit after Singapore launches, based on whether Andrew prefers a dedicated marketing UI.

## Registry

- Linear AIR: AIR-118 (current) — Backlog. Prior entry AIO-101 superseded.
- Requested by: AI Office / Marketing team

## Watch for

- Andrew's post-Singapore-launch decision on Resend Broadcasts vs MailChimp for the 6-email nurture series.
- Free tier is generous but production should be on the paid tier for support coverage.
