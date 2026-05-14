---
type: source
source_type: laptop
title: connection_link
slug: connection-link
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/brightbean-studio/templates/onboarding/email/connection_link.html
original_size: 3923
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:41Z"
sensitivity: dept
sensitivity_confidence: 0.70
sensitivity_reason: "Email template HTML for Brightbean Studio onboarding flow — boilerplate-ish work output, no PII; dept-shareable but low-signal"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# connection_link

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/onboarding/email/connection_link.html` on 2026-05-14._

<table width="100%" data-cellpadding="0" data-cellspacing="0"
style="background-color: #FAFAF9; padding: 40px 20px;">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><table width="100%" data-cellpadding="0"
data-cellspacing="0"
style="max-width: 520px; background: #FFFFFF; border-radius: 12px; border: 1px solid #E7E5E4; overflow: hidden;">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center; padding: 32px 32px 24px;"><h1
id="connect-your-social-accounts"
style="margin: 0; font-size: 20px; font-weight: 700; color: #1C1917; letter-spacing: -0.01em;">Connect
your social accounts</h1>
<p>{{ org_name }} has invited you to connect your accounts to <strong>{{
workspace_name }}</strong>.</p></td>
</tr>
<tr>
<td style="text-align: center; padding: 0 32px 28px;"><a
href="%7B%7B%20link_url%20%7D%7D" style="
                                display: inline-block;
                                padding: 12px 32px;
                                font-size: 14px; font-weight: 600;
                                color: #FFFFFF; background-color: #F97316;
                                border-radius: 9999px;
                                text-decoration: none;
                                box-shadow: 0 4px 14px rgba(249,115,22,0.28);
                            ">Connect Accounts</a></td>
</tr>
<tr>
<td style="text-align: center; padding: 0 32px 24px;"><table
width="100%" data-cellpadding="0" data-cellspacing="0"
style="background: #FAFAF9; border-radius: 8px; padding: 16px;">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td
style="padding: 16px; font-size: 13px; color: #57534E; line-height: 1.7"><strong>What
to expect:</strong><br />
1. You'll see a list of platforms to connect.<br />
2. Click "Connect" on each one you'd like to link.<br />
3. Click "Done" when finished to notify your team.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td style="text-align: center; padding: 0 32px 28px;"><p>This link
expires {{ expires_at|date:"M j, Y" }}.</p></td>
</tr>
</tbody>
</table>
<table width="100%" data-cellpadding="0" data-cellspacing="0"
style="max-width: 520px;">
<tbody>
<tr>
<td style="text-align: center; padding: 20px 32px;"><p>Sent by {{
org_name }}</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
