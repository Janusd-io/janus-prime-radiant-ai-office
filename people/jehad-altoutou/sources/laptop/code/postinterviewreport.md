---
type: source
source_type: laptop
title: PostInterviewReport
slug: postinterviewreport
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/PostInterviewReport.tsx"
original_size: 9444
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# PostInterviewReport

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/PostInterviewReport.tsx` on 2026-05-14._

```tsx
import {
  RECOMMENDATION_COLOR,
  RECOMMENDATION_LABEL,
  type PostInterviewReport as PostInterviewReportShape,
  type Recommendation,
} from "@/lib/recruitment";

export function PostInterviewReport({ report }: { report: PostInterviewReportShape }) {
  return (
    <section className="rounded-xl border border-zinc-200 bg-white p-0 dark:border-zinc-800 dark:bg-zinc-900">
      <div className="border-b border-zinc-200 px-6 py-5 dark:border-zinc-800">
        <div className="mb-1 text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
          Confidential - Post-Interview Assessment Package
        </div>
        <div className="flex flex-wrap items-end justify-between gap-3">
          <h2 className="text-lg font-semibold tracking-tight">Post-interview report</h2>
          <div className="flex items-center gap-3">
            <div className="text-right">
              <div className="text-[10px] uppercase tracking-wide text-zinc-500">Composite</div>
              <div className="text-2xl font-bold tabular-nums">
                {report.postScoreOutOf100.toFixed(1)}
                <span className="text-sm font-medium text-zinc-500">/100</span>
              </div>
            </div>
            <div className="text-right">
              <div className="text-[10px] uppercase tracking-wide text-zinc-500">Score</div>
              <div className="text-2xl font-bold tabular-nums">
                {report.postScoreOutOf10.toFixed(1)}
                <span className="text-sm font-medium text-zinc-500">/10</span>
              </div>
            </div>
            <span
              className={`inline-flex items-center rounded-full px-3 py-1.5 text-xs font-semibold ${RECOMMENDATION_COLOR[report.postRecommendation as Recommendation] ?? ""}`}
            >
              {RECOMMENDATION_LABEL[report.postRecommendation as Recommendation] ?? report.postRecommendation}
            </span>
          </div>
        </div>
      </div>

      <Section title="Interview Summary">
        <dl className="grid grid-cols-1 gap-x-6 gap-y-2 sm:grid-cols-2">
          <SummaryField label="Date" value={report.interviewSummary.date} />
          <SummaryField label="Format" value={report.interviewSummary.format} />
          <SummaryField label="Interviewer" value={report.interviewSummary.interviewer} />
          <SummaryField label="Duration" value={report.interviewSummary.durationMin ? `${report.interviewSummary.durationMin} min` : "Not specified"} />
          {report.interviewSummary.location && <SummaryField label="Location" value={report.interviewSummary.location} />}
        </dl>
      </Section>

      {report.interviewContext && (
        <Section title="Interview Context">
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
            {report.interviewContext}
          </p>
        </Section>
      )}

      {report.interviewScorecard.length > 0 && (
        <Section title="Interview Scorecard">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-2 py-2 text-left font-medium">#</th>
                  <th className="px-3 py-2 text-left font-medium">Dimension</th>
                  <th className="px-3 py-2 text-right font-medium">Score</th>
                  <th className="px-3 py-2 text-left font-medium">Evidence</th>
                  <th className="px-3 py-2 text-left font-medium">Signals</th>
                </tr>
              </thead>
              <tbody>
                {report.interviewScorecard.map((row, i) => (
                  <tr key={row.key} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-2 py-2 align-top text-zinc-500 tabular-nums">{i + 1}</td>
                    <td className="px-3 py-2 align-top font-medium">{row.label}</td>
                    <td className="px-3 py-2 align-top text-right">
                      <span className={scorePillClass(row.score)}>{row.score.toFixed(1)}</span>
                    </td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{row.evidence}</td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">
                      {row.quotes.length > 0 ? (
                        <ul className="space-y-1">
                          {row.quotes.map((quote, quoteIndex) => (
                            <li key={quoteIndex}>{quote}</li>
                          ))}
                        </ul>
                      ) : (
                        <span className="text-zinc-400">-</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {report.criticalFindings.length > 0 && (
        <Section title="Critical Findings">
          <ol className="space-y-3">
            {report.criticalFindings.map((finding, i) => (
              <li key={i} className="rounded-lg border border-zinc-200 p-3 dark:border-zinc-800">
                <h4 className="text-sm font-semibold">
                  {finding.index}. {finding.title}
                </h4>
                <p className="mt-1 text-xs text-zinc-700 dark:text-zinc-300">{finding.body}</p>
              </li>
            ))}
          </ol>
        </Section>
      )}

      {report.preVsPostComparison.length > 0 && (
        <Section title="Pre vs Post Comparison">
          <div className="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
            <table className="w-full text-xs">
              <thead className="bg-zinc-50 text-zinc-500 dark:bg-zinc-800/50">
                <tr>
                  <th className="px-3 py-2 text-left font-medium">Dimension</th>
                  <th className="px-3 py-2 text-right font-medium">Pre</th>
                  <th className="px-3 py-2 text-right font-medium">Post</th>
                  <th className="px-3 py-2 text-left font-medium">What changed</th>
                </tr>
              </thead>
              <tbody>
                {report.preVsPostComparison.map((row, i) => (
                  <tr key={i} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-3 py-2 align-top font-medium">{row.dimension}</td>
                    <td className="px-3 py-2 align-top text-right tabular-nums">
                      {row.preScore == null ? "-" : row.preScore.toFixed(1)}
                    </td>
                    <td className="px-3 py-2 align-top text-right tabular-nums">{row.postScore.toFixed(1)}</td>
                    <td className="px-3 py-2 align-top text-zinc-700 dark:text-zinc-300">{row.whatChanged}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Section>
      )}

      {report.mitigatingFactors.length > 0 && (
        <Section title="Mitigating Factors">
          <ul className="space-y-2 rounded-lg border-l-4 border-emerald-400 bg-emerald-50/50 px-4 py-3 dark:border-emerald-700 dark:bg-emerald-950/30">
            {report.mitigatingFactors.map((factor, i) => (
              <li key={i} className="text-xs text-zinc-700 dark:text-zinc-300">
                <span className="mr-2 text-emerald-600">-</span>
                {factor}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {report.finalRecommendation && (
        <Section title="Final Recommendation">
          <p className="whitespace-pre-wrap rounded-lg border-l-4 border-zinc-300 bg-zinc-50/50 p-4 text-sm italic leading-relaxed text-zinc-700 dark:border-zinc-600 dark:bg-zinc-800/30 dark:text-zinc-300">
            {report.finalRecommendation}
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

function SummaryField({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex justify-between gap-3 border-b border-zinc-100 py-1.5 text-xs dark:border-zinc-800">
      <dt className="text-zinc-500">{label}</dt>
      <dd className="max-w-[60%] text-right">{value || "-"}</dd>
    </div>
  );
}

function scorePillClass(score: number): string {
  let bg = "bg-zinc-100 text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300";
  if (score >= 8) bg = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200";
  else if (score >= 6.5) bg = "bg-green-100 text-green-900 dark:bg-green-950 dark:text-green-200";
  else if (score >= 5) bg = "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200";
  else if (score >= 3) bg = "bg-orange-100 text-orange-900 dark:bg-orange-950 dark:text-orange-200";
  else bg = "bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200";
  return `inline-flex min-w-[3em] items-center justify-center rounded px-2 py-0.5 text-xs font-bold tabular-nums ${bg}`;
}

```