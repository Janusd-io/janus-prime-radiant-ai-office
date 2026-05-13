---
type: source
notion_url: https://www.notion.so/356114fc090c81ddb84fe6c701c35e0a
notion_id: 356114fc-090c-81dd-b84f-e6c701c35e0a
title: Vibe-Coding & Vibe-Design Bakeoff — Cohort Analysis (May 2026)
source_type: notion-page
fetched: 2026-05-06
---

# Vibe-Coding & Vibe-Design Bakeoff — Cohort Analysis (May 2026)

**Status:** Active — cohort logged in AI Registry, all in Backlog except Replit (Evaluating)
**Last updated:** 2026-05-04
**Owner:** Michael Bruck, Head of AI Office

## Headline framing

This is **two distinct decisions** made independently, then composed:

1. **App-stage decision (vibe coding):** Pick a primary chat-to-app builder. Candidates: **Hercules, Lovable, Bolt, v0, Replit.** All output deployable, hosted full-stack applications.

2. **Design-stage decision (vibe design):** Pick a primary design front-end. Candidates: **Google Stitch, Claude Design.** Neither deploys a working app alone — both produce high-fidelity prototypes plus code, with hand-off to downstream coding agent or app builder.

**Full pipeline:** design tool → handoff → app builder. Natural pairings: *Stitch + Antigravity* (Google-native) or *Claude Design + Claude Code* (Anthropic-native).

## Cohort at a glance

| Tool | Stage | Status | Best at | Compliance |
|---|---|---|---|---|
| **Lovable** | App-stage | Backlog | End-to-end full-stack web apps, strong design polish | SOC 2 Type II + ISO 27001 + GDPR + EU/US/AU residency |
| **v0** | App-stage | Backlog | UI/component generation in Next.js + Tailwind + shadcn/ui | SOC 2 Type 2 (Vercel) + GDPR + sandboxed Function execution |
| **Replit** | App-stage | Evaluating | Real browser IDE + Replit Agent | SOC 2 Type II + GDPR + SSO on Teams |
| **Hercules** | App-stage | Backlog | Vertically integrated — commerce, mobile (App/Play Store), batteries-included | SOC 2 Type I + GDPR cert in progress + EU residency on Enterprise |
| **Bolt** | App-stage | Backlog | Multi-agent across labs, WebContainer runtime, design-system import | Opaque — Enterprise claims security; no public trust portal |
| **Stitch** | Design-stage | Backlog | Infinite canvas, voice, design-system DESIGN.md, parallel agent runs | Labs experiment — no DPA yet; inherits Google policies |
| **Claude Design** | Design-stage | Backlog | Chat + canvas, brand-aware, prototype + slide + PPTX + Canva exports, Claude Code handoff | Inherits Claude for Work: SOC 2 II + ISO 27001 + GDPR + ZDR |

## IT-readiness heat-map (today)

1. **Lovable** — strongest published cert stack; trust center; explicit data residency; SCIM on Enterprise.
2. **Claude Design** — rides existing Claude for Work agreement; certifications already accepted; zero net-new vendor.
3. **v0** — covered by Vercel SOC 2 Type 2; clear training-opt-out at Business+.
4. **Replit** — SOC 2 Type II + GDPR; SSO on Teams; mature.
5. **Hercules** — SOC 2 Type I (Type II roadmap); GDPR in progress; EU residency on Enterprise.
6. **Stitch** — Labs; no Stitch-specific DPA; boundary unclear; expected GA Q4 2026.
7. **Bolt** — opaque compliance; needs explicit security questionnaire before any Janus content.

## Design-stage comparison: Stitch vs Claude Design

| Dimension | Stitch | Claude Design |
|---|---|---|
| **Workflow** | Chat + infinite canvas, voice critique, parallel agent runs | Chat + canvas, inline comments, branch versioning |
| **Output** | High-fidelity UI flows; React code; MCP/SDK exports | Prototypes + decks + PPTX/PDF/Canva exports + Claude Code handoff |
| **Handoff** | AI Studio / Antigravity / any MCP IDE | Claude Code (local or Web) |
| **Cost today** | Free (Labs) | Free (rides Claude Team seats) |
| **Compliance today** | Labs status — no DPA, boundary unclear | Solid — inherits Claude for Work certs |
| **Composability** | Open-source DESIGN.md, MCP, SDK, skills library | Closed format, deep into Claude Code |
| **Ecosystem pull** | Google stack (Workspace, Gemini, Antigravity, Firebase) | Claude stack (Claude Team, Claude Code) |

**Practical read:** Claude Design wins on compliance and zero-onboarding today. Stitch wins on agentic-tool composability and alignment with Janus's Google footprint. Both credible — real choice partly depends on app-stage decision.

## How to run the bakeoff

**Pass 1 — App-stage cohort:**
1. Define one fixed Janus prompt (suggested: *"Build an internal RFP intake form with email notifications and a basic admin view"*).
2. Run same prompt through all five (Lovable, v0, Replit, Hercules, Bolt).
3. Single owner — consistent judging.
4. **Bolt prerequisite:** No evaluation beyond surface-level until StackBlitz answers security questionnaire.

**Pass 2 — Design-stage cohort:**
1. Same fixed prompt + UX design framing.
2. Run through Stitch and Claude Design.
3. Decide independently — but strong end-to-end pipeline signal (e.g., Stitch + Antigravity vs Lovable) is valid input.

**Cross-cutting actions:**
- Move all six new entries (AIR-87, 88, 89, 90, 91 + AIR-32) to **Evaluating** when bakeoff starts.
- **Adopt DESIGN.md as a Janus design-system handoff format** regardless of tool choice — open-source, no lock-in.
- **Loop IT/ITO early** under 2026-04-30 compliance reset.
- **Block free/personal accounts** on janusd.io emails for all six tools.

## Open questions before recommendation

1. Google-native pipeline (Stitch + Antigravity + Firebase) or independent best-of-breed (Lovable/v0/Replit)?
2. Realistic 6-month total cost at Janus pilot scale (10 active builders, ~5 hosted apps)?
3. Where does Stitch sit relative to Workspace certification boundary, and when does it exit Labs?
4. Can StackBlitz provide SOC 2 Type II, ISO 27001, GDPR DPA, and training-opt-out attestation in bakeoff timeline, or is Bolt effectively eliminated?
5. Must Janus design system be curated/formalised before Stitch or Claude Design can be meaningfully evaluated?
6. Who owns the bakeoff — AI Office, ITO, or jointly?

## Linear cohort

AIR-32 (Replit), AIR-80 (Claude Design), AIR-87 (Hercules), AIR-88 (Lovable), AIR-89 (Bolt), AIR-90 (v0), AIR-91 (Google Stitch).
