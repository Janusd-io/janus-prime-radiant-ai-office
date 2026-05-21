---
name: janus-html-deck
description: Build a Janus-branded HTML presentation as a single self-contained file. Use this skill whenever the user asks to create a deck, slides, or presentation that should follow Janus brand identity — typical triggers include "make a deck for X", "build slides on Y", "create a Janus presentation about Z", "convert this to an HTML deck", or any deck-building request inside the Janus workspace. Covers brand tokens (Montserrat typography, orange/navy/blue/ink palette, inline-SVG logo), required structural elements (orange header band, top-right logo, keyboard navigation), and a catalog of slide layout primitives (title, card grid, big stat callout, comparison columns, table, timeline, icon-row list, closing asks). Pairs with the `janus-html-deck-brand-guideline` document.
---

# Skill: Janus HTML deck

**Version:** 1.0
**Owner:** Michael Bruck, AI Office
**Last Updated:** 2026-05-19
**Scope:** Self-contained single-file HTML decks. No external assets required (fonts via Google Fonts CDN; logo embedded as inline SVG). Works across Claude Chat (web / desktop / mobile), Claude Code, and Cowork — no environment-specific tooling needed to produce a brand-correct output.

---

## When to use this skill

- "Create a deck for [topic]" / "make slides about X" — when context indicates a Janus audience
- "Build an HTML presentation" / "convert this to slides"
- "Create a Janus-branded version of these slides"
- Any deck-building request inside the Janus workspace, by default

Do **not** use this skill for: client-facing decks that must follow a different brand kit; .pptx output (use the public `pptx` skill instead); inline conversational explanations where a visual isn't actually warranted.

---

## What ships with this skill

- `SKILL.md` (this file) — brand tokens, structural rules, workflow
- `references/template.html` — minimal working skeleton (copy and extend)
- `references/example-deck.html` — fully-built reference deck showing every slide pattern in working use. Topic is a generic quarterly-planning approach for a small team — the content is illustrative and topic-neutral; what matters is the patterns it demonstrates.

---

## Brand surface (v1.0)

Source: Janus brand guideline v1.0 (2026-05-15). A refreshed brand kit from the marketing agency is expected; this skill will be re-versioned when it lands. Until then: **logos, fonts, colours — that's the brand surface.** Layout and motif choices are open.

### Colour palette

| Token | Hex | Role |
|---|---|---|
| `--brand-orange` | `#FCB745` | Primary load-bearing accent. Header band, card accents, stat numerals, eyebrows |
| `--brand-navy` | `#013A7D` | Dark slide background, table header background, accent text |
| `--brand-blue` | `#028CDC` | Tertiary accent. Use sparingly — data-viz status colours, not the main identity |
| `--brand-ink` | `#000000` | Primary text on light surfaces |
| `--brand-bg` | `#FFFFFF` | Light surface (default slide background) |
| `--ink-soft` | `#5D676F` | Muted text |
| `--hair` | `#DBE4EA` | Borders, hairlines, subtle dividers |

Dark slides use navy `#013A7D` as background, white as primary text, orange as accent. Light slides use white background, ink as primary text, orange as accent.

### Typography

Single family: **Montserrat** (Google Fonts). Required cuts: 300, 400, 500, 600, 700 plus italics. Loaded at the top of every deck via:

```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
```

Stack:

```css
font-family: 'Montserrat', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif;
```

Hierarchy guide:
- Title-XL (slide 1 hero): 700, `clamp(2.5rem, 5.5vw, 4.5rem)`, letter-spacing `-0.02em`
- Title-LG (slide titles): 600, `clamp(1.7rem, 3.2vw, 2.5rem)`, letter-spacing `-0.015em`
- Body: 400, `clamp(0.92rem, 1vw, 1rem)`, line-height 1.6
- Eyebrow / section labels: 700, uppercase, `letter-spacing: 0.16em` to `0.22em`
- Big stat numeral (e.g. "4–6"): 300 (Light) gives the elegant thin look; 700 (Bold) for impact

### Logo

The Janus logo is embedded as an inline SVG `<symbol>` once per deck (in `references/template.html`, near the top of `<body>`) and referenced via `<use href="#janus-logo">` on each slide. **Do not redraw, substitute, or re-source the logo — copy the symbol from the template verbatim.**

Wordmark colour flips automatically via the `--fill-0` CSS variable:
```css
.logo-block svg          { --fill-0: var(--brand-ink); }       /* default: black on light */
.slide.dark .logo-block svg { --fill-0: var(--ink-on-dark); }  /* white on dark */
```

The door panel (`#FCAD2A`), navy (`#013A7D`), and bright blue (`#028CDC`) accents are baked into the SVG paths and stay constant regardless of wordmark colour.

**Note:** the door panel uses `#FCAD2A` in the SVG, slightly different from `#FCB745` in the brand guideline. Both oranges sit side-by-side; the SVG value is preserved as the actual asset.

---

## Required structural elements (every slide)

These three elements appear on every slide without exception:

