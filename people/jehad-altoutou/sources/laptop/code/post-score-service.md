---
type: source
source_type: laptop
title: post-score-service
slug: post-score-service
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/recruitment/post-score-service.ts
original_size: 3327
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# post-score-service

_Extracted from `[[assessify|assessify]]/src/lib/recruitment/post-score-service.ts` on 2026-05-14._

```typescript
import { auditLog } from "@/lib/audit";
import { prisma } from "@/lib/db";
import { scorePostInterview } from "@/lib/recruitment/post-scoring-agent";
import type { PostInterviewReport } from "@/lib/recruitment";

export const MIN_TRANSCRIPT_LENGTH = 80;
export const MAX_TRANSCRIPT_LENGTH = 120_000;

export type PostInterviewIngestionInput = {
  applicationId: string;
  transcript: string;
  sourceRef?: string | null;
  interviewDate?: string | null;
  interviewer?: string | null;
  interviewFormat?: string | null;
  durationMin?: number | null;
  actorId?: string | null;
  actorEmail?: string | null;
  feedbackKind?: string;
  ipAddress?: string | null;
};

export async function ingestAndScorePostInterview(
  input: PostInterviewIngestionInput,
): Promise<{ report: PostInterviewReport | null; transcriptLength: number }> {
  const transcript = validateTranscript(input.transcript);

  const application = await prisma.application.findUnique({
    where: { id: input.applicationId },
    select: { id: true, status: true },
  });
  if (!application) throw new Error("Application not found");
  if (application.status !== "active") {
    throw new Error(`Application is ${application.status}; cannot score post-interview.`);
  }

  const sourceRef = String(input.sourceRef ?? "").trim() || "manual transcript";
  const durationMin = normalizeDuration(input.durationMin);

  await prisma.applicationFeedback.create({
    data: {
      applicationId: input.applicationId,
      actorId: input.actorId ?? "system:fireflies",
      kind: input.feedbackKind ?? "interview_transcript",
      content: transcript,
    },
  });

  await auditLog({
    userId: input.actorId ?? "system:fireflies",
    userEmail: input.actorEmail ?? "system@assessify",
    action: "recruitment.interview_transcript.ingested",
    targetType: "Application",
    targetId: input.applicationId,
    details: {
      sourceRef,
      interviewDate: input.interviewDate ?? null,
      interviewer: input.interviewer ?? null,
      interviewFormat: input.interviewFormat ?? null,
      durationMin,
      transcriptLength: transcript.length,
      feedbackKind: input.feedbackKind ?? "interview_transcript",
    },
    ipAddress: input.ipAddress ?? undefined,
  });

  const report = await scorePostInterview({
    applicationId: input.applicationId,
    transcript,
    sourceRef,
    interviewDate: input.interviewDate ?? null,
    interviewer: input.interviewer ?? null,
    interviewFormat: input.interviewFormat ?? null,
    durationMin,
    actorId: input.actorId ?? "system:fireflies",
    actorEmail: input.actorEmail ?? "system@assessify",
  });

  return { report, transcriptLength: transcript.length };
}

export function validateTranscript(raw: string): string {
  const transcript = String(raw ?? "").trim();
  if (transcript.length < MIN_TRANSCRIPT_LENGTH) {
    throw new Error(`Transcript or notes must be at least ${MIN_TRANSCRIPT_LENGTH} characters.`);
  }
  if (transcript.length > MAX_TRANSCRIPT_LENGTH) {
    throw new Error(
      `Transcript is too long. Limit is ${MAX_TRANSCRIPT_LENGTH.toLocaleString()} characters.`,
    );
  }
  return transcript;
}

export function normalizeDuration(value: unknown): number | null {
  const numeric = Number(value);
  return Number.isFinite(numeric) && numeric >= 0 ? numeric : null;
}


```