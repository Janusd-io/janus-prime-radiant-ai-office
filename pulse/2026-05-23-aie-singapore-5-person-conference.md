---
type: pulse
title: AI Engineer Singapore — 5 part-time people ran a 1,000-person conference by treating event ops as a data problem
slug: 2026-05-23-aie-singapore-5-person-conference
created: 2026-05-23
updated: 2026-05-23
departments: [ai-office, marketing, engineering]
countries: [sg]
confidence: high
sources: [2026-05-23-aie-singapore-5-person-conference-singh]
related: [agentic-lean-marketing-stack, builders-sellers-measurers, ai-native-enterprise-restructuring, stack-composition-framework, resend, singapore-launch]
---

# AI Engineer Singapore — 5 part-time people ran a 1,000-person conference by treating event ops as a data problem

Agrim Singh published a writeup on 2026-05-23 of how 5 part-time team members ran the AI Engineer Singapore conference for 1,000+ attendees. Source: [[2026-05-23-aie-singapore-5-person-conference-singh]]. The piece is a real-world operational exemplar of the agentic-lean operating model the AIO has been theorising — small headcount + extensive custom-software substrate, executed in Singapore, at conference scale.

## The stack they ran

| Tool | Role | Janus parallel |
|---|---|---|
| **[Convex](https://www.convex.dev/)** | Realtime backend for every custom app — speaker portal, workshop ops, live attendee site, lead scanner, admin tools | Janus doesn't have an equivalent; [[hostinger]] + Postgres is the closest substrate posture |
| **Next.js** | Web frontends for every surface | [[janus-website]] / [[janus-website-cms]] use the same stack via Vercel |
| **[[resend\|Resend]]** | All transactional + campaign email | Same vendor Janus locked in for the marketing stack ([[agentic-lean-marketing-stack]]) |
| **Devin AI** | Built the conference website | Janus doesn't use Devin; Cursor + Claude Code are the equivalents |
| **OpenAI Codex + Cursor Cloud** | Built the internal apps, especially while traveling | [[claude-code]] is the Janus equivalent surface |
| **Manus AI** | Browser-based ops teammate for LinkedIn + Twitter/X outreach | No Janus parallel — not in Registry. Worth a Stage 1 triage candidate if outreach automation becomes a need. |
| **Notion** | Lightweight human-readable layer where it made sense | Same role at Janus per the [[notion]] system-of-record |

The article explicitly frames Resend as part of the operational stack — direct external validation of the [[resend|Resend]] choice in Janus's marketing stack lock-in (2026-05-19).

## The seven operating principles (verbatim from the article)

1. **If data matters, put it in a backend.**
2. **If a workflow repeats, build a small app.**
3. **If staff need to inspect something, make an admin view.**
4. **If attendees need to act, give them a direct surface.**
5. **If agents need to help, expose an API.**
6. **If email depends on state, send from state.**
7. **If data is incomplete, save it anyway.**

These map onto the [[stack-composition-framework|Stack Composition Framework]] (composability + agent operability + reversibility) with one notable extension: **principle 5 ("if agents need to help, expose an API")** is the cleanest articulation yet of *making your own systems agent-readable* — not just *adopting agent-operable vendor tools* but *structuring your internal systems so agents can consume them*. The conference website was for humans; the conference API was for everything else.

## Three reads for the AIO

1. **External validation of the agentic-lean operating model at small-team scale.** [[builders-sellers-measurers|Drucker]] would have predicted this: 5 builders/sellers + the measurer-substrate written into custom software. The 5-people-to-1000-attendee ratio is the empirical proof at small scale that mirrors what JPMorgan-Dimon / Cloudflare-Prince are claiming at large scale (see [[ai-native-enterprise-restructuring]]). Same shape, different N. Cite alongside the Cloudflare layoff-while-growing data when the position needs a relatable mid-size example.

2. **Principle 5 ("expose an API") is the principle that's *missing* from the Stack Composition Framework.** The framework currently says: choose vendors that are themselves agent-operable. Singh's piece adds: *build your own systems to be agent-operable too*. For Janus this maps onto the Prime Radiant pattern explicitly — every wiki page is markdown-readable, frontmatter is queryable, the `index.md` is grep-able. But for Janus's *vendor-shaped* systems (the website, the CRM, the email tooling), the agent-operability question is not just "is this vendor MCP-friendly" but "have we exposed our own data layer so an agent can act on it." Worth a [[stack-composition-framework]] update or a question page proposing a fourth lens.

3. **Singapore-specific.** The conference was AI Engineer Singapore. Singh's writeup is a credible Singapore-tech-scene signal — exactly the kind of pulse [[singapore-news-monitoring|Bonaventure's Singapore monitoring]] should be picking up. The Janus Singapore launch ([[singapore-launch]]) and the broader [[ai-native-janus-positioning|positioning]] can reference this writeup as evidence of the agentic-lean model being already-practised inside the SG AI-engineering community. *This is the kind of operational story the lunch event in September 2026 should aim to be in conversation with.*

## Where the article diverges from the AIO posture

- **They used Devin AI + Cursor + Codex; Janus uses [[claude-code|Claude Code]].** Same family of agent-coding tools, different vendor mix. The article is vendor-agnostic on the build-stack point.
- **They used Convex (realtime backend).** Janus's posture is [[hostinger]] + Postgres (per the [[2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]] decision). Convex is a managed-service alternative; would deserve Stage 1 triage if a Janus project hits the same "we need a realtime backend in 3 days" requirement.
- **They used Manus AI for outreach.** Janus has not evaluated Manus. The use case (browser-agent that operates LinkedIn/Twitter at a constrained-delegation cadence) is interesting and would map well onto AIO outreach work if and when that becomes a need.

## Watch for

- Whether Singh's framework ("event ops is a data problem") gets adopted by other small-team conferences as the operational template.
- Manus AI uptake signals — if it's broadly useful for browser-agent outreach work, worth an AIR triage entry.
- Whether AI Engineer Singapore becomes an annual fixture — useful Janus marketing-and-recruitment surface if so.
- Cross-reference: how the [[singapore-news-monitoring|Singapore monitoring]] agent handles Singapore-tech-scene signals like this one. Worth checking whether this writeup was surfaced by that monitoring or only via Michael's manual inbox drop.
