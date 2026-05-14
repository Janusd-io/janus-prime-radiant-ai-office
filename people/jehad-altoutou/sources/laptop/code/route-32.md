---
type: source
source_type: laptop
title: route
slug: route-32
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/hr-forms/[id]/route.ts"
original_size: 3423
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/hr-forms/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// GET: Full submission detail
export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;

    const submission = await prisma.formSubmission.findUnique({
      where: { id },
      include: {
        template: true,
        files: true,
      },
    });

    if (!submission) {
      return Response.json({ error: "Submission not found" }, { status: 404 });
    }

    return Response.json({
      submission: {
        ...submission,
        formData: JSON.parse(submission.formData),
      },
    });
  } catch (error) {
    console.error("GET /api/admin/hr-forms/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// PATCH: Update review status
export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const { status, reviewNotes } = await req.json();

    const updated = await prisma.formSubmission.update({
      where: { id },
      data: {
        status: status ?? undefined,
        reviewNotes: reviewNotes ?? undefined,
        reviewedAt: status === "reviewed" || status === "flagged" ? new Date() : undefined,
      },
    });

    // Update invite status if reviewing
    if (updated.inviteCode && (status === "reviewed" || status === "flagged")) {
      await prisma.formInvite.updateMany({
        where: { code: updated.inviteCode },
        data: { status: "reviewed" },
      });
    }

    return Response.json({ ok: true, status: updated.status });
  } catch (error) {
    console.error("PATCH /api/admin/hr-forms/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const submission = await prisma.formSubmission.findUnique({ where: { id } });
    if (!submission) {
      return Response.json({ error: "Submission not found" }, { status: 404 });
    }

    // Only allow deleting drafts
    if (submission.status !== "draft") {
      return Response.json(
        { error: "Only draft submissions can be deleted" },
        { status: 400 }
      );
    }

    // Delete files, then submission, then free up the invite
    await prisma.formFile.deleteMany({ where: { submissionId: id } });

    if (submission.inviteCode) {
      await prisma.formInvite.updateMany({
        where: { code: submission.inviteCode },
        data: { status: "pending", submissionId: null },
      });
    }

    await prisma.formSubmission.delete({ where: { id } });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/hr-forms/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```