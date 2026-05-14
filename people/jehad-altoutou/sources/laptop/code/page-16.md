---
type: source
source_type: laptop
title: page
slug: page-16
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/rubrics/page.tsx
original_size: 3348
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/rubrics/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import { RubricDashboard, type RubricRow } from "./RubricDashboard";

export const dynamic = "force-dynamic";

type Criterion = {
  key: string;
  label: string;
  weight: number;
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

function parseCriteria(raw: string): Criterion[] {
  try {
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? (arr as Criterion[]) : [];
  } catch {
    return [];
  }
}

export default async function RubricsPage() {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const [rubrics, scoreGroups, jobRoles] = await Promise.all([
    prisma.recruitmentRubric.findMany({
      include: { jobRole: { include: { department: true } } },
      orderBy: [{ kind: "asc" }, { isActive: "desc" }, { updatedAt: "desc" }],
    }),
    prisma.applicationScore.groupBy({
      by: ["rubricId", "tier"],
      _count: { _all: true },
      _avg: { score: true },
    }),
    prisma.jobRole.findMany({
      where: { isActive: true },
      include: { department: true },
      orderBy: [{ department: { name: "asc" } }, { title: "asc" }],
    }),
  ]);

  // Build per-rubric { count by tier, avg score } from grouped results.
  type Tier = RubricRow["tierCounts"] extends Record<infer T, number> ? T : never;
  const TIER_KEYS: Tier[] = ["strong_match", "match", "consider", "weak", "reject"];
  const emptyTierCounts = (): Record<Tier, number> =>
    TIER_KEYS.reduce((acc, k) => ({ ...acc, [k]: 0 }), {} as Record<Tier, number>);

  type StatBucket = {
    tierCounts: Record<Tier, number>;
    weightedSum: number; // sum(avg * count) → divide by total
    total: number;
  };
  const statsByRubric = new Map<string, StatBucket>();
  for (const g of scoreGroups) {
    const bucket = statsByRubric.get(g.rubricId) ?? {
      tierCounts: emptyTierCounts(),
      weightedSum: 0,
      total: 0,
    };
    const tier = TIER_KEYS.includes(g.tier as Tier) ? (g.tier as Tier) : null;
    const count = g._count._all;
    if (tier) bucket.tierCounts[tier] = (bucket.tierCounts[tier] ?? 0) + count;
    bucket.weightedSum += (g._avg.score ?? 0) * count;
    bucket.total += count;
    statsByRubric.set(g.rubricId, bucket);
  }

  const rows: RubricRow[] = rubrics.map((r) => {
    const bucket = statsByRubric.get(r.id);
    return {
      id: r.id,
      name: r.name,
      kind: r.kind as "pre_interview" | "post_interview",
      jobRoleId: r.jobRoleId,
      jobRoleLabel: r.jobRole
        ? `${r.jobRole.department.name} → ${r.jobRole.title}`
        : null,
      isActive: r.isActive,
      version: r.version,
      criteria: parseCriteria(r.criteria),
      thresholdStrong: r.thresholdStrong,
      thresholdMatch: r.thresholdMatch,
      thresholdConsider: r.thresholdConsider,
      scoreCount: bucket?.total ?? 0,
      avgScore: bucket && bucket.total > 0 ? bucket.weightedSum / bucket.total : null,
      tierCounts: bucket?.tierCounts ?? emptyTierCounts(),
      updatedAt: r.updatedAt.toISOString(),
    };
  });

  return (
    <RubricDashboard
      rubrics={rows}
      jobRoles={jobRoles.map((j) => ({
        id: j.id,
        title: j.title,
        department: j.department.name,
      }))}
    />
  );
}

```