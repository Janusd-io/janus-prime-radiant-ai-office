---
type: source
source_type: laptop
title: page
slug: page-7
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/assessments/new/page.tsx
original_size: 6499
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/admin/assessments/new/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { ArrowLeft, Loader2, Sparkles } from "lucide-react";

interface JobRole {
  id: string;
  title: string;
  slug: string;
  department: { name: string; slug: string };
}

export default function NewAssessmentPage() {
  const router = useRouter();
  const [jobRoles, setJobRoles] = useState<JobRole[]>([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [jobRoleId, setJobRoleId] = useState("");
  const [passingScore, setPassingScore] = useState("60");
  const [timeLimit, setTimeLimit] = useState("");
  const [isCreating, setIsCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/admin/job-roles")
      .then((r) => r.json())
      .then((d) => setJobRoles(d.jobRoles ?? []));
  }, []);

  const handleCreate = async () => {
    if (!title.trim() || !jobRoleId) return;
    setIsCreating(true);
    setError(null);

    try {
      const res = await fetch("/api/admin/assessments", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: title.trim(),
          description: description.trim() || null,
          jobRoleId,
          passingScore: parseInt(passingScore) / 100,
          timeLimit: timeLimit ? parseInt(timeLimit) : null,
        }),
      });
      const data = await res.json();
      if (!res.ok) { setError(data.error); setIsCreating(false); return; }
      router.push(`/admin/assessments/${data.template.id}/edit`);
    } catch {
      setError("Network error");
      setIsCreating(false);
    }
  };

  // Group job roles by department
  const grouped = new Map<string, JobRole[]>();
  for (const jr of jobRoles) {
    const dept = jr.department.name;
    if (!grouped.has(dept)) grouped.set(dept, []);
    grouped.get(dept)!.push(jr);
  }

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <div className="flex items-center gap-4">
        <Link
          href="/admin/assessments"
          className="rounded-lg p-1.5 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
        >
          <ArrowLeft className="size-5" />
        </Link>
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">New Assessment</h1>
          <p className="text-sm text-muted-foreground">
            Create a new assessment template. You can add sections and questions next.
          </p>
        </div>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Basic Information</CardTitle>
          <CardDescription>
            Start with the essentials. You can adjust everything later.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div>
              <Label>Assessment Title</Label>
              <Input
                placeholder="e.g. Operations Coordinator Assessment"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="mt-1.5"
              />
            </div>

            <div>
              <Label htmlFor="assessment-description">Description</Label>
              <textarea
                id="assessment-description"
                placeholder="Short summary of what this assessment covers"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="mt-1.5 min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none transition-colors focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
              />
            </div>

            <div>
              <Label>Job Role</Label>
              <div className="mt-1.5">
                <Select value={jobRoleId} onValueChange={(v) => setJobRoleId(v ?? "")}>
                  <SelectTrigger className="w-full">
                    <SelectValue placeholder="Select a job role" />
                  </SelectTrigger>
                  <SelectContent>
                    {Array.from(grouped.entries()).map(([dept, roles]) => (
                      <SelectGroup key={dept}>
                        <SelectLabel>{dept}</SelectLabel>
                        {roles.map((r) => (
                          <SelectItem key={r.id} value={r.id}>{r.title}</SelectItem>
                        ))}
                      </SelectGroup>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <Label>Passing Score (%)</Label>
                <Input
                  type="number"
                  min="0"
                  max="100"
                  value={passingScore}
                  onChange={(e) => setPassingScore(e.target.value)}
                  className="mt-1.5"
                />
              </div>
              <div>
                <Label>Time Limit (minutes)</Label>
                <Input
                  type="number"
                  placeholder="Leave empty for no limit"
                  value={timeLimit}
                  onChange={(e) => setTimeLimit(e.target.value)}
                  className="mt-1.5"
                />
              </div>
            </div>

            {error && <p className="text-sm text-red-600">{error}</p>}

            <div className="flex gap-3 pt-2">
              <Button onClick={handleCreate} disabled={!title.trim() || !jobRoleId || isCreating} className="gap-2">
                {isCreating ? <Loader2 className="size-4 animate-spin" /> : <Sparkles className="size-4" />}
                Create Assessment
              </Button>
              <Button variant="outline" onClick={() => router.push("/admin/assessments")}>Cancel</Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

```