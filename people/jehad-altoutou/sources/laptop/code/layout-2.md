---
type: source
source_type: laptop
title: Assessify — layout
slug: layout-2
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/layout.tsx
original_size: 849
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# layout

_Extracted from `[[assessify|assessify]]/src/app/admin/layout.tsx` on 2026-05-14._

```tsx
import { getSession } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { AdminSidebar } from "@/components/admin/AdminSidebar";

export const dynamic = "force-dynamic";

export default async function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const user = await getSession();

  // Login page renders without the chrome.
  if (!user) return <>{children}</>;

  const leaveUnread = await prisma.leaveRequest
    .count({ where: { viewedByHr: false } })
    .catch(() => 0);
  const badges: Record<string, number> = { leaveUnread };

  return (
    <div className="flex min-h-screen bg-zinc-50 dark:bg-zinc-950">
      <AdminSidebar user={user} badges={badges} />

      <main className="flex-1">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">{children}</div>
      </main>
    </div>
  );
}

```