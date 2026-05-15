---
type: vendor
title: MiniMax
slug: minimax
air_id: AIR-71
status: Backlog
labels: [Technology, Functional]
departments: []
url: https://linear.app/janusd/issue/AIR-71/minimax
created: 2026-04-06
updated: 2026-04-06
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# MiniMax

> AI Registry entry [AIR-71](https://linear.app/janusd/issue/AIR-71/minimax) — status **Backlog** as of 2026-04-06. Departments: —.

**Category:** Foundation Model / Multimodal AI Platform
**Status:** Backlog
**Cost:** Free tier; API usage-based; Enterprise TBD
**Departments:** Technology
**Entity:** Chinese AI company (Shanghai, 2022)

## Overview

Multimodal foundation models — text, video, voice, AI agents. Latest model M2.7 (near-frontier with agentic capabilities). Available via API (api.minimax.chat), MiniMax Agent web interface, Hugging Face, OpenRouter.

## Capabilities

* Foundation models — M2.7 text generation
* Video generation — Hailuo AI
* Voice/Audio — TTS, voice cloning, music in 40+ languages
* AI Agents — Mini-Agent framework
* API Platform

## Security & Compliance

* **Data residency: China-based** — subject to Chinese regulations. Significant enterprise concern.
* **No known certifications** — SOC 2, ISO 27001, ISO 42001
* No enterprise SSO
* Self-hosting possible via Hugging Face (could mitigate data residency)

## Why Flagged

Lysander (Technology, Andre's team) using MiniMax for project work without AI Office awareness (flagged 2026-04-06). Michael steering toward [[gemini|Gemini]] as alternative.

## Considerations

* China-based — §5.2.3 likely restricts internal/client data use
* No enterprise controls — fails Microsoft Entra requirements (Action #21)
* Lysander may be using personal account with no enterprise protections
* Gemini infrastructure already available as alternative

*Backlog. Likely headed for Rejected unless self-hosted use case emerges.*
