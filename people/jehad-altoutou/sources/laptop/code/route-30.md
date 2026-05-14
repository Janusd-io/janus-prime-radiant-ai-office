---
type: source
source_type: laptop
title: route
slug: route-30
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/leave-balances/[employeeId]/reset/route.ts"
original_size: 1940
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/leave-balances/[employeeId]/reset/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { auditLog } from "@/lib/audit";
import { getClientIp } from "@/lib/rate-limit";

/**
 * POST /api/admin/leave-balances/[employeeId]/reset
 * Reset all leave balances for one employee in the current year (used → 0).
 * Optional body: { leaveType?: string } to reset only a specific leave type.
 */
export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ employeeId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  if (session.role !== "admin") {
    return NextResponse.json({ error: "Only admins can reset balances" }, { status: 403 });
  }

  const { employeeId } = await ctx.params;
  const year = new Date().getFullYear();

  const employee = await prisma.employee.findUnique({ where: { id: employeeId } });
  if (!employee) return NextResponse.json({ error: "Employee not found" }, { status: 404 });

  let leaveType: string | undefined;
  try {
    const body = await req.json().catch(() => ({}));
    if (typeof body?.leaveType === "string") leaveType = body.leaveType;
  } catch { /* no body, reset all */ }

  const where = leaveType
    ? { employeeId, year, leaveType }
    : { employeeId, year };

  const result = await prisma.leaveBalance.updateMany({
    where,
    data: { used: 0 },
  });

  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "leave_balance.reset",
    targetType: "Employee",
    targetId: employeeId,
    details: {
      employeeName: employee.fullName || employee.firstName,
      year,
      leaveType: leaveType ?? "ALL",
      rowsUpdated: result.count,
    },
    ipAddress: getClientIp(req),
  });

  return NextResponse.json({
    ok: true,
    reset: result.count,
    leaveType: leaveType ?? "all",
  });
}

```