---
type: source
source_type: laptop
title: route
slug: route-58
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/form-templates/[id]/route.ts"
original_size: 2371
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/form-templates/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// PATCH: update a form template
export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Admin only" }, { status: 403 });

    const { id } = await ctx.params;
    const { name, description, fields, isActive } = (await req.json()) as {
      name?: string;
      description?: string;
      fields?: unknown[];
      isActive?: boolean;
    };

    const data: Record<string, unknown> = {};
    if (name !== undefined) data.name = name.trim();
    if (description !== undefined) data.description = description?.trim() || null;
    if (fields !== undefined) data.fields = JSON.stringify(fields);
    if (isActive !== undefined) data.isActive = isActive;

    await prisma.formTemplate.update({ where: { id }, data });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH /api/admin/form-templates/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// DELETE: delete a form template (only if no submissions)
export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Admin only" }, { status: 403 });

    const { id } = await ctx.params;

    const submissionCount = await prisma.formSubmission.count({ where: { templateId: id } });
    if (submissionCount > 0) {
      return Response.json(
        { error: `Cannot delete: ${submissionCount} submission(s) use this template. Deactivate it instead.` },
        { status: 400 }
      );
    }

    await prisma.formInvite.deleteMany({ where: { templateId: id } });
    await prisma.formTemplate.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/form-templates/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```