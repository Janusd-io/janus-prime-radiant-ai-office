---
type: blueprint
tags: [blueprint, design-system, design-md, templates]
---

# DESIGN Templates — Drop Into a New Repo

> Two ready-to-drop `DESIGN.md` templates, one per register (from Twenty's product app vs its marketing site philosophy). **Pick the register per surface**, paste into the new repo, fill the brackets. See [[saas-blueprint-guide]] · [[design-tokens]].

Twenty deliberately runs two visual systems. Don't mix them on one surface.

---

## Template A — PRODUCT register (`DESIGN.md` for the app)

```md
# <App> — DESIGN.md (Product Register)

## Theme
Dense, functional UI on a token system. Light + dark via `.dark` class. Tokens in `globals.css` + tailwind config (see vault [[design-tokens]]).

## Color
Semantic tokens only — never raw hex. Neutrals carry the surface; one accent (indigo) for primary actions and focus. Danger/success/warning/info for status only.

## Spacing & Layout
4px grid (`gap-2` = 8px). Consistent rhythm: section gaps `space-y-6`, element gaps `space-y-3`, card padding `p-4`. App shell = left sidebar (nav) + top bar + optional right side-panel + command menu (Cmd+K).

## Typography
Inter (sans) for everything; DM Mono for IDs/numerics/eyebrows. Sizes: base 16, sm 14.7, lg 19.7. Weights 400/500/600. Hierarchy from scale + weight.

## Components
shadcn/ui themed via tokens. Every interactive element implements hover/focus-visible/active/disabled/loading states (contract in [[design-tokens]]). Empty states = icon + one line + CTA. Tables: inline edit, sort/filter, virtualized if >100 rows.

## Motion
75–300ms, ease-out. Hover transitions on background/border. No bounce, no parallax. Respect prefers-reduced-motion.

## Icons
lucide / @tabler/icons-react, 16px in body, 20px in buttons, stroke 2, aria-hidden when decorative.

## Bans
No hardcoded colors/spacing. No heavy drop shadows. No layout shift on load. No color-only state signals.
```

---

## Template B — EDITORIAL register (`DESIGN.md` for marketing/credibility)

Use for landing, pricing, partner/profile, about — surfaces where *the design itself is the credibility argument*.

```md
# <Site> — DESIGN.md (Editorial Register)

## Philosophy
Restraint. The page reads like a thoughtful indie publication, not a SaaS landing. Typography carries the design; whitespace is a feature.

## Color — Restrained
Tinted neutrals (black/white via CSS vars with alpha tones) carry 90%+. ONE accent ≤10%, often just deep ink for CTAs. No gradients, no glassmorphism, no saturated fills.

## Typography — carries the hierarchy
Serif + sans + mono trio. Hierarchy from SCALE + FAMILY CONTRAST, never from weight (max weight 500, no bold).
- Serif: headlines, names, headline numbers.
- Sans: body, prose, interactive labels.
- Mono: eyebrows, meta, currency labels, tabular numerics (uppercase, letter-spacing 0.06–0.08em).
Body line length 62–75ch.

## Spacing & Layout
4px base. Generous editorial breathing room (section gaps 40–56px). ASYMMETRIC two-column layouts where one column does the heavy lifting — NOT a 12-col bento of identical cards. One opinionated detail per page.

## Motion
Hover 250ms ease-out. Card entrance 700ms cubic-bezier(0.22,1,0.36,1), staggered. No bounce/elastic/parallax. Respect prefers-reduced-motion.

## Accessibility
WCAG AA. Focus ring `outline: 2px solid` (not color shift). Semantic landmarks. Color never the sole carrier of meaning.

## Anti-references (reject — they read as generic AI/SaaS)
Big-number heroes · identical icon-grid cards · gradient text · navy+lime schemes · "supercharge your workflow" copy · "Trusted by Fortune 500" logo strips · bento templates · Vercel-style scroll-pin on every section · stock handshake photos.

## Tonal anchors
Stripe docs (clarity) · Linear marketing (restraint) · print magazine (typography).
```

---

## Choosing the register
| Surface | Register |
|---|---|
| Dashboard, tables, settings, record views | **Product** |
| Landing, pricing, about, public profiles, blog | **Editorial** |

If unsure, ask: *is this surface arguing for credibility (editorial) or operating data (product)?*

## Related
- [[saas-blueprint-guide]] · [[design-tokens]] · [[twenty-crm]]
