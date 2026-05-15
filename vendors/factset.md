---
type: vendor
title: Factset
slug: factset
created: 2026-05-12
updated: 2026-05-12
status: Backlog
confidence: low
sources: [2026-05-12-aio-andrew-marketing]
related: []
audience: department
captured_by: jehad-altoutou
departments: []
air_id: AIR-96
---

# Factset

Vendor stub created from meeting [[2026-05-12-aio-andrew-marketing]] on 2026-05-12.

_Mention context:_ discussed and explicitly de-prioritised as a named input source

_To populate: replace this stub with real content and remove this notice._


---

## AI Registry — AIR-96

> Linear: [AIR-96](https://linear.app/janusd/issue/AIR-96/factset) · status **Backlog** · updated 2026-05-11.

**Category:** Financial Data Platform + AI Solutions for Finance
**Status:** Backlog
**Cost:** Enterprise sales-led; no public per-seat pricing. Historically thousands USD/seat/year for full Workstation.
**Departments:** Marketing, Finance, Office of CEO, AI Office
**Entity:** FactSet (NYSE: FDS)
**Requested by:** Bonaventure Wong via #ai-internal-hub 2026-05-05

## Overview

Long-established financial data and analytics platform. Tier-1 banks (Barclays, RBC), large manufacturers (Airbus, Renault), retailers, airlines. Past 18 months: AI repositioning — in-platform AI assistant, agent-friendly data access via MCP, AI-enabled Document Search (85k+ users beta), FactSet AI for Banking (with Finster AI), AI crime-risk tooling.

## Capabilities

* **AI-enabled Document Search** — semantic search across filings, earnings calls
* **FactSet AI for Banking** — workflow automation for IB and sell-side research
* **MCP server** — gives AI agents direct, governed access to FactSet data WITHOUT bespoke integrations. Unusual for financial data vendor.
* **Workstation + Concierge AI** — embedded AI assistance
* **AI Financial Crime/Risk** — integrated 2026 with ComplyAdvantage + Cobalt
* Open AI provider posture — public collaborations with OpenAI + Anthropic

## Janus Strategic Position (Updated 2026-05-11)

Original angles: (1) internal Finance utility, (2) commercial fluency. Neither firmly grounded.

**2026-05-08 Marketing Prime Radiant brainstorm produced concrete third angle: FactSet as Signals-layer source for Marketing Prime Radiant.** Prime Radiant pattern: Signals (raw inputs) + Infrastructure + Outputs. Marketing PR Signals layer needs dense industry-vertical coverage across Janus's verticals: real estate, real assets, asset management, sustainability, private equity, credits, banking. FactSet's editorial/data coverage maps onto vertical mix more precisely than almost any general news source. **MCP server makes integration tractable** — PR agents subscribe via MCP rather than bespoke API plumbing.

**Priority of angles post-Marketing brainstorm:**
1. **Marketing PR Signals source** (new, observed demand) — premium industry-vertical news/market data feed. MCP server is integration path. Pricing tier is gating.
2. **Commercial fluency** (original) — reference architecture for FS/asset-mgmt client engagements.
3. **Internal Finance** (original, lowest probability) — Ann Greed's team, historically priced for investment professionals not corporate finance.

## Considerations

* **Pricing tier is gating** — need sub-Workstation read-only data feed access via MCP for agent ingest, not human-analyst seats
* MCP integration angle — most important technical detail (catalog exposure, governance, rate limits)
* Compliance maturity — likely fine for tier-1 financial vendor; specifics need confirming
* Federation implication — if adopted for Marketing PR, becomes available to other dept PRs via MCP

*Backlog. Functional tier. Active Marketing PR Signals consideration; pricing-tier question is gating.*
