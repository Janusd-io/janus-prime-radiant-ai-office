---
type: source
source_type: meeting
title: AIO Standup 19 May 2026
slug: 2026-05-19-aio-standup
created: 2026-05-19
captured_by: jehad-altoutou
fireflies_id: 01KRZBX4QKXEEH8ZW600NMQ5B6
fireflies_url: https://app.fireflies.ai/view/01KRZBX4QKXEEH8ZW600NMQ5B6
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 56
audience: department
departments: [ai-office]
standup_skill_version: v3.21
parser_version: 3
related: [2925642613, 2925647238, 2925644294, 2925642425, 2925640113, 2925644383, 2925644438, 2925638351, 2925646633, 2925647447, 2882088496, 2891609467, 2882206428, 2882205554, 2918212263, 2892863693, 2918207019, 2917860817, 2900825519, 2917841885, 2924305391, 2917843553, AIR-76, AIR-77, AIR-79, AIR-93, AIR-103, AIR-109, AIR-110, AIR-111, AIR-112, AIR-113, AIR-114, AIR-115, AIR-116, AIR-117, AIR-118, AIR-119, AIR-120, AIP-24]
---

# AIO Standup 19 May 2026

**Attendees:** Michael Bruck, Jehad Altoutou
**Duration:** ~56 min
**Source:** [Fireflies](https://app.fireflies.ai/view/01KRZBX4QKXEEH8ZW600NMQ5B6)

---

## Key Decisions

### Marketing tech stack approved

Final stack selected for the Janus marketing site:

- **Cosmic CMS** (AIR-117) — headless CMS layer; AI-native agents, simpler than alternatives, cost-appropriate
- **Vercel** (AIR-113) — deployment / hosting; native Next.js support
- **Cloudflare** (AIR-116) — CDN + edge + security / DDoS protection
- **Attio** (AIR-76) — CRM; confirmed as direction; agent-first architecture; enterprise CRMs rejected
- **Resend** (AIR-118) — transactional email API
- **Google Sheets** (AIR-108) — interim lead capture (bridging until full CRM integration)

Enterprise alternatives formally evaluated and rejected: Salesforce (AIR-93), HubSpot (AIR-77), Mailchimp (AIR-111), Contentful (AIR-112), Sanity (AIR-114), Storyblok (AIR-115). Rejection rationale: all require 15–20 headcount to operate effectively; over-complex for current scale; pricing cliffs at meaningful feature tiers.

Monday item: 2925642613 (parent), sub-items 2925647238, 2925644294, 2925642425, 2925640113, 2925644383, 2925644438, 2925638351, 2925646633, 2925647447.

### New AI tool evaluation criteria

Three new criteria to be added to the `/ai-tool-evaluation` skill's gate framework:

1. **Composability** — does the tool expose APIs / webhooks / MCP hooks that allow it to be wired into automated workflows?
2. **Agent-operability** — can an AI agent operate the tool programmatically (read + write), or is it human-UI-only?
3. **Reversibility** — how hard is it to migrate away? Data portability, export formats, lock-in risk.

These criteria emerged from the marketing stack evaluation — Attio scored high on all three; Salesforce/HubSpot scored low.

### Voice recognition / speaker ID pipeline — new AIP project

Architecture approved for future build (queued post-current active projects):

```
Fireflies webhook (on transcript ready)
  → archive raw audio
  → Whisper large-v3 (self-hosted GPU)
  → diarization (pyannote.audio or AssemblyAI)
  → speaker matching (voice profile store)
  → enriched transcript → Prime Radiant ingest
```

Linear: AIP-24 (Backlog, Medium priority). Related registry entry: AIR-119 (OpenAI Whisper).

Motivation: Fireflies speaker attribution is calendar-metadata-based, not audio-based — frequently wrong. Standup skill v3.21 suppresses speaker names in brain outputs as a result. Accurate diarization unblocks re-enabling speaker attribution in Prime Radiant content.

### Speaker attribution suppression in CLAUDE.md

Agreed: stop surfacing potentially-wrong speaker names in brain/standup outputs until the voice recognition pipeline (AIP-24) is built and validated. CLAUDE.md should be updated to reflect this as an explicit policy. Prevents misleading attribution propagating into decisions and lessons.

### Nanoclaw as personal brain front-end

Nanoclaw (AIR-103, GitHub, lightweight personal AI brain framework by Wix co-founder) proposed as a personal brain front-end sitting in front of the department Prime Radiant. Concept: lightweight personal-context layer that augments the departmental institutional KB rather than replacing it. Gate 1 PASS was recorded on 18 May; evaluation continues.

---

## Action Items

- Update `/ai-tool-evaluation` skill with three new criteria: composability, agent-operability, reversibility
- Update CLAUDE.md speaker attribution suppression policy
- AIP-24: voice recognition pipeline — design phase to begin post-current sprint
- Confirm AIR-93 (Salesforce) and AIR-77 (HubSpot) status update to Rejected — currently still Evaluating; awaiting Michael's confirmation

---

## Registry Dispatch Summary

18 tools dispatched to Linear AIR from this standup:

**New entries created:**
AIR-109 (GitHub, Production), AIR-110 (Nomi, Backlog), AIR-111 (Mailchimp, Rejected), AIR-112 (Contentful, Rejected), AIR-113 (Vercel, Backlog), AIR-114 (Sanity, Rejected), AIR-115 (Storyblok, Rejected), AIR-116 (Cloudflare, Backlog), AIR-117 (Cosmic CMS, Backlog), AIR-118 (Resend, Backlog), AIR-119 (OpenAI Whisper, Backlog), AIR-120 (n8n, Backlog)

**Comments added to existing entries:**
AIR-103 (Nanoclaw — personal brain front-end use case), AIR-76 (Attio — confirmed CRM direction), AIR-79 (Hostinger — marketing site hosting context), AIR-93 (Salesforce — rejected for marketing stack), AIR-77 (HubSpot — rejected for marketing stack)

**Skipped (already Production / no new signal):** Fireflies, Gemini (AIR-5), Microsoft Clarity, Airwall X, Google Sheets (AIR-108 created 18 May). Next.js skipped — framework, not SaaS.

---

## Monday Coverage

**Context Coverage Invariant: PASS** — all 21 touched items carry `<h2>Description (from meeting notes)</h2>` blocks.

New parent + sub-items (Step 3G): 2925642613 + 2925647238, 2925644294, 2925642425, 2925640113, 2925644383, 2925644438, 2925638351, 2925646633, 2925647447

Existing source-bumped items (Step 3H, 0 backfills needed — all already covered): 2882088496, 2891609467, 2882206428, 2882205554, 2918212263, 2892863693, 2918207019, 2917860817, 2900825519, 2917841885, 2924305391, 2917843553
