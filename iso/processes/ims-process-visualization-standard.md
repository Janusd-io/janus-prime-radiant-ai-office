---
type: process
title: IMS Process Visualization Standard
slug: ims-process-visualization-standard
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, ims-compliance]
captured_by: jehad-altoutou
audience: [department]
confidence: high
sources: [diag-ims-visualization-standard]
related: [ims-digital-twin, unified-process-design-template, ai-tool-evaluation-diagram, iso-ims-puls]
---

# IMS Process Visualization Standard

The notation standard for **all** IMS process diagrams at Janus (DIAG-IMS-ProcessVisualizationStandard v1.0; ISO 9001 cl.4.4, ISO 5807). Owner: IMS/Compliance. Full spec verbatim in [[diag-ims-visualization-standard|the source]].

## Symbol library (10 elements, ISO 5807 / BPMN 2.0)
Start/End (oval) · Activity (rectangle) · Decision/Gate (diamond) · Document/Record (wavy-bottom rect, light yellow) · Data Store (cylinder, light blue) · Sub-process (rect with [+], light grey) · Input/Output (parallelogram, light green) · Message/Notification (rounded rect + envelope, light orange) · Swimlane (vertical column per actor) · Annotation (dashed bracket). **No other shapes** without updating the standard.

## Colour code (meaning carried by shape; colour secondary, must read in greyscale)
Document=amber `#C8A800`/`#FFF9E6` · Data Store=blue `#0066CC`/`#E1F0FA` · Input/Output=green `#339933`/`#E8F4E8` · Message=orange `#CC6600`/`#FFF0E6` · Rejected/exception path=grey `#AAAAAA` · main flow=white/`#333333`. No decorative colours.

## Layout rules
Landscape (A3 preferred); top-to-bottom within each swimlane, lanes left-to-right by sequence; **2–7 swimlanes** (one per actor: Person/Department/System/AI Agent); solid arrows for main flow, dashed for exceptions, label every decision branch; min 20px between elements / 40px between lanes; legend required bottom-left; title block (Process name, ID, version, date, status, owner, ISO refs) on every diagram.

## File management
`DIAG-[ProcessID]-v[version]-[YYYY-MM-DD].drawio` — `.drawio` is the editable master; export `.svg` (embed), `.pdf` (distribute), `.png` (reference). Versioned on any structural change.

## 19-rule AI build prompt
The standard embeds a 19-rule prompt so the [[ims-digital-twin|IMS digital twin]] can **generate compliant diagrams autonomously** from a process map. First applied to [[ai-tool-evaluation-diagram|the AI Tool Evaluation diagram]] (5 swimlanes). Full rule list in the source.
