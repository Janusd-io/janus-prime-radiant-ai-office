---
type: source
source_type: laptop
title: route
slug: route-38
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/departments/route.ts
original_size: 594
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/departments/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const departments = await prisma.department.findMany({
      orderBy: { name: "asc" },
    });
    return Response.json({ departments });
  } catch (error) {
    console.error("GET /api/admin/departments error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```