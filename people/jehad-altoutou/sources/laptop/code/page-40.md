---
type: source
source_type: laptop
title: page
slug: page-40
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/leave/new/page.tsx
original_size: 2422
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/leave/new/page.tsx` on 2026-05-14._

```tsx
import Image from "next/image";
import { prisma } from "@/lib/db";
import { LEAVE_TYPES } from "@/lib/leave";
import LeaveForm from "./LeaveForm";

export const dynamic = "force-dynamic";

export default async function NewLeaveRequestPage() {
  const [employeesRaw, lineManagersRaw] = await Promise.all([
    prisma.employee.findMany({
      where: { isActive: true },
      orderBy: { firstName: "asc" },
      select: { id: true, firstName: true, fullName: true, slackUserId: true },
    }),
    prisma.lineManager.findMany({
      where: { isActive: true },
      orderBy: { name: "asc" },
      select: { id: true, name: true, slackUserId: true },
    }),
  ]);

  // Identify employees who are ALSO line managers — their requests escalate to the CEO.
  const managerSlackIds = new Set(
    lineManagersRaw.map((m) => m.slackUserId).filter((x): x is string => Boolean(x))
  );
  const ceo = lineManagersRaw.find((m) => m.name === "Bonaventure Wong") ?? null;

  const ceoSlackId = ceo?.slackUserId ?? null;
  const employees = employeesRaw.map((e) => ({
    id: e.id,
    firstName: e.firstName,
    fullName: e.fullName,
    isLineManager: Boolean(e.slackUserId && managerSlackIds.has(e.slackUserId)),
    isCeo: Boolean(e.slackUserId && ceoSlackId && e.slackUserId === ceoSlackId),
  }));

  const lineManagers = lineManagersRaw.map(({ id, name }) => ({ id, name }));

  return (
    <div className="min-h-screen bg-zinc-50 py-12 dark:bg-zinc-950">
      <div className="mx-auto max-w-3xl px-4 sm:px-6">
        <div className="mb-8 flex flex-col items-center text-center">
          <Image
            src="/janusd-icon-200.png"
            alt="Janus Digital"
            width={64}
            height={64}
            className="mb-4"
          />
          <h1 className="text-3xl font-bold tracking-tight">Leave Request Form</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            Complete all fields, then submit for approval.
          </p>
        </div>

        <LeaveForm
          employees={employees}
          lineManagers={lineManagers}
          leaveTypes={[...LEAVE_TYPES]}
          ceoLineManagerId={ceo?.id ?? null}
          ceoLineManagerName={ceo?.name ?? null}
        />

        <p className="mt-8 text-center text-xs text-muted-foreground">
          Janus Digital · Leave Request Form · Confidential — HR use only
        </p>
      </div>
    </div>
  );
}

```