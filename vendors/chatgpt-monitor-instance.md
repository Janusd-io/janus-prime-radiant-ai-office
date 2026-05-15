---
type: vendor
title: ChatGPT (Monitor instance)
slug: chatgpt-monitor-instance
air_id: AIR-85
status: Monitor
labels: [Core Infrastructure]
departments: []
url: https://linear.app/janusd/issue/AIR-85/chatgpt
created: 2026-04-21
updated: 2026-04-21
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# [[chatgpt|ChatGPT]] (Monitor instance)

> AI Registry entry [AIR-85](https://linear.app/janusd/issue/AIR-85/chatgpt) — status **Monitor** as of 2026-04-21. Departments: —.

**Category:** Foundation Model / General-Purpose AI Assistant
**Cost:** Free; Go ~$8; Plus $20; Pro $200; Business $25/user (annual) or $30 (monthly); Enterprise custom
**Departments:** All (under review)
**Entity:** OpenAI

## Overview

Market-leading AI chatbot — broad enterprise adoption across consulting/legal/finance/marketing/engineering. Currently GPT-5.3/5.4. Tiered free → Enterprise.

## Key Products

* GPT-5.3 Instant + GPT-5.4 Thinking/Pro (context 54K-400K)
* Apps & Connectors — 60+ including Slack, Drive, SharePoint, GitHub, [[asana|Asana]]
* Deep Research & Agent Mode — autonomous multi-step
* Codex — integrated coding (Business/Enterprise expanded usage)
* Projects, Tasks, Custom GPTs
* Canvas, Data Analysis, Vision, Voice, Image Generation
* Company Knowledge (Business/Enterprise) — internal data grounding
* ChatGPT Record Mode — meeting transcription

## Security & Compliance

* SOC 2 Type 2 (Business/Enterprise)
* ISO 27001/27017/27018/27701 (Enterprise only)
* No training on business data by default (Business/Enterprise)
* AES-256 at rest, TLS 1.2 in transit
* Data residency: US, EU, UK, Japan, Canada, Korea, Singapore, India, Australia, UAE (Enterprise only)
* Enterprise Key Management (EKM), IP allowlisting, compliance API logs
* SAML SSO, SCIM, RBAC

## Why Monitor

Almost certainly already in informal use across Janus (free/personal accounts outside managed procurement). Monitor status allows AI Office to:

1. Assess **shadow-IT exposure**
2. Measure actual organisational dependency
3. Decide whether to formalise Business/Enterprise tenancy aligned with §5.2.3

Given [[google-gemini|Google Gemini]] is approved Core Infrastructure foundation model, question is whether ChatGPT is genuinely required alongside (dual-stack), should be consolidated into [[gemini|Gemini]], or specific teams have justified retention case.

## Considerations

* **Shadow IT exposure** — free/personal tier use violates §5.2.3 if internal/client data entered
* **Overlap with Google Gemini** — clear rationale needed
* **Overlap with [[claude-code|Claude Code]] (Codex) and Fireflies (Record Mode)** — duplicates already-approved tools
* **Multi-region pricing variance** — published AED pricing (UAE) diverges from USD list
* Only Enterprise tier offers UAE data residency — material for Country operations
* Individual paid tiers (Plus, Pro, Go) train on user data unless explicitly opted out

*Monitor. Core Infrastructure tier (under review). Distinct from [[chatgpt|AIR-41]] (also ChatGPT, Sandbox).*
