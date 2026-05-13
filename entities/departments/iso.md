---
type: department
title: ISO
slug: iso
created: 2026-05-11
updated: 2026-05-11
departments: [iso]
status: active
owner: simon-tarskih
related: [simon-tarskih, bonaventure-wong, iso-compliance-programme, 2026-05-01-iso-compliance-gate-before-automation, 2026-04-20-iso-first-stack-architectural-pivot, ai-policy-gate-approval]
---

# ISO

Janus's compliance function — ISO 9001 (quality management), ISO 27001 (information security), ISO 42001 (AI management). Cross-cutting across every other department: every AIO sandbox graduation, every ITO production handover, every HR contract template, every Marketing campaign asset, every Finance vendor contract touches the ISO function.

ISO sits structurally between [[office-of-ceo|Office of the CEO]] (Bonaventure as executive sponsor) and the rest of the company (where compliance evidence has to be generated, audited, and retained). Treated as a department in the wiki vocabulary because it has its own knowledge surface — the [[iso-compliance-programme]], the `/ims-enrolment` skill, and a growing reference set of ISO documentation, evidence templates, and audit artefacts.

## People

- **[[simon-tarskih]]** — ISO programme lead; reports to [[bonaventure-wong]]; primary curator of the eventual ISO Prime Radiant instance.
- **[[bonaventure-wong]]** — Executive sponsor; ISO 9001 mandatory across AIO/ITO interfaces (per [[2026-05-01-iso-compliance-gate-before-automation|the 2026-05-01 decision]]).

## Prime Radiant instance

Queued. The [[iso-compliance-programme]] already has substantial knowledge surface (22 references, ISO 9001/27001/42001 documentation work, the `/ims-enrolment` skill that enrolls departments into the compliance management system). When Simon is ready, the ISO Prime Radiant will spin up as a peer instance — likely sequenced after the Marketing pilot proves the federation pattern, but ahead of HR/Finance/Engineering/Training given how cross-cutting ISO is.

## Infrastructure layer (per three-layer model)

When the ISO instance stands up:

- ISO 9001 (quality management) documentation, audit evidence, process owner maps
- ISO 27001 (information security) controls, risk assessments, treatment plans
- ISO 42001 (AI management) — newer; AIO's tool evaluation framework is the obvious feeder
- Process taxonomies (the 11 open questions Simon has for each process owner)
- Compliance gate definitions (what does "ISO-compliant" mean for each handover surface)
- Audit cadence and evidence templates

A large part of the Infrastructure layer is *already being authored* by Simon as part of the [[iso-compliance-programme]] — the ISO instance, when it spins up, will inherit that content rather than rebuilding it.

## AIO ↔ ISO interface

ISO is the compliance anchor for every AIO output going to production. The two key interfaces:

1. **Tool evaluation gate** — every AI tool that passes the AIO evaluation framework (`/ai-tool-evaluation`) has to pass an ISO 42001 / 27001 check before ITO production handover. The [[ai-policy-gate-approval]] process formalises this.
2. **Skill standardisation** — Jehad's `/standup` skill, the `/ims-enrolment` skill, and any other skill that touches the AIO operational flow need ISO-aligned documentation (process owner, inputs, outputs, control points, KPIs). The standup-skill ISO alignment was one of the multi-track [[iso-compliance-programme]] streams.

## Cross-instance federation

ISO federates with **every** other department because compliance touches every department. The mesh-federation pattern ([[peer-to-peer-mesh-federation-pattern]]) suggests an `entities/departments/iso/` shared subfolder in *each* department vault — AIO×ISO, ITO×ISO, Marketing×ISO, HR×ISO, Finance×ISO. Compliance evidence specific to each pairing lands in that pairing's shared folder; the ISO Prime Radiant (when it stands up) reads from all of them.

## Key projects

[[iso-compliance-programme]] — multi-track: ISO docs foundation + ai-tool-evaluation ISO alignment + standup-skill ISO alignment + ISO facilitation skill build + `/ims-enrolment` skill.

## Status

Department entity created 2026-05-11 — closes the gap noted in the 11 May AIO standup (the original 2026-05-08 department-page creation pass missed ISO). The locked `departments:` vocabulary in CLAUDE.md was updated v0.8 → v0.9 in the same change.
