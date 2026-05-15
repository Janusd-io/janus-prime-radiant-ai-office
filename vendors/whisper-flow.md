---
type: vendor
title: Whisper Flow
slug: whisper-flow
air_id: AIR-92
status: Backlog
labels: [Functional, Technology, AI Policy]
departments: []
url: https://linear.app/janusd/issue/AIR-92/whisper-flow
created: 2026-05-04
updated: 2026-05-11
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Whisper Flow

> AI Registry entry [AIR-92](https://linear.app/janusd/issue/AIR-92/whisper-flow) — status **Backlog** as of 2026-05-11. Departments: —.

**Category:** AI Voice Dictation / Speech-to-Text
**Status:** Backlog
**Cost:** Free (2k words/week); Pro $15/$12 annual; Enterprise custom
**Departments:** Technology, AI Policy (initial)
**Entity:** Wispr AI, Inc.

## Overview

AI-powered voice dictation. Speech to text in any application across Mac/Windows/iPhone/Android. Marketed "4x faster than typing." AI auto-edits, command recognition, context-aware. 100+ languages, 95%+ accuracy claimed.

## Key Capabilities

* Universal voice dictation — system-wide push-to-talk in any text field
* **AI Auto-Edits** — removes filler words, fixes grammar, polishes prose
* AI Commands — rephrase, summarise, translate, change tone
* Context Awareness (per-app context; can be disabled)
* 100+ languages with dialect handling
* Custom vocabulary/dictionary for proprietary terms
* Cross-platform: macOS, Windows, iOS, Android

## Security & Compliance

* SOC 2 Type II ✅
* ISO 27001:2022 ✅
* HIPAA (with ZDR enabled)
* TLS/HTTPS in transit; encryption at rest
* **Privacy Mode** — no audio/transcripts/edits retained
* **Default (Privacy Mode OFF): dictation MAY be used to improve AI models**
* Enterprise: SSO/SAML (WorkOS), SCIM, Zero Data Retention, domain-based auto-add, org-level Context Awareness policy
* Cloud-based transcription (no fully offline mode)

## Why Flagged

Surfaced at 1 May 2026 AIO standup as candidate for:
1. Voice-capture front-end for **ISO facilitation skill** — facilitators dictate notes, decisions, prompts during live ISO sessions
2. Cross-Janus voice-print, post-processing of voice content, Fireflies companion
3. Quality-of-life productivity for voice-first thinkers

## Considerations

* **Default mode breaches §5.2.3** — Privacy Mode MUST be enforced or Enterprise + ZDR procured
* Cloud-only — every dictation leaves device; sensitive client content needs ZDR contractual
* Per-seat $12-15/user/month adds up at scale
* Overlap with Fireflies — Fireflies for meetings; Wispr for active dictation outside meetings
* Wispr AI relatively young — SOC 2 audit timeline + compliance program updates

*Backlog. Functional tier. Enterprise + ZDR + Privacy Mode mandatory for any rollout.*
