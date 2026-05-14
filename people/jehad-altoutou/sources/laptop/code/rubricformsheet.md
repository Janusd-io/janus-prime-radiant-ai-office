---
type: source
source_type: laptop
title: RubricFormSheet
slug: rubricformsheet
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/rubrics/RubricFormSheet.tsx
original_size: 2031
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# RubricFormSheet

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/rubrics/RubricFormSheet.tsx` on 2026-05-14._

```tsx
"use client";

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { RubricForm } from "./RubricForm";

type Criterion = {
  key: string;
  label: string;
  weight: number;
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

type JobRoleOption = { id: string; title: string; department: string };

type Initial = {
  name: string;
  kind: "pre_interview" | "post_interview";
  jobRoleId: string | null;
  isActive: boolean;
  criteria: Criterion[];
  thresholdStrong: number;
  thresholdMatch: number;
  thresholdConsider: number;
};

type Props = {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  mode: "create" | "edit";
  rubricId?: string;
  initial: Initial;
  jobRoles: JobRoleOption[];
};

// Centered modal dialog (replaces the earlier slide-in Sheet — gave too
// little horizontal room for the criterion editor + threshold row, leading
// to awkward wrapping).
export function RubricFormSheet({
  open,
  onOpenChange,
  mode,
  rubricId,
  initial,
  jobRoles,
}: Props) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="flex max-h-[90vh] w-[min(96vw,72rem)] max-w-[min(96vw,72rem)] flex-col gap-0 overflow-hidden p-0 sm:max-w-[min(96vw,72rem)]">
        <DialogHeader className="border-b border-zinc-200 px-6 py-4 text-left dark:border-zinc-800">
          <DialogTitle>{mode === "create" ? "New rubric" : "Edit rubric"}</DialogTitle>
          <DialogDescription>
            Define the dimensions, weights, and scoring guidance for the pre- or post-interview agent.
          </DialogDescription>
        </DialogHeader>
        <div className="flex-1 overflow-y-auto px-6 py-5">
          <RubricForm
            mode={mode}
            rubricId={rubricId}
            initial={initial}
            jobRoles={jobRoles}
            onSuccess={() => onOpenChange(false)}
          />
        </div>
      </DialogContent>
    </Dialog>
  );
}

```