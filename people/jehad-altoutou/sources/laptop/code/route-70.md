---
type: source
source_type: laptop
title: route
slug: route-70
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/slack/interactive/route.ts
original_size: 17705
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/slack/interactive/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import {
  verifySlackSignature,
  sendDM,
  updateMessage,
  openModal,
  getHrSlackId,
  hrApprovalMessage,
  rejectionModal,
  formatDate,
  formatTimestamp,
  slackAlert,
} from "@/lib/slack";
import { consumeBalance } from "@/lib/leave";

type SlackPayload =
  | {
      type: "block_actions";
      trigger_id: string;
      user: { id: string; username?: string; name?: string };
      actions: Array<{ action_id: string; value: string }>;
      container?: { channel_id?: string; message_ts?: string };
      channel?: { id: string };
      message?: { ts: string };
    }
  | {
      type: "view_submission";
      trigger_id: string;
      user: { id: string; username?: string; name?: string };
      view: {
        callback_id: string;
        private_metadata: string;
        state: {
          values: Record<string, Record<string, { value?: string }>>;
        };
      };
    };

export async function POST(req: NextRequest) {
  const rawBody = await req.text();
  const signature = req.headers.get("x-slack-signature");
  const timestamp = req.headers.get("x-slack-request-timestamp");

  if (!verifySlackSignature({ signature, timestamp }, rawBody)) {
    return new Response("invalid signature", { status: 401 });
  }

  // Slack sends form-urlencoded with a `payload` field containing JSON
  const params = new URLSearchParams(rawBody);
  const raw = params.get("payload");
  if (!raw) return new Response("missing payload", { status: 400 });
  const payload = JSON.parse(raw) as SlackPayload;

  try {
    if (payload.type === "block_actions") {
      return handleAction(payload);
    }
    if (payload.type === "view_submission") {
      return handleModalSubmit(payload);
    }
    return NextResponse.json({});
  } catch (err) {
    console.error("[slack/interactive] error:", err);
    slackAlert("Slack interactive handler failed", err);
    return NextResponse.json({ response_action: "errors" });
  }
}

// ─── Action (button click) handlers ──────────────────────────

async function handleAction(
  p: Extract<SlackPayload, { type: "block_actions" }>
): Promise<Response> {
  const action = p.actions[0];
  const requestId = action.value;

  const leaveReq = await prisma.leaveRequest.findUnique({
    where: { id: requestId },
    include: { employee: true, lineManager: true },
  });
  if (!leaveReq) {
    return NextResponse.json({ text: "Request not found." });
  }

  switch (action.action_id) {
    case "approve_manager":
      return approveManager(leaveReq, p);
    case "reject_manager":
      await openModal(
        p.trigger_id,
        rejectionModal({
          requestId,
          stage: "manager",
          employeeName: leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown",
        })
      );
      return new Response("", { status: 200 });
    case "approve_hr":
      return approveHr(leaveReq, p);
    case "ceo_acknowledge":
      return acknowledgeCeo(leaveReq, p);
    case "reject_hr":
      await openModal(
        p.trigger_id,
        rejectionModal({
          requestId,
          stage: "hr",
          employeeName: leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown",
        })
      );
      return new Response("", { status: 200 });
    default:
      return NextResponse.json({ text: "Unknown action." });
  }
}

// ─── Manager approves → notify HR ────────────────────────────

