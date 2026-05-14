---
type: source
source_type: laptop
title: MultiSelect
slug: multiselect
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/MultiSelect.tsx
original_size: 2240
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# MultiSelect

_Extracted from `[[assessify|assessify]]/src/components/assessment/MultiSelect.tsx` on 2026-05-14._

```tsx
"use client";

import { motion } from "framer-motion";
import { Check } from "lucide-react";

interface Option {
  key: string;
  label: string;
  value: string;
}

interface MultiSelectProps {
  options: Option[];
  selectedKeys: string[];
  onToggle: (key: string) => void;
}

export function MultiSelect({ options, selectedKeys, onToggle }: MultiSelectProps) {
  return (
    <div className="space-y-3">
      <p className="text-xs text-muted-foreground">Select all that apply</p>
      {options.map((opt, i) => {
        const isSelected = selectedKeys.includes(opt.key);
        return (
          <motion.button
            key={opt.key}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: i * 0.06, duration: 0.3 }}
            onClick={() => onToggle(opt.key)}
            className={`group flex w-full items-start gap-3 rounded-xl border-2 p-4 text-left transition-all ${
              isSelected
                ? "border-primary bg-primary/5 shadow-sm"
                : "border-zinc-200 hover:border-zinc-300 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:border-zinc-700 dark:hover:bg-zinc-900"
            }`}
          >
            <span
              className={`mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-md border-2 transition-all ${
                isSelected
                  ? "border-primary bg-primary"
                  : "border-zinc-300 group-hover:border-zinc-400 dark:border-zinc-600"
              }`}
            >
              {isSelected && (
                <motion.div initial={{ scale: 0 }} animate={{ scale: 1 }}>
                  <Check className="size-3 text-white" />
                </motion.div>
              )}
            </span>
            <span
              className={`text-sm leading-relaxed ${
                isSelected ? "font-medium text-foreground" : "text-zinc-600 dark:text-zinc-400"
              }`}
            >
              {opt.label}
            </span>
          </motion.button>
        );
      })}
      {selectedKeys.length > 0 && (
        <p className="text-xs text-muted-foreground">
          {selectedKeys.length} selected
        </p>
      )}
    </div>
  );
}

```