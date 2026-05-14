---
type: source
source_type: laptop
title: textarea
slug: textarea-3
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/ui/textarea.jsx
original_size: 1004
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# textarea

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/ui/textarea.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { cn } from '../../lib/utils';

export const Textarea = React.forwardRef(({ className, error, ...props }, ref) => {
    return (
        <div className="relative">
            <textarea
                className={cn(
                    'flex min-h-[120px] w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm ring-offset-white placeholder:text-gray-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-psi-blue-500 focus-visible:border-transparent disabled:cursor-not-allowed disabled:opacity-50 transition-all duration-200 resize-y',
                    error && 'border-red-500 focus-visible:ring-red-500',
                    className
                )}
                ref={ref}
                {...props}
            />
            {error && (
                <span className="text-xs text-red-500 mt-1 block font-medium animate-fade-in">{error}</span>
            )}
        </div>
    );
});

Textarea.displayName = 'Textarea';

```