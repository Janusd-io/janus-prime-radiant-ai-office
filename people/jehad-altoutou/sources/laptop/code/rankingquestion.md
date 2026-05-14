---
type: source
source_type: laptop
title: RankingQuestion
slug: rankingquestion
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/RankingQuestion.tsx
original_size: 2335
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# RankingQuestion

_Extracted from `assessify/src/components/assessment/RankingQuestion.tsx` on 2026-05-14._

```tsx
"use client";

import {  } from "react";
import { motion } from "framer-motion";
import { GripVertical, ArrowUp, ArrowDown } from "lucide-react";

interface Option {
  key: string;
  label: string;
}

interface RankingQuestionProps {
  options: Option[];
  order: string[];
  onReorder: (newOrder: string[]) => void;
}

export function RankingQuestion({ options, order, onReorder }: RankingQuestionProps) {
  const orderedOptions = order.map((key) => options.find((o) => o.key === key)!);

  const moveItem = (fromIndex: number, toIndex: number) => {
    if (toIndex < 0 || toIndex >= order.length) return;
    const newOrder = [...order];
    const [item] = newOrder.splice(fromIndex, 1);
    newOrder.splice(toIndex, 0, item);
    onReorder(newOrder);
  };

  return (
    <div className="space-y-2">
      <p className="text-xs text-muted-foreground">
        Drag or use arrows to rank from most to least important
      </p>
      {orderedOptions.map((opt, i) => (
        <motion.div
          key={opt.key}
          layout
          transition={{ duration: 0.2 }}
          className="flex items-center gap-3 rounded-xl border-2 border-zinc-200 bg-white p-3 dark:border-zinc-800 dark:bg-zinc-950"
        >
          <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-lg bg-primary/10 text-xs font-bold text-primary">
            {i + 1}
          </span>
          <GripVertical className="size-4 flex-shrink-0 text-zinc-400" />
          <span className="flex-1 text-sm">{opt.label}</span>
          <div className="flex gap-1">
            <button
              onClick={() => moveItem(i, i - 1)}
              disabled={i === 0}
              className="rounded-md p-1 text-zinc-400 transition-colors hover:bg-zinc-100 hover:text-zinc-600 disabled:opacity-30 dark:hover:bg-zinc-800"
            >
              <ArrowUp className="size-4" />
            </button>
            <button
              onClick={() => moveItem(i, i + 1)}
              disabled={i === orderedOptions.length - 1}
              className="rounded-md p-1 text-zinc-400 transition-colors hover:bg-zinc-100 hover:text-zinc-600 disabled:opacity-30 dark:hover:bg-zinc-800"
            >
              <ArrowDown className="size-4" />
            </button>
          </div>
        </motion.div>
      ))}
    </div>
  );
}

```