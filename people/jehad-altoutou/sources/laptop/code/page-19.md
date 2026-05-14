---
type: source
source_type: laptop
title: page
slug: page-19
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/page.tsx"
original_size: 13231
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect, notFound } from "next/navigation";
import Link from "next/link";
import {
  STAGE_LABEL,
  STAGE_COLOR,
  STATUS_LABEL,
  SCORE_TIER_LABEL,
  SCORE_TIER_COLOR,
  isFullReport,
  isPostInterviewReport,
  type RecruitmentStage,
  type ApplicationStatus,
  type ScoreTier,
  type FullPreScreeningReport,
  type PostInterviewReport as PostInterviewReportShape,
} from "@/lib/recruitment";
import { formatTimestamp } from "@/lib/slack";
import { SendInviteButton } from "./SendInviteButton";
import { ExportPdfButton } from "./ExportPdfButton";
import { PreScreeningReport } from "./PreScreeningReport";
import { PostInterviewScoringButton } from "./PostInterviewScoringButton";
import { PostInterviewReport } from "./PostInterviewReport";

export const dynamic = "force-dynamic";

export default async function ApplicationDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const { id } = await params;
  const application = await prisma.application.findUnique({
    where: { id },
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
      stages: { orderBy: { enteredAt: "desc" } },
      feedback: { orderBy: { createdAt: "desc" } },
      scores: {
        orderBy: { computedAt: "desc" },
        include: { rubric: true },
      },
      invites: { orderBy: { createdAt: "desc" } },
    },
  });

  if (!application) notFound();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <Link
            href="/admin/recruitment"
            className="text-xs text-zinc-500 hover:underline"
          >
            ← Back to pipeline
          </Link>
          <h1 className="mt-1 text-2xl font-bold tracking-tight">
            {application.candidate.firstName} {application.candidate.lastName}
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Applied for {application.jobRole.title} · {application.jobRole.department.name} ·{" "}
            {application.office ?? "no office"}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span
            className={`inline-flex items-center rounded-full px-3 py-1 text-xs font-medium ${STAGE_COLOR[application.currentStage as RecruitmentStage] ?? "bg-zinc-100 text-zinc-700"}`}
          >
            {STAGE_LABEL[application.currentStage as RecruitmentStage] ?? application.currentStage}
          </span>
          <span className="rounded-full bg-zinc-100 px-3 py-1 text-xs font-medium text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
            {STATUS_LABEL[application.status as ApplicationStatus] ?? application.status}
          </span>
          <div className="flex items-center gap-2">
            <ExportPdfButton applicationId={application.id} />
            <PostInterviewScoringButton
              applicationId={application.id}
              currentStage={application.currentStage}
              candidateName={`${application.candidate.firstName} ${application.candidate.lastName}`}
            />
            <SendInviteButton
              applicationId={application.id}
              currentStage={application.currentStage}
              candidateName={`${application.candidate.firstName} ${application.candidate.lastName}`}
              candidateEmail={application.candidate.email}
              roleTitle={application.jobRole.title}
            />
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <Card title="Candidate">
          <Field label="Email" value={application.candidate.email} />
          <Field label="Phone" value={application.candidate.phoneNumber} />
          <Field label="Nationality" value={application.candidate.nationality} />
          <Field label="Notice period" value={application.candidate.noticePeriod} />
          <Field label="LinkedIn" value={application.candidate.linkedinUrl} link />
          <Field label="Source" value={application.source ?? "—"} />
          {application.agencyName && <Field label="Agency" value={application.agencyName} />}
          <Field label="Currently" value={formatEmployment(application.candidate.currentlyEmployed)} />
          <Field label="Location" value={formatLocation(application.candidate.locationStatus)} />
          <Field label="Visa status" value={application.candidate.visaStatus} />
          <Field
            label="Driver's license"
            value={formatYesNo(application.candidate.hasDriversLicense)}
          />
          <Field label="AI tools" value={application.candidate.aiToolsProficiency} />
        </Card>
        <Card title="CV / documents">
          <Field label="CV file" value={application.candidate.cvFileName} />
          <Field
            label="Date CV received"
            value={
              application.cvReceivedAt
                ? formatTimestamp(application.cvReceivedAt)
                : null
            }
            placeholder="(not provided)"
          />
          <Field
            label="Drive file"
            value={application.candidate.cvDriveUrl}
            link
            placeholder="(awaiting Drive upload)"
          />
          <Field
            label="Drive folder"
            value={application.candidate.cvDriveFolderUrl}
            link
            placeholder="(awaiting Drive folder)"
          />
          <Field
            label="Uploaded at"
            value={
              application.candidate.cvUploadedAt
                ? formatTimestamp(application.candidate.cvUploadedAt)
                : null
            }
            placeholder="(pending)"
          />
        </Card>
        <Card title="Scoring">
          <ScoreRow
            label="Pre-interview"
            score={application.preScore}
            tier={application.preScoreTier as ScoreTier | null}
          />
          <ScoreRow
            label="Post-interview"
            score={application.postScore}
            tier={application.postScoreTier as ScoreTier | null}
          />
          {application.scores.length > 0 && (
            <details className="mt-3">
              <summary className="cursor-pointer text-xs text-zinc-500">
                Score history ({application.scores.length})
              </summary>
              <ul className="mt-2 space-y-2 text-xs">
                {application.scores.map((s) => (
                  <li key={s.id} className="rounded border border-zinc-200 p-2 dark:border-zinc-700">
                    <div className="flex items-center justify-between">
                      <span className="font-medium">{s.rubric.name}</span>
                      <span>{(s.score * 100).toFixed(0)}%</span>
                    </div>
                    <div className="text-zinc-500">
                      {s.kind} · {formatTimestamp(s.computedAt)} · {s.computedBy ?? "—"}
                    </div>
                  </li>
                ))}
              </ul>
            </details>
          )}
        </Card>
      </div>

      {(() => {
        // Find the most recent pre_interview score that has a full HR-shape report.
        const latestPre = application.scores.find((s) => s.kind === "pre_interview");
        if (!latestPre) return null;
        let parsed: unknown = null;
        try { parsed = JSON.parse(latestPre.breakdown); } catch { parsed = null; }
        if (!isFullReport(parsed)) return null;
        return <PreScreeningReport report={parsed as FullPreScreeningReport} />;
      })()}

      {(() => {
        const latestPost = application.scores.find((s) => s.kind === "post_interview");
        if (!latestPost) return null;
        let parsed: unknown = null;
        try { parsed = JSON.parse(latestPost.breakdown); } catch { parsed = null; }
        if (!isPostInterviewReport(parsed)) return null;
        return <PostInterviewReport report={parsed as PostInterviewReportShape} />;
      })()}

      <Card title="Stage history">
        {application.stages.length === 0 ? (
          <p className="text-sm text-zinc-500">No stage transitions yet.</p>
        ) : (
          <ol className="space-y-2 text-sm">
            {application.stages.map((s) => (
              <li
                key={s.id}
                className="flex items-start justify-between rounded border border-zinc-200 p-2 dark:border-zinc-700"
              >
                <div>
                  <div className="font-medium">
                    {STAGE_LABEL[s.stage as RecruitmentStage] ?? s.stage}
                  </div>
                  {s.notes && <div className="text-xs text-zinc-500">{s.notes}</div>}
                </div>
                <div className="text-xs text-zinc-500">{formatTimestamp(s.enteredAt)}</div>
              </li>
            ))}
          </ol>
        )}
      </Card>

      <Card title="Feedback &amp; notes">
        {application.feedback.length === 0 ? (
          <p className="text-sm text-zinc-500">No feedback yet. Use MCP tools to add.</p>
        ) : (
          <ul className="space-y-2 text-sm">
            {application.feedback.map((f) => (
              <li key={f.id} className="rounded border border-zinc-200 p-3 dark:border-zinc-700">
                <div className="flex items-center justify-between text-xs text-zinc-500">
                  <span>
                    {f.kind}
                    {f.score != null ? ` · ${f.score}/5` : ""}
                  </span>
                  <span>{formatTimestamp(f.createdAt)}</span>
                </div>
                <p className="mt-1 whitespace-pre-wrap">{f.content}</p>
              </li>
            ))}
          </ul>
        )}
      </Card>

      <Card title="Assessment invites">
        {application.invites.length === 0 ? (
          <p className="text-sm text-zinc-500">
            No assessment invites linked yet. The &quot;Send Interview Invite&quot; action ships in Phase 1.B.
          </p>
        ) : (
          <ul className="space-y-2 text-sm">
            {application.invites.map((inv) => (
              <li key={inv.id} className="rounded border border-zinc-200 p-3 dark:border-zinc-700">
                <div className="flex items-center justify-between">
                  <span className="font-medium">{inv.code}</span>
                  <span className="text-xs">{inv.status}</span>
                </div>
                <div className="text-xs text-zinc-500">{formatTimestamp(inv.createdAt)}</div>
              </li>
            ))}
          </ul>
        )}
      </Card>
    </div>
  );
}

