---
type: process
title: Janus HTML deck brand guideline (v1.0)
slug: janus-html-deck-brand-guideline
created: 2026-05-15
updated: 2026-05-15
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [2025-janus-brand-guidelines-v1.0, 2026-05-15-singapore-marketing-launch-plan-v1]
related: [marketing-prime-radiant, andrew-soane, 2026-05-12-html-as-presentation-format-adopted, 2026-05-15-singapore-marketing-launch-plan-v1, 2025-janus-brand-guidelines-v1.0]
---

# Janus HTML deck brand guideline (v1.0)

> **Status:** v1.0, 2026-05-15. Derived from the official [[2025-janus-brand-guidelines-v1.0|Janus brand guidelines PDF]] supplied by Michael 2026-05-15. **Scoped narrowly to logos, fonts, and colour palette** per Michael's instruction (verbal brand / taglines / voice are being refreshed by an agency Andrew has lined up; do not propagate any taglines from the brand book — they're stale).
>
> *Supersedes v0.1 (the preliminary guideline derived from Andrew's SG campaign-plan PPTX). The v0.1 orange `#F5A623` was close but wrong — official is `#FCB745`. v0.1 layout patterns and "Janus voice" lines should not be reused.*

This page tells any deck builder (human or AI) the minimum they need to make a Janus-brand-correct HTML deck. Everything else (layout, slide structure, content patterns) is open to judgment.

## 1. Colour palette

Anchor every Janus surface to these five values. They're the brand book's *Logo color composition*, page 11.

| Role | Hex | Brand-book meaning |
|---|---|---|
| **Main / primary** | `#FCB745` | "Energy, reality" — the load-bearing brand cue. If only one colour can be brand-correct, it's this. |
| **Sub-01 / structure** | `#000000` | "Structure, transition" — door outline, primary text. |
| **Sub-02 / depth** | `#013A7D` | "Technology, digital space" — deep-navy companion. |
| **Sub-03 / accent** | `#028CDC` | Bright accent blue — paired with sub-02 in the icon's right rail. |
| **Background** | `#FFFFFF` | Default light surface. |

For greyscale work + body copy, use `#5D676F` (Dark Grey) for de-emphasised text and `#DBE4EA` (Light Gray) for surface tints. Both are from the brand book's accent palette (page 12).

The brand book also defines a 10-colour accent palette (greens / blues / oranges / reds / purples with light variants) for data-viz and status colours. Use sparingly — the core identity is the five values above. Full accent table in [[2025-janus-brand-guidelines-v1.0|the brand book source]].

## 2. Typography

**Brand typeface: Montserrat.** Load from Google Fonts at the top of any HTML deck:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

The brand book specifies four cuts: **Montserrat Regular**, **Montserrat Italic**, **Montserrat SemiBold**, **Montserrat SemiBold Italic**. Cover the same ground in HTML with weights `400` / `400 italic` / `600` / `600 italic`. Add `300` (Light) and `700` (Bold) for title-slide / display use.

**Body text:** the brand book names **Arial** as the body-text fallback. For HTML, the natural pairing is `Montserrat` for everything (titles + body) with Arial as the fallback in the font stack — keeps you single-family while honouring the spec.

**Recommended font stack:**

```css
font-family: 'Montserrat', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
```

## 3. Logo

Two artwork variants are filed in the wiki:

- **`assets/branding/janus-logo-white.svg`** — horizontal logo, JANUS wordmark + door outline render white, orange door panel + navy/blue accents preserved. Use on dark backgrounds.
- **`assets/branding/janus-logo-black.svg`** — same logo, JANUS wordmark + door outline render black. Use on light backgrounds.

The brand book documents four official treatments (page 6):

1. **Horizontal logo** (icon + JANUS wordmark) — **main identification**. Use this by default.
2. **Pure pattern logo** (icon only) — secondary identification. Use for app icons, favicons, badges, anywhere the wordmark would be too small.
3. **Vertical logo** (stacked) — *not recommended* per the brand book. Don't use.
4. **Grayscale logo** — for metal plates / hard materials. Not relevant for HTML.

### Embedding the logo in an HTML deck

Two approaches, pick by deck context:

**Option A — `<img>` reference (clean, requires the SVG file to ship alongside the HTML):**

```html
<img src="assets/branding/janus-logo-black.svg" alt="Janus" width="120">
```

**Option B — inline SVG (self-contained, works even when the HTML moves):**

Paste the SVG contents directly. The wiki's SVGs use `var(--fill-0, white)` (or `#000` in the black variant) for the wordmark + door outline, so you can override via CSS by setting `--fill-0` on the `<svg>` element — handy when you want a single SVG to flip white/black contextually.

```html
<svg style="--fill-0: #FFFFFF;" viewBox="0 0 130 45">...</svg>
```

### Logo sizing + placement

- The brand book's safe-area construction (page 7) reserves space equal to the "J" glyph's height on all sides. For HTML decks, that's roughly `padding: 14px;` around the logo.
- For content slides (typical 1080 × 620 frame), aim for a logo width of `100–130px` with `padding: 14px 22px;` around it.
- Top-right is the conventional Janus content-slide placement (per the source PPTX which followed this convention). The brand book itself shows the logo top-left on some pages — both work; pick one and be consistent across the deck.

## 4. Drop-in CSS reference

Paste this block at the top of any new HTML deck. It encodes the brand correctly:

```css
:root {
  /* Janus brand — official palette */
  --brand-orange: #FCB745;
  --brand-navy: #013A7D;
  --brand-blue: #028CDC;
  --brand-ink: #000000;
  --brand-bg: #FFFFFF;

  /* Accent neutrals (brand-book accent palette, page 12) */
  --ink-soft: #5D676F;          /* Dark Grey */
  --hair: #DBE4EA;              /* Light Gray */
}

body {
  font-family: 'Montserrat', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
  color: var(--brand-ink);
  background: var(--brand-bg);
}

h1, h2, .deck-title { font-weight: 600; letter-spacing: -0.01em; }   /* Montserrat SemiBold for titles */
h3, .section-label { font-weight: 700; text-transform: uppercase; letter-spacing: 0.16em; }
em { font-style: italic; font-weight: 400; }                          /* Montserrat Italic — kept for emphasis */
```

## 5. What's explicitly NOT in scope

Per Michael 2026-05-15, the brand is being formally refreshed by an agency Andrew has engaged. Until that work lands:

- **Don't use any taglines from the brand book.** ("Where Data Meets Destiny" is stale and will be replaced.)
- **Don't use the "Janus is God of all beginnings…" footer line.** Same — stale.
- **Don't reuse the brand book's example slide-layouts as templates.** The book shows letterheads, billboards, T-shirts, business cards as examples. The agency will likely re-do these.
- **Layout / visual-motif choices remain open.** Pick whatever serves the deck content as long as the palette + typography + logo are correct.

This guideline will be re-versioned (v1.1 or v2.0) once the agency work lands. Until then: logos, fonts, colours — that's the brand surface.

## 6. Provenance + version notes

- **v1.0 (2026-05-15):** Derived from the official [[2025-janus-brand-guidelines-v1.0|Janus brand book]] (PDF, 32 pages, version 1.0 dated 2025). Logos saved as SVGs at `assets/branding/`. Palette, fonts, logo treatments all extracted directly from the brand book. Scope narrowed to logos / fonts / colours per Michael's instruction.
- **v0.1 (superseded):** The preliminary guideline derived from Andrew's SG campaign PPTX. Used `#F5A623` (close but wrong) and called out six layout patterns from the PPTX. Layout patterns and tagline references should not be reused.

## Quick reference card

```
Orange     #FCB745
Navy       #013A7D
Blue       #028CDC
Ink        #000000
BG         #FFFFFF
Mute       #5D676F
Hair       #DBE4EA

Font       Montserrat (300/400/500/600/700 + italics)
Logo       assets/branding/janus-logo-{white,black}.svg
```
