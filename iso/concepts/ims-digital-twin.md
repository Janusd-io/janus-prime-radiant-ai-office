---
type: concept
title: IMS Digital Twin
slug: ims-digital-twin
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, ims-compliance]
captured_by: jehad-altoutou
audience: [department]
confidence: high
sources: [ims-readiness-assessment-2026-06-08, reg-ims-process-register, tmpl-unified-process-design, tmpl-light-process-discovery]
related: [iso-ims-puls, three-iso-standards, ims-process-register, unified-process-design-template, ims-process-visualization-standard, ai-tool-evaluation-process-map, organisational-digital-twin, platform-development-process, simon-tarskih]
---

# IMS Digital Twin

Janus Digital's approach to building its **Integrated Management System** (ISO 9001 quality · ISO 27001 information security · ISO 42001 AI management) not as a static document set but as a **digital twin** — an AI-managed, machine-readable model of every company process, anchored to ISO clauses and kept live. Owned by the **IMS & Compliance function** ([[simon-tarskih|Simon]], Head of IMS & Compliance). Source of truth: the ISO/IMS document set received 2026-06-09 (filed under `iso/sources/`).

It is the **internal** counterpart to Janus's customer-facing twin work (cf. [[organisational-digital-twin]], [[hgtft]]); in the [[ims-process-register|process register]] it is process **C12 — Internal AI Product (IMS Digital Twin)**, held to the same lifecycle rigour as the external product (C1).

## The core mechanism — two-template architecture

The defining design idea (Phase 4 of the build): **one human-readable template, one machine-readable template**, with AI bridging them.

- **[[unified-process-design-template|Unified Digital Process Design Template]]** (technical, v11.0) — the full machine-readable data model for a process: SIPOC structure, four registries (Data Sources, Software, AI Models & Agents, Organisation Documents), gate criteria, KPIs, participant IDs, and full ISO clause anchoring.
- **[[tmpl-light-process-discovery|Process Discovery Template]]** (light, v2.0) — a plain-language companion that mirrors the technical template block-for-block but asks conversational questions with concrete examples, so any process owner can fill it **without ISO knowledge**. Two modes: **Discovery** (answer directly) and **Audit checklist** (point to where the info already lives).

> Process owners fill the **Light** template → **AI translates** it into the **Technical** format. *"This two-template architecture is the core mechanism of the IMS digital twin."* Proving the Light→Technical AI translation is the next milestone (see Gaps below).

## Build sequence (scope → structure → content → scale)

Per the [[ims-readiness-assessment-2026-06-08|build progress report]] (2026-06-08), four phases completed in ~1.5 months (solo effort):

1. **Strategic scope** (May 2026) — every clause of ISO 9001/27001/42001 cross-referenced against process codes with evidence requirements per clause → [[ims-clause-comparison-matrix|Clause Comparison Matrix]]; 41 processes identified, categorised, owners proposed → [[ims-process-register|Process Register]].
2. **Documentation methodology** (May–Jun) — the technical template (11 iterations) + the [[ims-process-visualization-standard|Visualization Standard]] (notation + a 19-rule AI build prompt so the twin can generate compliant diagrams autonomously).
3. **Pilot documented end-to-end** (Jun) — [[ai-tool-evaluation-process-map|AI Tool Evaluation & Approval]], the first fully-populated technical process map + Level-1 swimlane diagram. Validated the template; no design flaws found.
4. **Scale interface** (Jun) — the Light discovery template as the human interface to onboard 41 owners without ISO fluency.

## Gaps before scaling (per the readiness report)

1. **Pilot validation** — the AI Tool Evaluation pilot not yet confirmed by its process owner (Head of AI Native, [[michael-bruck|Michael]]).
2. **Light→Technical translation** — the AI conversion (the core twin mechanism) not yet tested.
3. **Process prioritisation** — no decision yet on which of the 41 to document first (should be by ISO audit risk + owner availability).
4. **Document lifecycle** — everything is DRAFT; no formal review/approval/sign-off records yet.

> Strategic read: *"No material structural gaps… the risks are operational rather than architectural — the methodology is sound, the tools are built, the next step is validation at scale."*

## Why it matters across the org
This is the substrate for ISO certification across all of Janus (Singapore, UK, UAE, future EU) and the reusable engine for documenting any department's processes. It connects to the existing [[ims-enrolment]] skill (department onboarding into the IMS) and the [[platform-development-process]] quality discipline.

## Document set (all DRAFT, 2026-06)
See [[iso-ims-puls]] for the full map. Sources: [[ims-readiness-assessment-2026-06-08]] · [[reg-ims-process-register]] · [[ims-clause-comparison-matrix]] · [[diag-ims-visualization-standard]] · [[unified-process-design-template]] ([[tmpl-unified-process-design|technical]] + [[tmpl-light-process-discovery|light]]) · [[proc-ims-ai-tool-evaluation]] (+ [[ai-tool-evaluation-diagram|diagram]]).
