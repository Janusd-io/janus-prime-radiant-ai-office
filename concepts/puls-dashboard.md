---
type: concept
title: PULS — Predictive Unified Live System
slug: puls-dashboard
created: 2026-05-14
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office, iso, it-ops]
sources: [plain-english-overview, jargon-decoder, parent-process, 04-formal-response]
related: [iso-ims-puls, iso-compliance-programme, ims-enrolment, ims-process-document-shape, simon-tarskih]
---

# PULS — Predictive Unified Live System

**PULS** (Predictive Unified Live System) is the live dashboard Janus is building to show the real-time status of every IMS process — the visible, monitored surface that turns the 20 written IMS documents into a continuously-evidenced compliance machine. As of 2026-05-14 PULS **does not exist yet** — the dashboard is to-be-built; the 20 IMS docs themselves are in flight via [[ims-enrolment]] department by department.

## What PULS is, in one sentence

A Next.js + Postgres + Vercel dashboard that reads from Notion (system of record for the 20 IMS docs), Linear (CAPA / audit), n8n on the [[hostinger-vps-sandbox|Hostinger VPS]] (automation signals), and the Claude API (predictive layer), and surfaces live KPI tiles + traffic-light status per process — filterable by entity (Dubai / SG / UK / future).

## The three properties — Live · Visible · Trusted

- **Live** — real-time. Status reflects what's actually happening, not a stale weekly export.
- **Visible** — anyone with access can inspect any process's evidence without asking.
- **Trusted** — built on the ISO standards (9001 + 27001 + 42001), so the dashboard's claims map to formal audit criteria.

## Why it matters

The pitch in Simon's deck: when the certification auditor shows up, Janus opens PULS and says "every process is green, here's the evidence" — instead of scrambling for weeks like every other company. The dashboard converts "audit-readiness" from an event into a continuous state.

This matters disproportionately for Janus because the certification target is **one certificate covering Dubai + Singapore + UK + future entities** (not separate audits per country). PULS lets a single auditor inspect every jurisdiction under one engagement.

## Proposed stack (Jehad's recommendation per [[parent-process|First Voice formal response]])

Deliberately reuses existing production tooling so PULS v1 ships in days not weeks:

- **System of record:** Notion (the 20 IMS docs live here; per Simon's deck slide 6)
- **Automation:** n8n on the Hostinger VPS (already live)
- **Build / run platform:** Next.js + Vercel + Neon Postgres
- **CAPA / audit:** Linear
- **Predictive layer:** Claude API + AI Gateway
- **Comms:** Slack

Rough cost: ~$90-190/mo. Estimated timeline: 8 weeks to Dubai pilot.

## Status (2026-05-14)

- Dashboard not yet built; awaits the AI/IT tooling-decision meeting (slide 17 Step 4) where the stack is locked in. Jehad has volunteered to lead that meeting.
- The 20 IMS process documents are produced department-by-department via [[ims-enrolment]] — AI Department is the worked example shipping today.
- KPI definitions per process are partial — most departments don't track formal KPIs yet; Simon is helping formalise pass/fail thresholds, measurement frequency, and target values so PULS can monitor automatically.

## What it isn't

- Not a GRC platform purchase. The whole point is to avoid the cost / lock-in of off-the-shelf GRC tools.
- Not the IMS itself. The IMS is the 20 process docs + 11 IMS Manual policies; PULS is the *monitoring surface* on top of them.
- Not where work actually happens. Notion / Linear / Monday / n8n remain authoritative for their domains — PULS reads from them.
