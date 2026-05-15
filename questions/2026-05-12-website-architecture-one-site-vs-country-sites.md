---
type: question
title: One Janus website with country sub-paths, or standalone country websites?
slug: 2026-05-12-website-architecture-one-site-vs-country-sites
created: 2026-05-12
updated: 2026-05-15
departments: [marketing, ai-office, office-of-ceo]
countries: [sg, gb]
owner: andrew-soane
status: active
sources: [2026-05-12-andrew-onboarding-review, 2026-05-15-singapore-marketing-launch-plan-v1, 2026-05-14-janus-singapore-white-paper-storms-ahead]
related: [andrew-soane, bonaventure-wong, michael-bruck, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market, 2026-05-14-janus-singapore-white-paper-storms-ahead, joyce-woo, ingest-2026-05-15-joyce-woo]
---

# Website architecture — one Janus site with country sub-paths, or standalone country websites?

Open question because Andrew anticipates a "mighty battle" with Bonaventure on this. Both positions have advocates within Janus; the decision is sequenced ahead of the Singapore launch landing-page work (single page needed in *days* per the [[2026-05-12-singapore-as-lead-market|Singapore lead-market decision]]).

## The two positions

### Position A — One Janus website with country sub-paths *(Andrew, Michael)*

`janusd.com` as the canonical site, with `janusd.com/sg`, `janusd.com/gb`, etc. as country sub-paths driven by CMS-driven localisation. Vanity URLs like `janusd-sg.com` can redirect to the canonical sub-path and still appear on Singapore-collateral / email signatures.

Andrew on the call (12 May):

> "I'm going to have a bit of a mighty battle with Bonaventure because he's going to want to build standalone dedicated web page websites for every country. And I just think that's a fool's economy. I think we have a standard `janusd.com`. Yes, we can buy URLs that will point to a — like the SG should point to a Singapore set of pages. But actually all it's really pointing to is `janusd.com/Singapore`."

Michael:

> "It's like when you go to the Apple site... you choose the country and language and the CMS will do what it needs to do. Every global brand, every company. Where he's coming from — I understand he wants to really emphasise that as a Singaporean company. Like IP addresses, you can still redirect."

**Advantages:** single CMS / asset library / nav / brand guidelines; cheap to maintain; supports multilingual roll-out cleanly when other countries open; matches what every global brand (Apple, etc.) does.

### Position B — Standalone country sites *(anticipated Bonaventure view)*

Distinct domains like `janusd-sg.com` / `janusd-uk.com` each as their own site. Reinforces country-specific branding (e.g. emphasising Janus is a Singaporean company in the Singapore market).

**Advantages:** strong country-of-origin branding; IP-address / hosting can be country-local; perceived sovereignty for in-country audiences.

## Why this needs to resolve before the Singapore launch

Andrew is committed to producing a single landing page on `janusd.com` or `janusd-sg.com` (the form here matters) in the next few days to drive the Singapore launch campaign (8th–9th July luncheon, multiple white-paper promotions, paid + organic social + PR). Whatever architecture is chosen, the first landing page sets the precedent.

## CMS implications

Position A presupposes a CMS that supports country-aware localisation. Andrew flagged he'd "really like to have a CMS in place" — the current Janus website does not run on a CMS with a proper style sheet (Michael confirmed). The CMS choice is therefore a downstream question: candidates floated were [[wix|Wix]] ("apparently the largest CMS by number of websites hosted"), Firebase, or building on a custom backend. Multilingual capability is a hard requirement.

Position B sidesteps the CMS-investment question short-term (each standalone site can be its own thing) but compounds the maintenance cost as countries grow.

## What we need from Bonaventure

A direct yes/no on the architectural principle:

- "Singapore (and future countries) live under one Janus site with country sub-paths" — Andrew's recommended path.
- "Each country gets its own standalone website" — would change the launch-page approach and the CMS roadmap.

Once resolved, the CMS-selection question (Wix / Firebase / build) can be scoped as a sub-project under [[marketing-prime-radiant]] or fold into a new project hub depending on size.

## Recommendation

**Position A** — one Janus site with country sub-paths, multilingual-ready CMS, vanity URLs as redirects. Janus presenting as Singaporean is achievable via the vanity-URL + email-signature route without fragmenting the asset library and brand guidelines.

Awaiting Bonaventure alignment. Andrew owns the conversation.

## Status update (2026-05-15) — campaign plan v1 assumes both URLs in use

The [[2026-05-15-singapore-marketing-launch-plan-v1|Singapore campaign plan v1]] (Andrew, 15 May 2026) lists *both* `janusd.com` and `janusdg.com` as campaign landing-page targets in week-1 of the timeline. Reads as if Andrew is operationally proceeding on a hybrid: `janusd.com` as the canonical site + `janusdg.com` as the SG vanity / redirect-friendly variant. This may be:

1. A pre-decision position — Andrew building for both URLs because the architecture question is still unresolved, hedging until the alignment conversation lands.
2. An implicit resolution — both URLs in use simultaneously, with `janusdg.com` redirecting / proxying to a `janusd.com/sg` country sub-path. This is roughly Position A with a vanity-URL on top.
3. A partial-resolution — Andrew has gone ahead with Position A's spirit (one canonical site + vanity URL) without explicitly resolving with Bonaventure.

Worth confirming with Andrew which reading is correct, and either closing this question with the v1-as-resolution or surfacing the gap to Bonaventure before the campaign goes live (week-1 build is in flight).

## Status update (2026-05-15) — a third URL surfaces in the Janus Singapore white paper

The [[2026-05-14-janus-singapore-white-paper-storms-ahead|Janus Singapore white paper]] (co-authored Bonaventure + Joyce Woo, PDF metadata 14 May 2026) uses `janusd.sg` as the operational identity for Janus Digital Singapore Pte. Ltd.:

- Contact: `engage@janusd.sg`
- Website: `janusd.sg`

Neither `janusd.com` (Andrew + Michael's canonical-site position) nor `janusdg.com` (the SG vanity URL in the campaign plan v1) appears in the white paper. The paper is signed by **the SG entity** (Janus Digital Singapore Pte. Ltd.) with the **UAE parent** (Janus Digital Global FZE) named alongside.

### Three URLs in play

| URL | Where it appears | Role |
|---|---|---|
| `janusd.com` | Position A (Andrew + Michael), v1 campaign plan landing page | Proposed canonical global site |
| `janusdg.com` | v1 campaign plan landing page | SG vanity / standalone-site-style URL |
| `janusd.sg` | Janus Singapore white paper contact + website | SG entity operational identity |

### What this changes

This nudges the question toward a **hybrid-resolution** reading (#2 in the previous status update): canonical `janusd.com` + SG vanity URL where the SG vanity is `janusd.sg` (the formal SG-entity domain) rather than `janusdg.com`. The `janusdg.com` URL may be a placeholder, a paid-media-friendly variant, or a planning-stage artefact that the white paper supersedes.

Either way: the white paper is the **most authoritative existing public surface** for Janus's Singapore identity (CEO-and-SG-CEO-co-signed), so its URL choice carries weight. If the campaign plan v1's `janusdg.com` was a draft and `janusd.sg` is the locked SG vanity, the open question simplifies considerably:

- Position A confirmed (canonical `janusd.com`) + SG vanity `janusd.sg` redirecting to `janusd.com/sg`.
- `janusdg.com` retired or quietly redirected.

Worth confirming with Andrew + Bonaventure as a same-conversation decision rather than waiting for the architectural alignment to resolve in isolation. The campaign goes live in week 1 (this week); URL choices ship with the first landing page.
