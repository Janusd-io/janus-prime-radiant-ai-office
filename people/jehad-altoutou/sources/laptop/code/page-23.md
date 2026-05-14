---
type: source
source_type: laptop
title: page
slug: page-23
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/leave-requests/[id]/page.tsx"
original_size: 6562
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/leave-requests/[id]/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect, notFound } from "next/navigation";
import Link from "next/link";
import { STATUS_LABEL, STATUS_COLOR } from "@/lib/leave";
import { formatDate, formatTimestamp } from "@/lib/slack";
import { ChevronLeft, FileText } from "lucide-react";
import DeleteRedirect from "./DeleteRedirect";
import MarkViewed from "./MarkViewed";

export const dynamic = "force-dynamic";

export default async function LeaveRequestDetail({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await getSession();
  if (!user) redirect("/admin/login");
  const { id } = await params;

  const r = await prisma.leaveRequest.findUnique({
    where: { id },
    include: { employee: true, lineManager: true },
  });
  if (!r) notFound();

  const emp = r.employee?.fullName || r.employee?.firstName || "Unknown employee";
  const managerName = r.lineManager?.name ?? "(deleted)";

  return (
    <div className="max-w-3xl">
      <MarkViewed id={r.id} alreadyViewed={r.viewedByHr} />
      <Link
        href="/admin/leave-requests"
        className="mb-4 inline-flex items-center gap-1 text-sm text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100"
      >
        <ChevronLeft className="size-4" />
        Back to Leave Requests
      </Link>

      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Leave Request — {emp}</h1>
          <div className="mt-2 flex items-center gap-3">
            <span
              className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${STATUS_COLOR[r.status] || ""}`}
            >
              {STATUS_LABEL[r.status] || r.status}
            </span>
            <span className="text-xs text-muted-foreground">
              Submitted {formatTimestamp(r.createdAt)}
            </span>
          </div>
        </div>
        <div className="flex gap-2">
          <DeleteRedirect id={r.id} employeeName={emp} />
          <Link
            href={`/api/leave/${r.id}/pdf`}
            target="_blank"
            className="inline-flex items-center gap-2 rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 dark:bg-white dark:text-zinc-900 dark:hover:bg-zinc-100"
          >
            <FileText className="size-4" />
            View / Download PDF
          </Link>
        </div>
      </div>

      <div className="space-y-6">
        <Section title="1. Employee Details">
          <Row label="Employee Name" value={emp} />
          <Row label="Department / Team" value={r.department || "—"} />
          <Row label="Date Submitted" value={formatTimestamp(r.employeeSignedAt)} />
        </Section>

        <Section title="2. Leave Details">
          <Row label="Type of Leave" value={r.leaveType} />
          <Row label="Start Date" value={formatDate(r.startDate)} />
          <Row label="End Date" value={formatDate(r.endDate)} />
          <Row
            label="Total Days"
            value={`${r.totalDays} working day${r.totalDays === 1 ? "" : "s"}`}
          />
          <Row label="Reason / Notes" value={r.reason || "—"} multiline />
        </Section>

        <Section title="3. Approval">
          <Row label="Line Manager" value={managerName} />
          <Row
            label="Line Manager Decision"
            value={r.managerDecision ? r.managerDecision.charAt(0).toUpperCase() + r.managerDecision.slice(1) : "Pending"}
          />
          <Row label="Line Manager Comments" value={r.managerComments || "—"} multiline />
          <Row
            label="Line Manager Decision At"
            value={r.managerDecisionAt ? formatTimestamp(r.managerDecisionAt) : "—"}
          />
          <Row
            label="HR Decision"
            value={r.hrDecision ? r.hrDecision.charAt(0).toUpperCase() + r.hrDecision.slice(1) : "Pending"}
          />
          <Row label="HR Comments" value={r.hrComments || "—"} multiline />
          <Row
            label="HR Decision At"
            value={r.hrDecisionAt ? formatTimestamp(r.hrDecisionAt) : "—"}
          />
        </Section>

        <Section title="4. Signatures">
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <Signature
              heading="Employee"
              name={r.employeeSignature}
              date={formatTimestamp(r.employeeSignedAt)}
            />
            <Signature
              heading="Line Manager"
              name={r.managerSignature}
              date={r.managerDecisionAt ? formatTimestamp(r.managerDecisionAt) : null}
            />
            <Signature
              heading="HR"
              name={r.hrSignature}
              date={r.hrDecisionAt ? formatTimestamp(r.hrDecisionAt) : null}
            />
          </div>
        </Section>
      </div>
    </div>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="overflow-hidden rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
      <div className="border-b border-zinc-200 bg-zinc-50 px-4 py-3 text-xs font-semibold uppercase tracking-wide text-zinc-600 dark:border-zinc-800 dark:bg-zinc-950 dark:text-zinc-400">
        {title}
      </div>
      <div className="divide-y divide-zinc-100 dark:divide-zinc-800">{children}</div>
    </div>
  );
}

function Row({ label, value, multiline }: { label: string; value: string; multiline?: boolean }) {
  return (
    <div className="grid grid-cols-3 gap-4 px-4 py-3 text-sm">
      <div className="text-zinc-500">{label}</div>
      <div className={`col-span-2 ${multiline ? "whitespace-pre-wrap" : ""}`}>{value}</div>
    </div>
  );
}

function Signature({
  heading,
  name,
  date,
}: {
  heading: string;
  name: string | null;
  date: string | null;
}) {
  return (
    <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-4 dark:border-zinc-800 dark:bg-zinc-950">
      <div className="text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
        {heading}
      </div>
      <div
        className="mt-2 min-h-[36px] border-b border-zinc-300 pb-2 text-xl dark:border-zinc-700"
        style={{ fontFamily: '"Snell Roundhand","Apple Chancery","Segoe Script",cursive', color: "#1e3a8a" }}
      >
        {name || <span className="text-sm text-zinc-400">Pending</span>}
      </div>
      <div className="mt-2 text-xs text-zinc-500">{date || ""}</div>
    </div>
  );
}

```