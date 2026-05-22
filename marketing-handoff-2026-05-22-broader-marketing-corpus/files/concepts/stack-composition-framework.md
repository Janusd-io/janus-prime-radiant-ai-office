---
type: concept
title: Stack Composition Framework
slug: stack-composition-framework
created: 2026-05-19
updated: 2026-05-19
departments: [ai-office, it-ops, marketing]
status: active
sources: [marketing-stack-technical-writeup]
related: [ai-tool-evaluation-framework, ai-tool-evaluation, mcp, agentic-ai, agent-skills, ai-native-mandate, agentic-lean-marketing-stack, post-rag-agent-data-stack, janus-prime-radiant-build]
---

# Stack Composition Framework

A three-lens evaluation layer for SaaS tooling decisions, proposed as a **pre-G1 filter** to the formal [[ai-tool-evaluation-framework|AI Tool Evaluation & Approval Framework]]. Surfaced as a load-bearing analytical contribution of the [[marketing-stack-technical-writeup]] (2026-05-19) where it produced the agentic-lean recommendation for the marketing stack.

The framework exists because the existing Gate 1–4 framework evaluates tools *in isolation* — but a lean team's actual problem is operating a *fleet* of tools that interlock. Per-tool evaluation can pass G1–G4 for every individual choice yet still produce an unmanageable stack if the tools don't compose, can't be operated by agents, or can't be migrated when needed.

## The three lenses

### 1. Composability

> What's the data-model contract between this tool and the two or three other tools that touch it?

- **Strong signals:** Standard primitives (contact/company/deal as flat records), clean export formats, documented integration patterns, REST-first API design.
- **Weak signals:** Proprietary data structures, custom objects required for basic use, integration only via paid marketplace connectors, UI-first information architecture.

### 2. Agent operability

> Can a lean team operate this tool primarily through agents like [[claude-code|Claude Code]], or does it require dedicated human ops time?

The **agent triad check**: real CLI + robust API + native MCP server. Plus: is the data model expressible in code (schema-as-code), or only in the UI? Is there a documented Skills pattern (à la [[agent-skills]]) that teaches Claude Code its conventions?

- **Strong signals:** Official MCP server with broad tool coverage, mature CLI covering most operations (not just deployment), public API as the primary interface, TypeScript / JSON schema definitions, documented Skills pattern.
- **Weak signals:** UI-first product where API is an afterthought, narrow CLI, community-only MCP server with limited tool coverage, schema only definable through the UI.

### 3. Reversibility

> If this tool needs to be replaced in 18 months, how hard is that migration?

The discipline that prevents the agentic-lean strategy from regressing over time. The strategy works because tools are replaceable; it stops working as soon as state accumulates that only one vendor can read.

- **Strong signals:** Standard data export formats (JSON, CSV, Parquet, SQL dumps), schema lives in our code repository, business logic implementable in standard languages (TypeScript, Python).
- **Weak signals:** Business logic locked into proprietary languages (Salesforce Apex, HubSpot HubL, Adobe HTL), export requires special tooling or vendor services, critical workflows depend on platform-specific extensions.

## Scoring

| Score | Verdict |
|---|---|
| 3/3 | Preferred default |
| 2/3 | Viable with documented trade-off |
| 1/3 | Generally reject |
| 0/3 | Reject |

## What enables this framework now (and didn't 18 months ago)

Two structural shifts in the 2024–2026 window:

- **MCP becoming a vendor-neutral default** ([[mcp]]). By mid-2026, native MCP servers ship from Salesforce, HubSpot, Attio, Vercel, Cloudflare, Sanity, Cosmic, Contentful, Adobe, Notion, Linear, Stripe, Monday, and hundreds of others. The "agent operability" lens is only meaningful once MCP is a credible expectation, not a wishlist item.
- **Mature agentic coding harnesses.** Vercel reporting 30% of deployments initiated by coding agents (~75% via [[claude-code]]) is the load-bearing data point that agent triad + skills is now a default operating mode for tooling, not an experiment.

## Where this fits in the gated framework

The proposal is to run the three lenses **before Gate 1** as a pre-filter:

```
proposed:  [Stack Composition pre-G1] → G1 viability → G2 fit → G3 sandbox → G4 approval
current:                                  G1 viability → G2 fit → G3 sandbox → G4 approval
```

A tool that scores 1/3 or 0/3 on Stack Composition can be rejected without running G1–G4, saving evaluator hours. A 2/3 tool proceeds with a documented trade-off attached to its evaluation. A 3/3 tool proceeds normally.

The three lenses are also relevant *inside* the gated framework — agent operability overlaps heavily with G2.1 (MCP/AI orchestration compatibility); reversibility overlaps with G1.3 (data portability). The pre-filter framing avoids double-evaluation by making these lenses the entry condition rather than a scored criterion downstream.

## First application — marketing stack

The framework's first concrete output was the [[marketing-stack-technical-writeup|2026-05-19 marketing stack writeup]] (Michael → Jehad), which used the three lenses to produce:

- **3/3 picks:** Cosmic (CMS), Attio (CRM)
- **2.5/3 strong runners-up:** Sanity (CMS — loses 0.5 on GROQ reversibility), Payload (CMS — interesting if self-hosting)
- **2/3 viable-with-trade-off:** Contentful (CMS — content-type caps), Salesforce (CRM — Apex lock-in), HubSpot (CRM — bundling play only)
- **1.5/3 reject:** Adobe AEM (CMS — HTL templating), HubSpot CMS Hub (HubL templating)

The corresponding aha is captured in [[agentic-lean-marketing-stack]].

## Watch for

- Adoption of the framework as a formal pre-G1 step in `processes/ai-tool-evaluation-framework.md` — currently a proposal, not ratified.
- Whether the three lenses generalise cleanly to non-marketing categories (engineering tooling, HR systems, financial software). Likely yes, but each domain will surface its own canonical "agent triad" expectations.
- Whether new tool categories (browser-native agents, e.g. Claude in Chrome) force a fourth lens or modify the existing three.
- Cross-references to the [[ai-native-mandate|AI-native mandate]] — the procurement-side rule that says "no AI tool unless approved." The Stack Composition Framework is the upstream filter that lets evaluators be confident a candidate is even worth running through approval.
