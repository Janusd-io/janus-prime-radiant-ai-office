---
type: source
source_type: laptop
title: Desktop Captures — utils
slug: utils-3
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/lib/utils.js
original_size: 271
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# utils

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/lib/utils.js` on 2026-05-14._

```javascript
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export const LANGUAGES = [
    'Arabic',
    'English',
    'Russian',
    'Chinese',
    'German',
    'Latin',
    'Spanish'
];

export function cn(...inputs) {
    return twMerge(clsx(inputs));
}

```