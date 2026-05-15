---
type: vendor
title: N8N
slug: n8n
air_id: AIR-19
status: Sandbox
labels: [Core Infrastructure, AI Policy, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-19/n8n
created: 2026-02-25
updated: 2026-04-21
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# N8N

> AI Registry entry [AIR-19](https://linear.app/janusd/issue/AIR-19/n8n) — status **Sandbox** as of 2026-04-21. Departments: —.

**Category:** Workflow Automation / Integration Platform
**Cost per User/Month:** $25.20 (Cloud starter)
**Number of Licences:** 1 (self-hosted)
**Total Monthly Cost:** ~$7-8 (Hostinger VPS share, AIR-79)
**Departments:** AI Policy, Technology

## Overview

Open-source workflow automation platform. Workflow backbone of Janus AI Office infrastructure — connects Fireflies, Linear, Notion, Slack, Google Workspace, AI model APIs. Selected over Make (AIR-20, Rejected) for flexibility, self-hosting, superior data manipulation.

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
