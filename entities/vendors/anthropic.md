---
type: vendor
title: Anthropic
slug: anthropic
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office]
status: active
confidence: high
sources: [karpathy-llm-wiki, claude-managed-agents-launch, claude-managed-agents-scaling, anthropic-building-effective-agents, claude-code-routines]
related: [claude, llm-wiki, agentic-ai]
---

# Anthropic

AI safety and research company. Founded 2021 by Dario and Daniela Amodei (and a group of ex-OpenAI researchers). Headquartered in San Francisco. Mission framing emphasises building "reliable, interpretable, and steerable" AI systems.

## Product surface (as of 2026-05-06)

The Claude product family — model and all consumer/developer surfaces — is documented at [[claude]]. Anthropic ships these under one umbrella in this wiki because they share a model, an org, and a coherent design philosophy; splitting them into separate vendor pages would fragment cross-references without adding clarity.

## Why this entity exists separately from `claude.md`

- **Company-level engagement** lives here: how Janus relates to Anthropic as a vendor, account-level decisions, terms of service, pricing posture.
- **Product-level details** live in [[claude]]: what each product does, how Janus uses it, evaluation notes.

If Anthropic ships a non-Claude product line in the future (e.g., a separate research SaaS), it would also live under this page rather than getting its own vendor entity, unless the product is genuinely arms-length.

## Posture in 2026

Aggressively expanding up the stack — from model API to agent platform (Claude Managed Agents launch [[2026-04-08-claude-managed-agents-launch]]), from coding assistant to scheduled automations ([[2026-04-14-claude-code-routines]]), from chat UI to embedded surfaces (Claude in Chrome, Cowork mode). Pattern: own the developer's full agent loop, not just the inference call.

## Watch for

- Pricing changes and Enterprise tier evolution.
- Competitive responses from OpenAI / Google to Anthropic's agent-platform plays.
- Whether the file-based memory format in Managed Agents becomes a portable standard or remains Anthropic-specific.
