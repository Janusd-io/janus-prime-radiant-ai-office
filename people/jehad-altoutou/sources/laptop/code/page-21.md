---
type: source
source_type: laptop
title: page
slug: page-21
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/departments/[slug]/page.tsx"
original_size: 10448
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/departments/[slug]/page.tsx` on 2026-05-14._

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
import {
  ArrowLeft,
  Users,
  CheckCircle,
  Clock,
  TrendingUp,
} from "lucide-react";
import Link from "next/link";
import { formatDistanceToNow } from "date-fns";
import { JobRolesManager } from "@/components/admin/JobRolesManager";
import { DepartmentInterviewerCard } from "@/components/admin/DepartmentInterviewerCard";

const recommendationColors: Record<string, string> = {
  strong_hire: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
  hire: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  consider: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  weak_fit: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  reject: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
};

const statusVariant: Record<string, "default" | "secondary" | "outline" | "destructive"> = {
  completed: "default",
  in_progress: "secondary",
  not_started: "outline",
  expired: "destructive",
  disqualified: "destructive",
};

export default async function DepartmentPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  await requireAuth();
  const { slug } = await params;

  const department = await prisma.department.findUnique({
    where: { slug },
    include: {
      jobRoles: {
        include: {
          assessmentTemplates: {
            include: {
              versions: {
                where: { status: "published" },
                include: {
                  sections: { select: { id: true } },
                  _count: { select: { candidateSessions: true } },
                },
              },
            },
          },
        },
      },
    },
  });

  if (!department) notFound();

  // Get all sessions for this department
  const sessions = await prisma.candidateSession.findMany({
    where: {
      version: {
        template: {
          jobRole: { departmentId: department.id },
        },
      },
    },
    orderBy: { createdAt: "desc" },
    include: {
      version: {
        include: {
          template: { include: { jobRole: true } },
        },
      },
      result: true,
      responses: { select: { id: true } },
    },
  });

  const completed = sessions.filter((s) => s.status === "completed");
  const inProgress = sessions.filter((s) => s.status === "in_progress");
  const results = completed.filter((s) => s.result).map((s) => s.result!);

  const avgScore =
    results.length > 0
      ? results.reduce((sum, r) => sum + r.normalizedScore, 0) / results.length
      : 0;

  const recommendations: Record<string, number> = {};
  for (const r of results) {
    recommendations[r.recommendation] = (recommendations[r.recommendation] ?? 0) + 1;
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center gap-4">
        <Link
          href="/admin"
          className="rounded-lg p-1.5 text-muted-foreground transition-colors hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
        >
          <ArrowLeft className="size-5" />
        </Link>
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">
            {department.name}
          </h1>
          <p className="text-sm text-muted-foreground">
            {department.jobRoles.length} role{department.jobRoles.length !== 1 ? "s" : ""}{" "}
            &middot; {sessions.length} total candidates
          </p>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {[
          { label: "Total Candidates", value: sessions.length, icon: Users, color: "text-blue-600", bg: "bg-blue-50 dark:bg-blue-950" },
          { label: "Completed", value: completed.length, icon: CheckCircle, color: "text-green-600", bg: "bg-green-50 dark:bg-green-950" },
          { label: "In Progress", value: inProgress.length, icon: Clock, color: "text-amber-600", bg: "bg-amber-50 dark:bg-amber-950" },
          { label: "Avg Score", value: `${Math.round(avgScore * 100)}%`, icon: TrendingUp, color: "text-purple-600", bg: "bg-purple-50 dark:bg-purple-950" },
        ].map((stat) => (
          <Card key={stat.label}>
            <CardContent className="flex items-center gap-4 pt-2">
              <div className={`rounded-lg p-2.5 ${stat.bg}`}>
                <stat.icon className={`size-5 ${stat.color}`} />
              </div>
              <div>
                <p className="text-2xl font-bold">{stat.value}</p>
                <p className="text-xs text-muted-foreground">{stat.label}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Interview scheduling default */}
      <DepartmentInterviewerCard
        departmentId={department.id}
        initialEmail={department.defaultInterviewer ?? null}
      />

      {/* Roles */}
      <JobRolesManager
        departmentId={department.id}
        departmentName={department.name}
        initialRoles={department.jobRoles.map((r) => ({
          id: r.id,
          title: r.title,
          slug: r.slug,
          description: r.description,
          isActive: r.isActive,
          templateCount: r.assessmentTemplates.length,
          jdSummary: r.jdSummary ?? null,
          jdResponsibilities: r.jdResponsibilities ?? null,
          jdRequirements: r.jdRequirements ?? null,
          jdNiceToHaves: r.jdNiceToHaves ?? null,
          jdYearsExperience: r.jdYearsExperience ?? null,
          interviewerEmail: r.interviewerEmail ?? null,
        }))}
      />

      {/* Result Distribution */}
      {Object.keys(recommendations).length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Result Distribution</CardTitle>
            <CardDescription>
              Recommendation breakdown for {department.name}
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-4">
              {Object.entries(recommendations).map(([rec, count]) => (
                <div
                  key={rec}
                  className="flex-1 rounded-lg border border-zinc-100 p-4 text-center dark:border-zinc-800"
                >
                  <span
                    className={`inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold ${
                      recommendationColors[rec] ?? "bg-zinc-100 text-zinc-800"
                    }`}
                  >
                    {rec.replace(/_/g, " ")}
                  </span>
                  <p className="mt-2 text-2xl font-bold">{count}</p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Sessions Table */}
      <Card>
        <CardHeader>
          <CardTitle>Candidates</CardTitle>
          <CardDescription>
            All candidates for {department.name}
          </CardDescription>
        </CardHeader>
        <CardContent className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Candidate</TableHead>
                <TableHead>Role</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Score</TableHead>
                <TableHead>Recommendation</TableHead>
                <TableHead>Date</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {sessions.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={6} className="py-8 text-center text-muted-foreground">
                    No candidates yet for this department.
                  </TableCell>
                </TableRow>
              ) : (
                sessions.map((session) => (
                  <TableRow key={session.id}>
                    <TableCell>
                      <Link
                        href={`/admin/sessions/${session.id}`}
                        className="font-medium hover:underline"
                      >
                        {session.candidateName}
                      </Link>
                      <p className="text-xs text-muted-foreground">
                        {session.candidateEmail}
                      </p>
                    </TableCell>
                    <TableCell className="text-xs">
                      {session.version.template.jobRole.title}
                    </TableCell>
                    <TableCell>
                      <Badge variant={statusVariant[session.status] ?? "outline"}>
                        {session.status.replace(/_/g, " ")}
                      </Badge>
                    </TableCell>
                    <TableCell>
                      {session.result ? (
                        <span className="font-semibold">
                          {Math.round(session.result.normalizedScore * 100)}%
                        </span>
                      ) : (
                        <span className="text-muted-foreground">-</span>
                      )}
                    </TableCell>
                    <TableCell>
                      {session.result ? (
                        <span
                          className={`inline-flex items-center rounded-full px-2 py-0.5 text-[10px] font-medium ${
                            recommendationColors[session.result.recommendation] ?? ""
                          }`}
                        >
                          {session.result.recommendation.replace(/_/g, " ")}
                        </span>
                      ) : (
                        <span className="text-muted-foreground">-</span>
                      )}
                    </TableCell>
                    <TableCell className="text-xs text-muted-foreground">
                      {formatDistanceToNow(session.createdAt, { addSuffix: true })}
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}

```