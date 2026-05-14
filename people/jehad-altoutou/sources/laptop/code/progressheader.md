---
type: source
source_type: laptop
title: ProgressHeader
slug: progressheader
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/ProgressHeader.tsx
original_size: 2360
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# ProgressHeader

_Extracted from `assessify/src/components/assessment/ProgressHeader.tsx` on 2026-05-14._

```tsx
"use client";

import { motion } from "framer-motion";
import { Clock } from "lucide-react";

interface ProgressHeaderProps {
  assessmentTitle: string;
  sectionTitle: string;
  currentQuestion: number;
  totalQuestions: number;
  overallProgress: number;
  timeSpent: number;
  timeLimit?: number | null;
}

export function ProgressHeader({
  assessmentTitle,
  sectionTitle,
  currentQuestion,
  totalQuestions,
  overallProgress,
  timeSpent,
  timeLimit,
}: ProgressHeaderProps) {
  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s.toString().padStart(2, "0")}`;
  };

  const remainingTime = timeLimit ? timeLimit * 60 - timeSpent : null;
  const isLowTime = remainingTime !== null && remainingTime < 300;

  return (
    <div className="sticky top-0 z-50 border-b border-zinc-200 bg-white/80 backdrop-blur-lg dark:border-zinc-800 dark:bg-zinc-950/80">
      <div className="mx-auto flex max-w-3xl items-center justify-between px-4 py-3">
        <div className="min-w-0 flex-1">
          <p className="truncate text-xs font-medium text-muted-foreground">
            {assessmentTitle}
          </p>
          <p className="truncate text-sm font-semibold">{sectionTitle}</p>
        </div>

        <div className="flex items-center gap-4">
          <span className="text-sm tabular-nums text-muted-foreground">
            {currentQuestion}/{totalQuestions}
          </span>

          {timeLimit && remainingTime !== null && (
            <div
              className={`flex items-center gap-1.5 rounded-full px-3 py-1 text-xs font-medium tabular-nums ${
                isLowTime
                  ? "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300"
                  : "bg-zinc-100 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400"
              }`}
            >
              <Clock className="size-3" />
              {formatTime(Math.max(0, remainingTime))}
            </div>
          )}
        </div>
      </div>

      {/* Progress bar */}
      <div className="h-1 bg-zinc-100 dark:bg-zinc-800">
        <motion.div
          className="h-full bg-primary"
          initial={{ width: 0 }}
          animate={{ width: `${overallProgress}%` }}
          transition={{ duration: 0.5, ease: "easeOut" }}
        />
      </div>
    </div>
  );
}

```