---
type: project
title: CRM Evaluation & Selection
slug: crm-evaluation-and-selection
created: 2026-05-07
updated: 2026-05-19
departments: [marketing, ai-office, office-of-ceo]
status: active
owner: michael-bruck
sources: [aio-2026-05-06, andrew-marketing-discussion-tracker, automations-2882205554, 2026-05-12-bonaventure-ai-native-call, 2026-05-12-andrew-onboarding-review, jehad-vault-crm-evaluation-and-selection, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting]
related: [andrew-soane, bonaventure-wong, michael-bruck, euclid-wong, ai-tool-evaluation, 2026-05-06-monday-com-to-production-this-week, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market, janus-crm-selection, agentic-lean-marketing-stack, stack-composition-framework]
---

# CRM Evaluation & Selection

Hub for locking down Janus's CRM platform choice. High-stakes architectural commitment — the chosen CRM becomes the system-of-record hub for customer data with a 2–3 year horizon, and frames a broader SaaS rationalisation thesis (CRM-centric integration vs. point-solution sprawl).

## Candidates

| Candidate | Posture | Notes |
|---|---|---|
| HubSpot | Michael leans toward | Strong all-in-one stack; integration breadth. Dispatched to /ai-registry for Gate 1. |
| Attio | In matrix evaluation | Newer entrant; modern data model. Andrew running matrix analysis. |
| Salesforce | In matrix evaluation | Industry default; Gate 1 dispatched. Heavier deployment. |
| Pipedrive | In matrix evaluation | Lightweight; sales-pipeline focused. |

## Decision framing

Per [[2026-05-06-monday-com-to-production-this-week]]: CRM lock-in is paired with the Monday production push, while [[bonaventure-wong]] is in the room. The window is now or post-his-return — choosing now is operationally easier.

The decision is the project. Once chosen, post-selection integration work may warrant its own project hub or fold into existing departmental projects (marketing automation, recruitment pipeline, etc.) — a question to revisit at lock-in.

## Stakeholders

- **Decision lead:** [[michael-bruck]]
- **Matrix analysis:** [[andrew-soane]]
- **Approval / strategic veto:** [[bonaventure-wong]]
- **Implementation:** [[euclid-wong]] / IT (post-selection)

## Linkage to [[ai-tool-evaluation]]

CRM candidates run through the standard Gate 1 viability screen via `/ai-registry` and `/ai-tool-evaluation` skills. As of 2026-05-06, HubSpot and Salesforce are dispatched for Gate 1; Attio and Pipedrive on the matrix but not yet dispatched.

## Watch for

- HubSpot and Salesforce Gate 1 outcomes.
- Andrew's matrix analysis output.
- Lock-in window before Bonaventure's departure.
- Post-selection scope: does the chosen CRM trigger an integration project hub, or fold into existing operational work?

## Update — 2026-05-12 AI Native CEO call

Bonaventure dial-in on the 12 May call ([[2026-05-12-bonaventure-ai-native-call]]) materially reframes the CRM scope:

- **Scope skepticism — "glorified contact list" risk.** Bonaventure: *"I just keep — it comes back down to glorified contact list. Sometimes maybe we'll just add it, but we're not growing that big. Let's start with Singapore, let's see if it works. If it doesn't, can we, you know, see what are the features people use and then implement that? Because eventually, as we said, as we integrate the AI native side, we might not have all these databases."*
- **Minimum-viable Singapore-first framing.** Aligned with [[2026-05-12-singapore-as-lead-market]] — start CRM thinking inside Singapore, not as a global pre-commitment.
- **Output spec required before scoping.** Bonaventure pushed back on the framing — "what are you looking for outputs here? Contacts, name, last name. Okay. Email, telephone number... What do you want out of this?" — and wants [[andrew-soane|Andrew]] to articulate the outputs before locking in a vendor. Bonaventure's read: Andrew has said *tracking* and *capturing*, but not what he's tracking or to what end.
- **Marketing-CRM vs sales-CRM distinction surfaced.** Michael flagged the possibility that what Andrew needs is a *marketing-campaign-management system* rather than a sales-pipeline CRM. Worth disambiguating before benchmarking continues.
- **Contact-capture mechanism is the bottleneck, not the CRM.** Bonaventure: "we have to have some kind of process of everyone... how do we capture content? Not through a physical card." Tangent emerged around LinkedIn / NFC cards / Obsidian-mobile-app for WhatsApp contact capture. Janus company cards / NFC fobs / keychains all surfaced as candidates. Worth a separate small project hub if it persists. **Provisional convention:** LinkedIn as the primary contact-capture surface; NFC cards / keychains evaluated as physical-tap supplement.
- **AI-native displaces CRM in the long run.** Bonaventure: "as we integrate the AI native side, we might not have all these databases." Frames the CRM decision as bridging not terminal.
- **Re-stated as not in critical path.** Michael on the call: "I'm not putting the CRM in the critical path here. Let's start without it." This is now triple-reinforced (5 May, 6 May, 12 May).