async function approveManager(
  leaveReq: Awaited<ReturnType<typeof prisma.leaveRequest.findUnique>> & {
    employee: { firstName: string; fullName: string | null; slackUserId: string | null };
    lineManager: { name: string; slackUserId: string | null };
  },
  p: Extract<SlackPayload, { type: "block_actions" }>
): Promise<Response> {
  if (!leaveReq) return NextResponse.json({});
  if (leaveReq.status !== "pending_manager") {
    return NextResponse.json({ text: "Already processed." });
  }

  const empName = leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown";
  const mgrName = leaveReq.lineManager?.name ?? "(removed)";

  const now = new Date();
  await prisma.leaveRequest.update({
    where: { id: leaveReq.id },
    data: {
      status: "pending_hr",
      managerDecision: "approved",
      managerDecisionAt: now,
      managerSignature: mgrName,
    },
  });

  // Update manager's original message to show resolved state
  const channel = p.container?.channel_id || p.channel?.id;
  const ts = p.container?.message_ts || p.message?.ts;
  if (channel && ts) {
    await updateMessage(channel, ts, `Approved — forwarded to HR.`, [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text:
            `:white_check_mark: *Approved* by you at ${formatTimestamp(now)}\n` +
            `Leave request for *${empName}* has been forwarded to HR for final approval.`,
        },
      },
    ]);
  }

  // DM HR
  const hrId = await getHrSlackId();
  if (hrId) {
    const { text, blocks } = hrApprovalMessage({
      requestId: leaveReq.id,
      employeeName: empName,
      leaveType: leaveReq.leaveType,
      startDate: formatDate(leaveReq.startDate),
      endDate: formatDate(leaveReq.endDate),
      totalDays: leaveReq.totalDays,
      managerName: mgrName,
      managerComments: null,
      reason: leaveReq.reason,
    });
    const dm = await sendDM(hrId, text, blocks);
    if (dm.ok && dm.ts && dm.channel) {
      await prisma.leaveRequest.update({
        where: { id: leaveReq.id },
        data: { hrSlackTs: dm.ts, hrSlackChannel: dm.channel },
      });
    }
  } else {
    console.warn("[leave] HR Slack ID could not be resolved — manual follow-up required.");
  }

  return NextResponse.json({});
}

// ─── HR approves → finalize, DM employee, mark unread ─────────

