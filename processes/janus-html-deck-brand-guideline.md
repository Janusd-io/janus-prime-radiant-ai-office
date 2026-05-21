---
type: process
title: Janus HTML deck brand guideline (v1.1)
slug: janus-html-deck-brand-guideline
created: 2026-05-15
updated: 2026-05-21
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [2025-janus-brand-guidelines-v1.0, 2026-05-15-singapore-marketing-launch-plan-v1, janus-html-deck-skill-v1.0]
related: [marketing-prime-radiant, andrew-soane, 2026-05-12-html-as-presentation-format-adopted, 2026-05-15-singapore-marketing-launch-plan-v1, 2025-janus-brand-guidelines-v1.0]
---

# Janus HTML deck brand guideline (v1.1)

> **Status:** v1.1, 2026-05-21. Major expansion over v1.0 — adds **required structural elements** (orange header band + top-right logo block on every slide), **typography hierarchy** with responsive `clamp()` values, the **slide-pattern catalog** (10 layout primitives), and the **single-file self-contained workflow** that the `janus-html-deck` skill (v1.0, 2026-05-19) operationalises. Derived from the official [[2025-janus-brand-guidelines-v1.0|Janus brand guidelines PDF]] supplied 2026-05-15 plus the skill bundle uploaded 2026-05-21. Still scoped to **logos, fonts, colour palette, and now visual structure** — verbal brand / taglines / voice remain under refresh by Andrew's agency; do not propagate any taglines from the brand book.
>
> *v1.0 (2026-05-15) → v1.1 (2026-05-21):* the SKILL.md + template.html + example-deck.html files in the [[janus-html-deck-skill-v1.0|janus-html-deck skill bundle]] are now the executable form of this guideline. Snapshots filed at `assets/janus-html-deck/`. v1.1 absorbs the structural rules and slide-pattern catalog from the skill bundle so the guideline page remains the canonical narrative reference.
>
> *v0.1 (superseded 2026-05-15):* preliminary guideline from Andrew's SG campaign-plan PPTX. Used `#F5A623` (wrong) and called out PPTX layout patterns. Do not reuse.

This page tells any deck builder (human or AI) the minimum they need to make a Janus-brand-correct HTML deck. The companion skill (`janus-html-deck`) packages the same content as a callable workflow with working template and example files; this page is the narrative reference both for humans reading the spec and for the skill's own provenance.

## 1. Colour palette

Anchor every Janus surface to these values. The five "core" tokens come from the brand book's *Logo color composition* (page 11); the two neutrals are from its accent palette (page 12).

| Token | Hex | Role |
|---|---|---|
| `--brand-orange` | `#FCB745` | Primary load-bearing accent. Header band, card accents, stat numerals, eyebrows. |
| `--brand-navy` | `#013A7D` | Dark slide background, table header background, accent text. "Technology, digital space." |
| `--brand-blue` | `#028CDC` | Tertiary accent — use sparingly. Data-viz status colours; not the main identity. |
| `--brand-ink` | `#000000` | Primary text on light surfaces. "Structure, transition." |
| `--brand-bg` | `#FFFFFF` | Default light surface. |
| `--ink-soft` | `#5D676F` | Muted text. (Brand-book "Dark Grey".) |
| `--hair` | `#DBE4EA` | Borders, hairlines, subtle dividers. (Brand-book "Light Gray".) |

**Dark slides** use navy `#013A7D` as background, white as primary text, orange as accent. **Light slides** use white background, ink as primary text, orange as accent.

The brand book also defines a 10-colour extended accent palette (greens / blues / oranges / reds / purples with light variants) intended for data-viz and status colours. Use sparingly — the core identity is the seven values above. Full accent table in [[2025-janus-brand-guidelines-v1.0|the brand book source]].

### Note on `#FCAD2A` vs `#FCB745`

The Janus logo SVG hard-codes the door panel as `#FCAD2A` (a slightly different orange than `#FCB745` in the brand palette). Both oranges sit side-by-side in practice — the brand-palette orange owns the header band, eyebrows, accents; the door-panel orange lives only inside the logo SVG. **Preserve `#FCAD2A` as the logo's actual asset value** — don't rewrite it to match `#FCB745`.

## 2. Typography

