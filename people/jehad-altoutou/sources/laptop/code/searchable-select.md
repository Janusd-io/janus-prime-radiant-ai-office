---
type: source
source_type: laptop
title: searchable-select
slug: searchable-select
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/ui/searchable-select.jsx
original_size: 6155
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# searchable-select

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/ui/searchable-select.jsx` on 2026-05-14._

```jsx
import React, { useState, useRef, useEffect, useMemo } from 'react';
import { cn } from '../../lib/utils';
import { ChevronDown, Search, Check } from 'lucide-react';

export const SearchableSelect = ({ options = [], value, onChange, placeholder, error, className }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const containerRef = useRef(null);
    const inputRef = useRef(null);

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

    // Filter options based on search term
    const filteredOptions = useMemo(() => {
        if (!searchTerm) return options;
        return options.filter(option => {
            const label = option.label || option;
            return String(label).toLowerCase().includes(searchTerm.toLowerCase());
        });
    }, [options, searchTerm]);

    // Handle selection
    const handleSelect = (option) => {
        const val = option.value || option;
        onChange(val);
        setIsOpen(false);
        setSearchTerm('');
    };

    // Focus search input when opening
    useEffect(() => {
        if (isOpen && inputRef.current) {
            inputRef.current.focus();
        }
    }, [isOpen]);

    // Find selected label
    const selectedLabel = useMemo(() => {
        if (!value) return '';
        const selectedOption = options.find(opt => (opt.value || opt) === value);
        return selectedOption ? (selectedOption.label || selectedOption) : value;
    }, [options, value]);

    return (
        <div className="relative group" ref={containerRef}>
            <div
                className={cn(
                    'flex h-12 w-full items-center justify-between rounded-xl border border-transparent bg-white/60 px-4 py-3 text-sm shadow-sm ring-1 ring-gray-200/50 backdrop-blur-sm transition-all duration-300 cursor-pointer',
                    'hover:bg-white/80 hover:ring-gray-300',
                    isOpen && 'ring-2 ring-psi-orange-500/50 bg-white shadow-md',
                    error && 'ring-red-500 bg-red-50/10',
                    className
                )}
                onClick={() => setIsOpen(!isOpen)}
            >
                <span className={cn('block truncate', !value && 'text-gray-400')}>
                    {value ? selectedLabel : (placeholder || 'Select an option')}
                </span>
                <ChevronDown className={cn("h-5 w-5 text-gray-400 transition-transform duration-200", isOpen && "rotate-180")} />
            </div>

            {/* Dropdown Menu */}
            {isOpen && (
                <div className="absolute z-50 mt-2 max-h-60 w-full overflow-hidden rounded-xl bg-white/90 backdrop-blur-xl shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm animate-fade-in border border-white/50 flex flex-col">
                    {/* Search Input */}
                    <div className="sticky top-0 z-10 bg-white/95 border-b border-gray-100 p-2">
                        <div className="relative">
                            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-gray-400" />
                            <input
                                ref={inputRef}
                                type="text"
                                className="w-full rounded-lg bg-gray-50 py-2 pl-9 pr-4 text-sm focus:outline-none focus:ring-1 focus:ring-psi-orange-500 text-gray-900 placeholder:text-gray-400"
                                placeholder="Search..."
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                                onClick={(e) => e.stopPropagation()}
                            />
                        </div>
                    </div>

                    {/* Options List */}
                    <div className="overflow-y-auto max-h-48 custom-scrollbar">
                        {filteredOptions.length > 0 ? (
                            filteredOptions.map((option) => {
                                const val = option.value || option;
                                const label = option.label || option;
                                const isSelected = val === value;

                                return (
                                    <div
                                        key={val}
                                        className={cn(
                                            'relative cursor-pointer select-none py-2.5 pl-4 pr-9 transition-colors',
                                            isSelected ? 'bg-psi-blue-50 text-psi-blue-900 font-medium' : 'text-gray-900 hover:bg-gray-50'
                                        )}
                                        onClick={() => handleSelect(option)}
                                    >
                                        <span className="block truncate">{label}</span>
                                        {isSelected && (
                                            <span className="absolute inset-y-0 right-0 flex items-center pr-3 text-psi-orange-600">
                                                <Check className="h-4 w-4" aria-hidden="true" />
                                            </span>
                                        )}
                                    </div>
                                );
                            })
                        ) : (
                            <div className="py-3 px-4 text-gray-500 text-center italic">No results found</div>
                        )}
                    </div>
                </div>
            )}

            {error && (
                <span className="text-xs text-red-500 mt-1.5 block font-medium animate-fade-in">{error}</span>
            )}
        </div>
    );
};

```