---
type: source
source_type: laptop
title: Assessify — page
slug: page-9
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/easter-eggs/page.tsx
original_size: 20404
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/easter-eggs/page.tsx` on 2026-05-14._

```tsx
import { requireAuth } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { EGGS } from "@/lib/easter-eggs";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Egg, Trophy, Star, Skull, Users, Target, Crown } from "lucide-react";
import { formatDistanceToNow } from "date-fns";

const difficultyConfig: Record<
  string,
  { color: string; bg: string; icon: React.ElementType }
> = {
  easy: { color: "text-emerald-700 dark:text-emerald-300", bg: "bg-emerald-100 dark:bg-emerald-900", icon: Egg },
  medium: { color: "text-blue-700 dark:text-blue-300", bg: "bg-blue-100 dark:bg-blue-900", icon: Star },
  hard: { color: "text-orange-700 dark:text-orange-300", bg: "bg-orange-100 dark:bg-orange-900", icon: Trophy },
  impossible: { color: "text-red-700 dark:text-red-300", bg: "bg-red-100 dark:bg-red-900", icon: Skull },
};

const difficultyBadge: Record<string, string> = {
  easy: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
  medium: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  hard: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  impossible: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
};

function bestAchievement(eggIds: string[]): { label: string; color: string } {
  if (eggIds.includes("egg_4")) return { label: "Impossible", color: "text-red-600 dark:text-red-400" };
  if (eggIds.includes("egg_3")) return { label: "Hard", color: "text-orange-600 dark:text-orange-400" };
  if (eggIds.includes("egg_2")) return { label: "Medium", color: "text-blue-600 dark:text-blue-400" };
  if (eggIds.includes("egg_1")) return { label: "Easy", color: "text-emerald-600 dark:text-emerald-400" };
  return { label: "Started", color: "text-zinc-500" };
}

