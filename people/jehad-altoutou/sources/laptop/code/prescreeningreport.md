---
type: source
source_type: laptop
title: PreScreeningReport
slug: prescreeningreport
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/PreScreeningReport.tsx"
original_size: 14437
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# PreScreeningReport

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/PreScreeningReport.tsx` on 2026-05-14._

```tsx
// Phase 1.B v2: HR-equivalent pre-screening report renderer.
// Server component — receives the parsed FullPreScreeningReport JSON and
// renders the same structure HR delivers in her Word documents (candidate
// snapshot, career arc, weighted scorecard, structural gaps, why to hire,
// risk register, interview questions, decision framework, compensation,
// onboarding plan, final assessment).

import {
  RECOMMENDATION_LABEL,
  RECOMMENDATION_COLOR,
  RISK_SEVERITY_COLOR,
  type FullPreScreeningReport,
  type Recommendation,
  type RiskSeverity,
} from "@/lib/recruitment";

export function PreScreeningReport({ report }: { report: FullPreScreeningReport }) {
  return (
    <section className="rounded-xl border border-zinc-200 bg-white p-0 dark:border-zinc-800 dark:bg-zinc-900">
      {/* Header */}
      <div className="border-b border-zinc-200 px-6 py-5 dark:border-zinc-800">
        <div className="mb-1 text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
          Confidential — Pre-Interview Assessment Package
        </div>
        <div className="flex flex-wrap items-end justify-between gap-3">
          <h2 className="text-lg font-semibold tracking-tight">Pre-screening report</h2>
          <div className="flex items-center gap-3">
            <div className="text-right">
              <div className="text-[10px] uppercase tracking-wide text-zinc-500">Composite</div>
              <div className="text-2xl font-bold tabular-nums">
                {report.scoreOutOf100.toFixed(1)}
                <span className="text-sm font-medium text-zinc-500">/100</span>
              </div>
            </div>
            <div className="text-right">
              <div className="text-[10px] uppercase tracking-wide text-zinc-500">Score</div>
              <div className="text-2xl font-bold tabular-nums">
                {report.scoreOutOf10.toFixed(1)}
                <span className="text-sm font-medium text-zinc-500">/10</span>
              </div>
            </div>
            <span
              className={`inline-flex items-center rounded-full px-3 py-1.5 text-xs font-semibold ${RECOMMENDATION_COLOR[report.recommendation as Recommendation] ?? ""}`}
            >
              {RECOMMENDATION_LABEL[report.recommendation as Recommendation] ?? report.recommendation}
            </span>
          </div>
        </div>
      </div>

      {/* Candidate Snapshot */}
      {report.candidateSnapshot.length > 0 && (
        <Section title="Candidate Snapshot">
          <dl className="grid grid-cols-1 gap-x-6 gap-y-2 sm:grid-cols-2">
            {report.candidateSnapshot.map((row, i) => (
              <div key={i} className="flex justify-between gap-3 border-b border-zinc-100 py-1.5 text-xs dark:border-zinc-800">
                <dt className="text-zinc-500">{row.label}</dt>
                <dd className="max-w-[60%] text-right">{row.value || "—"}</dd>
              </div>
            ))}
          </dl>
        </Section>
      )}

      {/* Career Arc */}
      {report.careerArc.phases.length > 0 && (
        <Section title="Career Arc & Relevance">
          <ol className="space-y-3">
            {report.careerArc.phases.map((p, i) => (
              <li key={i} className="rounded-lg border border-zinc-100 bg-zinc-50/50 p-3 dark:border-zinc-800 dark:bg-zinc-800/30">
                <h4 className="text-xs font-semibold">{p.title}</h4>
                <p className="mt-1.5 whitespace-pre-wrap text-xs text-zinc-700 dark:text-zinc-300">
                  {p.narrative}
                </p>
              </li>
            ))}
          </ol>
        </Section>
      )}

      {/* Weighted Scorecard */}
      {report.scorecard.length > 0 && (
        <Section title="Weighted Scorecard">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-2 py-2 text-left font-medium">#</th>
                  <th className="px-3 py-2 text-left font-medium">Dimension</th>
                  <th className="px-3 py-2 text-right font-medium">Weight</th>
                  <th className="px-3 py-2 text-right font-medium">Score</th>
                  <th className="px-3 py-2 text-left font-medium">Commentary</th>
                </tr>
              </thead>
              <tbody>
                {report.scorecard.map((row, i) => (
                  <tr key={row.key} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-2 py-2 align-top text-zinc-500 tabular-nums">{i + 1}</td>
                    <td className="px-3 py-2 align-top font-medium">{row.label}</td>
                    <td className="px-3 py-2 align-top text-right tabular-nums">
                      {(row.weight * 100).toFixed(0)}%
                    </td>
                    <td className="px-3 py-2 align-top text-right">
                      <span className={scorePillClass(row.score)}>{row.score.toFixed(1)}</span>
                    </td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{row.commentary}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {/* Positioning Summary */}
      {report.positioningSummary && (
        <Section title="Candidate Positioning Summary">
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
            {report.positioningSummary}
          </p>
        </Section>
      )}

      {/* Structural Gaps */}
      {report.structuralGaps.length > 0 && (
        <Section title="Structural Gaps">
          <ol className="space-y-3">
            {report.structuralGaps.map((g, i) => (
              <li
                key={i}
                className="rounded-lg border-l-4 border-rose-400 bg-rose-50/50 px-4 py-3 dark:border-rose-700 dark:bg-rose-950/30"
              >
                <h4 className="text-sm font-semibold">{g.title}</h4>
                <p className="mt-1 text-xs text-zinc-700 dark:text-zinc-300">{g.detail}</p>
              </li>
            ))}
          </ol>
        </Section>
      )}

      {/* Why to Hire */}
      {report.whyToHire.length > 0 && (
        <Section title="Why to Hire — The Case For">
          <ul className="space-y-2 rounded-lg border-l-4 border-emerald-400 bg-emerald-50/50 px-4 py-3 dark:border-emerald-700 dark:bg-emerald-950/30">
            {report.whyToHire.map((b, i) => (
              <li key={i} className="text-xs text-zinc-700 dark:text-zinc-300">
                <span className="mr-2 text-emerald-600">•</span>
                {b}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {/* Risk Register */}
      {report.riskRegister.length > 0 && (
        <Section title="Red Flags & Risk Register">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-2 py-2 text-left font-medium">#</th>
                  <th className="px-3 py-2 text-left font-medium">Risk</th>
                  <th className="px-3 py-2 text-left font-medium">Severity</th>
                  <th className="px-3 py-2 text-left font-medium">Detail</th>
                  <th className="px-3 py-2 text-left font-medium">Mitigation</th>
                </tr>
              </thead>
              <tbody>
                {report.riskRegister.map((r, i) => (
                  <tr key={i} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-2 py-2 align-top text-zinc-500 tabular-nums">{i + 1}</td>
                    <td className="px-3 py-2 align-top font-medium">{r.risk}</td>
                    <td className="px-3 py-2 align-top">
                      <span
                        className={`inline-flex items-center rounded border px-1.5 py-0.5 text-[10px] font-semibold ${RISK_SEVERITY_COLOR[r.severity as RiskSeverity] ?? ""}`}
                      >
                        {r.severity}
                      </span>
                    </td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{r.detail}</td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{r.mitigation}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {/* Interview Questions */}
      {report.interviewQuestions.length > 0 && (
        <Section title="Recommended Interview Questions">
          <div className="space-y-3">
            {report.interviewQuestions.map((q, i) => (
              <div key={i} className="rounded-lg border border-zinc-200 p-3 dark:border-zinc-800">
                <div className="text-[10px] font-semibold uppercase tracking-wide text-zinc-500">
                  {q.theme}
                </div>
                <p className="mt-1 text-xs font-medium">{q.question}</p>
                <p className="mt-2 rounded bg-zinc-50 p-2 text-[11px] text-zinc-700 dark:bg-zinc-800/50 dark:text-zinc-300">
                  <strong className="text-zinc-500">Listen for:</strong> {q.listenFor}
                </p>
              </div>
            ))}
          </div>
        </Section>
      )}

      {/* Decision Framework */}
      {report.decisionFramework.length > 0 && (
        <Section title="Post-Interview Decision Framework">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-3 py-2 text-left font-medium">Interview Outcome</th>
                  <th className="px-3 py-2 text-left font-medium">Recommendation</th>
                </tr>
              </thead>
              <tbody>
                {report.decisionFramework.map((d, i) => (
                  <tr key={i} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-3 py-2 align-top font-medium">{d.outcome}</td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{d.recommendation}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {/* Compensation */}
      {report.compensation.length > 0 && (
        <Section title="Recommended Compensation Structure">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-3 py-2 text-left font-medium">Component</th>
                  <th className="px-3 py-2 text-left font-medium">Proposed</th>
                  <th className="px-3 py-2 text-left font-medium">Rationale</th>
                </tr>
              </thead>
              <tbody>
                {report.compensation.map((c, i) => (
                  <tr key={i} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-3 py-2 align-top font-medium">{c.component}</td>
                    <td className="px-3 py-2 align-top">{c.proposed}</td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{c.rationale}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {/* Onboarding Plan */}
      {report.onboardingPlan.length > 0 && (
        <Section title="Onboarding Plan (First 90 Days)">
          <ol className="space-y-3">
            {report.onboardingPlan.map((p, i) => (
              <li key={i} className="rounded-lg border border-zinc-200 p-3 dark:border-zinc-800">
                <div className="flex items-center gap-2">
                  <span className="inline-flex items-center rounded bg-zinc-100 px-1.5 py-0.5 text-[10px] font-semibold text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
                    {p.phase}
                  </span>
                  <h4 className="text-xs font-semibold">{p.title}</h4>
                </div>
                <p className="mt-2 whitespace-pre-wrap text-xs text-zinc-700 dark:text-zinc-300">
                  {p.narrative}
                </p>
              </li>
            ))}
          </ol>
        </Section>
      )}

      {/* Final Assessment */}
      {report.finalAssessment && (
        <Section title="Final Assessment">
          <p className="whitespace-pre-wrap rounded-lg border-l-4 border-zinc-300 bg-zinc-50/50 p-4 text-sm italic leading-relaxed text-zinc-700 dark:border-zinc-600 dark:bg-zinc-800/30 dark:text-zinc-300">
            {report.finalAssessment}
          </p>
        </Section>
      )}
    </section>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="border-b border-zinc-100 px-6 py-5 last:border-b-0 dark:border-zinc-800">
      <h3 className="mb-3 text-xs font-semibold uppercase tracking-wider text-zinc-500">{title}</h3>
      {children}
    </section>
  );
}

function scorePillClass(score: number): string {
  // 0-10 scale matching HR's report
  let bg = "bg-zinc-100 text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300";
  if (score >= 8) bg = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200";
  else if (score >= 6.5) bg = "bg-green-100 text-green-900 dark:bg-green-950 dark:text-green-200";
  else if (score >= 5) bg = "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200";
  else if (score >= 3) bg = "bg-orange-100 text-orange-900 dark:bg-orange-950 dark:text-orange-200";
  else bg = "bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200";
  return `inline-flex min-w-[3em] items-center justify-center rounded px-2 py-0.5 text-xs font-bold tabular-nums ${bg}`;
}

```