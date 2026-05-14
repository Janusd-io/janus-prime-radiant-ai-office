---
type: source
source_type: laptop
title: Desktop Captures — useFormPersist
slug: useformpersist-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/hooks/useFormPersist.js
original_size: 1533
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# useFormPersist

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/hooks/useFormPersist.js` on 2026-05-14._

```javascript
import { useEffect } from 'react';

export const useFormPersist = (name, methods) => {
    const { watch, reset, getValues } = methods;
    const values = watch();

    useEffect(() => {
        const savedData = localStorage.getItem(name);
        if (savedData) {
            try {
                const parsedData = JSON.parse(savedData);
                // We might want to prompt user before restoring, but for now auto-restore or exposing a method is better
                // Requirement: "Restore Draft prompty on reload". 
                // So we won't auto-reset here, but rather return a method to check/restore.
            } catch (e) {
                console.error("Failed to parse saved form data", e);
            }
        }
    }, [name]);

    useEffect(() => {
        // Debounce saving to avoid perf hit
        const handler = setTimeout(() => {
            // Don't save files to localStorage
            const { attachment, ...safeToSave } = values;
            localStorage.setItem(name, JSON.stringify(safeToSave));
        }, 1000);

        return () => clearTimeout(handler);
    }, [values, name]);

    const loadDraft = () => {
        const savedData = localStorage.getItem(name);
        if (savedData) {
            try {
                return JSON.parse(savedData);
            } catch (e) {
                return null;
            }
        }
        return null;
    };

    const clearDraft = () => {
        localStorage.removeItem(name);
    };

    return { loadDraft, clearDraft };
};

```