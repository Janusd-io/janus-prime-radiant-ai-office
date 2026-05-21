---
type: vendor
title: Anthropic
slug: anthropic
created: 2026-05-06
updated: 2026-05-21
departments: [ai-office]
status: active
confidence: high
sources: [karpathy-llm-wiki, claude-managed-agents-launch, claude-managed-agents-scaling, anthropic-building-effective-agents, claude-code-routines, 2026-05-19-kpmg-claude-alliance, 2026-05-21-anthropic-first-profitable-quarter]
related: [claude, llm-wiki, agentic-ai, ai-native-enterprise-restructuring, builders-sellers-measurers, ai-tool-evaluation-framework]
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
- IPO trajectory + valuation outcome relative to OpenAI / SpaceX (trillion-dollar tier projected).
- Whether Mythos model expands beyond the select-companies launch.

## Commercial trajectory — Q2 2026 (added 2026-05-21)

Two signals landed in one week that materially resolve vendor-viability risk on Anthropic:

- **KPMG global alliance** (announced 2026-05-19; see [[2026-05-19-kpmg-claude-alliance]]). 276,000+ KPMG employees across 138 countries get Claude access. Claude Cowork + Managed Agents embedded into KPMG's *Digital Gateway* client-work platform — starting with tax and legal client tools. Anthropic also named preferred-partner-for-private-equity. A tax-compliance agent that used to take weeks now takes minutes inside Digital Gateway. This is the largest single enterprise commit visible in the public record.
- **First profitable quarter projected** (WSJ, 2026-05-21; see [[2026-05-21-anthropic-first-profitable-quarter]]). Q2 2026 revenue projected $10.9B (130% Q-over-Q from Q1's $4.8B) with first operating profit of $559M. Growth rate exceeds Zoom-during-pandemic, Google/Meta-pre-IPO trajectories. Computing-cost ratio improving from 71¢ to 56¢ per $1 revenue — operational leverage kicking in. Trillion-dollar IPO trajectory alongside OpenAI and SpaceX. Anthropic primarily uses Google + Amazon chips (cheaper than Nvidia); takes more conservative data-centre commits than OpenAI; smaller consumer business reduces free-user subsidy load.
- **Political risk absorbed.** Months earlier, the Trump administration directed federal agencies to cut ties with Anthropic on security grounds (Anthropic refused to allow tech for "all lawful uses" per DoD demand). Relationship since improved; ongoing administration meetings on the Mythos model (released to a select group of companies due to cybersecurity risk).

**Implication for Gate 2.3 ("vendor viability — 24-month horizon").** The criterion is now structurally over-satisfied for Anthropic. Worth a footnote on [[ai-tool-evaluation-framework]] capturing the new baseline. See [[ai-native-enterprise-restructuring]] for the full thesis of how the Q2 signals validate the AIO operating model.
