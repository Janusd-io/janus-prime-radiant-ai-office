---
type: source
source_type: laptop
title: Assessify — page
slug: page-18
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/rubrics/[id]/edit/page.tsx"
original_size: 384
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/rubrics/[id]/edit/page.tsx` on 2026-05-14._

```tsx
import { redirect } from "next/navigation";

// Phase 1.B v2 polish: rubric authoring moved into a slide-in Sheet on the
// dashboard. Keep this URL working for any in-flight links/bookmarks.
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  redirect(`/admin/recruitment/rubrics?open=${encodeURIComponent(id)}`);
}

```