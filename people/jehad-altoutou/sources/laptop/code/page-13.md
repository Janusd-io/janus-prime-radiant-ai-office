---
type: source
source_type: laptop
title: page
slug: page-13
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/page.tsx
original_size: 9228
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import Link from "next/link";
import { applyRecruitmentScope } from "@/lib/auth-scope";
import {
  STAGE_LABEL,
  STAGE_COLOR,
  STATUS_LABEL,
  SCORE_TIER_LABEL,
  SCORE_TIER_COLOR,
  type RecruitmentStage,
  type ApplicationStatus,
  type ScoreTier,
} from "@/lib/recruitment";
import { formatTimestamp } from "@/lib/slack";
import { RecruitmentFiltersBar } from "./RecruitmentFiltersBar";

export const dynamic = "force-dynamic";

type SearchParams = {
  stage?: string;
  status?: string;
  source?: string;
  office?: string;
  q?: string;
};

export default async function RecruitmentPipelinePage({
  searchParams,
}: {
  searchParams: Promise<SearchParams>;
}) {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const sp = await searchParams;

  // Build the where clause from filters + scope
  let where: Record<string, unknown> = {};
  if (sp.stage) where.currentStage = sp.stage;
  if (sp.status) where.status = sp.status;
  if (sp.source) where.source = sp.source;
  if (sp.office) where.office = sp.office;
  if (sp.q) {
    where.candidate = {
      OR: [
        { firstName: { contains: sp.q } },
        { lastName: { contains: sp.q } },
        { email: { contains: sp.q } },
        { agencyName: { contains: sp.q } },
      ],
    };
  }
  where = applyRecruitmentScope(
    {
      id: user.id,
      role: user.role,
      office: user.office ?? null,
      scopedDepartments: user.scopedDepartments ?? null,
    },
    where,
  );

  const applications = await prisma.application.findMany({
    where,
    orderBy: { appliedAt: "desc" },
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
    },
    take: 200,
  });

  const stats = {
    total: applications.length,
    active: applications.filter((a) => a.status === "active").length,
    hired: applications.filter((a) => a.status === "closed_hired").length,
  };

  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Recruitment Pipeline</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {stats.total} application{stats.total === 1 ? "" : "s"} · {stats.active} active · {stats.hired} hired
          </p>
        </div>
        <div className="flex gap-2">
          <Link
            href="/admin/recruitment/rubrics"
            className="rounded-lg border border-zinc-200 bg-white px-4 py-2 text-sm font-medium hover:bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800"
          >
            Scoring rubrics
          </Link>
          <Link
            href="/admin/recruitment/candidates"
            className="rounded-lg border border-zinc-200 bg-white px-4 py-2 text-sm font-medium hover:bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800"
          >
            All candidates
          </Link>
        </div>
      </div>

      <RecruitmentFiltersBar initial={sp} />

      {applications.length === 0 ? (
        <div className="rounded-xl border border-dashed border-zinc-300 bg-white p-12 text-center dark:border-zinc-700 dark:bg-zinc-900">
          <p className="text-sm text-muted-foreground">
            No applications match these filters yet. Share the agency intake form or career page to start collecting candidates.
          </p>
        </div>
      ) : (
        <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
          <table className="w-full min-w-[1100px] text-sm">
            <thead className="border-b border-zinc-200 bg-zinc-50 text-[10px] uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
              <tr>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Candidate</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Role</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Dept</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Office</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Source</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Stage</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Pre-score</th>
                <th className="whitespace-nowrap px-3 py-2.5 text-left font-medium">Applied</th>
                <th className="px-3 py-2.5"></th>
              </tr>
            </thead>
            <tbody>
              {applications.map((a) => (
                <tr
                  key={a.id}
                  className="border-b border-zinc-100 last:border-0 hover:bg-zinc-50/80 dark:border-zinc-800 dark:hover:bg-zinc-800/40"
                >
                  <td className="whitespace-nowrap px-3 py-2.5">
                    <Link
                      href={`/admin/recruitment/${a.id}`}
                      className="font-medium hover:underline"
                    >
                      {a.candidate.firstName} {a.candidate.lastName}
                    </Link>
                    <div className="truncate text-xs text-zinc-500" title={a.candidate.email}>
                      {a.candidate.email}
                    </div>
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5 text-zinc-700 dark:text-zinc-300">
                    <div className="max-w-[16rem] truncate" title={a.jobRole.title}>
                      {a.jobRole.title}
                    </div>
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5 text-zinc-600 dark:text-zinc-400">
                    {a.jobRole.department.name}
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5 text-zinc-600 dark:text-zinc-400">
                    {a.office ?? "—"}
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5">
                    <SourceBadge source={a.source} agencyName={a.agencyName} />
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5">
                    <span
                      className={`inline-flex items-center whitespace-nowrap rounded-full px-2 py-0.5 text-xs font-medium ${STAGE_COLOR[a.currentStage as RecruitmentStage] ?? "bg-zinc-100 text-zinc-700"}`}
                    >
                      {STAGE_LABEL[a.currentStage as RecruitmentStage] ?? a.currentStage}
                    </span>
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5">
                    {a.preScore != null && a.preScoreTier ? (
                      <span
                        className={`inline-flex items-center whitespace-nowrap rounded-full px-2 py-0.5 text-xs font-medium ${SCORE_TIER_COLOR[a.preScoreTier as ScoreTier] ?? ""}`}
                        title={`Score: ${(a.preScore * 100).toFixed(0)}% · Status: ${STATUS_LABEL[a.status as ApplicationStatus] ?? a.status}`}
                      >
                        {SCORE_TIER_LABEL[a.preScoreTier as ScoreTier] ?? a.preScoreTier}
                      </span>
                    ) : (
                      <span className="text-xs text-zinc-400">pending</span>
                    )}
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5 text-xs text-zinc-500">
                    {formatTimestamp(a.appliedAt)}
                  </td>
                  <td className="whitespace-nowrap px-3 py-2.5">
                    <Link
                      href={`/admin/recruitment/${a.id}`}
                      className="text-sm font-medium text-blue-600 hover:underline dark:text-blue-400"
                    >
                      View
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function SourceBadge({ source, agencyName }: { source: string | null; agencyName: string | null }) {
  if (source === "agency") {
    const label = agencyName ? `Agency · ${agencyName}` : "Agency";
    return (
      <span
        className="inline-flex max-w-[14rem] items-center truncate rounded-full bg-blue-100 px-2 py-0.5 text-xs font-medium text-blue-900 dark:bg-blue-950 dark:text-blue-200"
        title={label}
      >
        {label}
      </span>
    );
  }
  if (source === "direct" || source === "career_page") {
    return (
      <span className="inline-flex items-center rounded-full bg-green-100 px-2 py-0.5 text-xs font-medium text-green-900 dark:bg-green-950 dark:text-green-200">
        Direct
      </span>
    );
  }
  if (source === "referral") {
    return (
      <span className="inline-flex items-center rounded-full bg-purple-100 px-2 py-0.5 text-xs font-medium text-purple-900 dark:bg-purple-950 dark:text-purple-200">
        Referral
      </span>
    );
  }
  return <span className="text-xs text-zinc-400">—</span>;
}

```