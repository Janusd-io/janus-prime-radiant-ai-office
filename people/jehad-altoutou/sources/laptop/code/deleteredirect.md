---
type: source
source_type: laptop
title: DeleteRedirect
slug: deleteredirect
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/leave-requests/[id]/DeleteRedirect.tsx"
original_size: 436
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# DeleteRedirect

_Extracted from `[[assessify|assessify]]/src/app/admin/leave-requests/[id]/DeleteRedirect.tsx` on 2026-05-14._

```tsx
"use client";

import { useRouter } from "next/navigation";
import DeleteLeaveButton from "../DeleteLeaveButton";

export default function DeleteRedirect({
  id,
  employeeName,
}: {
  id: string;
  employeeName: string;
}) {
  const router = useRouter();
  return (
    <DeleteLeaveButton
      id={id}
      employeeName={employeeName}
      variant="button"
      onDeleted={() => router.push("/admin/leave-requests")}
    />
  );
}

```