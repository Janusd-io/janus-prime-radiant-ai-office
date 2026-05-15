---
type: process
title: Janus HTML deck brand guideline (preliminary v0.1)
slug: janus-html-deck-brand-guideline
created: 2026-05-15
updated: 2026-05-15
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [2026-05-15-singapore-marketing-launch-plan-v1]
related: [marketing-prime-radiant, andrew-soane, 2026-05-12-html-as-presentation-format-adopted, 2026-05-15-singapore-marketing-launch-plan-v1]
---

# Janus HTML deck brand guideline — preliminary v0.1

> **Status:** preliminary v0.1, derived 2026-05-15 from [[2026-05-15-singapore-marketing-launch-plan-v1|Andrew's Singapore campaign plan v1 PPTX]] (the closest thing to an internal style reference Janus has as of mid-May 2026). Treat this as a starting point — Andrew or a brand designer will likely refine it. Until then, all HTML decks should anchor to the palette + type system below for visual continuity.

The Janus brand visible in Andrew's deck is: **a warm amber/orange primary on cool-gray neutrals, with full-bleed photographic title openers**, a geometric sans-serif (Montserrat) for everything, and a consistent JANUS-logo top-right anchor across content slides. This guideline encodes that into CSS variables and component patterns reusable across decks.

## Colour palette

| Role | Hex | Where it's used |
|---|---|---|
| **Brand orange** | `#F5A623` | Header bands, accent rules, section dividers, primary call-to-action highlights, the brand logo's accent block |
| **Orange — deep** | `#D9881A` | Watermark shading on solid-orange section breaks |
| **Orange — mid** | `#E5971D` | Mid-tone variant for orange-on-orange effects |
| **Ink — primary text** | `#1B1F3A` (or `#000`) | Body text on light backgrounds, deck title text in headers |
| **Cool gray — secondary** | `#8A95A8` | Footer line ("CONFIDENTIAL \| JANUS DIGITAL \| 2026"), slide numbers, deprioritised metadata |
| **Card background — cool tinted** | `#F6F7FA` | Default content-card fill on light slides |
| **Card background — ice tinted** | `#E8ECF4` | Secondary card fill / table row banding |
| **Divider gray** | `#EBEBEB` | Subtle horizontal rules and card borders |
| **Page background** | `#FFFFFF` | Default light slide background |

Treat the orange as the **load-bearing brand cue**. If only one colour can be brand-correct, it's `#F5A623`. The cool grays handle hierarchy below it.

## Typography

**Primary typeface: Montserrat** (extracted from the source PPTX as the dominant non-Calibri font, used for titles and emphasis).

For HTML decks, load Montserrat from Google Fonts at the top of the `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

| Element | Family | Weight | Approx. size |
|---|---|---|---|
| Title-slide headline | Montserrat | 300 (Light) | 56–72px |
| Section-header band (content slide) | Montserrat | 300 (Light) | 36–44px |
| Slide title (Header 1) | Montserrat | 600 (Semibold) | 28–32px |
| Subsection / card title | Montserrat | 700 (Bold) | 14–16px (often UPPERCASE, letterspaced) |
| Body | Montserrat | 400 (Regular) | 14–16px |
| Emphasised body | Montserrat | 600 (Semibold) | inherit |
| Footer / metadata | Montserrat | 500 (Medium) | 10–11px, UPPERCASE, letterspaced 0.18em, in cool-gray `#8A95A8` |

**Fallback stack:** `'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`.

Don't pair Montserrat with a serif unless the slide is explicitly opinion / editorial. The Janus deck stays single-family.

## Logo

- The Janus logo lives top-right on every content slide.
- It's a door-frame glyph (open doorway profile) in orange + light blue/gray, paired with the **JANUS** wordmark in dark ink.
- For HTML decks until a vector file lands in the wiki: leave the top-right reserved for the logo as a placeholder block and replace with the SVG/PNG when available. Don't substitute alternative marks.
- On full-bleed dark slides (e.g., title), the logo flips to a white-on-transparent variant.

## Slide patterns

The source deck uses six recurring layouts. Reach for them in this order before inventing a new shape.

### 1. Title slide — photographic full-bleed

- Dark photographic background (the source uses a Singapore skyline with lightning). For non-Singapore decks, pick a photograph that thematically anchors the content (a building, a city, an instrument, an industrial scene) — never a stock pattern or gradient.
- White text overlay, left-aligned, lower-third of the slide.
- Title in Montserrat Light 56–72px, with the **brand orange used sparingly** as a one-word highlight or version-number accent.
- Version / date line below the title: `v1.0 | 15.05.26` in a smaller, lighter weight.
- Bottom cream footer band: `CONFIDENTIAL | JANUS DIGITAL | 2026` left, slide number right, both in cool-gray.
- Logo top-right, white variant.

### 2. Content slide — orange header band

- Orange header band spanning the full slide width, ~80–100px tall.
- Slide title in the band: Montserrat Light, dark ink (not white), large size.
- White panel top-right for the logo cleanly separated from the orange.
- White body below the header with content blocks.
- Cool-gray footer line at the bottom: `CONFIDENTIAL | JANUS DIGITAL | 2026`.

### 3. Content card / row

- Light cool-gray fill (`#F6F7FA`).
- Orange icon (~28–32px) in a circle or filled shape, left-aligned.
- Bold body text right of the icon with body-text continuation in regular weight.
- Cards stacked vertically with generous spacing.

### 4. Data table

- Orange header row (`#F5A623`) with white text, Montserrat Semibold UPPERCASE small.
- Alternating row banding using `#F6F7FA` and white.
- Borders ultra-light or absent — use spacing instead.
- Numerals can be tabular for column alignment.

### 5. Timeline / Gantt

- Cool-gray gridlines or row separators.
- Bars in `#F5A623` for primary, with secondary roles in mid-blue / green / red kept muted (don't peacock with colour). Status colours from the source deck: muted navy bars + cyan for paid ads, green for "go-live" milestones, red for critical-path. Use sparingly.
- Week-column headers in the orange band.

### 6. Section break / Q&A slide

- Solid orange background.
- Large translucent watermark letters (e.g., "Q&A" at low opacity over the orange) — gives texture without competing.
- Foreground text in white Montserrat Light.

## CSS reference (drop-in block)

Use these CSS variables at the top of any new HTML deck:

```css
:root {
  /* Brand */
  --brand-orange: #F5A623;
  --brand-orange-deep: #D9881A;
  --brand-orange-mid: #E5971D;

  /* Ink */
  --ink: #1B1F3A;
  --ink-soft: #4A5072;
  --ink-mute: #8A95A8;

  /* Surfaces */
  --bg: #FFFFFF;
  --surface: #F6F7FA;
  --surface-cool: #E8ECF4;
  --hair: #EBEBEB;

  /* Footer / metadata */
  --footer-text: #8A95A8;
}

body { font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; color: var(--ink); }
h1, h2, .deck-title { font-weight: 300; letter-spacing: -0.01em; }
h3, .section-label { font-weight: 700; text-transform: uppercase; letter-spacing: 0.16em; }
.footer-meta { color: var(--footer-text); font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase; font-weight: 500; }
```

## What to avoid

- **Don't substitute the orange.** Don't shift to red, gold, or amber-but-different. `#F5A623` is the identity.
- **Don't pair Montserrat with a second display face.** Single-family discipline is part of the look.
- **Don't fill body slides with brand-orange.** Orange is a punctuation, not a background. Section breaks and the header band are the only full-orange surfaces.
- **Don't put text directly on busy photos.** Title slide photos need a darker tonal range (skylines at night, stormy skies) so white text reads cleanly. If the photo is too bright, dim it with a translucent dark overlay rather than fighting it.
- **Don't drop the JANUS logo or the footer line** on content slides — they're the brand signature.

## Provenance + version notes

- **v0.1 — 2026-05-15:** Derived from Andrew's [[2026-05-15-singapore-marketing-launch-plan-v1|Singapore campaign plan v1 PPTX]] by extracting theme colours from `ppt/slides/slide*.xml`, typography from the font table, and layout patterns from rendered slide images. Brand orange `#F5A623` and Montserrat are direct readings from the source deck.
- **Open:** no vector Janus logo currently in the wiki. Add when available; until then, top-right block placeholder.
- **Open:** is `#F5A623` truly the brand orange, or has Andrew chosen it locally for this deck? The Janus website + any future official brand artefacts should reconcile.
- **Open:** what's the company-default typeface (Montserrat across the source PPTX, but Calibri appears in some text frames as a fallback). Future versions of this guideline should commit to one.

Future revisions of this page should bump the version (`v0.2`, `v1.0`, …) and capture the reason for the change. When Andrew or a designer formalises a brand book, this page becomes the bridge between that book and HTML implementation specifically.
