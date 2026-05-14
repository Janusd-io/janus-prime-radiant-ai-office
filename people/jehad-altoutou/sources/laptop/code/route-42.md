---
type: source
source_type: laptop
title: Assessify — route
slug: route-42
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/sessions/[sessionId]/pdf/route.ts"
original_size: 11444
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/sessions/[sessionId]/pdf/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ sessionId: string }> }
) {
  try {
    const admin = await getSession();
    if (!admin) return Response.json({ error: "Unauthorized" }, { status: 401 });

    const { sessionId } = await ctx.params;

    const session = await prisma.candidateSession.findUnique({
      where: { id: sessionId },
      include: {
        version: {
          include: {
            template: { include: { jobRole: { include: { department: true } } } },
            sections: { orderBy: { sortOrder: "asc" } },
          },
        },
        responses: {
          include: {
            question: { include: { options: true } },
            section: true,
          },
          orderBy: { answeredAt: "asc" },
        },
        result: true,
        sectionScores: { include: { section: true } },
        competencyScores: { include: { competency: true } },
      },
    });

    if (!session) return Response.json({ error: "Session not found" }, { status: 404 });

    const r = session.result;
    const overallPct = r ? Math.round(r.normalizedScore * 100) : 0;
    const recLabel = r ? r.recommendation.replace(/_/g, " ") : "N/A";
    const confidencePct = r ? Math.round((r.confidenceRating ?? 0) * 100) : 0;
    const recColor: Record<string, string> = {
      strong_hire: "#059669", hire: "#16a34a", consider: "#d97706", weak_fit: "#ea580c", reject: "#dc2626",
    };
    const recBg: Record<string, string> = {
      strong_hire: "#ecfdf5", hire: "#f0fdf4", consider: "#fffbeb", weak_fit: "#fff7ed", reject: "#fef2f2",
    };

    const dept = session.version.template.jobRole.department.name;
    const role = session.version.template.jobRole.title;
    const templateTitle = session.version.template.title;
    const genDate = new Date().toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });

    const sectionRows = session.sectionScores
      .map((ss) => `
        <tr>
          <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;">${ss.section.title}</td>
          <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;text-align:right;">${ss.score}/${ss.maxScore}</td>
          <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;text-align:right;font-weight:600;">${Math.round(ss.normalizedScore * 100)}%</td>
        </tr>`)
      .join("");

    const competencyRows = session.competencyScores
      .sort((a, b) => b.normalizedScore - a.normalizedScore)
      .map((cs) => {
        const pct = Math.round(cs.normalizedScore * 100);
        const color = pct >= 70 ? "#16a34a" : pct >= 50 ? "#d97706" : "#dc2626";
        return `
          <tr>
            <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;">${cs.competency.name}</td>
            <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;text-align:right;">${cs.score}/${cs.maxScore}</td>
            <td style="padding:10px 16px;border-bottom:1px solid #e4e4e7;text-align:right;font-weight:600;color:${color};">${pct}%</td>
          </tr>`;
      })
      .join("");

    const questionRows = session.responses
      .map((resp) => {
        const selected = resp.selectedOptions ? JSON.parse(resp.selectedOptions) : [];
        const labels = resp.question.options
          .filter((o) => selected.includes(o.key))
          .map((o) => o.label)
          .join(", ");
        const answer = labels || resp.freeTextResponse || "(ranking/drag)";
        const scorePct = resp.maxPoints > 0 ? Math.round((resp.earnedPoints / resp.maxPoints) * 100) : 0;
        const scoreColor = scorePct >= 70 ? "#16a34a" : scorePct >= 40 ? "#d97706" : "#dc2626";
        return `
          <tr>
            <td style="padding:8px 16px;border-bottom:1px solid #f4f4f5;font-size:12px;color:#71717a;">${resp.section.title}</td>
            <td style="padding:8px 16px;border-bottom:1px solid #f4f4f5;font-size:12px;">${resp.question.title}</td>
            <td style="padding:8px 16px;border-bottom:1px solid #f4f4f5;font-size:12px;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${answer}</td>
            <td style="padding:8px 16px;border-bottom:1px solid #f4f4f5;font-size:12px;text-align:right;font-weight:600;color:${scoreColor};">${resp.earnedPoints}/${resp.maxPoints}</td>
            <td style="padding:8px 16px;border-bottom:1px solid #f4f4f5;font-size:12px;text-align:right;color:#71717a;">${resp.timeSpent}s</td>
          </tr>`;
      })
      .join("");

    const flags = r?.flags ? JSON.parse(r.flags) : [];
    const flagBadges = flags.map((f: string) =>
      `<span style="display:inline-block;background:#fef3c7;color:#92400e;padding:3px 10px;border-radius:12px;font-size:11px;margin:2px;font-weight:500;">${f.replace(/_/g, " ")}</span>`
    ).join(" ");

    const startedStr = session.startedAt
      ? new Date(session.startedAt).toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" })
      : "—";
    const completedStr = session.completedAt
      ? new Date(session.completedAt).toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" })
      : "—";

    const html = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Assessment Report — ${session.candidateName}</title>
  <style>
    @page { size: A4; margin: 15mm; }
    @media print {
      body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .no-print { display: none !important; }
    }
    * { box-sizing: border-box; }
    body { margin: 0; padding: 32px 36px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; color: #18181b; font-size: 12px; line-height: 1.5; background: #fff; }

    .header { display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 16px; border-bottom: 2px solid #18181b; margin-bottom: 20px; }
    .header .logo { font-size: 20px; font-weight: 800; letter-spacing: -0.03em; }
    .header .meta { text-align: right; font-size: 10px; color: #71717a; line-height: 1.6; }
    .header .meta .title { font-weight: 600; color: #18181b; font-size: 11px; }

    .candidate { margin-bottom: 20px; }
    .candidate h1 { font-size: 22px; font-weight: 700; margin: 0 0 2px; letter-spacing: -0.02em; }
    .candidate .sub { font-size: 11px; color: #71717a; margin: 0; }
    .candidate .dates { font-size: 10px; color: #a1a1aa; margin: 4px 0 0; }

    .summary { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 20px; }
    .summary .card { border: 1px solid #e4e4e7; border-radius: 8px; padding: 10px 12px; }
    .summary .card .lbl { font-size: 9px; color: #a1a1aa; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; }
    .summary .card .val { font-size: 20px; font-weight: 800; margin-top: 2px; letter-spacing: -0.02em; }
    .summary .card .sub { font-size: 10px; color: #71717a; }

    h2 { font-size: 13px; font-weight: 700; margin: 22px 0 8px; padding-bottom: 6px; border-bottom: 1.5px solid #18181b; }

    table { width: 100%; border-collapse: collapse; }
    th { text-align: left; padding: 7px 12px; background: #f4f4f5; font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #71717a; }
    td { padding: 6px 12px; border-bottom: 1px solid #f0f0f0; font-size: 11px; }

    .hiring-summary { background: #f9fafb; border: 1px solid #e4e4e7; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; font-size: 12px; line-height: 1.6; }

    .flags { margin-bottom: 16px; }

    .footer { margin-top: 32px; padding-top: 12px; border-top: 1px solid #e4e4e7; display: flex; justify-content: space-between; font-size: 9px; color: #a1a1aa; }

    .print-btn { position: fixed; top: 16px; right: 16px; background: #18181b; color: #fff; border: none; padding: 10px 24px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.15); z-index: 100; }
    .print-btn:hover { background: #27272a; }
  </style>
</head>
<body>
  <button class="print-btn no-print" onclick="window.print()">Download PDF</button>

  <!-- Header — first page only (not fixed) -->
  <div class="header">
    <div class="logo">Assessify</div>
    <div class="meta">
      <div class="title">${templateTitle}</div>
      <div>${dept} — ${role}</div>
      <div>Report generated ${genDate}</div>
    </div>
  </div>

  <!-- Candidate -->
  <div class="candidate">
    <h1>${session.candidateName}</h1>
    <p class="sub">${session.candidateEmail}</p>
    <p class="dates">Started: ${startedStr} &nbsp;&middot;&nbsp; Completed: ${completedStr}</p>
  </div>

  ${r ? `
  <!-- Summary -->
  <div class="summary">
    <div class="card">
      <div class="lbl">Overall Score</div>
      <div class="val">${overallPct}%</div>
      <div class="sub">${r.totalScore}/${r.maxScore} pts</div>
    </div>
    <div class="card" style="background:${recBg[r.recommendation] ?? "#f4f4f5"};">
      <div class="lbl">Recommendation</div>
      <div class="val" style="font-size:15px;color:${recColor[r.recommendation] ?? "#18181b"};text-transform:capitalize;">${recLabel}</div>
    </div>
    <div class="card">
      <div class="lbl">Confidence</div>
      <div class="val">${confidencePct}%</div>
    </div>
    <div class="card">
      <div class="lbl">Status</div>
      <div class="val" style="font-size:14px;text-transform:capitalize;">${session.status.replace(/_/g, " ")}</div>
      <div class="sub">${session.responses.length} responses</div>
    </div>
  </div>

  ${r.hiringSummary ? `<div class="hiring-summary"><strong>Hiring Summary:</strong> ${r.hiringSummary}</div>` : ""}
  ${flags.length ? `<div class="flags">${flagBadges}</div>` : ""}
  ` : `<p style="color:#71717a;">Assessment not yet completed.</p>`}

  ${session.sectionScores.length ? `
  <h2>Section Scores</h2>
  <table>
    <thead><tr><th>Section</th><th style="text-align:right;">Points</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>${sectionRows}</tbody>
  </table>` : ""}

  ${session.competencyScores.length ? `
  <h2>Competency Scores</h2>
  <table>
    <thead><tr><th>Competency</th><th style="text-align:right;">Points</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>${competencyRows}</tbody>
  </table>` : ""}

  <h2>Question Responses</h2>
  <table>
    <thead><tr><th>Section</th><th>Question</th><th>Answer</th><th style="text-align:right;">Score</th><th style="text-align:right;">Time</th></tr></thead>
    <tbody>${questionRows}</tbody>
  </table>

  <!-- Footer — flows at bottom of content, not fixed -->
  <div class="footer">
    <div>Assessify — Confidential Assessment Report</div>
    <div>Generated by ${admin.name} (${admin.email}) &middot; ${genDate}</div>
  </div>
</body>
</html>`;

    return new Response(html, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Disposition": `inline; filename="assessment-report-${session.candidateName.replace(/\s+/g, "-")}.html"`,
      },
    });
  } catch (error) {
    console.error("GET /api/admin/sessions/[sessionId]/pdf error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```