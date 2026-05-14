---
type: source
source_type: laptop
title: label
slug: label-3
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/ui/label.jsx
original_size: 545
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# label

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/ui/label.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { cn } from '../../lib/utils';

export const Label = React.forwardRef(({ className, required, children, ...props }, ref) => (
    <label
        ref={ref}
        className={cn(
            'text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-psi-blue-900 mb-2 block',
            className
        )}
        {...props}
    >
        {children}
        {required && <span className="text-psi-orange-500 ml-1">*</span>}
    </label>
));

Label.displayName = 'Label';

```