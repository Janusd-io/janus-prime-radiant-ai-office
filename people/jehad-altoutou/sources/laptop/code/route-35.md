---
type: source
source_type: laptop
title: Assessify — route
slug: route-35
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/recruitment/applications/[id]/schedule-interview/route.ts"
original_size: 8060
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/recruitment/applications/[id]/schedule-interview/route.ts` on 2026-05-14._

```typescript
/**
 * Phase 1.D: book an interview from the candidate detail page.
 *
 * Mirrors the (now-deleted) Slack `submitInterviewSchedule` handler. Inputs
 * arrive from the admin UI modal as Dubai-local date+time strings.
 *
 * Responses:
 *   200 { ok: true, interview: { ... } }
 *   409 { error, alternatives: [{ start, end }] }   // conflict
 *   400 { error }                                    // validation
 *   409 { error }                                    // no interviewer configured / past time / etc.
 */
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import {
  resolveInterviewerEmail,
  isBusyAt,
  findNextOpenSlots,
  createInterviewEvent,
  isWithinBusinessHours,
  INTERVIEW_DEFAULTS,
} from "@/lib/google-calendar";
import {
  sendInterviewConfirmationEmail,
  sendInterviewerNotificationEmail,
} from "@/lib/email";
import { auditLog } from "@/lib/audit";

