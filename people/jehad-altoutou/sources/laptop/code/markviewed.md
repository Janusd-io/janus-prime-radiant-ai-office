---
type: source
source_type: laptop
title: MarkViewed
slug: markviewed
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/leave-requests/[id]/MarkViewed.tsx"
original_size: 463
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# MarkViewed

_Extracted from `assessify/src/app/admin/leave-requests/[id]/MarkViewed.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function MarkViewed({
  id,
  alreadyViewed,
}: {
  id: string;
  alreadyViewed: boolean;
}) {
  const router = useRouter();

  useEffect(() => {
    if (alreadyViewed) return;
    fetch(`/api/leave/${id}/mark-viewed`, { method: "POST" })
      .then(() => router.refresh())
      .catch(() => {});
  }, [id, alreadyViewed, router]);

  return null;
}

```