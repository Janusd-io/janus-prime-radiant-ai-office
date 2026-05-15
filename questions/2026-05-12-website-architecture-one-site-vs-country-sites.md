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
sources: [2026-05-12-andrew-onboarding-review, 2026-05-15-singapore-marketing-launch-plan-v1]
related: [andrew-soane, bonaventure-wong, michael-bruck, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market]
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
