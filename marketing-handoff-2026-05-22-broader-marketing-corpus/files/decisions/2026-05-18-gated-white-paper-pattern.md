---
type: decision
title: White paper is gated behind email capture, no preview or direct download link
slug: 2026-05-18-gated-white-paper-pattern
created: 2026-05-18
updated: 2026-05-18
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
departments: [marketing, ai-office]
confidence: high
related: [janus-website, andrew-soane, 2026-05-14-janus-singapore-white-paper-storms-ahead, crm-evaluation-and-selection]
---

## Decision

The Janus Digital "[[2026-05-14-janus-singapore-white-paper-storms-ahead|How agentic AI can answer the storms ahead]]" white paper on `/insights/white-paper` is **gated** behind an email-capture form. The page has **no "Open the PDF" button** and **no inline preview iframe**. The only path to the PDF is form submission.

Submission writes the lead to Google Sheets (service-account auth, columns A–I: timestamp, name, email, company, role, consent, source, referer, ip) and triggers a Resend email with the PDF link.

## Why

Jehad's framing: *"we need them to click on email it to me so they can fill the form — this way they get the white paper in their email address they mentioned in the form and we get them in database as leads."*

Every reader is captured as a lead. This is the entire purpose of having a white paper as Phase-1 marketing infrastructure — the document is the bait, the form is the trap, the Sheet is the (interim) CRM.

## Trade-offs accepted

- We will lose some impatient readers who won't fill a form. That's fine — we want qualified leads who'll trade an email for the doc, not pageviews.
- The Sheets backend is interim. When HubSpot (or whatever CRM wins the [[crm-evaluation-and-selection]] evaluation) lands, the form fan-out doubles to Sheets + CRM before cutting over fully.

## How this implements

- `/insights/white-paper` shows: hero, table of contents (read-only), the email-capture form. That's it.
- Form `POST /api/white-paper` → Zod validates → Google Sheets append → Resend sends email with `WHITE_PAPER_URL` link.
- The PDF itself sits at `web/public/janus-white-paper.pdf` so the link can resolve to `https://janusd.com/janus-white-paper.pdf` once deployed.

## What to do with this decision

If someone tries to add a "preview PDF" or "download without form" button on this page — point them here. The whole page is engineered to force the gate.
