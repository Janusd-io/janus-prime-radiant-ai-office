---
type: vendor
title: VibeVoice
slug: vibevoice
created: 2026-05-14
updated: 2026-05-14
confidence: high
captured_by: jehad-altoutou
audience: [department]
departments: [ai-office]
sources: [vibevoice-tts, vibevoice-asr, vibevoice-realtime-0-5b, vibevoice-vllm-asr, readme-4, 1p-vibevoice, 1p-abs, security, contributing]
related: [microsoft, huggingface, vllm]
---

# VibeVoice

Microsoft Research open-source speech-AI suite. Three models in the family:

- **VibeVoice-TTS (1.5B)** — long-form multi-speaker TTS, up to 90 min and 4 speakers in a single pass over a 64K context. Next-token-diffusion framework with continuous speech tokenizers at an ultra-low 7.5Hz frame rate. Technical report: arxiv 2508.19205. VibeVoice-Large variant is disabled in releases.
- **VibeVoice-Realtime-0.5B** — streaming TTS for live narration / LLM-token-streamed speech, ~200ms first-audible-token latency. Acoustic tokenizer only (no semantic tokenizer) at 7.5Hz. English-primary with experimental support for nine more languages.
- **VibeVoice-ASR-7B** — unified speech-to-text handling 60-min long-form audio in one pass with joint diarization + timestamping (Who/When/What). 50+ languages with code-switching, customised hotwords for domain vocab.

Deployment path documented for vLLM as an OpenAI-compatible `/v1/chat/completions` plugin with data-parallel replicas behind a single port — no upstream vLLM source modification.

Fine-tuning via LoRA + `peft` (`finetuning-asr/`). License: standard Microsoft repo (see `security`, `contributing` for boilerplate disclosure and contribution policy — academic research code, minimalism enforced, no style PRs, English-only).

## AIO relevance (2026-05-14, confidence medium)

Not currently in the AI Registry. Jehad has cloned the repo locally and is exploring as a candidate for long-form transcription / synthetic-voice workflows. **Action — propose adding to Linear AIR backlog via `/ai-registry` for triage** rather than evaluating from this wiki directly. Worth comparing against Whisper, AssemblyAI, ElevenLabs (TTS side) once an evaluation is scoped.
