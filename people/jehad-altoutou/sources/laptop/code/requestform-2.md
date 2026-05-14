---
type: source
source_type: laptop
title: RequestForm
slug: requestform-2
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/form/RequestForm.jsx
original_size: 10560
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# RequestForm

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/form/RequestForm.jsx` on 2026-05-14._

```jsx
import React, { useState } from 'react';
import { useForm, FormProvider, Controller } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { formSchema } from '../../lib/schemas';
import { useFormPersist } from '../../hooks/useFormPersist';
import { submitToWebhook } from '../../lib/api';
import { Button } from '../ui/button';
import { Input } from '../ui/input';
import { Label } from '../ui/label';
import { Select } from '../ui/select';
import { Card, CardContent } from '../ui/card';
import { BankDetailsFields } from './sections/BankDetailsFields';
import { PersonalDataFields } from './sections/PersonalDataFields';
import { ReviewSummary } from './ReviewSummary';
import { CheckCircle2, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

export const RequestForm = () => {
    const [isReviewing, setIsReviewing] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitSuccess, setSubmitSuccess] = useState(null); // { referenceId: string }
    const [submitError, setSubmitError] = useState(null);

    const methods = useForm({
        resolver: zodResolver(formSchema),
        defaultValues: {
            requesterName: '',
            requesterEmail: '',
            requestType: undefined,
        },
        mode: "onBlur"
    });

    const { watch, handleSubmit, trigger, reset, getValues } = methods;
    const requestType = watch('requestType');

    // Persistence
    const { loadDraft, clearDraft } = useFormPersist('janus-form-v1', methods);

    const handleReview = async () => {
        const valid = await trigger();
        if (valid) {
            setIsReviewing(true);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    };

        const onFinalSubmit = async () => {
        setIsSubmitting(true);
        setSubmitError(null);
        let formValues = getValues();

        // 1. Enforce specific schema order and isolate form types
        let orderedKeys = [];
        if (formValues.requestType === 'Bank Details') {
            orderedKeys = [
                'requestType', 'referenceId', 'requesterName', 'requesterEmail', 'requesterPhone',
                'bankName', 'branchLocation', 'accountName', 'accountNo', 'iban', 'swiftCode', 'sortCode', 'address', 'signatureDate', 
                'notes', 'attachment'
            ];
        } else {
            orderedKeys = [
                'requestType', 'referenceId', 'requesterName', 'requesterEmail', 'requesterPhone',
                'title', 'firstName', 'preferredName', 'surname', 'otherSurname',
                'nationality', 'placeOfBirth', 'dateOfBirth', 'maritalStatus', 'religion',
                'physicalAddress', 'homePhone', 'mobilePhone', 'personalEmail',
                'overseasAddress', 'overseasHomePhone',
                'fatherName', 'motherName', 'spouseName', 'spouseDateOfBirth',
                'children', 'education', 'qualifications', 'languageProficiency',
                'nextOfKinName', 'nextOfKinRelationship', 'nextOfKinAddress', 'nextOfKinHomePhone', 'nextOfKinMobilePhone', 'nextOfKinWorkPhone',
                'emergencyContactName', 'emergencyContactRelationship', 'emergencyContactAddress', 'emergencyContactHomePhone', 'emergencyContactMobilePhone', 'emergencyContactWorkPhone',
                'previousCompany', 'previousJobTitle', 
                'hrDateOfHire', 'hrJobTitle', 'hrDepartment', 'hrOfficeLocation',
                'notes', 'attachment'
            ];
        }

        const referenceId = `REQ-${Date.now()}`;
        const rawData = { ...formValues, referenceId };
        const data = {};
        
        // Assemble payload rigidly matching the ordered template
        orderedKeys.forEach(key => {
            if (rawData[key] !== undefined) {
                data[key] = rawData[key];
            }
        });

        // Generate Reference ID client-side so it can be sent to webhook (handled in rawData)
        
        try {
            const result = await submitToWebhook(data);
            // Use server response ID if available, otherwise fallback to client-generated ID
            setSubmitSuccess({ referenceId: result?.referenceId || referenceId });
            clearDraft();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch (error) {
            setSubmitError(error.message || "Something went wrong. Please try again.");
        } finally {
            setIsSubmitting(false);
        }
    };

    if (submitSuccess) {
        return (
            <div className="flex flex-col items-center justify-center py-12 text-center animate-fade-in">
                <div className="bg-green-100 p-4 rounded-full mb-6">
                    <CheckCircle2 className="w-16 h-16 text-green-600" />
                </div>
                <h2 className="text-3xl font-bold text-janus-blue-900 mb-2">Form Submitted!</h2>
                <p className="text-gray-600 max-w-md mx-auto mb-8">
                    Your HR information has been successfully submitted to Janus. We have received your data and it will be processed shortly.
                </p>
                <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 mb-8">
                    <p className="text-sm text-gray-500 mb-1 uppercase tracking-wide">Reference ID</p>
                    <p className="text-xl font-mono font-bold text-janus-blue-600">{submitSuccess.referenceId}</p>
                </div>
                <Button onClick={() => window.location.reload()}>Submit Another Form</Button>
            </div>
        );
    }

    if (isReviewing) {
        return (
            <ReviewSummary
                data={getValues()}
                onEdit={() => setIsReviewing(false)}
                onSubmit={onFinalSubmit}
                isSubmitting={isSubmitting}
                submitError={submitError}
            />
        );
    }

    return (
        <FormProvider {...methods}>
            <form onSubmit={(e) => e.preventDefault()} className="space-y-8 animate-fade-in">

                {/* Requester Details */}
                <section className="space-y-4">
                    <div className="flex items-center gap-2 mb-2">
                        <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                        <h2 className="text-xl font-semibold text-janus-blue-900">Requester Details</h2>
                    </div>
                    <Card>
                        <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div className="space-y-2">
                                <Label required>Full Name</Label>
                                <Input
                                    {...methods.register('requesterName')}
                                    placeholder="Your Name"
                                    error={methods.formState.errors.requesterName?.message}
                                />
                            </div>
                            <div className="space-y-2">
                                <Label required>Email ID</Label>
                                <Input
                                    {...methods.register('requesterEmail')}
                                    placeholder="name@janus-digital.com"
                                    error={methods.formState.errors.requesterEmail?.message}
                                />
                            </div>
                            <div className="space-y-2">
                                <Label>Phone (Optional)</Label>
                                <Input
                                    {...methods.register('requesterPhone')}
                                    placeholder="+971..."
                                />
                            </div>
                        </CardContent>
                    </Card>
                </section>

                {/* Request Type Selector */}
                <section className="space-y-4">
                    <div className="flex items-center gap-2 mb-2">
                        <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                        <h2 className="text-xl font-semibold text-janus-blue-900">Form Type</h2>
                    </div>

                    <div className="space-y-2">
                        <Controller
                            control={methods.control}
                            name="requestType"
                            render={({ field }) => (
                                <Select
                                    value={field.value}
                                    onChange={field.onChange}
                                    options={[
                                        { value: 'Bank Details', label: 'Bank Details Form' },
                                        { value: 'Personal Data', label: 'Janus Personal Data Form' }
                                    ]}
                                    placeholder="Select HR Form Type..."
                                    error={methods.formState.errors.requestType?.message}
                                />
                            )}
                        />
                    </div>
                </section>

                {/* Conditional Sections */}
                <div className="min-h-[300px]">
                    {requestType === 'Bank Details' && <BankDetailsFields />}
                    {requestType === 'Personal Data' && <PersonalDataFields />}
                </div>

                {/* Global Error Message */}
                {submitError && (
                    <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg flex items-center">
                        <AlertCircle className="w-5 h-5 mr-2" />
                        {submitError}
                    </div>
                )}

                {/* Action Bar */}
                <div className="pt-4 border-t border-gray-200 flex justify-end">
                    <Button
                        type="button"
                        onClick={handleReview}
                        size="lg"
                        className="w-full sm:w-auto bg-janus-blue-500 hover:bg-janus-blue-600"
                        disabled={!requestType} // Disable until type selected
                    >
                        Review Form
                    </Button>
                </div>

            </form>
        </FormProvider>
    );
};

```