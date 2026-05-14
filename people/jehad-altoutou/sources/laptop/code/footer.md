---
type: source
source_type: laptop
title: Footer
slug: footer
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/Footer.tsx
original_size: 5954
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Footer

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/Footer.tsx` on 2026-05-14._

```tsx
'use client';

import Link from 'next/link';
import { useState } from 'react';
import LegalModal from './LegalModal';
import { PrivacyPolicy, TermsOfService, RefundPolicy } from './legal/PolicyContent';

export default function Footer() {
  const [modalType, setModalType] = useState<'privacy' | 'tos' | 'refund' | null>(null);

  const policies = {
    privacy: { title: 'Privacy Policy', content: <PrivacyPolicy /> },
    tos: { title: 'Terms of Service', content: <TermsOfService /> },
    refund: { title: 'Refund & Replacement Policy', content: <RefundPolicy /> }
  };

  return (
    <footer className="bg-white border-t border-border py-16">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-5 gap-12 mb-16">
          <div className="col-span-1 md:col-span-2">
            <Link href="/" className="flex items-center gap-3 mb-6">
              <img 
                src="/logo.png" 
                alt="Dubai Leads" 
                className="h-10 w-auto object-contain brightness-110"
              />
              <span className="text-2xl font-heading font-black tracking-tighter text-foreground uppercase">
                DUBAI<span className="text-primary italic">LEADS</span>
              </span>
            </Link>
            <p className="text-muted-foreground text-sm max-w-sm leading-relaxed">
              The premier marketplace for verified Dubai real estate buyer enquiries. We bridge the gap between high-intent investors and professional agents.
            </p>
          </div>
          
          <div>
            <h4 className="font-bold text-sm uppercase tracking-widest mb-6">Solutions</h4>
            <ul className="space-y-4 text-sm text-muted-foreground">
              <li><Link href="/real-estate-api" className="hover:text-primary transition-colors font-semibold text-foreground">Dubai Real Estate API</Link></li>
              <li><Link href="/dubai-real-estate-leads" className="hover:text-primary transition-colors">Dubai Real Estate Leads</Link></li>
              <li><Link href="/property-buyer-leads-dubai" className="hover:text-primary transition-colors">Property Buyer Leads</Link></li>
              <li><Link href="/off-plan-leads-dubai" className="hover:text-primary transition-colors">Off-Plan Leads</Link></li>
              <li><Link href="/dubai-investor-leads" className="hover:text-primary transition-colors">Dubai Investor Leads</Link></li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-bold text-sm uppercase tracking-widest mb-6">Company</h4>
            <ul className="space-y-4 text-sm text-muted-foreground">
              <li><Link href="/about" className="hover:text-primary transition-colors">About Us</Link></li>
              <li><Link href="#how-it-works" className="hover:text-primary transition-colors">How It Works</Link></li>
              <li><Link href="#pricing" className="hover:text-primary transition-colors">Pricing</Link></li>
              <li>
                <button 
                  onClick={() => setModalType('tos')} 
                  className="hover:text-primary transition-colors"
                >
                  Terms of Service
                </button>
              </li>
              <li>
                <button 
                  onClick={() => setModalType('refund')} 
                  className="hover:text-primary transition-colors"
                >
                  Refund Policy
                </button>
              </li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-bold text-sm uppercase tracking-widest mb-6">Resources</h4>
            <ul className="space-y-4 text-sm text-muted-foreground">
              <li><Link href="/where-to-buy-dubai-property-leads" className="hover:text-primary transition-colors">Where to Buy Leads</Link></li>
              <li><Link href="/blog/how-real-estate-agents-get-leads-in-dubai" className="hover:text-primary transition-colors">How Agents Get Leads</Link></li>
              <li><Link href="/blog/cost-of-real-estate-leads-dubai" className="hover:text-primary transition-colors">Cost of Leads</Link></li>
              <li><Link href="/blog/off-plan-property-leads-guide" className="hover:text-primary transition-colors">Off-Plan Leads Guide</Link></li>
              <li><Link href="/blog/top-new-off-plan-projects-dubai-2026" className="hover:text-primary transition-colors">Top New UAE Projects 2026</Link></li>
              <li><Link href="/blog/best-lead-generation-for-dubai-brokers" className="hover:text-primary transition-colors">Best Lead Generation</Link></li>
            </ul>
          </div>
        </div>
        
        <div className="pt-8 border-t border-border flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex flex-col md:flex-row items-center gap-4">
            <p className="text-xs text-muted-foreground">
              © {new Date().getFullYear()} Dubai Property Leads. All rights reserved.
            </p>
            <button 
              onClick={() => setModalType('privacy')} 
              className="text-xs text-muted-foreground hover:text-foreground transition-colors"
            >
              Privacy Policy
            </button>
          </div>
          <div className="flex gap-6">
            <span className="text-xs text-muted-foreground hover:text-foreground cursor-pointer transition-colors">Twitter</span>
            <span className="text-xs text-muted-foreground hover:text-foreground cursor-pointer transition-colors">LinkedIn</span>
          </div>
        </div>
      </div>

      <LegalModal 
        isOpen={!!modalType} 
        onClose={() => setModalType(null)} 
        title={modalType ? policies[modalType].title : ''}
      >
        {modalType ? policies[modalType].content : null}
      </LegalModal>
    </footer>
  );
}

```