function Card({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
      <h2 className="mb-3 text-sm font-semibold tracking-tight">{title}</h2>
      <div className="space-y-2">{children}</div>
    </section>
  );
}

function Field({
  label,
  value,
  link,
  placeholder,
}: {
  label: string;
  value: string | null | undefined;
  link?: boolean;
  placeholder?: string;
}) {
  const v = value && value.length > 0 ? value : null;
  return (
    <div className="flex items-start justify-between gap-3 text-xs">
      <span className="text-zinc-500">{label}</span>
      {v ? (
        link ? (
          <a
            href={v}
            target="_blank"
            rel="noreferrer"
            className="max-w-[60%] truncate text-blue-600 hover:underline dark:text-blue-400"
            title={v}
          >
            {v}
          </a>
        ) : (
          <span className="max-w-[60%] truncate text-right" title={v}>
            {v}
          </span>
        )
      ) : (
        <span className="text-zinc-400">{placeholder ?? "—"}</span>
      )}
    </div>
  );
}

function ScoreRow({
  label,
  score,
  tier,
}: {
  label: string;
  score: number | null;
  tier: ScoreTier | null;
}) {
  return (
    <div className="flex items-center justify-between text-xs">
      <span className="text-zinc-500">{label}</span>
      {score != null && tier ? (
        <span
          className={`inline-flex items-center rounded-full px-2 py-0.5 font-medium ${SCORE_TIER_COLOR[tier]}`}
          title={`${(score * 100).toFixed(0)}%`}
        >
          {SCORE_TIER_LABEL[tier]} · {(score * 100).toFixed(0)}%
        </span>
      ) : (
        <span className="text-zinc-400">pending</span>
      )}
    </div>
  );
}

function formatEmployment(v: string | null | undefined): string | null {
  if (!v) return null;
  if (v === "employed") return "Currently employed";
  if (v === "not_working") return "Not working";
  if (v === "freelancing") return "Freelancing";
  return v;
}

function formatLocation(v: string | null | undefined): string | null {
  if (!v) return null;
  if (v === "in_uae") return "In UAE";
  if (v === "outside_uae") return "Outside UAE";
  return v;
}

function formatYesNo(v: boolean | null | undefined): string | null {
  if (v === true) return "Yes";
  if (v === false) return "No";
  return null;
}

```