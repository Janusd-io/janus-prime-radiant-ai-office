---
type: source
source_type: laptop
title: email
slug: email-2
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/lib/email.ts
original_size: 2953
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# email

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/lib/email.ts` on 2026-05-14._

```typescript
import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.GMAIL_USER,
    pass: process.env.GMAIL_APP_PASSWORD,
  },
});

export const sendLeadEmail = async (to: string, csvContent: string, packageName: string) => {
  if (!process.env.GMAIL_USER || !process.env.GMAIL_APP_PASSWORD) {
    console.log('--- MOCK EMAIL START (GMAIL) ---');
    console.log(`To: ${to}`);
    console.log(`Subject: Your Dubai Buyer Leads - ${packageName}`);
    console.log('CSV Content Attached');
    console.log('--- MOCK EMAIL END ---');
    return;
  }

  const mailOptions = {
    from: process.env.GMAIL_USER,
    to,
    subject: `Your Dubai Buyer Leads - ${packageName}`,
    text: `Thank you for your purchase of ${packageName} package. Attached is your spreadsheet containing verified Dubai property buyer enquiries. Best of luck with your deals.`,
    attachments: [
      {
        filename: 'dubai_buyer_leads.csv',
        content: csvContent,
      },
    ],
  };

  try {
    await transporter.sendMail(mailOptions);
  } catch (error) {
    console.error('Error sending email:', error);
    throw error;
  }
};

export const sendErrorReport = async (error: any, context: string) => {
  const recipient = 'jehad.altoutou@gmail.com';
  
  if (!process.env.GMAIL_USER || !process.env.GMAIL_APP_PASSWORD) {
    console.log('--- ERROR REPORT MOCK START (GMAIL) ---');
    console.log(`To: ${recipient}`);
    console.log(`Subject: [URGENT] Website Payment Error - ${context}`);
    console.log(`Error: ${error.message || error}`);
    console.log('--- ERROR REPORT MOCK END ---');
    return;
  }

  const mailOptions = {
    from: process.env.GMAIL_USER,
    to: recipient,
    subject: `[URGENT] Website Payment Error - ${context}`,
    text: `A critical error occurred on the website during a payment attempt.\n\nContext: ${context}\nError: ${error.message || error}\nTimestamp: ${new Date().toISOString()}\n\nPlease investigate this issue immediately.`,
    html: `
      <div style="font-family: sans-serif; padding: 20px; border: 1px solid #eee; border-radius: 10px;">
        <h2 style="color: #e11d48;">Critical Payment Error</h2>
        <p>A critical error occurred on the website during a payment attempt.</p>
        <hr style="border: 0; border-top: 1px solid #eee;" />
        <p><strong>Context:</strong> ${context}</p>
        <p><strong>Error:</strong> <span style="color: #e11d48; font-family: monospace;">${error.message || error}</span></p>
        <p><strong>Timestamp:</strong> ${new Date().toLocaleString()}</p>
        <hr style="border: 0; border-top: 1px solid #eee;" />
        <p style="font-size: 12px; color: #666;">This is an automated error report from your Dubai Leads platform.</p>
      </div>
    `,
  };

  try {
    await transporter.sendMail(mailOptions);
  } catch (err) {
    console.error('Failed to send error report email:', err);
  }
};

```