---
type: source
source_type: laptop
title: page
slug: page-49
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/admin/proposals/new/page.tsx
original_size: 10674
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# page

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/admin/proposals/new/page.tsx` on 2026-05-14._

```tsx
'use client';

import { useState, FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { ArrowLeft, Copy, Check, Loader2, AlertCircle } from 'lucide-react';

interface CreatedResult {
  slug: string;
  email: string;
  contactName: string;
  companyName: string;
  plainPassword: string;
}

export default function NewProposalPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [created, setCreated] = useState<CreatedResult | null>(null);
  const [copiedField, setCopiedField] = useState<string | null>(null);

  function copy(text: string, field: string) {
    navigator.clipboard.writeText(text);
    setCopiedField(field);
    setTimeout(() => setCopiedField(null), 2000);
  }

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError('');
    setLoading(true);

    const formData = new FormData(e.currentTarget);
    const body = Object.fromEntries(
      [...formData.entries()].map(([k, v]) => [k, v.toString().trim()])
    );

    try {
      const res = await fetch('/api/admin/proposals', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.error ?? 'Failed to create proposal');
        return;
      }

      setCreated({
        slug: data.client.slug,
        email: data.client.email,
        contactName: data.client.contactName,
        companyName: data.client.companyName,
        plainPassword: data.plainPassword,
      });
    } catch {
      setError('Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  }

  if (created) {
    const loginUrl = `${typeof window !== 'undefined' ? window.location.origin : ''}/proposals/login`;
    const proposalUrl = `${typeof window !== 'undefined' ? window.location.origin : ''}/proposals/${created.slug}`;

    return (
      <div className="min-h-screen bg-[#0a0e1a] text-white flex items-center justify-center px-4">
        <div className="w-full max-w-lg">
          <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-2xl p-6 mb-6">
            <h2 className="font-heading font-bold text-lg text-emerald-400 mb-1">Proposal Created</h2>
            <p className="text-sm text-slate-400">
              Share these credentials with {created.contactName} at {created.companyName}. The password is shown once and cannot be recovered.
            </p>
          </div>

          <div className="space-y-3">
            {[
              { label: 'Login URL', value: loginUrl, field: 'url' },
              { label: 'Email', value: created.email, field: 'email' },
              { label: 'Password (save now)', value: created.plainPassword, field: 'password', highlight: true },
              { label: 'Proposal URL', value: proposalUrl, field: 'proposal' },
            ].map(({ label, value, field, highlight }) => (
              <div
                key={field}
                className={`flex items-center justify-between gap-4 p-4 rounded-xl border ${
                  highlight
                    ? 'bg-amber-500/10 border-amber-500/30'
                    : 'bg-white/3 border-white/8'
                }`}
              >
                <div className="flex-1 min-w-0">
                  <p className={`text-[10px] font-bold uppercase tracking-widest mb-0.5 ${highlight ? 'text-amber-400' : 'text-slate-500'}`}>
                    {label}
                  </p>
                  <p className={`text-sm font-mono truncate ${highlight ? 'text-amber-200' : 'text-slate-200'}`}>{value}</p>
                </div>
                <button
                  onClick={() => copy(value, field)}
                  className={`flex-shrink-0 flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                    highlight
                      ? 'bg-amber-500/20 hover:bg-amber-500/30 text-amber-300'
                      : 'bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white'
                  }`}
                >
                  {copiedField === field ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
            ))}
          </div>

          <div className="mt-6 flex gap-3">
            <Link
              href="/admin/proposals"
              className="flex-1 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-sm text-center transition-all"
            >
              Back to Dashboard
            </Link>
            <button
              onClick={() => setCreated(null)}
              className="flex-1 py-3 rounded-xl bg-white/5 hover:bg-white/10 text-slate-300 hover:text-white font-semibold text-sm transition-all"
            >
              Create Another
            </button>
          </div>
        </div>
      </div>
    );
  }

  const fieldClass =
    'w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder:text-slate-500 focus:outline-none focus:border-blue-500/60 transition-all text-sm';
  const labelClass = 'block text-xs font-semibold text-slate-400 mb-1.5 uppercase tracking-wider';

  return (
    <div className="min-h-screen bg-[#0a0e1a] text-white">
      <header className="border-b border-white/5 px-6 py-4 flex items-center gap-4">
        <Link
          href="/admin/proposals"
          className="text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="font-heading text-lg font-bold">New Proposal</h1>
          <p className="text-xs text-slate-500">Create client access and proposal record</p>
        </div>
      </header>

      <main className="p-6 max-w-2xl mx-auto">
        {error && (
          <div className="mb-6 flex items-center gap-2 text-red-400 bg-red-500/10 border border-red-500/20 rounded-xl px-4 py-3 text-sm">
            <AlertCircle className="w-4 h-4 flex-shrink-0" />
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Client info */}
          <section>
            <h2 className="font-heading font-bold text-base mb-4 text-slate-200">Client Information</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className={labelClass}>Company Name *</label>
                <input name="companyName" required placeholder="Noorzad Properties" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Contact Name *</label>
                <input name="contactName" required placeholder="Nikhil Masand" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Email *</label>
                <input name="email" type="email" required placeholder="marketing@company.ae" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Role / Title</label>
                <input name="role" placeholder="Marketing Manager" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Phone</label>
                <input name="phone" placeholder="+971 52 178 4598" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Website</label>
                <input name="website" placeholder="www.company.ae" className={fieldClass} />
              </div>
              <div className="sm:col-span-2">
                <label className={labelClass}>Office Address</label>
                <input name="officeAddress" placeholder="B-801 The Opus Tower, Business Bay" className={fieldClass} />
              </div>
            </div>
          </section>

          {/* Proposal details */}
          <section>
            <h2 className="font-heading font-bold text-base mb-4 text-slate-200">Proposal Details</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className={labelClass}>Lead Volume</label>
                <input name="packageVolume" type="number" placeholder="300" className={fieldClass} />
              </div>
              <div>
                <label className={labelClass}>Meeting Date</label>
                <input name="meetingDate" type="date" className={fieldClass} />
              </div>
              <div className="sm:col-span-2">
                <label className={labelClass}>Pricing Display</label>
                <input
                  name="pricingDisplay"
                  placeholder="e.g. Custom Enterprise — contact for pricing"
                  className={fieldClass}
                />
              </div>
              <div className="sm:col-span-2">
                <label className={labelClass}>Pricing Notes (internal)</label>
                <textarea
                  name="pricingNotes"
                  rows={3}
                  placeholder="Volume pricing at X AED/lead, negotiated discount..."
                  className={`${fieldClass} resize-none`}
                />
              </div>
              <div className="sm:col-span-2">
                <label className={labelClass}>Discovery Notes</label>
                <textarea
                  name="discoveryNotes"
                  rows={3}
                  placeholder="Key points from the discovery call..."
                  className={`${fieldClass} resize-none`}
                />
              </div>
              <div className="sm:col-span-2">
                <label className={labelClass}>Internal Notes</label>
                <textarea
                  name="notes"
                  rows={2}
                  placeholder="Internal notes about this client..."
                  className={`${fieldClass} resize-none`}
                />
              </div>
            </div>
          </section>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3.5 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:opacity-40 disabled:cursor-not-allowed text-white font-bold text-sm transition-all flex items-center justify-center gap-2"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : 'Create Proposal & Generate Credentials'}
          </button>
        </form>
      </main>
    </div>
  );
}

```