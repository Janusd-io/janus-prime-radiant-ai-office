---
type: person
title: Jon Austin
slug: jon-austin
created: 2026-06-11
updated: 2026-06-11
departments: [ai-office, office-of-ceo]
status: active
kind: internal
owner: michael-bruck
captured_by: michael-bruck
sources: [2026-06-11-jon-austin-cto-intro]
related: [bonaventure-wong, janus-prime-radiant-build, michael-bruck]
---

# Jon Austin

**Role:** Incoming CTO, Janus Digital. Start date: TBD.

Australian. Background spans hardware/software engineering, enterprise pre-sales, and technical leadership. Describes his current direction as returning from management back to hands-on technical work — "back in the weeds."

## Background

- **AWS principal architect (Singapore, ~2019):** First principal architect hire in Singapore; focused on large-enterprise pre-sales and customer deployments. Found AWS infrastructure complex and over-engineered; now advocates for simpler patterns (Cloudflare Workers over multi-AZ EC2; SQLite-style simplicity).
- **Fintech:** Worked with/around Mox (Standard Chartered virtual bank, Hong Kong) and the Vacuum Labs team. Plugged into a fintech founder/CTO network including the Mox/Mocks ecosystem.
- **Recent work:** Deployed a multilingual website entirely using Claude; ranked #1 on Google in 6 weeks. Experimenting with Hermes agent framework (see [[questions/ingest-2026-06-11-hermes-vendor-page]]).

## How he joined

Introduced via the fintech network: Chris Ash (Mox) → Ned → [[bonaventure-wong|Bonaventure Wong]] → Jon Austin. Bonaventure arranged the intro call on 11 June 2026. LinkedIn connection established.

## Technical perspective (from intro call)

- Endorsed the **Prime Radiant continual-distillation architecture** immediately: *"It's a continual distillation. Right. It just gets tighter and tighter."* Compared Markdown to ASCII's unexpected resurgence as the canonical LLM format.
- **Build vs buy:** Strongly build-oriented since Opus 4.5 (Dec 2025); Claude Fable (Jun 2026) another step change. *"The needle on build versus buy has just massively swung to build in the last few months."*
- **Infra philosophy:** Cloudflare Workers as default deployment target — "100% success rate." Terraform + Claude Code as workable provisioning path. No multi-AZ unless the workload genuinely requires it.
- **Hermes:** Recommended as the agent orchestration framework gaining CTO-circle consensus. Open source/commercial SaaS model (like Supabase); provider abstraction; guardrails included. Mentioned it is being discussed heavily in his CTO WhatsApp groups.
- **Claude Fable:** Released Jun 9-10 2026; Jon described it as "another step change." Has experience with Claude Mythos Preview via an Australian top-4 bank (found 9,000 vulnerabilities in their codebase on a test run).

## Role context at Janus

Jon will work closely with [[bonaventure-wong|Bonaventure Wong]] (CEO) and [[michael-bruck|Michael Bruck]] (AI Office). Bonaventure framed his scope in the context of Janus scaling to 10 countries by end of year and needing knowledge-base connectivity as the proving point. Jon offered to assist with Prime Radiant cloud hosting and Janus website infrastructure.
