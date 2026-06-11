---
type: project
title: Janus CRM Selection
slug: janus-crm-selection
created: 2026-05-05
updated: 2026-06-11
status: active
owner: michael-bruck
captured_by: jehad-altoutou
departments: [marketing, ai-office, office-of-ceo]
sources: [2026-05-05-michael-jehad-andrew-weekly-meeting, marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting, 2026-06-10-andrew-soane-attio-demo, 2026-06-10-michael-bruck-twenty-crm-demo]
related: [crm-evaluation-and-selection, agentic-lean-marketing-stack, stack-composition-framework, janus-website-cms, marketing-prime-radiant, attio, twenty]
audience: department
---

# Janus CRM Selection

The Janus CRM platform decision. **Attio** was the leading candidate as of 2026-05-19; evaluation reopened in June 2026 with a structured 5-vendor sprint week. **[[twenty|Twenty CRM]]** emerged as a strong second contender after a June 10 demo. Decision expected week of June 16, 2026. Companion to the broader [[crm-evaluation-and-selection]] hub.

## June 2026 evaluation sprint

Week of June 9–13, 2026 — Andrew ran 5 vendor calls. One vendor dropped immediately (unnamed; described as corporate, inflexible, "their way or the highway" — likely Salesforce or HubSpot Enterprise). Four remaining:

| Vendor | Demo date | Status |
|---|---|---|
| [[attio\|Attio]] | Jun 10 (intro) + Jun 11 (full demo) | Active — top contender |
| [[twenty\|Twenty CRM]] | Jun 10 | Active — top contender |
| HubSpot | Jun 9 (referenced) | Lower-ranked per Andrew |
| Monday.com | Jun 9 (referenced) | Possible; but board-model mismatch for CRM |

**Twenty CRM signals (Jun 10 demo):** Open source, 3 years old, US company, founder Felix Malfait (prior company Kunai sold to Airbnb). Clients: Bayer (migrating from Salesforce), PwC. Fully configurable relational model; API/MCP-first; RBAC for agent scoping; Fuelty Edge for code-declared custom apps. Jehad code-reviewed it: "nicely built, well defined." Michael: "big fan of open source... more than I was expecting." Andrew: above HubSpot in ranking.

**Attio signals (Jun 10 intro + Jun 11 full demo):** Confirmed agent-native MCP design; call transcription potentially replacing Fireflies; full Janus use-case demo (Singapore white paper lead capture flow) to run Jun 11.

**Decision criteria (unchanged):** composability, agent operability, reversibility per [[stack-composition-framework]].

## Decision — Attio

**Attio** scored 3/3 on the [[stack-composition-framework]]:

- **Composability** — Relationship-graph data model with standard objects (Person, Company, Deal). MongoDB-style queries (industry-standard).
- **Agent operability** — Agent-native by design. Attio's positioning statement: *"An MCP server cannot be designed like a public API, because context windows and token costs force different primitives."* They designed the data model and MCP surface together rather than retrofitting MCP onto an existing UI-first product.
- **Reversibility** — Plain JSON / CSV export. No proprietary query language. Pricing published on the website (no "contact sales" gating) — Free tier with real features; Plus $29–36/user/month; Pro $69–86/user/month.

**Trade-offs:** Smaller integration ecosystem than HubSpot / Salesforce. Reporting is shallower than the giants. Both judged acceptable at Janus's stage.

### Linear AIR

AIR-76. Status: Backlog as of 2026-05-19 — requirements list to be prepared by Andrew, due 2026-05-26. Expected to pass formal evaluation once requirements are mapped.

## Alternatives considered

| Candidate | Score | Why not |
|---|---|---|
| **Salesforce** | 2/3 | Deepest MCP integration in the category (60+ tools, dynamic toolset loading, SOQL queries, Apex test execution). Mature CLI. **Loses on reversibility because of Apex.** Any meaningful customization accumulates non-portable Java-derived code. Viable *only* with the explicit constraint of writing zero Apex; risky once that line is crossed. |
| **HubSpot** | 2/3 | 136 MCP tools, but the official server is read-heavy — write operations require community servers with low adoption. Strong only if going all-in on the HubSpot ecosystem (CRM + Marketing Hub + CMS Hub). Standalone, weaker than Attio at Janus's stage. |
| **[[monday]]** | n/a | Has an official MCP server, but board-centric data model is not relationship-centric. Already in use for project tracking / AI Registry. Explicitly **not** being promoted to system-of-record for customer relationships. |
| **Pipedrive** | n/a | Earlier-stage candidate in the matrix analysis; not pursued after Attio surfaced as a 3/3. |

## Stakeholders

- **Decision lead:** [[michael-bruck]]
- **Requirements + operational owner:** [[andrew-soane]]
- **Approval / strategic veto:** [[bonaventure-wong]] (will see the holistic MarTech vendor assessment Michael is preparing)
- **Implementation:** [[jehad-altoutou]] + IT/DA

## Operational pattern (post-onboarding)

Singapore launch leads land in a Google Sheet workaround → migrate to Attio in the June post-launch window as seed data. Configure MCP for Claude Code so it can score, segment, and draft outreach against the CRM directly. Andrew operates campaigns through Claude Code rather than dedicated CRM UI for most workflows.

## Watch for

- Andrew's requirements list (due 2026-05-26).
- Michael's holistic MarTech vendor assessment for Bonaventure (no hard due date).
- Attio's Gate 1 outcome once requirements are submitted (expected to pass).
- Migration of Google Sheet leads into Attio after Singapore launch settles.