**Brand typeface: Montserrat.** Load from Google Fonts at the top of any HTML deck. The full cut set the skill uses:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
```

Weights: **300 / 400 / 500 / 600 / 700** plus italics for 400 and 600. Covers the brand book's spec of *Regular / Italic / SemiBold / SemiBold Italic* plus Light (300) for elegant display numerals and Bold (700) for hero titles.

**Recommended font stack:**

```css
font-family: 'Montserrat', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
```

Single-family-with-Arial-fallback honours the brand-book's "Montserrat titles / Arial body" spec while keeping decks self-contained when the CDN isn't reachable.

### Hierarchy (responsive via `clamp()`)

| Token | Weight | Size | Letter-spacing | Use |
|---|---|---|---|---|
| `.title-xl` | 700 | `clamp(2.5rem, 5.5vw, 4.5rem)` | `-0.02em` | Slide-1 hero title only |
| `.title-lg` | 600 | `clamp(1.7rem, 3.2vw, 2.5rem)` | `-0.015em` | Per-slide titles |
| `.lede` | 400 | `clamp(1rem, 1.2vw, 1.1rem)` | normal | Slide intro paragraph (~72ch max) |
| `.body` | 400 | `clamp(0.92rem, 1vw, 1rem)` | normal | Body text |
| `.eyebrow` | 700 | `0.7rem` | `0.16em`–`0.22em` | Uppercase section labels (orange) |
| Big-stat numeral | 300 (or 700) | sized to slide | tight | Stat callout — 300 for elegant, 700 for impact |

The `clamp()` pattern keeps the deck legible at the smallest common projection size (1280×720) without breaking at larger viewports.

## 3. Logo

Two artwork variants are filed in the wiki under `assets/branding/`:

- **`janus-logo-white.svg`** — JANUS wordmark + door outline render white; orange door panel + navy / bright-blue accents preserved. For dark backgrounds.
- **`janus-logo-black.svg`** — same logo with the wordmark + door outline rendered black. For light backgrounds.

The brand book documents four official treatments (page 6):

1. **Horizontal logo** (icon + wordmark) — **main identification**. Default.
2. **Pure-pattern logo** (icon only) — secondary; favicons, badges, small surfaces.
3. **Vertical logo** (stacked) — *not recommended* per the brand book. Don't use.
4. **Grayscale logo** — for metal plates and hard materials. Not relevant for HTML.

### Embedding the logo — three options

**Option A — Inline `<symbol>` + `<use>` (recommended for HTML decks).** The skill's template ships the logo as a single inline `<symbol id="janus-logo">` defined once at the top of `<body>`, then references it on every slide via `<svg><use href="#janus-logo"/></svg>`. Wordmark colour flips automatically via the `--fill-0` CSS variable:

```css
.logo-block svg { --fill-0: var(--brand-ink); }       /* default: black on light slides */
.slide.dark .logo-block svg { --fill-0: var(--ink-on-dark); }  /* white on dark slides */
```

The door panel (`#FCAD2A`), navy (`#013A7D`), and bright blue (`#028CDC`) accents are baked into the SVG paths and stay constant regardless of wordmark colour. **Do not redraw, substitute, or re-source the logo** — copy the symbol from the template verbatim.

**Option B — `<img>` reference.** Clean for non-deck pages where the SVG file can ship alongside the HTML:

```html
<img src="assets/branding/janus-logo-black.svg" alt="Janus" width="120">
```

**Option C — Pasted inline SVG.** Self-contained even when the HTML moves. Override the wordmark colour by setting `--fill-0` on the `<svg>`:

```html
<svg style="--fill-0: #FFFFFF;" viewBox="0 0 130 45">...</svg>
```

### Logo sizing + placement

- Brand-book safe-area (page 7) reserves space equal to the "J" glyph's height on all sides — for HTML, roughly `padding: 14px`.
- Skill default for content slides: `116×40px` lockup, positioned `top: 3vh; right: 6vw;` absolutely. Top-right is the Janus content-slide convention.
- The brand book itself shows the logo top-left on some pages — both work; pick one and be consistent.

## 4. Required structural elements (every slide)

These three elements appear on **every slide** without exception. They're the consistent brand cue across the deck:

1. **Orange header band.** 6px high, full width, `var(--brand-orange)`, absolutely positioned at the top. Strong continuous brand stripe.
2. **Logo block top-right.** `116×40px`, absolutely positioned at `top: 3vh; right: 6vw;`. Wordmark colour flips automatically based on `.slide.dark`.
3. **Slide title.** Montserrat 600 (`.title-lg`) with tightened letter-spacing. On light slides → ink; on dark slides → white.

Markup pattern repeated on every slide:

