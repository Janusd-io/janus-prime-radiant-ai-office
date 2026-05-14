---
type: source
source_type: laptop
title: vitest.config
slug: vitest-config
created: 2026-04-27
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/vitest.config.ts
original_size: 572
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:32Z"
---

# vitest.config

_Extracted from `[[assessify|assessify]]/vitest.config.ts` on 2026-05-14._

```typescript
import { defineConfig } from "vitest/config";
import path from "node:path";

export default defineConfig({
  test: {
    environment: "node",
    globals: false,
    include: ["src/**/*.test.ts", "tests/**/*.test.ts"],
    setupFiles: ["./tests/setup.ts"],
    // Tests share an ephemeral SQLite file per worker; run sequentially within
    // a worker so we can truncate between tests without locking issues.
    pool: "forks",
    fileParallelism: false,
    testTimeout: 15_000,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});

```