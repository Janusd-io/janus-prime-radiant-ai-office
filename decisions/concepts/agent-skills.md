---
type: concept
title: Agent Skills
slug: agent-skills
created: 2026-05-06
updated: 2026-05-12
departments: [ai-office, engineering]
confidence: high
sources: [google-skills-repository, skill-graphs-arscontexta]
related: [model-context-protocol, agentic-ai, llm-wiki, 2026-05-06-skills-stay-as-skills-not-plugins]
---

# Agent Skills

Packaged, condensed expertise that agents can load on demand. A skill bundles instructions, examples, and (often) supporting tooling so an agent can accomplish a domain-specific task without polluting its general context window. The pattern has been popularised by [[anthropic|Anthropic]] ([[claude|Claude]] Code skills, Cowork skills) and is now being mirrored by other vendors.

## Two strands of the conversation in 2026

1. **First-party skill repositories.** Google announced its Official Agent Skills Repository at Cloud Next 2026 ([[2026-04-22-google-skills-repository]]) — condensed, real-time expertise for BigQuery, GKE, Gemini API, etc., explicitly framed as a way to "avoid context bloat."
2. **Skill graphs over flat skills.** [[skill-graphs-arscontexta]] argues that flat `SKILL.md` files miss the structural value of *connections between skills*; structured knowledge graphs enable applications that flat skills can't. Adjacent in spirit to the [[llm-wiki]] pattern.

## At Janus

Skills are first-class in Cowork (Janus's Claude desktop tool). The `ai-registry`, `ai-tool-evaluation`, and `standup` skills are operational examples. The eventual question: should the [[llm-wiki]] also be exposed as a skill so other Cowork sessions can read against it without manually loading pages?

**Skills not plugins:** Janus tooling stays as Claude *skills*, not Cowork *plugins* — see [[2026-05-06-skills-stay-as-skills-not-plugins]] for the decision. Plugins were considered as a distribution mechanism but rejected on portability and complexity grounds. Skills' markdown-first contract is the right shape for the AIO's iteration tempo.

## Relevant for AI tool evaluation

A vendor that ships skills (or first-class agent integrations) lowers the integration cost dramatically. Worth elevating as a Stage 1 viability criterion in the [[ai-tool-evaluation]] framework alongside MCP support.
