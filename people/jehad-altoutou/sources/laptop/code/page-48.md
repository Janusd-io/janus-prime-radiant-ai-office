---
type: source
source_type: laptop
title: page
slug: page-48
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/admin/proposals/page.tsx
original_size: 12304
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# page

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/admin/proposals/page.tsx` on 2026-05-14._

```tsx
'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  Plus, LogOut, RefreshCw, Copy, Check, ToggleLeft, ToggleRight,
  ExternalLink, Loader2, AlertCircle, Users
} from 'lucide-react';

interface ProposalClient {
  id: string;
  companyName: string;
  contactName: string;
  email: string;
  role: string | null;
  phone: string | null;
  slug: string;
  status: string;
  notes: string | null;
  meetingDate: string | null;
  createdAt: string;
  proposal: {
    packageVolume: number | null;
    pricingNotes: string | null;
    status: string;
  } | null;
}

export default function AdminDashboard() {
  const router = useRouter();
  const [clients, setClients] = useState<ProposalClient[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [resettingId, setResettingId] = useState<string | null>(null);
  const [newPassword, setNewPassword] = useState<{ id: string; password: string } | null>(null);
  const [togglingId, setTogglingId] = useState<string | null>(null);

  async function loadClients() {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/proposals');
      if (res.status === 401) { router.push('/admin/login'); return; }
      const data = await res.json();
      setClients(data);
    } catch {
      setError('Failed to load proposals');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { loadClients(); }, []);

  async function logout() {
    await fetch('/api/admin/auth/logout', { method: 'POST' });
    router.push('/admin/login');
  }

  async function resetPassword(id: string) {
    setResettingId(id);
    setNewPassword(null);
    try {
      const res = await fetch(`/api/admin/proposals/${id}/reset-password`, { method: 'POST' });
      const data = await res.json();
      if (res.ok) setNewPassword({ id, password: data.plainPassword });
    } finally {
      setResettingId(null);
    }
  }

  async function toggleStatus(client: ProposalClient) {
    setTogglingId(client.id);
    try {
      await fetch(`/api/admin/proposals/${client.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: client.status === 'active' ? 'inactive' : 'active' }),
      });
      setClients((prev) =>
        prev.map((c) =>
          c.id === client.id
            ? { ...c, status: c.status === 'active' ? 'inactive' : 'active' }
            : c
        )
      );
    } finally {
      setTogglingId(null);
    }
  }

  function copyToClipboard(text: string, id: string) {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  }

  return (
    <div className="min-h-screen bg-[#0a0e1a] text-white">
      {/* Header */}
      <header className="border-b border-white/5 px-6 py-4 flex items-center justify-between">
        <div>
          <h1 className="font-heading text-lg font-bold">Proposals Admin</h1>
          <p className="text-xs text-slate-500">Dubai Property Leads — Internal Tool</p>
        </div>
        <div className="flex items-center gap-3">
          <Link
            href="/admin/proposals/new"
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-sm font-semibold transition-all"
          >
            <Plus className="w-4 h-4" />
            New Proposal
          </Link>
          <button
            onClick={logout}
            className="flex items-center gap-2 px-4 py-2 bg-white/5 hover:bg-white/10 rounded-xl text-sm font-semibold transition-all text-slate-400 hover:text-white"
          >
            <LogOut className="w-4 h-4" />
            Logout
          </button>
        </div>
      </header>

      <main className="p-6 max-w-6xl mx-auto">
        {error && (
          <div className="mb-6 flex items-center gap-2 text-red-400 bg-red-500/10 border border-red-500/20 rounded-xl px-4 py-3 text-sm">
            <AlertCircle className="w-4 h-4 flex-shrink-0" />
            {error}
          </div>
        )}

        {loading ? (
          <div className="flex items-center justify-center py-24">
            <Loader2 className="w-8 h-8 text-blue-400 animate-spin" />
          </div>
        ) : clients.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-24 text-center">
            <Users className="w-12 h-12 text-slate-600 mb-4" />
            <p className="text-slate-400 font-medium">No proposals yet</p>
            <p className="text-slate-600 text-sm mt-1">Create the first client proposal to get started.</p>
            <Link
              href="/admin/proposals/new"
              className="mt-6 flex items-center gap-2 px-5 py-2.5 bg-blue-600 hover:bg-blue-500 rounded-xl text-sm font-semibold transition-all"
            >
              <Plus className="w-4 h-4" />
              Create First Proposal
            </Link>
          </div>
        ) : (
          <div className="space-y-4">
            {clients.map((client) => (
              <div
                key={client.id}
                className="bg-white/3 border border-white/8 rounded-2xl p-6 hover:border-white/15 transition-all"
              >
                <div className="flex items-start justify-between gap-4 flex-wrap">
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-3 mb-1 flex-wrap">
                      <h2 className="font-heading font-bold text-lg leading-tight">{client.companyName}</h2>
                      <span
                        className={`text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded-full ${
                          client.status === 'active'
                            ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/20'
                            : 'bg-slate-500/15 text-slate-500 border border-slate-500/20'
                        }`}
                      >
                        {client.status}
                      </span>
                      {client.proposal && (
                        <span
                          className={`text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded-full ${
                            client.proposal.status === 'published'
                              ? 'bg-blue-500/15 text-blue-400 border border-blue-500/20'
                              : 'bg-amber-500/15 text-amber-400 border border-amber-500/20'
                          }`}
                        >
                          {client.proposal.status}
                        </span>
                      )}
                    </div>

                    <p className="text-sm text-slate-300">
                      {client.contactName}
                      {client.role && <span className="text-slate-500"> · {client.role}</span>}
                    </p>
                    <p className="text-sm text-slate-500">{client.email}</p>
                    {client.phone && <p className="text-sm text-slate-500">{client.phone}</p>}

                    <div className="mt-3 flex items-center gap-4 text-xs text-slate-500 flex-wrap">
                      {client.proposal?.packageVolume && (
                        <span className="text-slate-400 font-medium">
                          {client.proposal.packageVolume.toLocaleString()} leads
                        </span>
                      )}
                      <span>
                        Slug: <code className="text-slate-300 font-mono">{client.slug}</code>
                      </span>
                      {client.meetingDate && (
                        <span>Meeting: {new Date(client.meetingDate).toLocaleDateString()}</span>
                      )}
                      <span>Created: {new Date(client.createdAt).toLocaleDateString()}</span>
                    </div>
                  </div>

                  <div className="flex items-center gap-2 flex-shrink-0 flex-wrap">
                    <a
                      href={`/proposals/${client.slug}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/5 hover:bg-white/10 text-xs font-medium text-slate-300 hover:text-white transition-all"
                    >
                      <ExternalLink className="w-3.5 h-3.5" />
                      View
                    </a>

                    <button
                      onClick={() => copyToClipboard(client.slug, `slug-${client.id}`)}
                      className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/5 hover:bg-white/10 text-xs font-medium text-slate-300 hover:text-white transition-all"
                      title="Copy slug"
                    >
                      {copiedId === `slug-${client.id}` ? (
                        <Check className="w-3.5 h-3.5 text-emerald-400" />
                      ) : (
                        <Copy className="w-3.5 h-3.5" />
                      )}
                      Slug
                    </button>

                    <button
                      onClick={() => resetPassword(client.id)}
                      disabled={resettingId === client.id}
                      className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/5 hover:bg-amber-500/10 text-xs font-medium text-slate-300 hover:text-amber-400 transition-all disabled:opacity-40"
                      title="Reset password"
                    >
                      {resettingId === client.id ? (
                        <Loader2 className="w-3.5 h-3.5 animate-spin" />
                      ) : (
                        <RefreshCw className="w-3.5 h-3.5" />
                      )}
                      Reset PW
                    </button>

                    <button
                      onClick={() => toggleStatus(client)}
                      disabled={togglingId === client.id}
                      className="flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/5 hover:bg-white/10 text-xs font-medium text-slate-300 hover:text-white transition-all disabled:opacity-40"
                      title="Toggle active/inactive"
                    >
                      {togglingId === client.id ? (
                        <Loader2 className="w-3.5 h-3.5 animate-spin" />
                      ) : client.status === 'active' ? (
                        <ToggleRight className="w-3.5 h-3.5 text-emerald-400" />
                      ) : (
                        <ToggleLeft className="w-3.5 h-3.5" />
                      )}
                      {client.status === 'active' ? 'Deactivate' : 'Activate'}
                    </button>
                  </div>
                </div>

                {/* New password revealed after reset */}
                {newPassword?.id === client.id && (
                  <div className="mt-4 p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-between gap-4">
                    <div>
                      <p className="text-xs text-amber-400 font-semibold mb-0.5">New password (save this now — shown once)</p>
                      <code className="text-amber-300 font-mono text-sm">{newPassword.password}</code>
                    </div>
                    <button
                      onClick={() => copyToClipboard(newPassword.password, `pw-${client.id}`)}
                      className="flex-shrink-0 flex items-center gap-1 px-3 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-medium transition-all"
                    >
                      {copiedId === `pw-${client.id}` ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                      Copy
                    </button>
                  </div>
                )}

                {client.notes && (
                  <p className="mt-3 text-xs text-slate-500 border-t border-white/5 pt-3">{client.notes}</p>
                )}
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

```