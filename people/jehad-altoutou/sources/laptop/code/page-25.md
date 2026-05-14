---
type: source
source_type: laptop
title: page
slug: page-25
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/sessions/[sessionId]/page.tsx"
original_size: 17329
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/sessions/[sessionId]/page.tsx` on 2026-05-14._

```tsx
import { requireAuth } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { notFound } from "next/navigation";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { ArrowLeft, CheckCircle, XCircle, AlertTriangle, FileDown, Info } from "lucide-react";
import Link from "next/link";

export default async function SessionDetailPage({
  params,
}: {
  params: Promise<{ sessionId: string }>;
}) {
  await requireAuth();
  const { sessionId } = await params;

  const session = await prisma.candidateSession.findUnique({
    where: { id: sessionId },
    include: {
      version: {
        include: {
          template: { include: { jobRole: { include: { department: true } } } },
          sections: { orderBy: { sortOrder: "asc" } },
        },
      },
      responses: {
        include: {
          question: { include: { options: true, competencies: { include: { competency: true } } } },
          section: true,
        },
        orderBy: { answeredAt: "asc" },
      },
      result: true,
      sectionScores: { include: { section: true } },
      competencyScores: { include: { competency: true } },
      analyticsEvents: { orderBy: { timestamp: "asc" }, take: 50 },
    },
  });

  if (!session) notFound();

  const recommendationColors: Record<string, string> = {
    strong_hire: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
    hire: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
    consider: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
    weak_fit: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
    reject: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center gap-4">
        <Link
          href="/admin/sessions"
          className="rounded-lg p-1.5 text-muted-foreground transition-colors hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
        >
          <ArrowLeft className="size-5" />
        </Link>
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">
            {session.candidateName}
          </h1>
          <p className="text-sm text-muted-foreground">
            {session.candidateEmail} &middot;{" "}
            {session.version.template.title} v{session.version.versionNumber}
          </p>
        </div>
        <a
          href={`/api/admin/sessions/${sessionId}/pdf`}
          target="_blank"
          className="ml-auto inline-flex items-center gap-2 rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-zinc-800 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-200"
        >
          <FileDown className="size-4" />
          Export PDF
        </a>
      </div>

      {/* Result Summary */}
      {session.result && (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <Card>
            <CardContent className="pt-2">
              <p className="text-xs text-muted-foreground">Overall Score</p>
              <p className="text-3xl font-bold">
                {Math.round(session.result.normalizedScore * 100)}%
              </p>
              <p className="text-xs text-muted-foreground">
                {session.result.totalScore}/{session.result.maxScore} points
              </p>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-2">
              <p className="text-xs text-muted-foreground">Recommendation</p>
              <span
                className={`mt-1 inline-flex items-center rounded-full px-3 py-1 text-sm font-semibold ${
                  recommendationColors[session.result.recommendation] ?? ""
                }`}
              >
                {session.result.recommendation.replace(/_/g, " ")}
              </span>
            </CardContent>
          </Card>
          <Card className="overflow-visible">
            <CardContent className="pt-2">
              <div className="flex items-center gap-1.5">
                <p className="text-xs text-muted-foreground">Confidence</p>
                <div className="group relative">
                  <Info className="size-3 cursor-help text-muted-foreground/60" />
                  <div className="pointer-events-none absolute left-0 top-full z-[100] mt-2 w-72 rounded-xl border border-zinc-200 bg-white p-3.5 text-xs leading-relaxed text-zinc-600 opacity-0 shadow-xl transition-opacity group-hover:pointer-events-auto group-hover:opacity-100 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-400">
                    <div className="absolute -top-1.5 left-3 h-3 w-3 rotate-45 border-l border-t border-zinc-200 bg-white dark:border-zinc-700 dark:bg-zinc-900" />
                    <p className="mb-1.5 font-semibold text-zinc-900 dark:text-zinc-100">How is confidence calculated?</p>
                    <p>Confidence reflects how reliable the overall score is, based on two factors:</p>
                    <ul className="mt-1.5 list-inside list-disc space-y-0.5">
                      <li><strong>Completion rate (40%)</strong> — did the candidate answer all questions?</li>
                      <li><strong>Score consistency (60%)</strong> — how uniform were scores across sections? Low variance = high consistency.</li>
                    </ul>
                    <p className="mt-1.5">A higher confidence means the result is more trustworthy for hiring decisions.</p>
                  </div>
                </div>
              </div>
              <p className="text-3xl font-bold">
                {Math.round((session.result.confidenceRating ?? 0) * 100)}%
              </p>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="pt-2">
              <p className="text-xs text-muted-foreground">Status</p>
              <Badge variant="default" className="mt-1">
                {session.status.replace(/_/g, " ")}
              </Badge>
              {session.completedAt && (
                <p className="mt-1 text-xs text-muted-foreground">
                  {new Date(session.completedAt).toLocaleDateString()}
                </p>
              )}
            </CardContent>
          </Card>
        </div>
      )}

      {/* Hiring Summary */}
      {session.result?.hiringSummary && (
        <Card>
          <CardHeader>
            <CardTitle>Hiring Summary</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm leading-relaxed">
              {session.result.hiringSummary}
            </p>
            {session.result.flags && (
              <div className="mt-3 flex flex-wrap gap-2">
                {JSON.parse(session.result.flags).map((flag: string) => (
                  <span
                    key={flag}
                    className="inline-flex items-center gap-1 rounded-full bg-amber-50 px-2.5 py-0.5 text-xs font-medium text-amber-700 dark:bg-amber-950 dark:text-amber-300"
                  >
                    <AlertTriangle className="size-3" />
                    {flag.replace(/_/g, " ")}
                  </span>
                ))}
              </div>
            )}
            {session.result.automationLabels && (
              <div className="mt-2 flex flex-wrap gap-2">
                {JSON.parse(session.result.automationLabels).map(
                  (label: string) => (
                    <Badge key={label} variant="secondary">
                      {label.replace(/_/g, " ")}
                    </Badge>
                  )
                )}
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* Section Scores */}
      {session.sectionScores.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Section Scores</CardTitle>
            <CardDescription>Performance by assessment section</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {session.sectionScores.map((ss) => (
                <div key={ss.id}>
                  <div className="mb-1 flex items-center justify-between">
                    <span className="text-sm font-medium">
                      {ss.section.title}
                    </span>
                    <span className="text-sm font-semibold">
                      {Math.round(ss.normalizedScore * 100)}%
                    </span>
                  </div>
                  <div className="h-2 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                    <div
                      className="h-full rounded-full bg-primary transition-all"
                      style={{
                        width: `${Math.round(ss.normalizedScore * 100)}%`,
                      }}
                    />
                  </div>
                  <p className="mt-0.5 text-xs text-muted-foreground">
                    {ss.score}/{ss.maxScore} pts &middot; weight:{" "}
                    {ss.section.weight}
                  </p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Competency Scores */}
      {session.competencyScores.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Competency Scores</CardTitle>
            <CardDescription>
              Performance by assessed competency
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {session.competencyScores
                .sort((a, b) => b.normalizedScore - a.normalizedScore)
                .map((cs) => (
                  <div
                    key={cs.id}
                    className="rounded-lg border border-zinc-100 p-3 dark:border-zinc-800"
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-medium">
                        {cs.competency.name}
                      </span>
                      <span
                        className={`text-sm font-bold ${
                          cs.normalizedScore >= 0.7
                            ? "text-green-600"
                            : cs.normalizedScore >= 0.5
                              ? "text-amber-600"
                              : "text-red-600"
                        }`}
                      >
                        {Math.round(cs.normalizedScore * 100)}%
                      </span>
                    </div>
                    <div className="mt-2 h-1.5 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                      <div
                        className={`h-full rounded-full transition-all ${
                          cs.normalizedScore >= 0.7
                            ? "bg-green-500"
                            : cs.normalizedScore >= 0.5
                              ? "bg-amber-500"
                              : "bg-red-500"
                        }`}
                        style={{
                          width: `${Math.round(cs.normalizedScore * 100)}%`,
                        }}
                      />
                    </div>
                    <p className="mt-1 text-xs text-muted-foreground">
                      {cs.score}/{cs.maxScore} pts
                    </p>
                  </div>
                ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Individual Responses */}
      <Card>
        <CardHeader>
          <CardTitle>Question Responses</CardTitle>
          <CardDescription>
            Detailed breakdown of each answer
          </CardDescription>
        </CardHeader>
        <CardContent className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Section</TableHead>
                <TableHead>Question</TableHead>
                <TableHead>Answer</TableHead>
                <TableHead>Score</TableHead>
                <TableHead>Time</TableHead>
                <TableHead>Flags</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {session.responses.map((resp) => {
                const selectedKeys = resp.selectedOptions
                  ? JSON.parse(resp.selectedOptions)
                  : [];
                const selectedLabels = resp.question.options
                  .filter((o) => selectedKeys.includes(o.key))
                  .map((o) => o.label);
                const correctKeys = resp.question.options
                  .filter((o) => o.isCorrect)
                  .map((o) => o.key);
                const isFullyCorrect =
                  selectedKeys.length === correctKeys.length &&
                  selectedKeys.every((k: string) => correctKeys.includes(k));

                return (
                  <TableRow key={resp.id}>
                    <TableCell className="text-xs">
                      {resp.section.title}
                    </TableCell>
                    <TableCell>
                      <p className="max-w-xs truncate text-sm font-medium">
                        {resp.question.title}
                      </p>
                    </TableCell>
                    <TableCell>
                      <div className="max-w-xs">
                        {selectedLabels.length > 0 ? (
                          selectedLabels.map((label: string, i: number) => (
                            <p key={i} className="truncate text-xs">
                              {label}
                            </p>
                          ))
                        ) : resp.freeTextResponse ? (
                          <p className="truncate text-xs">
                            {resp.freeTextResponse}
                          </p>
                        ) : (
                          <span className="text-xs text-muted-foreground">
                            (ranking/drag)
                          </span>
                        )}
                      </div>
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center gap-1.5">
                        {isFullyCorrect ? (
                          <CheckCircle className="size-3.5 text-green-500" />
                        ) : resp.earnedPoints > 0 ? (
                          <AlertTriangle className="size-3.5 text-amber-500" />
                        ) : (
                          <XCircle className="size-3.5 text-red-500" />
                        )}
                        <span className="text-sm font-medium">
                          {resp.earnedPoints}/{resp.maxPoints}
                        </span>
                      </div>
                    </TableCell>
                    <TableCell className="text-xs text-muted-foreground">
                      {resp.timeSpent}s
                    </TableCell>
                    <TableCell>
                      {resp.flaggedIndicators &&
                        JSON.parse(resp.flaggedIndicators).map(
                          (flag: string) => (
                            <Badge
                              key={flag}
                              variant="destructive"
                              className="mr-1 text-[10px]"
                            >
                              {flag}
                            </Badge>
                          )
                        )}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Analytics Events */}
      <Card>
        <CardHeader>
          <CardTitle>Session Timeline</CardTitle>
          <CardDescription>Analytics events for this session</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-2">
            {session.analyticsEvents.map((evt) => (
              <div
                key={evt.id}
                className="flex items-center gap-3 text-xs text-muted-foreground"
              >
                <span className="w-20 flex-shrink-0 text-right font-mono">
                  {new Date(evt.timestamp).toLocaleTimeString()}
                </span>
                <div className="h-2 w-2 flex-shrink-0 rounded-full bg-primary" />
                <span className="font-medium text-foreground">
                  {evt.eventType.replace(/_/g, " ")}
                </span>
                {evt.eventData && (
                  <span className="truncate">
                    {evt.eventData.substring(0, 80)}
                  </span>
                )}
              </div>
            ))}
            {session.analyticsEvents.length === 0 && (
              <p className="text-sm text-muted-foreground">No events recorded.</p>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

```