export default async function EasterEggsPage() {
  await requireAuth();

  const [claims, huntStartEvents, huntFinishEvents] = await Promise.all([
    prisma.easterEggClaim.findMany({ orderBy: { claimedAt: "desc" } }),
    prisma.analyticsEvent.findMany({
      where: { eventType: "egg_hunt_started" },
      orderBy: { timestamp: "desc" },
    }),
    prisma.analyticsEvent.findMany({
      where: { eventType: "egg_hunt_finished" },
      orderBy: { timestamp: "desc" },
    }),
  ]);

  // Build finish data lookup by email
  const finishByEmail = new Map<string, { timestamp: Date; reason: string; eggsSolved: number }>();
  for (const evt of huntFinishEvents) {
    const data = evt.eventData ? JSON.parse(evt.eventData) : {};
    const email = data.candidateEmail;
    if (email && !finishByEmail.has(email)) {
      finishByEmail.set(email, {
        timestamp: evt.timestamp,
        reason: data.reason ?? "unknown",
        eggsSolved: data.eggsSolved ?? 0,
      });
    }
  }

  // Build hunter profiles: everyone who started + their claims
  const hunterMap = new Map<
    string,
    {
      name: string;
      email: string;
      startedAt: Date;
      finishedAt: Date | null;
      finishReason: string | null;
      sessionId: string | null;
      eggsClaimed: { eggId: string; claimedAt: Date }[];
    }
  >();

  // Add hunters from analytics events
  for (const evt of huntStartEvents) {
    const data = evt.eventData ? JSON.parse(evt.eventData) : {};
    const email = data.candidateEmail;
    if (!email) continue;
    if (!hunterMap.has(email)) {
      const finish = finishByEmail.get(email);
      hunterMap.set(email, {
        name: data.candidateName ?? "Unknown",
        email,
        startedAt: evt.timestamp,
        finishedAt: finish?.timestamp ?? null,
        finishReason: finish?.reason ?? null,
        sessionId: evt.sessionId,
        eggsClaimed: [],
      });
    }
  }

  // Add hunters from claims (in case they claimed without triggering the event)
  for (const claim of claims) {
    if (!hunterMap.has(claim.candidateEmail)) {
      const finish = finishByEmail.get(claim.candidateEmail);
      hunterMap.set(claim.candidateEmail, {
        name: claim.candidateName,
        email: claim.candidateEmail,
        startedAt: claim.claimedAt,
        finishedAt: finish?.timestamp ?? null,
        finishReason: finish?.reason ?? null,
        sessionId: claim.sessionId,
        eggsClaimed: [],
      });
    }
    hunterMap.get(claim.candidateEmail)!.eggsClaimed.push({
      eggId: claim.eggId,
      claimedAt: claim.claimedAt,
    });
  }

  const hunters = [...hunterMap.values()].sort((a, b) => {
    // Sort by eggs found (desc), then by earliest start
    if (b.eggsClaimed.length !== a.eggsClaimed.length)
      return b.eggsClaimed.length - a.eggsClaimed.length;
    return a.startedAt.getTime() - b.startedAt.getTime();
  });

  const totalHunters = hunters.length;
  const completionists = hunters.filter((h) => h.eggsClaimed.length === 4);
  const impossibleFinders = hunters.filter((h) =>
    h.eggsClaimed.some((e) => e.eggId === "egg_4")
  );

  // Egg stats
  const eggStats = Object.values(EGGS).map((egg) => {
    const eggClaims = claims.filter((c) => c.eggId === egg.id);
    return {
      ...egg,
      claimCount: eggClaims.length,
      firstClaim: eggClaims.length > 0 ? eggClaims[eggClaims.length - 1] : null,
      solveRate: totalHunters > 0 ? eggClaims.length / totalHunters : 0,
    };
  });

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Easter Eggs</h1>
        <p className="text-sm text-muted-foreground">
          Track who started the hunt and their progress.
        </p>
      </div>

      {/* Overview stats */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-blue-50 p-2.5 dark:bg-blue-950">
              <Users className="size-5 text-blue-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{totalHunters}</p>
              <p className="text-xs text-muted-foreground">Total Hunters</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-emerald-50 p-2.5 dark:bg-emerald-950">
              <Target className="size-5 text-emerald-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{claims.length}</p>
              <p className="text-xs text-muted-foreground">Total Eggs Found</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-purple-50 p-2.5 dark:bg-purple-950">
              <Crown className="size-5 text-purple-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{completionists.length}</p>
              <p className="text-xs text-muted-foreground">Completionists</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-red-50 p-2.5 dark:bg-red-950">
              <Skull className="size-5 text-red-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{impossibleFinders.length}</p>
              <p className="text-xs text-muted-foreground">Found the Impossible</p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Egg breakdown */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {eggStats.map((egg) => {
          const config = difficultyConfig[egg.difficulty] ?? difficultyConfig.easy;
          const EggIcon = config.icon;
          return (
            <Card key={egg.id}>
              <CardContent className="pt-3">
                <div className="flex items-center gap-3">
                  <div className={`rounded-lg p-2 ${config.bg}`}>
                    <EggIcon className={`size-4 ${config.color}`} />
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-semibold">{egg.name}</p>
                    <p className="text-[10px] text-muted-foreground">
                      {egg.difficulty}
                    </p>
                  </div>
                  <span className="text-xl font-bold">{egg.claimCount}</span>
                </div>
                <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                  <div
                    className={`h-full rounded-full ${config.bg}`}
                    style={{
                      width: `${Math.round(egg.solveRate * 100)}%`,
                    }}
                  />
                </div>
                <div className="mt-1 flex items-center justify-between text-[10px] text-muted-foreground">
                  <span>{Math.round(egg.solveRate * 100)}% solve rate</span>
                  {egg.firstClaim && (
                    <span>First: {egg.firstClaim.candidateName}</span>
                  )}
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>

      {/* Hunter Leaderboard */}
      <Card>
        <CardHeader>
          <CardTitle>Hunter Leaderboard</CardTitle>
          <CardDescription>
            Every candidate who started the egg hunt, ranked by progress
          </CardDescription>
        </CardHeader>
        <CardContent className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="w-8">#</TableHead>
                <TableHead>Candidate</TableHead>
                <TableHead>Progress</TableHead>
                <TableHead>Best Achievement</TableHead>
                <TableHead>Eggs Found</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Started</TableHead>
                <TableHead>Finished</TableHead>
                <TableHead>Duration</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {hunters.length === 0 ? (
                <TableRow>
                  <TableCell
                    colSpan={9}
                    className="py-8 text-center text-muted-foreground"
                  >
                    No one has started the egg hunt yet.
                  </TableCell>
                </TableRow>
              ) : (
                hunters.map((hunter, i) => {
                  const achievement = bestAchievement(
                    hunter.eggsClaimed.map((e) => e.eggId)
                  );
                  const solvedIds = new Set(
                    hunter.eggsClaimed.map((e) => e.eggId)
                  );
                  return (
                    <TableRow key={hunter.email}>
                      <TableCell className="text-xs font-bold text-muted-foreground">
                        {i + 1}
                      </TableCell>
                      <TableCell>
                        <div className="flex items-center gap-2">
                          {hunter.eggsClaimed.length === 4 && (
                            <Crown className="size-3.5 text-purple-500" />
                          )}
                          <div>
                            <p className="text-sm font-medium">
                              {hunter.name}
                            </p>
                            <p className="text-xs text-muted-foreground">
                              {hunter.email}
                            </p>
                          </div>
                        </div>
                      </TableCell>
                      <TableCell>
                        <div className="flex items-center gap-2">
                          <div className="flex gap-1">
                            {["egg_1", "egg_2", "egg_3", "egg_4"].map(
                              (eggId) => {
                                const eggDef =
                                  EGGS[eggId as keyof typeof EGGS];
                                const config =
                                  difficultyConfig[eggDef.difficulty];
                                return (
                                  <span
                                    key={eggId}
                                    title={`${eggDef.difficulty}: ${eggDef.name}`}
                                    className={`flex h-6 w-6 items-center justify-center rounded-md text-[10px] font-bold ${
                                      solvedIds.has(eggId)
                                        ? `${config.bg} ${config.color}`
                                        : "bg-zinc-100 text-zinc-400 dark:bg-zinc-800"
                                    }`}
                                  >
                                    {solvedIds.has(eggId) ? "✓" : "·"}
                                  </span>
                                );
                              }
                            )}
                          </div>
                          <span className="text-xs font-semibold">
                            {hunter.eggsClaimed.length}/4
                          </span>
                        </div>
                      </TableCell>
                      <TableCell>
                        <span
                          className={`text-xs font-semibold ${achievement.color}`}
                        >
                          {achievement.label}
                        </span>
                      </TableCell>
                      <TableCell>
                        <div className="flex flex-wrap gap-1">
                          {hunter.eggsClaimed
                            .sort(
                              (a, b) =>
                                new Date(a.claimedAt).getTime() -
                                new Date(b.claimedAt).getTime()
                            )
                            .map((claim) => {
                              const eggDef =
                                EGGS[claim.eggId as keyof typeof EGGS];
                              return (
                                <span
                                  key={claim.eggId}
                                  className={`inline-flex items-center rounded-full px-1.5 py-0.5 text-[9px] font-medium ${
                                    difficultyBadge[eggDef?.difficulty ?? "easy"]
                                  }`}
                                  title={`Found ${formatDistanceToNow(claim.claimedAt, { addSuffix: true })}`}
                                >
                                  {eggDef?.name ?? claim.eggId}
                                </span>
                              );
                            })}
                          {hunter.eggsClaimed.length === 0 && (
                            <span className="text-xs text-muted-foreground">
                              No eggs yet
                            </span>
                          )}
                        </div>
                      </TableCell>
                      <TableCell>
                        {hunter.finishedAt ? (
                          hunter.finishReason === "completed_all" ? (
                            <span className="inline-flex items-center rounded-full bg-emerald-100 px-2 py-0.5 text-[10px] font-medium text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">
                              Completed
                            </span>
                          ) : (
                            <span className="inline-flex items-center rounded-full bg-zinc-100 px-2 py-0.5 text-[10px] font-medium text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400">
                              Gave up
                            </span>
                          )
                        ) : (
                          <span className="inline-flex items-center rounded-full bg-blue-100 px-2 py-0.5 text-[10px] font-medium text-blue-700 dark:bg-blue-900 dark:text-blue-300">
                            In progress
                          </span>
                        )}
                      </TableCell>
                      <TableCell className="text-xs text-muted-foreground whitespace-nowrap">
                        {hunter.startedAt.toLocaleDateString()}{" "}
                        {hunter.startedAt.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                      </TableCell>
                      <TableCell className="text-xs text-muted-foreground whitespace-nowrap">
                        {hunter.finishedAt
                          ? `${hunter.finishedAt.toLocaleDateString()} ${hunter.finishedAt.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}`
                          : "—"}
                      </TableCell>
                      <TableCell className="text-xs font-medium whitespace-nowrap">
                        {hunter.finishedAt
                          ? (() => {
                              const ms = hunter.finishedAt.getTime() - hunter.startedAt.getTime();
                              const mins = Math.floor(ms / 60000);
                              const hrs = Math.floor(mins / 60);
                              if (hrs > 0) return `${hrs}h ${mins % 60}m`;
                              return `${mins}m`;
                            })()
                          : "—"}
                      </TableCell>
                    </TableRow>
                  );
                })
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Recent Activity Feed */}
      <Card>
        <CardHeader>
          <CardTitle>Recent Activity</CardTitle>
          <CardDescription>Latest egg discoveries</CardDescription>
        </CardHeader>
        <CardContent>
          {claims.length === 0 ? (
            <p className="text-sm text-muted-foreground">
              No eggs found yet. The hunt is on!
            </p>
          ) : (
            <div className="space-y-3">
              {claims.slice(0, 20).map((claim) => {
                const eggDef = EGGS[claim.eggId as keyof typeof EGGS];
                const config = eggDef
                  ? difficultyConfig[eggDef.difficulty]
                  : difficultyConfig.easy;
                const EggIcon = config?.icon ?? Egg;
                return (
                  <div
                    key={claim.id}
                    className="flex items-center gap-3 rounded-lg border border-zinc-100 p-3 dark:border-zinc-800"
                  >
                    <div className={`rounded-md p-1.5 ${config?.bg}`}>
                      <EggIcon className={`size-3.5 ${config?.color}`} />
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm">
                        <span className="font-medium">
                          {claim.candidateName}
                        </span>{" "}
                        found{" "}
                        <span className={`font-semibold ${config?.color}`}>
                          {eggDef?.name ?? claim.eggId}
                        </span>
                      </p>
                      <p className="text-[10px] text-muted-foreground">
                        {claim.candidateEmail}
                      </p>
                    </div>
                    <span
                      className={`inline-flex items-center rounded-full px-2 py-0.5 text-[10px] font-medium ${
                        difficultyBadge[eggDef?.difficulty ?? "easy"]
                      }`}
                    >
                      {eggDef?.difficulty ?? "unknown"}
                    </span>
                    <span className="text-[10px] text-muted-foreground whitespace-nowrap">
                      {formatDistanceToNow(claim.claimedAt, {
                        addSuffix: true,
                      })}
                    </span>
                  </div>
                );
              })}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

```