```html
<section class="slide">  <!-- add .dark for navy-bg slides -->
  <div class="header-band"></div>
  <div class="logo-block">
    <svg viewBox="0 0 130 45"><use href="#janus-logo"/></svg>
  </div>
  <!-- slide content here -->
</section>
```

## 5. Drop-in CSS reference

Paste this block at the top of any new HTML deck. It encodes the brand correctly and matches what the skill's `template.html` ships:

```css
:root {
  /* Official brand palette */
  --brand-orange: #FCB745;
  --brand-navy:   #013A7D;
  --brand-blue:   #028CDC;
  --brand-ink:    #000000;
  --brand-bg:     #FFFFFF;
  --ink-soft:     #5D676F;
  --hair:         #DBE4EA;

  /* Deck-specific mappings */
  --bg:           var(--brand-bg);
  --bg-dark:      var(--brand-navy);
  --bg-subtle:    #F7F9FA;
  --bg-orange-soft: #FEF5E0;    /* light orange tint for soft accents */
  --bg-navy-soft:   #E8EEF7;
  --ink:          var(--brand-ink);
  --ink-muted:    var(--ink-soft);
  --ink-faint:    #94A3B8;
  --ink-on-dark:  #FFFFFF;
  --ink-on-dark-muted: #B0B7BD;
  --border:       var(--hair);
  --border-strong: #C5D0D8;

  --font: 'Montserrat', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
}
```

## 6. Slide-pattern catalog

The `janus-html-deck` skill's `references/example-deck.html` ships a fully-built reference deck demonstrating every pattern below. A snapshot lives at `assets/janus-html-deck/example-deck.html` for inspection. Copy the markup for whichever pattern fits the slide you're building.

| # | Pattern | When to use |
|---|---|---|
| 1 | **Title hero (dark)** | Slide 1. Navy background, accent bar, `.title-xl`, orange italic subtitle, author/date/status footer. |
| 2 | **Three-card icon grid** | Constraints / pillars / capabilities — three parallel items at the same level of abstraction. |
| 3 | **Two-column with proof boxes** | "What's changed" — claim on one side, proof / evidence box on the other. |
| 4 | **Two-path comparison** | Neutral vs accent-tinted columns to contrast options or before/after. |
| 5 | **Big stat callout** | Single hero number + implication panel. Use Light (300) weight for elegant numerals or Bold (700) for impact. |
| 6 | **Numbered framework cards** | 3–5 sequential lenses or steps; top-border + circle badge per card. |
| 7 | **Stack table** | Many-row tables; navy header, tightened cell padding to fit dense rows on a single slide. |
| 8 | **Four-step timeline** | Linear progression — numbered circles connected by a dashed orange line. |
| 9 | **Icon row list** | 4–6 items at the same level; circular icon container + title + body per row. |
| 10 | **Closing dark slide with numbered asks** | Final ask / call to action; large orange numerals on dark background. |

Layout, visual motifs, and slide structure are **open** beyond these patterns. Anything that serves the content while keeping the brand surface (palette + typography + logo + header band) intact is fine. Copy and adapt; don't invent new patterns where one of the ten already fits.

## 7. Workflow for building a deck

1. **Start from the skill's `references/template.html`** (snapshot at `assets/janus-html-deck/template.html`). Copy to your working location. It ships with the CSS variables block, the inline SVG logo symbol, the keyboard navigation script, two example slides (one dark, one light), and a print stylesheet for PDF export at 1280×720.

2. **Reference `references/example-deck.html`** (snapshot at `assets/janus-html-deck/example-deck.html`) for the slide-pattern markup. Copy the pattern that fits.

3. **Apply content.** Keep slide count modest — **8–12 slides** is the sweet spot for executive decks. Each slide should make one clear point. If a slide has more than three bullet-equivalents, split it.

4. **Test before delivering.** Open the HTML file in a browser and check:
   - Arrow keys / space / PageDown advance slides; Home / End jump to first / last; `#3` URL hash deep-links to slide 3.
   - Content fits at 1280×720 (smallest common projection size).
   - No content overflow into footer or off-screen at standard viewport heights.
   - Logo flips colour correctly on dark vs light slides.
   - Header band visible at the very top of every slide.

5. **Deliver as a single file.** Self-contained. No external asset folder needed — fonts come via Google Fonts CDN, logo is embedded as an inline SVG symbol, all CSS and JS inlined in `<head>` / `<body>`.

## 8. What NOT to do

Per Janus brand guideline v1.0 + skill v1.0:

