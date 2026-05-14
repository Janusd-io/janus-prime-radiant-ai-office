---
type: source
source_type: laptop
title: page
slug: page-29
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/invites/page.tsx
original_size: 15746
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/admin/invites/page.tsx` on 2026-05-14._

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
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
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
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Send,
  Loader2,
  Copy,
  Check,
  Plus,
  Trash2,
  AlertTriangle,
  Monitor,
  Cog,
  Heart,
  DollarSign,
  Building2,
} from "lucide-react";

const deptIcons: Record<string, React.ElementType> = {
  "Information Technology": Monitor,
  Operations: Cog,
  "Human Resources": Heart,
  Finance: DollarSign,
};

interface Template {
  id: string;
  title: string;
  slug: string;
  jobRole: { title: string; department: { name: string } };
}

interface Invite {
  id: string;
  code: string;
  candidateName: string;
  candidateEmail: string;
  status: string;
  sessionId: string | null;
  expiresAt: string | null;
  createdAt: string;
  template: {
    title: string;
    jobRole: { title: string; department: { name: string } };
  };
}

const statusConfig: Record<string, { label: string; variant: "default" | "secondary" | "outline" | "destructive" }> = {
  pending: { label: "Pending", variant: "outline" },
  started: { label: "Started", variant: "secondary" },
  completed: { label: "Completed", variant: "default" },
  expired: { label: "Expired", variant: "destructive" },
};

export default function InvitesPage() {
  const [invites, setInvites] = useState<Invite[]>([]);
  const [templates, setTemplates] = useState<Template[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [templateId, setTemplateId] = useState("");
  const [expiresInDays, setExpiresInDays] = useState("7");
  const [isCreating, setIsCreating] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [deleteTarget, setDeleteTarget] = useState<Invite | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/admin/invites")
      .then((r) => r.json())
      .then((d) => setInvites(d.invites ?? []));

    fetch("/api/assessments")
      .then((r) => r.json())
      .then((d) => {
        const all = (d.assessments ?? []).map((a: {
          id: string;
          title: string;
          slug: string;
          jobRole: { title: string; department: string };
        }) => ({
          id: a.id,
          title: a.title,
          slug: a.slug,
          jobRole: { title: a.jobRole.title, department: { name: a.jobRole.department } },
        }));
        setTemplates(all);
        if (all.length === 1) setTemplateId(all[0].id);
      });
  }, []);

  const handleCreate = async () => {
    if (!name.trim() || !email.trim() || !templateId) return;
    setIsCreating(true);
    setError(null);

    try {
      const res = await fetch("/api/admin/invites", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          candidateName: name.trim(),
          candidateEmail: email.trim(),
          templateId,
          expiresInDays: parseInt(expiresInDays) || 7,
        }),
      });

      const data = await res.json();
      if (!res.ok) {
        setError(data.error || "Failed to create invite.");
        setIsCreating(false);
        return;
      }

      // Reload invites
      const refreshed = await fetch("/api/admin/invites").then((r) => r.json());
      setInvites(refreshed.invites ?? []);

      setName("");
      setEmail("");
      setExpiresInDays("7");
      setShowForm(false);
    } catch {
      setError("Network error.");
    }
    setIsCreating(false);
  };

  const copyLink = (code: string, id: string) => {
    const link = `${window.location.origin}/assess/invite/${code}`;
    navigator.clipboard.writeText(link);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    try {
      await fetch(`/api/admin/invites?id=${deleteTarget.id}`, {
        method: "DELETE",
      });
      setInvites((prev) => prev.filter((i) => i.id !== deleteTarget.id));
    } catch {
      // ignore
    }
    setIsDeleting(false);
    setDeleteTarget(null);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Invites</h1>
          <p className="text-sm text-muted-foreground">
            Send assessment invitations to candidates.
          </p>
        </div>
        <Button onClick={() => setShowForm(!showForm)} className="gap-2">
          <Plus className="size-4" />
          New Invite
        </Button>
      </div>

      {/* Create form */}
      {showForm && (
        <Card>
          <CardHeader>
            <CardTitle>Create Invite</CardTitle>
            <CardDescription>
              Generate a unique assessment link for a candidate.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <Label htmlFor="name">Candidate Name</Label>
                <Input
                  id="name"
                  placeholder="Jane Smith"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="mt-1.5"
                />
              </div>
              <div>
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="jane@company.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="mt-1.5"
                />
              </div>
              <div>
                <Label>Assessment</Label>
                <div className="mt-1.5">
                  <Select value={templateId} onValueChange={(v) => setTemplateId(v ?? "")}>
                    <SelectTrigger className="w-full">
                      <SelectValue placeholder="Select an assessment" />
                    </SelectTrigger>
                    <SelectContent>
                      {(() => {
                        const grouped = new Map<string, typeof templates>();
                        for (const t of templates) {
                          const dept = t.jobRole.department.name;
                          if (!grouped.has(dept)) grouped.set(dept, []);
                          grouped.get(dept)!.push(t);
                        }
                        return Array.from(grouped.entries()).map(
                          ([dept, items]) => {
                            const DeptIcon = deptIcons[dept] ?? Building2;
                            return (
                              <SelectGroup key={dept}>
                                <SelectLabel>
                                  <span className="flex items-center gap-1.5">
                                    <DeptIcon className="size-3" />
                                    {dept}
                                  </span>
                                </SelectLabel>
                                {items.map((t) => (
                                  <SelectItem key={t.id} value={t.id}>
                                    {t.title}
                                  </SelectItem>
                                ))}
                              </SelectGroup>
                            );
                          }
                        );
                      })()}
                    </SelectContent>
                  </Select>
                </div>
              </div>
              <div>
                <Label htmlFor="expires">Expires In (days)</Label>
                <Input
                  id="expires"
                  type="number"
                  min="1"
                  value={expiresInDays}
                  onChange={(e) => setExpiresInDays(e.target.value)}
                  className="mt-1.5"
                />
              </div>
            </div>

            {error && (
              <p className="mt-3 text-sm text-red-600 dark:text-red-400">
                {error}
              </p>
            )}

            <div className="mt-4 flex gap-3">
              <Button
                onClick={handleCreate}
                disabled={
                  !name.trim() || !email.trim() || !templateId || isCreating
                }
                className="gap-2"
              >
                {isCreating ? (
                  <Loader2 className="size-4 animate-spin" />
                ) : (
                  <Send className="size-4" />
                )}
                Create Invite
              </Button>
              <Button variant="outline" onClick={() => setShowForm(false)}>
                Cancel
              </Button>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Invites table */}
      <Card>
        <CardContent className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Candidate</TableHead>
                <TableHead>Assessment</TableHead>
                <TableHead>Department</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Expires</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {invites.length === 0 ? (
                <TableRow>
                  <TableCell
                    colSpan={6}
                    className="py-8 text-center text-muted-foreground"
                  >
                    No invites yet. Click &quot;New Invite&quot; to create one.
                  </TableCell>
                </TableRow>
              ) : (
                invites.map((inv) => {
                  const sc = statusConfig[inv.status] ?? statusConfig.pending;
                  const isExpired =
                    inv.expiresAt && new Date(inv.expiresAt) < new Date();
                  return (
                    <TableRow key={inv.id}>
                      <TableCell>
                        <p className="text-sm font-medium">
                          {inv.candidateName}
                        </p>
                        <p className="text-xs text-muted-foreground">
                          {inv.candidateEmail}
                        </p>
                      </TableCell>
                      <TableCell className="text-xs">
                        {inv.template.title}
                      </TableCell>
                      <TableCell className="text-xs">
                        {inv.template.jobRole.department.name}
                      </TableCell>
                      <TableCell>
                        <Badge
                          variant={
                            isExpired ? "destructive" : sc.variant
                          }
                        >
                          {isExpired ? "Expired" : sc.label}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-xs text-muted-foreground">
                        {inv.expiresAt
                          ? new Date(inv.expiresAt).toLocaleDateString()
                          : "Never"}
                      </TableCell>
                      <TableCell>
                        <div className="flex items-center gap-1">
                          <button
                            onClick={() => copyLink(inv.code, inv.id)}
                            className="inline-flex items-center gap-1.5 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground transition-colors hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
                            title="Copy invite link"
                          >
                            {copiedId === inv.id ? (
                              <>
                                <Check className="size-3 text-green-500" />
                                Copied
                              </>
                            ) : (
                              <>
                                <Copy className="size-3" />
                                Copy
                              </>
                            )}
                          </button>
                          <button
                            onClick={() => setDeleteTarget(inv)}
                            className="inline-flex items-center gap-1.5 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground transition-colors hover:bg-red-50 hover:text-red-600 dark:hover:bg-red-950 dark:hover:text-red-400"
                            title="Delete invite"
                          >
                            <Trash2 className="size-3" />
                          </button>
                        </div>
                      </TableCell>
                    </TableRow>
                  );
                })
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Delete confirmation dialog */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div
            className="fixed inset-0 bg-black/50"
            onClick={() => setDeleteTarget(null)}
          />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600 dark:text-red-400" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Invite</h3>
                <p className="text-xs text-muted-foreground">
                  This action cannot be undone.
                </p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Are you sure you want to delete the invite for{" "}
              <strong className="text-foreground">
                {deleteTarget.candidateName}
              </strong>{" "}
              ({deleteTarget.candidateEmail})? The invite link will stop
              working immediately.
            </p>
            <div className="flex justify-end gap-3">
              <Button
                variant="outline"
                onClick={() => setDeleteTarget(null)}
                disabled={isDeleting}
              >
                Cancel
              </Button>
              <Button
                variant="destructive"
                onClick={handleDelete}
                disabled={isDeleting}
                className="gap-2"
              >
                {isDeleting ? (
                  <Loader2 className="size-4 animate-spin" />
                ) : (
                  <Trash2 className="size-4" />
                )}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

```