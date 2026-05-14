---
type: source
source_type: laptop
title: auth
slug: auth-2
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/auth.ts
original_size: 2135
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# auth

_Extracted from `[[assessify|assessify]]/src/lib/mcp/auth.ts` on 2026-05-14._

```typescript
import crypto from "crypto";
import { prisma } from "@/lib/db";

export const TOKEN_PREFIX = "asf_mcp_";

export function generateToken(): { raw: string; prefix: string; hash: string } {
  const secret = crypto.randomBytes(32).toString("base64url");
  const raw = `${TOKEN_PREFIX}${secret}`;
  const hash = crypto.createHash("sha256").update(raw).digest("hex");
  const prefix = raw.slice(0, 14);
  return { raw, prefix, hash };
}

export function hashToken(raw: string): string {
  return crypto.createHash("sha256").update(raw).digest("hex");
}

export type McpSession = {
  userId: string;
  userName: string;
  userEmail: string;
  role: string;
  tokenId: string;
  scopes: string[];
  // Recruitment scoping (Phase 1.A). null = global access.
  office: string | null;
  scopedDepartments: string | null;
};

/**
 * Verify bearer token against McpToken table. Returns session info or null.
 * Updates lastUsedAt on success (fire-and-forget).
 */
export async function verifyMcpToken(raw: string): Promise<McpSession | null> {
  if (!raw?.startsWith(TOKEN_PREFIX)) return null;
  const tokenHash = hashToken(raw);
  const token = await prisma.mcpToken.findUnique({ where: { tokenHash } });
  if (!token) return null;
  if (token.revokedAt) return null;
  if (token.expiresAt && token.expiresAt < new Date()) return null;

  const user = await prisma.adminUser.findUnique({ where: { id: token.userId } });
  if (!user || !user.isActive) return null;

  // Best-effort lastUsedAt update
  prisma.mcpToken.update({ where: { id: token.id }, data: { lastUsedAt: new Date() } }).catch(() => {});

  return {
    userId: user.id,
    userName: user.name,
    userEmail: user.email,
    role: user.role,
    tokenId: token.id,
    scopes: token.scopes.split(",").map((s) => s.trim()).filter(Boolean),
    office: user.office ?? null,
    scopedDepartments: user.scopedDepartments ?? null,
  };
}

export function extractBearer(req: Request): string | null {
  const h = req.headers.get("authorization") ?? req.headers.get("Authorization");
  if (!h) return null;
  const m = h.match(/^Bearer\s+(.+)$/i);
  return m ? m[1].trim() : null;
}

```