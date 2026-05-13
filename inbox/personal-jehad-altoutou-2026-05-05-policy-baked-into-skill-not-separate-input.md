---
type: decision
title: "AI policy is baked into the skill, not passed as a separate input"
slug: 2026-05-05-policy-baked-into-skill-not-separate-input
created: 2026-05-05
updated: 2026-05-05
departments: [ai-office]
status: resolved
owner: unknown-speaker-1
decided_by: unknown-speaker-2
sources: [2026-05-05-may-05-11-03-am]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# AI policy is baked into the skill, not passed as a separate input

## Decision

Governance documents (AI policy, ISO policy) will be embedded inside the skill itself rather than treated as a distinct ISO input field.

## Why

Treating policy as an input forces every request to attach it, which is redundant when the skill always applies the same governance. Embedding the policy in the skill means version control and updates flow through the skill library (GitHub) and the skill carries its own authority. This keeps the ISO 'input' field strictly for request-specific data.

## Evidence

> Speaker 2: The policy is baked into the skill. Speaker 1: Yeah. Yeah. Because yeah. Speaker 2: The skill is written around.

## When

2026-05-05 · meeting [[2026-05-05-may-05-11-03-am]] · decided by [[unknown-speaker-2]] · owned by [[unknown-speaker-1]]

## Implications

- (to be populated by the owner)
