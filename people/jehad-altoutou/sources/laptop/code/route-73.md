---
type: source
source_type: laptop
title: route
slug: route-73
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/leave/[id]/pdf/route.ts"
original_size: 9103
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/leave/[id]/pdf/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { formatDate, formatTimestamp } from "@/lib/slack";
import { STATUS_LABEL } from "@/lib/leave";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const { id } = await ctx.params;

  const r = await prisma.leaveRequest.findUnique({
    where: { id },
    include: { employee: true, lineManager: true },
  });
  if (!r) return new Response("Not found", { status: 404 });

  const empName = r.employee?.fullName || r.employee?.firstName || "Unknown";
  const managerName = r.lineManager?.name ?? "(removed)";
  const approvalDate = r.hrDecisionAt ? formatTimestamp(r.hrDecisionAt) : "—";
  const submittedDate = formatTimestamp(r.employeeSignedAt);
  const managerDecidedAt = r.managerDecisionAt ? formatTimestamp(r.managerDecisionAt) : "—";

  // CEO self-submissions skip the approval chain entirely.
  // Detect via employee identity OR the auto-approval marker comment.
  const isCeoRequest =
    r.employee?.fullName === "Bonaventure Wong" ||
    (r.managerComments?.includes("CEO self-approval") ?? false);

  const statusBadge = (() => {
    const bg: Record<string, string> = {
      approved: "#ecfdf5",
      pending_manager: "#fffbeb",
      pending_hr: "#eff6ff",
      rejected_manager: "#fef2f2",
      rejected_hr: "#fef2f2",
      blocked_balance: "#f4f4f5",
    };
    const fg: Record<string, string> = {
      approved: "#047857",
      pending_manager: "#b45309",
      pending_hr: "#1d4ed8",
      rejected_manager: "#b91c1c",
      rejected_hr: "#b91c1c",
      blocked_balance: "#3f3f46",
    };
    return `<span style="display:inline-block;padding:4px 12px;border-radius:999px;font-size:12px;font-weight:600;background:${bg[r.status] ?? "#f4f4f5"};color:${fg[r.status] ?? "#3f3f46"};">${STATUS_LABEL[r.status] ?? r.status}</span>`;
  })();

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Leave Request — ${empName}</title>
<style>
  @page { margin: 24mm 18mm; }
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #18181b;
    margin: 0;
    padding: 24px;
    background: #fff;
  }
  .wrap { max-width: 780px; margin: 0 auto; }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 16px;
    margin-bottom: 24px;
    gap: 20px;
  }
  .header-left { display: flex; align-items: center; gap: 16px; }
  .header-logo { width: 58px; height: 58px; object-fit: contain; }
  .header h1 {
    color: #1e3a8a;
    font-size: 22px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0;
  }
  .header .sub { color: #64748b; font-size: 12px; margin-top: 4px; }
  .brand {
    text-align: right;
    font-size: 11px;
    color: #64748b;
    line-height: 1.5;
  }
  .brand strong { color: #1e3a8a; font-size: 13px; font-weight: 700; letter-spacing: 0.3px; display: block; }
  h2 {
    color: #1e40af;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #e4e4e7;
    padding-bottom: 6px;
    margin: 28px 0 12px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #e4e4e7;
    font-size: 13px;
  }
  td {
    padding: 10px 14px;
    border-bottom: 1px solid #f4f4f5;
    vertical-align: top;
  }
  td.label {
    width: 35%;
    background: #fafafa;
    font-weight: 600;
    color: #475569;
    border-right: 1px solid #e4e4e7;
  }
  .signatures {
    display: flex;
    gap: 16px;
    margin-top: 12px;
  }
  .sig-box {
    flex: 1;
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    padding: 14px;
    background: #fafafa;
  }
  .sig-box .heading {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #71717a;
    margin-bottom: 10px;
  }
  .sig-box .name {
    font-family: "Snell Roundhand", "Apple Chancery", "Segoe Script", cursive;
    font-size: 22px;
    color: #1e3a8a;
    padding: 8px 0;
    border-bottom: 1px solid #cbd5e1;
    min-height: 40px;
  }
  .sig-box .meta { font-size: 11px; color: #64748b; margin-top: 6px; }
  .footer {
    margin-top: 32px;
    padding-top: 12px;
    border-top: 1px dashed #cbd5e1;
    font-size: 11px;
    color: #94a3b8;
    text-align: center;
  }
  .print-btn {
    position: fixed;
    top: 16px;
    right: 16px;
    background: #18181b;
    color: #fff;
    border: 0;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 13px;
    cursor: pointer;
    font-weight: 600;
  }
  @media print { .print-btn { display: none; } }
</style>
</head>
<body>
  <button class="print-btn" onclick="window.print()">Download as PDF</button>
  <div class="wrap">
    <div class="header">
      <div class="header-left">
        <img class="header-logo" src="/janusd-icon-200.png" alt="Janus Digital" />
        <div>
          <h1>Leave Request Form</h1>
          <div class="sub">Confidential — HR use · ${statusBadge}</div>
        </div>
      </div>
      <div class="brand">
        <strong>JANUS DIGITAL</strong>
        <span>Human Resources</span>
      </div>
    </div>

    <h2>1. Employee Details</h2>
    <table>
      <tr><td class="label">Employee Name</td><td>${empName}</td></tr>
      <tr><td class="label">Department / Team</td><td>${r.department || "—"}</td></tr>
      <tr><td class="label">Date Submitted</td><td>${submittedDate}</td></tr>
    </table>

    <h2>2. Leave Details</h2>
    <table>
      <tr><td class="label">Type of Leave</td><td>${r.leaveType}</td></tr>
      <tr><td class="label">Start Date</td><td>${formatDate(r.startDate)}</td></tr>
      <tr><td class="label">End Date</td><td>${formatDate(r.endDate)}</td></tr>
      <tr><td class="label">Total Days Requested</td><td>${r.totalDays} working day${r.totalDays === 1 ? "" : "s"}</td></tr>
      <tr><td class="label">Reason / Notes</td><td>${escapeHtml(r.reason || "—")}</td></tr>
    </table>

    <h2>3. Approval</h2>
    ${isCeoRequest ? `<table>
      <tr><td class="label">Approval Type</td><td>Auto-approved per CEO policy — no line manager or HR review required</td></tr>
      <tr><td class="label">HR Acknowledgement</td><td>${r.hrAcknowledgedAt ? `Acknowledged by ${escapeHtml(r.hrAcknowledgedBy || "HR")} at ${formatTimestamp(r.hrAcknowledgedAt)}` : `<span style="color:#b45309">Pending — HR has not yet acknowledged</span>`}</td></tr>
    </table>` : `<table>
      <tr><td class="label">Line Manager</td><td>${managerName}</td></tr>
      <tr><td class="label">Line Manager Decision</td><td>${r.managerDecision ? r.managerDecision.charAt(0).toUpperCase() + r.managerDecision.slice(1) : "Pending"}</td></tr>
      <tr><td class="label">Line Manager Comments</td><td>${escapeHtml(r.managerComments || "—")}</td></tr>
      <tr><td class="label">Line Manager Decision Date</td><td>${managerDecidedAt}</td></tr>
      <tr><td class="label">HR Decision</td><td>${r.hrDecision ? r.hrDecision.charAt(0).toUpperCase() + r.hrDecision.slice(1) : "Pending"}</td></tr>
      <tr><td class="label">HR Comments</td><td>${escapeHtml(r.hrComments || "—")}</td></tr>
      <tr><td class="label">HR Decision Date</td><td>${approvalDate}</td></tr>
    </table>`}

    <h2>4. Signatures</h2>
    ${isCeoRequest ? `<div class="signatures">
      <div class="sig-box" style="flex: 1;">
        <div class="heading">CEO Signature</div>
        <div class="name">${escapeHtml(r.employeeSignature)}</div>
        <div class="meta">Signed ${submittedDate}</div>
      </div>
    </div>` : `<div class="signatures">
      <div class="sig-box">
        <div class="heading">Employee Signature</div>
        <div class="name">${escapeHtml(r.employeeSignature)}</div>
        <div class="meta">Signed ${submittedDate}</div>
      </div>
      <div class="sig-box">
        <div class="heading">Line Manager Signature</div>
        <div class="name">${r.managerSignature ? escapeHtml(r.managerSignature) : "<span style='color:#cbd5e1'>Pending</span>"}</div>
        <div class="meta">${r.managerDecisionAt ? `Signed ${managerDecidedAt}` : ""}</div>
      </div>
      <div class="sig-box">
        <div class="heading">HR Signature</div>
        <div class="name">${r.hrSignature ? escapeHtml(r.hrSignature) : "<span style='color:#cbd5e1'>Pending</span>"}</div>
        <div class="meta">${r.hrDecisionAt ? `Signed ${approvalDate}` : ""}</div>
      </div>
    </div>`}

    <div class="footer">
      Janus Digital — Leave Request · Generated ${formatTimestamp(new Date())}<br>
      Request ID: ${r.id}
    </div>
  </div>
</body>
</html>`;

  return new Response(html, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Content-Disposition": `inline; filename="leave-${empName.replace(/\s+/g, "-")}.html"`,
    },
  });
}

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

```