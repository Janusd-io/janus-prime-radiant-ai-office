---
type: decision
title: "Website scope expanded: full React/TypeScript rebuild with GDPR consent and Mailchimp integration"
slug: 2026-05-18-website-react-typescript-full-rebuild
created: 2026-05-18
updated: 2026-05-18
status: active
departments: [ai-office, office-of-ceo]
countries: [sg, ae, gb]
owner: michael-bruck
decided_by: bonaventure-wong
captured_by: jehad-altoutou
sources: [2026-05-18-ai-native-ceo]
related: [2026-05-12-singapore-as-lead-market, andrew-soane, joyce-woo]
---

# Website scope expanded: full React/TypeScript rebuild with GDPR consent and Mailchimp integration

**Date:** 18 May 2026
**Source:** AI Native CEO meeting ([[2026-05-18-ai-native-ceo]])
**Decided by:** Joint (Bonaventure Wong, AI Office team)

---

## Decision

What was originally scoped as a **landing-page build** has been expanded to a **full React/TypeScript rebuild** of the Janus website.

Two mandatory requirements added:

1. **GDPR consent popup** — required for Singapore campaign compliance.
2. **Mailchimp integration** — required for email capture as part of the Singapore launch campaign.

Monday tracking item: 2917841885.

---

## Context

The Singapore campaign plan v1 ([[2026-05-15-singapore-marketing-launch-plan-v1]]) created a hard dependency — the website must support email capture and comply with data-consent regulations before the campaign goes live. This scope expansion was surfaced and confirmed in the 18 May 2026 CEO meeting.

The Mailchimp integration is required to feed leads generated from the Singapore campaign into the email marketing workflow; the GDPR/PDPA consent popup is required to make that capture legally compliant.

---

## Implications

- The build is now a full React/TypeScript project, not a lightweight landing-page iteration. Engineering scope increased accordingly.
- GDPR/PDPA consent is a blocker for any email-capture-dependent campaign activation.
- Mailchimp integration must be in place before the 9-week campaign clock (week commencing 11 May → 8/9 July luncheon) reaches the email-outreach phase.
- [[andrew-soane|Andrew's]] campaign timeline depends on the website being ready; this is a critical dependency.
