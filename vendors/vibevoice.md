---
type: vendor
title: VibeVoice
slug: vibevoice
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
status: dormant
confidence: medium
captured_by: jehad-altoutou
audience: department
sources: [readme-3]
related: [anthropic, openai]
migrated_from: entities/vendors/vibevoice.md
---
Microsoft's open-source frontier voice AI family: **VibeVoice-ASR-7B** (60-minute single-pass speech-to-text with who/when/what diarization, 50+ languages, vLLM-supported), **VibeVoice-TTS-1.5B** (90-minute multi-speaker TTS, ICLR 2026 oral — but Microsoft removed the open code in Sep 2025 over misuse, only weights remain), and **VibeVoice-Realtime-0.5B** (streaming TTS with ~300ms first-audible latency).

Key technical signal: continuous speech tokenizers at **7.5 Hz frame rate** with next-token diffusion for the acoustic head — the ultra-low frame rate is what unlocks the 60-minute single-pass property for ASR. Cloned to Jehad's laptop (`/Users/jehad/VibeVoice`) per `readme-3` source.

Not actively used in any AIO production workflow as of 2026-05-14; relevant as a watch-list vendor for any future voice-AI evaluation (e.g. meeting transcription alternatives to [[fireflies]], voice-enabled agent interfaces). Confidence is `medium` because the TTS take-down means a commercial path is unclear and provenance now leans research-only.
