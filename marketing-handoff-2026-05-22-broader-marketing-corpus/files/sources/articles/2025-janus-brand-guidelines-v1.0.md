---
type: source
title: "Janus Brand Guidelines — Version 1.0 (2025)"
slug: 2025-janus-brand-guidelines-v1.0
created: 2026-05-15
updated: 2026-05-15
source_type: article
source_format: pdf
source_publisher: Janus Digital
source_published: 2025
source_pages: 32
binary: 2025-janus-brand-guidelines-v1.0.pdf
---

# Janus Brand Guidelines v1.0

Janus Digital's official brand book. 32 pages, PDF. Filed at `sources/articles/2025-janus-brand-guidelines-v1.0.{pdf,md}`. The PDF is the authoritative source for any visual-identity question.

## Five chapters

1. **Brand logo** — visual elements analysis, symbolic interpretation, four logo treatments (horizontal / pure pattern / vertical / grayscale), safe-area construction, 3D explorations.
2. **Colors** — visual tonality, logo color composition (BG + main + 3 sub colors), accent palette (10 named colors with light variants).
3. **Fonts** — Montserrat as the brand typeface (Regular, Italic, SemiBold, SemiBold-Italic), Arial as body fallback. Application examples in left-aligned + center-aligned forms.
4. **Auxiliary graphics** — door-pattern watermark + repeating-icon background pattern.
5. **Application** — work badges, business cards / stationery, T-shirts, doorplate signage, large-format billboards, social-media identity.

## Brand voice strings — **deprecated / do not use**

The brand book carries taglines ("Where Data Meets Destiny"), product-position lines, and a mythological-framing footer line. **These are now stale** per Michael 2026-05-15 — Andrew has an agency lined up to refresh the verbal brand and these lines will be replaced. Use this brand book *only* for logos, fonts, and the colour palette. Do not propagate any of the taglines or voice strings to new artefacts.

## Official colour palette

From brand book page 11 ("Logo color composition"):

| Role | Hex | RGB | CMYK | Brand meaning |
|---|---|---|---|---|
| **Main color** | `#FCB745` | 252/183/69 | 3/37/76/0 | Energy, reality |
| **Sub color 01** | `#000000` | 0/0/0 | 0/0/0/100 | Structure, transition |
| **Sub color 02** | `#013A7D` | 1/58/125 | 100/89/31/0 | Technology, digital space |
| **Sub color 03** | `#028CDC` | 2/140/220 | 79/37/0/0 | (paired with sub-02 in the icon's right rail) |
| **Background** | `#FFFFFF` | 255/255/255 | 0/0/0/0 | Background |

Accent palette from page 12 — 10 named colours, each with a "Light" variant for surfaces / backgrounds:

| Name | Light variant | Saturated |
|---|---|---|
| Yellow | `#FEFFFA` (Light Yellow) | — |
| Gray | `#DBE4EA` (Light Gray) / `#5D676F` (Dark Grey) |
| Green | `#D2FFE1` | `#00D280` |
| Azure | `#C8F5FF` | `#00D0FF` |
| Purple | `#E6D2FF` | `#A263FF` |
| Blue | `#DBEEFF` | `#5699FF` |
| Orange | `#FFE6C8` | `#FF6E00` |
| Red | `#FFDCCD` | `#FF5B45` |

Use the accent palette for chart-and-data visualisations, status colours, or section-by-section colour coding. The core brand identity stays anchored to `#FCB745` + `#013A7D` + `#028CDC` + black/white.

## Typography (brand book pages 15–16)

- **Brand typeface:** **Montserrat** — Regular, Italic, SemiBold, SemiBold Italic (cited specifically as "Title Font"). A free + open-source geometric sans serif designed by Julieta Ulanovsky, inspired by old posters of Montserrat, Buenos Aires.
- **Body fallback:** Arial-Regular (cited specifically as "Body Text").
- Typographic application examples on page 17 (left-aligned and centre-aligned variants) show the signature signature pattern:
  - Small label "Janus Digital"
  - Large bold title (e.g., "Autonomous Intelligence for Real Assets")
  - Smaller caption (e.g., "Data-driven optimization for superior returns on real assets")

## Logo treatments

Four official treatments documented on brand book page 6 + 14:

1. **Horizontal logo** — icon + JANUS wordmark, side-by-side. **This is the main identification.**
2. **Pure pattern logo** — icon only. **Secondary identification.** Used in app icons, small surfaces, work badges.
3. **Vertical logo** — icon over JANUS wordmark, stacked. *Not recommended* — wordmark gets too small.
4. **Grayscale** — for metal plates / hard materials (signage etching).

Page 13 shows four full-colour backgrounds for the horizontal logo: white, brand-orange, black, sub-color navy (#013A7D). Page 14 shows the pattern-only variants on black, dark grey, brand-orange, and navy.

## Brand assets in the wiki

- **PDF:** `sources/articles/2025-janus-brand-guidelines-v1.0.pdf` (this file's binary twin)
- **SVG (white variant):** `assets/branding/janus-logo-white.svg` — horizontal logo, white wordmark + door outline, preserved colour fills for orange door panel and navy/blue accents. Use on dark backgrounds.
- **SVG (black variant):** `assets/branding/janus-logo-black.svg` — same logo, black wordmark + door outline. Use on light backgrounds.
- **Note on the SVG's orange:** The provided SVG file uses `#FCAD2A` for the door panel — a touch darker than the brand book's `#FCB745`. The SVG is the artwork as delivered; the brand book is the authoritative spec for any *new* colour application. Keep the SVG fills as-is (don't re-author the artwork); use `#FCB745` everywhere else.

## Implications for downstream surfaces

- HTML decks → [[janus-html-deck-brand-guideline|the HTML deck brand guideline]] now updated to v1.0 with these official values + embedded logo.
- Marketing collateral → Andrew's campaign assets should reconcile against this book (the campaign PPTX used `#F5A623` which is close-but-not-correct).
- Website / future Janus.sg landing pages → palette + Montserrat + tagline ("Where Data Meets Destiny") all applicable.
- ISO documentation, business cards, signage, swag → page 27 onwards covers stationery + doorplate + apparel templates.

## Why this matters

Before this book landed in the wiki, the only available brand reference was Andrew's SG campaign PPTX — a downstream artefact that used a close-but-different orange (`#F5A623` vs `#FCB745`). With the authoritative book in hand, every future HTML deck, document, or external surface should reconcile against the values here, not Andrew's deck. This is also the strongest argument yet for keeping the wiki's `assets/branding/` folder as a stable home for vector brand artefacts so anyone (human or AI) building a Janus surface can grab the real logo in one step.
