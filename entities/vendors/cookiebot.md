---
type: vendor
title: Cookiebot
slug: cookiebot
created: 2026-06-01
updated: 2026-06-01
departments: [marketing, it-ops]
status: active
confidence: medium
sources: [marketing-stack-technical-writeup, agentic-lean-marketing-stack]
related: [cloudflare, janus-website-cms, singapore-launch, agentic-lean-marketing-stack]
---

# Cookiebot

**Category:** Cookie Consent & Privacy Compliance
**AIR:** AIR-124
**Stack Composition score:** TBD (procurement target 2026-06-02)

Cookiebot is a cookie consent management platform (CMP) that auto-scans websites for cookies, classifies them, and presents GDPR/ePrivacy-compliant consent banners. Selected as the compliance layer for the Janus Singapore marketing launch; procurement due 2026-06-02 as a pre-launch legal dependency.

## Role in the Janus marketing stack

Legal pre-requisite before paid traffic goes live on the Singapore landing pages. The Singapore launch campaign (planned for the July → September rescheduled luncheon) requires GDPR-compliant cookie consent for any EU/SG data-subject visitors. Cookiebot provides: auto-scan of all cookies loaded on the site, categorised consent (necessary / statistics / marketing / preferences), a customisable banner, and a compliance record.

## Alternatives considered

The [[agentic-lean-marketing-stack]] brief notes this as "commodity tooling" — Andrew can pick. Alternatives: Iubenda, OneTrust (enterprise), hand-rolled consent banner. Cookiebot selected for: ease of integration (single script tag), CMO-familiar UI for consent reporting, and competitive pricing at startup tier.

## Watch for

- Procurement completion by 2026-06-02 (Singapore campaign legal dependency).
- Integration with Google Analytics (AIR-125) — Cookiebot blocks GA until analytics consent is granted; test the consent → analytics event flow before paid traffic.
- GDPR vs. PDPA alignment: Singapore's Personal Data Protection Act has slightly different requirements from EU GDPR; confirm Cookiebot's SG-specific configuration.
