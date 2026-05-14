---
type: source
source_type: laptop
title: route
slug: route-62
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/mcp/route.ts
original_size: 7889
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/mcp/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { extractBearer, verifyMcpToken } from "@/lib/mcp/auth";
import { TOOL_DEFINITIONS, callTool } from "@/lib/mcp/tools";
import { checkRateLimit, getClientIp } from "@/lib/rate-limit";
import { slackAlert } from "@/lib/slack";

export const dynamic = "force-dynamic";

const SERVER_INSTRUCTIONS = `You are connected to Assessify, Janus Digital's HR assessment + leave platform. You help the authenticated admin operate the platform — assume the user has admin authority for the actions they request, and identity is enforced by the bearer token, not by anything you assume here.

The full set of tools you can call is whatever \`tools/list\` returns — read every tool's \`description\` to learn its precise contract. The rules below are cross-cutting and apply to every relevant tool; they do not replace the per-tool descriptions.

MANDATORY BEHAVIOUR:
1. Always call a search_* or list_* tool before any create_*, update_*, or delete_* on the same entity. Never invent IDs — fetch them.
2. Whenever you create or update structured content (assessments, sections, questions, options, invites), present the COMPLETE proposed change to the user as a markdown outline and wait for explicit approval ("yes", "looks good", "create it") before calling the write tool. Drafts are easier to fix before they're written than after.
3. Section weights must sum to exactly 1.0. Adding or removing a section does NOT auto-rebalance — call set_section_weights to fix the distribution before activating an assessment.
4. MCQ questions (single_select / multi_select) need at least one option with points > 0 and at least one with points = 0.
5. Recommendation thresholds must satisfy strongHire > hire > consider, all in 0..1.
6. New assessments default to isActive=false (draft). After creation, return the portal edit URL and ask whether the user wants to activate (toggle_assessment_active).
7. Activations and deactivations are explicit — only call toggle_assessment_active when the user says "activate", "publish", "go live", "deactivate", or a clear synonym in the current turn.
8. Email sends are explicit — for create_candidate_invite, sendEmail defaults to false. Only set it to true when the user literally says "send the invite", "email the candidate", "dispatch", or equivalent in the current turn. A "send it" from a previous turn does not count. If unsure, ask: "Should I email this or just give you the link?"
9. Deletions are permanent — for delete_question and detach_question_from_section, look up the question stem first, show it to the user, and wait for an explicit "yes delete" before calling.
10. After any write, report (a) what changed with IDs, (b) the relevant portal link, and (c) the next action ("review", "activate", "send invite").
11. Bulk and revocation tools follow the same gating: bulk_create_candidate_invites, bulk_toggle_assessment_active, bulk_delete_questions, bulk_tag_questions, revoke_invite, archive_*. Show the full target list to the user and wait for explicit approval before calling — these affect many records at once.
12. When \`externalId\` is provided to a create_* tool (create_assessment, create_candidate_invite, bulk_create_candidate_invites per-row, create_question, add_question, create_job_role, create_competency, create_department), the call is idempotent: a second call with the same externalId returns the existing record (\`idempotent: true\`) instead of creating a duplicate. Use lookup_by_external_id when you only need to map an external ID back to an Assessify ID without writing.

When something the user asks for is outside the available tools (e.g. analytics, candidate scoring, leave management, admin user invites, form templates), tell them it is a portal task and link to https://assessify.janusd.io/admin.
`;

type JsonRpcReq = { jsonrpc: "2.0"; id?: string | number | null; method: string; params?: Record<string, unknown> };
type JsonRpcRes =
  | { jsonrpc: "2.0"; id: string | number | null; result: unknown }
  | { jsonrpc: "2.0"; id: string | number | null; error: { code: number; message: string } };

function rpcOk(id: string | number | null | undefined, result: unknown): JsonRpcRes {
  return { jsonrpc: "2.0", id: id ?? null, result };
}
function rpcErr(id: string | number | null | undefined, code: number, message: string): JsonRpcRes {
  return { jsonrpc: "2.0", id: id ?? null, error: { code, message } };
}

export async function GET() {
  return NextResponse.json({
    name: "assessify-mcp",
    version: "1.0.0",
    protocol: "mcp/1.0",
    transport: "streamable-http",
    note: "POST JSON-RPC 2.0 with Authorization: Bearer <token>.",
  });
}

function authChallengeHeaders(req: NextRequest): Record<string, string> {
  const url = new URL(req.url);
  const base = process.env.PUBLIC_APP_URL ?? `${url.protocol}//${url.host}`;
  const metadata = `${base}/.well-known/oauth-protected-resource`;
  return {
    "WWW-Authenticate": `Bearer realm="Assessify MCP", resource_metadata="${metadata}"`,
  };
}

export async function POST(req: NextRequest) {
  // Rate limit: 60 req/min per IP. Token-authenticated, but a leaked or
  // misbehaving token shouldn't be able to hammer the server until manual
  // revocation. 60/min is generous for normal MCP client usage (one tool
  // call per second peak) but cheap to recover from if hit.
  const rl = checkRateLimit(req, "mcp", 60, 60_000);
  if (rl) return rl;

  const token = extractBearer(req);
  if (!token) {
    return NextResponse.json(rpcErr(null, -32001, "Authorization required"), {
      status: 401,
      headers: authChallengeHeaders(req),
    });
  }
  const session = await verifyMcpToken(token);
  if (!session) {
    return NextResponse.json(rpcErr(null, -32001, "Invalid or expired token"), {
      status: 401,
      headers: authChallengeHeaders(req),
    });
  }

  let payload: JsonRpcReq | JsonRpcReq[];
  try {
    payload = (await req.json()) as JsonRpcReq | JsonRpcReq[];
  } catch {
    return NextResponse.json(rpcErr(null, -32700, "Parse error"), { status: 400 });
  }

  const clientIp = getClientIp(req);
  const handle = async (msg: JsonRpcReq): Promise<JsonRpcRes> => {
    try {
      switch (msg.method) {
        case "initialize":
          return rpcOk(msg.id, {
            protocolVersion: "2024-11-05",
            capabilities: { tools: {} },
            serverInfo: { name: "assessify-mcp", version: "1.0.0" },
            instructions: SERVER_INSTRUCTIONS,
          });
        case "notifications/initialized":
          return rpcOk(msg.id, {});
        case "ping":
          return rpcOk(msg.id, {});
        case "tools/list":
          return rpcOk(msg.id, { tools: TOOL_DEFINITIONS });
        case "tools/call": {
          const params = (msg.params ?? {}) as { name?: string; arguments?: Record<string, unknown> };
          if (!params.name) return rpcErr(msg.id, -32602, "Missing tool name");
          const result = await callTool(params.name, params.arguments ?? {}, session, clientIp);
          return rpcOk(msg.id, result);
        }
        default:
          return rpcErr(msg.id, -32601, `Method not found: ${msg.method}`);
      }
    } catch (e) {
      const errMsg = e instanceof Error ? e.message : String(e);
      console.error(`[mcp] method ${msg.method} failed:`, e);
      slackAlert(`MCP ${msg.method} failed`, e, { method: msg.method, params: msg.params });
      return rpcErr(msg.id, -32000, errMsg);
    }
  };

  if (Array.isArray(payload)) {
    const out = await Promise.all(payload.map(handle));
    return NextResponse.json(out);
  }
  const out = await handle(payload);
  // Notifications (no id) must return 202 without body
  if (payload.method.startsWith("notifications/") && payload.id == null) {
    return new NextResponse(null, { status: 202 });
  }
  return NextResponse.json(out);
}

```