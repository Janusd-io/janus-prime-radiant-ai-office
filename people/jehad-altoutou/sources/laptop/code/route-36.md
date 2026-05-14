---
type: source
source_type: laptop
title: Assessify — route
slug: route-36
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/recruitment/applications/[id]/post-score/route.ts"
original_size: 2074
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/recruitment/applications/[id]/post-score/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { getSession } from "@/lib/auth";
import { ingestAndScorePostInterview } from "@/lib/recruitment/post-score-service";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id: applicationId } = await ctx.params;
    const body = (await req.json().catch(() => ({}))) as {
      transcript?: string;
      sourceRef?: string;
      interviewDate?: string;
      interviewer?: string;
      interviewFormat?: string;
      durationMin?: number;
    };

    const report = await ingestAndScorePostInterview({
      applicationId,
      transcript: String(body.transcript ?? ""),
      sourceRef: body.sourceRef ?? null,
      interviewDate: body.interviewDate ?? null,
      interviewer: body.interviewer ?? null,
      interviewFormat: body.interviewFormat ?? null,
      durationMin: body.durationMin,
      actorId: session.id,
      actorEmail: session.email,
      feedbackKind: "interview_transcript",
      ipAddress: req.headers.get("x-forwarded-for"),
    });
    if (!report.report) {
      return Response.json(
        { error: "Transcript saved, but post-interview scoring did not complete. Check Slack/server logs for details." },
        { status: 502 },
      );
    }

    return Response.json({
      ok: true,
      scoreOutOf100: report.report.postScoreOutOf100,
      recommendation: report.report.postRecommendation,
    });
  } catch (error) {
    console.error("POST /api/admin/recruitment/applications/[id]/post-score error:", error);
    const message = error instanceof Error ? error.message : "Internal server error";
    const status =
      message === "Application not found" ? 404 :
      message.includes("cannot score post-interview") ? 409 :
      message.includes("Transcript") || message.includes("notes") ? 400 :
      500;
    return Response.json({ error: message }, { status });
  }
}

```