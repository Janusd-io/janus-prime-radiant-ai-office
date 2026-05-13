---
type: vendor
title: Wispr Flow
slug: wispr-flow
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: active
confidence: medium
sources: [pr-backup-wispr-flow]
related: [linear, fireflies, ai-tool-evaluation]
audience: [department]
captured_by: jehad-altoutou
---

# Wispr Flow

Voice dictation tool. Active candidate in Linear AIR as **AIR-92** (Backlog status as of 2026-05-01). Sometimes referenced internally as "Whisper Flow" — Wispr Flow is the canonical product name. The existing `whisperflow.md` stub in this vault is the same vendor under a misspelled slug; flagged for orchestrator canonicalization.

## Why Janus is evaluating it

- **ISO facilitation skill voice capture** — primary driver. Simon's ISO documentation flow (input → activities → output) is voice-friendly; transcribing facilitated sessions reduces the typing/post-processing tax.
- **[[fireflies|Fireflies]] adjacency.** Potential voice-print augmentation alongside meeting transcripts.
- **General productivity.** AIO and engineering staff who prefer dictation for long-form output.

## Compliance posture

Per Section 5.2.3 of the AI policy: **Enterprise tier + Zero Data Retention required** before any sensitive-data use. The Backlog stage in Linear AIR must clear that gate before Sandbox.

## Status

- AIR ID: AIR-92
- Stage: Backlog (as of 2026-05-01)
- Labels: Functional, Technology, AI Policy
- Ready for [[ai-tool-evaluation]] Gate 1. Awaiting dispatch.

## Watch for

- Gate 1 outcome (data training exclusion + portability are likely failure modes for any voice-capture tool).
- Whether the ISO facilitation skill development progresses fast enough to need Wispr Flow ready.
