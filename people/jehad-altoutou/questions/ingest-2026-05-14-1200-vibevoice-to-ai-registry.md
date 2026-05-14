---
type: question
title: Add VibeVoice (Microsoft TTS/ASR suite) to AI Registry backlog?
slug: ingest-2026-05-14-1200-vibevoice-to-ai-registry
created: 2026-05-14
updated: 2026-05-14
status: active
owner: jehad-altoutou
captured_by: jehad-altoutou
audience: [department]
departments: [ai-office]
sources: [vibevoice-tts, vibevoice-asr, vibevoice-realtime-0-5b, vibevoice-vllm-asr]
related: [vibevoice]
---

# Add VibeVoice to AI Registry backlog?

## Proposed action

File a new Linear AIR backlog issue (via `/ai-registry` skill, never directly) for **VibeVoice** (Microsoft open-source TTS/ASR family) so the AI Office can decide whether to evaluate it for long-form transcription and synthetic-voice use cases.

## Reasoning

Jehad has cloned the repo locally (laptop scan picked up `~/VibeVoice/`) and read through the three model cards (TTS, ASR, Realtime). The capability claims are unusual for an open-source release:

- 90-minute single-pass multi-speaker TTS at 7.5Hz tokenizer frame rate
- 60-minute single-pass ASR with joint diarization + timestamping
- 200ms first-token streaming TTS
- vLLM-compatible deployment with data-parallel replicas

If the claims hold up under evaluation, this changes the cost/quality envelope for any AIO workflow that consumes long Fireflies transcripts or generates narrated content.

## Alternative interpretations

1. **Research-grade only** — academic code with minimalism-first contributor policy may not be production-grade. Worth a sandbox check before any commitment.
2. **Whisper is good enough** — incumbent open-source ASR may already cover Janus's needs at lower integration cost.
3. **Vendor coverage already exists** — ElevenLabs / AssemblyAI / Deepgram are already in the registry; this may duplicate triage effort.

## What would resolve it

- Michael's call on whether to add to AIR backlog at standard priority
- If yes: `/ai-registry add` from the standup or this question
- If no: archive this question with the rationale recorded
