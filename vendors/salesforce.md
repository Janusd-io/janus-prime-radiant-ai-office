---
type: vendor
title: Salesforce
slug: salesforce
air_id: AIR-93
status: Evaluating
labels: [Marketing, Commercial, Functional]
departments: [marketing]
url: https://linear.app/janusd/issue/AIR-93/salesforce
created: 2026-05-05
updated: 2026-06-12
captured_by: jehad-altoutou
sources: [2026-06-09-salesforce-janus-digital-global]
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[marketing]]


# Salesforce

> AI Registry entry [AIR-93](https://linear.app/janusd/issue/AIR-93/salesforce) — status **Evaluating** as of 2026-05-05. Departments: marketing.

**Category:** CRM / Customer Relationship Management Platform (enterprise gold standard) — BENCHMARK only
**Cost:** Sales Cloud — Starter ~$25; Pro ~$100; Enterprise ~$165; Unlimited ~$330; Einstein 1/Agentforce $500+. Implementation 1.5-3x licence cost year 1.
**Departments:** Commercial, Marketing — benchmark only, NOT adoption candidate
**Entity:** NYSE: CRM. Founded 1999, HQ SF. Used by majority of Fortune 500.

## Overview

Global market-leading CRM platform. De facto enterprise gold standard against which all other CRMs (HubSpot, [[attio|Attio]], Monday CRM, Microsoft Dynamics) are measured. Spans Sales Cloud, Service Cloud, Marketing Cloud, Commerce Cloud, Data Cloud, Tableau, MuleSoft, Slack, Einstein/Agentforce AI layer.

## Key Products

* **Sales Cloud** — lead, contact, opportunity, pipeline, forecast, territory; CPQ
* **Service Cloud** — omni-channel cases, KB, field service, AI agent productivity
* **Marketing Cloud** — journey orchestration, segmentation, personalisation
* **Data Cloud** — real-time CDP with zero-copy to Snowflake, [[databricks|Databricks]], BigQuery
* **Einstein AI / Agentforce** — Copilot, GPT, autonomous service/sales agents on Einstein Trust Layer
* **Tableau & Pulse** — embedded analytics with AI insights
* **MuleSoft** — enterprise integration/API management
* **AppExchange** — 5,000+ certified partner apps
* **Industry Clouds** — Financial Services, Health, Public Sector, Manufacturing

## Security

* SOC 1/2 Type II, SOC 3, ISO 27001/27017/27018/22301
* HIPAA, PCI-DSS Level 1, FedRAMP (Mod/High Gov Cloud Plus), IRAP, C5, ENS, TX-RAMP
* GDPR/UK GDPR, EU Data Residency (Hyperforce)
* Shield Platform Encryption, BYOK
* Einstein Trust Layer — zero data retention, PII masking, audit trail

## Janus Strategic Position

**Benchmark / comparison anchor in Andrew's CRM AI analysis matrix — NOT a likely adoption candidate.** Sets the ceiling for what a CRM can do. Comparing HubSpot/Attio/Monday against Salesforce frames trade-offs Janus is making: how much CRM capability sacrificed, at what cost saving, by choosing lighter platform.

Michael's note: "gold standard but probably too expensive/large." Janus as mid-stage digital consultancy almost certainly cannot justify Salesforce licence economics, implementation (3-9 months), or dedicated admin/developer resourcing.

## Considerations

* **Cost** — TCO 5-10x sticker; minimum viable Sales Cloud $50-150k year 1
* **Complexity** — dedicated Salesforce admin/developer required
* **Implementation** — 3-9 months vs weeks for HubSpot/Attio
* **Overlap risk** — significantly with HubSpot, Attio
* **Workforce maturity** — Salesforce skills need to be hired or trained (multi-year)
* **Lock-in** — heaviest data model investment of any major CRM

## Discovery call — 9 Jun 2026

Salesforce (Sam + Yasmin, Dublin tech-sector team covering Middle East) <> Janus (Andrew Soane, Michael Bruck, Jehad Altoutou, DXB office). Source: [[2026-06-09-salesforce-janus-digital-global]]. Speaker labels are room labels (shared mic) — quotes below rely on internal consistency, attribution `transcript-only`.

- **Process friction is the headline.** Salesforce insists on its own evaluation sequence — scoping call with a technical resource → tailored demo → implementation planning + commercials — and explicitly declines to demo without scoping ("we don't do demos [from this team]; we've got solution engineers that run the demos"). Andrew pushed back hard, asking for a standard CRM demo that week; rep conceded only after Andrew flagged this as the third conversation without a demo and cited "big bloated machine" internal pushback.
- **Standalone-CRM aversion.** Rep: Salesforce "walks away from solo CRM projects" — wants full-ecosystem (Data Cloud, Tableau, MuleSoft, Agentforce) engagements. Direct tension with Janus's start-small intent (~5 licences at signing, scale with country openings — 30 countries by end-2027 per the call).
- **Pragmatic concessions offered:** CRM-only demo + fast pricing; implementation partner suggestion (Matthew Ansley, reportedly Claude-using) to keep setup under ~$20k; pitched Anthropic's own Salesforce pattern (Salesforce as system of record, Claude as engagement layer) as alignment with Janus's Claude/Slack-mediated architecture.
- **Next step:** Andrew to send the CRM requirements list ([[crm-requirements-high-level]]); demo + commercial conversation targeted within the week. Janus stated timeline: shortlist 3 of 4 vendors, decision the following week.
- **Read-across:** the call validates the existing "Considerations" above — process weight and ecosystem-bundling pressure showed up pre-sale. Whether Salesforce stays in the shortlist after this friction is recorded in [[janus-crm-selection]].

*Evaluating. Functional tier. Benchmark/comparison anchor in Andrew Weekly 5 May 2026 CRM matrix; live discovery call 9 Jun 2026 as part of the June evaluation sprint.*
