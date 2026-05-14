---
type: source
source_type: notion
slug: vibe-coding-vibe-design-bakeoff-cohort-analysis
title: Vibe-Coding & Vibe-Design Bakeoff — Cohort Analysis (May 2026)
created: 2026-05-04
captured_by: jehad-altoutou
notion_url: https://www.notion.so/356114fc090c81ddb84fe6c701c35e0a
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

**Status:** Active — cohort logged in AI Registry, all in Backlog except Replit (Evaluating)
**Last updated:** 2026-05-04
**Owner:** Michael Bruck, Head of AI Office
**Linear cohort:** [AIR-87 Hercules](https://linear.app/janusd/issue/AIR-87/hercules) · [AIR-32 Replit](https://linear.app/janusd/issue/AIR-32/replit) · [AIR-88 Lovable](https://linear.app/janusd/issue/AIR-88/lovable) · [AIR-89 Bolt](https://linear.app/janusd/issue/AIR-89/bolt) · [AIR-90 v0](https://linear.app/janusd/issue/AIR-90/v0) · [AIR-91 Google Stitch](https://linear.app/janusd/issue/AIR-91/google-stitch) · [AIR-80 Claude Design](https://linear.app/janusd/issue/AIR-80/claude-design)
---
## Why this page exists
A Slack request in `#ai-internal-hub` for Hercules turned into a full cohort analysis across the chat-to-app ("vibe coding") and chat-to-design ("vibe design") category. The analysis grew across multiple conversational turns and risks getting lost as the chat scrolls. This page is the durable record. The Linear entries hold the per-tool detail; this page holds the *framing* — how the tools relate to each other, how the bakeoff should be run, and where each tool sits on IT-readiness today.
---
## Headline framing
The cohort isn't one bakeoff — it's **two distinct decisions** that should be made independently and then composed:
1. **App-stage decision (vibe coding)** — pick a primary chat-to-app builder. Candidates: **Hercules, Lovable, Bolt, v0, Replit.** All five output a deployable, hosted full-stack application.
2. **Design-stage decision (vibe design)** — pick a primary design front-end. Candidates: **Google Stitch, Claude Design.** Neither deploys a working app on its own — both produce high-fidelity prototypes plus code, with hand-off to a downstream coding agent or app builder.
The full pipeline is **design tool → handoff → app builder**. Today's natural pairings are *Stitch + Antigravity* (Google-native) or *Claude Design + Claude Code* (Anthropic-native). Each pairing leans on existing Janus investments, so picking the design tool nudges the app-builder decision and vice versa.
---
## The cohort at a glance
<table header-row="true">
<tr>
<td>Tool</td>
<td>AIR</td>
<td>Vendor</td>
<td>Stage</td>
<td>Status today</td>
<td>Best at</td>
<td>Public compliance</td>
</tr>
<tr>
<td>**Lovable**</td>
<td>AIR-88</td>
<td>Lovable (Stockholm)</td>
<td>App-stage</td>
<td>Backlog</td>
<td>End-to-end full-stack web apps with strong design polish</td>
<td>SOC 2 Type II + ISO 27001 + GDPR + EU/US/AU residency</td>
</tr>
<tr>
<td>**v0**</td>
<td>AIR-90</td>
<td>Vercel</td>
<td>App-stage</td>
<td>Backlog</td>
<td>UI/component generation in Next.js + Tailwind + shadcn/ui</td>
<td>SOC 2 Type 2 (under Vercel) + GDPR + sandboxed Function execution</td>
</tr>
<tr>
<td>**Replit**</td>
<td>AIR-32</td>
<td>Replit</td>
<td>App-stage</td>
<td>Evaluating</td>
<td>Real browser IDE + Replit Agent for builders who want a real codebase</td>
<td>SOC 2 Type II + GDPR + SSO on Teams</td>
</tr>
<tr>
<td>**Hercules**</td>
<td>AIR-87</td>
<td>Zeus AI Labs (SF)</td>
<td>App-stage</td>
<td>Backlog</td>
<td>Vertically integrated stack — native commerce, mobile (App Store / Play), batteries-included</td>
<td>SOC 2 Type I + GDPR cert in progress + EU residency on Enterprise</td>
</tr>
<tr>
<td>**Bolt**</td>
<td>AIR-89</td>
<td>StackBlitz</td>
<td>App-stage</td>
<td>Backlog</td>
<td>Multi-agent across labs, WebContainer runtime, design-system import</td>
<td>Opaque public posture — Enterprise claims security; no public trust portal</td>
</tr>
<tr>
<td>**Stitch**</td>
<td>AIR-91</td>
<td>Google Labs</td>
<td>Design-stage</td>
<td>Backlog</td>
<td>Infinite design canvas, voice mode, design-system [DESIGN.md](http://DESIGN.md), parallel agent runs</td>
<td>Google Labs experiment — no Stitch-specific DPA yet; inherits Google policies</td>
</tr>
<tr>
<td>**Claude Design**</td>
<td>AIR-80</td>
<td>Anthropic</td>
<td>Design-stage</td>
<td>Backlog</td>
<td>Chat + canvas, brand-aware, prototype + slide + PPTX + Canva exports, Claude Code handoff</td>
<td>Inherits Claude for Work: SOC 2 Type II + ISO 27001 + GDPR + ZDR options</td>
</tr>
</table>
---
## IT-readiness heat-map (today)
Based on public posture today — independent of capability fit. Higher = lower friction to approve through ITO under the 2026-04-30 compliance reset.
1. **Lovable** — strongest published cert stack in the cohort; published trust center; explicit data residency; SCIM on Enterprise.
2. **Claude Design** — rides on existing Claude for Work agreement; certifications already accepted; zero net-new vendor onboarding.
3. **v0** — covered by Vercel's SOC 2 Type 2 attestation; clear training-opt-out at Business+; well-documented threat model.
4. **Replit** — SOC 2 Type II + GDPR; SSO on Teams; mature platform.
5. **Hercules** — SOC 2 Type I (Type II on roadmap); GDPR cert in progress; EU residency available on Enterprise.
6. **Stitch** — Labs status; no Stitch-specific DPA; inherits Google policies but boundary unclear; expected GA Q4 2026.
7. **Bolt** — opaque public compliance posture; needs explicit security questionnaire and DPA conversation before any Janus content.
---
## App-stage cohort (vibe coding)
### Lovable — AIR-88
*Stockholm-based; chat-to-app full-stack web; Lovable Cloud for managed hosting/auth/DB; mobile app recently launched.*
- **Pricing:** Free; **Pro \$25/mo** (100 credits, shared across unlimited users); **Business \$50/mo** (adds SSO, RBAC, security center); **Enterprise** custom (SCIM, audit logs, custom connectors). Pricing per workspace, not per seat — unusual and cost-efficient for many occasional builders.
- **Compliance:** SOC 2 Type II ✅ · ISO 27001 ✅ · GDPR ✅ · EU/US/AU residency · No model training on customer prompts/code/workspace · Trust center at [trust.lovable.dev](http://trust.lovable.dev).
- **Differentiation:** Strongest compliance posture in the cohort. Pro plan's shared-credit pool fits Janus's likely usage profile (many occasional builders). Explicit no-CI/CD-access posture reads well for IT.
- **Weakness:** Lovable Cloud lock-in for hosting; primarily web-only (mobile is newer); credit pricing predictability degrades at scale.
### v0 — AIR-90
*Vercel; origin as a Tailwind + shadcn/ui component generator, expanded into full chat-to-app; deploys to Vercel by default.*
- **Pricing:** Free \$0 (\$5 credits, 7 msg/day); **Team \$30/user** (\$30 credits, \$2/day on login); **Business \$100/user** (Team + training-opt-out by default); **Enterprise** custom (SAML SSO, RBAC, no-training guarantee, SLAs). Token-priced models from v0 Mini (\$1/1M input) up to v0 Max Fast (\$30/\$150 per 1M).
- **Compliance:** SOC 2 Type 2 ✅ (under Vercel) · GDPR ✅ · Vercel Trust Center · Training opt-out auto on Business+ · SAML SSO + RBAC + audit logs on Enterprise.
- **Differentiation:** Strongest UI quality in the cohort (Tailwind + shadcn/ui defaults); embedded in third-party IDEs (Cline / Cursor / OpenAI Codex / Zed); explicit threat-model docs and sandboxed Vercel Function execution.
- **Weakness:** Most opinionated stack — Next.js + Vercel native, less useful outside that pipeline. Business at \$100/user is the highest sticker in the cohort.
### Replit — AIR-32
*Mature browser IDE + Replit Agent. Already in Evaluating status, only cohort tool that is.*
- **Pricing:** Free Starter; Replit Core \$25/mo; Replit Teams \$40/seat/mo.
- **Compliance:** SOC 2 Type II ✅ · GDPR ✅ · SSO/SAML on Teams · Private repls on paid · Firewall and networking controls on Teams.
- **Differentiation:** Real IDE with multi-language support, real shells, mobile coding, and a strong dev community. The agent sits inside a fully developer-grade environment, not a chat-only surface.
- **Weakness:** Tool-sprawl risk — VS Code (AIR-15), Claude Code (AIR-13), Firebase Studio (AIR-31), Antigravity (AIR-16/AIR-34) already in the picture. AI Agent demos well but production-quality output is the open question.
### Hercules — AIR-87
*Zeus AI Labs (SF); claims 100k+ users; the most vertically integrated stack in the cohort — auth/db/payments/email/push/analytics native; mobile + commerce out of the box.*
- **Pricing:** Free + credit-based pay-as-you-go; specific seat tiers not publicly listed (page is JS-rendered). Business tier unlocks SSO/SAML; Enterprise is custom.
- **Compliance:** SOC 2 Type I (Type II roadmap) · GDPR cert in progress · HIPAA claimed at Enterprise · TLS 1.3 + AES-256-GCM · EU (Frankfurt) or US (Virginia) residency · Training opt-out only on Team / Enterprise (default-on otherwise).
- **Differentiation:** Lowest integration surface — single-vendor stack means less third-party glue to govern. First-class Apple App Store / Google Play publish.
- **Weakness:** Default-on training on free / individual plans rules them out for Janus content under Section 5.2.3. Newer vendor with less public maturity. Apps lock to Hercules Cloud (Cloudflare + Convex) — portability unverified.
### Bolt — AIR-89
*StackBlitz; built on the WebContainer browser runtime; pitches itself as the "professional vibe coding tool" with multi-agent routing across frontier labs.*
- **Pricing:** Free \$0 (1M tokens/mo, 300K daily cap); Pro \$25/mo (10M tokens/mo); Teams \$30/user/mo; Enterprise custom. Token rollover for one extra month on paid plans.
- **Compliance:** **Opaque.** Enterprise marketing references "compliance support" but no public trust portal, no published SOC 2 attestation, no documented data residency or training-opt-out story. Public reviews early 2026 reported "no SOC 2 / GDPR / HIPAA."
- **Differentiation:** Multi-agent across labs in one UI; very large codebase support; corporate design-system import (Porsche, WaPo, Material UI, Chakra, Shadcn referenced); WebContainer near-native dev feel.
- **Weakness:** Compliance gap is the single biggest concern — needs explicit security questionnaire and DPA conversation before any Janus content. Token-based pricing predictability is harder than seat-based.
---
## Design-stage cohort (vibe design)
Stitch and Claude Design are near-mirror images of each other and are a different category from the app-stage cohort. Both produce high-fidelity prototypes plus code, both rely on a downstream coding agent to ship, both ride on a frontier-lab Labs/preview surface.
### Google Stitch — AIR-91
*Google Labs; coined "vibe design"; AI-native infinite canvas; relaunched 2026-03-18 with design agent + agent manager + voice + *[*DESIGN.md*](http://DESIGN.md)* format.*
- **Pricing:** Free during Google Labs phase. Reported limits: \~400 daily design credits, \~12,450/month. Paid plans expected by Q4 2026; third-party speculation positions pricing 30–50% below Figma.
- **Compliance:** Labs experiment — no Stitch-specific DPA or trust portal. Inherits Google's broader posture but the boundary (Workspace cert vs Labs) is unclear. Workspace SSO probable; data residency / training opt-out unclear.
- **Differentiation:** Design-system import via URL or [DESIGN.md](http://DESIGN.md) (open-sourced 2026-04-21). Voice mode for live critique. Parallel agent runs for divergent exploration. Open-source MCP server, SDK, and skills library (`google-labs-code/stitch-skills`, \~2.4k GitHub stars) — composable with Claude Code, Cursor, and the rest of the agentic stack.
- **Strategic angle:** Slots cleanly into Janus's existing Google footprint (Workspace + Gemini AIR-5 + Google Cloud AIR-7 + AI Studio AIR-8 + Gemini CLI AIR-12 + Antigravity AIR-16/AIR-34 + Firebase Studio AIR-31). Lowest-friction entry point for Marketing / Commercial today.
### Claude Design — AIR-80
*Anthropic Labs; chat + canvas; design system aware; preview status; rides on existing Claude for Work agreements.*
- **Pricing:** Effectively free for Janus — included with existing Claude subscriptions (Pro / Max / Team / Enterprise) during research preview; usage counts against each user's Claude allowance, no separate per-seat charge.
- **Compliance:** Inherits Claude for Work — SOC 2 Type II ✅ · ISO 27001 ✅ · GDPR ✅ · ZDR options · admin controls on Team / Enterprise. **Solid today, no net-new vendor onboarding.**
- **Differentiation:** Broader artefact range than Stitch — slide decks, PPTX, PDF, Canva exports, prototypes, and mocks. Direct Claude Code handoff (local agent or Claude Code Web). Inline canvas comments + branch versioning.
- **Strategic angle:** Composes with Janus's existing Claude stack (Janus Sandbox Claude Team, Claude Code already in Functional production). Design system not yet curated for Janus — that's the gating item before a meaningful pilot.
### Stitch vs Claude Design — point-by-point
<table header-row="true">
<tr>
<td>Dimension</td>
<td>Google Stitch (AIR-91)</td>
<td>Claude Design (AIR-80)</td>
</tr>
<tr>
<td>**Workflow**</td>
<td>Chat + infinite canvas, voice critique, parallel agent runs</td>
<td>Chat + canvas, inline comments, branch versioning</td>
</tr>
<tr>
<td>**Output**</td>
<td>High-fidelity UI flows; React code; MCP/SDK exports</td>
<td>Prototypes + slide decks + PPTX/PDF/Canva exports + Claude Code handoff</td>
</tr>
<tr>
<td>**Handoff target**</td>
<td>AI Studio · Antigravity · any MCP-compatible IDE</td>
<td>Claude Code (local or Web)</td>
</tr>
<tr>
<td>**Cost today**</td>
<td>Free (Labs)</td>
<td>Free (rides on existing Claude Team seats)</td>
</tr>
<tr>
<td>**Compliance today**</td>
<td>Labs status — no DPA, boundary unclear</td>
<td>Solid — inherits Claude for Work cert stack</td>
</tr>
<tr>
<td>**Composability**</td>
<td>Strong — open-source [DESIGN.md](http://DESIGN.md), MCP server, SDK, skills library</td>
<td>Mediumish — closed format, deep into Claude Code</td>
</tr>
<tr>
<td>**Ecosystem pull**</td>
<td>Google stack (Workspace, Gemini, Antigravity, Firebase)</td>
<td>Claude stack (Claude Team, Claude Code)</td>
</tr>
<tr>
<td>**Output range**</td>
<td>Narrower — UI/UX flows for apps and websites</td>
<td>Broader — UI + decks + prototypes + brand artefacts</td>
</tr>
<tr>
<td>**Voice / multimodal**</td>
<td>Voice mode, multimodal canvas</td>
<td>Multimodal but no voice</td>
</tr>
</table>
**Practical read:** Claude Design wins on compliance and zero-onboarding today. Stitch wins on agentic-tool composability and tighter alignment with Janus's Google footprint. Both are credible — and the *real* choice is partly downstream of the app-stage decision, since each design tool's natural handoff target points at a different builder.
---
## How to run the bakeoff
Split it into two passes — don't try to compare design tools and full-app builders in one matrix.
### Pass 1 — App-stage cohort
1. **Define one fixed Janus prompt.** Suggested baseline: *"Build an internal RFP intake form with email notifications and a basic admin view."* Useful enough that the output is judgable; small enough that token / credit burn stays bounded.
2. **Run the same prompt through all five.** Lovable, v0, Replit, Hercules, Bolt. Capture: design quality, accuracy, iteration count to working state, time-to-deployable, total credit/token spend, code structure, and where the output sits on the IT-readiness heat-map above.
3. **Single owner.** All five evaluations led by one person to keep judging consistent.
4. **Bolt prerequisite.** Bolt should not be evaluated beyond surface-level until StackBlitz answers a security questionnaire (SOC 2 status, training-opt-out, data residency, DPA availability). Otherwise we're picking based on aesthetics and the compliance gap kills it at handover.
### Pass 2 — Design-stage cohort
1. **Same fixed Janus prompt** plus a UX-design framing (e.g., *"Design the screens for the RFP intake form before we build it"*) to keep the comparison apples-to-apples.
2. **Run through Stitch and Claude Design.** Compare design quality, design-system fidelity (loading a Janus brand kit into each), handoff fidelity to the chosen Pass 1 winner, and end-to-end pipeline ergonomics.
3. **Decide independently.** The design-stage winner should be chosen on its own merits, not bundled with the app-stage decision — but a strong combination signal (e.g., Stitch + Antigravity outperforming Lovable end-to-end) is a valid input.
### Cross-cutting actions
- **Move all six new entries (AIR-87, 88, 89, 90, 91 + the existing AIR-32) to *Evaluating**\* when the bakeoff officially starts. Today five of them are in Backlog.
- **Adopt **[**DESIGN.md**](http://DESIGN.md)** as a Janus design-system handoff format** regardless of which tool wins. The format is open-source and travels — there's no lock-in cost, and it gives us a portable design-system primitive to point any of these tools at.
- **Loop in IT/ITO early** under the 2026-04-30 compliance reset. The sandbox trial is structurally a separate-company sandbox with two-step approval and a joint AIO/ITO production handover. The cohort decision should be ITO-aware from day one to avoid rework.
- **Block free / personal accounts** on `janusd.io` emails for all six tools before any rollout. Even with no-training-by-default on paid Lovable / v0 / Hercules tiers, free tiers are a data-boundary risk.
---
## Open questions to resolve before recommendation
1. Does Janus standardise on a Google-native pipeline (Stitch + Antigravity + Firebase / Google Cloud) or pick an independent best-of-breed (Lovable / v0 / Replit) for chat-to-app?
2. What's the realistic 6-month total cost across the cohort at Janus pilot scale (10 active builders, \~5 hosted apps)? Important since pricing models vary wildly — credits (Lovable, Hercules, v0), tokens (Bolt, v0), per-seat (Replit), and per-Workspace (Lovable Pro).
3. Where exactly does Stitch sit relative to Workspace's certification and DPA boundary today, and when does it exit Labs?
4. Is StackBlitz/Bolt willing to provide SOC 2 Type II attestation, ISO 27001, GDPR DPA, and a written training-opt-out — and is that *actually achievable* in the bakeoff timeline, or is Bolt effectively eliminated by compliance?
5. Does the Janus design system need to be curated / formalised before either Stitch or Claude Design can be meaningfully evaluated? (Probably yes — both tools' outputs hinge on a configured design system.)
6. Who owns the bakeoff — AI Office, ITO, or jointly per the compliance reset?
---
## Linear cross-reference
<table header-row="true">
<tr>
<td>AIR</td>
<td>Title</td>
<td>Status</td>
<td>Linear</td>
</tr>
<tr>
<td>AIR-32</td>
<td>Replit</td>
<td>Evaluating</td>
<td>[https://linear.app/janusd/issue/AIR-32/replit](https://linear.app/janusd/issue/AIR-32/replit)</td>
</tr>
<tr>
<td>AIR-80</td>
<td>Claude Design</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-80/claude-design](https://linear.app/janusd/issue/AIR-80/claude-design)</td>
</tr>
<tr>
<td>AIR-87</td>
<td>Hercules</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-87/hercules](https://linear.app/janusd/issue/AIR-87/hercules)</td>
</tr>
<tr>
<td>AIR-88</td>
<td>Lovable</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-88/lovable](https://linear.app/janusd/issue/AIR-88/lovable)</td>
</tr>
<tr>
<td>AIR-89</td>
<td>Bolt</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-89/bolt](https://linear.app/janusd/issue/AIR-89/bolt)</td>
</tr>
<tr>
<td>AIR-90</td>
<td>v0</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-90/v0](https://linear.app/janusd/issue/AIR-90/v0)</td>
</tr>
<tr>
<td>AIR-91</td>
<td>Google Stitch</td>
<td>Backlog</td>
<td>[https://linear.app/janusd/issue/AIR-91/google-stitch](https://linear.app/janusd/issue/AIR-91/google-stitch)</td>
</tr>
</table>
---
## Source references
**Vendor pages**
- Hercules: [https://hercules.app/](https://hercules.app/) · [https://hercules.app/pricing](https://hercules.app/pricing) · [https://hercules.app/docs/platform/enterprise](https://hercules.app/docs/platform/enterprise) · [https://hercules.app/docs/platform/sso-saml](https://hercules.app/docs/platform/sso-saml) · [https://hercules.app/legal/privacy](https://hercules.app/legal/privacy)
- Lovable: [https://lovable.dev/](https://lovable.dev/) · [https://lovable.dev/pricing](https://lovable.dev/pricing) · [https://lovable.dev/security](https://lovable.dev/security) · [https://lovable.dev/enterprise-landing](https://lovable.dev/enterprise-landing) · [https://trust.lovable.dev/](https://trust.lovable.dev/) · [https://lovable.dev/data-processing-agreement](https://lovable.dev/data-processing-agreement)
- Bolt: [https://bolt.new/](https://bolt.new/) · [https://bolt.new/pricing](https://bolt.new/pricing) · [https://github.com/stackblitz/bolt.new](https://github.com/stackblitz/bolt.new) · [https://stackblitz.com/privacy-policy](https://stackblitz.com/privacy-policy)
- v0: [https://v0.app/](https://v0.app/) · [https://v0.app/pricing](https://v0.app/pricing) · [https://v0.app/docs/security](https://v0.app/docs/security) · [https://security.vercel.com/](https://security.vercel.com/)
- Replit: in registry (AIR-32)
- Stitch: [https://stitch.withgoogle.com/](https://stitch.withgoogle.com/) · [https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/) · [https://stitch.withgoogle.com/docs/design-md/overview/](https://stitch.withgoogle.com/docs/design-md/overview/) · [https://stitch.withgoogle.com/docs/mcp/setup/](https://stitch.withgoogle.com/docs/mcp/setup/) · [https://github.com/google-labs-code/stitch-sdk](https://github.com/google-labs-code/stitch-sdk) · [https://github.com/google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- Claude Design: [https://claude.ai/design](https://claude.ai/design) · [https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing](https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing) · [https://support.claude.com/en/articles/14604416-get-started-with-claude-design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) · [https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans](https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans)
**Janus governance references**
- Janus AI & Automated Systems Policy — Section 5.2.1 (Tool Categorisation), 5.2.3 (Data Boundaries), 5.2.4 (Justification Protocol), 5.3.1 (Accountability), 5.4 (Violations).
- AIO ↔ ITO compliance reset, 2026-04-30 — sandbox = separate company, two-step approval, joint production handover, ISO 9001 mandatory.
