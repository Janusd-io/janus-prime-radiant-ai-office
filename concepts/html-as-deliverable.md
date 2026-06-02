---
type: concept
title: HTML as deliverable
slug: html-as-deliverable
created: 2026-05-12
updated: 2026-06-02
sources: [2026-05-12-aio-andrew-marketing, 2026-05-20-claude-html-effectiveness-shihipar]
related: [janus-html-deck, ralph-loop-pattern, claude-code, recursive-self-improving-loop, organisational-digital-twin]
audience: department
captured_by: jehad-altoutou
departments: [ai-office, marketing, engineering]
---

# HTML as deliverable

The discipline of preferring **HTML over Markdown** as the output format for agent-produced artefacts intended for human reading or sharing. Originated as an AIO stance during the 2026-05-12 AIO ↔ Marketing meeting (*"HTML over PowerPoint/PDF/NotebookLM for AIO outputs"*); externally validated and operationally formalised by Anthropic itself on 2026-05-20 via Thariq Shihipar's *"Using Claude Code: The unreasonable effectiveness of HTML"* blog post ([[2026-05-20-claude-html-effectiveness-shihipar]]).

## Why HTML over Markdown (Shihipar's argument, 2026-05-20)

The canonical case from Anthropic-internal practice on the Claude Code team:

1. **Information density.** HTML can carry tables, CSS-styled design data, SVG illustrations, executable JS snippets, interactive HTML+JS+CSS elements, spatial data via absolute positioning, and embedded images. In Markdown the model fakes these (ASCII diagrams, Unicode colour estimates, ad-hoc tables). *"In my opinion, there is almost no set of information that Claude can read that you cannot efficiently represent with HTML."*
2. **Readability past ~100 lines.** Markdown stops being usable around the 100-line mark; Shihipar reports he stops reading and nobody else in his organisation reads either. HTML files structured with tabs, sections, illustrations, and links *"can be mobile responsive so you can read it differently based on your form factor."* The chance someone actually reads a spec, report, or PR write-up is much higher when it ships as HTML.
3. **Ease of sharing.** Browsers don't render Markdown natively. HTML uploads to any link surface, opens anywhere, and doesn't require attachment workflows.
4. **Two-way interactions.** HTML can carry sliders, knobs, prototype controls, and "copy as JSON / copy as prompt" buttons that turn UI gestures back into machine-readable inputs the agent can resume from. *"You stay in the loop, but the loop gets much tighter."*
5. **Data ingestion via Claude Code.** Claude Code's ability to read the codebase, MCP-connected tools (Slack, Linear, etc.), browser context (Claude in Chrome), and git history means it can synthesise across all of these into one HTML output — exactly the pattern this wiki uses for [[janus-html-deck|Janus-branded decks]] and architecture diagrams.

Shihipar's caveat — the only one he gives — is that Markdown is more token-efficient. He responds that with the *1MM context window in Opus 4.7*, the increase isn't noticeable, and the higher likelihood of the artefact being read more than offsets the cost.

His own current practice: *"I have honestly stopped using Markdown altogether for almost everything, but I'm probably far on the HTML maximalist side of things."*

## Use cases (Shihipar's catalogue + AIO adoption)

| Use case | Shihipar example | AIO instance |
|---|---|---|
| Specs / planning / exploration | Multi-option mockups in one HTML grid; implementation plans with mockups + data flow | The wiki's `presentations/` folder; [[singapore-monitoring-frame-audit-2026-05]] |
| Code review and understanding | Render diffs + annotations + flowcharts inline | Not yet a wiki use case |
| Design and prototypes | Sketch designs in HTML, then port to React / Swift / native | [[janus-html-deck]] decks; brand-aligned slide artefacts |
| Reports / research / learning | Long HTML doc, interactive explainer, or slideshow | Most AIO outbound artefacts since 2026-05-12 |
| Custom editing interfaces | Throwaway editor — Linear-ticket re-prioritiser, feature-flag editor, prompt tuner with side-by-side preview, all with "copy back" export | Not yet a wiki use case — strong fit for the lint workflow, where a "review and re-prioritise carry-forward queue" HTML editor would compress the human-in-loop step |

## Why this matters to the AI Office

Three reads:

1. **The 2026-05-12 AIO stance is now Anthropic-blessed.** Shihipar's piece is the cleanest external validation of a discipline AIO already operates under. Cite it when explaining the stance to risk-sensitive Janus audiences who would treat "AIO chose HTML over PowerPoint" as a heterodox call — it isn't; it's the same call the Claude Code team made.
2. **Strong fit with the [[recursive-self-improving-loop]] *Quality Gate* step.** Shihipar's "throwaway editor" pattern (HTML file built per-task with copy-back-as-prompt) is a concrete way to compress the human-review step in the YC five-part loop. The human stays in the decision but the input/output surface is HTML, not chat. Worth proposing as an AIO build for the lint workflow specifically.
3. **Pairs with [[janus-html-deck]] brand discipline.** The skill that produces Janus-branded HTML decks is the AIO's first formalisation of HTML-as-deliverable for outbound artefacts. The Shihipar piece is its inbound counterpart: HTML-as-deliverable for *internal* artefacts (specs, reports, dashboards, editors). Same format, different audience and styling discipline.

## Operating principle for AIO

*If the artefact will be read by more than one person, by anyone other than the agent that generated it, or by anyone more than a few hours after generation — prefer HTML.* Markdown is fine for transient agent-to-agent communication; HTML is the discipline for any artefact crossing a boundary (cross-team, cross-time, outbound).

The wiki itself remains in Markdown — because each page is short, version-controlled, and grep-targeted, and because Obsidian renders Markdown natively. The discipline applies to *deliverables*, not to the substrate underneath them. The [[janus-html-deck|`janus-html-deck`]] skill is the inverse-discipline tool: take Markdown context, produce branded HTML for sharing.

## Related concepts

- **[[janus-html-deck]]** — Janus-branded HTML deck skill; the outbound-deliverable instantiation of this discipline.
- **[[ralph-loop-pattern]]** — agent-runtime loop; HTML is the natural artefact format for *Ralph progress-saves* (state preserved between iterations).
- **[[claude-code]]** — the tool Shihipar's piece is written about; HTML generation is now first-class in Claude Code.
- **[[recursive-self-improving-loop]]** — HTML editors are the natural Quality-Gate surface for human-in-loop review steps.
