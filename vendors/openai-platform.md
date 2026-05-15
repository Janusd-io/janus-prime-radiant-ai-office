---
type: vendor
title: OpenAI Platform
slug: openai-platform
air_id: AIR-86
status: Sandbox
labels: [AI Office Infrastructure, AI Policy]
departments: [ai-office]
url: https://linear.app/janusd/issue/AIR-86/openai-platform
created: 2026-04-21
updated: 2026-04-21
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[ai-office]]


# OpenAI Platform

> AI Registry entry [AIR-86](https://linear.app/janusd/issue/AIR-86/openai-platform) — status **Sandbox** as of 2026-04-21. Departments: ai-office.

**Category:** AI Model API Platform / Developer Console
**Cost per User/Month:** Usage-based (token-metered); no per-seat fee. GPT-5.4 $2.50/1M input, $15/1M output; mini $0.75/$4.50; nano $0.20/$1.25. Tool fees (web search $10/1k). Batch API = 50% discount.
**Number of Licences:** 1 (organisation)
**Departments:** AI Policy

## Overview

OpenAI's developer console and API billing surface — programmatic access to GPT-5.x family, reasoning models, realtime, image, embeddings, audio, Codex. Plus prompt engineering, fine-tuning, evaluations, agent building, fine-grained cost/usage governance at Project level. OpenAI's equivalent of [[google-ai-studio|Google AI Studio]] ([[google-ai-studio|AIR-8]]) — operator-facing counterpart to consumer [[chatgpt|ChatGPT]] ([[chatgpt|AIR-41]]).

## Capabilities

* Model API: Responses, Chat Completions, Realtime, Images, Audio (STT/TTS), Embeddings, Moderation, Fine-tuning
* Playground — browser IDE for prompt iteration, model comparison
* Projects — isolate API keys, rate limits, spending caps per workstream
* Evals framework
* Agents & Tools: Web Search, Code Interpreter, File Search, function calling
* Batch API — 24hr async at 50% discount
* Service Tiers: Standard, Priority, Flex, Scale, Reserved
* Fine-tuning & Distillation

## Integrations

* Official SDKs: Python, Node.js, .NET, Java, Go
* Direct integration with N8N ([[n8n|AIR-19]]), [[dify|Dify]] ([[dify|AIR-22]]), [[pipedream|Pipedream]] ([[pipedream|AIR-78]])
* SSO/SAML for org login (Enterprise)
* MCP support in Responses API
* Usage/billing export via API

## Security & Compliance

* SOC 2 Type 2, GDPR
* Data residency — EU/US (+10%)
* Zero Data Retention (ZDR) for eligible enterprise
* API data not used for training by default
* HIPAA BAAs available under enterprise
* SSO/SAML, SCIM, per-project API key scoping
* ISO 27001, 27017, 27018, 27701; CSA STAR Level 1

## Relevance

Org-level account for building/piloting/operating OpenAI-powered automations. Mirrors Google AI Studio (AIR-8) relationship with [[gemini|Gemini]]. Prerequisite for downstream OpenAI-dependent tools (Codex [[openai-codex|AIR-84]], N8N/Dify/Pipedream workflows). Without governed platform account, developers would use personal keys — policy breach under §5.2.3.

## Considerations

* Usage-based billing — set conservative monthly budget BEFORE opening keys
* DPA / data residency decision needed before non-public data
* Overlap with Gemini ([[google-gemini|AIR-5]], AIR-8) — justify incremental spend
* Key hygiene — all access via OpenAI Projects with named owners and spend caps
* Sandbox scope — no confidential/client data until promoted to Production

*Sandbox. AI Office Infrastructure tier.*
