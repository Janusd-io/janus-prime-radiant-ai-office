---
type: question
title: "Create vendor page for Celonis — action-oriented process mining / OCEL"
slug: ingest-2026-06-09-celonis-vendor-page
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, engineering]
status: active
owner: michael-bruck
sources: [odt-competitive-analysis-2026, park-van-der-aalst-dto-process-mining]
related: [organisational-digital-twin, park-van-der-aalst-dto-process-mining]
---

# Create vendor page for Celonis — action-oriented process mining / OCEL

## What this is

Celonis is the leading commercial platform for **object-centric and action-oriented process mining** — the same academic tradition as the [[park-van-der-aalst-dto-process-mining|Park & van der Aalst DT-IM paper]] (RWTH Aachen PADS group). They monitor operational ERP event logs continuously, identify bottlenecks, and trigger automated corrections. Classified in [[odt-competitive-analysis-2026]] as "Adjacent Process Mining."

No Celonis vendor page currently exists in this wiki.

## Proposed action

Create `vendors/celonis.md`.

## Key data points from [[odt-competitive-analysis-2026]]

- **Architecture**: Object-Centric Process Mining + Action-Oriented Process Mining (OCEL/OCPN-based). Continuously monitors ERP event logs to identify bottlenecks and trigger automated corrections.
- **Maturity**: Scaled commercial product (enterprise SaaS; subscription pricing).
- **What it does**: Reconstructs highly accurate process flows from transactional event data, then writes back configuration changes to the underlying ERP. This is the commercial instantiation of the academic DT-IM pattern.
- Source: [researchgate.net/publication/355794218](https://www.researchgate.net/publication/355794218_Realizing_A_Digital_Twin_of_An_Organization_Using_Action-oriented_Process_Mining)

## Relevance to Janus

Celonis is the commercial layer sitting directly adjacent to the Park/van der Aalst academic work already filed in [[park-van-der-aalst-dto-process-mining]]. The PADS RWTH research group that produced the DT-IM architecture is the same lineage Celonis's process-mining technology is built on. As Janus considers how to productise the HGTFT / ODT combination, understanding what Celonis already does commercially (and where it falls short) is important competitive intelligence.

The [[odt-competitive-analysis-2026]] competition table places Celonis in "Adjacent Process Mining" — not in the "Analyst-DTO" segment — because Celonis focuses on ERP process flows, not the full organisational digital twin. The gap between "Celonis monitors ERP logs" and "full DTO with agentic layer and institutional memory" is the gap Janus is positioned to fill for mid-market clients.

## Decision needed

Straightforward vendor page creation. Suggest creating `vendors/celonis.md` with a process-mining category note and explicit linkage to [[park-van-der-aalst-dto-process-mining]] for the academic grounding.
