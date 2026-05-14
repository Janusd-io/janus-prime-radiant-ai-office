---
type: source
source_type: laptop
title: google-calendar
slug: google-calendar
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/google-calendar.ts
original_size: 14886
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# google-calendar

_Extracted from `[[assessify|assessify]]/src/lib/google-calendar.ts` on 2026-05-14._

```typescript
/**
 * Google Calendar client for Phase 1.D interview scheduling.
 *
 * Hits Google's REST APIs directly (no `googleapis` SDK) so the bundle stays
 * small. Three core operations:
 *   - getFreeBusy(emails, start, end) → busy intervals per attendee
 *   - findNextOpenSlots(interviewerEmail, durationMin, count) → suggestions
 *   - createInterviewEvent(...) → returns { eventId, meetUrl, htmlLink }
 *
 * Provisioning model:
 *   - One Workspace mailbox owns the events (interview@janusd.com).
 *   - Each interviewer shares free/busy with that mailbox in Calendar settings.
 *   - A long-lived OAuth refresh_token for the mailbox lives in GoogleToken.
 *
 * Mock mode:
 *   Set GOOGLE_MOCK=1 to bypass real Google calls. Useful before provisioning
 *   is complete. Returns deterministic fake free/busy + fake event IDs.
 */
import { prisma } from "@/lib/db";

const GOOGLE_MOCK = process.env.GOOGLE_MOCK === "1";

const INTERVIEW_MAILBOX = process.env.INTERVIEW_MAILBOX_EMAIL ?? "interview@janusd.com";
const FIREFLIES_EMAIL = process.env.FIREFLIES_INVITE_EMAIL ?? "fred@fireflies.ai";
const TIMEZONE = process.env.INTERVIEW_TIMEZONE ?? "Asia/Dubai";
const BUSINESS_HOURS_START = Number(process.env.INTERVIEW_BUSINESS_HOURS_START ?? "9");
const BUSINESS_HOURS_END = Number(process.env.INTERVIEW_BUSINESS_HOURS_END ?? "18");
const DEFAULT_DURATION_MIN = Number(process.env.INTERVIEW_DEFAULT_DURATION_MIN ?? "60");

export const INTERVIEW_DEFAULTS = {
  mailbox: INTERVIEW_MAILBOX,
  firefliesEmail: FIREFLIES_EMAIL,
  timezone: TIMEZONE,
  businessHoursStart: BUSINESS_HOURS_START,
  businessHoursEnd: BUSINESS_HOURS_END,
  defaultDurationMin: DEFAULT_DURATION_MIN,
  mock: GOOGLE_MOCK,
};

// ─── Access token refresh ────────────────────────────────────

let cachedAccessToken: { token: string; expiresAt: number } | null = null;

async function getAccessToken(): Promise<string> {
  if (GOOGLE_MOCK) return "mock-access-token";

  // Reuse cached token if it's still good for >60s.
  if (cachedAccessToken && cachedAccessToken.expiresAt - Date.now() > 60_000) {
    return cachedAccessToken.token;
  }

  const row = await prisma.googleToken.findUnique({
    where: { email: INTERVIEW_MAILBOX },
  });
  if (!row) {
    throw new Error(
      `[google-calendar] No GoogleToken row for ${INTERVIEW_MAILBOX} — ` +
        `run /api/google/oauth/start to capture the refresh token first.`,
    );
  }

  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_OAUTH_CLIENT_SECRET;
  if (!clientId || !clientSecret) {
    throw new Error(
      "[google-calendar] GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_CLIENT_SECRET not set",
    );
  }

  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: clientId,
      client_secret: clientSecret,
      refresh_token: row.refreshToken,
      grant_type: "refresh_token",
    }),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`[google-calendar] token refresh failed: ${res.status} ${body}`);
  }
  const json = (await res.json()) as { access_token: string; expires_in: number };
  cachedAccessToken = {
    token: json.access_token,
    expiresAt: Date.now() + json.expires_in * 1000,
  };
  await prisma.googleToken.update({
    where: { email: INTERVIEW_MAILBOX },
    data: { lastRefreshAt: new Date() },
  });
  return json.access_token;
}

// ─── Interviewer resolution ──────────────────────────────────

/**
 * Resolve the interviewer email for an application via COALESCE:
 *   JobRole.interviewerEmail ?? Department.defaultInterviewer ?? null
 */
export async function resolveInterviewerEmail(applicationId: string): Promise<{
  email: string | null;
  source: "jobrole" | "department" | "none";
  roleTitle: string;
  departmentName: string;
}> {
  const app = await prisma.application.findUnique({
    where: { id: applicationId },
    include: { jobRole: { include: { department: true } } },
  });
  if (!app) throw new Error(`Application ${applicationId} not found`);
  const role = app.jobRole;
  if (role.interviewerEmail) {
    return {
      email: role.interviewerEmail,
      source: "jobrole",
      roleTitle: role.title,
      departmentName: role.department.name,
    };
  }
  if (role.department.defaultInterviewer) {
    return {
      email: role.department.defaultInterviewer,
      source: "department",
      roleTitle: role.title,
      departmentName: role.department.name,
    };
  }
  return {
    email: null,
    source: "none",
    roleTitle: role.title,
    departmentName: role.department.name,
  };
}

// ─── Free/busy ───────────────────────────────────────────────

export type BusyInterval = { start: Date; end: Date };

export async function getFreeBusy(
  emails: string[],
  windowStart: Date,
  windowEnd: Date,
): Promise<Record<string, BusyInterval[]>> {
  if (GOOGLE_MOCK) {
    // Deterministic mock: every weekday 12:00–13:00 local is "busy" (lunch).
    const result: Record<string, BusyInterval[]> = {};
    for (const email of emails) {
      const intervals: BusyInterval[] = [];
      const cursor = new Date(windowStart);
      while (cursor < windowEnd) {
        const dow = cursor.getDay();
        if (dow !== 0 && dow !== 6) {
          const lunchStart = new Date(cursor);
          lunchStart.setHours(12, 0, 0, 0);
          const lunchEnd = new Date(cursor);
          lunchEnd.setHours(13, 0, 0, 0);
          if (lunchStart >= windowStart && lunchEnd <= windowEnd) {
            intervals.push({ start: lunchStart, end: lunchEnd });
          }
        }
        cursor.setDate(cursor.getDate() + 1);
        cursor.setHours(0, 0, 0, 0);
      }
      result[email] = intervals;
    }
    return result;
  }

  const accessToken = await getAccessToken();
  const res = await fetch("https://www.googleapis.com/calendar/v3/freeBusy", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      timeMin: windowStart.toISOString(),
      timeMax: windowEnd.toISOString(),
      timeZone: TIMEZONE,
      items: emails.map((email) => ({ id: email })),
    }),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`[google-calendar] freeBusy failed: ${res.status} ${body}`);
  }
  const json = (await res.json()) as {
    calendars: Record<string, { busy?: Array<{ start: string; end: string }>; errors?: unknown[] }>;
  };
  const result: Record<string, BusyInterval[]> = {};
  for (const email of emails) {
    const cal = json.calendars[email];
    if (!cal || cal.errors) {
      // Not shared / not visible — treat as "no data" (empty busy list).
      result[email] = [];
      continue;
    }
    result[email] = (cal.busy ?? []).map((b) => ({
      start: new Date(b.start),
      end: new Date(b.end),
    }));
  }
  return result;
}

// ─── Slot suggestions ────────────────────────────────────────

export type Slot = { start: Date; end: Date };

/**
 * Find the next `count` open slots of `durationMin` for `interviewerEmail`
 * starting from `from` (defaults to now + 1h to give HR breathing room),
 * inside business hours (Mon–Fri 09:00–18:00 in INTERVIEW_TIMEZONE).
 *
 * Granularity: 30-minute aligned starts.
 */
export async function findNextOpenSlots(
  interviewerEmail: string,
  opts: { durationMin?: number; count?: number; from?: Date } = {},
): Promise<Slot[]> {
  const durationMin = opts.durationMin ?? DEFAULT_DURATION_MIN;
  const count = opts.count ?? 3;
  const from = opts.from ?? new Date(Date.now() + 60 * 60_000);

  // Look ahead 14 calendar days, which is plenty for ~3 suggestions.
  const windowEnd = new Date(from.getTime() + 14 * 24 * 60 * 60_000);
  const busyMap = await getFreeBusy([interviewerEmail], from, windowEnd);
  const busy = busyMap[interviewerEmail] ?? [];

  const slots: Slot[] = [];
  // Iterate 30-minute steps starting at the next half-hour boundary >= from.
  const cursor = new Date(from);
  cursor.setMinutes(cursor.getMinutes() >= 30 ? 60 : 30, 0, 0);

  while (cursor < windowEnd && slots.length < count) {
    const localHour = getLocalHour(cursor);
    const dow = getLocalDow(cursor);
    const isWeekday = dow >= 1 && dow <= 5;
    const startsInHours = localHour >= BUSINESS_HOURS_START && localHour < BUSINESS_HOURS_END;
    const endsInHours =
      (localHour * 60 + cursor.getMinutes() + durationMin) <= BUSINESS_HOURS_END * 60;

    if (isWeekday && startsInHours && endsInHours) {
      const slotEnd = new Date(cursor.getTime() + durationMin * 60_000);
      const overlaps = busy.some((b) => !(slotEnd <= b.start || cursor >= b.end));
      if (!overlaps) {
        slots.push({ start: new Date(cursor), end: slotEnd });
      }
    }
    cursor.setMinutes(cursor.getMinutes() + 30);
  }
  return slots;
}

/**
 * Returns local hour/dow in INTERVIEW_TIMEZONE. Uses Intl, no extra deps.
 */
function getLocalHour(d: Date): number {
  const f = new Intl.DateTimeFormat("en-GB", {
    timeZone: TIMEZONE,
    hour: "numeric",
    hour12: false,
  });
  return Number(f.format(d));
}
function getLocalDow(d: Date): number {
  // 0=Sun..6=Sat
  const f = new Intl.DateTimeFormat("en-US", { timeZone: TIMEZONE, weekday: "short" });
  const dayMap: Record<string, number> = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
  return dayMap[f.format(d)] ?? 0;
}

/**
 * Returns true if the interviewer is busy during the proposed window.
 * Falls back to "not busy" if free/busy data is missing (calendar not shared).
 */
export async function isBusyAt(
  interviewerEmail: string,
  start: Date,
  end: Date,
): Promise<boolean> {
  const busyMap = await getFreeBusy([interviewerEmail], start, end);
  const intervals = busyMap[interviewerEmail] ?? [];
  return intervals.some((b) => !(end <= b.start || start >= b.end));
}

// ─── Event creation ──────────────────────────────────────────

export type CreateInterviewEventArgs = {
  candidateEmail: string;
  candidateName: string;
  interviewerEmail: string;
  interviewerName?: string;
  roleTitle: string;
  start: Date;
  durationMin: number;
  description?: string;
  includeFireflies?: boolean;
};

export type CreatedEvent = {
  eventId: string;
  meetUrl: string | null;
  htmlLink: string | null;
};

export async function createInterviewEvent(
  args: CreateInterviewEventArgs,
): Promise<CreatedEvent> {
  const end = new Date(args.start.getTime() + args.durationMin * 60_000);

  if (GOOGLE_MOCK) {
    const id = `mock-event-${Math.random().toString(36).slice(2, 10)}`;
    // Build a Google Calendar *prefill* URL so "Open in Calendar" opens the
    // event editor with title, time, attendees, and description already filled
    // in — the interviewer just hits Save in their own calendar. This is the
    // only way to surface a real-looking event before real OAuth is wired.
    const attendees = [args.candidateEmail, args.interviewerEmail];
    if (args.includeFireflies !== false) attendees.push(FIREFLIES_EMAIL);
    const params = new URLSearchParams({
      action: "TEMPLATE",
      text: `Interview · ${args.candidateName} · ${args.roleTitle}`,
      dates: `${toGcalDate(args.start)}/${toGcalDate(end)}`,
      details: args.description ?? `Interview for ${args.roleTitle}.`,
      add: attendees.join(","),
      ctz: TIMEZONE,
    });
    return {
      eventId: id,
      meetUrl: `https://meet.google.com/mock-${id.slice(-6)}`,
      htmlLink: `https://calendar.google.com/calendar/render?${params.toString()}`,
    };
  }

  const accessToken = await getAccessToken();
  const attendees = [
    { email: args.candidateEmail, displayName: args.candidateName },
    { email: args.interviewerEmail, displayName: args.interviewerName ?? args.interviewerEmail },
  ];
  if (args.includeFireflies !== false) {
    attendees.push({ email: FIREFLIES_EMAIL, displayName: "Fireflies Notetaker" });
  }

  const body = {
    summary: `Interview · ${args.candidateName} · ${args.roleTitle}`,
    description: args.description ?? "",
    start: { dateTime: args.start.toISOString(), timeZone: TIMEZONE },
    end: { dateTime: end.toISOString(), timeZone: TIMEZONE },
    attendees,
    conferenceData: {
      createRequest: {
        requestId: `assessify-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
        conferenceSolutionKey: { type: "hangoutsMeet" },
      },
    },
    reminders: { useDefault: true },
  };

  const url = new URL(
    `https://www.googleapis.com/calendar/v3/calendars/${encodeURIComponent(INTERVIEW_MAILBOX)}/events`,
  );
  url.searchParams.set("conferenceDataVersion", "1");
  url.searchParams.set("sendUpdates", "all");

  const res = await fetch(url.toString(), {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const errBody = await res.text();
    throw new Error(`[google-calendar] event create failed: ${res.status} ${errBody}`);
  }
  const json = (await res.json()) as {
    id: string;
    hangoutLink?: string;
    htmlLink?: string;
    conferenceData?: { entryPoints?: Array<{ entryPointType: string; uri: string }> };
  };
  const meetUrl =
    json.hangoutLink ??
    json.conferenceData?.entryPoints?.find((e) => e.entryPointType === "video")?.uri ??
    null;
  return {
    eventId: json.id,
    meetUrl,
    htmlLink: json.htmlLink ?? null,
  };
}

/**
 * Format a Date as Google Calendar's URL date param: YYYYMMDDTHHMMSSZ (UTC).
 */
function toGcalDate(d: Date): string {
  const pad = (n: number) => String(n).padStart(2, "0");
  return (
    `${d.getUTCFullYear()}${pad(d.getUTCMonth() + 1)}${pad(d.getUTCDate())}` +
    `T${pad(d.getUTCHours())}${pad(d.getUTCMinutes())}${pad(d.getUTCSeconds())}Z`
  );
}

// ─── Business-hours guard helper (for UI / modal validation) ──

export function isWithinBusinessHours(start: Date, durationMin: number): boolean {
  const dow = getLocalDow(start);
  if (dow < 1 || dow > 5) return false;
  const startMin = getLocalHour(start) * 60 + Number(
    new Intl.DateTimeFormat("en-GB", { timeZone: TIMEZONE, minute: "numeric" }).format(start),
  );
  const endMin = startMin + durationMin;
  return startMin >= BUSINESS_HOURS_START * 60 && endMin <= BUSINESS_HOURS_END * 60;
}

```