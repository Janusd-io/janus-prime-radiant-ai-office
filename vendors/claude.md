---
type: vendor
title: Claude
slug: claude
air_id: AIR-10
status: Production
labels: [AI Policy, Office of CEO, Functional]
departments: [ai-office, engineering, office-of-ceo]
url: https://linear.app/janusd/issue/AIR-10/claude
created: 2026-02-25
updated: 2026-05-31
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
confidence: high
sources: [karpathy-llm-wiki, anthropic-building-effective-agents, claude-managed-agents-launch, claude-managed-agents-quickstart, claude-managed-agents-scaling, claude-managed-agents-memory, claude-managed-agents-memory-rlancemartin, claude-code-routines, claude-code-prompt-caching-lessons, claude-code-limits-harness-pawelhuryn, himanshustwts-claude-code-memory-architecture, jehad-vault-claude, 2026-05-19-kpmg-claude-alliance, 2026-05-21-mit-tech-review-code-with-claude-london, 2026-05-20-every-google-io-agents-agents-agents, 2026-05-19-nyt-google-winning-ai-race, 2026-05-26-bloomberg-bankers-claude-cost]
related: [anthropic, llm-wiki, janus-prime-radiant-build, agent-memory, agent-harness, agent-skills, model-context-protocol, 2026-05-06-skills-stay-as-skills-not-plugins, ai-native-enterprise-restructuring, claude-code]
migrated_from: entities/vendors/claude.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[office-of-ceo]]


# Claude

