---
type: source
source_type: laptop
title: page
slug: page-31
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/analytics/page.tsx
original_size: 18986
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/analytics/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {  } from "@/components/ui/button";
import {
} from "@/components/ui/select";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  BarChart3,
  Users,
  Send,
  CheckCircle,
  TrendingUp,
  Target,
  Clock,
  AlertTriangle,
  Loader2,
  ArrowLeft,
  Building2,
} from "lucide-react";

interface OverviewData {
  totalSessions: number;
  completedSessions: number;
  completionRate: number;
  totalInvites: number;
  pendingInvites: number;
  totalResults: number;
  avgScore: number;
  recommendationDistribution: Record<string, number>;
  assessments: Array<{
    id: string;
    title: string;
    department: string;
    departmentSlug: string;
    jobRole: string;
    versionId: string | null;
    status: string;
    candidates: number;
    questions: number;
  }>;
}

interface FunnelData {
  total: number;
  started: number;
  completed: number;
  completionRate: number;
  dropOffRate: number;
}

interface QuestionStat {
  questionId: string;
  slug: string;
  title: string;
  avgScore: number;
  avgTime: number;
  failRate: number;
  attempts: number;
}

interface CompetencyStat {
  slug: string;
  name: string;
  avgScore: number;
  count: number;
}

interface DistributionData {
  distribution: Record<string, number>;
  totalCandidates: number;
  avgScore: number;
}

const recColors: Record<string, { bg: string; text: string; bar: string }> = {
  strong_hire: { bg: "bg-emerald-50 dark:bg-emerald-950", text: "text-emerald-700 dark:text-emerald-300", bar: "bg-emerald-500" },
  hire: { bg: "bg-green-50 dark:bg-green-950", text: "text-green-700 dark:text-green-300", bar: "bg-green-500" },
  consider: { bg: "bg-amber-50 dark:bg-amber-950", text: "text-amber-700 dark:text-amber-300", bar: "bg-amber-500" },
  weak_fit: { bg: "bg-orange-50 dark:bg-orange-950", text: "text-orange-700 dark:text-orange-300", bar: "bg-orange-500" },
  reject: { bg: "bg-red-50 dark:bg-red-950", text: "text-red-700 dark:text-red-300", bar: "bg-red-500" },
};

