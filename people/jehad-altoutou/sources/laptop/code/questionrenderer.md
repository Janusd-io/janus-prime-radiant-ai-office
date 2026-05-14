---
type: source
source_type: laptop
title: QuestionRenderer
slug: questionrenderer
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/assessment/QuestionRenderer.tsx
original_size: 6123
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# QuestionRenderer

_Extracted from `assessify/src/components/assessment/QuestionRenderer.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { SingleSelect } from "./SingleSelect";
import { MultiSelect } from "./MultiSelect";
import { RankingQuestion } from "./RankingQuestion";
import { ArrowRight, Loader2 } from "lucide-react";

interface QuestionOption {
  key: string;
  label: string;
  value: string;
  sortOrder: number;
}

interface Question {
  id: string;
  slug: string;
  title: string;
  prompt: string;
  questionType: string;
  difficulty: string;
  options: QuestionOption[];
}

interface QuestionRendererProps {
  question: Question;
  questionNumber: number;
  totalInSection: number;
  onSubmitAnswer: (answer: {
    questionId: string;
    selectedOptions?: string[];
    rankingOrder?: string[];
    timeSpent: number;
  }) => Promise<void>;
  isLast: boolean;
}

export function QuestionRenderer({
  question,
  questionNumber,
  totalInSection,
  onSubmitAnswer,
  isLast,
}: QuestionRendererProps) {
  const [selectedKey, setSelectedKey] = useState<string | null>(null);
  const [selectedKeys, setSelectedKeys] = useState<string[]>([]);
  const [rankingOrder, setRankingOrder] = useState<string[]>(
    question.options
      .sort((a, b) => a.sortOrder - b.sortOrder)
      .map((o) => o.key)
  );
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [startTime] = useState(() => Date.now());

  // Reset state when question changes. We intentionally exclude
  // question.options because it's recreated on every render — keying off
  // question.id is the stable signal that the question itself changed.
  useEffect(() => {
    setSelectedKey(null);
    setSelectedKeys([]);
    setRankingOrder(
      question.options
        .sort((a, b) => a.sortOrder - b.sortOrder)
        .map((o) => o.key)
    );
    setIsSubmitting(false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [question.id]);

  const hasAnswer =
    question.questionType === "ranking" || question.questionType === "drag_order"
      ? true
      : question.questionType === "multi_select"
        ? selectedKeys.length > 0
        : selectedKey !== null;

  const handleSubmit = async () => {
    if (!hasAnswer || isSubmitting) return;
    setIsSubmitting(true);
    const timeSpent = Math.round((Date.now() - startTime) / 1000);

    const answer: Parameters<typeof onSubmitAnswer>[0] = {
      questionId: question.id,
      timeSpent,
    };

    if (question.questionType === "ranking" || question.questionType === "drag_order") {
      answer.rankingOrder = rankingOrder;
    } else if (question.questionType === "multi_select") {
      answer.selectedOptions = selectedKeys;
    } else {
      answer.selectedOptions = selectedKey ? [selectedKey] : [];
    }

    await onSubmitAnswer(answer);
  };

  const difficultyColors: Record<string, string> = {
    easy: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300",
    medium: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300",
    hard: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300",
  };

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={question.id}
        initial={{ opacity: 0, x: 60 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0, x: -60 }}
        transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
        className="mx-auto max-w-2xl px-4 py-8"
      >
        {/* Question header */}
        <div className="mb-6">
          <div className="mb-3 flex items-center gap-2">
            <span className="text-xs font-medium text-muted-foreground">
              Question {questionNumber} of {totalInSection}
            </span>
            <span
              className={`rounded-full px-2 py-0.5 text-[10px] font-medium ${
                difficultyColors[question.difficulty] ?? ""
              }`}
            >
              {question.difficulty}
            </span>
          </div>
          <h3 className="text-xl font-semibold leading-snug tracking-tight">
            {question.title}
          </h3>
          <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
            {question.prompt}
          </p>
        </div>

        {/* Question body */}
        <div className="mb-8">
          {(question.questionType === "single_select" ||
            question.questionType === "scenario" ||
            question.questionType === "situational_judgment") && (
            <SingleSelect
              options={question.options}
              selectedKey={selectedKey}
              onSelect={setSelectedKey}
            />
          )}

          {question.questionType === "multi_select" && (
            <MultiSelect
              options={question.options}
              selectedKeys={selectedKeys}
              onToggle={(key) =>
                setSelectedKeys((prev) =>
                  prev.includes(key)
                    ? prev.filter((k) => k !== key)
                    : [...prev, key]
                )
              }
            />
          )}

          {(question.questionType === "ranking" ||
            question.questionType === "drag_order") && (
            <RankingQuestion
              options={question.options}
              order={rankingOrder}
              onReorder={setRankingOrder}
            />
          )}
        </div>

        {/* Submit */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: hasAnswer ? 1 : 0.4 }}
          className="flex justify-end"
        >
          <Button
            onClick={handleSubmit}
            disabled={!hasAnswer || isSubmitting}
            size="lg"
            className="gap-2"
          >
            {isSubmitting ? (
              <Loader2 className="size-4 animate-spin" />
            ) : (
              <>
                {isLast ? "Complete Section" : "Next"}
                <ArrowRight className="size-4" />
              </>
            )}
          </Button>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}

```