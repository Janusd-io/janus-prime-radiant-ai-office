---
type: source
source_type: laptop
title: ResetBalanceButton
slug: resetbalancebutton
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/leave-balances/ResetBalanceButton.tsx
original_size: 2726
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# ResetBalanceButton

_Extracted from `assessify/src/app/admin/leave-balances/ResetBalanceButton.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { RotateCcw } from "lucide-react";
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

export default function ResetBalanceButton({
  employeeId,
  employeeName,
  leaveType,
}: {
  employeeId: string;
  employeeName: string;
  /** If provided, resets only that leave type. If omitted, resets ALL. */
  leaveType?: string;
}) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  const scope = leaveType ? leaveType : "all leave types";

  async function handleReset() {
    setBusy(true);
    try {
      const res = await fetch(`/api/admin/leave-balances/${employeeId}/reset`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: leaveType ? JSON.stringify({ leaveType }) : undefined,
      });
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        alert(data.error ?? "Failed to reset balance");
        setBusy(false);
        return;
      }
      router.refresh();
    } catch {
      alert("Network error");
      setBusy(false);
    }
  }

  return (
    <AlertDialog>
      <AlertDialogTrigger
        className="inline-flex size-7 items-center justify-center rounded-md text-zinc-400 hover:bg-amber-50 hover:text-amber-700 dark:hover:bg-amber-950"
        title={leaveType ? `Reset ${leaveType}` : "Reset all leave types"}
      >
        <RotateCcw className="size-3.5" />
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Reset leave balance?</AlertDialogTitle>
          <AlertDialogDescription>
            This will reset <strong>{scope}</strong> for <strong>{employeeName}</strong>
            {" "}back to zero used for the current year. Allocated amounts stay the same.
            <br />
            <br />
            The action is logged in the audit log. Previously approved leave requests are
            <em> not </em> modified — only the counter is reset.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel disabled={busy}>Cancel</AlertDialogCancel>
          <AlertDialogAction
            onClick={handleReset}
            disabled={busy}
            className="bg-amber-600 text-white hover:bg-amber-700"
          >
            {busy ? "Resetting…" : "Reset"}
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
}

```