---
type: source
source_type: laptop
title: page
slug: page-22
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/leave-requests/page.tsx
original_size: 7316
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/admin/leave-requests/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import Link from "next/link";
import { STATUS_LABEL, STATUS_COLOR, buildLeaveCalendar } from "@/lib/leave";
import { formatDate, formatTimestamp } from "@/lib/slack";
import DeleteLeaveButton from "./DeleteLeaveButton";
import { TeamLeaveCalendar } from "./TeamLeaveCalendar";

export const dynamic = "force-dynamic";

export default async function LeaveRequestsPage() {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const requests = await prisma.leaveRequest.findMany({
    orderBy: { createdAt: "desc" },
    include: { employee: true, lineManager: true },
  });

  const unreadCount = requests.filter((r) => !r.viewedByHr).length;
  const calendarRequests = requests.filter(
    (request) =>
      request.employee &&
      request.lineManager &&
      request.endDate >= new Date() &&
      ["pending_manager", "pending_hr", "approved"].includes(request.status),
  );
  const calendar = buildLeaveCalendar(
    calendarRequests.map((request) => ({
      id: request.id,
      leaveType: request.leaveType,
      startDate: request.startDate,
      endDate: request.endDate,
      status: request.status,
      employee: {
        fullName: request.employee?.fullName ?? null,
        firstName: request.employee?.firstName ?? "",
      },
      lineManager: {
        id: request.lineManager?.id ?? "",
        name: request.lineManager?.name ?? "Unknown manager",
      },
    })),
  );

  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Leave Requests</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {requests.length} total{unreadCount > 0 ? ` · ${unreadCount} new` : ""}
          </p>
        </div>
        <div className="flex gap-2">
          <Link
            href="/admin/leave-balances"
            className="rounded-lg border border-zinc-200 bg-white px-4 py-2 text-sm font-medium hover:bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800"
          >
            Leave Balances
          </Link>
          <Link
            href="/leave/new"
            target="_blank"
            className="rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 dark:bg-white dark:text-zinc-900 dark:hover:bg-zinc-100"
          >
            Open Form (New Tab)
          </Link>
        </div>
      </div>

      <div className="mb-6">
        <TeamLeaveCalendar
          days={calendar.days}
          rows={calendar.rows}
          overlaps={calendar.overlaps}
          upcoming={calendarRequests
            .slice()
            .sort((a, b) => a.startDate.getTime() - b.startDate.getTime())
            .map((r) => ({
              id: r.id,
              employeeName: r.employee?.fullName || r.employee?.firstName || "Unknown",
              managerName: r.lineManager?.name ?? "Unknown manager",
              leaveType: r.leaveType,
              startDate: r.startDate,
              endDate: r.endDate,
              status: r.status,
              totalDays: r.totalDays,
              department: r.employee?.department ?? r.department ?? null,
            }))}
        />
      </div>

      {requests.length === 0 ? (
        <div className="rounded-xl border border-dashed border-zinc-300 bg-white p-12 text-center dark:border-zinc-700 dark:bg-zinc-900">
          <p className="text-sm text-muted-foreground">
            No leave requests yet. Share the form link:{" "}
            <code className="rounded bg-zinc-100 px-1.5 py-0.5 text-xs dark:bg-zinc-800">
              /leave/new
            </code>
          </p>
        </div>
      ) : (
        <div className="overflow-hidden rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
          <table className="w-full text-sm">
            <thead className="border-b border-zinc-200 bg-zinc-50 text-xs uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
              <tr>
                <th className="px-4 py-3 text-left font-medium">Employee</th>
                <th className="px-4 py-3 text-left font-medium">Type</th>
                <th className="px-4 py-3 text-left font-medium">Dates</th>
                <th className="px-4 py-3 text-left font-medium">Days</th>
                <th className="px-4 py-3 text-left font-medium">Line Manager</th>
                <th className="px-4 py-3 text-left font-medium">Status</th>
                <th className="px-4 py-3 text-left font-medium">Submitted</th>
                <th className="px-4 py-3"></th>
              </tr>
            </thead>
            <tbody>
              {requests.map((r) => (
                <tr
                  key={r.id}
                  className="border-b border-zinc-100 last:border-0 hover:bg-zinc-50/80 dark:border-zinc-800 dark:hover:bg-zinc-800/40"
                >
                  <td className="px-4 py-3">
                    <div className="flex items-center gap-2">
                      {!r.viewedByHr && (
                        <span className="size-2 rounded-full bg-blue-500" title="New / unread" />
                      )}
                      <span className="font-medium">
                        {r.employee?.fullName || r.employee?.firstName || "(deleted)"}
                      </span>
                    </div>
                  </td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">
                    {r.leaveType}
                  </td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">
                    {formatDate(r.startDate)} → {formatDate(r.endDate)}
                  </td>
                  <td className="px-4 py-3">{r.totalDays}</td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">
                    {r.lineManager?.name ?? "(deleted)"}
                  </td>
                  <td className="px-4 py-3">
                    <span
                      className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${STATUS_COLOR[r.status] || ""}`}
                    >
                      {STATUS_LABEL[r.status] || r.status}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-xs text-zinc-500">
                    {formatTimestamp(r.createdAt)}
                  </td>
                  <td className="px-4 py-3">
                    <div className="flex items-center justify-end gap-1">
                      <Link
                        href={`/admin/leave-requests/${r.id}`}
                        className="text-sm font-medium text-blue-600 hover:underline dark:text-blue-400"
                      >
                        View
                      </Link>
                      <DeleteLeaveButton
                        id={r.id}
                        employeeName={r.employee?.fullName || r.employee?.firstName || "Unknown"}
                      />
                    </div>
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

```