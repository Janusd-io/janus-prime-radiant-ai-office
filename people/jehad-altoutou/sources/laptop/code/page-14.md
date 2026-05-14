---
type: source
source_type: laptop
title: page
slug: page-14
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/candidates/page.tsx
original_size: 4139
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/candidates/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import Link from "next/link";
import { applyOfficeScope } from "@/lib/auth-scope";
import { formatTimestamp } from "@/lib/slack";
import { CandidateFiltersBar } from "./CandidateFiltersBar";

export const dynamic = "force-dynamic";

type SearchParams = { q?: string; office?: string; source?: string };

export default async function CandidateListPage({
  searchParams,
}: {
  searchParams: Promise<SearchParams>;
}) {
  const user = await getSession();
  if (!user) redirect("/admin/login");

  const sp = await searchParams;
  let where: Record<string, unknown> = { archivedAt: null };
  if (sp.q) {
    where.OR = [
      { firstName: { contains: sp.q } },
      { lastName: { contains: sp.q } },
      { email: { contains: sp.q } },
      { agencyName: { contains: sp.q } },
    ];
  }
  if (sp.office) where.office = sp.office;
  if (sp.source) where.source = sp.source;
  where = applyOfficeScope({ office: user.office ?? null }, where);

  const candidates = await prisma.candidate.findMany({
    where,
    orderBy: { createdAt: "desc" },
    include: {
      _count: { select: { applications: true } },
    },
    take: 200,
  });

  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <Link href="/admin/recruitment" className="text-xs text-zinc-500 hover:underline">
            ← Pipeline
          </Link>
          <h1 className="mt-1 text-2xl font-bold tracking-tight">Candidates</h1>
          <p className="mt-1 text-sm text-muted-foreground">{candidates.length} total</p>
        </div>
      </div>

      <CandidateFiltersBar initial={sp} />

      {candidates.length === 0 ? (
        <div className="rounded-xl border border-dashed border-zinc-300 bg-white p-12 text-center dark:border-zinc-700 dark:bg-zinc-900">
          <p className="text-sm text-muted-foreground">No candidates yet.</p>
        </div>
      ) : (
        <div className="overflow-hidden rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
          <table className="w-full text-sm">
            <thead className="border-b border-zinc-200 bg-zinc-50 text-xs uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-950">
              <tr>
                <th className="px-4 py-3 text-left font-medium">Name</th>
                <th className="px-4 py-3 text-left font-medium">Email</th>
                <th className="px-4 py-3 text-left font-medium">Office</th>
                <th className="px-4 py-3 text-left font-medium">Source</th>
                <th className="px-4 py-3 text-left font-medium"># Apps</th>
                <th className="px-4 py-3 text-left font-medium">Created</th>
              </tr>
            </thead>
            <tbody>
              {candidates.map((c) => (
                <tr
                  key={c.id}
                  className="border-b border-zinc-100 last:border-0 hover:bg-zinc-50/80 dark:border-zinc-800 dark:hover:bg-zinc-800/40"
                >
                  <td className="px-4 py-3">
                    <Link
                      href={`/admin/recruitment/candidates/${c.id}`}
                      className="font-medium hover:underline"
                    >
                      {c.firstName} {c.lastName}
                    </Link>
                  </td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">{c.email}</td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">{c.office ?? "—"}</td>
                  <td className="px-4 py-3 text-zinc-600 dark:text-zinc-400">
                    {c.source === "agency" && c.agencyName ? `Agency: ${c.agencyName}` : c.source ?? "—"}
                  </td>
                  <td className="px-4 py-3">{c._count.applications}</td>
                  <td className="px-4 py-3 text-xs text-zinc-500">{formatTimestamp(c.createdAt)}</td>
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