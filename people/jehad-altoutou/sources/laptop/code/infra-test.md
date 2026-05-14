---
type: source
source_type: laptop
title: infra.test
slug: infra-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/infra.test.ts
original_size: 580
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# infra.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/infra.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { makeDepartment } from "../../../../tests/factories";

describe("test infrastructure", () => {
  it("can write and read from the ephemeral database", async () => {
    const d = await makeDepartment({ name: "Smoke" });
    const found = await prisma.department.findUnique({ where: { id: d.id } });
    expect(found?.name).toBe("Smoke");
  });

  it("starts each test with a clean slate", async () => {
    const count = await prisma.department.count();
    expect(count).toBe(0);
  });
});

```