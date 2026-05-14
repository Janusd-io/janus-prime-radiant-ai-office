---
type: source
source_type: laptop
title: api
slug: api-2
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/lib/api.js
original_size: 3767
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# api

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/lib/api.js` on 2026-05-14._

```javascript
export const submitToWebhook = async (data) => {
    const webhookUrl = import.meta.env.VITE_N8N_WEBHOOK_URL || "https://n8n.srv1086109.hstgr.cloud/webhook/2f1599d5-732f-4ab2-bde1-c879f2265451";
    const webhookSecret = import.meta.env.VITE_WEBHOOK_SECRET;

    if (!webhookUrl) throw new Error("Webhook URL is not configured.");

    const { attachment, ...textData } = data;
    
    // Check if there are actually any files
    let hasFiles = false;
    if (attachment) {
        if (Array.isArray(attachment) && attachment.length > 0) hasFiles = true;
        if (attachment instanceof File) hasFiles = true;
    }

    const fetchOptions = {
        method: 'POST',
        headers: {}
    };

    if (hasFiles) {
        // Send as multipart/form-data
        const formData = new FormData();
        Object.entries(textData).forEach(([key, value]) => {
            if (value === undefined || value === null) return;
            if (Array.isArray(value)) {
                // Flatten array of objects into simple key-index-property mapping for n8n
                value.forEach((item, index) => {
                    if (typeof item === 'object' && item !== null) {
                        Object.entries(item).forEach(([subKey, subValue]) => {
                            if (subValue) formData.append(`${key}_${index + 1}_${subKey}`, subValue);
                        });
                    } else if (item) {
                        formData.append(`${key}_${index + 1}`, item);
                    }
                });
            } else {
                formData.append(key, value);
            }
        });
        
        if (Array.isArray(attachment)) {
            attachment.forEach((file) => formData.append('files', file));
        } else {
            formData.append('files', attachment);
        }
        
        fetchOptions.body = formData;
    } else {
        // Send purely as JSON
        fetchOptions.headers['Content-Type'] = 'application/json';
        fetchOptions.body = JSON.stringify(textData);
    }

    const maxRetries = 3;
    let attempt = 0;

    // Use direct URL. If CORS fails, it will throw a fetch error instead of 500.
    // If Vite proxy was giving 500 previously, doing direct fetch will bypass it.
    let requestUrl = webhookUrl;
    if (import.meta.env.DEV) {
        try {
            const u = new URL(webhookUrl);
            requestUrl = u.pathname + u.search;
        } catch (e) {
            console.warn("Invalid webhook URL format", e);
        }
    }

    while (attempt < maxRetries) {
        try {
            const response = await fetch(requestUrl, fetchOptions);

            if (!response.ok) {
                // If 5xx error, retry. If 4xx, probably don't retry unless specific cases?
                // User said "if there was any issue and it hit an error it should try again"
                // Let's retry on any non-ok status for robustness as per user request, 
                // but usually 400s are client errors. However, n8n might return 500 equivalent.
                throw new Error(`Submission failed: ${response.status} ${response.statusText}`);
            }

            // Attempt to parse JSON, but if empty response (often 200 OK with no body), handle gracefully
            const text = await response.text();
            return text ? JSON.parse(text) : { success: true };

        } catch (error) {
            attempt++;
            console.error(`Webhook submission attempt ${attempt} failed:`, error);

            if (attempt >= maxRetries) {
                throw error;
            }

            // Wait before retrying (e.g., 1s, 2s, 4s)
            await new Promise(resolve => setTimeout(resolve, 1000 * Math.pow(2, attempt - 1)));
        }
    }
};

```