1. **Orange header-band stripe.** 6px high, full width, `var(--brand-orange)`, absolute positioned at top. Strong consistent brand cue.
2. **Logo block top-right.** 116×40px, absolute positioned at `top: 3vh; right: 6vw;`. Wordmark colour flips automatically based on `.slide.dark`.
3. **Slide title.** Montserrat 600, letter-spacing tightened. On light slides → ink; on dark slides → white.

Markup pattern repeated on every slide:

```html
<section class="slide">  <!-- add .dark for navy-bg slides -->
  <div class="header-band"></div>
  <div class="logo-block"><svg viewBox="0 0 130 45"><use href="#janus-logo"/></svg></div>
  <!-- slide content here -->
</section>
```

---

## What NOT to do

Per Janus brand guideline v1.0:

- **No taglines from the brand book.** "Where Data Meets Destiny", "God of all beginnings…" — stale, will be replaced by the agency refresh.
- **No reuse of the brand book's example slide-layouts as templates.** Letterheads, billboards, T-shirts shown in the book are illustrative, not canonical patterns.
- **No logo substitution or redraw.** Use the embedded SVG symbol verbatim.
- **No fonts other than Montserrat.** Arial is the fallback only.
- **No colours outside the brand palette** for the main identity. The brand-book accent palette (greens, reds, purples) is reserved for data-viz status colours, sparingly.
- **No `#` prefix on hex in CSS variables** if you're using them in places that don't accept it (most CSS works either way, but the convention here is no `#` in the CSS variable values).

Layout, visual motifs, and slide structure are **open** — anything that serves the content while keeping the brand surface (palette + typography + logo + header band) intact is fine.

---

## Workflow for building a deck

1. **Start from `references/template.html`.** Copy it to your working location. It ships with:
   - CSS variables block (brand tokens, layout helpers, navigation styles)
   - Inline SVG symbol definition for the logo
   - Keyboard navigation script (arrow keys, page up/down, space, Home/End)
   - Two example slides (one dark, one light) demonstrating both modes
   - Print stylesheet for PDF export at 1280×720

2. **Reference `references/example-deck.html` for slide patterns.** It contains real examples of every primitive — copy whichever pattern fits the slide you're building:
   - Title slide (dark hero)
   - 3-card grid (icon + title + body cards)
   - 2-column with proof boxes
   - 2-column path comparison (neutral vs accent-tinted)
   - Big stat callout (large numeral + implication panel)
   - Numbered lens cards (top-border + circle badge)
   - Stack table (navy header, tightened cell padding for many-row tables)
   - 4-step timeline (numbered circles + dashed orange connector)
   - Icon row list (circular icon container + title + body rows)
   - Closing dark slide (numbered asks with large orange numerals)

3. **Apply content.** Keep slide count modest — **8–12 slides** is the sweet spot for executive decks. Each slide should make one clear point. If a slide has more than three bullet-equivalents, split it.

4. **Test before delivering.** Open the HTML file in a browser and check:
   - Navigate with arrow keys — content fits at 1280×720 (smallest common projection size)
   - No content overflow into footer or off-screen at standard viewport heights
   - Logo flips colour correctly on dark vs light slides
   - Header band visible at the very top of every slide

5. **Deliver as a single file.** Self-contained. No external asset folder needed.

---

## Cross-environment notes

This skill produces a single self-contained HTML file that runs anywhere modern HTML runs. The build process is the same regardless of environment:

- **Claude Chat (web / desktop / mobile):** Build via `create_file`, present via `present_files`. Open in browser to preview. If `bash` is available, you can render to images via `playwright` or `puppeteer` for visual QA — but it's optional.
- **Claude Code:** Build via file tools, validate by opening in browser.
- **Cowork:** Build the file directly. No rendering or QA tools required to produce a brand-correct output; the patterns in `example-deck.html` are pre-validated.

The deck itself runs on any browser — laptop, projector, mobile preview. Print to PDF via browser print dialog; the print stylesheet formats it to 1280×720 pages.

---

## Provenance + version notes

- **v1.0 (2026-05-19):** initial release. Encodes the brand surface established in `janus-html-deck-brand-guideline` v1.0 and the slide patterns refined across the first Janus HTML decks (May 2026). Inline SVG symbol pulled from the weekly AIO call deck.
- **Future:** will be re-versioned when the marketing agency's brand refresh lands. At minimum the colour palette in `template.html` updates and the logo SVG swaps to new artwork. Slide patterns and structural rules likely carry forward — they're not brand-specific in a way that breaks when the visual identity changes.

---

## Quick reference card

```
Palette
  Orange     #FCB745   primary accent
  Navy       #013A7D   dark slides + table header
  Blue       #028CDC   tertiary (sparing)
  Ink        #000000   text
  BG         #FFFFFF   light surface
  Mute       #5D676F   muted text
  Hair       #DBE4EA   borders

Font       Montserrat (300/400/500/600/700 + italics)
Logo       inline SVG symbol, ref via <use href="#janus-logo">
Required   header-band + logo-block on every slide
Format     single self-contained HTML file
```
