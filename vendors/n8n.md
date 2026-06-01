---
type: vendor
title: N8N
slug: n8n
air_id: AIR-19
status: Sandbox
labels: [Core Infrastructure, AI Policy, Technology]
departments: [ai-office, engineering]
url: https://linear.app/janusd/issue/AIR-19/n8n
created: 2026-02-25
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
confidence: medium
related: [hostinger, monday, 2026-04-22-self-host-n8n-on-hostinger, 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins, 2026-04-23-monday-hostinger-notion-stack-adopted]
migrated_from: entities/vendors/n8n.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# N8N

> AI Registry entry [AIR-19](https://linear.app/janusd/issue/AIR-19/n8n) — status **Sandbox** as of 2026-04-21. Departments: —.

**Category:** Workflow Automation / Integration Platform
**Cost per User/Month:** $25.20 (Cloud starter)
**Number of Licences:** 1 (self-hosted)
**Total Monthly Cost:** ~$7-8 ([[hostinger|Hostinger]] VPS share, [[hostinger|AIR-79]])
**Departments:** AI Policy, Technology

## Overview

Open-source workflow automation platform. Workflow backbone of Janus AI Office infrastructure — connects Fireflies, [[linear|Linear]], Notion, Slack, [[google-workspace|Google Workspace]], AI model APIs. Selected over [[make|Make]] ([[make|AIR-20]], Rejected) for flexibility, self-hosting, superior data manipulation.

## Capabilities

* Visual workflow builder
* 400+ integrations
* Code nodes (JS, Python) for custom logic
* AI agent nodes (OpenAI, Anthropic, Google AI)
* Webhook triggers
* Cron scheduling
* Error handling with retries
* Self-hosting on Hostinger Docker (AIR-79)
* Workflow versioning

## Hosting History — Key Decision

* **Feb-Apr 2026:** Self-hosted on GCP
* **17 Apr 2026:** Consolidation on GCP upheld (Operations Notebook #62)
* **20 Apr 2026 — REVERSED.** April GCP pilot billing surprise exposed opaque, non-forecastable unit costs (egress, per-request charges). Hostinger KVM VPS pricing significantly cheaper. Decision: move N8N to Hostinger VPS. Transparent fixed monthly pricing, Malaysia regional DC, Docker-native, one-click N8N app. GCP retained only for managed-service departmental projects.

## Security & Compliance

* Self-hosted on Hostinger VPS — full data sovereignty
* SOC 2 Type II (cloud version)
* Hostinger ISO 27001 with DPA
* Role-based access
* Credential encryption
* Audit logging

## Relevance

Automation engine tying together Janus AI infrastructure. Powers standup processing pipeline (Fireflies → N8N → Notion + Linear), meeting transcript analysis, cross-system sync, scheduled reporting. Self-hosting keeps workflow data within Janus-controlled infrastructure — critical for meeting transcripts and internal data.

*Deployed to AI Policy and Technology. Core Infrastructure tier. Self-hosted on Hostinger VPS (AIR-79); migrated from GCP on 20 Apr 2026.*

## Merged from `entities/vendors/n8n.md`

# n8n

Open-source workflow automation platform (Zapier-style). Self-hosted at Janus per the 2026-04-22 decision to self-host on [[hostinger]] rather than [[google-cloud|GCP]] — the per-trigger metering complexity of GCP was the trigger; n8n on Hostinger keeps automation costs predictable.

## Janus use

- Workflow glue for ingestion pipelines feeding the AI Office (Fireflies → Monday → wiki).
- Part of the three-tool stack adopted on 2026-04-23: [[monday]] (ops SoR) + [[hostinger]] (self-host substrate, including n8n) + [[notion]] (docs).

## Posture

Workflow automation isn't an AI tool (per the 2026-05-06 taxonomy decision — see [[2026-05-06-ai-tool-taxonomy-scope-policy]]), but n8n's role in stitching together AI tooling (webhook receivers for Fireflies, scheduled triggers for ingest jobs) makes it load-bearing operational plumbing. Retained where the work is plumbing; superseded by purpose-built [[agent-skills|Claude skills]] where the work is AI-shaped.

## Merged from `entities/vendors/n8n.md`

# n8n

Open-source workflow automation platform (Zapier-style). Self-hosted at Janus per the 2026-04-22 decision to self-host on [[hostinger]] rather than [[google-cloud|GCP]] — the per-trigger metering complexity of GCP was the trigger; n8n on Hostinger keeps automation costs predictable.

## Janus use

- Workflow glue for ingestion pipelines feeding the AI Office (Fireflies → Monday → wiki).
- Part of the three-tool stack adopted on 2026-04-23: [[monday]] (ops SoR) + [[hostinger]] (self-host substrate, including n8n) + [[notion]] (docs).

## Posture

Workflow automation isn't an AI tool (per the 2026-05-06 taxonomy decision — see [[2026-05-06-ai-tool-taxonomy-scope-policy]]), but n8n's role in stitching together AI tooling (webhook receivers for Fireflies, scheduled triggers for ingest jobs) makes it load-bearing operational plumbing. Retained where the work is plumbing; superseded by purpose-built [[agent-skills|Claude skills]] where the work is AI-shaped.
