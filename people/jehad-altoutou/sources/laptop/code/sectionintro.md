---
type: source
source_type: laptop
title: SectionIntro
slug: sectionintro
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/SectionIntro.tsx
original_size: 2962
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# SectionIntro

_Extracted from `[[assessify|assessify]]/src/components/assessment/SectionIntro.tsx` on 2026-05-14._

```tsx
"use client";

import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import {
  HeartHandshake,
  BrainCircuit,
  MonitorCog,
  ArrowRight,
} from "lucide-react";

const iconMap: Record<string, React.ElementType> = {
  "heart-handshake": HeartHandshake,
  "brain-circuit": BrainCircuit,
  "monitor-cog": MonitorCog,
};

interface SectionIntroProps {
  title: string;
  description: string;
  introText: string;
  iconName?: string;
  sectionNumber: number;
  totalSections: number;
  questionCount: number;
  onStart: () => void;
}

export function SectionIntro({
  title,
  description,
  introText,
  iconName,
  sectionNumber,
  totalSections,
  questionCount,
  onStart,
}: SectionIntroProps) {
  const Icon = iconName ? iconMap[iconName] ?? MonitorCog : MonitorCog;

  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -40 }}
      transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
      className="flex min-h-[60vh] flex-col items-center justify-center px-4 text-center"
    >
      <motion.div
        initial={{ scale: 0.5, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
        className="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-primary/10"
      >
        <Icon className="size-10 text-primary" />
      </motion.div>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="mb-2 text-sm font-medium text-muted-foreground"
      >
        Section {sectionNumber} of {totalSections}
      </motion.p>

      <motion.h2
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.35 }}
        className="mb-3 text-3xl font-bold tracking-tight"
      >
        {title}
      </motion.h2>

      <motion.p
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.45 }}
        className="mb-6 max-w-lg text-base text-muted-foreground"
      >
        {description}
      </motion.p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.55 }}
        className="mb-8 max-w-md rounded-xl bg-muted/50 p-5 text-sm leading-relaxed text-muted-foreground"
      >
        {introText}
      </motion.div>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.65 }}
        className="flex items-center gap-4"
      >
        <span className="text-sm text-muted-foreground">
          {questionCount} questions
        </span>
        <Button onClick={onStart} size="lg" className="gap-2">
          Begin Section <ArrowRight className="size-4" />
        </Button>
      </motion.div>
    </motion.div>
  );
}

```