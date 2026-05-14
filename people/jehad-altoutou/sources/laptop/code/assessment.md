---
type: source
source_type: laptop
title: assessment
slug: assessment
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/types/assessment.ts
original_size: 3876
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# assessment

_Extracted from `assessify/src/types/assessment.ts` on 2026-05-14._

```typescript
// ─── Core Types ──────────────────────────────────────────────

export type QuestionType =
  | "single_select"
  | "multi_select"
  | "scenario"
  | "ranking"
  | "situational_judgment"
  | "short_text"
  | "confidence_rating"
  | "drag_order"
  | "troubleshoot_sim"
  | "branching";

export type ScoringStrategy =
  | "exact"
  | "partial"
  | "rubric"
  | "weighted_options"
  | "scenario_based";

export type Difficulty = "easy" | "medium" | "hard";

export type SessionStatus =
  | "not_started"
  | "in_progress"
  | "paused"
  | "completed"
  | "expired"
  | "disqualified";

export type Recommendation =
  | "strong_hire"
  | "hire"
  | "consider"
  | "weak_fit"
  | "reject";

export type AssessmentVersionStatus = "draft" | "published" | "archived";

// ─── Analytics Event Types ───────────────────────────────────

export type AnalyticsEventType =
  | "assessment_started"
  | "section_entered"
  | "question_viewed"
  | "answer_selected"
  | "answer_changed"
  | "answer_submitted"
  | "question_completed"
  | "section_completed"
  | "assessment_paused"
  | "assessment_resumed"
  | "assessment_submitted"
  | "assessment_completed"
  | "result_generated"
  | "admin_reviewed"
  | "result_exported";

// ─── Scoring Types ───────────────────────────────────────────

export interface ScoringResult {
  earnedPoints: number;
  maxPoints: number;
  normalizedScore: number;
  scoringReason: string;
  flaggedIndicators: string[];
  competencyImpacts: { competencyId: string; points: number; maxPoints: number }[];
}

export interface SectionScoreResult {
  sectionId: string;
  slug: string;
  title: string;
  score: number;
  maxScore: number;
  normalizedScore: number;
  weightedScore: number;
  weight: number;
}

export interface CompetencyScoreResult {
  competencyId: string;
  slug: string;
  name: string;
  score: number;
  maxScore: number;
  normalizedScore: number;
}

export interface AssessmentResult {
  candidateId: string;
  assessmentId: string;
  assessmentVersion: string;
  role: string;
  completedAt: string;
  status: string;
  totalScore: number;
  maxScore: number;
  normalizedScore: number;
  recommendation: Recommendation;
  confidenceRating: number;
  sectionScores: SectionScoreResult[];
  competencyScores: CompetencyScoreResult[];
  flags: string[];
  automationLabels: string[];
  riskIndicators: string[];
  hiringSummary: string;
  questionResults: QuestionResult[];
}

export interface QuestionResult {
  questionId: string;
  slug: string;
  sectionId: string;
  questionType: QuestionType;
  earnedPoints: number;
  maxPoints: number;
  normalizedScore: number;
  timeSpent: number;
  scoringReason: string;
  flaggedIndicators: string[];
}

// ─── Webhook Types ───────────────────────────────────────────

export interface WebhookPayload {
  event: string;
  timestamp: string;
  data: Record<string, unknown>;
}

// ─── UI State Types ──────────────────────────────────────────

export interface AssessmentState {
  sessionId: string;
  currentSectionIndex: number;
  currentQuestionIndex: number;
  answers: Record<string, AnswerPayload>;
  sectionProgress: Record<string, number>;
  startedAt: string;
  timeSpent: number;
}

export interface AnswerPayload {
  questionId: string;
  selectedOptions?: string[];
  freeTextResponse?: string;
  rankingOrder?: string[];
  confidenceLevel?: number;
  dragOrder?: string[];
  branchingPath?: string;
  timeSpent: number;
}

```