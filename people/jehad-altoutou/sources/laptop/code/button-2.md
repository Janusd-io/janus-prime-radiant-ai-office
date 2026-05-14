---
type: source
source_type: laptop
title: Desktop Captures — button
slug: button-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/ui/button.jsx
original_size: 1541
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# button

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/ui/button.jsx` on 2026-05-14._

```jsx
import { motion } from 'framer-motion';
import { cn } from '../../lib/utils';
import { Loader2 } from 'lucide-react';

export const Button = ({
    className,
    variant = 'primary',
    size = 'default',
    isLoading = false,
    children,
    ...props
}) => {
    const variants = {
        primary: 'bg-psi-orange-500 text-white hover:bg-psi-orange-600 shadow-md hover:shadow-lg',
        secondary: 'bg-psi-blue-500 text-white hover:bg-psi-blue-600 shadow-md hover:shadow-lg',
        outline: 'border-2 border-psi-blue-200 text-psi-blue-700 hover:border-psi-blue-500 hover:bg-psi-blue-50',
        ghost: 'text-psi-blue-600 hover:bg-psi-blue-50',
        destructive: 'bg-red-500 text-white hover:bg-red-600',
    };

    const sizes = {
        sm: 'h-9 px-3 text-sm',
        default: 'h-11 px-5 py-2',
        lg: 'h-14 px-8 text-lg',
        icon: 'h-10 w-10 p-2',
    };

    return (
        <motion.button
            whileTap={{ scale: 0.98 }}
            className={cn(
                'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-psi-orange-500 disabled:pointer-events-none disabled:opacity-50',
                variants[variant],
                sizes[size],
                className
            )}
            disabled={isLoading || props.disabled}
            {...props}
        >
            {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            {children}
        </motion.button>
    );
};

```