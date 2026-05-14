---
type: source
source_type: laptop
title: route
slug: route-18
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/recruitment/drive-callback/route.ts
original_size: 3519
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/recruitment/drive-callback/route.ts` on 2026-05-14._

```typescript
// n8n calls this endpoint after it finishes uploading a candidate's CV to
// Google Drive. Phase 1.A: metadata-only patch — sets cvDriveUrl and
// cvDriveFolderUrl on the Candidate. Does NOT advance Application stage.
// Does NOT trigger scoring. Both flows are independent — see plan
// /Users/jehad/.claude/plans/vast-tumbling-glacier.md "Three independent flows".
import { NextRequest } from "next/server";
import crypto from "crypto";
import { prisma } from "@/lib/db";
import { auditLog } from "@/lib/audit";
import { slackAlert } from "@/lib/slack";

const SHARED_SECRET_ENV = "RECRUITMENT_DRIVE_CALLBACK_SECRET";

function verifySignature(rawBody: string, signature: string | null): boolean {
  const secret = process.env[SHARED_SECRET_ENV];
  if (!secret) {
    // No secret configured → reject all callbacks. Forces explicit setup.
    return false;
  }
  if (!signature) return false;
  const expected = crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  // timingSafeEqual requires equal-length buffers
  const a = Buffer.from(expected, "hex");
  const b = Buffer.from(signature, "hex");
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

export async function POST(req: NextRequest) {
  try {
    const rawBody = await req.text();
    const signature = req.headers.get("x-webhook-signature");
    if (!verifySignature(rawBody, signature)) {
      return Response.json({ error: "Invalid signature" }, { status: 401 });
    }

    let body: {
      candidateId?: string;
      cvDriveUrl?: string;
      cvDriveFolderUrl?: string;
      cvFileName?: string;
    };
    try {
      body = JSON.parse(rawBody);
    } catch {
      return Response.json({ error: "Invalid JSON" }, { status: 400 });
    }

    const { candidateId, cvDriveUrl, cvDriveFolderUrl, cvFileName } = body;
    if (!candidateId || (!cvDriveUrl && !cvDriveFolderUrl)) {
      return Response.json(
        { error: "candidateId + at least one of cvDriveUrl/cvDriveFolderUrl required" },
        { status: 400 },
      );
    }

    const existing = await prisma.candidate.findUnique({ where: { id: candidateId } });
    if (!existing) {
      return Response.json({ error: "Candidate not found" }, { status: 404 });
    }

    const updated = await prisma.candidate.update({
      where: { id: candidateId },
      data: {
        cvDriveUrl: cvDriveUrl ?? existing.cvDriveUrl,
        cvDriveFolderUrl: cvDriveFolderUrl ?? existing.cvDriveFolderUrl,
        cvFileName: cvFileName ?? existing.cvFileName,
        cvUploadedAt: cvDriveUrl ? new Date() : existing.cvUploadedAt,
      },
    });

    await auditLog({
      userId: "system:n8n",
      userEmail: "n8n@assessify",
      action: "recruitment.drive.callback",
      targetType: "Candidate",
      targetId: candidateId,
      details: {
        cvDriveUrl: cvDriveUrl ?? null,
        cvDriveFolderUrl: cvDriveFolderUrl ?? null,
        cvFileName: cvFileName ?? null,
      },
      ipAddress: req.headers.get("x-forwarded-for") ?? undefined,
    });

    return Response.json({
      ok: true,
      candidateId: updated.id,
      cvDriveUrl: updated.cvDriveUrl,
      cvDriveFolderUrl: updated.cvDriveFolderUrl,
    });
  } catch (error) {
    console.error("POST /api/recruitment/drive-callback error:", error);
    slackAlert("Recruitment Drive callback failed", error, {
      route: "/api/recruitment/drive-callback",
    });
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```