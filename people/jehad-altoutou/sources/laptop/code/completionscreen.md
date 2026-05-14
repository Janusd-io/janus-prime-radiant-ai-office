---
type: source
source_type: laptop
title: CompletionScreen
slug: completionscreen
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/CompletionScreen.tsx
original_size: 2836
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# CompletionScreen

_Extracted from `assessify/src/components/assessment/CompletionScreen.tsx` on 2026-05-14._

```tsx
"use client";

import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { CheckCircle, Sparkles, ArrowRight } from "lucide-react";

interface CompletionScreenProps {
  isCalculating: boolean;
  onViewResults: () => void;
}

export function CompletionScreen({
  isCalculating,
  onViewResults,
}: CompletionScreenProps) {
  return (
    <div className="flex min-h-[70vh] flex-col items-center justify-center px-4 text-center">
      {isCalculating ? (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="flex flex-col items-center"
        >
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
            className="mb-6"
          >
            <Sparkles className="size-16 text-primary" />
          </motion.div>
          <h2 className="mb-2 text-2xl font-bold tracking-tight">
            Calculating your results...
          </h2>
          <p className="text-muted-foreground">
            This will only take a moment.
          </p>
        </motion.div>
      ) : (
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
          className="flex flex-col items-center"
        >
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
            className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-green-100 dark:bg-green-950"
          >
            <CheckCircle className="size-10 text-green-600 dark:text-green-400" />
          </motion.div>

          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mb-2 text-3xl font-bold tracking-tight"
          >
            Assessment Complete!
          </motion.h2>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="mb-8 max-w-md text-muted-foreground"
          >
            Thank you for completing the assessment. Our team will review
            your responses and reach out with next steps.
          </motion.p>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
          >
            <Button onClick={onViewResults} size="lg" className="gap-2">
              Continue <ArrowRight className="size-4" />
            </Button>
          </motion.div>
        </motion.div>
      )}
    </div>
  );
}

```