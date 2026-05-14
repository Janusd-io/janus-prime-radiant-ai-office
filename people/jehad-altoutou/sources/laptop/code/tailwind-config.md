---
type: source
source_type: laptop
title: tailwind.config
slug: tailwind-config
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/theme/static_src/tailwind.config.js
original_size: 544
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# tailwind.config

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/theme/static_src/tailwind.config.js` on 2026-05-14._

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Templates
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    // Theme
    './src/**/*.css',
  ],
  theme: {
    extend: {
      colors: {
        // White-label overridable via CSS custom properties
        brand: {
          primary: 'var(--brand-primary, #4f46e5)',
          'primary-hover': 'var(--brand-primary-hover, #4338ca)',
          secondary: 'var(--brand-secondary, #7c3aed)',
        },
      },
    },
  },
  plugins: [],
}

```