async function approveHr(
  leaveReq: Awaited<ReturnType<typeof prisma.leaveRequest.findUnique>> & {
    employee: { firstName: string; fullName: string | null; slackUserId: string | null; id: string };
    lineManager: { name: string };
  },
  p: Extract<SlackPayload, { type: "block_actions" }>
): Promise<Response> {
  if (!leaveReq) return NextResponse.json({});
  if (leaveReq.status !== "pending_hr") {
    return NextResponse.json({ text: "Already processed." });
  }

  const now = new Date();
  const hrName = "Mariam Mahmood";
  const empName = leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown";
  const mgrName = leaveReq.lineManager?.name ?? "(removed)";

  await prisma.leaveRequest.update({
    where: { id: leaveReq.id },
    data: {
      status: "approved",
      hrDecision: "approved",
      hrDecisionAt: now,
      hrSignature: hrName,
    },
  });

  // Consume balance (only for capped leave types)
  if (leaveReq.employee?.id) {
    await consumeBalance(leaveReq.employee.id, leaveReq.leaveType, leaveReq.totalDays);
  }

  // Update HR's message
  const channel = p.container?.channel_id || p.channel?.id;
  const ts = p.container?.message_ts || p.message?.ts;
  if (channel && ts) {
    await updateMessage(channel, ts, `Approved — employee notified.`, [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text:
            `:white_check_mark: *Approved* at ${formatTimestamp(now)}\n` +
            `Leave request for *${empName}* has been approved. The employee has been notified.`,
        },
      },
    ]);
  }

  // Build the absolute URL to the PDF
  const base = process.env.PUBLIC_APP_URL || "http://localhost:3000";
  const pdfUrl = `${base}/api/leave/${leaveReq.id}/pdf`;

  // DM employee
  if (leaveReq.employee?.slackUserId) {
    const dm = await sendDM(
      leaveReq.employee.slackUserId,
      `Your leave request has been approved.`,
      [
        {
          type: "header",
          text: { type: "plain_text", text: "Leave Request Approved" },
        },
        {
          type: "section",
          text: {
            type: "mrkdwn",
            text:
              `Hi *${empName}*, great news — your leave request has been approved.\n\n` +
              `*Leave Type:* ${leaveReq.leaveType}\n` +
              `*From:* ${formatDate(leaveReq.startDate)}\n` +
              `*To:* ${formatDate(leaveReq.endDate)}\n` +
              `*Total Days:* ${leaveReq.totalDays}\n\n` +
              `Approved by *${mgrName}* (Line Manager) and *${hrName}* (HR) on ${formatTimestamp(now)}.\n\n` +
              `<${pdfUrl}|:page_facing_up: View / Download your approval document>`,
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

  return NextResponse.json({});
}

// ─── HR acknowledges a CEO auto-approved leave ───────────────

async function acknowledgeCeo(
  leaveReq: Awaited<ReturnType<typeof prisma.leaveRequest.findUnique>> & {
    employee: { firstName: string; fullName: string | null };
  },
  p: Extract<SlackPayload, { type: "block_actions" }>
): Promise<Response> {
  if (!leaveReq) return NextResponse.json({});
  // Idempotent — clicking twice doesn't re-record
  if (leaveReq.hrAcknowledgedAt) {
    return NextResponse.json({ text: "Already acknowledged." });
  }

  const now = new Date();
  const empName = leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown";
  const ackBy = p.user?.name || p.user?.username || p.user?.id || "HR";

  await prisma.leaveRequest.update({
    where: { id: leaveReq.id },
    data: { hrAcknowledgedAt: now, hrAcknowledgedBy: ackBy },
  });

  const channel = p.container?.channel_id || p.channel?.id;
  const ts = p.container?.message_ts || p.message?.ts;
  if (channel && ts) {
    await updateMessage(channel, ts, `Acknowledged — record kept.`, [
      {
        type: "header",
        text: { type: "plain_text", text: "CEO Leave Notice" },
      },
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text:
            `*${empName}* (CEO) submitted a leave request — auto-approved per policy.\n\n` +
            `:white_check_mark: *Acknowledged by ${ackBy}* at ${formatTimestamp(now)}.`,
        },
      },
      {
        type: "context",
        elements: [
          { type: "mrkdwn", text: `<https://assessify.janusd.io/admin/leave-requests/${leaveReq.id}|View record>` },
        ],
      },
    ]);
  }

  return NextResponse.json({});
}

// ─── Modal submissions (rejection with reason) ────────────────

async function handleModalSubmit(
  p: Extract<SlackPayload, { type: "view_submission" }>
): Promise<Response> {
  const requestId = p.view.private_metadata;
  const reason =
    p.view.state.values.rejection_reason?.reason_input?.value?.trim() || "";

  const leaveReq = await prisma.leaveRequest.findUnique({
    where: { id: requestId },
    include: { employee: true, lineManager: true },
  });
  if (!leaveReq) return NextResponse.json({});

  const now = new Date();
  const isManagerReject = p.view.callback_id === "reject_manager_submit";

  if (isManagerReject && leaveReq.status !== "pending_manager") {
    return NextResponse.json({
      response_action: "errors",
      errors: { rejection_reason: "This request has already been processed." },
    });
  }
  if (!isManagerReject && leaveReq.status !== "pending_hr") {
    return NextResponse.json({
      response_action: "errors",
      errors: { rejection_reason: "This request has already been processed." },
    });
  }

  const empName = leaveReq.employee?.fullName || leaveReq.employee?.firstName || "Unknown employee";
  const mgrName = leaveReq.lineManager?.name ?? "(removed)";

  if (isManagerReject) {
    await prisma.leaveRequest.update({
      where: { id: leaveReq.id },
      data: {
        status: "rejected_manager",
        managerDecision: "rejected",
        managerDecisionAt: now,
        managerComments: reason,
        managerSignature: mgrName,
        // Treat as already reviewed by HR since no HR stage runs — keep out of unread
        viewedByHr: false,
      },
    });
    // Update original Slack DM
    if (leaveReq.managerSlackChannel && leaveReq.managerSlackTs) {
      await updateMessage(
        leaveReq.managerSlackChannel,
        leaveReq.managerSlackTs,
        "Rejected — employee notified.",
        [
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                `:x: *Rejected* by you at ${formatTimestamp(now)}\n` +
                `*Reason:* ${reason || "(none provided)"}\n\n` +
                `The employee has been notified.`,
            },
          },
        ]
      );
    }
    // Notify employee
    if (leaveReq.employee?.slackUserId) {
      await sendDM(
        leaveReq.employee.slackUserId,
        `Your leave request has been declined by your line manager.`,
        [
          {
            type: "header",
            text: { type: "plain_text", text: "Leave Request Declined" },
          },
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                `Hi *${empName}*, unfortunately your leave request has been declined by your line manager, *${mgrName}*.\n\n` +
                `*Leave Type:* ${leaveReq.leaveType}\n` +
                `*From:* ${formatDate(leaveReq.startDate)}\n` +
                `*To:* ${formatDate(leaveReq.endDate)}\n` +
                `*Total Days:* ${leaveReq.totalDays}\n\n` +
                `*Reason provided:* ${reason || "(not provided)"}\n\n` +
                `If you would like to discuss this further, please reach out to your line manager directly.`,
            },
          },
          {
            type: "context",
            elements: [
              { type: "mrkdwn", text: `Decision recorded at ${formatTimestamp(now)}` },
            ],
          },
        ]
      );
    }
    // Also notify HR so she has context even though the flow ended
    const hrIdR = await getHrSlackId();
    if (hrIdR) {
      await sendDM(
        hrIdR,
        `Leave request declined by line manager — ${empName}`,
        [
          {
            type: "header",
            text: { type: "plain_text", text: "Leave Request Declined (No HR Action Needed)" },
          },
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                `*${empName}*'s leave request was declined by their line manager, *${mgrName}*.\n\n` +
                `*Leave Type:* ${leaveReq.leaveType}\n` +
                `*From:* ${formatDate(leaveReq.startDate)}\n` +
                `*To:* ${formatDate(leaveReq.endDate)}\n` +
                `*Total Days:* ${leaveReq.totalDays}\n\n` +
                `*Manager's reason:* ${reason || "(not provided)"}\n\n` +
                `The employee has been notified. No HR action required — logging this for your visibility.`,
            },
          },
          {
            type: "context",
            elements: [
              { type: "mrkdwn", text: `Decision recorded at ${formatTimestamp(now)} · View in portal: <https://assessify.janusd.io/admin/leave-requests/${leaveReq.id}|open>` },
            ],
          },
        ]
      );
    }
  } else {
    // HR rejection
    await prisma.leaveRequest.update({
      where: { id: leaveReq.id },
      data: {
        status: "rejected_hr",
        hrDecision: "rejected",
        hrDecisionAt: now,
        hrComments: reason,
        hrSignature: "Mariam Mahmood",
      },
    });
    if (leaveReq.hrSlackChannel && leaveReq.hrSlackTs) {
      await updateMessage(
        leaveReq.hrSlackChannel,
        leaveReq.hrSlackTs,
        "Rejected — employee notified.",
        [
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                `:x: *Rejected* by HR at ${formatTimestamp(now)}\n` +
                `*Reason:* ${reason || "(none provided)"}\n\n` +
                `The employee has been notified.`,
            },
          },
        ]
      );
    }
    if (leaveReq.employee?.slackUserId) {
      await sendDM(
        leaveReq.employee.slackUserId,
        `Your leave request has been declined by HR.`,
        [
          {
            type: "header",
            text: { type: "plain_text", text: "Leave Request Declined" },
          },
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                `Hi *${empName}*, unfortunately your leave request has been declined by HR.\n\n` +
                `*Leave Type:* ${leaveReq.leaveType}\n` +
                `*From:* ${formatDate(leaveReq.startDate)}\n` +
                `*To:* ${formatDate(leaveReq.endDate)}\n` +
                `*Total Days:* ${leaveReq.totalDays}\n\n` +
                `Your line manager (*${mgrName}*) had approved this request, however HR has declined it with the following reason:\n\n` +
                `*${reason || "(not provided)"}*\n\n` +
                `Please reach out to HR (*@mariamm*) if you have any questions or would like to discuss next steps.`,
            },
          },
          {
            type: "context",
            elements: [
              { type: "mrkdwn", text: `Decision recorded at ${formatTimestamp(now)}` },
            ],
          },
        ]
      );
    }
  }

  return NextResponse.json({});
}


```