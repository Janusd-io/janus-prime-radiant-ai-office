---
type: source
source_type: laptop
title: slack
slug: slack
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/slack.ts
original_size: 16497
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# slack

_Extracted from `[[assessify|assessify]]/src/lib/slack.ts` on 2026-05-14._

```typescript
import crypto from "crypto";

const SLACK_API = "https://slack.com/api";

function token() {
  const t = process.env.SLACK_BOT_TOKEN;
  if (!t) throw new Error("SLACK_BOT_TOKEN not set");
  return t;
}

function secret() {
  const s = process.env.SLACK_SIGNING_SECRET;
  if (!s) throw new Error("SLACK_SIGNING_SECRET not set");
  return s;
}

type SlackBlock = Record<string, unknown>;

async function slackCall<T = Record<string, unknown>>(
  method: string,
  body: Record<string, unknown>
): Promise<T & { ok: boolean; error?: string }> {
  const res = await fetch(`${SLACK_API}/${method}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      Authorization: `Bearer ${token()}`,
    },
    body: JSON.stringify(body),
  });
  return res.json() as Promise<T & { ok: boolean; error?: string }>;
}

/**
 * Open a DM channel with a user. Returns the D-prefixed channel ID.
 * Required when the user hasn't messaged the bot yet — chat.postMessage
 * with a bare user ID as channel fails with "channel_not_found".
 */
async function openDm(userId: string): Promise<string | null> {
  const res = await slackCall<{ channel?: { id: string } }>("conversations.open", {
    users: userId,
  });
  if (!res.ok) {
    console.error("[slack] conversations.open failed:", res.error);
    return null;
  }
  return res.channel?.id ?? null;
}

export async function sendDM(
  userIdOrChannel: string,
  text: string,
  blocks?: SlackBlock[]
): Promise<{ ok: boolean; ts?: string; channel?: string; error?: string }> {
  // Channel IDs (C/D/G prefix) can be used directly. For user IDs (U/W prefix)
  // we first try chat.postMessage directly — works if the user has DMed the bot
  // before. If that fails with channel_not_found, we open a fresh DM via
  // conversations.open (requires im:write scope) and retry.
  const isUserId = userIdOrChannel.startsWith("U") || userIdOrChannel.startsWith("W");
  let channel = userIdOrChannel;

  let res = await slackCall<{ ts?: string; channel?: string }>("chat.postMessage", {
    channel,
    text,
    blocks,
  });

  if (!res.ok && isUserId && res.error === "channel_not_found") {
    const dm = await openDm(userIdOrChannel);
    if (dm) {
      channel = dm;
      res = await slackCall<{ ts?: string; channel?: string }>("chat.postMessage", {
        channel,
        text,
        blocks,
      });
    }
  }

  if (!res.ok) console.error("[slack] sendDM failed:", res.error);
  return res;
}

export async function updateMessage(
  channel: string,
  ts: string,
  text: string,
  blocks?: SlackBlock[]
) {
  const res = await slackCall("chat.update", { channel, ts, text, blocks });
  if (!res.ok) console.error("[slack] updateMessage failed:", res.error);
  return res;
}

export async function openModal(triggerId: string, view: SlackBlock) {
  const res = await slackCall("views.open", { trigger_id: triggerId, view });
  if (!res.ok) console.error("[slack] openModal failed:", res.error);
  return res;
}


/**
 * Slack alert DM to the designated operator (defaults to Jehad).
 * Dedupes identical titles within a 5-minute window so a flapping endpoint
 * doesn't spam. Never throws — alert failures only log to console.
 */
const alertDedupe = new Map<string, number>();
const ALERT_DEDUPE_MS = 5 * 60 * 1000;

