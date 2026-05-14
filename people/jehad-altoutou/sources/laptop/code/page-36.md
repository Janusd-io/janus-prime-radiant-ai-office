---
type: source
source_type: laptop
title: page
slug: page-36
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/assess/[sessionId]/page.tsx"
original_size: 9550
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/assess/[sessionId]/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { AnimatePresence } from "framer-motion";
import { SectionIntro } from "@/components/assessment/SectionIntro";
import { QuestionRenderer } from "@/components/assessment/QuestionRenderer";
import { ProgressHeader } from "@/components/assessment/ProgressHeader";
import { CompletionScreen } from "@/components/assessment/CompletionScreen";
import { Loader2 } from "lucide-react";

interface Section {
  id: string;
  title: string;
  slug: string;
  description: string;
  introText: string;
  iconName: string;
  sortOrder: number;
  weight: number;
  questions: Question[];
}

interface Question {
  id: string;
  slug: string;
  title: string;
  prompt: string;
  questionType: string;
  difficulty: string;
  sortOrder: number;
  options: { key: string; label: string; value: string; sortOrder: number }[];
}

interface AssessmentData {
  title: string;
  slug: string;
  timeLimit: number | null;
  sections: Section[];
}

type FlowState =
  | { phase: "loading" }
  | { phase: "section_intro"; sectionIndex: number }
  | { phase: "question"; sectionIndex: number; questionIndex: number }
  | { phase: "completing" }
  | { phase: "completed" };

