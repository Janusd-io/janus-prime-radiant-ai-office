---
type: blueprint
tags: [blueprint, design-system, tokens, tailwind, css]
---

# Design Tokens — Paste-Ready Theme

> Real, copy-paste token values derived from Twenty CRM's theme (`packages/twenty-ui/src/theme/constants`), re-expressed as CSS variables + a Tailwind config for the the SaaS Default Stack (Next.js 15 / Prisma / Clerk / Tailwind+shadcn / Stripe / Resend). **Paste this before building any UI.** After this, never write a raw hex or px in a component. See [[saas-blueprint-guide]].

## Principles (why these values)
- **4px spacing grid** — every gap/padding is a multiple of 4. Kills visual noise.
- **Semantic color names** (`primary`, `secondary`, `tertiary`, `danger`, `success`) not raw hex. Themeable + lint-enforceable.
- **Light/dark share the SAME token names** — only the values swap. Components never branch on theme.
- **Hierarchy from scale + weight contrast** (400/500/600), not from many ad-hoc sizes.
- **Subtle depth** — small shadows + optional glass blur, never heavy drop shadows.
- **Snappy motion** — 75–300ms; nothing janky/bouncy.

## `globals.css` — CSS variables (light + dark)

```css
:root {
  /* gray scale (light) — Twenty gray1..gray12 */
  --gray-1: 255 255 255;   --gray-2: 252 252 252;  --gray-3: 247 247 247;
  --gray-4: 241 241 241;   --gray-5: 235 235 235;  --gray-6: 214 214 214;
  --gray-7: 204 204 204;   --gray-8: 179 179 179;  --gray-9: 153 153 153;
  --gray-10: 131 131 131;  --gray-11: 102 102 102; --gray-12: 51 51 51;

  /* semantic surfaces */
  --background-primary: var(--gray-1);
  --background-secondary: var(--gray-2);
  --background-tertiary: var(--gray-4);
  --background-quaternary: var(--gray-5);

  /* semantic text */
  --text-primary: var(--gray-12);
  --text-secondary: var(--gray-11);
  --text-tertiary: var(--gray-9);
  --text-light: var(--gray-8);
  --text-inverted: var(--gray-1);

  /* borders */
  --border-strong: var(--gray-6);
  --border-medium: var(--gray-5);
  --border-light: var(--gray-4);

  /* accents (Radix Indigo-ish) + semantics */
  --accent: 70 96 213;        /* indigo */
  --accent-hover: 145 154 234;
  --danger: 212 40 35;        /* red */
  --success: 76 162 113;      /* green */
  --warning: 230 115 51;      /* orange */
  --info: 70 96 213;          /* blue */

  /* radius (px) */
  --radius-xs: 2px; --radius-sm: 4px; --radius-md: 8px;
  --radius-xl: 20px; --radius-pill: 999px;

  /* shadows */
  --shadow-light: 0 2px 4px rgb(0 0 0 / 0.04), 0 0 4px rgb(0 0 0 / 0.08);
  --shadow-strong: 2px 4px 16px rgb(0 0 0 / 0.16), 0 2px 4px rgb(0 0 0 / 0.08);
  --shadow-modal: 0 0 8px rgb(0 0 0 / 0.16), 0 8px 64px -16px rgb(0 0 0 / 0.48);

  /* motion */
  --duration-instant: 75ms; --duration-fast: 150ms; --duration-normal: 300ms;
  --ease: cubic-bezier(0.22, 1, 0.36, 1);
}

.dark {
  --gray-1: 23 23 23;   --gray-2: 30 30 30;   --gray-3: 38 38 38;
  --gray-4: 46 46 46;   --gray-5: 56 56 56;   --gray-6: 71 71 71;
  --gray-7: 92 92 92;   --gray-8: 117 117 117; --gray-9: 153 153 153;
  --gray-10: 179 179 179; --gray-11: 204 204 204; --gray-12: 235 235 235;
  /* semantic vars above re-resolve automatically; override accents if needed */
}
```

## `tailwind.config.ts` — map tokens to utilities

```ts
import type { Config } from 'tailwindcss';

const rgb = (v: string) => `rgb(var(${v}) / <alpha-value>)`;

export default {
  darkMode: 'class',
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: rgb('--background-primary'),
          secondary: rgb('--background-secondary'),
          tertiary: rgb('--background-tertiary'),
        },
        foreground: {
          DEFAULT: rgb('--text-primary'),
          secondary: rgb('--text-secondary'),
          tertiary: rgb('--text-tertiary'),
          light: rgb('--text-light'),
          inverted: rgb('--text-inverted'),
        },
        border: {
          DEFAULT: rgb('--border-medium'),
          strong: rgb('--border-strong'),
          light: rgb('--border-light'),
        },
        accent: { DEFAULT: rgb('--accent'), hover: rgb('--accent-hover') },
        danger: rgb('--danger'), success: rgb('--success'),
        warning: rgb('--warning'), info: rgb('--info'),
      },
      // 4px grid: spacing-1 = 4px, spacing-2 = 8px ... Tailwind default already does this.
      borderRadius: {
        xs: 'var(--radius-xs)', sm: 'var(--radius-sm)', md: 'var(--radius-md)',
        xl: 'var(--radius-xl)', pill: 'var(--radius-pill)',
      },
      boxShadow: {
        light: 'var(--shadow-light)', strong: 'var(--shadow-strong)', modal: 'var(--shadow-modal)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['DM Mono', 'monospace'],
        serif: ['var(--font-serif)', 'serif'], // for editorial register only
      },
      fontSize: {
        xs: ['0.85rem', '1.5'], sm: ['0.92rem', '1.5'], base: ['1rem', '1.5'],
        lg: ['1.23rem', '1.3'], xl: ['1.54rem', '1.2'], '2xl': ['1.85rem', '1.1'],
      },
      transitionTimingFunction: { brand: 'var(--ease)' },
      transitionDuration: { instant: '75ms', fast: '150ms', normal: '300ms' },
    },
  },
} satisfies Config;
```

## State-styling contract (apply to every interactive element)
- **hover** → border steps `border` → `border-strong`, or subtle bg tint; transition `background 150ms`.
- **focus-visible** → `outline: 2px solid` accent, `outline-offset: 2px` (never color-only).
- **disabled** → `text-foreground-tertiary`, `pointer-events-none`, `opacity-60`.
- **loading** → skeleton or spinner in place; never layout shift.
- **error** → `border-danger`, `text-danger`, helper text below.
- **empty** → illustration/icon + one-line explanation + primary CTA. Never a blank panel.

## Sizing tokens
Inputs/buttons heights: xs 20 / sm 24 / md 28 / lg 32 px (Twenty values; bump to 32/36/40 for touch-first apps).
Modal widths: sm 300 / md 400 / lg 53% / xl 1200×800. Side panel 500px. Icons (Tabler/lucide) 14/16/20/24, stroke 2.

## ESLint rule to ban raw colors (the enforcement that makes it stick)
Add `no-restricted-syntax` blocking hex literals in `className`/style, or use `eslint-plugin-tailwindcss` + a custom rule. Twenty ships a dedicated `no-hardcoded-colors` lint rule — replicate the intent.

## Related
- [[saas-blueprint-guide]] · [[design-templates]] · [[twenty-crm]]
