---
type: source
source_type: meeting
title: "AI Native CEO — 18 May 2026"
slug: 2026-05-18-ai-native-ceo
created: 2026-05-18
captured_by: jehad-altoutou
fireflies_id: 01KRA6FQZ2WEX5WJ3EX1W3E3G8
fireflies_url: https://app.fireflies.ai/view/AI-Native-CEO::01KRA6FQZ2WEX5WJ3EX1W3E3G8
attendees: [michael-bruck, jehad-altoutou, bonaventure-wong, joyce-woo]
duration_min: 60
audience: department
departments: [ai-office, office-of-ceo]
countries: [sg, ae]
standup_skill_version: v3.17
privacy: public
related: [janus-prime-radiant-build, nanoclaw, notion, 2026-05-18-ceo-global-kb-unified-market-ui, 2026-05-18-nanoclaw-as-personal-ai-coa-candidate, 2026-05-18-website-react-typescript-full-rebuild]
---

# AI Native CEO — 18 May 2026

**Attendees:** Michael Bruck, Jehad Altoutou, Bonaventure Wong, Joyce Woo (Singapore)
**Duration:** ~60 min | **Fireflies:** [01KRA6FQZ2WEX5WJ3EX1W3E3G8](https://app.fireflies.ai/view/AI-Native-CEO::01KRA6FQZ2WEX5WJ3EX1W3E3G8)

*Note: Morning AIO standup skipped (company town hall). This CEO meeting replaces it as the primary knowledge-capture surface for the day.*

---

## Clean Meeting Summary

Wide-ranging CEO session covering Prime Radiant architecture, Andrew onboarding, website scope, ISO facilitation skill, Notion deprecation, Slack bot sprawl, NanoClaw evaluation, Joyce Singapore rollout, and CEO-level direction on the global knowledge base strategy.

**Prime Radiant demo landed well.** Jehad demo'd to Bonaventure and Joyce: entity nodes auto-sourced from Joyce's white paper, Obsidian graph view, HTML deck generated from the system with interim Janus brand CSS. Both received it positively. GitHub sync confirmed as the canonical vault backend — Google Shared Drive ruled out definitively (streaming service incompatible with Claude Code's local-file requirement).

**Andrew Prime Radiant initialisation today/tomorrow.** Bulk Fireflies import + Markdown doc import as the primary first-content seed mechanism.

**Website scope expanded.** What was scoped as a landing-page build is now a full React/TypeScript rebuild. GDPR consent popup and Mailchimp integration required for Singapore campaign compliance.

**ISO facilitation skill nearing completion.** Joyce is awaiting Simon Tarskih's sign-off before company-wide distribution.

**Notion deprecation confirmed end-May.** Feeds straight to Prime Radiant, one fewer tool in the stack.

**Slack bot sprawl raised by Bonaventure.** Multiple bots per person (Slack-side clutter). Proposed resolution: one bot per person as a personal AI chief-of-staff. NanoClaw identified as the technical candidate — open-source, self-hosted, Docker container isolation per agent, native Slack Socket Mode. AIR-103 created in Linear; Gate 1 PASS on all five criteria. Status: Evaluating.

**Joyce queued for Prime Radiant rollout.** A separate demo session to be scheduled.

**CEO direction on global knowledge base.** Bonaventure: one unified global knowledge base, market-specific UI layer, open access. Cross-department connectivity is the goal. Singapore two-layer model: read access to global KB + local vault feeding back upward. Obsidian's single-repo limitation blocks cross-department connectivity at scale — deferred as a known constraint.

---

## Decisions Made

| Decision | Owner | Rationale |
|---|---|---|
| GitHub sync as canonical vault backend (confirmed CEO-level) | Jehad | Streaming service incompatibility with Claude Code; confirmed in demo to Bonaventure + Joyce |
| Global KB = one unified base, market-specific UI layer | Bonaventure | CEO direction; cross-department connectivity is the design target |
| Singapore two-layer model: read-access to global + local vault feeds back | Bonaventure | Balances global coherence with SG localisation |
| NanoClaw as Slack bot sprawl solution candidate | Joint | Self-hosted, Docker isolation, native Slack Socket Mode; AIR-103 Evaluating |
| Website scope: full React/TypeScript rebuild (not just landing page) | Joint | GDPR consent + Mailchimp integration required for SG campaign compliance |
| Notion deprecation confirmed end-May | Joint | Feeds straight to Prime Radiant; one fewer tool |

---

## Next Steps

### 🎯 Near-term
- Andrew Prime Radiant initialisation via bulk Fireflies + Markdown import (2891609467)
- Website full React/TypeScript rebuild with GDPR popup + Mailchimp (2917841885)
- ISO facilitation skill: Joyce awaiting Simon sign-off (2889155963)
- Schedule separate Prime Radiant demo session for Joyce (2917860605)

### 📅 This week
- NanoClaw Stage 2 Technical Qualification — AIR-103 (following Gate 1 PASS)
- Notion deprecation cutover preparation (2882088507)

### 🏔️ Longer horizon
- Global KB unified architecture: cross-department federation design
- Obsidian single-repo limitation resolution (deferred)
- Joyce Singapore Prime Radiant rollout (after demo session)

---

## Monday Items Touched

| Item | ID | Action | Description Update |
|---|---|---|---|
| Prime Radiant hub | 2900825519 | Source bump | ✅ 577181986 |
| Andrew rollout | 2891609467 | Source bump + sub-items | ✅ 577182033 |
| Joyce / Singapore | 2917860605 | Source bump + sub-items | ✅ 577182080 |
| ISO facilitation skill | 2889155963 | Source bump + sub-items | ✅ 577182117 |
| Website rebuild | 2917841885 | Source bump + sub-items | ✅ 577182160 |
| Notion restructure | 2882088507 | Source bump + sub-items | ✅ 577182209 |
| Nomi AI | 2882088496 | Source bump | ✅ 577182262 |
| Data architecture | 2882208018 | Source bump + sub-items | ✅ 577182359 |

**Sub-items created (10):** 2923828783, 2923758997, 2923824262, 2923819639, 2923820069, 2923830615, 2923830420, 2923828482, 2923759293, 2923830605

**Context coverage: 8/8 ✅**

---

## Linear AIP Reconciliation

| AIP | Linear | Monday | Action |
|---|---|---|---|
| AIP-21 | Done (2026-04-24) | In Testing (Assessify HR) | ⚠️ 12th consecutive unresolved conflict. No transcript authority to resolve. Manual Linear closure required — close AIP-21, note AIP-23 as live successor. |

---

## AI Registry / Evaluation Outcomes

- **AIR-103 NanoClaw created and Gate 1 assessed.** Classification: Infrastructure. Gate 1: ✅ PASS (all 5 criteria). Status: Evaluating. Gate 1 comment posted to Linear (comment ID: ed1658cc-4571-4a21-b5e2-f27d479f2005). See [[nanoclaw]] vendor entity.