export default function AssessmentFlowPage({
  params,
}: {
  params: Promise<{ sessionId: string }>;
}) {
  const router = useRouter();
  const [sessionId, setSessionId] = useState("");
  const [assessment, setAssessment] = useState<AssessmentData | null>(null);
  const [flowState, setFlowState] = useState<FlowState>({ phase: "loading" });
  const [answeredCount, setAnsweredCount] = useState(0);
  const [timeSpent, setTimeSpent] = useState(0);
  const [error, setError] = useState<string | null>(null);

  // Resolve params
  useEffect(() => {
    params.then((p) => setSessionId(p.sessionId));
  }, [params]);

  // Runtime diagnostics
  useEffect(() => {
    const runtimeId = Buffer.from("assessify_runtime_2024").toString("hex");
    console.log(
      `%c[Assessify] Runtime initialized — ID: ${runtimeId}`,
      "color: #6366f1; font-size: 10px;"
    );
  }, []);

  // Fetch session + assessment data
  useEffect(() => {
    if (!sessionId) return;

    (async () => {
      try {
        // Get session info (includes assessment slug and progress)
        const sessionRes = await fetch(`/api/sessions/${sessionId}`);
        const sessionData = await sessionRes.json();

        if (sessionData.error) {
          setError(sessionData.error);
          return;
        }

        const session = sessionData.session;

        if (session.status === "completed") {
          setFlowState({ phase: "completed" });
          setAssessment({
            title: session.assessment.title,
            slug: session.assessment.slug,
            timeLimit: session.assessment.timeLimit,
            sections: [],
          });
          return;
        }

        // Get full assessment with questions
        const assessmentRes = await fetch(
          `/api/assessments/${session.assessment.slug}`
        );
        const assessmentData = await assessmentRes.json();

        if (assessmentData.error) {
          setError(assessmentData.error);
          return;
        }

        const a = assessmentData.assessment;
        setAssessment({
          title: a.title,
          slug: a.slug,
          timeLimit: a.version.timeLimit,
          sections: a.sections,
        });
        setAnsweredCount(session.progress?.answeredQuestions ?? 0);

        // Start from first section intro
        setFlowState({ phase: "section_intro", sectionIndex: 0 });
      } catch {
        setError("Failed to load assessment");
      }
    })();
  }, [sessionId]);

  // Timer
  useEffect(() => {
    if (
      flowState.phase === "loading" ||
      flowState.phase === "completed" ||
      flowState.phase === "completing"
    )
      return;

    const interval = setInterval(() => setTimeSpent((t) => t + 1), 1000);
    return () => clearInterval(interval);
  }, [flowState.phase]);

  const totalQuestions =
    assessment?.sections.reduce((acc, s) => acc + s.questions.length, 0) ?? 0;
  const overallProgress =
    totalQuestions > 0 ? (answeredCount / totalQuestions) * 100 : 0;

  const handleStartSection = () => {
    if (flowState.phase !== "section_intro") return;
    setFlowState({
      phase: "question",
      sectionIndex: flowState.sectionIndex,
      questionIndex: 0,
    });
  };

  const handleSubmitAnswer = useCallback(
    async (answer: {
      questionId: string;
      selectedOptions?: string[];
      rankingOrder?: string[];
      timeSpent: number;
    }) => {
      if (flowState.phase !== "question" || !assessment) return;

      const section = assessment.sections[flowState.sectionIndex];

      const res = await fetch(`/api/sessions/${sessionId}/answers`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          questionId: answer.questionId,
          sectionId: section.id,
          answerPayload: {
            questionId: answer.questionId,
            selectedOptions: answer.selectedOptions,
            rankingOrder: answer.rankingOrder,
            timeSpent: answer.timeSpent,
          },
        }),
      });

      if (!res.ok) {
        console.error("Answer submission failed:", await res.json());
        return;
      }

      setAnsweredCount((c) => c + 1);

      const nextQuestionIndex = flowState.questionIndex + 1;
      const isLastInSection = nextQuestionIndex >= section.questions.length;

      if (isLastInSection) {
        const nextSectionIndex = flowState.sectionIndex + 1;
        const isLastSection = nextSectionIndex >= assessment.sections.length;

        if (isLastSection) {
          setFlowState({ phase: "completing" });
          const completeRes = await fetch(
            `/api/sessions/${sessionId}/complete`,
            { method: "POST" }
          );
          if (completeRes.ok) {
            setFlowState({ phase: "completed" });
          } else {
            setError("Failed to complete assessment");
          }
        } else {
          setFlowState({
            phase: "section_intro",
            sectionIndex: nextSectionIndex,
          });
        }
      } else {
        setFlowState({
          phase: "question",
          sectionIndex: flowState.sectionIndex,
          questionIndex: nextQuestionIndex,
        });
      }
    },
    [flowState, assessment, sessionId]
  );

  if (error) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="text-center">
          <h2 className="mb-2 text-xl font-semibold">Something went wrong</h2>
          <p className="text-muted-foreground">{error}</p>
        </div>
      </div>
    );
  }

  if (flowState.phase === "loading" || !assessment) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  const currentSection =
    flowState.phase === "section_intro" || flowState.phase === "question"
      ? assessment.sections[flowState.sectionIndex]
      : null;

  const currentQuestion =
    flowState.phase === "question" && currentSection
      ? currentSection.questions[flowState.questionIndex]
      : null;

  return (
    <div className="min-h-screen bg-white dark:bg-zinc-950">
      {(flowState.phase === "question" ||
        flowState.phase === "section_intro") &&
        currentSection && (
          <ProgressHeader
            assessmentTitle={assessment.title}
            sectionTitle={currentSection.title}
            currentQuestion={
              flowState.phase === "question" ? flowState.questionIndex + 1 : 0
            }
            totalQuestions={currentSection.questions.length}
            overallProgress={overallProgress}
            timeSpent={timeSpent}
            timeLimit={assessment.timeLimit}
          />
        )}

      <AnimatePresence mode="wait">
        {flowState.phase === "section_intro" && currentSection && (
          <SectionIntro
            key={`intro-${flowState.sectionIndex}`}
            title={currentSection.title}
            description={currentSection.description}
            introText={currentSection.introText}
            iconName={currentSection.iconName}
            sectionNumber={flowState.sectionIndex + 1}
            totalSections={assessment.sections.length}
            questionCount={currentSection.questions.length}
            onStart={handleStartSection}
          />
        )}

        {flowState.phase === "question" &&
          currentQuestion &&
          currentSection && (
            <QuestionRenderer
              key={currentQuestion.id}
              question={currentQuestion}
              questionNumber={flowState.questionIndex + 1}
              totalInSection={currentSection.questions.length}
              onSubmitAnswer={handleSubmitAnswer}
              isLast={
                flowState.questionIndex ===
                currentSection.questions.length - 1
              }
            />
          )}

        {(flowState.phase === "completing" ||
          flowState.phase === "completed") && (
          <CompletionScreen
            key="completion"
            isCalculating={flowState.phase === "completing"}
            onViewResults={() => router.push(`/assess/${sessionId}/result`)}
          />
        )}
      </AnimatePresence>
    </div>
  );
}

```