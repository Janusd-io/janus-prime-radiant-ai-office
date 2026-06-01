---
type: vendor
title: Wispr Flow
slug: wispr-flow
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: active
confidence: medium
sources: [aio-2026-05-01, jehad-vault-wispr-flow]
related: [linear, fireflies, ai-tool-evaluation]
migrated_from: entities/vendors/wispr-flow.md
---
# Wispr Flow

Voice dictation tool. Active candidate in Linear AIR as **AIR-92** (Backlog status as of 2026-05-01). Sometimes referenced internally as "Whisper Flow" — Wispr Flow is the canonical product name.

## Why Janus is evaluating it

- **ISO facilitation skill voice capture.** Primary driver — Simon's ISO documentation flow (input → activities → output) is voice-friendly; transcribing facilitated sessions reduces the typing/post-processing tax.
- **Fireflies adjacency.** Potential voice-print augmentation alongside [[fireflies]] meeting transcripts.
- **General productivity.** Broader use cases for AIO and engineering staff who prefer dictation over typing for long-form output.

## Compliance posture

Per Section 5.2.3 of the AI policy: **Enterprise tier + Zero Data Retention required** before any sensitive-data use. The Backlog stage in Linear AIR will need to clear that gate before Sandbox.

## Status

- **AIR ID:** AIR-92
- **Stage:** Backlog (as of 2026-05-01)
- **Labels:** Functional, Technology, AI Policy
- **Ready for [[ai-tool-evaluation]] Gate 1.** Awaiting dispatch.

## Watch for

- Gate 1 outcome (data training exclusion + portability are the likely failure modes for any voice-capture tool).
- Whether the ISO facilitation skill development progresses fast enough to need Wispr Flow ready, or whether other inputs unblock that work first.