export async function slackAlert(
  title: string,
  error: unknown,
  context?: Record<string, unknown>
): Promise<void> {
  const userId = process.env.ALERT_SLACK_USER_ID || "U0ANY8M11M3";
  if (!process.env.SLACK_BOT_TOKEN) return;

  const key = title;
  const now = Date.now();
  const last = alertDedupe.get(key);
  if (last && now - last < ALERT_DEDUPE_MS) return;
  alertDedupe.set(key, now);

  const msg = error instanceof Error ? error.message : String(error);
  const stack = error instanceof Error && error.stack ? error.stack : "";
  const env = process.env.APP_URL || "unknown";

  const blocks: SlackBlock[] = [
    {
      type: "section",
      text: { type: "mrkdwn", text: `:rotating_light: *Assessify alert — ${title}*` },
    },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: `*Error*\n\`${msg.slice(0, 200)}\`` },
        { type: "mrkdwn", text: `*Environment*\n${env}` },
      ],
    },
  ];
  if (context && Object.keys(context).length > 0) {
    blocks.push({
      type: "section",
      text: {
        type: "mrkdwn",
        text: "*Context*\n```" + JSON.stringify(context, null, 2).slice(0, 1500) + "```",
      },
    });
  }
  if (stack) {
    blocks.push({
      type: "section",
      text: {
        type: "mrkdwn",
        text: "*Stack*\n```" + stack.slice(0, 1500) + "```",
      },
    });
  }

  try {
    await sendDM(userId, `:rotating_light: Assessify alert: ${title} — ${msg}`, blocks);
  } catch (e) {
    console.error("[slack] alert DM failed:", e);
  }
}

type SlackUser = {
  id: string;
  name?: string;
  deleted?: boolean;
  is_bot?: boolean;
  profile?: { email?: string; real_name?: string };
};

export async function lookupByHandle(handle: string): Promise<string | null> {
  const res = await fetch(`${SLACK_API}/users.list`, {
    headers: { Authorization: `Bearer ${token()}` },
  });
  const data = (await res.json()) as { ok: boolean; members?: SlackUser[] };
  if (!data.ok || !data.members) return null;
  const clean = handle.replace(/^@/, "").toLowerCase();
  const match = data.members.find(
    (u) => !u.deleted && !u.is_bot && u.name?.toLowerCase() === clean
  );
  return match?.id ?? null;
}

export async function lookupByEmail(email: string): Promise<string | null> {
  const res = await fetch(
    `${SLACK_API}/users.lookupByEmail?email=${encodeURIComponent(email)}`,
    { headers: { Authorization: `Bearer ${token()}` } }
  );
  const data = (await res.json()) as { ok: boolean; user?: SlackUser; error?: string };
  return data.ok && data.user ? data.user.id : null;
}

/** Resolve HR Slack ID once per process, cached. Tries env override, then handle, then email. */
let hrIdCache: string | null | undefined = undefined;
export async function getHrSlackId(): Promise<string | null> {
  if (hrIdCache !== undefined) return hrIdCache;
  const override = process.env.SLACK_HR_USER_ID;
  if (override) {
    hrIdCache = override;
    return override;
  }
  const handle = process.env.SLACK_HR_HANDLE || "mariamm";
  const byHandle = await lookupByHandle(handle);
  if (byHandle) {
    hrIdCache = byHandle;
    return byHandle;
  }
  const email = process.env.SLACK_HR_EMAIL;
  if (email) {
    const byEmail = await lookupByEmail(email);
    if (byEmail) {
      hrIdCache = byEmail;
      return byEmail;
    }
  }
  hrIdCache = null;
  return null;
}

/** Verify Slack request signature per https://api.slack.com/authentication/verifying-requests-from-slack */
export function verifySlackSignature(
  headers: { signature: string | null; timestamp: string | null },
  rawBody: string
): boolean {
  const { signature, timestamp } = headers;
  if (!signature || !timestamp) return false;
  const ts = Number(timestamp);
  if (!Number.isFinite(ts)) return false;
  // Reject if older than 5 minutes (replay protection)
  if (Math.abs(Math.floor(Date.now() / 1000) - ts) > 60 * 5) return false;
  const base = `v0:${timestamp}:${rawBody}`;
  const expected =
    "v0=" + crypto.createHmac("sha256", secret()).update(base).digest("hex");
  try {
    return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(signature));
  } catch {
    return false;
  }
}

// ─── Message builders for leave flow ───────────────────────────

