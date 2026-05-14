---
type: source
source_type: laptop
title: LeaveForm
slug: leaveform
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/leave/new/LeaveForm.tsx
original_size: 12148
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# LeaveForm

_Extracted from `assessify/src/app/leave/new/LeaveForm.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useMemo, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

type Employee = { id: string; firstName: string; fullName: string | null; isLineManager: boolean; isCeo: boolean };
type LineManager = { id: string; name: string };

type FormState = {
  employeeId: string;
  department: string;
  leaveType: string;
  startDate: string;
  endDate: string;
  reason: string;
  lineManagerId: string;
  employeeSignature: string;
};

function calculateBusinessDays(startStr: string, endStr: string): number {
  if (!startStr || !endStr) return 0;
  const start = new Date(startStr);
  const end = new Date(endStr);
  if (isNaN(start.getTime()) || isNaN(end.getTime()) || end < start) return 0;
  let count = 0;
  const cur = new Date(start);
  while (cur <= end) {
    const day = cur.getDay();
    if (day !== 0 && day !== 6) count++;
    cur.setDate(cur.getDate() + 1);
  }
  return count;
}

export default function LeaveForm({
  employees,
  lineManagers,
  leaveTypes,
  ceoLineManagerId,
  ceoLineManagerName,
}: {
  employees: Employee[];
  lineManagers: LineManager[];
  leaveTypes: string[];
  ceoLineManagerId: string | null;
  ceoLineManagerName: string | null;
}) {
  const [state, setState] = useState<FormState>({
    employeeId: "",
    department: "",
    leaveType: "",
    startDate: "",
    endDate: "",
    reason: "",
    lineManagerId: "",
    employeeSignature: "",
  });
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<
    | null
    | { ok: true; status: string; message: string }
    | { ok: false; error: string }
  >(null);

  const totalDays = useMemo(
    () => calculateBusinessDays(state.startDate, state.endDate),
    [state.startDate, state.endDate]
  );

  const selectedEmployee = employees.find((e) => e.id === state.employeeId);
  const isCeoSelf = Boolean(selectedEmployee?.isCeo);
  // Escalate to CEO for line managers, but NOT for the CEO himself (he auto-approves).
  const escalateToCeo = Boolean(
    selectedEmployee?.isLineManager && !isCeoSelf && ceoLineManagerId
  );

  // For line managers → auto-select CEO as approver. For the CEO himself →
  // auto-select his own LineManager record (server short-circuits to auto-approve).
  useEffect(() => {
    if ((escalateToCeo || isCeoSelf) && ceoLineManagerId && state.lineManagerId !== ceoLineManagerId) {
      setState((s) => ({ ...s, lineManagerId: ceoLineManagerId }));
    }
  }, [escalateToCeo, isCeoSelf, ceoLineManagerId, state.lineManagerId]);

  function set<K extends keyof FormState>(k: K, v: FormState[K]) {
    setState((s) => ({ ...s, [k]: v }));
  }

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setResult(null);

    if (!state.employeeId || !state.leaveType || !state.startDate || !state.endDate ||
        !state.lineManagerId || !state.employeeSignature.trim()) {
      setResult({ ok: false, error: "Please fill in all required fields." });
      return;
    }
    if (totalDays <= 0) {
      setResult({ ok: false, error: "End date must be on or after start date." });
      return;
    }
    // Signature must match selected employee's name
    const expected = (selectedEmployee?.fullName || selectedEmployee?.firstName || "").trim().toLowerCase();
    if (state.employeeSignature.trim().toLowerCase() !== expected) {
      setResult({
        ok: false,
        error: `Signature must match your selected name (${selectedEmployee?.fullName || selectedEmployee?.firstName}).`,
      });
      return;
    }

    setSubmitting(true);
    try {
      const res = await fetch("/api/leave", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...state, totalDays }),
      });
      const data = await res.json();
      if (!res.ok) {
        setResult({ ok: false, error: data.error ?? "Submission failed." });
      } else {
        setResult({ ok: true, status: data.status, message: data.message });
        // Reset (keep employee + signature so they can submit multiple if needed)
        setState((s) => ({
          ...s,
          department: "",
          leaveType: "",
          startDate: "",
          endDate: "",
          reason: "",
          lineManagerId: "",
        }));
      }
    } catch {
      setResult({ ok: false, error: "Network error. Please try again." });
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="space-y-6">
      {/* 1. Employee Details */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">1. Employee Details</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="employee">Employee Name *</Label>
            <Select value={state.employeeId} onValueChange={(v) => set("employeeId", v ?? "")}>
              <SelectTrigger id="employee">
                <SelectValue placeholder="-- Select employee --" />
              </SelectTrigger>
              <SelectContent>
                {employees.map((e) => (
                  <SelectItem key={e.id} value={e.id}>
                    {e.fullName || e.firstName}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          <div className="space-y-2">
            <Label htmlFor="department">Department / Team</Label>
            <Input
              id="department"
              value={state.department}
              onChange={(e) => set("department", e.target.value)}
              placeholder="e.g. Operations"
            />
          </div>
          <div className="space-y-2">
            <Label>Date Submitted</Label>
            <Input value={new Date().toLocaleDateString("en-GB")} disabled />
          </div>
        </CardContent>
      </Card>

      {/* 2. Leave Details */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">2. Leave Details</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="type">Type of Leave *</Label>
            <Select value={state.leaveType} onValueChange={(v) => set("leaveType", v ?? "")}>
              <SelectTrigger id="type">
                <SelectValue placeholder="-- Select leave type --" />
              </SelectTrigger>
              <SelectContent>
                {leaveTypes.map((t) => (
                  <SelectItem key={t} value={t}>{t}</SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="start">Start Date *</Label>
              <Input
                id="start"
                type="date"
                value={state.startDate}
                onChange={(e) => set("startDate", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="end">End Date *</Label>
              <Input
                id="end"
                type="date"
                value={state.endDate}
                onChange={(e) => set("endDate", e.target.value)}
              />
            </div>
          </div>
          <div className="space-y-2">
            <Label>Total Days Requested</Label>
            <Input value={totalDays > 0 ? `${totalDays} working day${totalDays === 1 ? "" : "s"}` : ""} disabled />
          </div>
          <div className="space-y-2">
            <Label htmlFor="reason">Reason / Notes (optional)</Label>
            <Textarea
              id="reason"
              rows={3}
              value={state.reason}
              onChange={(e) => set("reason", e.target.value)}
            />
          </div>
        </CardContent>
      </Card>

      {/* 3. Approval (preview) */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">3. Approval</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="manager">Line Manager *</Label>
            {isCeoSelf ? (
              <>
                <Input id="manager" value="Auto-approved (CEO)" disabled />
                <p className="text-xs text-emerald-700 dark:text-emerald-400">
                  As CEO, your leave is automatically approved on submission.
                  HR ({ceoLineManagerName ? "mariamm" : "@mariamm"}) will be notified for record-keeping.
                </p>
              </>
            ) : escalateToCeo ? (
              <>
                <Input id="manager" value={ceoLineManagerName ?? ""} disabled />
                <p className="text-xs text-amber-700 dark:text-amber-400">
                  Because you are a line manager, your request is routed to the CEO
                  ({ceoLineManagerName}) for approval.
                </p>
              </>
            ) : (
              <Select value={state.lineManagerId} onValueChange={(v) => set("lineManagerId", v ?? "")}>
                <SelectTrigger id="manager">
                  <SelectValue placeholder="-- Select line manager --" />
                </SelectTrigger>
                <SelectContent>
                  {lineManagers.map((m) => (
                    <SelectItem key={m.id} value={m.id}>{m.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            )}
          </div>
          <p className="text-xs text-muted-foreground">
            {isCeoSelf
              ? "Your request is auto-approved and logged. HR receives a notification."
              : "After submission, your line manager will be notified on Slack for approval. Once approved by both the line manager and HR, you will receive a confirmation."}
          </p>
        </CardContent>
      </Card>

      {/* 4. Signature */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">4. Signature</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="sig">Employee Signature (type your name) *</Label>
            <Input
              id="sig"
              value={state.employeeSignature}
              onChange={(e) => set("employeeSignature", e.target.value)}
              placeholder={selectedEmployee?.fullName || selectedEmployee?.firstName || "Type your name"}
            />
            <p className="text-xs text-muted-foreground">
              Your signature must match your selected employee name.
            </p>
          </div>
          <div className="space-y-2">
            <Label>Date</Label>
            <Input value={new Date().toLocaleDateString("en-GB")} disabled />
          </div>
        </CardContent>
      </Card>

      {result && (
        <div
          className={`rounded-lg border p-4 text-sm ${
            result.ok
              ? "border-emerald-300 bg-emerald-50 text-emerald-900 dark:border-emerald-700 dark:bg-emerald-950 dark:text-emerald-100"
              : "border-red-300 bg-red-50 text-red-900 dark:border-red-700 dark:bg-red-950 dark:text-red-100"
          }`}
        >
          {result.ok ? (
            <div>
              <p className="font-semibold">Submitted successfully</p>
              <p className="mt-1">{result.message}</p>
            </div>
          ) : (
            <p>{result.error}</p>
          )}
        </div>
      )}

      <div className="flex justify-end">
        <Button type="submit" disabled={submitting} size="lg">
          {submitting ? "Submitting…" : "Submit Leave Request"}
        </Button>
      </div>
    </form>
  );
}

```