## Update — 2026-05-12 Andrew onboarding review (timing committed)

Per [[2026-05-12-andrew-onboarding-review]] (3pm Andrew session), CRM timing is now concretely scoped:

- **Decision target: ~2–3 weeks** (end-May / first-week-June) to a HubSpot recommendation that Bonaventure agrees with.
- **Implementation runway: ~3 more weeks** for SaaS terms negotiation + setup. Michael's view: should be shorter at our seat count (1–3 users initially) — limited negotiating leverage but also limited deal complexity.
- **Total runway:** ~mid-June for live implementation if HubSpot is the chosen vendor.
- **External pressure point:** the HubSpot rep ("Tony") has been pinging Janus on the deal staleness; not material to our decision pace but a signal that the vendor sees the deal as a near-term close.

**Interim system-of-record for Singapore launch:** Google Sheets, populated via a registration form on the new Singapore landing page. Form → Sheets → manual review → invitation list for the 8th–9th July luncheon. Once the CRM lands, the Sheets data backfills into the CRM and the funnel becomes automatic.

**Marketing-CRM vs sales-CRM:** confirmed Marketing needs the marketing-campaign-management capabilities (email sequences, lead nurture, campaign analytics), not just sales pipeline tracking. This affects which HubSpot edition / which alternative makes sense — Andrew to weigh in on feature priority before the final recommendation.

## Update — 2026-05-19 stack analysis flips recommendation to Attio

Per the [[marketing-stack-technical-writeup]] (Michael → Jehad, 2026-05-19) and the [[2026-05-19-aio-mktg-meeting]] (Michael × Andrew), the CRM recommendation has flipped from **HubSpot-leaning** to **Attio**. The flip is grounded in the new [[stack-composition-framework]] (three lenses: composability, agent operability, reversibility), proposed as a pre-G1 filter to [[ai-tool-evaluation-framework]]:

| Candidate | Score | Verdict |
|---|---|---|
| **Attio** | 3/3 | **Recommended.** Agent-native by design; relationship-graph data model; MongoDB-style queries; published pricing; plain-JSON / CSV export. AIR-76. |
| Salesforce | 2/3 | Viable *only* with zero-Apex constraint — loses on reversibility once any meaningful customization accumulates. |
| HubSpot | 2/3 | Bundling play only — strong if going all-in on HubSpot CRM + Marketing Hub + CMS Hub. Standalone weaker than Attio at Janus's stage. Official MCP server is read-heavy. |
| [[monday]] | n/a | Board-centric data model is not relationship-centric. **Explicitly not** being promoted to CRM. |

**Current status (2026-05-19):** Andrew confirmed direction on Attio. Requirements list due 2026-05-26. Attio expected to pass formal evaluation once requirements are mapped. Michael preparing a holistic MarTech vendor assessment for [[bonaventure-wong]] (no hard due date) — this is the document that will formally re-pitch the CRM call to leadership.

The dedicated [[janus-crm-selection]] project hub captures the operational detail of the Attio implementation; this hub remains the evaluation-history record for how Janus got from HubSpot-leaning → Attio.