export function managerApprovalMessage(args: {
  requestId: string;
  employeeName: string;
  leaveType: string;
  startDate: string; // formatted
  endDate: string;
  totalDays: number;
  reason: string | null;
}): { text: string; blocks: SlackBlock[] } {
  const { requestId, employeeName, leaveType, startDate, endDate, totalDays, reason } = args;
  const text = `Leave request from ${employeeName} — pending your approval`;
  const blocks: SlackBlock[] = [
    { type: "header", text: { type: "plain_text", text: "Leave Request — Approval Needed" } },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: `*Employee*\n${employeeName}` },
        { type: "mrkdwn", text: `*Leave Type*\n${leaveType}` },
        { type: "mrkdwn", text: `*From*\n${startDate}` },
        { type: "mrkdwn", text: `*To*\n${endDate}` },
        { type: "mrkdwn", text: `*Total Days*\n${totalDays}` },
      ],
    },
    ...(reason
      ? [{ type: "section", text: { type: "mrkdwn", text: `*Reason*\n${reason}` } } as SlackBlock]
      : []),
    { type: "divider" },
    {
      type: "actions",
      block_id: "leave_manager_actions",
      elements: [
        {
          type: "button",
          style: "primary",
          text: { type: "plain_text", text: "Approve" },
          action_id: "approve_manager",
          value: requestId,
        },
        {
          type: "button",
          style: "danger",
          text: { type: "plain_text", text: "Reject" },
          action_id: "reject_manager",
          value: requestId,
        },
      ],
    },
  ];
  return { text, blocks };
}

// ─── Recruitment scoring message ─────────────────────────────

const TIER_EMOJI: Record<string, string> = {
  strong_match: ":star2:",
  match: ":white_check_mark:",
  consider: ":hourglass_flowing_sand:",
  weak: ":warning:",
  reject: ":x:",
};

const TIER_LABEL: Record<string, string> = {
  strong_match: "Strong match",
  match: "Match",
  consider: "Consider",
  weak: "Weak fit",
  reject: "Below threshold",
};

export function recruitmentScoredMessage(args: {
  applicationId: string;
  candidateName: string;
  roleTitle: string;
  department: string;
  office: string | null;
  source: string | null;
  agencyName: string | null;
  score: number;
  tier: string;
  topCriteria: Array<{ label: string; score: number; reasoning: string }>;
  dashboardUrl: string;
}): { text: string; blocks: SlackBlock[] } {
  const {
    applicationId, candidateName, roleTitle, department, office, source,
    agencyName, score, tier, topCriteria, dashboardUrl,
  } = args;
  const tierEmoji = TIER_EMOJI[tier] ?? ":mag:";
  const tierLabel = TIER_LABEL[tier] ?? tier;
  const scorePct = `${(score * 100).toFixed(0)}%`;
  const sourceLabel = source === "agency" && agencyName
    ? `Agency · ${agencyName}`
    : source === "direct"
      ? "Direct application"
      : source ?? "—";

  const text = `New candidate scored — ${candidateName} for ${roleTitle} (${tierLabel}, ${scorePct})`;
  const blocks: SlackBlock[] = [
    {
      type: "header",
      text: { type: "plain_text", text: `${tierEmoji} New candidate scored — ${tierLabel}`, emoji: true },
    },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: `*Candidate*\n${candidateName}` },
        { type: "mrkdwn", text: `*Role*\n${roleTitle}` },
        { type: "mrkdwn", text: `*Department*\n${department}` },
        { type: "mrkdwn", text: `*Office*\n${office ?? "—"}` },
        { type: "mrkdwn", text: `*Source*\n${sourceLabel}` },
        { type: "mrkdwn", text: `*Score*\n${scorePct} (${tierLabel})` },
      ],
    },
    ...(topCriteria.length > 0
      ? [
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text:
                "*Top criteria*\n" +
                topCriteria
                  .map(
                    (c) =>
                      `• *${c.label}* — ${(c.score * 100).toFixed(0)}%${
                        c.reasoning ? ` — ${truncate(c.reasoning, 140)}` : ""
                      }`,
                  )
                  .join("\n"),
            },
          } as SlackBlock,
        ]
      : []),
    { type: "divider" },
    {
      type: "actions",
      block_id: "recruitment_scored_actions",
      elements: [
        {
          type: "button",
          style: "primary",
          text: { type: "plain_text", text: "Open candidate", emoji: true },
          url: dashboardUrl,
          action_id: `open_candidate_${applicationId}`,
        },
      ],
    },
    {
      type: "context",
      elements: [
        {
          type: "mrkdwn",
          text: ":calendar: Schedule the interview from the candidate page (top-right button).",
        },
      ],
    },
  ];
  return { text, blocks };
}

