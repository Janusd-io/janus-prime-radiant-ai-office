---
type: project
title: Janus Website CMS
slug: janus-website-cms
created: 2026-05-05
updated: 2026-05-19
status: active
owner: michael-bruck
captured_by: jehad-altoutou
departments: [marketing, ai-office, it-ops]
sources: [2026-05-05-michael-jehad-andrew-weekly-meeting, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting]
related: [agentic-lean-marketing-stack, stack-composition-framework, janus-website, singapore-launch, marketing-prime-radiant, janus-crm-selection]
audience: department
---

# Janus Website CMS

The headless CMS layer for the Janus marketing site fleet (janusd.com, janusd.sg, janusd.co.uk, future ccTLDs). Locked to **Cosmic** as of 2026-05-19 on the basis of the [[agentic-lean-marketing-stack]] analysis.

## Decision — Cosmic

**Cosmic** scored 3/3 on the [[stack-composition-framework]]:

- **Composability** — REST-first, TypeScript SDK, MongoDB-style query operators (industry-standard, no proprietary query language).
- **Agent operability** — Official MCP server (`npx @cosmicjs/mcp`) with 17–18 tools (Object Types, Objects, Media, Search). Published Agent Skill (`npx claude-skill add cosmic-headless-cms`) that teaches Claude Code its conventions persistently — same primitive as Janus's [[standup]] / [[ai-registry]] / [[ai-tool-evaluation]] skills. Full-stack CLI handling content management AND Vercel deployment in one command.
- **Reversibility** — Content stored as plain JSON, exportable via API. No proprietary query language to lock in.

Plus operational fit: 400+ locales via `locale=` query parameter; 5 buckets on the Business plan ($499/mo) so Janus can have master bucket + per-region buckets (master = global content, SG bucket = Singapore overrides, UK bucket = UK overrides, …).

### Linear AIR

AIR-117. Status: Backlog as of 2026-05-19 — confirmed direction per Andrew. Requirements list to be prepared by Andrew, due 2026-05-26. No CMS for the initial Singapore launch (hand-coded Next.js pages); Cosmic onboarding lands in the post-launch June window.

## Alternatives considered

| Candidate | Score | Why not |
|---|---|---|
| **Sanity** | 2.5/3 | Strong runner-up, highest G2 rating. Loses 0.5 on reversibility because of GROQ (proprietary query language). |
| **Contentful** | 2/3 | Mature, but hard caps on content types (48 / 150) and locales (3 on Basic). Aggressive cost scaling on multi-locale. |
| **Payload** | 2.5/3 | TypeScript-native, schema-as-code, can install inside Next.js directly. MCP community-only (not official). Worth keeping on radar for full data ownership scenarios. AIR-122 (Backlog). |
| **Adobe AEM** | 1.5/3 | HTL templating accumulates vendor-specific state; enterprise DXP pricing; explicitly called out as "legacy system" by Michael in the 2026-05-19 meeting. **Rejected.** AIR-121. |
| **HubSpot CMS Hub** | 1.5/3 | HubL templating is HubSpot-proprietary; HubDB is HubSpot-only; MCP coverage read-heavy. |

## Operational pattern (post-onboarding)

Master Cosmic bucket holds global content (HQ leadership, brand-wide copy). Per-region buckets hold local overrides (SG case studies, UK press, etc.). Andrew describes campaigns in plain language → Claude Code drafts content → review happens in Cosmic UI → publishes via MCP. Cosmic's MCP and Agent SDKs explicitly support operating across multiple buckets in the same project.

## Stakeholders

- **Decision lead:** [[michael-bruck]]
- **Requirements + operational owner:** [[andrew-soane]]
- **Implementation:** [[jehad-altoutou]] (initial integration), [[andrew-soane]] (ongoing content ops)

## Watch for

- Andrew's requirements list (due 2026-05-26).
- Cosmic onboarding in the June post-Singapore-launch window.
- Multi-bucket multi-region pattern in practice once both SG and UK have local content needs.
- Whether the Agent Skill stays maintained — its persistence in Claude Code is part of the agent-operability score.
