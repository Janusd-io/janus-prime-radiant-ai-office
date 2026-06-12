---
type: vendor
title: Deel
slug: deel
created: 2026-05-06
updated: 2026-06-12
departments: [hr, finance]
status: active
confidence: high
sources: [aio-2026-05-04, 2026-06-12-assessify-hr-meeting]
related: [assessify, linear]
migrated_from: entities/vendors/deel.md
---
# Deel

HR / payroll platform with developer API. At Janus, currently used as the **headless backend** for HR operations — line managers do not interact with Deel directly; they interact via agentic UIs that sit on top of Deel.

## Status

- **Linear AIR-168** — Deel registered in the AI Registry on 2026-06-12, status **Production** (registering existing reality; the tool was in production HR use with no AIR entry). Labels: Functional, Finance. Note: Linear has no "HR" department label as of 2026-06-12 — HR scope is carried in the description body only.
- **Linear AIP-15** "Deel API & Developer Platform — Capability Assessment" — In Progress as of 2026-05-04. Active backend dependency.
- An earlier "Set up Deel sandbox account" task (May 2026, Monday sub-item 2898219506) covered middleware/API integration over Deel.

## Replacement strategy (decided 2026-06-12, Assessify HR meeting)

Strategic direction from the [[2026-06-12-assessify-hr-meeting|Assessify HR meeting]]: the internal [[assessify|Assessify]] platform will **progressively replace Deel** — recruitment, leave management, and employee profiles first; performance management and training later. Deel is retained specifically for **multi-country payroll calculations** (tax, pension, social insurance) until an internal payroll module is built.

Current production footprint (per Theresa Wong, HR): leave tracking, payslips, multi-country payroll. Per `2026-06-12-assessify-hr-meeting` ("I actually prefer our payslip more than the Deel payment"), HR's preference already runs toward the internal surfaces; and per the same transcript ("the only thing why we may only use Deel is because they will calculate everything automatically for us"), the automatic multi-country payroll calculation is the sole retained dependency. Jehad Altoutou framed the direction explicitly: "we're building this as a platform to use instead of Deel."

## Janus architecture pattern (decided 2026-05-04)

Deel becomes the headless backend; agentic UIs become the user surface. Rationale: Deel's UI is suboptimal for line-manager workflows, and the agentic-UI middleware lets Janus shape the interaction without forking the data layer.

## Watch for

- AIR-168 status moving Production → Monitor (and eventually Deprecated for replaced modules) as Assessify modules go live; payroll calculation is the last dependency.
- Contract scope/renewal vs. the shrinking footprint — avoid paying for modules Assessify has replaced.
- Whether the agentic-UI-as-middleware pattern generalises to other vendors with awkward native UIs.
- Missing "HR" department label in Linear AIR — surfaced 2026-06-12; candidate label-vocabulary addition.
