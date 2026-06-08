---
type: source
source_type: meeting
title: AIO CEO Meeting 8 Jun 2026
slug: 2026-06-08-aio-ceo-meeting
created: 2026-06-08
updated: 2026-06-08
captured_by: jehad-altoutou
fireflies_id: 01KTK5SYNS1YGZ4FAZR4EFK7NF
fireflies_url: https://app.fireflies.ai/view/01KTK5SYNS1YGZ4FAZR4EFK7NF
attendees: [Michael Bruck, Bonaventure Wong, Jehad Altoutou]
duration_min: 54
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2900825519, 2924305391, 2976752077, 2976746728, 2976735394, 2976744834, fireflies, obsidian, google-calendar-mcp, gmail-mcp, bonaventure-wong, michael-bruck, jehad-altoutou]
---

# AIO CEO Meeting — 8 Jun 2026

54-minute meeting. Attendees: Michael Bruck, Bonaventure Wong, Jehad Altoutou. Source: [Fireflies](https://app.fireflies.ai/view/01KTK5SYNS1YGZ4FAZR4EFK7NF).

---

## Clean Meeting Summary

The meeting covered seven threads: (1) Fireflies Android performance, (2) Cowork vs Code explained, (3) Google Calendar and Gmail MCP demonstration, (4) Bonaventure's Prime Radiant enrollment and knowledge graph, (5) Keppel BIM certification strategy, (6) ARM secure enclave concept for sensor data provenance, and (7) Jane bot blocker.

**Fireflies Android performance.** Bonaventure observed that the Fireflies app on Android loads significantly more slowly than on iOS (which opens instantly). Jehad to investigate with Andre — check device class, app version, or account configuration. A Monday sub-item was created. Finding logged in AIR-9.

**Cowork vs Code.** Jehad explained the distinction to Bonaventure: Cowork is sandboxed (safe, isolated, no full computer access), Code is production (full access, more powerful). "Cowork is sandbox, Code is production."

**Google Calendar and Gmail MCP.** Jehad demonstrated the Google Calendar MCP connector: respond-to-event (notifying a meeting organizer when the user can't attend a meeting they can't directly edit), analyze-availability (reading team schedules), and schedule-meetings. Gmail MCP was mentioned for sending the reschedule email. Both tools filed in AIR (AIR-156, AIR-155). Open question: data passing through Claude context window and Section 5.2.3 boundaries — IT/Ops and AI Policy to confirm.

**Bonaventure Prime Radiant enrollment.** Bonaventure has been autonomously enrolled on a 7-day rolling window. He is browsing his knowledge graph. Obsidian mobile requires a paid Sync subscription; Android lacks Web Clipper and Graph View. Items tracked.

**Keppel BIM certification.** External teams deliver BIM files; Janus certifies them. First certification module for Keppel is a key deliverable. Data provenance is critical — future vision includes IoT devices "pre-baked as Genus compatible." AIO to align on what is needed before contract.

**ARM secure enclave concept.** Michael's strategic idea: use ARM chip secure enclaves to create tamper-proof hardware signatures for IoT sensors, ensuring data provenance can't be tampered with even at the hardware level. This could be foundational for the Keppel data provenance use case. Bonaventure to raise with Alexander at ARM tomorrow.

**Jane bot blocker.** Jane (formerly "Nomi") is the AIO-built leave-application bot. Andre took it down after a miscommunication with Euclid about deployment/ownership. The bot needs a handover guide so another team (Euclid/HR) can own it going forward. AIO deliverable: one-pager installation and configuration guide. Bonaventure to push Euclid on timeline.

---

## Decisions

- Prepare Jane bot installation and configuration guide for handover to receiving team (AIO deliverable).
- Bonaventure to raise ARM secure enclave concept with Alexander at ARM (tomorrow).
- BIM certification for Keppel is a priority deliverable; align scope before contract.

---

## Next Steps

### Today / By Next Standup
- [ ] Test Fireflies Android performance with Andre → [[2976746728]]
- [ ] Document Obsidian Sync mobile setup for Bonaventure (paid subscription, Android limitations) → [[2976735394]]
- [ ] Prepare one-pager installation and configuration guide for Jane bot → [[2976744834]]

### External / Other-Department (no Monday items — not AIO-owned)
- Bonaventure: Raise ARM secure enclave concept with Alexander at ARM (tomorrow)
- Bonaventure: Push Euclid on Jane bot handover timeline
- Bonaventure + Rosa: Align on Keppel deliverables / scope before contract
- Michael: 4pm call with Andrew (today); Simon call (tomorrow)

---

## Registry / Evaluation Outcomes

| Tool | AIR Issue | Action | Outcome |
|---|---|---|---|
| Fireflies.ai | AIR-9 | ENRICHED | Android performance gap added. iOS opens instantly; Android significantly slower. |
| Obsidian | AIR-74 | ENRICHED | Mobile sync findings added: paid Sync subscription required; Android lacks Web Clipper; Graph View desktop-only. Distinct from earlier substrate finding. |
| Plaud | AIR-157 | REVERTED | Entry was a hallucination artefact — Plaud was never mentioned in this meeting. AIR-157 moved to Rejected 2026-06-08. Grep of raw transcript confirmed zero matches. |
| Google Calendar MCP | AIR-156 | CREATED | Backlog. Respond-to-event, analyze-availability, schedule-meetings capabilities demonstrated. Data-boundary open question for IT/Ops. Gate 1 chained. |
| Gmail MCP | AIR-155 | CREATED | Backlog. Send emails via MCP. OAuth scope and admin policy open questions. Gate 1 chained. |

---

## Monday Writes Summary

**Parent items source-bumped (Step 3A):**
- [2900825519](https://janusd-company.monday.com/boards/5095012818/pulses/2900825519) Prime Radiant — company-wide knowledge graph + digital twin
- [2924305391](https://janusd-company.monday.com/boards/5095012818/pulses/2924305391) PM team onboarding to Prime Radiant (Lysander / Spike / Rosa)

**New parent created (Step 3D):**
- [2976752077](https://janusd-company.monday.com/boards/5095012818/pulses/2976752077) Jane — Janus AI assistant deployment and handover | Planned Automations | In Development | Jehad + Michael

**Sub-items created (Step 3B, 3 items):**

Under 2900825519:
- [2976746728](https://janusd-company.monday.com/boards/5095012849/pulses/2976746728) Test Fireflies Android performance with Andre — Jehad
- [2976735394](https://janusd-company.monday.com/boards/5095012849/pulses/2976735394) Document Obsidian Sync mobile setup for Bonaventure — Jehad

Under 2976752077:
- [2976744834](https://janusd-company.monday.com/boards/5095012849/pulses/2976744834) Prepare one-pager installation and configuration guide for Jane bot — Jehad + Michael

**Step 3H backfills:** 0 (both source-bumped parents already had Description headers from earlier today's AIO standup).

**Context Coverage Invariant (Step 3I):** PASS — 6/6 touched items have Description Updates.

**Deduplication (Step 2B.1):** 3 scanned | 2 cleared | 1 medium-confidence flag (Obsidian Sync) — user confirmed as distinct scope, created.

---

## External / Other-Department Follow-ups

*(Not AIO-owned; captured for record only — no Monday items created.)*

- **Bonaventure / ARM:** Raise ARM secure enclave sensor-provenance concept with Alexander at ARM tomorrow. Strategic hardware idea for IoT data integrity — potential collaboration with Keppel BIM certification use case.
- **Bonaventure / Euclid:** Push Euclid on Jane bot handover timeline — "why is it taking so long?"
- **Bonaventure + Rosa / Keppel:** Align on BIM certification deliverables and scope before contract. First certification module is the key near-term milestone.
- **Michael:** 4pm call with Andrew (today); Simon call (tomorrow).
