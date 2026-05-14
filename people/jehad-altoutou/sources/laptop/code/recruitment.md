---
type: source
source_type: laptop
title: recruitment
slug: recruitment
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/recruitment.ts
original_size: 8870
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# recruitment

_Extracted from `assessify/src/lib/recruitment.ts` on 2026-05-14._

```typescript
// Recruitment pipeline domain constants (Phase 1.A).
// Mirrors the STATUS_LABEL/STATUS_COLOR pattern in src/lib/leave.ts.

export const STAGE_FLOW = [
  "intake_received",
  "cv_review",
  "pre_scored",
  "interview_invited",
  "interview_scheduled",
  "interview_completed",
  "post_scored",
  "offer",
  "hired",
  "rejected",
  "withdrawn",
] as const;

export type RecruitmentStage = (typeof STAGE_FLOW)[number];

export const STAGE_LABEL: Record<RecruitmentStage, string> = {
  intake_received: "Intake received",
  cv_review: "CV review",
  pre_scored: "Pre-screen scored",
  interview_invited: "Interview invited",
  interview_scheduled: "Interview scheduled",
  interview_completed: "Interview completed",
  post_scored: "Post-interview scored",
  offer: "Offer extended",
  hired: "Hired",
  rejected: "Rejected",
  withdrawn: "Withdrawn",
};

export const STAGE_COLOR: Record<RecruitmentStage, string> = {
  intake_received: "bg-blue-100 text-blue-900",
  cv_review: "bg-indigo-100 text-indigo-900",
  pre_scored: "bg-violet-100 text-violet-900",
  interview_invited: "bg-amber-100 text-amber-900",
  interview_scheduled: "bg-amber-200 text-amber-900",
  interview_completed: "bg-orange-100 text-orange-900",
  post_scored: "bg-fuchsia-100 text-fuchsia-900",
  offer: "bg-teal-100 text-teal-900",
  hired: "bg-emerald-100 text-emerald-900",
  rejected: "bg-rose-100 text-rose-900",
  withdrawn: "bg-zinc-200 text-zinc-700",
};

export const APPLICATION_STATUSES = [
  "active",
  "closed_hired",
  "closed_rejected",
  "closed_withdrawn",
] as const;

export type ApplicationStatus = (typeof APPLICATION_STATUSES)[number];

export const STATUS_LABEL: Record<ApplicationStatus, string> = {
  active: "Active",
  closed_hired: "Closed — Hired",
  closed_rejected: "Closed — Rejected",
  closed_withdrawn: "Closed — Withdrawn",
};

export const SOURCES = ["agency", "career_page", "direct", "referral"] as const;
export type ApplicationSource = (typeof SOURCES)[number];

export const SOURCE_LABEL: Record<ApplicationSource, string> = {
  agency: "Agency",
  career_page: "Career page",
  direct: "Direct",
  referral: "Referral",
};

export const OFFICES = ["Dubai", "Singapore"] as const;
export type Office = (typeof OFFICES)[number];

export const NOTICE_PERIODS = [
  "Immediately available",
  "Less than 1 month",
  "1 month",
  "2 months",
  "3 months",
  "More than 3 months",
] as const;

export type NoticePeriod = (typeof NOTICE_PERIODS)[number];

export const SCORE_TIERS = ["strong_match", "match", "consider", "weak", "reject"] as const;
export type ScoreTier = (typeof SCORE_TIERS)[number];

export const SCORE_TIER_LABEL: Record<ScoreTier, string> = {
  strong_match: "Strong match",
  match: "Match",
  consider: "Consider",
  weak: "Weak fit",
  reject: "Below threshold",
};

export const SCORE_TIER_COLOR: Record<ScoreTier, string> = {
  strong_match: "bg-emerald-100 text-emerald-900",
  match: "bg-green-100 text-green-900",
  consider: "bg-amber-100 text-amber-900",
  weak: "bg-orange-100 text-orange-900",
  reject: "bg-rose-100 text-rose-900",
};

/** Tier mapping from raw 0..1 score against rubric thresholds. */
export function scoreToTier(
  score: number,
  thresholds: { strong: number; match: number; consider: number },
): ScoreTier {
  if (score >= thresholds.strong) return "strong_match";
  if (score >= thresholds.match) return "match";
  if (score >= thresholds.consider) return "consider";
  if (score >= thresholds.consider * 0.7) return "weak";
  return "reject";
}

// ─── HR-style recommendations + report shape (Phase 1.B v2) ───────────

export const RECOMMENDATIONS = [
  "strong_hire",
  "hire",
  "conditional_advance",
  "consider",
  "do_not_advance",
] as const;
export type Recommendation = (typeof RECOMMENDATIONS)[number];

export const RECOMMENDATION_LABEL: Record<Recommendation, string> = {
  strong_hire: "Strong Hire",
  hire: "Hire",
  conditional_advance: "Conditional Advance — Interview Required",
  consider: "Consider",
  do_not_advance: "Do Not Advance",
};

export const RECOMMENDATION_COLOR: Record<Recommendation, string> = {
  strong_hire: "bg-emerald-100 text-emerald-900",
  hire: "bg-green-100 text-green-900",
  conditional_advance: "bg-amber-100 text-amber-900",
  consider: "bg-orange-100 text-orange-900",
  do_not_advance: "bg-rose-100 text-rose-900",
};

export const RISK_SEVERITIES = ["HIGH", "MEDIUM-HIGH", "MEDIUM", "LOW-MEDIUM", "LOW"] as const;
export type RiskSeverity = (typeof RISK_SEVERITIES)[number];

export const RISK_SEVERITY_COLOR: Record<RiskSeverity, string> = {
  HIGH: "bg-rose-100 text-rose-900 border-rose-300 dark:bg-rose-950 dark:text-rose-200 dark:border-rose-800",
  "MEDIUM-HIGH": "bg-orange-100 text-orange-900 border-orange-300 dark:bg-orange-950 dark:text-orange-200 dark:border-orange-800",
  MEDIUM: "bg-amber-100 text-amber-900 border-amber-300 dark:bg-amber-950 dark:text-amber-200 dark:border-amber-800",
  "LOW-MEDIUM": "bg-yellow-100 text-yellow-900 border-yellow-300 dark:bg-yellow-950 dark:text-yellow-200 dark:border-yellow-800",
  LOW: "bg-zinc-100 text-zinc-700 border-zinc-300 dark:bg-zinc-800 dark:text-zinc-300 dark:border-zinc-700",
};

/** Map weighted /100 composite to recommendation tier, with thresholds matched
 *  to HR's actual cutoffs (Terence at 54.5/100 → Conditional Advance). */
export function compositeToRecommendation(
  scoreOutOf100: number,
  thresholds: { strong: number; match: number; consider: number },
): Recommendation {
  // thresholds are 0..1; scale to 0..100
  const s = scoreOutOf100;
  if (s >= thresholds.strong * 100) return "strong_hire";
  if (s >= thresholds.match * 100) return "hire";
  if (s >= thresholds.consider * 100) return "conditional_advance";
  if (s >= thresholds.consider * 100 * 0.7) return "consider";
  return "do_not_advance";
}

/** Full pre-screening report shape produced by the agent. Persisted as the
 *  ApplicationScore.breakdown JSON. */
export interface FullPreScreeningReport {
  scoreOutOf100: number;       // weighted composite, HR uses /100
  scoreOutOf10: number;        // /10 derived for display
  recommendation: Recommendation;
  candidateSnapshot: Array<{ label: string; value: string | null }>;
  careerArc: { phases: Array<{ title: string; narrative: string }> };
  scorecard: Array<{
    key: string;
    label: string;
    weight: number;             // 0..1 (matches rubric criterion weight)
    score: number;              // 0..10
    commentary: string;
  }>;
  positioningSummary: string;
  structuralGaps: Array<{ title: string; detail: string }>;
  whyToHire: string[];
  riskRegister: Array<{
    risk: string;
    severity: RiskSeverity;
    detail: string;
    mitigation: string;
  }>;
  interviewQuestions: Array<{ theme: string; question: string; listenFor: string }>;
  decisionFramework: Array<{ outcome: string; recommendation: string }>;
  compensation: Array<{ component: string; proposed: string; rationale: string }>;
  onboardingPlan: Array<{
    phase: string; // e.g. "Days 1–14"
    title: string;
    narrative: string;
  }>;
  finalAssessment: string;
}

/** Type guard — distinguishes new full-report breakdown from the legacy
 *  thin shape `[{criterionKey, score, reasoning}]`. */
export function isFullReport(x: unknown): x is FullPreScreeningReport {
  return (
    typeof x === "object" &&
    x !== null &&
    "scorecard" in x &&
    Array.isArray((x as { scorecard?: unknown }).scorecard)
  );
}

/** Future shape — Phase 1.C will produce this from interview transcripts. */
export interface PostInterviewReport {
  postScoreOutOf100: number;
  postScoreOutOf10: number;
  postRecommendation: Recommendation;
  interviewSummary: {
    date: string;
    format: string;
    interviewer: string;
    durationMin: number;
    location?: string;
  };
  interviewContext: string;
  interviewScorecard: Array<{
    key: string;
    label: string;
    score: number; // 0..10
    evidence: string;
    quotes: string[];
  }>;
  criticalFindings: Array<{ index: number; title: string; body: string }>;
  preVsPostComparison: Array<{
    dimension: string;
    preScore: number | null;
    postScore: number;
    whatChanged: string;
  }>;
  mitigatingFactors: string[];
  finalRecommendation: string;
}

export function isPostInterviewReport(x: unknown): x is PostInterviewReport {
  return (
    typeof x === "object" &&
    x !== null &&
    "interviewScorecard" in x &&
    Array.isArray((x as { interviewScorecard?: unknown }).interviewScorecard)
  );
}

export const RECRUITMENT_INTAKE_AGENCY = "recruitment_intake_agency";
export const RECRUITMENT_INTAKE_DIRECT = "recruitment_intake_direct";

export function isRecruitmentIntakeFormType(formType: string | null | undefined): boolean {
  return formType === RECRUITMENT_INTAKE_AGENCY || formType === RECRUITMENT_INTAKE_DIRECT;
}

```