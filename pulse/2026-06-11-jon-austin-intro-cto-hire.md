---
type: pulse
title: "Jon Austin joins as CTO — build vs buy pendulum, Hermes framework, Claude Fable"
slug: 2026-06-11-jon-austin-intro-cto-hire
created: 2026-06-11
updated: 2026-06-11
departments: [ai-office, office-of-ceo]
confidence: high
sources: [2026-06-11-jon-austin-cto-intro]
related: [janus-prime-radiant-build, bonaventure-wong, michael-bruck]
---

# Jon Austin joins as CTO — build vs buy pendulum, Hermes framework, Claude Fable

**Why this matters to the AIO:** Jon Austin will join Janus as CTO. The intro call (June 11, 2026) produced three operationally relevant signals: (1) independent validation of the Prime Radiant continual-distillation architecture by an experienced practitioner; (2) a strong recommendation for the **Hermes** agent orchestration framework as the developer-consensus pick in CTO circles; (3) confirmation that **Claude Fable** (released ~June 9-10, 2026) represents another step-change in model capability — already generating significant buzz and real deployment results in the Australian enterprise market.

## Context

Introduction arranged by Bonaventure Wong. Jon is Australian, ex-AWS principal architect (first principal hire in Singapore, ~2019), fintech background (Mox / Standard Chartered virtual bank; Vacuum Labs). Described as having recently moved back from management into technical work ("back in the weeds"). Connected via the fintech network: Chris Ash → Ned → Bonaventure.

## Prime Radiant validation

Michael gave a live demo of the Prime Radiant architecture. Jon's summary: *"It's a continual distillation. Right. It just gets tighter and tighter."* He independently compared Markdown to ASCII (both had seemed dead, both are resurgent because of LLMs). Also drew the SQLite analogy — a system that scales from one user to a million on a flat file is elegant, not under-engineered. Brittle current setup acknowledged; cloud hosting target confirmed ([[janus-prime-radiant-build]]). Jon offered to assist with the infrastructure migration.

## Hermes agent framework

Jon recommended **Hermes** as the agent orchestration framework generating consensus in CTO WhatsApp groups. Key properties from the intro call: open source; commercial hosted SaaS model (like Supabase); abstracts provider-specific API integrations; works across data sources (RAG, markdown directory, SQL database); implements guardrails; developers building at serious scale are adopting it. Jon is experimenting with it currently. Michael noted it is on his tracker and added it to the evaluation queue. See escalation `questions/ingest-2026-06-11-hermes-vendor-page.md`.

## Claude Fable

Released approximately June 9-10, 2026 (two days before this call). Jon: *"With Fable, it's another step change again."* Heavy discussion in CTO peer networks. He credited two model moments as responsible for the current build-vs-buy swing: Opus 4.5 (released ~December 2025) and now Fable. Real-world evidence from an Australian top-4 bank: they spent 250–280M AUD with Anthropic in the trailing 12 months; access model was Microsoft Teams gating for non-technical staff; temporary access to Claude Mythos Preview surfaced 9,000 vulnerabilities in their codebase, triggering internal panic. Consistent with Amodei's policy essay (same day).

## Build vs buy

Jon's closing thesis: *"The needle on build versus buy has just massively swung to build in the last few months."* Open source + extend + maintain now dominates over enterprise SaaS for internal tools, specifically since Opus 4.5. Validates the direction of the AIO tooling strategy (Assessify, Prime Radiant, NanoClaude). Aligns with the [[builders-sellers-measurers]] framing.

## Other technology signals (lower priority)

- **Temporal** (durable workflow engine, Uber Cadence fork): just valued at $5.5B. Jon mentioned it as a successful commercial open source example. Relevant if Janus needs reliable background job execution at scale; file as low-priority research item.
- **Cloudflare Workers**: Jon recommended these over CloudFront/Vercel for infrastructure. *"100% success rate on Cloudflare Workers — deploy on free tier."* Relevant to the AIO website infrastructure session to be scheduled with IT.
- **NanoClaude / nanopl**: Jon referenced it by name as a containerised Claude Code deployment model. He's aware of it from the same CTO circles.
