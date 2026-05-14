---
type: source
source_type: laptop
title: page
slug: page-4
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/page.tsx
original_size: 12779
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/page.tsx` on 2026-05-14._

```tsx
import { requireAuth } from "@/lib/auth";
import { prisma } from "@/lib/db";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Users,
  CheckCircle,
  Clock,
  TrendingUp,
  Building2,
  ChevronRight,
  Monitor,
  Cog,
  Heart,
  DollarSign,
} from "lucide-react";
import Link from "next/link";

const departmentConfig: Record<string, { color: string; icon: React.ElementType }> = {
  "information-technology": { color: "bg-blue-50 dark:bg-blue-950 text-blue-600", icon: Monitor },
  operations: { color: "bg-amber-50 dark:bg-amber-950 text-amber-600", icon: Cog },
  "human-resources": { color: "bg-pink-50 dark:bg-pink-950 text-pink-600", icon: Heart },
  finance: { color: "bg-emerald-50 dark:bg-emerald-950 text-emerald-600", icon: DollarSign },
  default: { color: "bg-zinc-50 dark:bg-zinc-800 text-zinc-600", icon: Building2 },
};

const recommendationColors: Record<string, string> = {
  strong_hire: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
  hire: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  consider: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  weak_fit: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  reject: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
};

export default async function AdminDashboard() {
  await requireAuth();

  // Fetch departments with their full pipeline data
  const departments = await prisma.department.findMany({
    include: {
      jobRoles: {
        include: {
          assessmentTemplates: {
            include: {
              versions: {
                where: { status: "published" },
                include: {
                  candidateSessions: {
                    include: { result: true },
                  },
                },
              },
            },
          },
        },
      },
    },
    orderBy: { name: "asc" },
  });

  // Compute per-department stats
  const deptStats = departments.map((dept) => {
    const allSessions = dept.jobRoles.flatMap((jr) =>
      jr.assessmentTemplates.flatMap((at) =>
        at.versions.flatMap((v) => v.candidateSessions)
      )
    );
    const completed = allSessions.filter((s) => s.status === "completed");
    const inProgress = allSessions.filter((s) => s.status === "in_progress");
    const results = completed.filter((s) => s.result).map((s) => s.result!);
    const avgScore =
      results.length > 0
        ? results.reduce((sum, r) => sum + r.normalizedScore, 0) / results.length
        : 0;

    const recommendations: Record<string, number> = {};
    for (const r of results) {
      recommendations[r.recommendation] = (recommendations[r.recommendation] ?? 0) + 1;
    }

    return {
      id: dept.id,
      name: dept.name,
      slug: dept.slug,
      roles: dept.jobRoles.map((jr) => ({
        id: jr.id,
        title: jr.title,
        slug: jr.slug,
        templateCount: jr.assessmentTemplates.length,
      })),
      totalCandidates: allSessions.length,
      completed: completed.length,
      inProgress: inProgress.length,
      avgScore,
      recommendations,
      hireRate:
        results.length > 0
          ? ((recommendations.strong_hire ?? 0) + (recommendations.hire ?? 0)) / results.length
          : 0,
    };
  });

  // Global stats
  const globalTotal = deptStats.reduce((s, d) => s + d.totalCandidates, 0);
  const globalCompleted = deptStats.reduce((s, d) => s + d.completed, 0);
  const globalInProgress = deptStats.reduce((s, d) => s + d.inProgress, 0);
  const globalAvg =
    deptStats.filter((d) => d.completed > 0).length > 0
      ? deptStats.reduce((s, d) => s + d.avgScore * d.completed, 0) /
        Math.max(globalCompleted, 1)
      : 0;

  // Recent sessions across all departments
  const recentSessions = await prisma.candidateSession.findMany({
    take: 8,
    orderBy: { createdAt: "desc" },
    include: {
      version: {
        include: {
          template: {
            include: { jobRole: { include: { department: true } } },
          },
        },
      },
      result: true,
    },
  });

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Dashboard</h1>
        <p className="text-sm text-muted-foreground">
          Hiring pipeline overview across all departments.
        </p>
      </div>

      {/* Global Stats */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {[
          { label: "Total Candidates", value: globalTotal, icon: Users, color: "text-blue-600", bg: "bg-blue-50 dark:bg-blue-950" },
          { label: "Completed", value: globalCompleted, icon: CheckCircle, color: "text-green-600", bg: "bg-green-50 dark:bg-green-950" },
          { label: "In Progress", value: globalInProgress, icon: Clock, color: "text-amber-600", bg: "bg-amber-50 dark:bg-amber-950" },
          { label: "Avg Score", value: `${Math.round(globalAvg * 100)}%`, icon: TrendingUp, color: "text-purple-600", bg: "bg-purple-50 dark:bg-purple-950" },
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

      {/* Department Cards */}
      <div>
        <h2 className="mb-4 text-lg font-semibold tracking-tight">
          Departments
        </h2>
        <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
          {deptStats.map((dept) => {
            const config = departmentConfig[dept.slug] ?? departmentConfig.default;
            const DeptIcon = config.icon;
            return (
              <Link
                key={dept.id}
                href={`/admin/departments/${dept.slug}`}
                className="group"
              >
                <Card className="transition-shadow hover:shadow-md">
                  <CardHeader>
                    <div className="flex items-start justify-between">
                      <div className="flex items-center gap-3">
                        <div className={`rounded-lg p-2.5 ${config.color}`}>
                          <DeptIcon className="size-5" />
                        </div>
                        <div>
                          <CardTitle className="text-base">
                            {dept.name}
                          </CardTitle>
                          <CardDescription>
                            {dept.roles.length} role{dept.roles.length !== 1 ? "s" : ""}{" "}
                            &middot;{" "}
                            {dept.roles.map((r) => r.title).join(", ")}
                          </CardDescription>
                        </div>
                      </div>
                      <ChevronRight className="size-4 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-4 gap-3">
                      <div>
                        <p className="text-lg font-bold">{dept.totalCandidates}</p>
                        <p className="text-[10px] text-muted-foreground">
                          Candidates
                        </p>
                      </div>
                      <div>
                        <p className="text-lg font-bold">{dept.completed}</p>
                        <p className="text-[10px] text-muted-foreground">
                          Completed
                        </p>
                      </div>
                      <div>
                        <p className="text-lg font-bold">
                          {Math.round(dept.avgScore * 100)}%
                        </p>
                        <p className="text-[10px] text-muted-foreground">
                          Avg Score
                        </p>
                      </div>
                      <div>
                        <p className="text-lg font-bold">
                          {Math.round(dept.hireRate * 100)}%
                        </p>
                        <p className="text-[10px] text-muted-foreground">
                          Hire Rate
                        </p>
                      </div>
                    </div>

                    {/* Mini recommendation bar */}
                    {dept.completed > 0 && (
                      <div className="mt-3 flex gap-1">
                        {Object.entries(dept.recommendations).map(
                          ([rec, count]) => (
                            <div
                              key={rec}
                              className={`h-1.5 rounded-full ${
                                recommendationColors[rec]?.split(" ")[0] ?? "bg-zinc-200"
                              }`}
                              style={{
                                width: `${(count / dept.completed) * 100}%`,
                              }}
                              title={`${rec.replace(/_/g, " ")}: ${count}`}
                            />
                          )
                        )}
                      </div>
                    )}

                    {dept.inProgress > 0 && (
                      <p className="mt-2 text-[10px] text-muted-foreground">
                        {dept.inProgress} currently in progress
                      </p>
                    )}
                  </CardContent>
                </Card>
              </Link>
            );
          })}

          {deptStats.length === 0 && (
            <Card className="lg:col-span-2">
              <CardContent className="flex flex-col items-center justify-center py-12">
                <Building2 className="size-12 text-muted-foreground" />
                <p className="mt-4 text-sm text-muted-foreground">
                  No departments configured yet.
                </p>
              </CardContent>
            </Card>
          )}
        </div>
      </div>

      {/* Recent Activity */}
      <Card>
        <CardHeader>
          <CardTitle>Recent Candidates</CardTitle>
          <CardDescription>Latest sessions across all departments</CardDescription>
        </CardHeader>
        <CardContent>
          {recentSessions.length === 0 ? (
            <p className="text-sm text-muted-foreground">No candidates yet.</p>
          ) : (
            <div className="space-y-3">
              {recentSessions.map((session) => (
                <Link
                  key={session.id}
                  href={`/admin/sessions/${session.id}`}
                  className="flex items-center justify-between rounded-lg border border-zinc-100 p-3 transition-colors hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-800/50"
                >
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium">
                      {session.candidateName}
                    </p>
                    <p className="truncate text-xs text-muted-foreground">
                      {session.version.template.jobRole.department.name}{" "}
                      &middot; {session.version.template.jobRole.title}
                    </p>
                  </div>
                  <div className="ml-4 flex items-center gap-2">
                    {session.result ? (
                      <>
                        <span className="text-sm font-semibold">
                          {Math.round(session.result.normalizedScore * 100)}%
                        </span>
                        <span
                          className={`inline-flex items-center rounded-full px-2 py-0.5 text-[10px] font-medium ${
                            recommendationColors[session.result.recommendation] ?? ""
                          }`}
                        >
                          {session.result.recommendation.replace(/_/g, " ")}
                        </span>
                      </>
                    ) : (
                      <Badge variant="secondary">
                        {session.status.replace(/_/g, " ")}
                      </Badge>
                    )}
                  </div>
                </Link>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

```