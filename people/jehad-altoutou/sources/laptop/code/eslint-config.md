---
type: source
source_type: laptop
title: eslint.config
slug: eslint-config
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/eslint.config.mjs
original_size: 1128
original_ext: .mjs
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:32Z"
---

# eslint.config

_Extracted from `assessify/eslint.config.mjs` on 2026-05-14._

```mjs
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
  {
    // Rule policy:
    //   - Real correctness rules (purity, immutability, exhaustive-deps,
    //     unused vars/expressions) stay as errors — they find actual bugs.
    //   - React Compiler rules that over-flag idiomatic patterns
    //     (set-state-in-effect, static-components) and `no-explicit-any` in
    //     legacy code are demoted to warnings: still surfaced in IDE/CI,
    //     not blocking. Track the warning count over time and pay it down
    //     file-by-file rather than gating every merge on a giant cleanup.
    rules: {
      "react-hooks/set-state-in-effect": "warn",
      "react-hooks/static-components": "warn",
      "@typescript-eslint/no-explicit-any": "warn",
    },
  },
]);

export default eslintConfig;

```