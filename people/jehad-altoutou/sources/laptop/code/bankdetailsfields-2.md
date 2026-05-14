---
type: source
source_type: laptop
title: BankDetailsFields
slug: bankdetailsfields-2
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/form/sections/BankDetailsFields.jsx
original_size: 3313
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# BankDetailsFields

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/form/sections/BankDetailsFields.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { useFormContext } from 'react-hook-form';
import { Input } from '../../ui/input';
import { Label } from '../../ui/label';
import { Card, CardContent } from '../../ui/card';
import { motion } from 'framer-motion';

export const BankDetailsFields = () => {
    const { register, formState: { errors } } = useFormContext();

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="space-y-6"
        >
            <div className="flex items-center gap-2 mb-2">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Bank Details</h3>
            </div>
            
            <Card>
                <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                        <Label required>Bank Name</Label>
                        <Input {...register('bankName')} placeholder="Enter bank name" error={errors.bankName?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Branch / Location</Label>
                        <Input {...register('branchLocation')} placeholder="Enter branch location" error={errors.branchLocation?.message} />
                    </div>
                    <div className="space-y-2 md:col-span-2">
                        <Label>Address</Label>
                        <Input {...register('address')} placeholder="Enter address" error={errors.address?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Account Name</Label>
                        <Input {...register('accountName')} placeholder="John Doe" error={errors.accountName?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Account No.</Label>
                        <Input {...register('accountNo')} placeholder="Enter account number" error={errors.accountNo?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>IBAN</Label>
                        <Input {...register('iban')} placeholder="AE..." error={errors.iban?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Swift Code</Label>
                        <Input {...register('swiftCode')} placeholder="Enter swift code" error={errors.swiftCode?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Sort Code</Label>
                        <Input {...register('sortCode')} placeholder="Enter sort code" error={errors.sortCode?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Date (dd/mm/yy)</Label>
                        <Input {...register('signatureDate')} placeholder="DD/MM/YY" error={errors.signatureDate?.message} />
                    </div>
                </CardContent>
            </Card>
        </motion.div>
    );
};

```