---
source_file: "SOP.md"
type: "integration"
community: "HR Forms, n8n Integration, Employee Role"
location: "section 7"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - n8n
  - automation
  - community/HR_Forms,_n8n_Integration,_Employee_Role
---

# n8n Integration

n8n instance hosted at `https://n8n.srv1086109.hstgr.cloud`.

## Workflows

### 1. HR Document Processor
- **Webhook:** `POST /webhook/2f1599d5-732f-4ab2-bde1-c879f2265451`
- **Switch routes by:** `formType` (bank_details) or `formName` (Personal Data Form)
- **Bank Details branch:** folder check/create → Design Bank Details HTML → upload → convert to Google Doc → delete temp → Slack
- **Personal Data branch:** folder check/create → upload attachments → Design Professional Table HTML → upload → convert to Google Doc → delete temp → Slack
- **Key pattern:** Both branches duplicate nodes for "folder exists" vs "folder created" paths (If node splits into two parallel pipelines)

### 2. Error Handler
- **Trigger:** `errorTrigger` node (n8n built-in, not webhook)
- **Actions:** Log to Google Sheets (`Error Logs` spreadsheet) + Slack DM
- **Columns:** Timestamp, Workflow, URL, Node (lastNodeExecuted), Error Message
- **Gotcha:** Only fires on production executions, NOT manual test runs. Each monitored workflow must have this set as its Error Workflow in workflow Settings.
- **Google Sheet ID:** `1cPp7GZNqDgEBa54ivX1VhW94E2x_XerGPPije_DDaB4`

## Webhook Payload (from Assessify)
Assessify fires webhooks from `src/lib/webhooks.ts` (HMAC-signed). Form submissions send:
- `event`: `form.submitted`
- `data.formType`: `bank_details` | `personal_data`
- `data.formName`: display name
- `data.employee`: `{ name, email }`
- `data.bankDetails` / `data.personalInformation` / etc.: form-specific fields
- `data.files[]`: `{ fileName, fileType, base64Data }` — attachments as base64

## Connections
- [[Webhooks & Automation]] - `references` [EXTRACTED]
- [[Google Drive Integration]] - HR doc storage
- [[HR Forms]] - form submission source

## Related
- [[n8n-workflow|/n8n-workflow]]
- [[n8n-code|/n8n-code]]
- [[assessify|Assessify]]