function truncate(s: string, max: number): string {
  if (s.length <= max) return s;
  return s.slice(0, max - 1).trimEnd() + "…";
}

export function hrApprovalMessage(args: {
  requestId: string;
  employeeName: string;
  leaveType: string;
  startDate: string;
  endDate: string;
  totalDays: number;
  managerName: string;
  managerComments: string | null;
  reason: string | null;
}): { text: string; blocks: SlackBlock[] } {
  const {
    requestId, employeeName, leaveType, startDate, endDate, totalDays,
    managerName, managerComments, reason,
  } = args;
  const text = `Leave request from ${employeeName} — approved by ${managerName}, awaiting HR approval`;
  const blocks: SlackBlock[] = [
    { type: "header", text: { type: "plain_text", text: "Leave Request — HR Approval Needed" } },
    {
      type: "context",
      elements: [{ type: "mrkdwn", text: `:white_check_mark: Approved by *${managerName}*` }],
    },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: `*Employee*\n${employeeName}` },
        { type: "mrkdwn", text: `*Leave Type*\n${leaveType}` },
        { type: "mrkdwn", text: `*From*\n${startDate}` },
        { type: "mrkdwn", text: `*To*\n${endDate}` },
        { type: "mrkdwn", text: `*Total Days*\n${totalDays}` },
      ],
    },
    ...(reason
      ? [{ type: "section", text: { type: "mrkdwn", text: `*Reason*\n${reason}` } } as SlackBlock]
      : []),
    ...(managerComments
      ? [{ type: "section", text: { type: "mrkdwn", text: `*Manager Comments*\n${managerComments}` } } as SlackBlock]
      : []),
    { type: "divider" },
    {
      type: "actions",
      block_id: "leave_hr_actions",
      elements: [
        {
          type: "button",
          style: "primary",
          text: { type: "plain_text", text: "Approve" },
          action_id: "approve_hr",
          value: requestId,
        },
        {
          type: "button",
          style: "danger",
          text: { type: "plain_text", text: "Reject" },
          action_id: "reject_hr",
          value: requestId,
        },
      ],
    },
  ];
  return { text, blocks };
}

export function rejectionModal(args: {
  requestId: string;
  stage: "manager" | "hr";
  employeeName: string;
}): SlackBlock {
  const { requestId, stage, employeeName } = args;
  return {
    type: "modal",
    callback_id: stage === "manager" ? "reject_manager_submit" : "reject_hr_submit",
    private_metadata: requestId,
    title: { type: "plain_text", text: "Reject Leave Request" },
    submit: { type: "plain_text", text: "Submit" },
    close: { type: "plain_text", text: "Cancel" },
    blocks: [
      {
        type: "section",
        text: { type: "mrkdwn", text: `Rejecting leave request for *${employeeName}*.` },
      },
      {
        type: "input",
        block_id: "rejection_reason",
        label: { type: "plain_text", text: "Reason" },
        element: {
          type: "plain_text_input",
          action_id: "reason_input",
          multiline: true,
          placeholder: { type: "plain_text", text: "Please provide a reason for the rejection" },
        },
      },
    ],
  };
}

// ─── Formatters ────────────────────────────────────────────────

/** HH:MM AM/PM DD/MM/YY */
export function formatTimestamp(d: Date): string {
  const hours = d.getHours();
  const minutes = d.getMinutes();
  const ampm = hours >= 12 ? "PM" : "AM";
  const h12 = hours % 12 === 0 ? 12 : hours % 12;
  const pad = (n: number) => String(n).padStart(2, "0");
  const dd = pad(d.getDate());
  const mm = pad(d.getMonth() + 1);
  const yy = String(d.getFullYear()).slice(-2);
  return `${pad(h12)}:${pad(minutes)} ${ampm} ${dd}/${mm}/${yy}`;
}

/** DD/MM/YYYY for display */
export function formatDate(d: Date): string {
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${pad(d.getDate())}/${pad(d.getMonth() + 1)}/${d.getFullYear()}`;
}

```