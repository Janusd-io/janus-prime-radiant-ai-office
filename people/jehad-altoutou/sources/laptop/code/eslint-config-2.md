---
type: source
source_type: laptop
title: eslint.config
slug: eslint-config-2
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/eslint.config.mjs
original_size: 465
original_ext: .mjs
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# eslint.config

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/eslint.config.mjs` on 2026-05-14._

```mjs
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;

```