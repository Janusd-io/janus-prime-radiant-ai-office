---
type: source
source_type: laptop
title: route
slug: route-71
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/leave/route.ts
original_size: 12977
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/leave/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import {
  LEAVE_TYPES,
  calculateBusinessDays,
  checkBalance,
  consumeBalance,
} from "@/lib/leave";
import {
  sendDM,
  getHrSlackId,
  managerApprovalMessage,
  formatDate,
  formatTimestamp,
  slackAlert,
} from "@/lib/slack";

type Body = {
  employeeId: string;
  lineManagerId: string;
  department?: string;
  leaveType: string;
  startDate: string;
  endDate: string;
  reason?: string;
  employeeSignature: string;
  totalDays?: number;
};

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as Body;

    // Validate
    if (!body.employeeId || !body.lineManagerId || !body.leaveType ||
        !body.startDate || !body.endDate || !body.employeeSignature?.trim()) {
      return NextResponse.json({ error: "Missing required fields" }, { status: 400 });
    }
    if (!LEAVE_TYPES.includes(body.leaveType as (typeof LEAVE_TYPES)[number])) {
      return NextResponse.json({ error: "Invalid leave type" }, { status: 400 });
    }

    const start = new Date(body.startDate);
    const end = new Date(body.endDate);
    if (isNaN(start.getTime()) || isNaN(end.getTime()) || end < start) {
      return NextResponse.json({ error: "Invalid date range" }, { status: 400 });
    }
    const totalDays = calculateBusinessDays(start, end);
    if (totalDays <= 0) {
      return NextResponse.json({ error: "At least 1 working day required" }, { status: 400 });
    }

    const [employee, manager] = await Promise.all([
      prisma.employee.findUnique({ where: { id: body.employeeId } }),
      prisma.lineManager.findUnique({ where: { id: body.lineManagerId } }),
    ]);
    if (!employee || !manager) {
      return NextResponse.json({ error: "Employee or line manager not found" }, { status: 404 });
    }

    // Signature must match employee name
    const expected = (employee.fullName || employee.firstName).trim().toLowerCase();
    if (body.employeeSignature.trim().toLowerCase() !== expected) {
      return NextResponse.json(
        { error: "Signature does not match employee name" },
        { status: 400 }
      );
    }

    // Hierarchy: if the employee is themselves a line manager, their request MUST
    // route to the CEO (Bonaventure Wong). Override any other pick silently.
    const employeeIsLineManager = employee.slackUserId
      ? Boolean(
          await prisma.lineManager.findFirst({
            where: { slackUserId: employee.slackUserId, isActive: true },
            select: { id: true },
          })
        )
      : false;
    let effectiveManager = manager;
    if (employeeIsLineManager) {
      const ceo = await prisma.lineManager.findFirst({
        where: { name: "Bonaventure Wong", isActive: true },
      });
      if (!ceo) {
        return NextResponse.json(
          { error: "CEO record missing — cannot route line-manager request" },
          { status: 500 }
        );
      }
      effectiveManager = ceo;
    }

    // Balance check
    const balance = await checkBalance(employee.id, body.leaveType, totalDays);

    if (!balance.sufficient) {
      // Create blocked request
      const req = await prisma.leaveRequest.create({
        data: {
          employeeId: employee.id,
          lineManagerId: effectiveManager.id,
          department: body.department || null,
          leaveType: body.leaveType,
          startDate: start,
          endDate: end,
          totalDays,
          reason: body.reason || null,
          status: "blocked_balance",
          employeeSignature: body.employeeSignature.trim(),
          balanceDrained: true,
        },
      });

      // Notify employee (if Slack ID known)
      if (employee.slackUserId) {
        await sendDM(
          employee.slackUserId,
          `Your leave request could not be submitted.`,
          [
            {
              type: "section",
              text: {
                type: "mrkdwn",
                text:
                  `Hi *${employee.fullName || employee.firstName}*, your *${body.leaveType}* request for *${totalDays} day${totalDays === 1 ? "" : "s"}* ` +
                  `(${formatDate(start)} → ${formatDate(end)}) could not be submitted because your leave balance for this type is exhausted.\n\n` +
                  `*Remaining balance:* ${balance.remaining} day${balance.remaining === 1 ? "" : "s"}\n\n` +
                  `Please contact HR (*@mariamm*) to discuss next steps — she will advise on unpaid leave options or adjustments.`,
              },
            },
          ]
        );
      }
      // Notify HR
      const hrId = await getHrSlackId();
      if (hrId) {
        await sendDM(
          hrId,
          `Leave request blocked — balance drained for ${employee.fullName || employee.firstName}.`,
          [
            {
              type: "header",
              text: { type: "plain_text", text: "Leave Balance — Attention Needed" },
            },
            {
              type: "section",
              text: {
                type: "mrkdwn",
                text:
                  `*${employee.fullName || employee.firstName}* has attempted to submit a *${body.leaveType}* request for *${totalDays} day${totalDays === 1 ? "" : "s"}* ` +
                  `(${formatDate(start)} → ${formatDate(end)}), but their balance for this leave type is exhausted.\n\n` +
                  `*Allocated:* ${balance.allocated === 9999 ? "Uncapped" : balance.allocated} · *Used:* ${balance.used} · *Remaining:* ${balance.remaining}\n\n` +
                  `Please advise the employee on the appropriate next steps (unpaid leave, policy exception, etc.).`,
              },
            },
            {
              type: "context",
              elements: [
                { type: "mrkdwn", text: `Request ID: \`${req.id}\` · Submitted via the Assessify Leave Portal` },
              ],
            },
          ]
        );
      }

      return NextResponse.json({
        ok: true,
        status: "blocked_balance",
        message:
          `Your leave balance for ${body.leaveType} is exhausted. HR has been notified and will follow up with next steps.`,
      });
    }

    // CEO auto-approval: if the employee IS Bonaventure, skip both approval stages.
    // The request is signed by him, HR is notified (informational only), balance consumed.
    const isCeo =
      employee.slackUserId && employee.slackUserId === effectiveManager.slackUserId &&
      effectiveManager.name === "Bonaventure Wong";

    if (isCeo) {
      const now = new Date();
      const empName = employee.fullName || employee.firstName;
      const leaveReq = await prisma.leaveRequest.create({
        data: {
          employeeId: employee.id,
          lineManagerId: effectiveManager.id,
          department: body.department || null,
          leaveType: body.leaveType,
          startDate: start,
          endDate: end,
          totalDays,
          reason: body.reason || null,
          status: "approved",
          employeeSignature: body.employeeSignature.trim(),
          managerDecision: "approved",
          managerDecisionAt: now,
          managerComments: "Auto-approved — CEO self-approval",
          managerSignature: empName,
          hrDecision: "approved",
          hrDecisionAt: now,
          hrComments: "Auto-approved — notified only",
          hrSignature: "—",
        },
      });

      // Consume balance
      await consumeBalance(employee.id, body.leaveType, totalDays);

      const base = process.env.PUBLIC_APP_URL || "http://localhost:3000";
      const pdfUrl = `${base}/api/leave/${leaveReq.id}/pdf`;

      // Notify HR (informational — no approval needed, but Acknowledge for record)
      const hrId = await getHrSlackId();
      if (hrId) {
        const hrDm = await sendDM(
          hrId,
          `${empName} has taken leave — please acknowledge`,
          [
            {
              type: "header",
              text: { type: "plain_text", text: "CEO Leave Notice" },
            },
            {
              type: "section",
              text: {
                type: "mrkdwn",
                text:
                  `*${empName}* (CEO) has submitted a leave request. Per policy it is auto-approved — no approval action is required from you.\n\n` +
                  `*Leave Type:* ${body.leaveType}\n` +
                  `*From:* ${formatDate(start)}\n` +
                  `*To:* ${formatDate(end)}\n` +
                  `*Total Days:* ${totalDays}\n\n` +
                  (body.reason ? `*Reason:* ${body.reason}\n\n` : "") +
                  `Click *Acknowledge* below so we have a record that you've been informed.`,
              },
            },
            {
              type: "actions",
              elements: [
                {
                  type: "button",
                  style: "primary",
                  text: { type: "plain_text", text: ":white_check_mark: Acknowledge" },
                  action_id: "ceo_acknowledge",
                  value: leaveReq.id,
                },
              ],
            },
            {
              type: "context",
              elements: [
                { type: "mrkdwn", text: `Submitted at ${formatTimestamp(now)} · <${pdfUrl}|View document> · <https://assessify.janusd.io/admin/leave-requests/${leaveReq.id}|Portal record>` },
              ],
            },
          ]
        );
        // Persist ts/channel so the interactive handler can update the message
        if (hrDm.ok && hrDm.ts && hrDm.channel) {
          await prisma.leaveRequest.update({
            where: { id: leaveReq.id },
            data: { hrSlackTs: hrDm.ts, hrSlackChannel: hrDm.channel },
          });
        }
      }

      // Confirm to the CEO himself
      if (employee.slackUserId) {
        const dm = await sendDM(
          employee.slackUserId,
          `Your leave request has been recorded and auto-approved.`,
          [
            {
              type: "header",
              text: { type: "plain_text", text: "Leave Request Auto-Approved" },
            },
            {
              type: "section",
              text: {
                type: "mrkdwn",
                text:
                  `Hi *${empName}*, your leave request has been recorded as approved.\n\n` +
                  `*Leave Type:* ${body.leaveType}\n` +
                  `*From:* ${formatDate(start)}\n` +
                  `*To:* ${formatDate(end)}\n` +
                  `*Total Days:* ${totalDays}\n\n` +
                  `HR (*@mariamm*) has been notified for record-keeping purposes.\n\n` +
                  `<${pdfUrl}|:page_facing_up: View / Download document>`,
              },
            },
          ]
        );
        if (dm.ok && dm.ts) {
          await prisma.leaveRequest.update({
            where: { id: leaveReq.id },
            data: { employeeSlackTs: dm.ts, pdfPath: pdfUrl },
          });
        }
      }

      return NextResponse.json({
        ok: true,
        status: "approved",
        message: `Your leave has been recorded and auto-approved. HR has been notified for record-keeping.`,
      });
    }

    // Happy path: create pending_manager request + DM line manager
    const leaveReq = await prisma.leaveRequest.create({
      data: {
        employeeId: employee.id,
        lineManagerId: effectiveManager.id,
        department: body.department || null,
        leaveType: body.leaveType,
        startDate: start,
        endDate: end,
        totalDays,
        reason: body.reason || null,
        status: "pending_manager",
        employeeSignature: body.employeeSignature.trim(),
      },
    });

    if (effectiveManager.slackUserId) {
      const { text, blocks } = managerApprovalMessage({
        requestId: leaveReq.id,
        employeeName: employee.fullName || employee.firstName,
        leaveType: body.leaveType,
        startDate: formatDate(start),
        endDate: formatDate(end),
        totalDays,
        reason: body.reason || null,
      });
      const dm = await sendDM(effectiveManager.slackUserId, text, blocks);
      if (dm.ok && dm.ts && dm.channel) {
        await prisma.leaveRequest.update({
          where: { id: leaveReq.id },
          data: { managerSlackTs: dm.ts, managerSlackChannel: dm.channel },
        });
      }
    } else {
      console.warn(
        `[leave] Line manager ${effectiveManager.name} has no Slack ID — request ${leaveReq.id} awaiting manual follow-up.`
      );
    }

    return NextResponse.json({
      ok: true,
      status: "pending_manager",
      message: `Your request has been sent to ${effectiveManager.name} for approval. You will be notified once a decision is made.`,
    });
  } catch (err) {
    console.error("[POST /api/leave] error:", err);
    slackAlert("Leave submission failed", err);
    return NextResponse.json({ error: "Internal server error" }, { status: 500 });
  }
}

```