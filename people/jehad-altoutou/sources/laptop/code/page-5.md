---
type: source
source_type: laptop
title: page
slug: page-5
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/settings/page.tsx
original_size: 30287
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/settings/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import McpTokensCard from "./McpTokensCard";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Plus,
  Trash2,
  Copy,
  Check,
  Loader2,
  AlertTriangle,
  Webhook,
  Eye,
  EyeOff,
  Users,
  Send,
  ShieldCheck,
  UserX,
  UserCheck,
  KeyRound,
  RefreshCw,
  X,
} from "lucide-react";

const ALL_EVENTS = [
  { value: "assessment.completed", label: "Assessment Completed", description: "Fires when a candidate finishes an assessment" },
  { value: "form.submitted", label: "Form Submitted", description: "Fires when an employee submits an HR form" },
  { value: "assessment.started", label: "Assessment Started", description: "Fires when a candidate begins an assessment" },
];

interface WebhookEndpoint {
  id: string;
  url: string;
  secret: string | null;
  events: string;
  isActive: boolean;
  createdAt: string;
  _count: { deliveries: number };
}

interface AdminUser {
  id: string;
  name: string;
  email: string;
  role: string;
  isActive: boolean;
  createdAt: string;
}

export default function SettingsPage() {
  const [endpoints, setEndpoints] = useState<WebhookEndpoint[]>([]);
  const [adminUsers, setAdminUsers] = useState<AdminUser[]>([]);
  const [currentUser, setCurrentUser] = useState<{ id: string; role: string } | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [url, setUrl] = useState("");
  const [selectedEvents, setSelectedEvents] = useState<Set<string>>(new Set());
  const [isCreating, setIsCreating] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [visibleSecrets, setVisibleSecrets] = useState<Set<string>>(new Set());
  const [deleteTarget, setDeleteTarget] = useState<WebhookEndpoint | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const loadUsers = () => {
    fetch("/api/admin/users")
      .then((r) => r.json())
      .then((d) => setAdminUsers(d.users ?? []));
  };

  useEffect(() => {
    fetch("/api/admin/webhooks")
      .then((r) => r.json())
      .then((d) => setEndpoints(d.endpoints ?? []));
    loadUsers();
    fetch("/api/admin/auth")
      .then((r) => r.json())
      .then((d) => { if (d.user) setCurrentUser({ id: d.user.id, role: d.user.role }); })
      .catch(() => {});
  }, []);

  const handleCreate = async () => {
    if (!url.trim() || selectedEvents.size === 0) return;
    setIsCreating(true);
    setError(null);

    try {
      const res = await fetch("/api/admin/webhooks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url.trim(), events: Array.from(selectedEvents) }),
      });
      const data = await res.json();
      if (!res.ok) { setError(data.error); setIsCreating(false); return; }

      // Refresh
      const refreshed = await fetch("/api/admin/webhooks").then((r) => r.json());
      setEndpoints(refreshed.endpoints ?? []);
      setUrl("");
      setSelectedEvents(new Set());
      setShowForm(false);
    } catch { setError("Network error"); }
    setIsCreating(false);
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    await fetch(`/api/admin/webhooks?id=${deleteTarget.id}`, { method: "DELETE" }).catch(() => {});
    setEndpoints((prev) => prev.filter((e) => e.id !== deleteTarget.id));
    setIsDeleting(false);
    setDeleteTarget(null);
  };

  const copySecret = (secret: string, id: string) => {
    navigator.clipboard.writeText(secret);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const toggleSecret = (id: string) => {
    setVisibleSecrets((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id); else next.add(id);
      return next;
    });
  };

  const toggleEvent = (event: string) => {
    setSelectedEvents((prev) => {
      const next = new Set(prev);
      if (next.has(event)) next.delete(event); else next.add(event);
      return next;
    });
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Settings</h1>
        <p className="text-sm text-muted-foreground">
          Platform configuration and integrations.
        </p>
      </div>

      {/* Webhook Endpoints */}
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Webhook Endpoints</CardTitle>
              <CardDescription>
                Receive real-time notifications when events happen on the platform.
              </CardDescription>
            </div>
            <Button onClick={() => setShowForm(!showForm)} className="gap-2">
              <Plus className="size-4" /> Add Endpoint
            </Button>
          </div>
        </CardHeader>
        <CardContent>
          {/* Create form */}
          {showForm && (
            <div className="mb-6 rounded-xl border border-zinc-200 bg-zinc-50 p-5 dark:border-zinc-800 dark:bg-zinc-800/30">
              <h4 className="mb-4 text-sm font-semibold">New Webhook Endpoint</h4>
              <div className="space-y-4">
                <div>
                  <Label>Endpoint URL</Label>
                  <Input
                    placeholder="https://your-n8n-instance.com/webhook/..."
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    className="mt-1.5"
                  />
                  <p className="mt-1 text-[10px] text-muted-foreground">
                    The URL that will receive POST requests with event payloads.
                  </p>
                </div>

                <div>
                  <Label>Events to subscribe</Label>
                  <div className="mt-2 space-y-2">
                    {ALL_EVENTS.map((evt) => (
                      <button
                        key={evt.value}
                        onClick={() => toggleEvent(evt.value)}
                        className={`flex w-full items-center gap-3 rounded-lg border-2 p-3 text-left transition-all ${
                          selectedEvents.has(evt.value)
                            ? "border-primary bg-primary/5"
                            : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-700"
                        }`}
                      >
                        <div
                          className={`flex h-5 w-5 items-center justify-center rounded-md border-2 transition-all ${
                            selectedEvents.has(evt.value)
                              ? "border-primary bg-primary"
                              : "border-zinc-300 dark:border-zinc-600"
                          }`}
                        >
                          {selectedEvents.has(evt.value) && (
                            <Check className="size-3 text-white" />
                          )}
                        </div>
                        <div>
                          <p className="text-sm font-medium">{evt.label}</p>
                          <p className="text-[10px] text-muted-foreground">{evt.description}</p>
                        </div>
                      </button>
                    ))}
                  </div>
                </div>

                {error && <p className="text-xs text-red-600">{error}</p>}

                <div className="flex gap-3">
                  <Button onClick={handleCreate} disabled={!url.trim() || selectedEvents.size === 0 || isCreating} className="gap-2">
                    {isCreating ? <Loader2 className="size-4 animate-spin" /> : <Webhook className="size-4" />}
                    Create Endpoint
                  </Button>
                  <Button variant="outline" onClick={() => { setShowForm(false); setError(null); }}>Cancel</Button>
                </div>
              </div>
            </div>
          )}

          {/* Endpoints list */}
          {endpoints.length === 0 && !showForm ? (
            <div className="flex flex-col items-center py-8">
              <Webhook className="mb-3 size-10 text-muted-foreground" />
              <p className="text-sm text-muted-foreground">No webhook endpoints configured.</p>
              <p className="text-xs text-muted-foreground">Click &quot;Add Endpoint&quot; to start receiving events.</p>
            </div>
          ) : (
            <div className="space-y-3">
              {endpoints.map((ep) => {
                const events = (() => { try { return JSON.parse(ep.events) as string[]; } catch { return []; } })();
                const secretVisible = visibleSecrets.has(ep.id);

                return (
                  <div key={ep.id} className="rounded-xl border border-zinc-200 p-4 dark:border-zinc-800">
                    <div className="flex items-start justify-between">
                      <div className="min-w-0 flex-1">
                        <div className="flex items-center gap-2">
                          <code className="truncate text-sm font-medium">{ep.url}</code>
                          <span className={`inline-block h-2 w-2 rounded-full ${ep.isActive ? "bg-green-500" : "bg-zinc-300"}`} />
                        </div>
                        <div className="mt-2 flex flex-wrap gap-1.5">
                          {events.map((evt) => (
                            <Badge key={evt} variant="secondary">{evt}</Badge>
                          ))}
                        </div>
                      </div>
                      <button
                        onClick={() => setDeleteTarget(ep)}
                        className="ml-2 rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                      >
                        <Trash2 className="size-4" />
                      </button>
                    </div>

                    {/* Secret */}
                    {ep.secret && (
                      <div className="mt-3 flex items-center gap-2">
                        <span className="text-[10px] text-muted-foreground">Signing secret:</span>
                        <code className="rounded bg-zinc-100 px-2 py-0.5 font-mono text-[10px] dark:bg-zinc-800">
                          {secretVisible ? ep.secret : "whsec_••••••••••••••••"}
                        </code>
                        <button onClick={() => toggleSecret(ep.id)} className="text-muted-foreground hover:text-foreground">
                          {secretVisible ? <EyeOff className="size-3" /> : <Eye className="size-3" />}
                        </button>
                        <button onClick={() => copySecret(ep.secret!, ep.id)} className="text-muted-foreground hover:text-foreground">
                          {copiedId === ep.id ? <Check className="size-3 text-green-500" /> : <Copy className="size-3" />}
                        </button>
                      </div>
                    )}

                    <p className="mt-2 text-[10px] text-muted-foreground">
                      {ep._count.deliveries} deliveries &middot; Created {new Date(ep.createdAt).toLocaleDateString()}
                    </p>
                  </div>
                );
              })}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Team Members */}
      <TeamMembersCard
        users={adminUsers}
        currentUser={currentUser}
        onRefresh={loadUsers}
      />

      {/* MCP Tokens (Claude Custom Connector) */}
      <McpTokensCard currentUser={currentUser} />

      {/* Webhook Delete confirmation */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Webhook</h3>
                <p className="text-xs text-muted-foreground">This will also delete all delivery logs.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Are you sure you want to delete the webhook endpoint for{" "}
              <strong className="text-foreground">{deleteTarget.url}</strong>?
            </p>
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteTarget(null)} disabled={isDeleting}>Cancel</Button>
              <Button variant="destructive" onClick={handleDelete} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// ─── Team Members Card ───────────────────────────────────────

function TeamMembersCard({
  users, currentUser, onRefresh,
}: {
  users: AdminUser[];
  currentUser: { id: string; role: string } | null;
  onRefresh: () => void;
}) {
  const isAdmin = currentUser?.role === "admin";
  const [showInvite, setShowInvite] = useState(false);
  const [inviteEmail, setInviteEmail] = useState("");
  const [inviteRole, setInviteRole] = useState("user");
  const [inviting, setInviting] = useState(false);
  const [inviteError, setInviteError] = useState<string | null>(null);
  const [inviteSuccess, setInviteSuccess] = useState<string | null>(null);

  const [resetTarget, setResetTarget] = useState<AdminUser | null>(null);
  const [resetPassword, setResetPassword] = useState("");
  const [resetting, setResetting] = useState(false);
  const [resetError, setResetError] = useState<string | null>(null);

  const [deleteTarget, setDeleteTarget] = useState<AdminUser | null>(null);
  const [deleting, setDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  const [actionLoading, setActionLoading] = useState<string | null>(null);

  const handleInvite = async () => {
    if (!inviteEmail.trim()) return;
    setInviting(true);
    setInviteError(null);
    setInviteSuccess(null);
    try {
      const res = await fetch("/api/admin/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: inviteEmail.trim(), role: inviteRole }),
      });
      const data = await res.json();
      if (!res.ok) { setInviteError(data.error); setInviting(false); return; }
      setInviteSuccess(data.emailSent ? "Invite sent!" : "Invite created (email delivery may have failed). Share the link manually.");
      setInviteEmail("");
      onRefresh();
    } catch { setInviteError("Network error"); }
    setInviting(false);
  };

  const handleToggleActive = async (user: AdminUser) => {
    setActionLoading(user.id);
    await fetch(`/api/admin/users/${user.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ isActive: !user.isActive }),
    });
    onRefresh();
    setActionLoading(null);
  };

  const handleChangeRole = async (user: AdminUser, newRole: string) => {
    setActionLoading(user.id);
    await fetch(`/api/admin/users/${user.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role: newRole }),
    });
    onRefresh();
    setActionLoading(null);
  };

  const handleResetPassword = async () => {
    if (!resetTarget || !resetPassword) return;
    setResetting(true);
    setResetError(null);
    try {
      const res = await fetch(`/api/admin/users/${resetTarget.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ newPassword: resetPassword }),
      });
      const data = await res.json();
      if (!res.ok) { setResetError(data.error); setResetting(false); return; }
      setResetTarget(null);
      setResetPassword("");
    } catch { setResetError("Network error"); }
    setResetting(false);
  };

  const handleResendInvite = async (user: AdminUser) => {
    setActionLoading(user.id);
    await fetch(`/api/admin/users/${user.id}/resend`, { method: "POST" });
    setActionLoading(null);
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setDeleting(true);
    setDeleteError(null);
    try {
      const res = await fetch(`/api/admin/users/${deleteTarget.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) { setDeleteError(data.error); setDeleting(false); return; }
      setDeleteTarget(null);
      onRefresh();
    } catch { setDeleteError("Network error"); }
    setDeleting(false);
  };

  const getStatus = (user: AdminUser): { label: string; color: string } => {
    if (user.isActive) return { label: "Active", color: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300" };
    if (user.name === "Pending") return { label: "Pending", color: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300" };
    return { label: "Deactivated", color: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300" };
  };

  return (
    <>
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Team Members</CardTitle>
              <CardDescription>Manage who has access to the admin panel.</CardDescription>
            </div>
            {isAdmin && (
              <Button onClick={() => { setShowInvite(!showInvite); setInviteError(null); setInviteSuccess(null); }} className="gap-2">
                <Plus className="size-4" /> Invite Member
              </Button>
            )}
          </div>
        </CardHeader>
        <CardContent>
          {/* Invite form */}
          {showInvite && isAdmin && (
            <div className="mb-6 rounded-xl border border-zinc-200 bg-zinc-50 p-5 dark:border-zinc-800 dark:bg-zinc-800/30">
              <h4 className="mb-4 text-sm font-semibold">Invite New Member</h4>
              <div className="space-y-3">
                <div>
                  <Label>Work Email</Label>
                  <Input
                    type="email"
                    placeholder="colleague@company.com"
                    value={inviteEmail}
                    onChange={(e) => setInviteEmail(e.target.value)}
                    className="mt-1.5"
                  />
                </div>
                <div>
                  <Label>Role</Label>
                  <div className="mt-1.5">
                    <Select value={inviteRole} onValueChange={(v) => setInviteRole(v ?? "user")}>
                      <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
                      <SelectContent>
                        <SelectItem value="admin">Admin — Full access, can manage users</SelectItem>
                        <SelectItem value="user">User — View and operate, no user management</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>
                {inviteError && <p className="text-xs text-red-600">{inviteError}</p>}
                {inviteSuccess && <p className="text-xs text-emerald-600">{inviteSuccess}</p>}
                <div className="flex gap-2">
                  <Button onClick={handleInvite} disabled={!inviteEmail.trim() || inviting} className="gap-2">
                    {inviting ? <Loader2 className="size-4 animate-spin" /> : <Send className="size-4" />}
                    Send Invite
                  </Button>
                  <Button variant="outline" onClick={() => setShowInvite(false)}>Cancel</Button>
                </div>
              </div>
            </div>
          )}

          {/* User list */}
          {users.length === 0 ? (
            <div className="flex flex-col items-center py-8">
              <Users className="size-10 text-muted-foreground" />
              <p className="mt-3 text-sm text-muted-foreground">No team members yet.</p>
            </div>
          ) : (
            <div className="space-y-2">
              {users.map((user) => {
                const status = getStatus(user);
                const isSelf = currentUser?.id === user.id;
                const isPending = user.name === "Pending" && !user.isActive;
                const isLoading = actionLoading === user.id;

                return (
                  <div key={user.id} className="flex items-center gap-4 rounded-xl border border-zinc-100 p-4 dark:border-zinc-800">
                    {/* Avatar circle */}
                    <div className="flex size-9 flex-shrink-0 items-center justify-center rounded-full bg-zinc-100 text-sm font-semibold text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400">
                      {user.name === "Pending" ? "?" : user.name.charAt(0).toUpperCase()}
                    </div>
                    {/* Info */}
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2">
                        <p className="truncate text-sm font-medium">{user.name}</p>
                        <Badge variant={user.role === "admin" ? "default" : "outline"} className="text-[10px]">
                          {user.role === "admin" ? "Admin" : "User"}
                        </Badge>
                        <span className={`rounded-full px-1.5 py-0.5 text-[10px] font-medium ${status.color}`}>
                          {status.label}
                        </span>
                        {isSelf && <span className="text-[10px] text-muted-foreground">(you)</span>}
                      </div>
                      <p className="truncate text-xs text-muted-foreground">{user.email}</p>
                    </div>
                    {/* Actions (admin only, not self) */}
                    {isAdmin && !isSelf && (
                      <div className="flex items-center gap-1">
                        {isLoading ? (
                          <Loader2 className="size-4 animate-spin text-muted-foreground" />
                        ) : (
                          <>
                            {isPending && (
                              <button
                                onClick={() => handleResendInvite(user)}
                                title="Resend invite"
                                className="rounded-md p-1.5 text-zinc-400 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-blue-950"
                              >
                                <RefreshCw className="size-3.5" />
                              </button>
                            )}
                            {user.isActive && (
                              <>
                                <button
                                  onClick={() => handleChangeRole(user, user.role === "admin" ? "user" : "admin")}
                                  title={`Change to ${user.role === "admin" ? "User" : "Admin"}`}
                                  className="rounded-md p-1.5 text-zinc-400 hover:bg-zinc-100 hover:text-zinc-600 dark:hover:bg-zinc-800"
                                >
                                  <ShieldCheck className="size-3.5" />
                                </button>
                                <button
                                  onClick={() => { setResetTarget(user); setResetPassword(""); setResetError(null); }}
                                  title="Reset password"
                                  className="rounded-md p-1.5 text-zinc-400 hover:bg-amber-50 hover:text-amber-600 dark:hover:bg-amber-950"
                                >
                                  <KeyRound className="size-3.5" />
                                </button>
                              </>
                            )}
                            {user.isActive ? (
                              <button
                                onClick={() => handleToggleActive(user)}
                                title="Deactivate"
                                className="rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                              >
                                <UserX className="size-3.5" />
                              </button>
                            ) : !isPending ? (
                              <button
                                onClick={() => handleToggleActive(user)}
                                title="Reactivate"
                                className="rounded-md p-1.5 text-zinc-400 hover:bg-green-50 hover:text-green-600 dark:hover:bg-green-950"
                              >
                                <UserCheck className="size-3.5" />
                              </button>
                            ) : null}
                            <button
                              onClick={() => { setDeleteTarget(user); setDeleteError(null); }}
                              title="Delete"
                              className="rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                            >
                              <Trash2 className="size-3.5" />
                            </button>
                          </>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Reset password modal */}
      {resetTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={() => setResetTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="rounded-lg bg-amber-50 p-2 dark:bg-amber-950">
                  <KeyRound className="size-5 text-amber-600" />
                </div>
                <div>
                  <h3 className="text-sm font-semibold">Reset Password</h3>
                  <p className="text-xs text-muted-foreground">{resetTarget.name} ({resetTarget.email})</p>
                </div>
              </div>
              <button onClick={() => setResetTarget(null)} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
                <X className="size-4" />
              </button>
            </div>
            <div className="space-y-3">
              <div>
                <Label>New Password</Label>
                <Input
                  type="password"
                  placeholder="Minimum 8 characters"
                  value={resetPassword}
                  onChange={(e) => setResetPassword(e.target.value)}
                  className="mt-1.5"
                />
              </div>
              {resetError && <p className="text-xs text-red-600">{resetError}</p>}
              <div className="flex justify-end gap-3">
                <Button variant="outline" onClick={() => setResetTarget(null)} disabled={resetting}>Cancel</Button>
                <Button onClick={handleResetPassword} disabled={resetPassword.length < 8 || resetting} className="gap-2">
                  {resetting ? <Loader2 className="size-4 animate-spin" /> : <KeyRound className="size-4" />}
                  Reset
                </Button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Delete user modal */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete User</h3>
                <p className="text-xs text-muted-foreground">This action cannot be undone.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Delete <strong className="text-foreground">{deleteTarget.name}</strong> ({deleteTarget.email})?
            </p>
            {deleteError && <p className="mb-3 rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">{deleteError}</p>}
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteTarget(null)} disabled={deleting}>Cancel</Button>
              <Button variant="destructive" onClick={handleDelete} disabled={deleting} className="gap-2">
                {deleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

```