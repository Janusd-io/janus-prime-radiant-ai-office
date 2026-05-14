---
type: source
source_type: laptop
title: PolicyContent
slug: policycontent
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/legal/PolicyContent.tsx
original_size: 4318
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# PolicyContent

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/legal/PolicyContent.tsx` on 2026-05-14._

```tsx
import React from 'react';

export const PrivacyPolicy = () => (
  <div className="space-y-4">
    <p>Last Updated: {new Date().toLocaleDateString()}</p>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">1. Information We Collect</h3>
      <p>We collect information that you provide directly to us when you subscribe to our services, including your name, email address, and payment information processed through Stripe.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">2. How We Use Your Information</h3>
      <p>We use the information we collect to provide, maintain, and improve our services, to process transactions, and to communicate with you about your account and our services.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">3. Data Security</h3>
      <p>We use industry-standard security measures, including AES-256 encryption, to protect your personal information. We are committed to maintaining the highest level of security to ensure your data remains confidential and safe.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">4. Your Rights</h3>
      <p>You have the right to access, update, or delete your personal information at any time. Please contact us to exercise these rights.</p>
    </section>
  </div>
);

export const TermsOfService = () => (
  <div className="space-y-4">
    <p>Last Updated: {new Date().toLocaleDateString()}</p>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">1. Acceptance of Terms</h3>
      <p>By accessing or using the Dubai Property Leads platform, you agree to be bound by these Terms of Service.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">2. Use of Leads</h3>
      <p>Leads provided by our platform are for the exclusive use of the purchaser. Reselling or distributing these leads to third parties is strictly prohibited.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">3. Accuracy of Information</h3>
      <p>While we strive for 100% accuracy, we do not guarantee the completeness or accuracy of any lead information. Real estate market conditions change rapidly.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">4. Limitation of Liability</h3>
      <p>Dubai Property Leads shall not be liable for any indirect, incidental, or consequential damages resulting from the use of our services.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">5. Lead Distribution Policy</h3>
      <p>To ensure healthy competition and maximum reliability for our partners, each lead is shared with a maximum of 3 professional users. This model guarantees that buyers receive timely responses while providing agents with a high probability of conversion. By purchasing a lead, you acknowledge and accept this distribution structure.</p>
    </section>
  </div>
);

export const RefundPolicy = () => (
  <div className="space-y-4">
    <p>Last Updated: {new Date().toLocaleDateString()}</p>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">1. Lead Replacement Policy</h3>
      <p>We provide a 100% replacement guarantee for leads with invalid contact information (wrong number or invalid email) if reported within 48 hours of delivery.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">2. Refund Eligibility</h3>
      <p>Due to the nature of digital lead delivery, all sales are final. We do not offer cash refunds. However, we ensure your credits are fairly applied for any verified invalid leads.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">3. Reporting Issues</h3>
      <p>To report an issue and request a replacement, please email <span className="font-bold">dubaipropertylead@gmail.com</span> with the lead details and the nature of the issue.</p>
    </section>
    <section>
      <h3 className="text-lg font-bold text-slate-900 mb-2">4. Processing Time</h3>
      <p>Replacement lead requests are typically processed within 24 hours of receiving the report.</p>
    </section>
  </div>
);

```