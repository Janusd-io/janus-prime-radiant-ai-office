---
type: source
source_type: laptop
title: Assessify — page
slug: page-26
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/team/page.tsx
original_size: 1866
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/team/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import { TeamPageClient } from "./TeamPageClient";

export const dynamic = "force-dynamic";

export default async function TeamPage() {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const [employees, managers] = await Promise.all([
    prisma.employee.findMany({
      include: { lineManager: { select: { id: true, name: true } } },
      orderBy: [{ isActive: "desc" }, { firstName: "asc" }],
    }),
    prisma.lineManager.findMany({
      include: { _count: { select: { directReports: true } } },
      orderBy: [{ isActive: "desc" }, { name: "asc" }],
    }),
  ]);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">Team</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Manage employees and line managers. Records added here power the leave-request form, Slack
          DMs, and balance tracking. Soft-archive (Inactive) preserves history.
        </p>
      </div>

      <TeamPageClient
        initialEmployees={employees.map((e) => ({
          id: e.id,
          firstName: e.firstName,
          fullName: e.fullName,
          email: e.email,
          slackUserId: e.slackUserId,
          slackHandle: e.slackHandle,
          department: e.department,
          isActive: e.isActive,
          lineManagerId: e.lineManagerId,
          lineManagerName: e.lineManager?.name ?? null,
        }))}
        initialManagers={managers.map((m) => ({
          id: m.id,
          name: m.name,
          email: m.email,
          slackUserId: m.slackUserId,
          slackHandle: m.slackHandle,
          isActive: m.isActive,
          directReports: m._count.directReports,
        }))}
      />
    </div>
  );
}

```