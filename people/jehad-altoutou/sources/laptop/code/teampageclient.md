---
type: source
source_type: laptop
title: TeamPageClient
slug: teampageclient
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/team/TeamPageClient.tsx
original_size: 18521
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# TeamPageClient

_Extracted from `assessify/src/app/admin/team/TeamPageClient.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  AlertTriangle,
  Archive,
  Edit,
  Loader2,
  Plus,
  Save,
  Users,
  X,
} from "lucide-react";

export type EmployeeRow = {
  id: string;
  firstName: string;
  fullName: string | null;
  email: string | null;
  slackUserId: string | null;
  slackHandle: string | null;
  department: string | null;
  isActive: boolean;
  lineManagerId: string | null;
  lineManagerName: string | null;
};

export type ManagerRow = {
  id: string;
  name: string;
  email: string | null;
  slackUserId: string | null;
  slackHandle: string | null;
  isActive: boolean;
  directReports: number;
};

const UNASSIGNED = "__unassigned__";

export function TeamPageClient({
  initialEmployees,
  initialManagers,
}: {
  initialEmployees: EmployeeRow[];
  initialManagers: ManagerRow[];
}) {
  const router = useRouter();
  const [, startTransition] = useTransition();

  const [employees] = useState(initialEmployees);
  const [managers] = useState(initialManagers);

  const [editingEmployee, setEditingEmployee] = useState<EmployeeRow | null>(null);
  const [editingManager, setEditingManager] = useState<ManagerRow | null>(null);
  const [creatingEmployee, setCreatingEmployee] = useState(false);
  const [creatingManager, setCreatingManager] = useState(false);

  function refresh() {
    startTransition(() => router.refresh());
  }

  return (
    <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
      {/* Employees */}
      <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-3 flex items-center justify-between">
          <h2 className="flex items-center gap-2 text-sm font-semibold">
            <Users className="size-4" />
            Employees <span className="text-xs text-muted-foreground">({employees.length})</span>
          </h2>
          <Button size="sm" onClick={() => setCreatingEmployee(true)} className="gap-1.5">
            <Plus className="size-3.5" /> Add employee
          </Button>
        </div>
        <ul className="divide-y divide-zinc-100 dark:divide-zinc-800">
          {employees.map((e) => (
            <li key={e.id} className="flex items-center justify-between gap-3 py-2 text-sm">
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-2">
                  <span className="font-medium truncate">{e.fullName || e.firstName}</span>
                  {!e.isActive && (
                    <span className="rounded bg-zinc-100 px-1.5 py-0.5 text-[10px] uppercase text-zinc-500 dark:bg-zinc-800">
                      Archived
                    </span>
                  )}
                </div>
                <div className="truncate text-xs text-muted-foreground">
                  {[e.email, e.department, e.lineManagerName ? `→ ${e.lineManagerName}` : null]
                    .filter(Boolean)
                    .join(" · ") || "—"}
                </div>
              </div>
              <button
                type="button"
                onClick={() => setEditingEmployee(e)}
                className="rounded-md p-1.5 text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800"
                aria-label="Edit"
              >
                <Edit className="size-3.5" />
              </button>
            </li>
          ))}
          {employees.length === 0 && (
            <li className="py-6 text-center text-sm text-muted-foreground">
              No employees yet. Click <strong>Add employee</strong> to get started.
            </li>
          )}
        </ul>
      </section>

      {/* Managers */}
      <section className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-3 flex items-center justify-between">
          <h2 className="flex items-center gap-2 text-sm font-semibold">
            <Users className="size-4" />
            Line managers <span className="text-xs text-muted-foreground">({managers.length})</span>
          </h2>
          <Button size="sm" onClick={() => setCreatingManager(true)} className="gap-1.5">
            <Plus className="size-3.5" /> Add manager
          </Button>
        </div>
        <ul className="divide-y divide-zinc-100 dark:divide-zinc-800">
          {managers.map((m) => (
            <li key={m.id} className="flex items-center justify-between gap-3 py-2 text-sm">
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-2">
                  <span className="font-medium truncate">{m.name}</span>
                  {!m.isActive && (
                    <span className="rounded bg-zinc-100 px-1.5 py-0.5 text-[10px] uppercase text-zinc-500 dark:bg-zinc-800">
                      Archived
                    </span>
                  )}
                  {m.directReports > 0 && (
                    <span className="rounded bg-blue-50 px-1.5 py-0.5 text-[10px] font-semibold text-blue-700 dark:bg-blue-950 dark:text-blue-300">
                      {m.directReports} report{m.directReports === 1 ? "" : "s"}
                    </span>
                  )}
                </div>
                <div className="truncate text-xs text-muted-foreground">{m.email || "—"}</div>
              </div>
              <button
                type="button"
                onClick={() => setEditingManager(m)}
                className="rounded-md p-1.5 text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800"
                aria-label="Edit"
              >
                <Edit className="size-3.5" />
              </button>
            </li>
          ))}
          {managers.length === 0 && (
            <li className="py-6 text-center text-sm text-muted-foreground">
              No managers yet. Click <strong>Add manager</strong> to get started.
            </li>
          )}
        </ul>
      </section>

      {(creatingEmployee || editingEmployee) && (
        <EmployeeDialog
          initial={editingEmployee}
          managers={managers.filter((m) => m.isActive)}
          onClose={() => {
            setCreatingEmployee(false);
            setEditingEmployee(null);
          }}
          onSaved={() => {
            setCreatingEmployee(false);
            setEditingEmployee(null);
            refresh();
          }}
        />
      )}
      {(creatingManager || editingManager) && (
        <ManagerDialog
          initial={editingManager}
          onClose={() => {
            setCreatingManager(false);
            setEditingManager(null);
          }}
          onSaved={() => {
            setCreatingManager(false);
            setEditingManager(null);
            refresh();
          }}
        />
      )}
    </div>
  );
}

// ─── Dialogs ────────────────────────────────────────────────────────────────

function EmployeeDialog({
  initial,
  managers,
  onClose,
  onSaved,
}: {
  initial: EmployeeRow | null;
  managers: ManagerRow[];
  onClose: () => void;
  onSaved: () => void;
}) {
  const mode = initial ? "edit" : "create";
  const [firstName, setFirstName] = useState(initial?.firstName ?? "");
  const [fullName, setFullName] = useState(initial?.fullName ?? "");
  const [email, setEmail] = useState(initial?.email ?? "");
  const [slackHandle, setSlackHandle] = useState(initial?.slackHandle ?? "");
  const [slackUserId, setSlackUserId] = useState(initial?.slackUserId ?? "");
  const [department, setDepartment] = useState(initial?.department ?? "");
  const [lineManagerId, setLineManagerId] = useState(initial?.lineManagerId ?? UNASSIGNED);
  const [isActive, setIsActive] = useState(initial?.isActive ?? true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function save() {
    setError(null);
    if (!firstName.trim()) return setError("First name is required.");
    setSubmitting(true);
    try {
      const url = mode === "create" ? "/api/admin/team/employees" : `/api/admin/team/employees/${initial!.id}`;
      const res = await fetch(url, {
        method: mode === "create" ? "POST" : "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          firstName,
          fullName: fullName || null,
          email: email || null,
          slackUserId: slackUserId || null,
          slackHandle: slackHandle || null,
          department: department || null,
          isActive,
          lineManagerId: lineManagerId === UNASSIGNED ? null : lineManagerId,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to save");
        setSubmitting(false);
        return;
      }
      onSaved();
    } catch {
      setError("Network error");
      setSubmitting(false);
    }
  }

  async function archive() {
    if (!initial) return;
    if (!confirm(`Archive ${initial.fullName || initial.firstName}? Leave history is preserved.`)) return;
    setSubmitting(true);
    try {
      const res = await fetch(`/api/admin/team/employees/${initial.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to archive");
        setSubmitting(false);
        return;
      }
      onSaved();
    } catch {
      setError("Network error");
      setSubmitting(false);
    }
  }

  return (
    <DialogShell
      title={mode === "create" ? "Add employee" : "Edit employee"}
      onClose={onClose}
      onSave={save}
      onArchive={mode === "edit" && initial?.isActive ? archive : undefined}
      submitting={submitting}
      error={error}
    >
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
        <Field label="First name" required>
          <Input value={firstName} onChange={(e) => setFirstName(e.target.value)} placeholder="Jane" />
        </Field>
        <Field label="Full name">
          <Input value={fullName} onChange={(e) => setFullName(e.target.value)} placeholder="Jane Doe" />
        </Field>
        <Field label="Email">
          <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="jane@janusd.com" />
        </Field>
        <Field label="Department">
          <Input value={department} onChange={(e) => setDepartment(e.target.value)} placeholder="Finance" />
        </Field>
        <Field label="Slack handle">
          <Input value={slackHandle} onChange={(e) => setSlackHandle(e.target.value)} placeholder="janedoe" />
        </Field>
        <Field label="Slack user ID">
          <Input value={slackUserId} onChange={(e) => setSlackUserId(e.target.value)} placeholder="U0APLC6GW14" />
        </Field>
        <div className="sm:col-span-2">
          <Label className="text-xs">Line manager</Label>
          <Select value={lineManagerId} onValueChange={(v) => setLineManagerId(v ?? UNASSIGNED)}>
            <SelectTrigger className="mt-1.5 w-full">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value={UNASSIGNED}>— Unassigned —</SelectItem>
              {managers.map((m) => (
                <SelectItem key={m.id} value={m.id}>{m.name}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
        <div className="sm:col-span-2">
          <label className="flex cursor-pointer items-center gap-2 text-xs">
            <input
              type="checkbox"
              checked={isActive}
              onChange={(e) => setIsActive(e.target.checked)}
              className="size-4 rounded border-zinc-300"
            />
            <span>Active — appears in dropdowns and receives Slack DMs.</span>
          </label>
        </div>
      </div>
    </DialogShell>
  );
}

function ManagerDialog({
  initial,
  onClose,
  onSaved,
}: {
  initial: ManagerRow | null;
  onClose: () => void;
  onSaved: () => void;
}) {
  const mode = initial ? "edit" : "create";
  const [name, setName] = useState(initial?.name ?? "");
  const [email, setEmail] = useState(initial?.email ?? "");
  const [slackHandle, setSlackHandle] = useState(initial?.slackHandle ?? "");
  const [slackUserId, setSlackUserId] = useState(initial?.slackUserId ?? "");
  const [isActive, setIsActive] = useState(initial?.isActive ?? true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function save() {
    setError(null);
    if (!name.trim()) return setError("Name is required.");
    setSubmitting(true);
    try {
      const url = mode === "create" ? "/api/admin/team/managers" : `/api/admin/team/managers/${initial!.id}`;
      const res = await fetch(url, {
        method: mode === "create" ? "POST" : "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          email: email || null,
          slackUserId: slackUserId || null,
          slackHandle: slackHandle || null,
          isActive,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to save");
        setSubmitting(false);
        return;
      }
      onSaved();
    } catch {
      setError("Network error");
      setSubmitting(false);
    }
  }

  async function archive() {
    if (!initial) return;
    const msg =
      initial.directReports > 0
        ? `Archive ${initial.name}? ${initial.directReports} employee${initial.directReports === 1 ? "" : "s"} will be un-linked from this manager.`
        : `Archive ${initial.name}?`;
    if (!confirm(msg)) return;
    setSubmitting(true);
    try {
      const res = await fetch(`/api/admin/team/managers/${initial.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to archive");
        setSubmitting(false);
        return;
      }
      onSaved();
    } catch {
      setError("Network error");
      setSubmitting(false);
    }
  }

  return (
    <DialogShell
      title={mode === "create" ? "Add line manager" : "Edit line manager"}
      onClose={onClose}
      onSave={save}
      onArchive={mode === "edit" && initial?.isActive ? archive : undefined}
      submitting={submitting}
      error={error}
    >
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
        <Field label="Name" required>
          <Input value={name} onChange={(e) => setName(e.target.value)} placeholder="John Smith" />
        </Field>
        <Field label="Email">
          <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="john@janusd.com" />
        </Field>
        <Field label="Slack handle">
          <Input value={slackHandle} onChange={(e) => setSlackHandle(e.target.value)} placeholder="johns" />
        </Field>
        <Field label="Slack user ID">
          <Input value={slackUserId} onChange={(e) => setSlackUserId(e.target.value)} placeholder="U0APLC6GW14" />
        </Field>
        <div className="sm:col-span-2">
          <label className="flex cursor-pointer items-center gap-2 text-xs">
            <input
              type="checkbox"
              checked={isActive}
              onChange={(e) => setIsActive(e.target.checked)}
              className="size-4 rounded border-zinc-300"
            />
            <span>Active — appears in dropdowns and receives leave-approval DMs.</span>
          </label>
        </div>
      </div>
    </DialogShell>
  );
}

function DialogShell({
  title,
  onClose,
  onSave,
  onArchive,
  submitting,
  error,
  children,
}: {
  title: string;
  onClose: () => void;
  onSave: () => void;
  onArchive?: () => void;
  submitting: boolean;
  error: string | null;
  children: React.ReactNode;
}) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/50" onClick={onClose} />
      <div className="relative z-10 w-full max-w-lg rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-base font-semibold">{title}</h3>
          <button
            onClick={onClose}
            className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
          >
            <X className="size-4" />
          </button>
        </div>
        {children}
        {error && (
          <div className="mt-3 flex items-start gap-2 rounded-lg bg-rose-50 p-2.5 text-xs text-rose-700 dark:bg-rose-950 dark:text-rose-300">
            <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
            <span>{error}</span>
          </div>
        )}
        <div className="mt-5 flex items-center justify-between">
          {onArchive ? (
            <Button
              type="button"
              variant="outline"
              onClick={onArchive}
              disabled={submitting}
              className="gap-2 text-rose-700 hover:bg-rose-50 dark:text-rose-300 dark:hover:bg-rose-950"
            >
              <Archive className="size-4" /> Archive
            </Button>
          ) : (
            <span />
          )}
          <div className="flex gap-2">
            <Button variant="outline" onClick={onClose} disabled={submitting}>
              Cancel
            </Button>
            <Button onClick={onSave} disabled={submitting} className="gap-2">
              {submitting ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
              Save
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

function Field({
  label,
  required,
  children,
}: {
  label: string;
  required?: boolean;
  children: React.ReactNode;
}) {
  return (
    <div>
      <Label className="text-xs">
        {label}
        {required && <span className="text-rose-600"> *</span>}
      </Label>
      <div className="mt-1.5">{children}</div>
    </div>
  );
}

```