const TERMINAL_STAGES = new Set([
  "hired",
  "rejected",
  "withdrawn",
]);

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id: applicationId } = await ctx.params;

  const application = await prisma.application.findUnique({
    where: { id: applicationId },
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
    },
  });
  if (!application) {
    return NextResponse.json({ error: "Application not found" }, { status: 404 });
  }
  if (application.status !== "active" || TERMINAL_STAGES.has(application.currentStage)) {
    return NextResponse.json(
      { error: `Application is ${application.currentStage}; can't schedule an interview.` },
      { status: 409 },
    );
  }

  const body = (await req.json().catch(() => ({}))) as {
    date?: string; // YYYY-MM-DD (Dubai)
    time?: string; // HH:mm (Dubai)
    durationMin?: number;
    notes?: string;
  };
  if (!body.date || !body.time) {
    return NextResponse.json(
      { error: "date and time are required" },
      { status: 400 },
    );
  }
  const duration = Number(body.durationMin ?? INTERVIEW_DEFAULTS.defaultDurationMin);
  if (!Number.isFinite(duration) || duration < 15 || duration > 240) {
    return NextResponse.json(
      { error: "durationMin must be between 15 and 240" },
      { status: 400 },
    );
  }

  const start = dubaiClockToUtc(body.date, body.time);
  if (Number.isNaN(start.getTime())) {
    return NextResponse.json({ error: "Invalid date/time" }, { status: 400 });
  }
  if (start.getTime() < Date.now() + 30 * 60_000) {
    return NextResponse.json(
      { error: "Pick a time at least 30 minutes from now." },
      { status: 400 },
    );
  }
  if (!isWithinBusinessHours(start, duration)) {
    return NextResponse.json(
      {
        error: `Must be Mon–Fri ${INTERVIEW_DEFAULTS.businessHoursStart}:00–${INTERVIEW_DEFAULTS.businessHoursEnd}:00 ${INTERVIEW_DEFAULTS.timezone}.`,
      },
      { status: 400 },
    );
  }

  const interviewer = await resolveInterviewerEmail(applicationId);
  if (!interviewer.email) {
    return NextResponse.json(
      {
        error:
          "No interviewer configured. Set Department.defaultInterviewer or JobRole.interviewerEmail first.",
      },
      { status: 409 },
    );
  }

  const end = new Date(start.getTime() + duration * 60_000);
  const busy = await isBusyAt(interviewer.email, start, end);
  if (busy) {
    const alternatives = await findNextOpenSlots(interviewer.email, {
      durationMin: duration,
      count: 3,
      from: start,
    });
    return NextResponse.json(
      {
        error: `${interviewer.email} is already busy at that time.`,
        conflict: true,
        alternatives: alternatives.map((a) => ({
          start: a.start.toISOString(),
          end: a.end.toISOString(),
        })),
      },
      { status: 409 },
    );
  }

  const candidate = application.candidate;
  const candidateName = `${candidate.firstName} ${candidate.lastName}`;
  let event;
  try {
    event = await createInterviewEvent({
      candidateEmail: candidate.email,
      candidateName,
      interviewerEmail: interviewer.email,
      roleTitle: application.jobRole.title,
      start,
      durationMin: duration,
      description: body.notes
        ? `Interview for ${application.jobRole.title}.\n\n${body.notes}`
        : `Interview for ${application.jobRole.title}.`,
    });
  } catch (err) {
    console.error("[schedule-interview] createInterviewEvent failed:", err);
    return NextResponse.json(
      {
        error:
          "Couldn't create the calendar event. Check Google OAuth or set GOOGLE_MOCK=1 to test without provisioning.",
      },
      { status: 502 },
    );
  }

  const now = new Date();
  const interview = await prisma.interview.create({
    data: {
      applicationId,
      scheduledAt: start,
      durationMin: duration,
      timezone: INTERVIEW_DEFAULTS.timezone,
      interviewerEmail: interviewer.email,
      interviewerName: interviewer.email.split("@")[0],
      candidateEmail: candidate.email,
      meetUrl: event.meetUrl,
      calendarEventId: event.eventId,
      calendarHtmlLink: event.htmlLink,
      scheduledBySlackUserId: null,
    },
  });

  await prisma.application.update({
    where: { id: applicationId },
    data: { currentStage: "interview_scheduled" },
  });
  await prisma.applicationStage.create({
    data: {
      applicationId,
      stage: "interview_scheduled",
      enteredAt: now,
      notes: `Interview scheduled for ${formatSlotDubai(start, duration)} with ${interviewer.email} (by ${session.email})`,
      actorId: session.id,
    },
  });

  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "recruitment.interview.scheduled",
    targetType: "Application",
    targetId: applicationId,
    details: {
      interviewId: interview.id,
      interviewerEmail: interviewer.email,
      scheduledAt: start.toISOString(),
      durationMin: duration,
      mock: INTERVIEW_DEFAULTS.mock,
    },
  });

  try {
    await sendInterviewConfirmationEmail({
      to: candidate.email,
      candidateName,
      roleTitle: application.jobRole.title,
      departmentName: application.jobRole.department.name,
      interviewerEmail: interviewer.email,
      scheduledAt: start,
      durationMin: duration,
      meetUrl: event.meetUrl,
    });
  } catch (err) {
    console.error("[schedule-interview] confirmation email failed:", err);
  }

  try {
    await sendInterviewerNotificationEmail({
      to: interviewer.email,
      candidateName,
      candidateEmail: candidate.email,
      roleTitle: application.jobRole.title,
      departmentName: application.jobRole.department.name,
      scheduledAt: start,
      durationMin: duration,
      meetUrl: event.meetUrl,
      calendarHtmlLink: event.htmlLink,
      notes: body.notes,
    });
  } catch (err) {
    console.error("[schedule-interview] interviewer notification email failed:", err);
  }

  return NextResponse.json({
    ok: true,
    mock: INTERVIEW_DEFAULTS.mock,
    interview: {
      id: interview.id,
      scheduledAt: interview.scheduledAt.toISOString(),
      durationMin: interview.durationMin,
      interviewerEmail: interview.interviewerEmail,
      meetUrl: interview.meetUrl,
      calendarHtmlLink: interview.calendarHtmlLink,
    },
  });
}

function dubaiClockToUtc(date: string, time: string): Date {
  const [y, mo, d] = date.split("-").map(Number);
  const [h, mi] = time.split(":").map(Number);
  return new Date(Date.UTC(y, mo - 1, d, h - 4, mi));
}

function formatSlotDubai(start: Date, durationMin: number): string {
  const fmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    weekday: "short",
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  return `${fmt.format(start)} GST (${durationMin} min)`;
}

```