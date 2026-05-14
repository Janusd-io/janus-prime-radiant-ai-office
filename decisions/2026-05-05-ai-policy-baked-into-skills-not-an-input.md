---
type: decision
title: AI policy is baked into each evaluation skill rather than passed as a separate Input
slug: 2026-05-05-ai-policy-baked-into-skills-not-an-input
created: 2026-05-05
updated: 2026-05-05
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-05-may-05-11-03-am]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# AI policy is baked into each evaluation skill rather than passed as a separate Input

## Decision

The AI policy governing tool evaluation is embedded in the skill itself; it is not treated as a separate input document on the ISO mapping.

## Why

A skill is software (treated like source code), and the policy is the standard the skill is written around. Passing the policy as an input each run is redundant and would let it drift across versions; embedding it in the versioned skill keeps the policy and the execution in lockstep.

## Evidence

> Speaker 2: The policy is baked into the skill. The skill is written around... the description of the activity.

## When

2026-05-05 · meeting [[2026-05-05-may-05-11-03-am]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
