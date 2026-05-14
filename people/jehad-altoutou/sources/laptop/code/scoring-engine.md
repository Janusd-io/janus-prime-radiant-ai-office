---
type: source
source_type: laptop
title: scoring-engine
slug: scoring-engine
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/scoring-engine.ts
original_size: 13485
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# scoring-engine

_Extracted from `assessify/src/lib/scoring-engine.ts` on 2026-05-14._

```typescript
import type {
  ScoringResult,
  SectionScoreResult,
  CompetencyScoreResult,
  Recommendation,
  AnswerPayload,
} from "@/types/assessment";

// ─── Question-Level Scoring ──────────────────────────────────

interface QuestionData {
  id: string;
  questionType: string;
  maxPoints: number;
  weight: number;
  scoringStrategy: string;
  correctAnswerKey: string | null;
  rubric: string | null;
  partialCreditRules: string | null;
  knockoutFlag: boolean;
  knockoutThreshold: number | null;
  options: {
    key: string;
    points: number;
    isCorrect: boolean;
  }[];
  competencies: {
    competencyId: string;
    weight: number;
  }[];
}

export function scoreQuestion(
  question: QuestionData,
  answer: AnswerPayload
): ScoringResult {
  const { scoringStrategy, questionType, maxPoints, options, competencies } =
    question;

  let earnedPoints = 0;
  let scoringReason = "";
  const flaggedIndicators: string[] = [];

  switch (scoringStrategy) {
    case "weighted_options":
      earnedPoints = scoreWeightedOptions(options, answer);
      scoringReason = `Scored via weighted options: ${earnedPoints}/${maxPoints}`;
      break;

    case "exact":
      earnedPoints = scoreExact(question, answer);
      scoringReason =
        earnedPoints > 0 ? "Correct answer selected" : "Incorrect answer";
      break;

    case "partial":
      earnedPoints = scorePartial(question, answer);
      scoringReason = `Partial credit: ${earnedPoints}/${maxPoints}`;
      break;

    case "rubric":
      earnedPoints = scoreRubric(question, answer);
      scoringReason = `Rubric-based scoring: ${earnedPoints}/${maxPoints}`;
      break;

    case "scenario_based":
      earnedPoints = scoreScenario(question, answer);
      scoringReason = `Scenario evaluation: ${earnedPoints}/${maxPoints}`;
      break;

    default:
      earnedPoints = scoreWeightedOptions(options, answer);
      scoringReason = `Default scoring: ${earnedPoints}/${maxPoints}`;
  }

  // Clamp
  earnedPoints = Math.max(0, Math.min(earnedPoints, maxPoints));

  // Flag detection
  if (answer.timeSpent < 3 && questionType !== "single_select") {
    flaggedIndicators.push("suspiciously_fast_response");
  }
  if (
    question.knockoutFlag &&
    question.knockoutThreshold !== null &&
    earnedPoints / maxPoints < question.knockoutThreshold
  ) {
    flaggedIndicators.push("knockout_threshold_failed");
  }
  if (!answer.selectedOptions?.length && !answer.freeTextResponse && !answer.rankingOrder?.length && !answer.dragOrder?.length) {
    flaggedIndicators.push("unanswered_question");
  }

  const normalizedScore = maxPoints > 0 ? earnedPoints / maxPoints : 0;

  // Competency impacts
  const competencyImpacts = competencies.map((c) => ({
    competencyId: c.competencyId,
    points: earnedPoints * c.weight,
    maxPoints: maxPoints * c.weight,
  }));

  return {
    earnedPoints,
    maxPoints,
    normalizedScore,
    scoringReason,
    flaggedIndicators,
    competencyImpacts,
  };
}

function scoreWeightedOptions(
  options: QuestionData["options"],
  answer: AnswerPayload
): number {
  if (!answer.selectedOptions?.length) return 0;
  return answer.selectedOptions.reduce((sum, key) => {
    const opt = options.find((o) => o.key === key);
    return sum + (opt?.points ?? 0);
  }, 0);
}

function scoreExact(question: QuestionData, answer: AnswerPayload): number {
  if (!question.correctAnswerKey) return 0;
  try {
    const correct = JSON.parse(question.correctAnswerKey);
    if (Array.isArray(correct)) {
      const selected = answer.selectedOptions ?? [];
      if (
        selected.length === correct.length &&
        selected.every((s) => correct.includes(s))
      ) {
        return question.maxPoints;
      }
      return 0;
    }
    if (answer.selectedOptions?.includes(correct)) {
      return question.maxPoints;
    }
    return 0;
  } catch {
    return 0;
  }
}

function scorePartial(question: QuestionData, answer: AnswerPayload): number {
  if (!question.correctAnswerKey) return scoreWeightedOptions(question.options, answer);
  try {
    const correct: string[] = JSON.parse(question.correctAnswerKey);
    const selected = answer.selectedOptions ?? [];
    if (!Array.isArray(correct)) return scoreExact(question, answer);

    const correctCount = selected.filter((s) => correct.includes(s)).length;
    const incorrectCount = selected.filter((s) => !correct.includes(s)).length;
    const ratio = Math.max(0, (correctCount - incorrectCount * 0.5)) / correct.length;
    return question.maxPoints * ratio;
  } catch {
    return 0;
  }
}

function scoreRubric(question: QuestionData, answer: AnswerPayload): number {
  // For rubric-based scoring (free text), use option points as proxy
  if (answer.selectedOptions?.length) {
    return scoreWeightedOptions(question.options, answer);
  }
  // Free text — default to mid-range score (would be reviewed by admin)
  if (answer.freeTextResponse && answer.freeTextResponse.trim().length > 10) {
    return question.maxPoints * 0.5;
  }
  return 0;
}

function scoreScenario(question: QuestionData, answer: AnswerPayload): number {
  // Scenario-based uses weighted options
  return scoreWeightedOptions(question.options, answer);
}

// ─── Ranking / Drag-Order Scoring ────────────────────────────

export function scoreRanking(
  correctOrder: string[],
  submittedOrder: string[]
): number {
  if (!submittedOrder.length || !correctOrder.length) return 0;
  let score = 0;
  const n = correctOrder.length;
  for (let i = 0; i < n; i++) {
    if (submittedOrder[i] === correctOrder[i]) {
      score += 1;
    } else {
      // Partial credit for items within 1 position
      const actualPos = submittedOrder.indexOf(correctOrder[i]);
      if (actualPos >= 0 && Math.abs(actualPos - i) === 1) {
        score += 0.5;
      }
    }
  }
  return score / n;
}

// ─── Section-Level Scoring ───────────────────────────────────

interface SectionData {
  id: string;
  slug: string;
  title: string;
  weight: number;
}

interface QuestionScore {
  sectionId: string;
  earnedPoints: number;
  maxPoints: number;
}

export function scoreSections(
  sections: SectionData[],
  questionScores: QuestionScore[]
): SectionScoreResult[] {
  return sections.map((section) => {
    const sectionQuestions = questionScores.filter(
      (q) => q.sectionId === section.id
    );
    const score = sectionQuestions.reduce((s, q) => s + q.earnedPoints, 0);
    const maxScore = sectionQuestions.reduce((s, q) => s + q.maxPoints, 0);
    const normalizedScore = maxScore > 0 ? score / maxScore : 0;
    const weightedScore = normalizedScore * section.weight;

    return {
      sectionId: section.id,
      slug: section.slug,
      title: section.title,
      score: Math.round(score * 100) / 100,
      maxScore,
      normalizedScore: Math.round(normalizedScore * 1000) / 1000,
      weightedScore: Math.round(weightedScore * 1000) / 1000,
      weight: section.weight,
    };
  });
}

// ─── Competency-Level Scoring ────────────────────────────────

interface CompetencyData {
  id: string;
  slug: string;
  name: string;
}

interface CompetencyImpact {
  competencyId: string;
  points: number;
  maxPoints: number;
}

export function scoreCompetencies(
  competencies: CompetencyData[],
  impacts: CompetencyImpact[]
): CompetencyScoreResult[] {
  return competencies.map((comp) => {
    const compImpacts = impacts.filter((i) => i.competencyId === comp.id);
    const score = compImpacts.reduce((s, i) => s + i.points, 0);
    const maxScore = compImpacts.reduce((s, i) => s + i.maxPoints, 0);
    const normalizedScore = maxScore > 0 ? score / maxScore : 0;

    return {
      competencyId: comp.id,
      slug: comp.slug,
      name: comp.name,
      score: Math.round(score * 100) / 100,
      maxScore: Math.round(maxScore * 100) / 100,
      normalizedScore: Math.round(normalizedScore * 1000) / 1000,
    };
  });
}

// ─── Final Recommendation ────────────────────────────────────

export interface RecommendationThresholds {
  strongHire: number;
  hire: number;
  consider: number;
  weakFit: number;
}

export const DEFAULT_THRESHOLDS: RecommendationThresholds = {
  strongHire: 0.85,
  hire: 0.70,
  consider: 0.55,
  weakFit: 0.40,
};

export function calculateRecommendation(
  normalizedScore: number,
  flags: string[],
  thresholds: RecommendationThresholds = DEFAULT_THRESHOLDS
): Recommendation {
  const hasKnockout = flags.includes("knockout_threshold_failed");

  if (hasKnockout) return "reject";
  if (normalizedScore >= thresholds.strongHire) return "strong_hire";
  if (normalizedScore >= thresholds.hire) return "hire";
  if (normalizedScore >= thresholds.consider) return "consider";
  if (normalizedScore >= thresholds.weakFit) return "weak_fit";
  return "reject";
}

export function parseThresholds(json: string | null): RecommendationThresholds {
  if (!json) return DEFAULT_THRESHOLDS;
  try {
    const parsed = JSON.parse(json);
    return {
      strongHire: parsed.strongHire ?? DEFAULT_THRESHOLDS.strongHire,
      hire: parsed.hire ?? DEFAULT_THRESHOLDS.hire,
      consider: parsed.consider ?? DEFAULT_THRESHOLDS.consider,
      weakFit: parsed.weakFit ?? DEFAULT_THRESHOLDS.weakFit,
    };
  } catch {
    return DEFAULT_THRESHOLDS;
  }
}

export function calculateConfidence(
  sectionScores: SectionScoreResult[],
  totalQuestions: number,
  answeredQuestions: number
): number {
  // Confidence based on completion rate and score variance
  const completionRate = totalQuestions > 0 ? answeredQuestions / totalQuestions : 0;
  const scores = sectionScores.map((s) => s.normalizedScore);
  const mean = scores.reduce((a, b) => a + b, 0) / (scores.length || 1);
  const variance =
    scores.reduce((sum, s) => sum + Math.pow(s - mean, 2), 0) /
    (scores.length || 1);
  const consistency = Math.max(0, 1 - variance);

  return Math.round(completionRate * 0.4 + consistency * 0.6 * 100) / 100;
}

export function generateHiringSummary(
  recommendation: Recommendation,
  sectionScores: SectionScoreResult[],
  competencyScores: CompetencyScoreResult[],
  flags: string[]
): string {
  const labels: Record<Recommendation, string> = {
    strong_hire: "Strong Hire — Candidate demonstrated exceptional performance",
    hire: "Hire — Candidate meets requirements with solid performance",
    consider: "Consider — Candidate shows potential but has areas for development",
    weak_fit: "Weak Fit — Candidate falls below expectations in key areas",
    reject: "Reject — Candidate does not meet minimum requirements",
  };

  let summary = labels[recommendation] + ".";

  // Top strengths
  const strengths = competencyScores
    .filter((c) => c.normalizedScore >= 0.8)
    .map((c) => c.name);
  if (strengths.length) {
    summary += ` Strengths: ${strengths.join(", ")}.`;
  }

  // Weaknesses
  const weaknesses = competencyScores
    .filter((c) => c.normalizedScore < 0.5)
    .map((c) => c.name);
  if (weaknesses.length) {
    summary += ` Needs improvement: ${weaknesses.join(", ")}.`;
  }

  if (flags.length) {
    summary += ` Flags: ${flags.join(", ")}.`;
  }

  return summary;
}

export function generateAutomationLabels(
  recommendation: Recommendation,
  sectionScores: SectionScoreResult[],
  competencyScores: CompetencyScoreResult[],
  flags: string[]
): string[] {
  const labels: string[] = [];

  if (recommendation === "strong_hire" || recommendation === "hire") {
    labels.push("eligible_for_interview");
  }
  if (recommendation === "strong_hire") {
    labels.push("fast_track_candidate");
  }
  if (recommendation === "reject") {
    labels.push("auto_reject");
  }

  // Section-specific
  const aiSection = sectionScores.find((s) => s.slug === "ai-awareness");
  if (aiSection && aiSection.normalizedScore >= 0.8) {
    labels.push("high_ai_readiness");
  }
  const cultureSection = sectionScores.find((s) => s.slug === "cultural-fit");
  if (cultureSection && cultureSection.normalizedScore >= 0.85) {
    labels.push("strong_cultural_alignment");
  }

  // Flag-based
  if (flags.includes("knockout_threshold_failed")) {
    labels.push("knockout_triggered");
  }
  if (flags.includes("suspiciously_fast_response")) {
    labels.push("review_response_timing");
  }

  // Competency-specific
  const troubleshooting = competencyScores.find(
    (c) => c.slug === "troubleshooting"
  );
  if (troubleshooting && troubleshooting.normalizedScore < 0.5) {
    labels.push("needs_improvement_in_troubleshooting");
  }

  return labels;
}

export function generateRiskIndicators(
  sectionScores: SectionScoreResult[],
  competencyScores: CompetencyScoreResult[],
  flags: string[]
): string[] {
  const risks: string[] = [];

  // Low section scores
  for (const s of sectionScores) {
    if (s.normalizedScore < 0.4) {
      risks.push(`low_${s.slug}_score`);
    }
  }

  // Low competency scores
  for (const c of competencyScores) {
    if (c.normalizedScore < 0.35) {
      risks.push(`critical_weakness_${c.slug}`);
    }
  }

  if (flags.includes("suspiciously_fast_response")) {
    risks.push("potential_integrity_concern");
  }

  return risks;
}

```