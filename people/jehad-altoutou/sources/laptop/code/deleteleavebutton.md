---
type: source
source_type: laptop
title: DeleteLeaveButton
slug: deleteleavebutton
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/leave-requests/DeleteLeaveButton.tsx
original_size: 2709
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# DeleteLeaveButton

_Extracted from `[[assessify|assessify]]/src/app/admin/leave-requests/DeleteLeaveButton.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Trash2 } from "lucide-react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

export default function DeleteLeaveButton({
  id,
  employeeName,
  variant = "icon",
  onDeleted,
}: {
  id: string;
  employeeName: string;
  variant?: "icon" | "button";
  onDeleted?: () => void;
}) {
  const router = useRouter();
  const [deleting, setDeleting] = useState(false);

  async function handleDelete() {
    setDeleting(true);
    try {
      const res = await fetch(`/api/leave/${id}`, { method: "DELETE" });
      if (!res.ok) {
        alert("Failed to delete");
        setDeleting(false);
        return;
      }
      if (onDeleted) onDeleted();
      router.refresh();
    } catch {
      alert("Failed to delete");
      setDeleting(false);
    }
  }

  const triggerClass =
    variant === "icon"
      ? "inline-flex size-8 items-center justify-center rounded-md text-zinc-500 hover:bg-red-50 hover:text-red-600 dark:hover:bg-red-950"
      : "inline-flex items-center gap-2 rounded-lg border border-red-200 bg-white px-4 py-2 text-sm font-medium text-red-600 hover:bg-red-50 dark:border-red-900 dark:bg-zinc-900 dark:hover:bg-red-950";

  return (
    <AlertDialog>
      <AlertDialogTrigger
        className={triggerClass}
        title={variant === "icon" ? "Delete leave request" : undefined}
      >
        <Trash2 className="size-4" />
        {variant === "button" && <span>Delete Record</span>}
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Delete leave request?</AlertDialogTitle>
          <AlertDialogDescription>
            This will permanently delete the leave request for{" "}
            <strong>{employeeName}</strong>. This action cannot be undone.
            <br />
            <br />
            Note: this does <strong>not</strong> refund any balance that was
            consumed if the request was already approved.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel disabled={deleting}>Cancel</AlertDialogCancel>
          <AlertDialogAction
            onClick={handleDelete}
            disabled={deleting}
            className="bg-red-600 text-white hover:bg-red-700"
          >
            {deleting ? "Deleting…" : "Delete"}
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
}

```