---
type: source
source_type: laptop
title: schemas
slug: schemas
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/lib/schemas.js
original_size: 5773
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# schemas

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/lib/schemas.js` on 2026-05-14._

```javascript
import { z } from 'zod';

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const ACCEPTED_IMAGE_TYPES = ["image/jpeg", "image/jpg", "image/png", "image/webp", "application/pdf", "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"];

export const requesterSchema = z.object({
    requesterName: z.string().min(2, "Name is required"),
    requesterEmail: z.string().email("Invalid email address"),
    requesterPhone: z.string().optional(),
});

export const formSchema = z.object({
    requesterName: z.string().min(2, "Name is required"),
    requesterEmail: z.string().email("Invalid email address"),
    requesterPhone: z.string().optional(),

    requestType: z.enum([
        "Bank Details",
        "Personal Data"
    ], { required_error: "Please select an HR form type" }),

    // Bank Details Fields
    bankName: z.string().optional(),
    branchLocation: z.string().optional(),
    address: z.string().optional(),
    accountName: z.string().optional(),
    accountNo: z.string().optional(),
    iban: z.string().optional(),
    swiftCode: z.string().optional(),
    sortCode: z.string().optional(),
    signatureDate: z.string().optional(),

    // Personal Data Fields
    title: z.string().optional(),
    firstName: z.string().optional(),
    preferredName: z.string().optional(),
    surname: z.string().optional(),
    otherSurname: z.string().optional(),
    nationality: z.string().optional(),
    placeOfBirth: z.string().optional(),
    physicalAddress: z.string().optional(),
    homePhone: z.string().optional(),
    mobilePhone: z.string().optional(),
    overseasAddress: z.string().optional(),
    overseasHomePhone: z.string().optional(),
    dateOfBirth: z.string().optional(),
    maritalStatus: z.string().optional(),
    personalEmail: z.string().optional(),
    religion: z.string().optional(),
    fatherName: z.string().optional(),
    motherName: z.string().optional(),
    spouseName: z.string().optional(),
    spouseDateOfBirth: z.string().optional(),

    // Arrays for dynamic fields
    children: z.array(z.object({
        name: z.string().optional(),
        gender: z.string().optional(),
        dateOfBirth: z.string().optional()
    })).optional(),

    education: z.array(z.object({
        university: z.string().optional(),
        startDate: z.string().optional(),
        endDate: z.string().optional(),
        degreeType: z.string().optional(),
        majorSubject: z.string().optional(),
        gradeGpa: z.string().optional(),
        graduationDate: z.string().optional()
    })).optional(),

    qualifications: z.array(z.object({
        dateIssued: z.string().optional(),
        description: z.string().optional(),
        certificateNumber: z.string().optional()
    })).optional(),

    // Next of kin
    nextOfKinName: z.string().optional(),
    nextOfKinAddress: z.string().optional(),
    nextOfKinHomePhone: z.string().optional(),
    nextOfKinMobilePhone: z.string().optional(),
    nextOfKinWorkPhone: z.string().optional(),
    nextOfKinRelationship: z.string().optional(),

    // Emergency contact
    emergencyContactName: z.string().optional(),
    emergencyContactAddress: z.string().optional(),
    emergencyContactHomePhone: z.string().optional(),
    emergencyContactMobilePhone: z.string().optional(),
    emergencyContactWorkPhone: z.string().optional(),
    emergencyContactRelationship: z.string().optional(),

    languageProficiency: z.array(z.object({
        language: z.string().optional(),
        skill: z.string().optional(),
        level: z.string().optional()
    })).optional(),

    // Previous employment
    previousCompany: z.string().optional(),
    previousJobTitle: z.string().optional(),

    // Firm information (To be completed by HR - optional)
    hrDateOfHire: z.string().optional(),
    hrJobTitle: z.string().optional(),
    hrDepartment: z.string().optional(),
    hrOfficeLocation: z.string().optional(),

    // Shared
    notes: z.string().optional(),
    attachment: z.any().optional(),
}).superRefine((data, ctx) => {
    if (data.requestType === "Bank Details") {
        if (!data.bankName) ctx.addIssue({ path: ["bankName"], message: "Bank Name is required", code: "custom" });
        if (!data.branchLocation) ctx.addIssue({ path: ["branchLocation"], message: "Branch/Location is required", code: "custom" });
        if (!data.accountName) ctx.addIssue({ path: ["accountName"], message: "Account Name is required", code: "custom" });
        if (!data.accountNo) ctx.addIssue({ path: ["accountNo"], message: "Account No is required", code: "custom" });
        if (!data.iban) ctx.addIssue({ path: ["iban"], message: "IBAN is required", code: "custom" });
    }

    if (data.requestType === "Personal Data") {
        if (!data.firstName) ctx.addIssue({ path: ["firstName"], message: "First Name is required", code: "custom" });
        if (!data.surname) ctx.addIssue({ path: ["surname"], message: "Surname is required", code: "custom" });
        if (!data.nationality) ctx.addIssue({ path: ["nationality"], message: "Nationality is required", code: "custom" });
        if (!data.dateOfBirth) ctx.addIssue({ path: ["dateOfBirth"], message: "Date of Birth is required", code: "custom" });
        if (!data.personalEmail) ctx.addIssue({ path: ["personalEmail"], message: "Personal Email is required", code: "custom" });
        if (!data.mobilePhone) ctx.addIssue({ path: ["mobilePhone"], message: "Mobile Phone is required", code: "custom" });
        if (!data.fatherName) ctx.addIssue({ path: ["fatherName"], message: "Father's Name is required", code: "custom" });
        if (!data.motherName) ctx.addIssue({ path: ["motherName"], message: "Mother's Name is required", code: "custom" });
    }
});

```