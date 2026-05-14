---
type: source
source_type: laptop
title: 06-FIRST-VOICE-FINAL
slug: 06-first-voice-final
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/06-FIRST-VOICE-FINAL.md
original_size: 5698
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.85
sensitivity_reason: "Jehad's First Voice questionnaire response to ISO lead — descriptive of his role; dept-shareable IMS evidence."
---

# 06-FIRST-VOICE-FINAL

_Extracted from `Documents/janus-puls-onboarding/06-FIRST-VOICE-FINAL.md` on 2026-05-14._

# PULS First Voice — AI Operations Engineer

**Submitted by:** Jehad — AI Operations Engineer, Janus Digital
**Process areas:** C1 AI System Design & Development · C2 Software Development & Release · S2 IT Infrastructure & Data Governance
**To:** Simon (ISO Lead)
**Date:** 7 May 2026

---

Hi Simon,

Following the IMS Development Programme deck, here are my answers to the six PULS First Voice questions for my AI Operations Engineer role. Happy to walk through any section in our tooling sync.

---

## Q1 — My work · inputs & outputs

### Sources of inputs

- **Internal — meetings:** Department / team kickoff meetings where requirements are gathered face-to-face.
- **Internal — Slack:** Slack channels for async requests, feature ideas, and support questions from other departments.
- **Internal — leadership:** Michael Bruck (AI Projects lead) for strategic priority and approval.
- **External — vendors:** Anthropic (Claude), OpenAI, Vercel, Hostinger, Airwallex, n8n.
- **External — regulators:** UAE, Singapore, UK (jurisdiction-specific requirements when applicable).

### Inputs

- Requirements gathered from meetings or Slack threads.
- Existing system constraints (current stack, infrastructure, budget).
- Access requirements (credentials, third-party API keys).
- Strategic direction from Michael / leadership.

### Activities (how I work end-to-end)

1. **Gather requirements** — meetings or Slack until scope is clear.
2. **Build in sandbox** — develop the feature / system in an isolated environment.
3. **Run testing phase** — stress test from all angles: functionality, UI/UX, security, APIs. Try to break it.
4. **Fix and enrol** — patch what testing surfaced.
5. **Document** — write SOP, README, implementation plan.
6. **Hand over to IT** — IT department deploys it from sandbox to company-wide internal use.

### Outputs

- Sandbox-tested working software (feature, system, automation, AI agent).
- SOP document.
- README.
- Implementation plan.
- Handover package for the IT department.

### Receivers of outputs

- **Primary:** IT department — they take the handover package and deploy company-wide.
- **Secondary:** Internal end-users (the departments / teams who requested the feature).
- **Eventual:** Process Owners, clients, partners (when the work is client-facing).

---

## Q2 — Controls and check points

| Stage | Control |
|---|---|
| **Before build** | Requirements gathered and confirmed (no build starts without complete scope) |
| **Build** | Done in isolated sandbox — never directly in production |
| **Stress test** | Functionality coverage · UI/UX walkthrough · security checks · API behaviour under load · attempts to break the system |
| **Pre-handover** | SOP + README + implementation plan must all exist |
| **Handover gate** | IT department reviews and accepts before company-wide deploy |

---

## Q3 — Tools & systems I use

### AI

- Claude AI (Claude API + Claude Code)
- OpenAI (GPT models, Codex)
- Antigravity (Gemini skills system, 1,328+ modules)
- AI Gateway (provider routing)

### Development

- Claude Code, Codex
- Cursor / VS Code
- Next.js 15 (App Router) · React · TypeScript · Tailwind · shadcn/ui
- Drizzle ORM · Neon Postgres
- n8n (workflow automation, self-hosted)

### Infrastructure & deployment

- Vercel (frontend / API hosting)
- Hostinger VPS (Ubuntu 24.04, Docker, Caddy) — runs n8n + Postgres
- GitHub (source control, CI/CD)
- Cloudflare / GoDaddy (DNS)

### Productivity & comms

- Notion (documentation)
- Linear (issues, CAPA, audit findings)
- Slack (team comms)
- Obsidian (knowledge brain / personal knowledge graph)

> **Note for the AI Systems Register (ISO 42001):** Claude AI, OpenAI, Antigravity, Claude Code, Codex, AI Gateway and any agent built on top of these all need register entries. Happy to draft the schema if useful.

---

## Q4 — My KPIs

I don't currently track formal KPIs. My quality bar is **"can I break it?"** — I try to find weaknesses myself before users do, across five areas:

- **Functionality** — does every feature work under expected load?
- **UI / UX** — is it usable, accessible, and intuitive?
- **Security** — does it survive standard attack patterns and API abuse?
- **APIs** — response times, error rates, edge cases.
- **Stability** — does it stay up under sustained use?

If I can't break it across those five areas, it's ready for handover.

**Open ask:** I'd appreciate your help defining formal KPIs for these criteria — pass/fail thresholds, measurement frequency, target values — so the test phase produces something the PULS dashboard can monitor automatically.

---

## Q5 — What I need to work better

Nothing is blocking me right now.

**Future asks:**

- More access budget for evaluating new tools and platforms, so we don't fall behind on AI tooling improvements.
- Faster path to spin up sandboxes for testing new approaches.

---

## Q6 — Questions & ideas

- Should every Claude Code skill I author become an AI Systems Register entry automatically (for example via a pre-commit hook)? Zero-overhead 42001 compliance for our internal AI tooling.
- For the C1 / C2 / S2 process documents — am I the named Process Owner, or splitting with Michael?
- Suggestion: the PULS First Voice form itself could live inside PULS — its responses become the seed data for each process document, closing the feedback loop described on slide 15 of the deck.
- Suggestion: build the first 3 process documents (mine — C1, C2, S2) as the proof-of-concept template before rolling out the form to the whole company.

---

Best,
Jehad

*AI Operations Engineer · Janus Digital · jehada@janusd.io*
