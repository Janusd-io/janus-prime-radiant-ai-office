---
type: source
source_type: laptop
title: email
slug: email
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/email.ts
original_size: 28618
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# email

_Extracted from `[[assessify|assessify]]/src/lib/email.ts` on 2026-05-14._

```typescript
import { Resend } from "resend";
import { slackAlert } from "@/lib/slack";

let _resend: Resend | null = null;
function getResend() {
  if (!_resend) {
    _resend = new Resend(process.env.RESEND_API_KEY);
  }
  return _resend;
}

const FROM_EMAIL = process.env.RESEND_FROM_EMAIL ?? "Assessify <onboarding@resend.dev>";

// ─── Assessment Invite Email ────────────────────────────────

export async function sendAssessmentInviteEmail({
  to,
  candidateName,
  assessmentTitle,
  department,
  jobRole,
  inviteLink,
  expiresAt,
}: {
  to: string;
  candidateName: string;
  assessmentTitle: string;
  department: string;
  jobRole: string;
  inviteLink: string;
  expiresAt: Date | null;
}) {
  const expiryText = expiresAt
    ? `This link expires on ${expiresAt.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" })}.`
    : "";

  const { data, error } = await getResend().emails.send({
    from: FROM_EMAIL,
    to: [to],
    subject: `You're invited to take the ${jobRole} assessment`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="padding:32px 32px 0;text-align:center;">
              <div style="display:inline-block;width:48px;height:48px;background-color:#f0f0ff;border-radius:12px;line-height:48px;font-size:24px;">&#10024;</div>
              <h1 style="margin:16px 0 0;font-size:22px;font-weight:700;color:#18181b;letter-spacing:-0.02em;">
                You're Invited
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding:24px 32px;">
              <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#3f3f46;">
                Hi ${candidateName},
              </p>
              <p style="margin:0 0 24px;font-size:15px;line-height:1.6;color:#3f3f46;">
                You have been invited to complete an assessment for the <strong>${jobRole}</strong> position in the <strong>${department}</strong> department.
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#fafafa;border-radius:12px;border:1px solid #e4e4e7;margin-bottom:24px;">
                <tr>
                  <td style="padding:16px;">
                    <p style="margin:0 0 4px;font-size:14px;font-weight:600;color:#18181b;">${assessmentTitle}</p>
                    <p style="margin:0;font-size:13px;color:#71717a;">${department} &middot; ${jobRole}</p>
                  </td>
                </tr>
              </table>
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center">
                    <a href="${inviteLink}" style="display:inline-block;background-color:#18181b;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;padding:12px 32px;border-radius:10px;letter-spacing:-0.01em;">
                      Start Assessment &rarr;
                    </a>
                  </td>
                </tr>
              </table>
              ${expiryText ? `<p style="margin:20px 0 0;font-size:12px;color:#a1a1aa;text-align:center;">${expiryText}</p>` : ""}
            </td>
          </tr>
          <tr>
            <td style="padding:0 32px 32px;">
              <hr style="border:none;border-top:1px solid #e4e4e7;margin:0 0 16px;">
              <p style="margin:0;font-size:12px;color:#a1a1aa;line-height:1.5;">
                If you did not expect this email, you can safely ignore it.<br>
                Sent by Assessify
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`.trim(),
  });

  if (error) {
    console.error("Failed to send assessment invite email:", error);
    slackAlert("Assessment invite email failed", error, { to });
    throw new Error(`Email send failed: ${error.message}`);
  }

  return data;
}

// ─── Form Invite Email ─────────────────────────────────────
// One sender, three voices — picked by formType. Originally only used for
// HR onboarding (personal_data, bank_details), so the copy was hard-coded
// as "Welcome to the Team!". Recruitment intake forms reuse the same code
// path but are NOT onboarding — agencies submitting candidates and direct
// applicants need their own copy that doesn't claim someone is hired.

type FormEmailVariant = {
  category: "hr_onboarding" | "agency_intake" | "direct_intake";
  emoji: string;
  iconBg: string;
  pillBg: string;
  pillBorder: string;
  pillTextStrong: string;
  pillTextLight: string;
  pillCategoryLabel: string;
  subject: (formName: string) => string;
  heading: string;
  greeting: (name: string) => string;
  paragraphs: string[];
  ctaLabel: string;
  helperText: string;
  signoff: string;
};

function pickVariant(formType: string | null | undefined): FormEmailVariant {
  // Default = HR onboarding (preserves prior behaviour for personal_data,
  // bank_details, and any unknown / legacy form types).
  if (formType === "recruitment_intake_agency") {
    return {
      category: "agency_intake",
      emoji: "&#128221;", // 📝
      iconBg: "#eff6ff",
      pillBg: "#eff6ff",
      pillBorder: "#bfdbfe",
      pillTextStrong: "#1e3a8a",
      pillTextLight: "#3b82f6",
      pillCategoryLabel: "Recruitment · Agency Submission",
      subject: (formName) => `Submit a candidate — ${formName}`,
      heading: "Submit a Candidate",
      greeting: (name) => `Hi ${name},`,
      paragraphs: [
        "You've been invited to submit a candidate for an open role through Assessify.",
        "Use the link below to upload the candidate's CV and provide the intake details we need to review them. Submission triggers our automated pre-screening pipeline.",
      ],
      ctaLabel: "Submit Candidate &rarr;",
      helperText:
        "Your progress is saved automatically. You can save and return later. If you need help, reply to this email and our recruitment team will get back to you.",
      signoff: "Sent by Assessify &middot; Recruitment",
    };
  }
  if (formType === "recruitment_intake_direct") {
    return {
      category: "direct_intake",
      emoji: "&#128188;", // 💼
      iconBg: "#eff6ff",
      pillBg: "#eff6ff",
      pillBorder: "#bfdbfe",
      pillTextStrong: "#1e3a8a",
      pillTextLight: "#3b82f6",
      pillCategoryLabel: "Job Application",
      subject: (formName) => `Complete your application — ${formName}`,
      heading: "Complete Your Application",
      greeting: (name) => `Hi ${name},`,
      paragraphs: [
        "Thanks for your interest in the role. To submit your application, we need a few details and your CV.",
        "Use the link below to complete the form. It takes about five minutes.",
      ],
      ctaLabel: "Complete Application &rarr;",
      helperText:
        "Your progress is saved automatically, so you can complete the form at your own pace. If you have any questions, feel free to reply to this email.",
      signoff: "Sent by Assessify &middot; Recruitment",
    };
  }
  // hr_onboarding (personal_data, bank_details, and the historical default).
  return {
    category: "hr_onboarding",
    emoji: "&#127881;", // 🎉
    iconBg: "#ecfdf5",
    pillBg: "#ecfdf5",
    pillBorder: "#bbf7d0",
    pillTextStrong: "#166534",
    pillTextLight: "#4ade80",
    pillCategoryLabel: "Employee Onboarding",
    subject: (formName) => `Welcome aboard! Please complete your ${formName.toLowerCase()}`,
    heading: "Welcome to the Team!",
    greeting: (name) => `Hi ${name},`,
    paragraphs: [
      "Congratulations on your new role! We are excited to have you joining us soon.",
      "To get your onboarding started, we need you to fill out a quick form with some essential details. This helps us set everything up for your first day.",
    ],
    ctaLabel: "Complete Your Form &rarr;",
    helperText:
      "Your progress is saved automatically, so you can complete the form at your own pace. If you have any questions, feel free to reach out to the HR team.",
    signoff: "Welcome aboard! We look forward to working with you.<br>\n                Sent by Assessify &middot; HR Team",
  };
}

export async function sendOnboardingFormEmail({
  to,
  employeeName,
  formName,
  formType,
  inviteLink,
  expiresAt,
}: {
  to: string;
  employeeName: string;
  formName: string;
  /** FormTemplate.formType. Drives copy. Optional for back-compat. */
  formType?: string | null;
  inviteLink: string;
  expiresAt: Date | null;
}) {
  const variant = pickVariant(formType);
  const expiryText = expiresAt
    ? `Please complete this form by ${expiresAt.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" })}.`
    : "";

  const paragraphsHtml = variant.paragraphs
    .map(
      (p, i) =>
        `<p style="margin:0 0 ${i === variant.paragraphs.length - 1 ? "24px" : "8px"};font-size:15px;line-height:1.6;color:#3f3f46;">${p}</p>`,
    )
    .join("\n              ");

  const { data, error } = await getResend().emails.send({
    from: FROM_EMAIL,
    to: [to],
    subject: variant.subject(formName),
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="padding:32px 32px 0;text-align:center;">
              <div style="display:inline-block;width:48px;height:48px;background-color:${variant.iconBg};border-radius:12px;line-height:48px;font-size:24px;">${variant.emoji}</div>
              <h1 style="margin:16px 0 0;font-size:22px;font-weight:700;color:#18181b;letter-spacing:-0.02em;">
                ${variant.heading}
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding:24px 32px;">
              <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#3f3f46;">
                ${variant.greeting(employeeName)}
              </p>
              ${paragraphsHtml}

              <table width="100%" cellpadding="0" cellspacing="0" style="background-color:${variant.pillBg};border-radius:12px;border:1px solid ${variant.pillBorder};margin-bottom:24px;">
                <tr>
                  <td style="padding:16px;">
                    <p style="margin:0 0 4px;font-size:14px;font-weight:600;color:${variant.pillTextStrong};">${formName}</p>
                    <p style="margin:0;font-size:13px;color:${variant.pillTextLight};">${variant.pillCategoryLabel}</p>
                  </td>
                </tr>
              </table>

              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center">
                    <a href="${inviteLink}" style="display:inline-block;background-color:#18181b;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;padding:12px 32px;border-radius:10px;letter-spacing:-0.01em;">
                      ${variant.ctaLabel}
                    </a>
                  </td>
                </tr>
              </table>

              ${expiryText ? `<p style="margin:20px 0 0;font-size:12px;color:#a1a1aa;text-align:center;">${expiryText}</p>` : ""}

              <p style="margin:20px 0 0;font-size:13px;line-height:1.6;color:#71717a;">
                ${variant.helperText}
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding:0 32px 32px;">
              <hr style="border:none;border-top:1px solid #e4e4e7;margin:0 0 16px;">
              <p style="margin:0;font-size:12px;color:#a1a1aa;line-height:1.5;">
                ${variant.signoff}
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`.trim(),
  });

  if (error) {
    console.error("Failed to send form invite email:", error);
    slackAlert("Form invite email failed", error, { to, formType });
    throw new Error(`Email send failed: ${error.message}`);
  }

  return data;
}

// ─── Admin Invite Email ────────────────────────────────────

export async function sendAdminInviteEmail({
  to,
  inviterName,
  role,
  inviteLink,
}: {
  to: string;
  inviterName: string;
  role: string;
  inviteLink: string;
}) {
  const roleLabel = role === "admin" ? "Admin" : "User";

  const { data, error } = await getResend().emails.send({
    from: FROM_EMAIL,
    to: [to],
    subject: `You've been invited to join Assessify`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="padding:32px 32px 0;text-align:center;">
              <div style="display:inline-block;width:48px;height:48px;background-color:#eff6ff;border-radius:12px;line-height:48px;font-size:24px;">&#128101;</div>
              <h1 style="margin:16px 0 0;font-size:22px;font-weight:700;color:#18181b;letter-spacing:-0.02em;">
                You're Invited
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding:24px 32px;">
              <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#3f3f46;">
                Hi there,
              </p>
              <p style="margin:0 0 24px;font-size:15px;line-height:1.6;color:#3f3f46;">
                <strong>${inviterName}</strong> has invited you to join <strong>Assessify</strong> as a <strong>${roleLabel}</strong>. Click the button below to set up your account.
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#eff6ff;border-radius:12px;border:1px solid #bfdbfe;margin-bottom:24px;">
                <tr>
                  <td style="padding:16px;">
                    <p style="margin:0 0 4px;font-size:14px;font-weight:600;color:#1e40af;">Assessify Platform</p>
                    <p style="margin:0;font-size:13px;color:#3b82f6;">Role: ${roleLabel}</p>
                  </td>
                </tr>
              </table>
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center">
                    <a href="${inviteLink}" style="display:inline-block;background-color:#18181b;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;padding:12px 32px;border-radius:10px;letter-spacing:-0.01em;">
                      Set Up Your Account &rarr;
                    </a>
                  </td>
                </tr>
              </table>
              <p style="margin:20px 0 0;font-size:12px;color:#a1a1aa;text-align:center;">This invite expires in 7 days.</p>
            </td>
          </tr>
          <tr>
            <td style="padding:0 32px 32px;">
              <hr style="border:none;border-top:1px solid #e4e4e7;margin:0 0 16px;">
              <p style="margin:0;font-size:12px;color:#a1a1aa;line-height:1.5;">
                If you did not expect this email, you can safely ignore it.<br>
                Sent by Assessify
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`.trim(),
  });

  if (error) {
    console.error("Failed to send admin invite email:", error);
    slackAlert("Admin invite email failed", error, { to });
    throw new Error(`Email send failed: ${error.message}`);
  }

  return data;
}

// ─── Interview Confirmation Email (Phase 1.D) ────────────────

export async function sendInterviewConfirmationEmail({
  to,
  candidateName,
  roleTitle,
  departmentName,
  interviewerEmail,
  scheduledAt,
  durationMin,
  meetUrl,
}: {
  to: string;
  candidateName: string;
  roleTitle: string;
  departmentName: string;
  interviewerEmail: string;
  scheduledAt: Date;
  durationMin: number;
  meetUrl: string | null;
}) {
  const dateFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
  const timeFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  const whenDate = dateFmt.format(scheduledAt);
  const whenTime = timeFmt.format(scheduledAt);

  const { data, error } = await getResend().emails.send({
    from: FROM_EMAIL,
    to: [to],
    subject: `Interview confirmed — ${roleTitle} at Janus Digital`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="padding:32px 32px 0;text-align:center;">
              <div style="display:inline-block;width:48px;height:48px;background-color:#eef9f1;border-radius:12px;line-height:48px;font-size:24px;">&#128197;</div>
              <h1 style="margin:16px 0 0;font-size:22px;font-weight:700;color:#18181b;letter-spacing:-0.02em;">
                Your interview is scheduled
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding:24px 32px 8px;">
              <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#3f3f46;">
                Hi ${candidateName},
              </p>
              <p style="margin:0 0 20px;font-size:15px;line-height:1.6;color:#3f3f46;">
                Thanks for applying for the <strong>${roleTitle}</strong> role in our <strong>${departmentName}</strong> team. We'd like to invite you to an interview. A calendar invite has been sent to this email address — please accept it so the meeting lands in your calendar.
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#fafafa;border-radius:12px;border:1px solid #e4e4e7;margin-bottom:20px;">
                <tr>
                  <td style="padding:16px 18px;">
                    <p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">Date</p>
                    <p style="margin:0 0 14px;font-size:15px;font-weight:600;color:#18181b;">${whenDate}</p>
                    <p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">Time</p>
                    <p style="margin:0 0 14px;font-size:15px;font-weight:600;color:#18181b;">${whenTime} GST (Asia/Dubai) · ${durationMin} minutes</p>
                    <p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">Interviewer</p>
                    <p style="margin:0;font-size:15px;font-weight:600;color:#18181b;">${interviewerEmail}</p>
                  </td>
                </tr>
              </table>
              ${
                meetUrl
                  ? `<table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center" style="padding-bottom:8px;">
                    <a href="${meetUrl}" style="display:inline-block;background-color:#18181b;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;padding:12px 32px;border-radius:10px;letter-spacing:-0.01em;">
                      Join Google Meet &rarr;
                    </a>
                  </td>
                </tr>
              </table>`
                  : ""
              }
              <p style="margin:16px 0 0;font-size:13px;line-height:1.6;color:#71717a;">
                If you need to reschedule or have any questions, just reply to this email and we'll sort it out.
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding:0 32px 32px;">
              <hr style="border:none;border-top:1px solid #e4e4e7;margin:24px 0 16px;" />
              <p style="margin:0;font-size:12px;color:#a1a1aa;text-align:center;">
                Janus Digital · Interview Coordination
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`.trim(),
  });

  if (error) {
    console.error("Failed to send interview confirmation email:", error);
    slackAlert("Interview confirmation email failed", error, { to });
    throw new Error(`Email send failed: ${error.message}`);
  }

  return data;
}

// ─── Interviewer Notification Email (Phase 1.D) ───────────────

export async function sendInterviewerNotificationEmail({
  to,
  candidateName,
  candidateEmail,
  roleTitle,
  departmentName,
  scheduledAt,
  durationMin,
  meetUrl,
  calendarHtmlLink,
  notes,
}: {
  to: string;
  candidateName: string;
  candidateEmail: string;
  roleTitle: string;
  departmentName: string;
  scheduledAt: Date;
  durationMin: number;
  meetUrl: string | null;
  calendarHtmlLink: string | null;
  notes?: string | null;
}) {
  const dateFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
  const timeFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  const whenDate = dateFmt.format(scheduledAt);
  const whenTime = timeFmt.format(scheduledAt);

  const { data, error } = await getResend().emails.send({
    from: FROM_EMAIL,
    to: [to],
    subject: `Interview scheduled — ${candidateName} for ${roleTitle}`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background-color:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f5;padding:40px 20px;">
    <tr>
      <td align="center">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
          <tr>
            <td style="padding:32px 32px 0;text-align:center;">
              <div style="display:inline-block;width:48px;height:48px;background-color:#eef2ff;border-radius:12px;line-height:48px;font-size:24px;">&#128100;</div>
              <h1 style="margin:16px 0 0;font-size:22px;font-weight:700;color:#18181b;letter-spacing:-0.02em;">
                You&rsquo;re scheduled to interview
              </h1>
            </td>
          </tr>
          <tr>
            <td style="padding:24px 32px 8px;">
              <p style="margin:0 0 16px;font-size:15px;line-height:1.6;color:#3f3f46;">
                An interview has been booked on your calendar for the <strong>${roleTitle}</strong> role in the <strong>${departmentName}</strong> team.
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#fafafa;border-radius:12px;border:1px solid #e4e4e7;margin-bottom:20px;">
                <tr>
                  <td style="padding:16px 18px;">
                    <p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">Candidate</p>
                    <p style="margin:0 0 4px;font-size:15px;font-weight:600;color:#18181b;">${candidateName}</p>
                    <p style="margin:0 0 14px;font-size:13px;color:#71717a;">${candidateEmail}</p>
                    <p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">When</p>
                    <p style="margin:0 0 14px;font-size:15px;font-weight:600;color:#18181b;">${whenDate} &middot; ${whenTime} GST &middot; ${durationMin} min</p>
                    ${
                      notes
                        ? `<p style="margin:0 0 6px;font-size:12px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:0.04em;">Notes</p>
                    <p style="margin:0;font-size:14px;color:#3f3f46;white-space:pre-wrap;">${escapeHtml(notes)}</p>`
                        : ""
                    }
                  </td>
                </tr>
              </table>
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center" style="padding-bottom:8px;">
                    ${
                      meetUrl
                        ? `<a href="${meetUrl}" style="display:inline-block;background-color:#18181b;color:#ffffff;font-size:14px;font-weight:600;text-decoration:none;padding:12px 28px;border-radius:10px;letter-spacing:-0.01em;margin-right:8px;">Join Google Meet &rarr;</a>`
                        : ""
                    }
                    ${
                      calendarHtmlLink
                        ? `<a href="${calendarHtmlLink}" style="display:inline-block;background-color:#ffffff;color:#18181b;border:1px solid #d4d4d8;font-size:14px;font-weight:600;text-decoration:none;padding:12px 28px;border-radius:10px;letter-spacing:-0.01em;">Open in Calendar</a>`
                        : ""
                    }
                  </td>
                </tr>
              </table>
              <p style="margin:16px 0 0;font-size:12px;line-height:1.6;color:#a1a1aa;">
                You should also receive a Google Calendar invite at this address once OAuth is fully configured. If not, click &ldquo;Open in Calendar&rdquo; above.
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding:0 32px 32px;">
              <hr style="border:none;border-top:1px solid #e4e4e7;margin:24px 0 16px;" />
              <p style="margin:0;font-size:12px;color:#a1a1aa;text-align:center;">
                Janus Digital &middot; Interview Coordination
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>`.trim(),
  });

  if (error) {
    console.error("Failed to send interviewer notification email:", error);
    slackAlert("Interviewer notification email failed", error, { to });
    // Don't throw — interviewer email is a courtesy, not load-bearing.
    return null;
  }

  return data;
}

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// ─── Backward compatibility alias ───────────────────────────
export const sendInviteEmail = sendAssessmentInviteEmail;

```