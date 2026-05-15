---
type: vendor
title: Whisper Transcription
slug: whisper-transcription
air_id: AIR-73
status: Backlog
labels: [AI Policy, Functional]
departments: []
url: https://linear.app/janusd/issue/AIR-73/whisper-transcription
created: 2026-04-06
updated: 2026-04-06
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Whisper Transcription

> AI Registry entry [AIR-73](https://linear.app/janusd/issue/AIR-73/whisper-transcription) — status **Backlog** as of 2026-04-06. Departments: —.

**Category:** On-Device Transcription / Speech-to-Text
**Status:** Backlog
**Cost:** One-time purchase (Mac App Store); no subscription
**Departments:** AI Policy

## Overview

Native macOS app for on-device speech-to-text using OpenAI's Whisper model. All audio processing happens LOCALLY — no audio leaves the device. Apple Silicon optimised (Metal Performance Shaders, Neural Engine).

## Capabilities

* On-device transcription with downloaded Whisper models (small through large-v3)
* Speaker diarisation
* Word-level timestamps
* Live microphone recording
* Batch processing
* SRT subtitle export
* Multi-language with auto-detection
* Multiple model sizes (speed vs accuracy)

## Security & Compliance

* **Fully offline** — no audio data leaves device after model download
* **No cloud component**
* **No account required**
* Strongest possible privacy posture for transcription
* No enterprise certifications (desktop app, not managed service)

## Relevance

Complement to Fireflies ([[fireflies-ai|AIR-9]]) for on-device, fully private transcription. Fills gap for offline transcription of sensitive recordings — confidential audio that cannot be processed via cloud.

## Considerations

* macOS only — not Windows/Linux
* No collaboration/sharing (unlike Fireflies)
* No API/integration
* 8GB RAM min, 16GB+ recommended
* Does NOT replace Fireflies — strictly complementary

*Backlog. Functional tier. Strongest §5.2.3 alignment.*
