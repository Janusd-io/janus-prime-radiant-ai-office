---
type: source
source_type: laptop
title: route
slug: route-39
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/departments/[id]/route.ts"
original_size: 1365
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/departments/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const body = (await req.json()) as {
      name?: string;
      description?: string;
      defaultInterviewer?: string;
    };

    const trimOrNull = (v: string | undefined | null) => {
      if (v === undefined) return undefined;
      if (v === null) return null;
      const t = v.trim();
      return t.length > 0 ? t : null;
    };

    await prisma.department.update({
      where: { id },
      data: {
        ...(body.name !== undefined && { name: body.name.trim() }),
        ...(body.description !== undefined && {
          description: trimOrNull(body.description),
        }),
        ...(body.defaultInterviewer !== undefined && {
          defaultInterviewer: trimOrNull(body.defaultInterviewer),
        }),
      },
    });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH /api/admin/departments/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```