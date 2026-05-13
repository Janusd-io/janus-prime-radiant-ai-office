---
type: decision
title: ISO compliance becomes a gate before automation projects begin
slug: 2026-05-01-iso-compliance-gate-before-automation
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, it-ops]
status: resolved
owner: michael
sources: [aio-2026-05-01]
related: [ai-tool-evaluation]
---

# ISO compliance becomes a gate before automation projects begin

**Decision date:** 2026-05-01
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-01]]

## What

ISO compliance work — captured as input → activities → output documentation — is now a prerequisite gate before automation projects can begin execution. Simon facilitates the ISO documentation process; a dedicated "ISO facilitation skill" is being built to support him.

## Why

Without the ISO documentation in place, automation projects risk shipping into a compliance gap that requires rework or rollback. Putting ISO ahead of automation makes the dependency explicit and prevents downstream churn.

## Implications

- Automation projects are blocked until ISO documentation for the relevant scope is complete.
- A new skill ("Build ISO facilitation skill for Simon") is being developed with input/activities/output schema, draft questions list, and Whisper Flow voice-capture integration.
- ISO standards interpretation must align with Bonaventure's and Simon's expectations — judgement call rather than mechanical compliance.

## Related

- The [[ai-tool-evaluation]] framework's Stage 4 IT handover is downstream of ISO.
- This decision is the upstream constraint on several blocked Monday items (e.g., `#60 ISO officer process documentation`).
