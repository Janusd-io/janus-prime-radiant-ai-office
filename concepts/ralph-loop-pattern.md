---
type: concept
title: "Ralph Loop Pattern"
slug: ralph-loop-pattern
created: 2026-05-07
updated: 2026-05-07
confidence: high
related: [agent-harness, agentic-ai, context-engineering]
sources: [ralph-wiggum-simpsons-ai, ralph-wiggum-software-engineer]
---

An agent iteration pattern where the model's own failures are fed back into its context without sanitization, forcing it to confront errors and iterate until a completion promise (e.g., "all tests pass") is met.

## Origin

Geoffrey Huntley (May 2025, rural Australia) created the pattern as a 5-line bash script to solve the human-in-the-loop bottleneck in agent coding. Core insight: pipe stderr + stack traces + hallucinations back into stdin and let the model iterate on raw failure data. Naive persistence—brute force—works because the model "dreams" solutions under pressure.

## Two implementations

**The Huntley Ralph (community bash script):** Chaotic, unbridled, best for creative exploration. The loop runs until human kills it or model succeeds.

**The Official Ralph (Anthropic plugin, late 2025):** Safe, structured, enterprise-ready. Uses a Stop Hook that intercepts exit attempts, checks for a Completion Promise (e.g., "All tests passed"), and if not met, feeds failure as structured data back into the loop. Prevents infinite hallucination spirals.

## Key mechanisms

- **Unsanitized feedback:** Model sees raw errors, not cleaned/abstracted versions
- **Stop Hook:** Intercepts model exit, verifies completion promise before allowing finish
- **Completion Promise:** Explicit condition (tests pass, linter succeeds, type-checks clean) that must be true to exit
- **Strong feedback loops:** TypeScript + unit tests + linters provide concrete, checkable verification

## Why it works

Under pressure to resolve its own failures, the model iterates rather than hallucinating. The feedback loop is tight: fail -> confront failure -> modify -> test -> fail or succeed -> repeat. This is fundamentally different from single-shot generation or multi-turn dialogue where the model can avoid its own mistakes.

## Enterprise wins

- $50k contracts executed for $297 in API costs (cost arbitrage between human + agent)
- 6 repositories auto-generated overnight (Y Combinator hackathon stress test)
- 14-hour autonomous codebase upgrades (React v16→v19 without human input)

## Relation to agent-harness

The ralph loop is a specific instantiation of the [[agent-harness|harness pattern]]: it emphasizes feedback + verification (the "verify work" phase) as the primary driver of agent capability. Rather than smarter prompts or better models, the ralph loop proves that iteration under constraint is what matters.
