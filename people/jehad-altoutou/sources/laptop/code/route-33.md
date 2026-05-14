---
type: source
source_type: laptop
title: route
slug: route-33
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/recruitment/rubrics/route.ts
original_size: 5876
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/recruitment/rubrics/route.ts` on 2026-05-14._

```typescript
// Phase 1.B v2: rubric authoring API.
// List all RecruitmentRubric rows; create new ones.
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { auditLog } from "@/lib/audit";

const WEIGHT_TOLERANCE = 0.001;

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  const rubrics = await prisma.recruitmentRubric.findMany({
    include: { jobRole: { include: { department: true } } },
    orderBy: [{ kind: "asc" }, { isActive: "desc" }, { updatedAt: "desc" }],
  });
  return Response.json({ rubrics });
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const body = await req.json();
    const validated = validateRubricInput(body);
    if (validated.error) return Response.json({ error: validated.error }, { status: 400 });

    const rubric = await prisma.recruitmentRubric.create({
      data: {
        name: validated.name,
        kind: validated.kind,
        jobRoleId: validated.jobRoleId,
        version: 1,
        isActive: validated.isActive,
        criteria: JSON.stringify(validated.criteria),
        thresholdStrong: validated.thresholdStrong,
        thresholdMatch: validated.thresholdMatch,
        thresholdConsider: validated.thresholdConsider,
      },
    });

    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "recruitment.rubric.create",
      targetType: "RecruitmentRubric",
      targetId: rubric.id,
      details: { name: rubric.name, kind: rubric.kind, jobRoleId: rubric.jobRoleId },
    });

    return Response.json({ rubric }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/recruitment/rubrics error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

type ValidatedRubric = {
  error?: string;
  name: string;
  kind: "pre_interview" | "post_interview";
  jobRoleId: string | null;
  isActive: boolean;
  criteria: Array<{
    key: string;
    label: string;
    weight: number;
    scoringPrompt: string;
    commentaryGuidance?: string;
    redFlagSignals?: string[];
  }>;
  thresholdStrong: number;
  thresholdMatch: number;
  thresholdConsider: number;
};

export function validateRubricInput(body: unknown): ValidatedRubric {
  const empty: ValidatedRubric = {
    name: "",
    kind: "pre_interview",
    jobRoleId: null,
    isActive: true,
    criteria: [],
    thresholdStrong: 0.85,
    thresholdMatch: 0.7,
    thresholdConsider: 0.55,
  };

  if (typeof body !== "object" || body === null) return { ...empty, error: "Invalid body" };
  const b = body as Record<string, unknown>;

  const name = String(b.name ?? "").trim();
  if (!name) return { ...empty, error: "name is required" };

  const kind = String(b.kind ?? "");
  if (kind !== "pre_interview" && kind !== "post_interview") {
    return { ...empty, error: "kind must be 'pre_interview' or 'post_interview'" };
  }

  const jobRoleId = typeof b.jobRoleId === "string" && b.jobRoleId.length > 0 ? b.jobRoleId : null;

  const criteriaRaw = b.criteria;
  if (!Array.isArray(criteriaRaw) || criteriaRaw.length === 0) {
    return { ...empty, error: "criteria must be a non-empty array" };
  }

  const criteria: ValidatedRubric["criteria"] = [];
  let totalWeight = 0;
  for (let i = 0; i < criteriaRaw.length; i++) {
    const c = criteriaRaw[i] as Record<string, unknown>;
    const key = String(c.key ?? "").trim();
    const label = String(c.label ?? "").trim();
    const weightRaw = Number(c.weight);
    const scoringPrompt = String(c.scoringPrompt ?? "").trim();
    if (!key) return { ...empty, error: `criterion ${i}: key is required` };
    if (!label) return { ...empty, error: `criterion ${i}: label is required` };
    if (!Number.isFinite(weightRaw) || weightRaw <= 0 || weightRaw > 1) {
      return { ...empty, error: `criterion ${i}: weight must be a number in (0, 1]` };
    }
    if (!scoringPrompt) return { ...empty, error: `criterion ${i}: scoringPrompt is required` };

    const commentaryGuidance =
      typeof c.commentaryGuidance === "string" ? c.commentaryGuidance.trim() : undefined;
    const redFlagSignals = Array.isArray(c.redFlagSignals)
      ? (c.redFlagSignals as unknown[]).map((s) => String(s).trim()).filter(Boolean)
      : undefined;

    criteria.push({
      key,
      label,
      weight: weightRaw,
      scoringPrompt,
      commentaryGuidance: commentaryGuidance || undefined,
      redFlagSignals: redFlagSignals && redFlagSignals.length > 0 ? redFlagSignals : undefined,
    });
    totalWeight += weightRaw;
  }
  if (Math.abs(totalWeight - 1) > WEIGHT_TOLERANCE) {
    return { ...empty, error: `criterion weights must sum to 1.0 (got ${totalWeight.toFixed(4)})` };
  }
  const keys = new Set(criteria.map((c) => c.key));
  if (keys.size !== criteria.length) {
    return { ...empty, error: "criterion keys must be unique" };
  }

  const thresholdStrong = clamp01(Number(b.thresholdStrong ?? 0.85));
  const thresholdMatch = clamp01(Number(b.thresholdMatch ?? 0.7));
  const thresholdConsider = clamp01(Number(b.thresholdConsider ?? 0.55));
  if (!(thresholdStrong > thresholdMatch && thresholdMatch > thresholdConsider)) {
    return { ...empty, error: "thresholds must satisfy strong > match > consider, all in 0..1" };
  }

  return {
    name,
    kind: kind as "pre_interview" | "post_interview",
    jobRoleId,
    isActive: b.isActive !== false, // default true
    criteria,
    thresholdStrong,
    thresholdMatch,
    thresholdConsider,
  };
}

function clamp01(n: number): number {
  if (!Number.isFinite(n)) return 0;
  return Math.max(0, Math.min(1, n));
}

```