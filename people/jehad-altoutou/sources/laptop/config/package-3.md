---
type: source
source_type: laptop
title: Brightbean Studio — package
slug: package-3
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/theme/static_src/package.json
original_size: 359
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# package

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/theme/static_src/package.json` on 2026-05-14._

```json
{
  "name": "brightbean-theme",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "tailwindcss -i ./src/styles.css -o ../static/css/dist/styles.css --watch",
    "build": "tailwindcss -i ./src/styles.css -o ../static/css/dist/styles.css --minify"
  },
  "dependencies": {
    "@tailwindcss/cli": "^4.0.0",
    "tailwindcss": "^4.0.0"
  }
}

```