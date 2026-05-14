---
type: source
source_type: laptop
title: page
slug: page-43
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/success/page.tsx
original_size: 1808
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# page

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/success/page.tsx` on 2026-05-14._

```tsx
import Link from 'next/link';
import { CheckCircle2, Mail, ArrowRight } from 'lucide-react';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

export default function SuccessPage() {
  return (
    <main className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex-grow flex items-center justify-center py-20 px-4">
        <div className="max-w-md w-full text-center p-8 rounded-3xl bg-white border border-border shadow-2xl">
          <div className="w-20 h-20 bg-emerald-50 rounded-full flex items-center justify-center mx-auto mb-8 border border-emerald-100">
            <CheckCircle2 className="w-10 h-10 text-emerald-500" />
          </div>
          
          <h1 className="font-heading text-3xl font-bold mb-4">Payment Successful!</h1>
          <p className="text-muted-foreground mb-8">
            Your Dubai property buyer leads are being prepared. You will receive an email with the CSV file attached within the next 2-5 minutes.
          </p>
          
          <div className="p-4 rounded-2xl bg-blue-50 border border-blue-100 flex items-start gap-3 text-left mb-8">
            <Mail className="w-5 h-5 text-primary flex-shrink-0 mt-0.5" />
            <p className="text-sm text-blue-900 leading-relaxed">
              Please check your spam folder if you don't see our email from <strong>no-reply@dubai-leads.com</strong>.
            </p>
          </div>
          
          <Link 
            href="/" 
            className="w-full py-4 bg-primary text-white rounded-xl font-bold hover:bg-blue-700 transition-all flex items-center justify-center gap-2"
          >
            Back to Home
            <ArrowRight className="w-5 h-5" />
          </Link>
        </div>
      </div>
      <Footer />
    </main>
  );
}

```