---
type: source
source_type: laptop
title: page
slug: page-24
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/sessions/page.tsx
original_size: 5051
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/sessions/page.tsx` on 2026-05-14._

```tsx
import { requireAuth } from "@/lib/auth";
import { prisma } from "@/lib/db";
import {
  Card,
  CardContent,
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import Link from "next/link";
import { formatDistanceToNow } from "date-fns";

export default async function SessionsPage() {
  await requireAuth();

  const sessions = await prisma.candidateSession.findMany({
    orderBy: { createdAt: "desc" },
    include: {
      version: { include: { template: { include: { jobRole: true } } } },
      result: true,
      responses: { select: { id: true } },
    },
  });

  const statusVariant: Record<string, "default" | "secondary" | "outline" | "destructive"> = {
    completed: "default",
    in_progress: "secondary",
    not_started: "outline",
    expired: "destructive",
    disqualified: "destructive",
  };

  const recommendationColors: Record<string, string> = {
    strong_hire: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
    hire: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
    consider: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
    weak_fit: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
    reject: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Candidates</h1>
        <p className="text-sm text-muted-foreground">
          All candidate assessment sessions.
        </p>
      </div>

      <Card>
        <CardContent className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Candidate</TableHead>
                <TableHead>Assessment</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Score</TableHead>
                <TableHead>Recommendation</TableHead>
                <TableHead>Questions</TableHead>
                <TableHead>Date</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {sessions.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={7} className="py-8 text-center text-muted-foreground">
                    No sessions yet.
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
                      {session.version.template.title}
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
                      {session.responses.length} answered
                    </TableCell>
                    <TableCell className="text-xs text-muted-foreground">
                      {formatDistanceToNow(session.createdAt, {
                        addSuffix: true,
                      })}
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