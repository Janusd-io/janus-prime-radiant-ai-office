---
type: source
source_type: meeting
title: AIO, Marketing Meeting 19 May 2026
slug: 2026-05-19-aio-mktg-meeting
created: 2026-05-19
captured_by: jehad-altoutou
fireflies_id: 01KRZTZDE9GZR83M4MMTMJ62BV
fireflies_url: https://app.fireflies.ai/view/01KRZTZDE9GZR83M4MMTMJ62BV
attendees: [Michael Bruck, Andrew Soane]
duration_min: 54
audience: department
departments: [ai-office, marketing]
standup_skill_version: v3.21
parser_version: 3
related: [2926686817, 2926686914, 2926631478, 2926634971, 2926635333, 2926631656, 2926648775, 2926649128, 2926633922, 2882205554, 2892863693, 2918212263, 2917860817, AIR-76, AIR-111, AIR-113, AIR-116, AIR-117, AIR-118, AIR-121, AIR-122, AIR-123, AIR-124, AIR-125, AIR-126]
---

# AIO, Marketing Meeting 19 May 2026

**Attendees:** Michael Bruck, Andrew Soane
**Duration:** ~54 min
**Source:** [Fireflies](https://app.fireflies.ai/view/01KRZTZDE9GZR83M4MMTMJ62BV)

---

## Key Decisions

### Marketing tech stack — detailed requirements review

Meeting focused on the operational requirements behind the already-approved marketing stack. Key clarifications:

- **Cosmic CMS (AIR-117)** — confirmed direction; requirements list to be prepared by Andrew (due 2026-05-26). No CMS needed for the initial site launch; Cosmic onboarding in a subsequent phase.
- **Vercel (AIR-113)** — confirmed; DA (IT) to assist with setup. Jehad to coordinate (due 2026-05-26).
- **Cloudflare (AIR-116)** — confirmed; Andrew noted DA is already familiar, reducing onboarding friction. Jehad to coordinate with DA/IT (due 2026-05-26).
- **Attio (AIR-76)** — requirements list to be prepared by Andrew (due 2026-05-26); expected to pass formal evaluation once mapped.
- **Resend (AIR-118)** — confirmed for transactional email. Relationship to MailChimp clarified: Resend = programmatic/transactional; MailChimp = broadcast/campaigns. Complementary if both adopted.
- **Google Analytics (AIR-125)** — confirmed as analytics layer for the marketing site.
- **Cookiebot (AIR-124)** — named as the specific cookie compliance vendor. Legal pre-launch requirement. Andrew to procure by 2026-06-02.

### MailChimp status — hold open

MailChimp (AIR-111) was kept open rather than rejected. Andrew has not yet decided whether to adopt it for the broadcast/campaign email layer. Status reverted from Rejected → Backlog pending Andrew's decision.

### Adobe Experience Manager — explicitly rejected

AEM (AIR-121) explicitly called out by Michael as a "legacy system" — not suitable for Janus's current scale. Consistent with all enterprise CMS rejections from this evaluation cycle (Contentful, Sanity, Storyblok, Storyblok).

### Holistic Martech vendor assessment for Bonaventure

Michael to prepare a full Martech vendor comparison document for Bonaventure (no hard due date). Covers the full stack rationale to enable leadership sign-off.

### Singapore campaign — site readiness dependency

Site needs to be live and compliant (cookie banner, privacy policy) before the Singapore campaign goes live. Hard constraints:
- Cookie compliance (Cookiebot) — Andrew to procure by 2026-06-02
- Privacy policy — Andrew to draft and publish by 2026-06-02

### Martech landscape analysis — expand scope

Michael to expand the Martech analysis beyond the tools directly in scope (due 2026-05-26). Includes brand agency tools (deferred — no specific tool named yet) and B2B intent tools (Mombara, AIR-123; LinkedIn Sales Navigator, AIR-126 — both year 2/3 considerations).

---

## Action Items

- Prepare CMS requirements list (Andrew, due 2026-05-26)
- Prepare email marketing requirements list (Andrew, due 2026-05-26)
- Procure Cookiebot (Andrew, due 2026-06-02)
- Privacy policy go-live (Andrew, due 2026-06-02)
- Coordinate Cloudflare + Vercel setup with DA/IT (Jehad, due 2026-05-26)
- Expand Martech analysis scope (Michael, due 2026-05-26)
- Prepare holistic Martech vendor assessment for Bonaventure (Michael)
- Share Claude HTML deck skill with Andrew (Michael, today)

---

## Registry Dispatch Summary

6 new AIR entries created from this meeting:

**New entries created:**
AIR-121 (Adobe Experience Manager, Rejected), AIR-122 (Payload CMS, Backlog), AIR-123 (Mombara, Backlog), AIR-124 (Cookiebot, Backlog/High), AIR-125 (Google Analytics, Production), AIR-126 (LinkedIn Sales Navigator, Backlog)

**Status changes:**
AIR-111 (MailChimp) — Rejected → Backlog (hold open per Andrew)

**Comments added to existing entries:**
AIR-113 (Vercel — IT coordination context), AIR-116 (Cloudflare — DA familiarity, IT coordination), AIR-117 (Cosmic CMS — requirements list + no CMS for initial launch), AIR-76 (Attio — requirements list agreed, expected to pass), AIR-118 (Resend — transactional vs broadcast boundary with MailChimp)

---

## Monday Coverage

**Context Coverage Invariant: PASS** — all 13 touched items carry `<h2>Description (from meeting notes)</h2>` blocks.

New parent + sub-items (Step 3G): 2926686817 + 2926686914, 2926631478, 2926634971, 2926635333, 2926631656, 2926648775, 2926649128, 2926633922

Existing source-bumped items (Step 3H, 0 backfills needed — all already covered): 2882205554, 2892863693, 2918212263, 2917860817
