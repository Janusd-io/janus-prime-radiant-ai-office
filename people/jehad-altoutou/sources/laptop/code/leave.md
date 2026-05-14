---
type: source
source_type: laptop
title: leave
slug: leave
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/leave.ts
original_size: 7983
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# leave

_Extracted from `assessify/src/lib/leave.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";

export const LEAVE_TYPES = [
  "Annual Leave",
  "Sick Leave",
  "Business Travel Leave",
  "Maternity Leave",
  "Paternity Leave",
  "Emergency Leave",
  "Hajj Leave",
  "Unpaid / Other Leave",
] as const;

export type LeaveType = (typeof LEAVE_TYPES)[number];

/** Inclusive business-day count (counts weekdays only, inclusive of both endpoints). */
export function calculateBusinessDays(start: Date, end: Date): number {
  if (end < start) return 0;
  let count = 0;
  const cur = new Date(start);
  cur.setHours(0, 0, 0, 0);
  const last = new Date(end);
  last.setHours(0, 0, 0, 0);
  while (cur <= last) {
    const day = cur.getDay();
    if (day !== 0 && day !== 6) count++;
    cur.setDate(cur.getDate() + 1);
  }
  return count;
}

/** Balance check: returns { allocated, used, remaining, uncapped, sufficient } */
export async function checkBalance(
  employeeId: string,
  leaveType: string,
  daysRequested: number,
  year: number = new Date().getFullYear()
) {
  const balance = await prisma.leaveBalance.findUnique({
    where: { employeeId_year_leaveType: { employeeId, year, leaveType } },
  });
  if (!balance) {
    return {
      allocated: 0, used: 0, remaining: 0, uncapped: false, sufficient: false,
    };
  }
  const uncapped = balance.allocated >= 9999;
  const remaining = balance.allocated - balance.used;
  return {
    allocated: balance.allocated,
    used: balance.used,
    remaining,
    uncapped,
    sufficient: uncapped || remaining >= daysRequested,
  };
}

/** Atomically increment the `used` count after final approval. */
export async function consumeBalance(
  employeeId: string,
  leaveType: string,
  days: number,
  year: number = new Date().getFullYear()
) {
  await prisma.leaveBalance.update({
    where: { employeeId_year_leaveType: { employeeId, year, leaveType } },
    data: { used: { increment: days } },
  });
}

export const STATUS_LABEL: Record<string, string> = {
  pending_manager: "Pending Line Manager",
  pending_hr: "Pending HR",
  approved: "Approved",
  rejected_manager: "Rejected by Line Manager",
  rejected_hr: "Rejected by HR",
  blocked_balance: "Blocked — Balance Drained",
};

export const STATUS_COLOR: Record<string, string> = {
  pending_manager: "bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-200",
  pending_hr: "bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-200",
  approved: "bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200",
  rejected_manager: "bg-red-100 text-red-800 dark:bg-red-950 dark:text-red-200",
  rejected_hr: "bg-red-100 text-red-800 dark:bg-red-950 dark:text-red-200",
  blocked_balance: "bg-zinc-200 text-zinc-800 dark:bg-zinc-800 dark:text-zinc-200",
};

export type LeaveCalendarRequest = {
  id: string;
  leaveType: string;
  startDate: Date;
  endDate: Date;
  status: string;
  employee: { fullName: string | null; firstName: string };
  lineManager: { id: string; name: string };
};

export type LeaveCalendarDay = {
  dateKey: string;
  date: Date;
  weekday: string;
  dayLabel: string;
};

export type LeaveCalendarCellEntry = {
  requestId: string;
  employeeName: string;
  leaveType: string;
  status: string;
};

export type LeaveCalendarRow = {
  managerId: string;
  managerName: string;
  approvedCount: number;
  pendingCount: number;
  cells: Record<string, { entries: LeaveCalendarCellEntry[] }>;
};

export type LeaveCalendarOverlap = {
  managerId: string;
  managerName: string;
  dateKey: string;
  label: string;
  employees: string[];
};

const CALENDAR_MIN_BUSINESS_DAYS = 30;   // ~6 weeks — always show at least this much
const CALENDAR_MAX_BUSINESS_DAYS = 130;  // ~6 months — cap so the table doesn't explode
const CALENDAR_TRAILING_BUFFER = 5;      // business days shown past the furthest leave

export function buildLeaveCalendar(
  requests: LeaveCalendarRequest[],
  startDate: Date = new Date(),
  businessDayWindow?: number,
): {
  days: LeaveCalendarDay[];
  rows: LeaveCalendarRow[];
  overlaps: LeaveCalendarOverlap[];
} {
  // Auto-size the window so it covers the furthest upcoming leave instead of
  // a fixed 20 business days. Without this, leaves planned more than ~4 weeks
  // out silently disappeared from the calendar even though they were approved.
  let window: number;
  if (typeof businessDayWindow === "number") {
    window = businessDayWindow;
  } else {
    let latestEnd: Date | null = null;
    for (const request of requests) {
      if (!latestEnd || request.endDate > latestEnd) latestEnd = request.endDate;
    }
    if (!latestEnd || latestEnd < startDate) {
      window = CALENDAR_MIN_BUSINESS_DAYS;
    } else {
      const businessDaysToLatest = calculateBusinessDays(startDate, latestEnd) + CALENDAR_TRAILING_BUFFER;
      window = Math.min(
        CALENDAR_MAX_BUSINESS_DAYS,
        Math.max(CALENDAR_MIN_BUSINESS_DAYS, businessDaysToLatest),
      );
    }
  }
  const days = buildBusinessDayWindow(startDate, window);
  const dayKeys = new Set(days.map((day) => day.dateKey));
  const rowsByManager = new Map<string, LeaveCalendarRow>();
  const overlaps: LeaveCalendarOverlap[] = [];

  for (const request of requests) {
    const managerId = request.lineManager.id;
    const managerName = request.lineManager.name;
    const row =
      rowsByManager.get(managerId) ??
      {
        managerId,
        managerName,
        approvedCount: 0,
        pendingCount: 0,
        cells: {},
      };
    rowsByManager.set(managerId, row);

    if (request.status === "approved") row.approvedCount += 1;
    else row.pendingCount += 1;

    for (const date of enumerateBusinessDates(request.startDate, request.endDate)) {
      const key = toDateKey(date);
      if (!dayKeys.has(key)) continue;
      const cell = row.cells[key] ?? { entries: [] };
      row.cells[key] = cell;
      cell.entries.push({
        requestId: request.id,
        employeeName: request.employee.fullName || request.employee.firstName,
        leaveType: request.leaveType,
        status: request.status,
      });
    }
  }

  const rows = [...rowsByManager.values()]
    .sort((a, b) => a.managerName.localeCompare(b.managerName))
    .map((row) => {
      for (const day of days) {
        const entries = row.cells[day.dateKey]?.entries ?? [];
        if (entries.length > 1) {
          overlaps.push({
            managerId: row.managerId,
            managerName: row.managerName,
            dateKey: day.dateKey,
            label: `${day.weekday} ${day.dayLabel}`,
            employees: entries.map((entry) => entry.employeeName),
          });
        }
      }
      return row;
    });

  return { days, rows, overlaps };
}

function buildBusinessDayWindow(startDate: Date, length: number): LeaveCalendarDay[] {
  const days: LeaveCalendarDay[] = [];
  const current = new Date(startDate);
  current.setHours(0, 0, 0, 0);
  while (days.length < length) {
    const weekday = current.getDay();
    if (weekday !== 0 && weekday !== 6) {
      days.push({
        dateKey: toDateKey(current),
        date: new Date(current),
        weekday: current.toLocaleDateString("en-US", { weekday: "short" }),
        dayLabel: current.toLocaleDateString("en-US", { month: "short", day: "numeric" }),
      });
    }
    current.setDate(current.getDate() + 1);
  }
  return days;
}

function enumerateBusinessDates(startDate: Date, endDate: Date) {
  const dates: Date[] = [];
  const current = new Date(startDate);
  current.setHours(0, 0, 0, 0);
  const end = new Date(endDate);
  end.setHours(0, 0, 0, 0);
  while (current <= end) {
    const weekday = current.getDay();
    if (weekday !== 0 && weekday !== 6) dates.push(new Date(current));
    current.setDate(current.getDate() + 1);
  }
  return dates;
}

function toDateKey(date: Date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

```