---
type: source
source_type: laptop
title: page
slug: page-2
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/oauth/authorize/page.tsx
original_size: 4788
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/oauth/authorize/page.tsx` on 2026-05-14._

```tsx
import Image from "next/image";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { redirect } from "next/navigation";
import { ConsentForm } from "./ConsentForm";

export const dynamic = "force-dynamic";

/**
 * OAuth 2.1 Authorization Endpoint (GET renders consent, POST submits).
 * Enforces PKCE (S256) per MCP spec.
 */
export default async function AuthorizePage({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  const params = await searchParams;
  const responseType = (params.response_type as string) || "";
  const clientId = (params.client_id as string) || "";
  const redirectUri = (params.redirect_uri as string) || "";
  const codeChallenge = (params.code_challenge as string) || "";
  const codeChallengeMethod = (params.code_challenge_method as string) || "";
  const state = (params.state as string) || "";
  const scope = (params.scope as string) || "read,write";

  if (responseType !== "code") return <AuthError title="Unsupported response_type" detail={responseType || "(missing)"} />;
  if (!clientId) return <AuthError title="Missing client_id" />;
  if (!redirectUri) return <AuthError title="Missing redirect_uri" />;
  if (!codeChallenge) return <AuthError title="Missing code_challenge (PKCE required)" />;
  if (codeChallengeMethod !== "S256") return <AuthError title="code_challenge_method must be S256" />;

  const client = await prisma.oAuthClient.findUnique({ where: { clientId } });
  if (!client) return <AuthError title="Unknown client_id" detail={clientId} />;

  const allowedRedirects: string[] = JSON.parse(client.redirectUris);
  if (!allowedRedirects.includes(redirectUri)) {
    return <AuthError title="redirect_uri not registered for this client" detail={redirectUri} />;
  }

  const session = await getSession();
  if (!session) {
    // Preserve the full authorize URL so we come back after login
    const currentUrl = new URL("/oauth/authorize", process.env.PUBLIC_APP_URL ?? "http://localhost:3000");
    for (const [k, v] of Object.entries(params)) {
      if (typeof v === "string") currentUrl.searchParams.set(k, v);
    }
    redirect(`/admin/login?next=${encodeURIComponent(currentUrl.pathname + currentUrl.search)}`);
  }

  return (
    <div className="min-h-screen bg-zinc-50 py-12 dark:bg-zinc-950">
      <div className="mx-auto max-w-lg px-4 sm:px-6">
        <div className="mb-6 flex flex-col items-center text-center">
          <Image src="/janusd-icon-200.png" alt="Janus Digital" width={56} height={56} className="mb-3" />
          <h1 className="text-xl font-semibold tracking-tight">Authorize Access</h1>
        </div>

        <div className="rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
          <p className="text-sm text-zinc-700 dark:text-zinc-300">
            <strong>{client.clientName}</strong> is requesting access to Assessify on behalf of{" "}
            <strong>{session.name}</strong> ({session.email}).
          </p>

          <div className="mt-4 rounded-lg border border-zinc-200 bg-zinc-50 p-3 text-xs dark:border-zinc-800 dark:bg-zinc-950">
            <p className="font-semibold text-zinc-700 dark:text-zinc-300">This app will be able to:</p>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-zinc-600 dark:text-zinc-400">
              <li>Search your employees, job roles, assessments, questions, and candidates</li>
              <li>Create job roles, assessments, and candidate invites (as drafts)</li>
              <li>All actions logged to the audit log under your admin account</li>
            </ul>
          </div>

          <p className="mt-4 text-xs text-zinc-500">
            Redirect after approval:{" "}
            <code className="rounded bg-zinc-100 px-1.5 py-0.5 dark:bg-zinc-800">{redirectUri}</code>
          </p>

          <ConsentForm
            clientId={clientId}
            redirectUri={redirectUri}
            codeChallenge={codeChallenge}
            codeChallengeMethod={codeChallengeMethod}
            state={state}
            scope={scope}
          />
        </div>

        <p className="mt-6 text-center text-xs text-muted-foreground">
          Janus Digital · Assessify OAuth Consent · You can revoke this access anytime from /admin/settings
        </p>
      </div>
    </div>
  );
}

function AuthError({ title, detail }: { title: string; detail?: string }) {
  return (
    <div className="mx-auto max-w-md p-10 text-center">
      <h1 className="text-lg font-semibold text-red-600">Authorization error</h1>
      <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">{title}</p>
      {detail && <p className="mt-1 font-mono text-xs text-zinc-500">{detail}</p>}
    </div>
  );
}

```