---
type: source
source_type: laptop
title: route
slug: route-19
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/recruitment/fireflies-callback/route.ts
original_size: 7135
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/recruitment/[[fireflies|fireflies]]-callback/route.ts` on 2026-05-14._

```typescript
import crypto from "crypto";
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { slackAlert } from "@/lib/slack";
import { ingestAndScorePostInterview } from "@/lib/recruitment/post-score-service";

const SHARED_SECRET_ENV = "RECRUITMENT_FIREFLIES_WEBHOOK_SECRET";

type FirefliesPayload = {
  applicationId?: string;
  candidateEmail?: string;
  candidateName?: string;
  roleSlug?: string;
  roleTitle?: string;
  transcript?: string;
  notes?: string;
  transcriptText?: string;
  sourceRef?: string;
  interviewDate?: string;
  interviewer?: string;
  interviewFormat?: string;
  durationMin?: number;
  meetingId?: string;
  transcriptUrl?: string;
  fireflies?: {
    meetingId?: string;
    transcriptUrl?: string;
    transcript?: string;
    candidateEmail?: string;
    candidateName?: string;
    roleSlug?: string;
    roleTitle?: string;
    interviewDate?: string;
    interviewer?: string;
    interviewFormat?: string;
    durationMin?: number;
  };
};

export async function GET(req: NextRequest) {
  const host = req.headers.get("host") ?? "assessify.janusd.io";
  const protocol = host.includes("localhost") ? "http" : "https";
  const webhookUrl = `${protocol}://${host}/api/recruitment/fireflies-callback`;
  return Response.json({
    ok: true,
    webhookUrl,
    signatureHeader: "x-webhook-signature",
    signatureAlgorithm: "hex(hmac_sha256(rawBody, RECRUITMENT_FIREFLIES_WEBHOOK_SECRET))",
    acceptedFields: [
      "applicationId",
      "candidateEmail",
      "candidateName",
      "roleSlug",
      "roleTitle",
      "transcript | notes | transcriptText",
      "sourceRef | transcriptUrl | meetingId",
      "interviewDate",
      "interviewer",
      "interviewFormat",
      "durationMin",
    ],
  });
}

export async function POST(req: NextRequest) {
  try {
    const rawBody = await req.text();
    const signature = req.headers.get("x-webhook-signature");
    if (!verifySignature(rawBody, signature)) {
      return Response.json({ error: "Invalid signature" }, { status: 401 });
    }

    let body: FirefliesPayload;
    try {
      body = JSON.parse(rawBody) as FirefliesPayload;
    } catch {
      return Response.json({ error: "Invalid JSON" }, { status: 400 });
    }

    const normalized = normalizePayload(body);
    const applicationId = await resolveApplicationId(normalized);
    if (!applicationId) {
      return Response.json(
        {
          error:
            "Could not resolve application automatically. Provide applicationId, or send candidateEmail plus roleSlug/roleTitle.",
        },
        { status: 404 },
      );
    }

    const report = await ingestAndScorePostInterview({
      applicationId,
      transcript: normalized.transcript,
      sourceRef: normalized.sourceRef,
      interviewDate: normalized.interviewDate,
      interviewer: normalized.interviewer,
      interviewFormat: normalized.interviewFormat ?? "Fireflies transcript",
      durationMin: normalized.durationMin,
      actorId: "system:fireflies-webhook",
      actorEmail: "fireflies@assessify",
      feedbackKind: "fireflies_transcript",
      ipAddress: req.headers.get("x-forwarded-for"),
    });
    if (!report.report) {
      return Response.json(
        { error: "Transcript ingested, but post-interview scoring did not complete." },
        { status: 502 },
      );
    }

    return Response.json({
      ok: true,
      applicationId,
      scoreOutOf100: report.report.postScoreOutOf100,
      recommendation: report.report.postRecommendation,
      sourceRef: normalized.sourceRef,
    });
  } catch (error) {
    console.error("POST /api/recruitment/fireflies-callback error:", error);
    await slackAlert("Recruitment Fireflies callback failed", error, {
      route: "/api/recruitment/fireflies-callback",
    }).catch(() => {});
    const message = error instanceof Error ? error.message : "Internal server error";
    const status = message.includes("Transcript") ? 400 : 500;
    return Response.json({ error: message }, { status });
  }
}

function verifySignature(rawBody: string, signature: string | null): boolean {
  const secret = process.env[SHARED_SECRET_ENV];
  if (!secret || !signature) return false;
  const expected = crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  const a = Buffer.from(expected, "hex");
  const b = Buffer.from(signature, "hex");
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

function normalizePayload(payload: FirefliesPayload) {
  const nested = payload.fireflies ?? {};
  const transcript =
    payload.transcript ??
    payload.notes ??
    payload.transcriptText ??
    nested.transcript ??
    "";
  const sourceRef =
    payload.sourceRef ??
    payload.transcriptUrl ??
    nested.transcriptUrl ??
    payload.meetingId ??
    nested.meetingId ??
    "fireflies transcript";

  return {
    applicationId: payload.applicationId?.trim() || null,
    candidateEmail: payload.candidateEmail?.trim().toLowerCase() || nested.candidateEmail?.trim().toLowerCase() || null,
    candidateName: payload.candidateName?.trim() || nested.candidateName?.trim() || null,
    roleSlug: payload.roleSlug?.trim() || nested.roleSlug?.trim() || null,
    roleTitle: payload.roleTitle?.trim() || nested.roleTitle?.trim() || null,
    transcript,
    sourceRef,
    interviewDate: payload.interviewDate ?? nested.interviewDate ?? null,
    interviewer: payload.interviewer ?? nested.interviewer ?? null,
    interviewFormat: payload.interviewFormat ?? nested.interviewFormat ?? "Fireflies transcript",
    durationMin: payload.durationMin ?? nested.durationMin ?? null,
  };
}

async function resolveApplicationId(input: {
  applicationId: string | null;
  candidateEmail: string | null;
  candidateName: string | null;
  roleSlug: string | null;
  roleTitle: string | null;
}) {
  if (input.applicationId) return input.applicationId;

  const where: {
    status: string;
    candidate?: { email?: string; firstName?: string; lastName?: string };
    jobRole?: { slug?: string; title?: string };
  } = { status: "active" };

  if (input.candidateEmail) {
    where.candidate = { email: input.candidateEmail };
  } else if (input.candidateName) {
    const [firstName, ...rest] = input.candidateName.split(/\s+/);
    where.candidate = {
      firstName,
      ...(rest.length > 0 ? { lastName: rest.join(" ") } : {}),
    };
  } else {
    return null;
  }

  if (input.roleSlug) {
    where.jobRole = { slug: input.roleSlug };
  } else if (input.roleTitle) {
    where.jobRole = { title: input.roleTitle };
  }

  const matches = await prisma.application.findMany({
    where,
    include: { candidate: true, jobRole: true },
    orderBy: { appliedAt: "desc" },
    take: 3,
  });

  if (matches.length === 1) return matches[0].id;
  if (matches.length === 0 && input.candidateEmail) {
    const fallback = await prisma.application.findFirst({
      where: {
        status: "active",
        candidate: { email: input.candidateEmail },
      },
      orderBy: { appliedAt: "desc" },
    });
    return fallback?.id ?? null;
  }
  return null;
}

```