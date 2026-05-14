---
type: source
source_type: laptop
title: Desktop Captures — select
slug: select-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/ui/select.jsx
original_size: 3891
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# select

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/ui/select.jsx` on 2026-05-14._

```jsx
import React, { useState, useRef, useEffect } from 'react';
import { cn } from '../../lib/utils';
import { ChevronDown, Check } from 'lucide-react';

export const Select = ({ options = [], value, onChange, placeholder, error, className }) => {
    const [isOpen, setIsOpen] = useState(false);
    const containerRef = useRef(null);

    // Close when clicking outside
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (containerRef.current && !containerRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    const handleSelect = (optionValue) => {
        onChange(optionValue);
        setIsOpen(false);
    };

    const selectedOption = options.find(opt => opt.value === value);

    return (
        <div className="relative group" ref={containerRef}>
            <div
                className={cn(
                    'flex h-12 w-full items-center justify-between rounded-xl border border-gray-200 bg-white px-4 py-3 text-sm shadow-sm transition-all duration-200 cursor-pointer',
                    'hover:border-gray-300',
                    isOpen && 'border-psi-orange-500 ring-1 ring-psi-orange-500',
                    error && 'border-red-500 bg-red-50/10',
                    className
                )}
                onClick={() => setIsOpen(!isOpen)}
            >
                <span className={cn('block truncate', !value && 'text-gray-400')}>
                    {selectedOption ? selectedOption.label : (placeholder || 'Select an option')}
                </span>
                <ChevronDown className={cn("h-5 w-5 text-gray-400 transition-transform duration-200", isOpen && "rotate-180")} />
            </div>

            {/* Dropdown Menu */}
            {isOpen && (
                <div className="absolute z-50 mt-2 max-h-60 w-full overflow-auto rounded-xl bg-white p-1 shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm animate-fade-in custom-scrollbar border border-gray-100">
                    {/* Placeholder as first disabled option */}
                    <div className="relative cursor-default select-none py-2.5 pl-4 pr-9 text-gray-400 italic border-b border-gray-50">
                        {placeholder || 'Select an option'}
                    </div>

                    {options.map((option) => {
                        const isSelected = option.value === value;
                        return (
                            <div
                                key={option.value}
                                className={cn(
                                    'relative cursor-pointer select-none py-2.5 pl-4 pr-9 transition-colors rounded-lg',
                                    isSelected ? 'bg-psi-blue-50 text-psi-blue-900 font-medium' : 'text-gray-900 hover:bg-gray-50'
                                )}
                                onClick={() => handleSelect(option.value)}
                            >
                                <span className="block truncate">{option.label}</span>
                                {isSelected && (
                                    <span className="absolute inset-y-0 right-0 flex items-center pr-3 text-psi-orange-600">
                                        <Check className="h-4 w-4" aria-hidden="true" />
                                    </span>
                                )}
                            </div>
                        );
                    })}
                </div>
            )}

            {error && (
                <span className="text-xs text-red-500 mt-1.5 block font-medium animate-fade-in">{error}</span>
            )}
        </div>
    );
};

Select.displayName = 'Select';

```