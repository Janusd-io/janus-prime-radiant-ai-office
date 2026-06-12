---
type: vendor
title: Monday CRM (monday Sales CRM)
slug: monday-crm
created: 2026-06-12
updated: 2026-06-12
departments: [commercial, marketing, office-of-ceo]
status: active
confidence: high
sources: []
related: [monday, janus-crm-selection, attio, twenty-crm]
---

# Monday CRM (monday Sales CRM)

Dedicated CRM product from monday.com (NASDAQ: MNDY), built on the same Work OS platform as [[monday|Monday.com Work OS]] (AIR-83) but separately licensed and purpose-built for sales pipeline management. As of June 2026, an active candidate in the Janus CRM evaluation alongside [[attio|Attio]] and [[twenty-crm|Twenty CRM]]; decision expected week of 16 June 2026. Linear AIR-167 (Evaluating, Gate 1 PASS 2026-06-12).

**Disambiguation:** This entry covers the *CRM product* (`monday.com/crm`). For Monday.com Work OS (project management, task boards, automation execution), see [[monday]]. The earlier decision [[2026-05-06-monday-not-an-ai-tool]] referred to Work OS; Monday CRM is a distinct product with AI-native features (AI Sales Agent, AI Lead Agent, AI email composition).

## What it is

A user-facing CRM application — contacts, deals, accounts, activities as board-based objects — plus two-way email sync, sales forecasting, quote generation, and AI agents for lead enrichment and deal progression. The platform continuity argument: if Janus standardises on Monday.com Work OS for operations, CRM data and sales workflows live in the same environment — same identity provider, same automation engine, same Slack integration, same onboarding overhead.

## Key capabilities

- **Sales pipeline** — Unlimited customisable deal pipelines (Basic+); Kanban, table, timeline, calendar, chart, and map views
- **Email integration** — Two-way Gmail/Outlook sync (Standard+); templates, sequences, mass emails, open/click tracking
- **AI agents** — AI Sales Agent, AI Lead Agent, AI email composition, column autofill, sentiment analysis (higher tiers; exact pricing not fully published)
- **Forecasting** — Visual dashboards and quota tracking (Pro+)
- **Quotes & invoices** — Built-in module
- **Post-sales** — Account management boards connect directly to Work OS project boards for delivery handoff

## Pricing (as of 2026-06-12)

| Tier | Price/user/month | Notes |
|---|---|---|
| Basic | $12 | Unlimited pipelines; no email sync; no automations |
| Standard | $17 | Two-way Gmail/Outlook sync; 250 automation actions/month |
| Pro | $28 | Forecasting dashboards; 25,000 automation actions/month; Google SSO |
| Enterprise | Custom | SAML SSO; 250,000 automation actions/month; 1TB storage; AI agents fully unlocked |

3-user minimum across all paid plans. AI agent features (AI Sales Agent, AI Lead Agent) are on higher tiers — exact tier gate not fully published at time of evaluation.

## Integrations

- Google Workspace: two-way Gmail sync, Google Calendar, Google Drive, Google SSO (Pro+)
- Slack: native integration with automation templates
- Salesforce two-way sync; HubSpot, Outlook, LinkedIn Sales Navigator, Pipedrive
- Zapier / Make (5,000+ apps); 200+ native integrations via monday Apps Marketplace
- GraphQL API at [developer.monday.com](https://developer.monday.com/api-reference) — explicitly covers "monday sales CRM" product; AI-friendly llms.txt at developer.monday.com/llms.txt

## Security & compliance

- SOC 2 Type II (annual audit); ISO 27001, 27017, 27018, 27032, 27701; GDPR, CCPA, HIPAA
- Google SSO (Pro+); SAML 2.0 / Okta / Azure AD (Enterprise only)
- **Data training exclusion: unconditional** — "monday.com does not use your customer data or content to train its AI models, and does not allow others to do so." AI providers (AWS Bedrock, Azure AI, Vertex AI) under Zero Data Retention commitments. All plans, not gated to Enterprise. Per [AI FAQs](https://support.monday.com/hc/en-us/articles/23227256685842-AI-FAQs) and [Trust Centre](https://monday.com/trustcenter).
- Annual third-party penetration testing; 2026 report available at trust.monday.com

## Gate 1 assessment — 2026-06-12

All five Gate 1 criteria pass unconditionally (AIR-167 Gate 1 comment, 2026-06-12):

| Criterion | Result |
|---|---|
| G1.1 Google Workspace | ✅ PASS |
| G1.2 Slack | ✅ PASS |
| G1.3 Data portability | ✅ PASS |
| G1.4 Data training exclusion | ✅ PASS (unconditional) |
| G1.5 Documented API | ✅ PASS |

**Gate 1 decision: PASS.** Proceeds to Stage 2 Technical Qualification. Note for Stage 2: SAML SSO requires Enterprise tier — cost implication to confirm before G2.2 (Enterprise-Grade Authentication) assessment.

## Watch for

- CRM decision outcome week of 16 June 2026 — if Attio or Twenty CRM wins, this entry moves to Rejected; file `decisions/2026-06-XX-select-crm.md`
- AI agent tier pricing — not fully published; clarify before Stage 2 cost modelling
- Platform continuity discount — does existing Work OS (AIR-83) subscription carry any bundled or discounted CRM pricing?
- G2.2 flag: SAML SSO only on Enterprise; confirm whether Google SSO (Pro) is sufficient for Janus identity requirements