- **No taglines from the brand book.** "Where Data Meets Destiny", "God of all beginnings…" — stale, will be replaced by the agency refresh.
- **No reuse of the brand book's example slide layouts as templates.** Letterheads, billboards, T-shirts shown in the book are illustrative, not canonical patterns.
- **No logo substitution or redraw.** Use the embedded SVG symbol from `template.html` verbatim.
- **No fonts other than Montserrat.** Arial is the fallback only.
- **No colours outside the brand palette** for the main identity. The brand-book extended accent palette (greens, reds, purples) is reserved for data-viz status colours, sparingly.
- **No omitting the header band or top-right logo.** Both appear on every slide — that's the brand surface.

## 9. Cross-environment notes

The skill produces a single self-contained HTML file that runs anywhere modern HTML runs:

- **Claude Chat (web / desktop / mobile):** Build via `create_file`, present via `present_files`. Open in browser to preview. Optional: render to images via `playwright` / `puppeteer` for visual QA if `bash` is available.
- **Claude Code:** Build via file tools, validate by opening in browser.
- **Cowork:** Build the file directly. No rendering or QA tools required to produce a brand-correct output; the patterns in `example-deck.html` are pre-validated.

The deck itself runs on any browser — laptop, projector, mobile preview. Print to PDF via browser print dialog; the print stylesheet formats it to 1280×720 pages.

## 10. Relationship to the `janus-html-deck` skill

This page (the brand guideline) and the `janus-html-deck` skill are **the same content in two forms**:

- **Guideline (this page)** — narrative reference. Spec for humans reading the brand, plus the canonical version-history. Survives across skill bundle changes.
- **Skill (`janus-html-deck` v1.0)** — executable workflow. SKILL.md plus the working `template.html` and `example-deck.html` files that a Claude session can read and copy from. Operationalises the guideline as a callable verb.

When the agency brand refresh lands, both versions move forward together: the guideline gets a v1.2 / v2.0 narrative bump documenting the deltas; the skill gets new artefacts (updated palette in `template.html`, swapped logo SVG, possibly new patterns in `example-deck.html`) and bumps its own version. The two stay in sync. Snapshots at `assets/janus-html-deck/` give the wiki a viewable copy independent of the skill bundle's local installation.

## 11. Provenance + version notes

- **v1.1 (2026-05-21):** absorbs the `janus-html-deck` skill bundle (v1.0, 2026-05-19) — adds required structural elements (header band + logo block), typography hierarchy with `clamp()` responsive values, slide-pattern catalog (10 patterns), single-file workflow, the `#FCAD2A` vs `#FCB745` note, expanded deck-specific CSS variable mappings, and the §10 guideline-and-skill relationship framing. Snapshots of `SKILL.md`, `template.html`, `example-deck.html` filed at `assets/janus-html-deck/`.
- **v1.0 (2026-05-15):** derived from the official [[2025-janus-brand-guidelines-v1.0|Janus brand book]] (PDF, 32 pages, version 1.0 dated 2025). Logos saved as SVGs at `assets/branding/`. Palette / fonts / logo treatments extracted directly from the brand book. Scope narrowed to logos / fonts / colours per Michael's instruction. The preliminary v0.1 (Andrew SG PPTX-derived; used `#F5A623`) is superseded.
- **Future:** re-version when the marketing agency's brand refresh lands. At minimum the colour palette in `template.html` updates and the logo SVG swaps to new artwork. Slide patterns and structural rules likely carry forward — they're not brand-specific in a way that breaks when the visual identity changes.

## Quick reference card

```
Palette
  Orange     #FCB745   primary accent (header band, eyebrows)
  Navy       #013A7D   dark slides, table header
  Blue       #028CDC   tertiary (data-viz, sparing)
  Ink        #000000   text on light
  BG         #FFFFFF   light surface
  Mute       #5D676F   muted text
  Hair       #DBE4EA   borders
  (Logo door uses #FCAD2A — preserved as asset value, not palette)

Font       Montserrat (300/400/500/600/700 + italics) via Google Fonts CDN
Logo       inline SVG <symbol id="janus-logo"> + <use href="#janus-logo">
           (snapshot artwork at assets/branding/janus-logo-{white,black}.svg)
Required   header-band (6px orange) + logo-block (top-right) on every slide
Format     single self-contained HTML file — no external asset folder

Patterns   10 slide layouts in assets/janus-html-deck/example-deck.html
Workflow   start from assets/janus-html-deck/template.html
Deck size  8-12 slides
Test at    1280×720 (smallest common projection)
```
