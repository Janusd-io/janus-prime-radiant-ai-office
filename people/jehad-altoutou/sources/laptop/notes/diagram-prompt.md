---
type: source
source_type: laptop
title: diagram-prompt
slug: diagram-prompt
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/templates/diagram-prompt.md
original_size: 5633
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Empty ChatGPT-image-generation prompt template — public-internal process artefact."
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# diagram-prompt

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/templates/diagram-prompt.md` on 2026-05-14._

# ChatGPT Diagram Prompt — [PROCESS TITLE]

> **How to use:** Copy everything between the two `---PROMPT---` markers below into ChatGPT (GPT-5 or GPT-4o with image generation). It produces a high-quality, wide, ISO-grade diagram of your process. Below the prompt is a **Mermaid backup** — if ChatGPT garbles the text (it sometimes does on text-heavy diagrams), open the Mermaid block in your process doc on [[github|GitHub]] or paste it into [mermaid.live](https://mermaid.live) to export as PNG/SVG.

---

## Filling in this prompt

The skill auto-populates the placeholders below from your completed process document. If you're filling in by hand:

- `[PROCESS TITLE]` — the name of your process (e.g., *"HR Department · Parent Process"* or *"Talent Acquisition — Hiring Workflow"*)
- `[SUBTITLE]` — short descriptor (e.g., *"[[iso-9001-figure-1|ISO 9001 Figure 1]] schematic · [N] activities"*)
- `[SOURCES LIST]` — bullet list from Section 2 of your process doc
- `[INPUTS LIST]` — bullet list from Section 3
- `[ACTIVITIES LIST]` — numbered list from Section 4 (the steps with one-line descriptions)
- `[OUTPUTS LIST]` — bullet list from Section 5
- `[RECEIVERS LIST]` — bullet list from Section 6
- `[CONTROLS LIST]` — bullet list from Section 7
- `[RESOURCES LIST]` — bullet list from Section 8
- `[KPI LIST]` — bullet list from Section 9 (use proposed KPIs if formal ones aren't defined yet)
- `[ISO CLAUSE FOOTER]` — the clause map at the bottom of your process doc

---

---PROMPT---

Generate a **high-resolution, ultra-wide professional business diagram** (aspect ratio 21:9 or wider, minimum 3840×1620 px) titled **"[PROCESS TITLE]"** with subtitle **"[SUBTITLE]"**.

**Style requirements:**

- Clean corporate / management-consulting aesthetic, similar to a [[mckinsey|McKinsey]] or [[deloitte|Deloitte]] slide
- Flat design, soft drop shadows on boxes, rounded corners (8px radius)
- White background
- Sans-serif typography (Inter, Helvetica Neue, or SF Pro), all text crisp and readable
- Professional ISO palette:
  - Activity / process boxes: navy `#1A4480` border, light blue `#E6F0FF` fill
  - Controls box: amber `#996600` border, soft yellow `#FFF8D6` fill
  - Resources box: deep red `#990000` border, soft pink `#FFE8E8` fill
  - KPI / monitoring box: green `#1B5E20` border, light green `#E8F5E9` fill
  - Sources / Inputs / Outputs / Receivers: mid-grey `#666` border, neutral grey `#F5F5F5` fill
- All arrows clean with arrowheads, no overlap
- Decision points (if any) as diamond shapes with two labelled exits (pass/fail or yes/no)

**Layout — strict horizontal left-to-right flow with controls above and resources below:**

```
                       [ CONTROLS — full width across top ]
                                    │
                                    ▼
[SOURCES OF INPUTS] → [INPUTS] → [ACTIVITIES — large central box] → [OUTPUTS] → [RECEIVERS OF OUTPUTS]
                                    ▲
                                    │
                       [ RESOURCES — full width across bottom ]

                       [ MONITORING & MEASUREMENT — KPIs box, attached to ACTIVITIES with dashed line ]
```

**Render every line of text exactly as written, in legible size:**

**TOP BOX — CONTROLS:**
Header: "CONTROLS"
Body bullets:
[CONTROLS LIST]

**LEFTMOST BOX — SOURCES OF INPUTS:**
Header: "SOURCES OF INPUTS"
Body bullets:
[SOURCES LIST]

**SECOND BOX — INPUTS:**
Header: "INPUTS"
Body bullets:
[INPUTS LIST]

**CENTRAL LARGE BOX — ACTIVITIES (this is the biggest box, render each activity as a numbered sub-box left to right with arrows between them):**
Header: "ACTIVITIES"
Sub-header: "[Number of activities]-step flow with control points (CP) between each step"

Inside this box, render the activities left to right with arrows and CP markers:

[ACTIVITIES LIST]

**FOURTH BOX — OUTPUTS:**
Header: "OUTPUTS"
Body bullets:
[OUTPUTS LIST]

**RIGHTMOST BOX — RECEIVERS OF OUTPUTS:**
Header: "RECEIVERS OF OUTPUTS"
Body bullets:
[RECEIVERS LIST]

**BOTTOM BOX — RESOURCES (full width):**
Header: "RESOURCES — Process Owner: [PROCESS OWNER NAME]"
Body bullets:
[RESOURCES LIST]

**KPI BOX (attached to ACTIVITIES with dashed line):**
Header: "MONITORING & MEASUREMENT — KPIs"
Body bullets:
[KPI LIST]

**Footer (centered below diagram):**
[ISO CLAUSE FOOTER]

**Critical:** Render all text legibly. Do not invent or change wording. Wide landscape orientation, never portrait. Output as a single high-resolution image.

---PROMPT---

## Mermaid backup (guaranteed perfect text)

If ChatGPT garbles any text (likely on text-heavy diagrams), use this Mermaid block instead. Open the parent process document in your browser (GitHub renders Mermaid natively), screenshot the rendered diagram, OR paste this block into [mermaid.live](https://mermaid.live) and export PNG/SVG.

The Mermaid version is already inside your process document — section 1, the `flowchart LR` code block. No separate copy needed here.

**Pro tip for mermaid.live exports:** in the Config tab set `themeVariables: { fontSize: '16px' }` for crispness, then Actions → SVG. SVG scales cleanly to any size.

---

## What to do with the generated image

1. Save the PNG/SVG as `diagram-[process-slug].png` (e.g., `diagram-talent-acquisition.png`)
2. Place it next to your process markdown file
3. Reference it in your handover bundle (the `handover-to-simon.md` Diagrams section)
4. Optional: embed it at the top of the process doc by replacing the Mermaid block with `![Process diagram](./diagram-[slug].png)`

The auditor sees the polished image; the markdown + Mermaid stays as the canonical source.