> AI Registry entry [AIR-10](https://linear.app/janusd/issue/AIR-10/claude) — status **Production** as of 2026-04-20. Departments: office-of-ceo.

**Category:** Foundation Model / AI Assistant
**Cost per User/Month:** Included in Claude Teams subscription
**Number of Licences:** 2
**Total Monthly Cost:** $0 (covered under Claude Teams — see [[claude-console|AIR-11]])
**Departments:** Office of CEO, AI Policy

---

## Overview

Claude is Anthropic's flagship AI assistant, available via [claude.ai](http://claude.ai) as a web and desktop application. It excels at complex reasoning, nuanced writing, long-document analysis, and careful instruction-following. At Janus Digital, Claude is used alongside [[google-gemini|Google Gemini]] ([[google-gemini|AIR-5]]) as a primary foundation model, with particular strength in tasks requiring precision, safety awareness, and extended context processing.

## Capabilities

* **Advanced reasoning** — Strong performance on complex analytical, logical, and mathematical tasks
* **Long-context processing** — Supports very large context windows for processing extensive documents
* **Writing and editing** — High-quality content generation, editing, and style adaptation
* **Code generation** — Capable across multiple programming languages with strong debugging ability
* **Document analysis** — PDF, image, and document understanding with careful extraction
* **Artifacts** — Interactive code, documents, and visualisations created within the conversation
* **Projects** — Persistent context spaces with uploaded knowledge bases
* **Tool use** — MCP (Model Context Protocol) support for connecting to external tools and data sources

## Security & Compliance

* **SOC 2 Type II** certified
* **GDPR** compliant
* **Data protection** — Claude Teams plan ensures conversations are not used for model training
* **SSO** — Available on Teams and Enterprise plans
* **No training on customer data** — Explicit contractual guarantee on Teams/Enterprise plans

## Relevance to Janus Digital

Claude is one of Janus Digital's two primary foundation models (alongside [[gemini|Gemini]]). Preferred for tasks requiring nuanced reasoning, careful writing, and complex document analysis. The Claude ecosystem ([[claude-code|Claude Code]], Claude for Excel, [[claude-for-powerpoint|Claude for PowerPoint]]) makes it a growing platform rather than just a chatbot.

*Deployed to Office of CEO and AI Policy. Functional tier.*

## Merged from `entities/vendors/claude.md`

# Claude (Anthropic product family)

Umbrella entry for all of [[anthropic]]'s consumer / developer / agent-platform surfaces. Janus's working principle: keep these together because they share a model, a mental model, and a coherent design philosophy; splitting them into one-vendor-page-per-product would fragment cross-references without meaningful benefit. Sub-products are listed below; create separate vendor pages only if a sub-product becomes genuinely arms-length.

## Sub-products

| Surface | What it is | Janus use |
|---|---|---|
| **Claude API / models** | The LLM family itself. Available via API and Anthropic SDK. | Powers the maintenance of this wiki and most AI Office automation. |
| **Claude (web/desktop chat)** | Consumer chat UI. | General drafting, evaluation, ad-hoc analysis. |
| **Claude Code** | CLI / IDE coding agent for developers. | Active use across engineering. Subject of its own deep-dive sources: harness framing ([[claude-code-limits-harness-pawelhuryn]]), prompt caching lessons ([[claude-code-prompt-caching-lessons]]), memory architecture ([[himanshustwts-claude-code-memory-architecture]]). |
| **Claude Code routines** | Scheduled / event-driven Claude Code automations on Anthropic-hosted infrastructure. Research preview as of 2026-04-14. | Not yet adopted; candidate for Stage 1 evaluation when out of preview. See [[2026-04-14-claude-code-routines]]. |
| **Claude Managed Agents** | Composable APIs for cloud-hosted agents at scale; launched 2026-04-08. File-based memory in public beta from 2026-04-23. | Not yet evaluated; relevant against Janus's broader agent-platform decisions. See [[2026-04-08-claude-managed-agents-launch]] and [[agent-memory]]. |
| **Cowork mode** | Claude desktop tool for non-developer file/task automation; provides connectors (Linear, Notion, Fireflies, Slack, Monday, Figma, etc.) and a sandboxed Linux shell. | The interface Michael uses to maintain this wiki. Plugins (bundles of MCPs + skills + tools) are first-class. |
| **Claude in Chrome** | Browser-side agent for navigating web tasks. | Not yet evaluated for Janus workflows. |
| **Claude Code on the web** | Web-hosted Claude Code execution surface (the substrate that routines run on). | Indirectly used — backbone for routines. |

## Cross-cutting properties

- **Skills** are first-class across surfaces (Claude Code, Cowork). See [[agent-skills]]. Janus already operates the `ai-registry`, `ai-tool-evaluation`, and `standup` skills. AIO tooling stays as Claude skills, not Cowork plugins — see [[2026-05-06-skills-stay-as-skills-not-plugins]] for the decision.
- **Memory** is increasingly first-class — Managed Agents has file-based memory; Claude Code has a memory architecture (per [[himanshustwts-claude-code-memory-architecture]]). See [[agent-memory]].
- **MCP** is the ambient connector protocol across all surfaces. See [[model-context-protocol]].

## Posture

Anthropic is moving up the stack from model API → agent platform. The "decoupling the brain from the hands" framing in [[claude-managed-agents-scaling]] is the most explicit articulation of this. For Janus, this means evaluating Claude isn't just "model quality" anymore — it's the quality of the surrounding harness, memory, skills, and routines together.

## Enterprise validation — Q2 2026 (added 2026-05-21)

The **KPMG global alliance** (2026-05-19; see [[2026-05-19-kpmg-claude-alliance]]) is the load-bearing external validation of the Claude product family at Big-Four scale:

- **276,000+ KPMG employees globally** gain access to Claude across 138 countries.
- **Claude Cowork and Claude Managed Agents** embedded inside KPMG's *Digital Gateway* (KPMG's main client-work platform, built on Microsoft Azure). Tax and legal client tools first, expanding across business functions.
- KPMG-built tax-compliance agents that previously took weeks across multiple tools now ship in minutes inside Digital Gateway. Quote from Rema Serafi (VC Tax, KPMG US): *"With Cowork and Managed Agents integrated in Digital Gateway, that same capability takes minutes. This is a totally different way of working."*
- Anthropic named preferred-partner-for-private-equity; KPMG advises PE portfolio companies on deploying Claude.
- KPMG also using Claude internally for cybersecurity (finding and fixing vulnerabilities under KPMG's Trusted AI framework).

Strategic implication for Janus's Claude-first stack: a Big-Four firm running a 276K-seat procurement, security, and legal review on Claude means Janus's choice is now defensible-on-precedent rather than pioneering. Cite KPMG when introducing Claude-first tooling to risk-sensitive Janus audiences (CLO once joined; legal review; investor pitches). See [[ai-native-enterprise-restructuring]] for the full thesis.

## Model cadence — Q1/Q2 2026 (added 2026-05-23)

- **Claude 4.6 (February 2026)** and **Claude 4.7 (April 2026)** — back-to-back model releases that materially upgraded the coding agent. Per Anthropic engineering lead Katelyn Lesse at Code with Claude London (2026-05-19; see [[2026-05-21-code-with-claude-london]]): *"I think that right now Claude is probably as good as a midlevel engineer at writing code. … But over time we want Claude to get better and better at all different types of engineering."*
- **"Dreaming" — agent memory inside Claude Code natively** (announced ~2026-05-07). Claude Code agents write task-specific notes; a "dreaming" consolidation pass spots patterns across them; later agents read the dreamed-out summaries to bootstrap context. Lands the multi-graph [[agent-memory]] thesis directly inside Claude Code, in the same family as Mnemon and MAGMA but vendor-shipped. See [[claude-code]] for the deeper writeup.
- **Stainless acquisition (2026-05-19, ~$300M).** Anthropic acquired Stainless, a platform for generating high-quality API SDKs and MCP servers — extending Claude's ability to connect to external data and tools at scale. Surfaced via Every / Context Window's I/O-week coverage at [[2026-05-20-every-google-io-agents-agents-agents]]; full context lives on the [[anthropic|parent vendor page]]. Implication for the Claude product family: the agent-to-software interoperability layer is now an Anthropic-owned strategic asset, not a third-party dependency.

## Competitive context — May 2026

The same week as Code with Claude, Google ran **I/O 2026** with **Gemini 3.5 Flash** (claimed Opus-4.7-class intelligence at 4× speed and half the cost), **Antigravity 2.0** (Cowork/Managed-Agents competitor on the desktop), and **Gemini Spark** (24/7 cloud personal agent). See [[2026-05-19-google-io-2026-agents-as-product]]. The Claude-vs-Gemini competitive surface is now most acute on (a) the price-performance frontier for fast routine inference, (b) the desktop-agent-orchestration platform, and (c) consumer ambient agents. Janus's posture is unchanged — Claude-first for AIO and engineering — but watch-for items below now include direct Google moves.

Updated 2026-05-31: NYT's *How Google Is Starting to Win the A.I. Race* ([[2026-05-19-nyt-google-winning-ai-race]]) reports **Gemini at ~900M regular users vs ~30× less estimated web traffic for Claude** — the consumer-chatbot gap is now an order of magnitude. The NYT framing names Claude as *"more focused on business customers"*. That positioning is consistent with the [[2026-05-19-kpmg-claude-alliance|KPMG alliance]] and Q2 enterprise trajectory: Anthropic isn't chasing consumer ambient agents head-on against Gemini; the enterprise-and-developer beachhead is where Claude is differentiated. Worth absorbing into outbound Janus positioning — "Claude is the enterprise-AI choice; Gemini is the consumer-AI choice; both can be right" is more defensible than implying Claude is winning a race it's not in.

## Cost trajectory — Bloomberg read (added 2026-05-31)

Bloomberg Opinion (Lionel Laurent, 2026-05-26; [[2026-05-26-bloomberg-bankers-claude-cost]]) reports per-firm Claude bills *"on track to rise from tens of thousands of dollars for a single firm to several million"* among European financial-services customers, driven by compute-supply constraints (H100 spot price rising even after Anthropic's SpaceX capacity deal). Laurent quotes Christopher Tozzi: *"Not every task needs a frontier model."* The piece reports financial-services customers experimenting with **in-house models for non-frontier tasks** — a posture the AIO already operates under via [[stack-composition-framework]] and [[tool-tiers]]. For Janus's current spend profile this is a watch-for, not a blocker: the pressure window for Janus is later than for tier-1 banks, but the discipline of *not* defaulting to frontier-class inference for every task is the right posture to enter the window with. Full read at [[2026-05-31-ai-cost-pressure-in-house-model-shift]].

## Watch for

- Convergence between Claude Code routines and Claude Managed Agents — at some point these may merge.
- Whether file-based agent memory becomes a portable Anthropic standard or stays Claude-only.
- Pricing rationalisation across surfaces (currently a mix of API consumption, Claude Code subscription tiers, and Managed Agents with its own model).
- Cowork plugin ecosystem maturity — important for Janus's wiki + skills setup.

## Merged from `entities/vendors/claude.md`

# Claude (Anthropic product family)

Umbrella entry for all of [[anthropic]]'s consumer / developer / agent-platform surfaces. Janus's working principle: keep these together because they share a model, a mental model, and a coherent design philosophy; splitting them into one-vendor-page-per-product would fragment cross-references without meaningful benefit. Sub-products are listed below; create separate vendor pages only if a sub-product becomes genuinely arms-length.

## Sub-products

| Surface | What it is | Janus use |
|---|---|---|
| **Claude API / models** | The LLM family itself. Available via API and Anthropic SDK. | Powers the maintenance of this wiki and most AI Office automation. |
| **Claude (web/desktop chat)** | Consumer chat UI. | General drafting, evaluation, ad-hoc analysis. |
| **Claude Code** | CLI / IDE coding agent for developers. | Active use across engineering. Subject of its own deep-dive sources: harness framing ([[claude-code-limits-harness-pawelhuryn]]), prompt caching lessons ([[claude-code-prompt-caching-lessons]]), memory architecture ([[himanshustwts-claude-code-memory-architecture]]). |
| **Claude Code routines** | Scheduled / event-driven Claude Code automations on Anthropic-hosted infrastructure. Research preview as of 2026-04-14. | Not yet adopted; candidate for Stage 1 evaluation when out of preview. See [[2026-04-14-claude-code-routines]]. |
| **Claude Managed Agents** | Composable APIs for cloud-hosted agents at scale; launched 2026-04-08. File-based memory in public beta from 2026-04-23. | Not yet evaluated; relevant against Janus's broader agent-platform decisions. See [[2026-04-08-claude-managed-agents-launch]] and [[agent-memory]]. |
| **Cowork mode** | Claude desktop tool for non-developer file/task automation; provides connectors (Linear, Notion, Fireflies, Slack, Monday, Figma, etc.) and a sandboxed Linux shell. | The interface Michael uses to maintain this wiki. Plugins (bundles of MCPs + skills + tools) are first-class. |
| **Claude in Chrome** | Browser-side agent for navigating web tasks. | Not yet evaluated for Janus workflows. |
| **Claude Code on the web** | Web-hosted Claude Code execution surface (the substrate that routines run on). | Indirectly used — backbone for routines. |

## Cross-cutting properties

- **Skills** are first-class across surfaces (Claude Code, Cowork). See [[agent-skills]]. Janus already operates the `ai-registry`, `ai-tool-evaluation`, and `standup` skills. AIO tooling stays as Claude skills, not Cowork plugins — see [[2026-05-06-skills-stay-as-skills-not-plugins]] for the decision.
- **Memory** is increasingly first-class — Managed Agents has file-based memory; Claude Code has a memory architecture (per [[himanshustwts-claude-code-memory-architecture]]). See [[agent-memory]].
- **MCP** is the ambient connector protocol across all surfaces. See [[model-context-protocol]].

## Posture

Anthropic is moving up the stack from model API → agent platform. The "decoupling the brain from the hands" framing in [[claude-managed-agents-scaling]] is the most explicit articulation of this. For Janus, this means evaluating Claude isn't just "model quality" anymore — it's the quality of the surrounding harness, memory, skills, and routines together.

## Enterprise validation — Q2 2026 (added 2026-05-21)

The **KPMG global alliance** (2026-05-19; see [[2026-05-19-kpmg-claude-alliance]]) is the load-bearing external validation of the Claude product family at Big-Four scale:

- **276,000+ KPMG employees globally** gain access to Claude across 138 countries.
- **Claude Cowork and Claude Managed Agents** embedded inside KPMG's *Digital Gateway* (KPMG's main client-work platform, built on Microsoft Azure). Tax and legal client tools first, expanding across business functions.
- KPMG-built tax-compliance agents that previously took weeks across multiple tools now ship in minutes inside Digital Gateway. Quote from Rema Serafi (VC Tax, KPMG US): *"With Cowork and Managed Agents integrated in Digital Gateway, that same capability takes minutes. This is a totally different way of working."*
- Anthropic named preferred-partner-for-private-equity; KPMG advises PE portfolio companies on deploying Claude.
- KPMG also using Claude internally for cybersecurity (finding and fixing vulnerabilities under KPMG's Trusted AI framework).

Strategic implication for Janus's Claude-first stack: a Big-Four firm running a 276K-seat procurement, security, and legal review on Claude means Janus's choice is now defensible-on-precedent rather than pioneering. Cite KPMG when introducing Claude-first tooling to risk-sensitive Janus audiences (CLO once joined; legal review; investor pitches). See [[ai-native-enterprise-restructuring]] for the full thesis.

## Model cadence — Q1/Q2 2026 (added 2026-05-23)

- **Claude 4.6 (February 2026)** and **Claude 4.7 (April 2026)** — back-to-back model releases that materially upgraded the coding agent. Per Anthropic engineering lead Katelyn Lesse at Code with Claude London (2026-05-19; see [[2026-05-21-code-with-claude-london]]): *"I think that right now Claude is probably as good as a midlevel engineer at writing code. … But over time we want Claude to get better and better at all different types of engineering."*
- **"Dreaming" — agent memory inside Claude Code natively** (announced ~2026-05-07). Claude Code agents write task-specific notes; a "dreaming" consolidation pass spots patterns across them; later agents read the dreamed-out summaries to bootstrap context. Lands the multi-graph [[agent-memory]] thesis directly inside Claude Code, in the same family as Mnemon and MAGMA but vendor-shipped. See [[claude-code]] for the deeper writeup.
- **Stainless acquisition (2026-05-19, ~$300M).** Anthropic acquired Stainless, a platform for generating high-quality API SDKs and MCP servers — extending Claude's ability to connect to external data and tools at scale. Surfaced via Every / Context Window's I/O-week coverage at [[2026-05-20-every-google-io-agents-agents-agents]]; full context lives on the [[anthropic|parent vendor page]]. Implication for the Claude product family: the agent-to-software interoperability layer is now an Anthropic-owned strategic asset, not a third-party dependency.

## Competitive context — May 2026

The same week as Code with Claude, Google ran **I/O 2026** with **Gemini 3.5 Flash** (claimed Opus-4.7-class intelligence at 4× speed and half the cost), **Antigravity 2.0** (Cowork/Managed-Agents competitor on the desktop), and **Gemini Spark** (24/7 cloud personal agent). See [[2026-05-19-google-io-2026-agents-as-product]]. The Claude-vs-Gemini competitive surface is now most acute on (a) the price-performance frontier for fast routine inference, (b) the desktop-agent-orchestration platform, and (c) consumer ambient agents. Janus's posture is unchanged — Claude-first for AIO and engineering — but watch-for items below now include direct Google moves.

Updated 2026-05-31: NYT's *How Google Is Starting to Win the A.I. Race* ([[2026-05-19-nyt-google-winning-ai-race]]) reports **Gemini at ~900M regular users vs ~30× less estimated web traffic for Claude** — the consumer-chatbot gap is now an order of magnitude. The NYT framing names Claude as *"more focused on business customers"*. That positioning is consistent with the [[2026-05-19-kpmg-claude-alliance|KPMG alliance]] and Q2 enterprise trajectory: Anthropic isn't chasing consumer ambient agents head-on against Gemini; the enterprise-and-developer beachhead is where Claude is differentiated. Worth absorbing into outbound Janus positioning — "Claude is the enterprise-AI choice; Gemini is the consumer-AI choice; both can be right" is more defensible than implying Claude is winning a race it's not in.

## Cost trajectory — Bloomberg read (added 2026-05-31)

Bloomberg Opinion (Lionel Laurent, 2026-05-26; [[2026-05-26-bloomberg-bankers-claude-cost]]) reports per-firm Claude bills *"on track to rise from tens of thousands of dollars for a single firm to several million"* among European financial-services customers, driven by compute-supply constraints (H100 spot price rising even after Anthropic's SpaceX capacity deal). Laurent quotes Christopher Tozzi: *"Not every task needs a frontier model."* The piece reports financial-services customers experimenting with **in-house models for non-frontier tasks** — a posture the AIO already operates under via [[stack-composition-framework]] and [[tool-tiers]]. For Janus's current spend profile this is a watch-for, not a blocker: the pressure window for Janus is later than for tier-1 banks, but the discipline of *not* defaulting to frontier-class inference for every task is the right posture to enter the window with. Full read at [[2026-05-31-ai-cost-pressure-in-house-model-shift]].

## Watch for

- Convergence between Claude Code routines and Claude Managed Agents — at some point these may merge.
- Whether file-based agent memory becomes a portable Anthropic standard or stays Claude-only.
- Pricing rationalisation across surfaces (currently a mix of API consumption, Claude Code subscription tiers, and Managed Agents with its own model).
- Cowork plugin ecosystem maturity — important for Janus's wiki + skills setup.
