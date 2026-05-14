---
type: concept
title: Agent Skills
slug: agent-skills
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [model-context-protocol, agentic-ai, llm-wiki, claude-skills]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `concepts/agent-skills.md` — this file is preserved as a source for divergent framing / additional context._

# Agent Skills

Packaged, condensed expertise that agents can load on demand. A skill bundles instructions, examples, and (often) supporting tooling so an agent can accomplish a domain-specific task without polluting its general context window. The pattern has been popularised by [[anthropic|Anthropic]] (Claude Code skills, Cowork skills) and is now being mirrored by other vendors.

## Two strands of the conversation in 2026

1. **First-party skill repositories.** Google announced its Official Agent Skills Repository at Cloud Next 2026 — condensed, real-time expertise for BigQuery, GKE, Gemini API, etc., explicitly framed as a way to "avoid context bloat."
2. **Skill graphs over flat skills.** Argues that flat `SKILL.md` files miss the structural value of *connections between skills*; structured knowledge graphs enable applications that flat skills can't. Adjacent in spirit to the [[llm-wiki]] pattern.

## At Janus

Skills are first-class in Cowork (Janus's Claude desktop tool). The `ai-registry`, `ai-tool-evaluation`, and `standup` skills are operational examples. The eventual question: should the [[llm-wiki]] also be exposed as a skill so other Cowork sessions can read against it without manually loading pages?

## Relevant for AI tool evaluation

A vendor that ships skills (or first-class agent integrations) lowers the integration cost dramatically. Worth elevating as a Stage 1 viability criterion in the AI tool evaluation framework alongside MCP support.

## Naming note

Live vault has stub `concepts/claude-skills.md`. The two overlap — `claude-skills` is vendor-specific, `agent-skills` is the general industry pattern. See escalation `questions/ingest-2026-05-13-1500-agent-skills-vs-claude-skills-relationship.md` for the relationship decision.
