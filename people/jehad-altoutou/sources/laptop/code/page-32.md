---
type: source
source_type: laptop
title: page
slug: page-32
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/careers/page.tsx
original_size: 3065
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/careers/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import Link from "next/link";

export const dynamic = "force-dynamic";

export default async function CareersPage() {
  const roles = await prisma.jobRole.findMany({
    where: { isActive: true },
    include: { department: true },
    orderBy: [{ department: { name: "asc" } }, { title: "asc" }],
  });

  // Group roles by department for a clean layout
  const byDepartment = new Map<string, typeof roles>();
  for (const r of roles) {
    const key = r.department.name;
    const existing = byDepartment.get(key);
    if (existing) existing.push(r);
    else byDepartment.set(key, [r]);
  }

  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <header className="mb-10">
        <h1 className="text-3xl font-bold tracking-tight">Careers at Janus Digital</h1>
        <p className="mt-3 text-base text-zinc-600 dark:text-zinc-300">
          We&apos;re hiring across Dubai and Singapore. Pick a role below to apply directly — no
          recruiter required.
        </p>
      </header>

      {roles.length === 0 ? (
        <div className="rounded-xl border border-dashed border-zinc-300 bg-white p-10 text-center dark:border-zinc-700 dark:bg-zinc-900">
          <p className="text-sm text-zinc-500">No open positions right now. Check back soon!</p>
        </div>
      ) : (
        <div className="space-y-10">
          {Array.from(byDepartment.entries()).map(([dept, items]) => (
            <section key={dept}>
              <h2 className="mb-4 text-sm font-semibold uppercase tracking-wide text-zinc-500">
                {dept}
              </h2>
              <ul className="space-y-3">
                {items.map((r) => (
                  <li
                    key={r.id}
                    className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900"
                  >
                    <div className="flex items-center justify-between gap-4">
                      <div className="min-w-0 flex-1">
                        <h3 className="text-base font-semibold">{r.title}</h3>
                        {r.description && (
                          <p className="mt-1 line-clamp-3 text-sm text-zinc-600 dark:text-zinc-400">
                            {r.description}
                          </p>
                        )}
                      </div>
                      <Link
                        href={`/careers/apply/${r.slug}`}
                        className="shrink-0 rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 dark:bg-white dark:text-zinc-900 dark:hover:bg-zinc-100"
                      >
                        Apply
                      </Link>
                    </div>
                  </li>
                ))}
              </ul>
            </section>
          ))}
        </div>
      )}

      <footer className="mt-16 border-t border-zinc-200 pt-6 text-xs text-zinc-500 dark:border-zinc-800">
        Powered by Assessify · Janus Digital
      </footer>
    </main>
  );
}

```