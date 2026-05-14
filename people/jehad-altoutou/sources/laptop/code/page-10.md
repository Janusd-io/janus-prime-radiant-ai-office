---
type: source
source_type: laptop
title: page
slug: page-10
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/leave-balances/page.tsx
original_size: 5505
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/leave-balances/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import Link from "next/link";
import { ChevronLeft } from "lucide-react";
import { LEAVE_TYPES } from "@/lib/leave";
import ResetBalanceButton from "./ResetBalanceButton";

export const dynamic = "force-dynamic";

export default async function LeaveBalancesPage() {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const year = new Date().getFullYear();

  const [employees, balances] = await Promise.all([
    prisma.employee.findMany({
      where: { isActive: true },
      orderBy: { firstName: "asc" },
    }),
    prisma.leaveBalance.findMany({ where: { year } }),
  ]);

  const balanceMap = new Map<string, { allocated: number; used: number }>();
  for (const b of balances) {
    balanceMap.set(`${b.employeeId}::${b.leaveType}`, {
      allocated: b.allocated,
      used: b.used,
    });
  }

  return (
    <div>
      <Link
        href="/admin/leave-requests"
        className="mb-4 inline-flex items-center gap-1 text-sm text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-100"
      >
        <ChevronLeft className="size-4" />
        Back to Leave Requests
      </Link>

      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">Leave Balances</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Balance overview for {year}. Used days are deducted only after final approval.
          Use the <span className="font-medium">reset</span> icon to clear an employee&apos;s balance — useful for fixing mistakes without resetting everyone.
        </p>
      </div>

      <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
        <table className="w-full text-sm">
          <thead className="border-b border-zinc-200 bg-zinc-50 text-xs uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
            <tr>
              <th className="sticky left-0 z-10 bg-zinc-50 px-4 py-3 text-left font-medium dark:bg-zinc-950">
                Employee
              </th>
              {LEAVE_TYPES.map((t) => (
                <th key={t} className="px-4 py-3 text-center font-medium whitespace-nowrap">
                  {t.replace(" Leave", "")}
                </th>
              ))}
              <th className="px-4 py-3 text-center font-medium whitespace-nowrap">Reset All</th>
            </tr>
          </thead>
          <tbody>
            {employees.map((e) => (
              <tr
                key={e.id}
                className="border-b border-zinc-100 last:border-0 hover:bg-zinc-50/80 dark:border-zinc-800 dark:hover:bg-zinc-800/40"
              >
                <td className="sticky left-0 z-10 bg-white px-4 py-3 font-medium dark:bg-zinc-900">
                  {e.fullName || e.firstName}
                </td>
                {LEAVE_TYPES.map((t) => {
                  const b = balanceMap.get(`${e.id}::${t}`);
                  const empName = e.fullName || e.firstName;
                  if (!b) return <td key={t} className="px-4 py-3 text-center text-zinc-400">—</td>;
                  if (b.allocated >= 9999) {
                    return (
                      <td key={t} className="px-4 py-3 text-center text-zinc-500">
                        <span title="Uncapped">∞</span>
                        {b.used > 0 && (
                          <span className="ml-1 text-xs">({b.used} used)</span>
                        )}
                      </td>
                    );
                  }
                  const remaining = b.allocated - b.used;
                  const pct = b.used / b.allocated;
                  const color =
                    pct >= 1 ? "text-red-600 dark:text-red-400" :
                    pct >= 0.8 ? "text-amber-600 dark:text-amber-400" :
                    "text-zinc-900 dark:text-zinc-100";
                  return (
                    <td key={t} className="px-4 py-3 text-center">
                      <div className="flex items-center justify-center gap-1">
                        <div className={`font-medium ${color}`}>
                          {remaining}/{b.allocated}
                        </div>
                        {b.used > 0 && (
                          <ResetBalanceButton
                            employeeId={e.id}
                            employeeName={empName}
                            leaveType={t}
                          />
                        )}
                      </div>
                      <div className="text-[10px] text-zinc-500">{b.used} used</div>
                    </td>
                  );
                })}
                <td className="px-4 py-3 text-center">
                  <ResetBalanceButton
                    employeeId={e.id}
                    employeeName={e.fullName || e.firstName}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-4 flex flex-wrap gap-4 text-xs text-muted-foreground">
        <span>
          <span className="mr-1 inline-block size-2 rounded-full bg-red-500"></span>
          Exhausted
        </span>
        <span>
          <span className="mr-1 inline-block size-2 rounded-full bg-amber-500"></span>
          ≥ 80% used
        </span>
        <span>∞ = uncapped</span>
      </div>
    </div>
  );
}

```