export default function AnalyticsPage() {
  const [overview, setOverview] = useState<OverviewData | null>(null);
  const [loading, setLoading] = useState(true);
  const [selectedVersionId, setSelectedVersionId] = useState<string | null>(null);
  const [drilldown, setDrilldown] = useState<{
    funnel: FunnelData | null;
    questions: QuestionStat[];
    competencies: CompetencyStat[];
    distribution: DistributionData | null;
  } | null>(null);
  const [drilldownLoading, setDrilldownLoading] = useState(false);

  useEffect(() => {
    fetch("/api/admin/analytics?type=overview")
      .then((r) => r.json())
      .then((d) => { setOverview(d.data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const loadDrilldown = async (versionId: string) => {
    setSelectedVersionId(versionId);
    setDrilldownLoading(true);
    const [f, q, c, dist] = await Promise.all([
      fetch(`/api/admin/analytics?type=funnel&versionId=${versionId}`).then((r) => r.json()),
      fetch(`/api/admin/analytics?type=questions&versionId=${versionId}`).then((r) => r.json()),
      fetch(`/api/admin/analytics?type=competencies&versionId=${versionId}`).then((r) => r.json()),
      fetch(`/api/admin/analytics?type=distribution&versionId=${versionId}`).then((r) => r.json()),
    ]);
    setDrilldown({
      funnel: f.data,
      questions: q.data ?? [],
      competencies: c.data ?? [],
      distribution: dist.data,
    });
    setDrilldownLoading(false);
  };

  if (loading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  if (!overview) {
    return (
      <div className="space-y-6">
        <h1 className="text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-muted-foreground">Failed to load analytics data.</p>
      </div>
    );
  }

  const selectedAssessment = overview.assessments.find((a) => a.versionId === selectedVersionId);

  // If drilldown is active, show assessment-specific analytics
  if (selectedVersionId && drilldown) {
    return (
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center gap-4">
          <button
            onClick={() => { setSelectedVersionId(null); setDrilldown(null); }}
            className="rounded-lg p-1.5 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
          >
            <ArrowLeft className="size-5" />
          </button>
          <div className="min-w-0 flex-1">
            <h1 className="text-2xl font-semibold tracking-tight">{selectedAssessment?.title ?? "Assessment"}</h1>
            <p className="text-sm text-muted-foreground">
              {selectedAssessment?.department} — {selectedAssessment?.jobRole}
            </p>
          </div>
        </div>

        {drilldownLoading ? (
          <div className="flex items-center justify-center py-12">
            <Loader2 className="size-8 animate-spin text-primary" />
          </div>
        ) : (
          <>
            {/* Funnel */}
            {drilldown.funnel && (
              <div className="grid grid-cols-2 gap-4 sm:grid-cols-5">
                <StatCard icon={Users} label="Total Sessions" value={drilldown.funnel.total} />
                <StatCard icon={Clock} label="Started" value={drilldown.funnel.started} />
                <StatCard icon={CheckCircle} label="Completed" value={drilldown.funnel.completed} />
                <StatCard icon={TrendingUp} label="Completion Rate" value={`${Math.round(drilldown.funnel.completionRate * 100)}%`} />
                <StatCard icon={AlertTriangle} label="Drop-off Rate" value={`${Math.round(drilldown.funnel.dropOffRate * 100)}%`} accent={drilldown.funnel.dropOffRate > 0.3 ? "red" : undefined} />
              </div>
            )}

            {/* Distribution */}
            {drilldown.distribution && drilldown.distribution.totalCandidates > 0 && (
              <Card>
                <CardHeader>
                  <CardTitle>Result Distribution</CardTitle>
                  <CardDescription>
                    {drilldown.distribution.totalCandidates} candidates — avg score: {Math.round(drilldown.distribution.avgScore * 100)}%
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {Object.entries(drilldown.distribution.distribution).map(([rec, count]) => {
                      const total = drilldown.distribution!.totalCandidates;
                      const pct = total > 0 ? (count / total) * 100 : 0;
                      const colors = recColors[rec] ?? recColors.consider;
                      return (
                        <div key={rec} className="flex items-center gap-4">
                          <span className={`w-28 rounded-full px-2.5 py-0.5 text-center text-xs font-semibold capitalize ${colors.bg} ${colors.text}`}>
                            {rec.replace(/_/g, " ")}
                          </span>
                          <div className="flex-1">
                            <div className="h-3 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                              <div className={`h-full rounded-full transition-all ${colors.bar}`} style={{ width: `${pct}%` }} />
                            </div>
                          </div>
                          <span className="w-12 text-right text-sm font-semibold">{count}</span>
                        </div>
                      );
                    })}
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Competency Heatmap */}
            {drilldown.competencies.length > 0 && (
              <Card>
                <CardHeader>
                  <CardTitle>Competency Performance</CardTitle>
                  <CardDescription>Average scores per competency across all candidates</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
                    {[...drilldown.competencies]
                      .sort((a, b) => b.avgScore - a.avgScore)
                      .map((c) => {
                        const pct = Math.round(c.avgScore * 100);
                        const color = pct >= 70 ? "bg-green-500" : pct >= 50 ? "bg-amber-500" : "bg-red-500";
                        const textColor = pct >= 70 ? "text-green-600" : pct >= 50 ? "text-amber-600" : "text-red-600";
                        return (
                          <div key={c.slug} className="rounded-xl border border-zinc-100 p-4 dark:border-zinc-800">
                            <div className="flex items-center justify-between">
                              <span className="text-sm font-medium">{c.name}</span>
                              <span className={`text-sm font-bold ${textColor}`}>{pct}%</span>
                            </div>
                            <div className="mt-2.5 h-2 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                              <div className={`h-full rounded-full transition-all ${color}`} style={{ width: `${pct}%` }} />
                            </div>
                            <p className="mt-1.5 text-[11px] text-muted-foreground">{c.count} candidates assessed</p>
                          </div>
                        );
                      })}
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Question Analytics */}
            {drilldown.questions.length > 0 && (
              <Card>
                <CardHeader>
                  <CardTitle>Question Performance</CardTitle>
                  <CardDescription>How candidates perform on individual questions</CardDescription>
                </CardHeader>
                <CardContent className="px-4 sm:px-6">
                  <Table>
                    <TableHeader>
                      <TableRow>
                        <TableHead>Question</TableHead>
                        <TableHead>Avg Score</TableHead>
                        <TableHead>Avg Time</TableHead>
                        <TableHead>Fail Rate</TableHead>
                        <TableHead>Attempts</TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {drilldown.questions.map((q) => (
                        <TableRow key={q.questionId}>
                          <TableCell className="max-w-xs truncate text-sm font-medium">{q.title}</TableCell>
                          <TableCell>
                            <span className={`font-semibold ${q.avgScore >= 0.7 ? "text-green-600" : q.avgScore >= 0.5 ? "text-amber-600" : "text-red-600"}`}>
                              {Math.round(q.avgScore * 100)}%
                            </span>
                          </TableCell>
                          <TableCell className="text-muted-foreground">{q.avgTime}s</TableCell>
                          <TableCell>
                            <Badge variant={q.failRate > 0.5 ? "destructive" : "secondary"}>
                              {Math.round(q.failRate * 100)}%
                            </Badge>
                          </TableCell>
                          <TableCell className="text-muted-foreground">{q.attempts}</TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </CardContent>
              </Card>
            )}

            {drilldown.funnel?.total === 0 && (
              <Card>
                <CardContent className="flex flex-col items-center py-12">
                  <BarChart3 className="size-10 text-muted-foreground" />
                  <p className="mt-3 text-sm text-muted-foreground">No candidate data yet for this assessment.</p>
                </CardContent>
              </Card>
            )}
          </>
        )}
      </div>
    );
  }

  // ─── Overview Dashboard ──────────────────────────────────

  const totalRecs = Object.values(overview.recommendationDistribution).reduce((s, n) => s + n, 0);
  const passRate = totalRecs > 0
    ? ((overview.recommendationDistribution.strong_hire ?? 0) + (overview.recommendationDistribution.hire ?? 0)) / totalRecs
    : 0;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Analytics</h1>
        <p className="text-sm text-muted-foreground">
          Platform-wide performance across all departments and assessments.
        </p>
      </div>

      {/* Global KPIs */}
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-6">
        <StatCard icon={Send} label="Total Invites" value={overview.totalInvites} />
        <StatCard icon={Users} label="Sessions" value={overview.totalSessions} />
        <StatCard icon={CheckCircle} label="Completed" value={overview.completedSessions} />
        <StatCard icon={TrendingUp} label="Completion Rate" value={`${Math.round(overview.completionRate * 100)}%`} />
        <StatCard icon={Target} label="Avg Score" value={`${Math.round(overview.avgScore * 100)}%`} />
        <StatCard icon={BarChart3} label="Pass Rate" value={`${Math.round(passRate * 100)}%`} accent={passRate < 0.5 ? "red" : undefined} />
      </div>

      {/* Global Recommendation Distribution */}
      {totalRecs > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Overall Recommendation Distribution</CardTitle>
            <CardDescription>{totalRecs} total results across all assessments</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex gap-3">
              {Object.entries(overview.recommendationDistribution).map(([rec, count]) => {
                const pct = totalRecs > 0 ? (count / totalRecs) * 100 : 0;
                const colors = recColors[rec] ?? recColors.consider;
                return (
                  <div key={rec} className={`flex-1 rounded-xl p-4 text-center ${colors.bg}`}>
                    <p className={`text-2xl font-bold ${colors.text}`}>{count}</p>
                    <p className={`mt-1 text-[11px] font-medium capitalize ${colors.text}`}>{rec.replace(/_/g, " ")}</p>
                    {pct > 0 && <p className="mt-0.5 text-[10px] text-muted-foreground">{Math.round(pct)}%</p>}
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Assessment Breakdown */}
      <Card>
        <CardHeader>
          <CardTitle>Assessments</CardTitle>
          <CardDescription>Click an assessment to see detailed analytics</CardDescription>
        </CardHeader>
        <CardContent>
          {overview.assessments.length === 0 ? (
            <div className="flex flex-col items-center py-8">
              <BarChart3 className="size-10 text-muted-foreground" />
              <p className="mt-3 text-sm text-muted-foreground">No assessments yet.</p>
            </div>
          ) : (
            <div className="space-y-2">
              {overview.assessments.map((a) => (
                <button
                  key={a.id}
                  onClick={() => a.versionId && loadDrilldown(a.versionId)}
                  disabled={!a.versionId}
                  className="flex w-full items-center gap-4 rounded-xl border border-zinc-100 p-4 text-left transition-colors hover:bg-zinc-50 disabled:opacity-50 dark:border-zinc-800 dark:hover:bg-zinc-800/50"
                >
                  <div className="rounded-lg bg-zinc-100 p-2.5 dark:bg-zinc-800">
                    <Building2 className="size-4 text-zinc-600 dark:text-zinc-400" />
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2">
                      <p className="truncate text-sm font-semibold">{a.title}</p>
                      <Badge variant={a.status === "published" ? "default" : "outline"} className="text-[10px]">
                        {a.status}
                      </Badge>
                    </div>
                    <p className="text-xs text-muted-foreground">{a.department} — {a.jobRole}</p>
                  </div>
                  <div className="flex gap-6 text-center">
                    <div>
                      <p className="text-lg font-bold">{a.candidates}</p>
                      <p className="text-[10px] text-muted-foreground">Candidates</p>
                    </div>
                    <div>
                      <p className="text-lg font-bold">{a.questions}</p>
                      <p className="text-[10px] text-muted-foreground">Questions</p>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Pending Invites */}
      {overview.pendingInvites > 0 && (
        <Card>
          <CardContent className="flex items-center gap-4 py-4">
            <div className="rounded-lg bg-amber-50 p-2 dark:bg-amber-950">
              <Send className="size-4 text-amber-600" />
            </div>
            <div>
              <p className="text-sm font-medium">{overview.pendingInvites} pending invite{overview.pendingInvites !== 1 ? "s" : ""}</p>
              <p className="text-xs text-muted-foreground">Candidates who haven&apos;t started their assessment yet.</p>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}

// ─── Stat Card ─────────────────────────────────────────────

function StatCard({
  icon: Icon,
  label,
  value,
  accent,
}: {
  icon: React.ComponentType<{ className?: string }>;
  label: string;
  value: string | number;
  accent?: "red";
}) {
  return (
    <Card>
      <CardContent className="flex items-center gap-3 pt-3">
        <div className={`rounded-lg p-2 ${accent === "red" ? "bg-red-50 dark:bg-red-950" : "bg-zinc-100 dark:bg-zinc-800"}`}>
          <Icon className={`size-4 ${accent === "red" ? "text-red-600" : "text-zinc-600 dark:text-zinc-400"}`} />
        </div>
        <div>
          <p className={`text-xl font-bold ${accent === "red" ? "text-red-600" : ""}`}>{value}</p>
          <p className="text-[10px] text-muted-foreground">{label}</p>
        </div>
      </CardContent>
    </Card>
  );
}

```