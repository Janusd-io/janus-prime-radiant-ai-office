---
type: source
source_type: laptop
title: TeamLeaveCalendar
slug: teamleavecalendar
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/leave-requests/TeamLeaveCalendar.tsx
original_size: 17428
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# TeamLeaveCalendar

_Extracted from `[[assessify|assessify]]/src/app/admin/leave-requests/TeamLeaveCalendar.tsx` on 2026-05-14._

```tsx
import { STATUS_LABEL, type LeaveCalendarDay, type LeaveCalendarOverlap, type LeaveCalendarRow } from "@/lib/leave";

export type UpcomingLeave = {
  id: string;
  employeeName: string;
  managerName: string;
  leaveType: string;
  startDate: Date;
  endDate: Date;
  status: string;
  totalDays: number;
  department: string | null;
};

type Props = {
  days: LeaveCalendarDay[];
  rows: LeaveCalendarRow[];
  overlaps: LeaveCalendarOverlap[];
  upcoming: UpcomingLeave[];
};

// ─── Department palette ─────────────────────────────────────────────────────
// 8 distinct colors. Each department gets one deterministically by name-hash;
// unassigned (null) falls back to slot 0. New departments require no code
// changes — the hash auto-distributes them.

const DEPT_PALETTE = [
  { bar: "bg-emerald-200 text-emerald-900 border-emerald-400 dark:bg-emerald-900/40 dark:text-emerald-100 dark:border-emerald-700", dot: "bg-emerald-500" },
  { bar: "bg-blue-200 text-blue-900 border-blue-400 dark:bg-blue-900/40 dark:text-blue-100 dark:border-blue-700",                   dot: "bg-blue-500" },
  { bar: "bg-violet-200 text-violet-900 border-violet-400 dark:bg-violet-900/40 dark:text-violet-100 dark:border-violet-700",       dot: "bg-violet-500" },
  { bar: "bg-amber-200 text-amber-900 border-amber-400 dark:bg-amber-900/40 dark:text-amber-100 dark:border-amber-700",             dot: "bg-amber-500" },
  { bar: "bg-rose-200 text-rose-900 border-rose-400 dark:bg-rose-900/40 dark:text-rose-100 dark:border-rose-700",                   dot: "bg-rose-500" },
  { bar: "bg-cyan-200 text-cyan-900 border-cyan-400 dark:bg-cyan-900/40 dark:text-cyan-100 dark:border-cyan-700",                   dot: "bg-cyan-500" },
  { bar: "bg-pink-200 text-pink-900 border-pink-400 dark:bg-pink-900/40 dark:text-pink-100 dark:border-pink-700",                   dot: "bg-pink-500" },
  { bar: "bg-indigo-200 text-indigo-900 border-indigo-400 dark:bg-indigo-900/40 dark:text-indigo-100 dark:border-indigo-700",       dot: "bg-indigo-500" },
];

function deptIdx(dept: string | null | undefined): number {
  if (!dept) return 0;
  let h = 0;
  for (let i = 0; i < dept.length; i++) h = (h * 31 + dept.charCodeAt(i)) >>> 0;
  return h % DEPT_PALETTE.length;
}

function deptColor(dept: string | null | undefined) {
  return DEPT_PALETTE[deptIdx(dept)];
}

// ─── Helpers ────────────────────────────────────────────────────────────────

function fmtRange(start: Date, end: Date): string {
  const sameMonth = start.getMonth() === end.getMonth() && start.getFullYear() === end.getFullYear();
  const startFmt = start.toLocaleDateString("en-GB", { day: "2-digit", month: "short" });
  const endFmt = end.toLocaleDateString("en-GB", {
    day: "2-digit",
    month: sameMonth ? undefined : "short",
    year: start.getFullYear() !== end.getFullYear() ? "numeric" : undefined,
  });
  return `${startFmt} → ${endFmt}`;
}

function statusPillClass(status: string): string {
  if (status === "approved")
    return "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200";
  if (status === "rejected_manager" || status === "rejected_hr")
    return "bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200";
  return "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200";
}

// Compute non-overlapping "lanes" for a manager's leaves so concurrent leaves
// stack vertically instead of being drawn on top of each other.
function computeLanes(
  leaves: UpcomingLeave[],
  days: LeaveCalendarDay[],
): Array<Array<{ leave: UpcomingLeave; startIdx: number; endIdx: number }>> {
  const sorted = [...leaves].sort((a, b) => a.startDate.getTime() - b.startDate.getTime());
  const lanes: Array<Array<{ leave: UpcomingLeave; startIdx: number; endIdx: number }>> = [];

  for (const leave of sorted) {
    const startMs = new Date(
      leave.startDate.getFullYear(),
      leave.startDate.getMonth(),
      leave.startDate.getDate(),
    ).getTime();
    const endMs = new Date(
      leave.endDate.getFullYear(),
      leave.endDate.getMonth(),
      leave.endDate.getDate(),
      23,
      59,
      59,
    ).getTime();

    let startIdx = -1;
    let endIdx = -1;
    for (let i = 0; i < days.length; i++) {
      const d = days[i].date.getTime();
      if (startIdx === -1 && d >= startMs) startIdx = i;
      if (d <= endMs) endIdx = i;
    }
    if (startIdx === -1 || endIdx < startIdx) continue; // leave is entirely outside the window

    // Greedy lane assignment — first lane whose last bar ends before this leave starts.
    let laneIdx = -1;
    for (let i = 0; i < lanes.length; i++) {
      const last = lanes[i][lanes[i].length - 1];
      if (last.endIdx < startIdx) {
        laneIdx = i;
        break;
      }
    }
    if (laneIdx === -1) {
      laneIdx = lanes.length;
      lanes.push([]);
    }
    lanes[laneIdx].push({ leave, startIdx, endIdx });
  }
  return lanes;
}

// ─── Component ──────────────────────────────────────────────────────────────

export function TeamLeaveCalendar({ days, rows, overlaps, upcoming }: Props) {
  const leavesByManager = new Map<string, UpcomingLeave[]>();
  for (const l of upcoming) {
    const arr = leavesByManager.get(l.managerName) ?? [];
    arr.push(l);
    leavesByManager.set(l.managerName, arr);
  }

  // Distinct departments present in the visible upcoming leaves — drives the legend.
  const distinctDepts = Array.from(
    new Set(upcoming.map((l) => l.department).filter((d): d is string => Boolean(d))),
  ).sort();

  // Pending fill — diagonal striping pattern.
  const pendingStripe =
    "repeating-linear-gradient(45deg, transparent 0, transparent 4px, rgba(0,0,0,0.08) 4px, rgba(0,0,0,0.08) 8px)";

  return (
    <section className="space-y-4 rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <h2 className="text-sm font-semibold tracking-tight">Team Leave Calendar</h2>
          <p className="mt-1 text-xs text-muted-foreground">
            Each bar spans the full leave period. Colors group by department; pending shown striped, approved solid.
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2 text-[11px] text-zinc-500">
          <span className="inline-flex items-center gap-1.5">
            <span className="inline-block h-2 w-4 rounded-sm bg-zinc-400" />
            Approved
          </span>
          <span className="inline-flex items-center gap-1.5">
            <span
              className="inline-block h-2 w-4 rounded-sm bg-zinc-200 dark:bg-zinc-700"
              style={{ backgroundImage: pendingStripe }}
            />
            Pending
          </span>
        </div>
      </div>

      {/* Department legend — dynamic, shows only departments visible right now. */}
      {distinctDepts.length > 0 && (
        <div className="flex flex-wrap items-center gap-3 text-[11px] text-muted-foreground">
          <span className="font-medium text-zinc-500">Departments:</span>
          {distinctDepts.map((dept) => (
            <span key={dept} className="inline-flex items-center gap-1.5">
              <span className={`inline-block h-2.5 w-2.5 rounded-sm ${deptColor(dept).dot}`} />
              {dept}
            </span>
          ))}
          {upcoming.some((l) => !l.department) && (
            <span className="inline-flex items-center gap-1.5">
              <span className={`inline-block h-2.5 w-2.5 rounded-sm ${deptColor(null).dot}`} />
              Unassigned
            </span>
          )}
        </div>
      )}

      {/* Upcoming leaves list */}
      {upcoming.length > 0 ? (
        <div className="rounded-lg border border-zinc-200 bg-zinc-50/50 p-3 dark:border-zinc-800 dark:bg-zinc-900/50">
          <div className="mb-2 flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wide text-zinc-600 dark:text-zinc-300">
              Upcoming Leaves
            </span>
            <span className="text-[10px] text-muted-foreground">
              {upcoming.length} request{upcoming.length === 1 ? "" : "s"}
            </span>
          </div>
          <ul className="divide-y divide-zinc-100 dark:divide-zinc-800">
            {upcoming.map((leave) => (
              <li key={leave.id} className="flex flex-wrap items-center justify-between gap-2 py-1.5 text-xs">
                <div className="min-w-0 flex-1">
                  <div className="flex items-center gap-2 font-medium text-zinc-900 dark:text-zinc-100">
                    <span className={`inline-block h-2.5 w-2.5 shrink-0 rounded-sm ${deptColor(leave.department).dot}`} />
                    {leave.employeeName}
                  </div>
                  <div className="text-[11px] text-muted-foreground">
                    {leave.leaveType} · {leave.totalDays} day{leave.totalDays === 1 ? "" : "s"} · manager: {leave.managerName}
                    {leave.department ? ` · ${leave.department}` : ""}
                  </div>
                </div>
                <div className="flex shrink-0 items-center gap-2">
                  <span className="tabular-nums text-zinc-700 dark:text-zinc-300">
                    {fmtRange(leave.startDate, leave.endDate)}
                  </span>
                  <span className={`rounded-full px-2 py-0.5 text-[10px] font-semibold ${statusPillClass(leave.status)}`}>
                    {STATUS_LABEL[leave.status] ?? leave.status}
                  </span>
                </div>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-3 text-xs text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
          No upcoming approved or pending leaves on the books.
        </div>
      )}

      {/* Overlap alerts */}
      {overlaps.length > 0 && (
        <div className="rounded-lg border border-rose-200 bg-rose-50 p-3 dark:border-rose-900 dark:bg-rose-950/30">
          <div className="mb-2 text-xs font-semibold uppercase tracking-wide text-rose-700 dark:text-rose-300">
            Overlap Alerts
          </div>
          <div className="grid gap-2 md:grid-cols-2">
            {overlaps.map((overlap) => (
              <div key={`${overlap.managerId}-${overlap.dateKey}`} className="rounded-md bg-white/70 px-3 py-2 text-xs dark:bg-zinc-900/60">
                <div className="font-medium text-zinc-900 dark:text-zinc-100">
                  {overlap.managerName} · {overlap.label}
                </div>
                <div className="mt-1 text-zinc-600 dark:text-zinc-300">
                  {overlap.employees.join(", ")}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bar calendar — replaces per-day cell highlighting with continuous bars per leave. */}
      <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
        {/* Month header (row 1) — uppercase month names spanning their date ranges */}
        {(() => {
          // Group consecutive days into month spans
          const monthSpans: Array<{ key: string; label: string; startIdx: number; endIdx: number }> = [];
          for (let i = 0; i < days.length; i++) {
            const d = days[i].date;
            const key = `${d.getFullYear()}-${d.getMonth()}`;
            const last = monthSpans[monthSpans.length - 1];
            if (last && last.key === key) {
              last.endIdx = i;
            } else {
              monthSpans.push({
                key,
                label: d.toLocaleDateString("en-US", { month: "long", year: "numeric" }),
                startIdx: i,
                endIdx: i,
              });
            }
          }
          return (
            <div className="flex border-b border-zinc-200 bg-zinc-100/60 dark:border-zinc-800 dark:bg-zinc-900/60">
              <div className="sticky left-0 z-20 w-48 shrink-0 border-r border-zinc-200 bg-zinc-100/60 px-3 py-1.5 text-[10px] font-semibold uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-900/60">
                Month
              </div>
              <div
                className="grow grid"
                style={{ gridTemplateColumns: `repeat(${days.length}, minmax(28px, 1fr))` }}
              >
                {monthSpans.map((span) => (
                  <div
                    key={span.key}
                    style={{ gridColumn: `${span.startIdx + 1} / ${span.endIdx + 2}` }}
                    className="border-l border-zinc-200 px-2 py-1.5 text-[10px] font-semibold uppercase tracking-wide text-zinc-600 dark:border-zinc-800 dark:text-zinc-300 first:border-l-0"
                  >
                    {span.label}
                  </div>
                ))}
              </div>
            </div>
          );
        })()}

        {/* Day header (row 2) — uniform: weekday letter + day number */}
        <div className="flex border-b border-zinc-200 bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-950">
          <div className="sticky left-0 z-20 w-48 shrink-0 border-r border-zinc-200 bg-zinc-50 px-3 py-2 text-xs font-medium text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
            Line Manager
          </div>
          <div
            className="grow grid"
            style={{ gridTemplateColumns: `repeat(${days.length}, minmax(28px, 1fr))` }}
          >
            {days.map((day, i) => {
              const isWeekStart = day.date.getDay() === 1 && i !== 0;
              return (
                <div
                  key={day.dateKey}
                  className={`flex flex-col items-center justify-center py-1.5 text-[10px] text-zinc-500 dark:text-zinc-400 ${
                    isWeekStart
                      ? "border-l border-zinc-300 dark:border-zinc-700"
                      : "border-l border-zinc-100 dark:border-zinc-900 first:border-l-0"
                  }`}
                >
                  <span className="leading-tight">{day.weekday.charAt(0)}</span>
                  <span className="leading-tight tabular-nums">{day.date.getDate()}</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Manager rows */}
        {rows.length === 0 ? (
          <div className="p-6 text-center text-xs text-muted-foreground">
            No upcoming leaves to display.
          </div>
        ) : (
          rows.map((row) => {
            const lanes = computeLanes(leavesByManager.get(row.managerName) ?? [], days);
            const laneCount = Math.max(1, lanes.length);
            return (
              <div key={row.managerId} className="flex border-t border-zinc-100 dark:border-zinc-800">
                <div className="sticky left-0 z-10 w-48 shrink-0 border-r border-zinc-200 bg-white px-3 py-2 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="text-xs font-medium">{row.managerName}</div>
                  <div className="mt-0.5 text-[10px] text-zinc-500">
                    {row.pendingCount} pending · {row.approvedCount} approved
                  </div>
                </div>
                <div
                  className="grow grid py-1"
                  style={{
                    gridTemplateColumns: `repeat(${days.length}, minmax(28px, 1fr))`,
                    gridTemplateRows: `repeat(${laneCount}, 22px)`,
                    gap: "3px 0",
                  }}
                >
                  {lanes.flatMap((lane, laneIdx) =>
                    lane.map((bar) => {
                      const palette = deptColor(bar.leave.department);
                      const isPending = bar.leave.status !== "approved";
                      return (
                        <div
                          key={bar.leave.id}
                          style={{
                            gridColumn: `${bar.startIdx + 1} / ${bar.endIdx + 2}`,
                            gridRow: laneIdx + 1,
                            ...(isPending ? { backgroundImage: pendingStripe } : {}),
                          }}
                          className={`mx-px overflow-hidden rounded border px-2 text-[10px] font-medium leading-[20px] ${palette.bar}`}
                          title={`${bar.leave.employeeName} · ${bar.leave.leaveType} · ${
                            STATUS_LABEL[bar.leave.status] ?? bar.leave.status
                          }\n${fmtRange(bar.leave.startDate, bar.leave.endDate)}${
                            bar.leave.department ? `\nDepartment: ${bar.leave.department}` : ""
                          }`}
                        >
                          <span className="block truncate">{bar.leave.employeeName}</span>
                        </div>
                      );
                    }),
                  )}
                </div>
              </div>
            );
          })
        )}
      </div>
    </section>
  );
}

```