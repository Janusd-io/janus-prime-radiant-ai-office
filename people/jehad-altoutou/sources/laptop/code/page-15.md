---
type: source
source_type: laptop
title: page
slug: page-15
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/candidates/[id]/page.tsx"
original_size: 5605
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/admin/recruitment/candidates/[id]/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect, notFound } from "next/navigation";
import Link from "next/link";
import {
  STAGE_LABEL,
  STAGE_COLOR,
  STATUS_LABEL,
  type RecruitmentStage,
  type ApplicationStatus,
} from "@/lib/recruitment";
import { formatTimestamp } from "@/lib/slack";

export const dynamic = "force-dynamic";

export default async function CandidateDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const { id } = await params;
  const candidate = await prisma.candidate.findUnique({
    where: { id },
    include: {
      applications: {
        orderBy: { appliedAt: "desc" },
        include: { jobRole: { include: { department: true } } },
      },
      invites: { orderBy: { createdAt: "desc" }, take: 10 },
    },
  });

  if (!candidate) notFound();

  return (
    <div className="space-y-6">
      <div>
        <Link href="/admin/recruitment/candidates" className="text-xs text-zinc-500 hover:underline">
          ← All candidates
        </Link>
        <h1 className="mt-1 text-2xl font-bold tracking-tight">
          {candidate.firstName} {candidate.lastName}
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          {candidate.email}
          {candidate.office ? ` · ${candidate.office}` : ""}
          {candidate.source === "agency" && candidate.agencyName ? ` · Agency: ${candidate.agencyName}` : ""}
        </p>
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
          <h2 className="mb-3 text-sm font-semibold tracking-tight">Profile</h2>
          <dl className="space-y-2 text-xs">
            <Row label="Phone" value={candidate.phoneNumber} />
            <Row label="Nationality" value={candidate.nationality} />
            <Row label="Notice period" value={candidate.noticePeriod} />
            <Row label="LinkedIn" value={candidate.linkedinUrl} link />
            <Row label="Source" value={candidate.source} />
            {candidate.agencyName && <Row label="Agency" value={candidate.agencyName} />}
            <Row label="Created" value={formatTimestamp(candidate.createdAt)} />
          </dl>
        </section>
        <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
          <h2 className="mb-3 text-sm font-semibold tracking-tight">Documents</h2>
          <dl className="space-y-2 text-xs">
            <Row label="CV file" value={candidate.cvFileName} />
            <Row label="Drive file" value={candidate.cvDriveUrl} link />
            <Row label="Drive folder" value={candidate.cvDriveFolderUrl} link />
            <Row
              label="Uploaded"
              value={candidate.cvUploadedAt ? formatTimestamp(candidate.cvUploadedAt) : null}
            />
          </dl>
        </section>
      </div>

      <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-3 text-sm font-semibold tracking-tight">
          Applications ({candidate.applications.length})
        </h2>
        {candidate.applications.length === 0 ? (
          <p className="text-sm text-zinc-500">No applications yet.</p>
        ) : (
          <ul className="space-y-2">
            {candidate.applications.map((a) => (
              <li
                key={a.id}
                className="flex items-center justify-between rounded border border-zinc-200 p-3 dark:border-zinc-700"
              >
                <div>
                  <Link
                    href={`/admin/recruitment/${a.id}`}
                    className="text-sm font-medium hover:underline"
                  >
                    {a.jobRole.title}
                  </Link>
                  <div className="text-xs text-zinc-500">
                    {a.jobRole.department.name} · {a.office ?? "no office"} · Applied{" "}
                    {formatTimestamp(a.appliedAt)}
                  </div>
                </div>
                <div className="flex items-center gap-2 text-xs">
                  <span
                    className={`inline-flex items-center rounded-full px-2 py-0.5 font-medium ${STAGE_COLOR[a.currentStage as RecruitmentStage] ?? "bg-zinc-100 text-zinc-700"}`}
                  >
                    {STAGE_LABEL[a.currentStage as RecruitmentStage] ?? a.currentStage}
                  </span>
                  <span className="text-zinc-500">
                    {STATUS_LABEL[a.status as ApplicationStatus] ?? a.status}
                  </span>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}

function Row({ label, value, link }: { label: string; value: string | null | undefined; link?: boolean }) {
  return (
    <div className="flex items-start justify-between gap-3">
      <dt className="text-zinc-500">{label}</dt>
      <dd className="max-w-[60%] truncate text-right">
        {value ? (
          link ? (
            <a
              href={value}
              target="_blank"
              rel="noreferrer"
              className="text-blue-600 hover:underline dark:text-blue-400"
            >
              {value}
            </a>
          ) : (
            value
          )
        ) : (
          <span className="text-zinc-400">—</span>
        )}
      </dd>
    </div>
  );
}

```