---
type: process
title: Unified Process Design Template (IMS)
slug: unified-process-design-template
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, ims-compliance]
captured_by: jehad-altoutou
audience: [department]
confidence: high
sources: [tmpl-unified-process-design, tmpl-light-process-discovery]
related: [ims-digital-twin, ims-process-register, ims-process-visualization-standard, ai-tool-evaluation-process-map, iso-ims-puls, ims-enrolment]
---

# Unified Process Design Template (IMS)

The documentation toolset at the heart of the [[ims-digital-twin|IMS digital twin]] — a **two-template pair** designed from scratch for the integrated three-standard context (not adapted from generic templates).

## Technical template (machine-readable) — TMPL-IMS-UnifiedProcessDesign v11.0
The full data model for documenting a process. Source: [[tmpl-unified-process-design]]. Captures:
- **Header**: Process ID, name, owner, applicable standards, **Process Objective** (outcome + measure + target + timeframe — e.g. *"100% of AI tool requests evaluated within 2 business days, with traceable approval/rejection records"*).
- **Participants**: persons (User_ID), departments (Company_ID/Dept_ID), systems (Software Registry), AI agents (AI_Model_ID) — each with an ID resolvable in a registry.
- **SIPOC blocks**: Input Sources → Inputs → Process steps → Outputs → Output destinations.
- **Four registries** referenced: Data Sources, Software, AI Models & Agents, Organisation Documents.
- **Gate criteria + KPIs**, and **full ISO clause anchoring** per step.

## Light template (human-readable) — TMPL-IMS-Light-UnifiedProcessDesign v2.0
The plain-language **Process Discovery Template**. Source: [[tmpl-light-process-discovery]]. Mirrors the technical template block-for-block with conversational questions + concrete examples, so a process owner needs **no ISO knowledge**. Two modes:
- **Mode A — Discovery**: answer each question in your own words.
- **Mode B — Audit Checklist**: point to where the info already lives (don't rewrite).
Complex processes: "Fill and flag" — document the main flow, mark `FLAG — possible sub-process` where a step is really a mini-process (documented later with the same template).

## How they work together
Owner fills the **Light** template → AI translates to the **Technical** format → diagram generated per the [[ims-process-visualization-standard|Visualization Standard]]. This is the scale interface for onboarding all 41 [[ims-process-register|registered processes]] and any department via [[ims-enrolment]]. Validated end-to-end on the [[ai-tool-evaluation-process-map|AI Tool Evaluation pilot]].
