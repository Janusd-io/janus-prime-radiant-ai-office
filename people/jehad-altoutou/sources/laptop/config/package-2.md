---
type: source
source_type: laptop
title: Brightbean Studio — package
slug: package-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/package.json
original_size: 203
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

_Extracted from `brightbean-studio/package.json` on 2026-05-14._

```json
{
  "name": "brightbean-studio",
  "private": true,
  "scripts": {
    "heroku-postbuild": "cd theme/static_src && npm ci && npm run build"
  },
  "cacheDirectories": ["theme/static_src/node_modules"]
}

```