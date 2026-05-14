---
type: source
source_type: laptop
title: page
slug: page-6
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/assessments/page.tsx
original_size: 15742
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/assessments/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  FileText,
  Layers,
  HelpCircle,
  Plus,
  Edit,
  Trash2,
  Loader2,
  AlertTriangle,
  Users,
  Copy,
  X,
} from "lucide-react";
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

interface Template {
  id: string;
  title: string;
  slug: string;
  description: string | null;
  isActive: boolean;
  jobRole: { title: string; department: { name: string; slug: string } };
  versions: Array<{
    id: string;
    versionNumber: number;
    status: string;
    passingScore: number;
    timeLimit: number | null;
    publishedAt: string | null;
    sections: Array<{ id: string; _count: { questions: number } }>;
    _count: { candidateSessions: number };
  }>;
}

const statusColors: Record<string, string> = {
  published: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
  draft: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  archived: "bg-zinc-100 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400",
};

export default function AssessmentsPage() {
  const router = useRouter();
  const [templates, setTemplates] = useState<Template[]>([]);
  const [jobRoles, setJobRoles] = useState<Array<{ id: string; title: string; department: { name: string } }>>([]);
  const [loading, setLoading] = useState(true);
  const [deleteTarget, setDeleteTarget] = useState<Template | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState<string | null>(null);
  const [duplicateTarget, setDuplicateTarget] = useState<Template | null>(null);
  const [duplicateTitle, setDuplicateTitle] = useState("");
  const [duplicateJobRoleId, setDuplicateJobRoleId] = useState("");
  const [isDuplicating, setIsDuplicating] = useState(false);
  const [duplicateError, setDuplicateError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/admin/assessments")
      .then((r) => r.json())
      .then((d) => {
        setTemplates(d.templates ?? []);
        setLoading(false);
      });
    fetch("/api/admin/job-roles")
      .then((r) => r.json())
      .then((d) => setJobRoles(d.jobRoles ?? []));
  }, []);

  const openDuplicate = (template: Template) => {
    setDuplicateTarget(template);
    setDuplicateTitle(`${template.title} (Copy)`);
    setDuplicateJobRoleId("");
    setDuplicateError(null);
  };

  const handleDuplicate = async () => {
    if (!duplicateTarget) return;
    setIsDuplicating(true);
    setDuplicateError(null);
    try {
      const res = await fetch(`/api/admin/assessments/${duplicateTarget.id}/duplicate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: duplicateTitle.trim() || undefined,
          jobRoleId: duplicateJobRoleId || undefined,
        }),
      });
      const data = await res.json();
      if (!res.ok) { setDuplicateError(data.error); setIsDuplicating(false); return; }
      setDuplicateTarget(null);
      router.push(`/admin/assessments/${data.template.id}/edit`);
    } catch { setDuplicateError("Network error"); }
    setIsDuplicating(false);
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    setDeleteError(null);
    try {
      const res = await fetch(`/api/admin/assessments/${deleteTarget.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) {
        setDeleteError(data.error);
        setIsDeleting(false);
        return;
      }
      setTemplates((prev) => prev.filter((t) => t.id !== deleteTarget.id));
      setDeleteTarget(null);
    } catch { setDeleteError("Network error"); }
    setIsDeleting(false);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Assessments</h1>
          <p className="text-sm text-muted-foreground">
            Manage assessment templates and versions.
          </p>
        </div>
        <Button onClick={() => router.push("/admin/assessments/new")} className="gap-2">
          <Plus className="size-4" /> New Assessment
        </Button>
      </div>

      {loading ? (
        <Card>
          <CardContent className="flex items-center justify-center py-12">
            <Loader2 className="size-6 animate-spin text-muted-foreground" />
          </CardContent>
        </Card>
      ) : templates.length === 0 ? (
        <Card>
          <CardContent className="flex flex-col items-center justify-center py-12">
            <FileText className="size-12 text-muted-foreground" />
            <p className="mt-4 text-sm text-muted-foreground">No assessments yet.</p>
            <Button onClick={() => router.push("/admin/assessments/new")} className="mt-4 gap-2">
              <Plus className="size-4" /> Create your first assessment
            </Button>
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-4">
          {templates.map((template) => {
            const latestVersion = template.versions[0];
            const totalQuestions = latestVersion?.sections.reduce(
              (acc, s) => acc + s._count.questions, 0
            ) ?? 0;
            const totalCandidates = template.versions.reduce(
              (acc, v) => acc + v._count.candidateSessions, 0
            );

            return (
              <Card key={template.id}>
                <CardHeader>
                  <div className="flex items-start justify-between">
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2">
                        <CardTitle>{template.title}</CardTitle>
                        {latestVersion && (
                          <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-[10px] font-medium ${statusColors[latestVersion.status] ?? ""}`}>
                            {latestVersion.status}
                          </span>
                        )}
                      </div>
                      <CardDescription>
                        {template.jobRole.department.name} &middot; {template.jobRole.title}
                      </CardDescription>
                      {template.description && (
                        <p className="mt-2 text-sm text-muted-foreground">{template.description}</p>
                      )}
                    </div>
                    <div className="flex gap-2">
                      <Button
                        variant="outline"
                        onClick={() => router.push(`/admin/assessments/${template.id}/edit`)}
                        className="gap-1.5 text-xs"
                      >
                        <Edit className="size-3" /> Edit
                      </Button>
                      <Button
                        variant="outline"
                        onClick={() => openDuplicate(template)}
                        className="gap-1.5 text-xs"
                      >
                        <Copy className="size-3" /> Duplicate
                      </Button>
                      <button
                        onClick={() => setDeleteTarget(template)}
                        className="rounded-lg p-2 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                      >
                        <Trash2 className="size-4" />
                      </button>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-3 gap-4">
                    <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
                      <Layers className="mb-1 size-4 text-muted-foreground" />
                      <p className="text-lg font-bold">{latestVersion?.sections.length ?? 0}</p>
                      <p className="text-[10px] text-muted-foreground">Sections</p>
                    </div>
                    <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
                      <HelpCircle className="mb-1 size-4 text-muted-foreground" />
                      <p className="text-lg font-bold">{totalQuestions}</p>
                      <p className="text-[10px] text-muted-foreground">Questions</p>
                    </div>
                    <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
                      <Users className="mb-1 size-4 text-muted-foreground" />
                      <p className="text-lg font-bold">{totalCandidates}</p>
                      <p className="text-[10px] text-muted-foreground">Candidates</p>
                    </div>
                  </div>

                  <div className="mt-3 flex items-center gap-4 text-xs text-muted-foreground">
                    <span>Passing score: {Math.round((latestVersion?.passingScore ?? 0) * 100)}%</span>
                    {latestVersion?.timeLimit && <span>Time limit: {latestVersion.timeLimit} min</span>}
                    {latestVersion?.publishedAt && (
                      <span>Published: {new Date(latestVersion.publishedAt).toLocaleDateString()}</span>
                    )}
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}

      {/* Delete confirmation */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Assessment</h3>
                <p className="text-xs text-muted-foreground">This action cannot be undone.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Delete <strong className="text-foreground">{deleteTarget.title}</strong>?
              All sections, questions, and scoring data will be permanently removed.
            </p>
            {deleteError && (
              <p className="mb-3 rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                {deleteError}
              </p>
            )}
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => { setDeleteTarget(null); setDeleteError(null); }} disabled={isDeleting}>
                Cancel
              </Button>
              <Button variant="destructive" onClick={handleDelete} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Duplicate modal */}
      {duplicateTarget && (() => {
        const grouped = new Map<string, typeof jobRoles>();
        for (const jr of jobRoles) {
          const dept = jr.department.name;
          if (!grouped.has(dept)) grouped.set(dept, []);
          grouped.get(dept)!.push(jr);
        }
        return (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            <div className="fixed inset-0 bg-black/50" onClick={() => setDuplicateTarget(null)} />
            <div className="relative z-10 w-full max-w-md rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
              <div className="mb-5 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="rounded-lg bg-blue-50 p-2 dark:bg-blue-950">
                    <Copy className="size-5 text-blue-600 dark:text-blue-400" />
                  </div>
                  <div>
                    <h3 className="text-sm font-semibold">Duplicate Assessment</h3>
                    <p className="text-xs text-muted-foreground">Creates a draft copy you can customize</p>
                  </div>
                </div>
                <button onClick={() => setDuplicateTarget(null)} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
                  <X className="size-4" />
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <Label>New Title</Label>
                  <Input
                    value={duplicateTitle}
                    onChange={(e) => setDuplicateTitle(e.target.value)}
                    placeholder="e.g. Operations Coordinator Assessment"
                    className="mt-1.5"
                  />
                </div>

                <div>
                  <Label>Assign to Job Role</Label>
                  <p className="mb-1.5 text-[10px] text-muted-foreground">
                    Leave unchanged to keep the same role, or pick a new one.
                  </p>
                  <Select value={duplicateJobRoleId} onValueChange={(v) => setDuplicateJobRoleId(v ?? "")}>
                    <SelectTrigger className="w-full">
                      <SelectValue placeholder="Same as original" />
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

                <div className="rounded-lg bg-zinc-50 p-3 text-xs text-muted-foreground dark:bg-zinc-800/50">
                  This will copy all sections, questions, options, scoring rules, and competency
                  assignments. The new assessment starts as a <strong>draft</strong> so you can edit
                  freely before publishing.
                </div>

                {duplicateError && (
                  <p className="text-xs text-red-600 dark:text-red-400">{duplicateError}</p>
                )}

                <div className="flex justify-end gap-3">
                  <Button variant="outline" onClick={() => setDuplicateTarget(null)} disabled={isDuplicating}>
                    Cancel
                  </Button>
                  <Button onClick={handleDuplicate} disabled={!duplicateTitle.trim() || isDuplicating} className="gap-2">
                    {isDuplicating ? <Loader2 className="size-4 animate-spin" /> : <Copy className="size-4" />}
                    Duplicate
                  </Button>
                </div>
              </div>
            </div>
          </div>
        );
      })()}
    </div>
  );
}

```