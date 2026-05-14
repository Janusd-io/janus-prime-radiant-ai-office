---
type: source
source_type: laptop
title: tsconfig
slug: tsconfig-2
created: 2026-04-09
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/prisma/tsconfig.json
original_size: 182
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
---

# tsconfig

_Extracted from `[[assessify|assessify]]/prisma/tsconfig.json` on 2026-05-14._

```json
{
  "extends": "../tsconfig.json",
  "compilerOptions": {
    "types": ["node"],
    "strict": false
  },
  "include": ["seed.ts", "../src/generated/prisma/**/*"],
  "exclude": []
}

```