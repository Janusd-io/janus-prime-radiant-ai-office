---
type: source
source_type: laptop
title: input
slug: input-3
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/ui/input.jsx
original_size: 1204
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# input

_Extracted from `Desktop/Form Request copy/src/components/ui/input.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { cn } from '../../lib/utils';

export const Input = React.forwardRef(({ className, type, error, ...props }, ref) => {
    return (
        <div className="relative group">
            <input
                type={type}
                className={cn(
                    'flex h-12 w-full rounded-xl border border-transparent bg-white/60 px-4 py-3 text-sm shadow-sm ring-1 ring-gray-200/50 backdrop-blur-sm placeholder:text-gray-400 transition-all duration-300',
                    'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-psi-orange-500/50 focus-visible:border-psi-orange-500 focus-visible:bg-white',
                    'hover:bg-white/80 hover:ring-gray-300',
                    'disabled:cursor-not-allowed disabled:opacity-50',
                    error && 'ring-red-500 focus-visible:ring-red-500 bg-red-50/10',
                    className
                )}
                ref={ref}
                {...props}
            />
            {error && (
                <span className="text-xs text-red-500 mt-1.5 block font-medium animate-fade-in">{error}</span>
            )}
        </div>
    );
});

Input.displayName = 'Input';

```