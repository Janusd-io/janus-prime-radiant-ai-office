---
type: source
source_type: laptop
title: magic_link
slug: magic-link
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/email/magic_link.html
original_size: 3043
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# magic_link

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/client_portal/email/magic_link.html` on 2026-05-14._

<table width="100%" data-cellpadding="0" data-cellspacing="0"
style="padding: 40px 20px;">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><table width="520" data-cellpadding="0"
data-cellspacing="0"
style="background: #FFFFFF; border-radius: 12px; border: 1px solid #E7E5E4; overflow: hidden;">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="padding: 32px 32px 0 32px"><p>{{ workspace.name }}</p></td>
</tr>
<tr>
<td style="padding: 24px 32px 32px 32px"><p>Hi {{
client_user.display_name }},</p>
<p>{{ created_by.display_name }} has shared content for your review.
Click below to access your portal and approve or provide feedback on
scheduled posts.</p>
<table data-cellpadding="0" data-cellspacing="0" width="100%">
<tbody>
<tr>
<td style="text-align: center;"><a href="%7B%7B%20magic_url%20%7D%7D"
style="display: inline-block; padding: 12px 32px; background: #F97316; color: #FFFFFF; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 9999px;">Review
Posts</a></td>
</tr>
</tbody>
</table>
<p>This link is valid for 30 days. If it expires, ask your account
manager for a new one.</p></td>
</tr>
<tr>
<td style="padding: 16px 32px; border-top: 1px solid #E7E5E4"><p>You're
receiving this because you're a client of {{ workspace.name }}.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
