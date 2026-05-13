---
type: decision
title: HTML adopted as Janus's primary presentation output format; PowerPoint deprioritised
slug: 2026-05-12-html-as-presentation-format-adopted
created: 2026-05-12
updated: 2026-05-12
status: resolved
owner: michael
departments: [ai-office, marketing, office-of-ceo]
confidence: high
sources: [2026-05-12-bonaventure-ai-native-call]
related: [bonaventure-wong, michael-bruck, andrew-soane, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-11-html-over-powerpoint-for-read-only-content, 2026-05-11-notebooklm-retirement-html-over-image-outputs]
---

## Decision

HTML is Janus's primary output format for presentations, briefs, decks, and read-only content delivered to internal or external audiences. PowerPoint is deprioritised. The 11 May lessons + decision ([[2026-05-11-html-over-powerpoint-for-read-only-content]], [[2026-05-11-notebooklm-retirement-html-over-image-outputs]]) are now CEO-endorsed and operational policy.

## Bonaventure on the call (12 May 2026)

Michael showed the HTML brief used for this CEO call + the HTML deck built for [[andrew-soane|Andrew]]'s onboarding to the Marketing Prime Radiant. Bonaventure's response:

> "That's fine. It's a damn. People have a problem with it. They're such a visual. Visual creatures. We are very visual species. And so as long as you can toddle in and out, they don't care how it's delivered and move forward and all that connected."

And on the dynamic potential:

> "You can have dynamic website if you know how to do it right, which is this."

Michael's framing on the call:

> "Creating HTML has been very difficult, but now it's easier to generate HTML than it is generated PowerPoint. It can render anything. It pulled all the information out of [the system]... It takes very little time and it's very cheap on the token budget."

## Options considered

1. **Continue with PowerPoint as default** — rejected; slow generation, expensive in tokens, harder to embed live data, can't be dynamically refreshed.
2. **HTML for read-only content, PowerPoint when an editable .pptx is explicitly requested** (chosen) — the 11 May lesson framing extended to a formal decision.
3. **PDF as universal output** — not seriously considered; preserves layout but loses the dynamic / wiki-integration upside HTML carries.

## Why this decision

- **Token economics.** HTML generation through Claude is 5-10× cheaper than PowerPoint for equivalent content density. Live-tested across the 12 May Bonaventure brief and the Andrew onboarding deck.
- **Wiki integration.** HTML outputs can pull directly from the wiki state and re-generate from current data; PowerPoint output is frozen at creation time.
- **Externalisability fits the [[ai-native-janus-positioning|AI Native pitch]].** Janus presenting HTML-rendered material reinforces the "we use what we sell" credibility — using a dynamic, AI-friendly output format is itself part of the positioning.
- **Visual fidelity adequate** — Bonaventure's response on the call confirms the rendered HTML reads as a real presentation, not a stripped-back text fallback.
- **Bonaventure's only caveat:** *"people have a problem with it... they're such a visual species."* I.e., the issue is audience habituation, not the format itself. Janus can lead audiences onto HTML; doesn't need PowerPoint as a defensive default.

## When this took effect

12 May 2026 — verbal adoption on the call. Operational immediately:

- The 12 May Bonaventure briefing is itself an HTML artefact (`aio-update-bonaventure-2026-05-12.html`).
- The Andrew onboarding deck (8 May → revised per Andrew's 12 May feedback) is HTML.
- The Marketing PR onboarding briefs for future department curators (HR, ISO, Finance) will be HTML-by-default.

## Implications

- **AIO tooling for presentation generation** continues to be Claude-skill-driven (HTML output by default); no need for a separate PowerPoint-generation skill.
- **Marketing PR outputs** — campaign briefs, POVs, white papers — generated as HTML; converted to PDF when the audience explicitly requires it (e.g., investor regulatory filings).
- **Style discipline** — Janus needs a brand stylesheet for HTML outputs. The 12 May Andrew deck was rendered without one ("kind of bland"). Style sheet / brand-CSS / fonts / colour palette is a Marketing PR deliverable.

## Related

- [[2026-05-11-html-over-powerpoint-for-read-only-content]] — originating lesson.
- [[2026-05-11-notebooklm-retirement-html-over-image-outputs]] — earlier decision retiring NotebookLM in favour of HTML for org-chart / presentation outputs.
- [[ai-native-janus-positioning]] — the strategic brief where this fits.
