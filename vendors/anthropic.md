---
type: vendor
title: Anthropic
slug: anthropic
created: 2026-05-06
updated: 2026-06-04
departments: [ai-office]
status: active
confidence: high
sources: [karpathy-llm-wiki, claude-managed-agents-launch, claude-managed-agents-scaling, anthropic-building-effective-agents, claude-code-routines, 2026-05-19-kpmg-claude-alliance, 2026-05-21-anthropic-first-profitable-quarter, 2026-05-20-every-google-io-agents-agents-agents, anthropic-labor-market-impacts-2026-03, 2026-05-26-bloomberg-bankers-claude-cost, anthropic-singapore-office]
related: [claude, llm-wiki, agentic-ai, ai-native-enterprise-restructuring, builders-sellers-measurers, ai-tool-evaluation-framework, observed-exposure-ai-labor-measure]
migrated_from: entities/vendors/anthropic.md
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
- **IPO target date sharpened (2026-05-26).** Bloomberg Opinion ([[2026-05-26-bloomberg-bankers-claude-cost]]) names *"as early as October"* for the stock-market listing — first specific calendar marker the wiki has captured for the IPO trajectory. Treat as opinion-column reporting, not an SEC filing, but consistent with the WSJ-reported Q2 profitability inflection.
- **Pricing-power signal (2026-05-26).** Bloomberg reports per-firm Claude bills among European financial-services customers *"on track to rise from tens of thousands of dollars for a single firm to several million"*, with even the [SpaceX capacity deal](https://www.anthropic.com/news/higher-limits-spacex) not fully absorbing demand. Anthropic is exercising pricing power that should drive the profitable-quarter trajectory; the customer-side response (in-house models for non-frontier tasks; cost-discipline narratives from StanChart's Winters) is captured in [[2026-05-31-ai-cost-pressure-in-house-model-shift]] and on the [[claude]] page.

**Implication for Gate 2.3 ("vendor viability — 24-month horizon").** The criterion is now structurally over-satisfied for Anthropic. Worth a footnote on [[ai-tool-evaluation-framework]] capturing the new baseline. See [[ai-native-enterprise-restructuring]] for the full thesis of how the Q2 signals validate the AIO operating model.

## International expansion — Singapore (added 2026-06-04)

Anthropic advertised four Singapore-based roles on 2026-06-04 (APAC head of accounting, two product support specialists, a regional research economist) — its first visible move toward an SG presence, following OpenAI and Google DeepMind. SG-relevant for Janus (lead market; opens W19). The **regional research economist** role — measuring AI's economic effects with governments/academics — is the in-region extension of the [[observed-exposure-ai-labor-measure|observed-exposure labor work]]. Valuation context: SG sovereign fund **GIC** (first invested Sept 2025; led the Feb 2026 US$30B Series G) is a major backer; the subsequent **Series H puts Anthropic at US$965B, ahead of OpenAI's US$852B**. Full read at [[2026-06-04-anthropic-singapore-office]].

## Corporate moves — May 2026

- **Stainless acquisition (2026-05-19, ~$300M).** Anthropic acquired [Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless), a platform for generating high-quality API SDKs and MCP servers. Reported price ~$300M per The Information. Notable: Stainless's former customers included **OpenAI and Google** — Anthropic has bought a developer-tools company that was core infrastructure for its top model-platform rivals. Strategic read: the acquisition extends Claude's ability to connect to data and tools (the MCP integration layer), tightens Anthropic's grip on the agent-to-software interoperability stack at a moment when both Google (Antigravity 2.0, Spark, Universal Commerce Protocol) and OpenAI (Codex) are pushing into the same surface. Surfaced via Every / Context Window's "Google I/O: Agents, Agents, Agents" coverage; see [[2026-05-20-every-google-io-agents-agents-agents]] for the broader weekly-cluster context. CEO Alex Rattray's earlier *AI & I* podcast appearance laid out the MCP design principles ("keep tools small, name them precisely, generate tightly defined outputs") that look in retrospect like the design ethos Anthropic was acquiring along with the company.

## Research output worth flagging

- **Labor market impacts of AI: A new measure and early evidence** (Anthropic Research; Massenkoff & McCrory; 2026-03-05, corrections 2026-03-08). Filed at [[anthropic-labor-market-impacts-2026-03]]. Introduces *[[observed-exposure-ai-labor-measure|observed exposure]]* — combines theoretical LLM capability with actual Claude-platform usage to measure occupational exposure to AI displacement. Reports no systematic unemployment increase in highly-exposed occupations since late 2022, but tentative evidence (statistically marginal) of a 14% drop in job-finding rates for *workers aged 22-25* entering exposed occupations. Echoes Brynjolfsson et al. (2025)'s 6-16% young-worker employment-fall finding. Important for Janus because Anthropic publishing this *itself* — using its own usage data as the input — is a meaningful posture choice (vendor transparency on the labor question is part of the AI-native sales narrative; cite when AIO is asked about displacement risk in the Marketing or HR positioning). Provides empirical reinforcement to the [[ai-native-enterprise-restructuring]] brief: the soft-landing thesis (no aggregate displacement, but pipeline tightening at the entry point) is now supported by Anthropic's own first-party data.
