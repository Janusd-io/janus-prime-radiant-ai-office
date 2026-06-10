---
type: integration
community: "HR Forms, n8n Integration, Employee Role"
tags:
  - n8n
  - google-drive
  - automation
---

# Google Drive Integration

Assessify HR form submissions are processed by [[n8n Integration|n8n]] and stored in Google Drive.

## Structure
- **Parent folder:** `HR Documents/` (ID: `1V2LhE-_eyqNsMSFySq9mMWU7u51DAtkz`)
- **Per-employee subfolder:** Created automatically using employee name
- **Contents per employee:**
  - Bank Details Google Doc (converted from HTML)
  - Personal Data Google Doc (converted from HTML)
  - Uploaded file attachments (passport scans, certificates, etc.)

## Flow
1. Assessify sends webhook with form data + base64 files
2. n8n checks if employee folder exists in HR Documents
3. Creates folder if missing
4. Uploads attachments as individual files
5. Generates styled HTML table → uploads → copies as native Google Doc → deletes temp HTML
6. Sends Slack notification with folder link

## Credentials
- Google Drive OAuth2: `Janus GDrive` (ID: `9wm4Mue5fKNfpXpL`)
- Google Sheets OAuth2: `Jehad Google Sheets` (ID: `ufMAYNUceVDn3duH`) — used by error handler

## Related
- [[n8n Integration]]
- [[HR Forms]]
- [[Webhooks & Automation]]
- [[assessify|Assessify]]
