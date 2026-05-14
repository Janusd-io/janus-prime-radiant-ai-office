---
type: source
source_type: laptop
title: ReviewSummary
slug: reviewsummary
created: 2026-04-08
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/form/ReviewSummary.jsx
original_size: 30033
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ReviewSummary

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/form/ReviewSummary.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { Button } from '../ui/button';
import { Card, CardContent } from '../ui/card';
import { Edit2, Send, FileText, CheckCircle2, User, Target, AlertCircle, Phone, Users, GraduationCap, HeartPulse, Briefcase, Info } from 'lucide-react';

export const ReviewSummary = ({ data, onEdit, onSubmit, isSubmitting, submitError }) => {

    const Section = ({ title, icon: Icon, children }) => {
        let hasContent = false;
        React.Children.forEach(children, child => {
            if (!child) return;
            if (child.props.value && child.props.value !== '') hasContent = true;
            if (child.props.items && child.props.items.length > 0) hasContent = true;
            if (child.props.files && (Array.isArray(child.props.files) ? child.props.files.length > 0 : true)) hasContent = true;
            if (Array.isArray(child.props.children) && child.props.children.length > 0) hasContent = true;
        });
        
        if (!hasContent) return null;

        return (
            <div className="relative group">
                <div className="absolute inset-0 bg-gradient-to-r from-slate-100/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-2xl -z-10" />
                <div className="mb-10 last:mb-0">
                    <div className="flex items-center gap-3 mb-6 relative">
                        <div className="absolute -left-4 top-1/2 -translate-y-1/2 w-1 h-6 bg-gradient-to-b from-blue-500 to-indigo-600 rounded-r-full opacity-0 group-hover:opacity-100 transition-all duration-300 transform -translate-x-full group-hover:translate-x-0" />
                        <div className="w-10 h-10 rounded-xl bg-white shadow-sm flex items-center justify-center border border-slate-100/50 ring-1 ring-slate-900/5 group-hover:shadow-md transition-all duration-300">
                            {Icon && <Icon className="w-5 h-5 text-indigo-600 transition-transform duration-300 group-hover:scale-110" />}
                        </div>
                        <h3 className="font-bold text-xl text-slate-800 tracking-tight">{title}</h3>
                    </div>
                    <div className="bg-white/60 backdrop-blur-md rounded-2xl p-6 border border-white/80 shadow-[0_2px_10px_-3px_rgba(6,81,237,0.1)] hover:shadow-[0_8px_30px_rgb(0,0,0,0.04)] transition-all duration-300 space-y-4 relative overflow-hidden">
                        <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-indigo-50/50 to-transparent rounded-bl-full pointer-events-none" />
                        {children}
                    </div>
                </div>
            </div>
        );
    };

    const Item = ({ label, value }) => {
        if (!value || (Array.isArray(value) && value.length === 0)) return null;
        return (
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 sm:gap-6 py-3 border-b border-slate-100 last:border-0 group/item hover:bg-slate-50/50 px-3 rounded-lg -mx-3 transition-colors duration-200">
                <div className="flex items-center gap-2 text-sm font-medium text-slate-500">
                    <span className="w-1 h-1 rounded-full bg-slate-300 group-hover/item:bg-indigo-400 transition-colors" />
                    {label}
                </div>
                <div className="text-sm text-slate-900 col-span-2 font-medium break-words leading-relaxed">
                    {value}
                </div>
            </div>
        );
    };

    const ArrayItem = ({ label, items, renderItem }) => {
        if (!items || items.length === 0) return null;
        return (
            <div className="py-4 border-b border-slate-100 last:border-0">
                <div className="flex items-center gap-2 mb-4 px-3">
                    <span className="w-1 h-1 rounded-full bg-indigo-400" />
                    <span className="text-sm font-semibold text-slate-700 tracking-wide uppercase">{label}</span>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 px-3">
                    {items.map((item, idx) => (
                        <div key={idx} className="group/card bg-white p-5 rounded-xl border border-slate-100 shadow-sm hover:shadow-lg hover:-translate-y-1 hover:border-indigo-100 transition-all duration-300 relative overflow-hidden">
                            <div className="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-transparent via-indigo-500 to-transparent opacity-0 group-hover/card:opacity-100 transition-opacity duration-300" />
                            {renderItem(item, idx)}
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    const AttachmentItem = ({ files }) => {
        if (!files) return null;
        const fileList = Array.isArray(files) ? files : [files];
        if (fileList.length === 0) return null;

        return (
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 sm:gap-6 py-4 border-t border-slate-100 mt-6 px-3">
                <span className="text-sm font-semibold text-slate-700 tracking-wide uppercase flex items-center gap-2">
                    <FileText className="w-4 h-4 text-indigo-500" /> Attachments
                </span>
                <div className="col-span-2 flex flex-wrap gap-3">
                    {fileList.map((file, idx) => (
                        <div key={idx} className="group relative flex items-center gap-3 bg-white px-4 py-2.5 rounded-xl border border-slate-200 shadow-sm hover:shadow-md hover:border-indigo-300 transition-all cursor-pointer">
                            <div className="absolute inset-0 bg-indigo-50/50 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity" />
                            <FileText className="w-4 h-4 text-indigo-500 relative z-10" />
                            <div className="flex flex-col relative z-10">
                                <span className="text-sm text-slate-700 font-medium truncate max-w-[180px]">{file.name}</span>
                                <span className="text-xs text-slate-400">{(file.size / 1024 / 1024).toFixed(2)} MB</span>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    return (
        <Card className="max-w-5xl mx-auto border-0 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.1)] rounded-[2rem] overflow-hidden bg-white/80 backdrop-blur-xl relative pb-24">
            {/* Ambient Background Effects */}
            <div className="absolute top-[-10%] left-[-10%] w-96 h-96 bg-blue-100/40 rounded-full blur-[100px] pointer-events-none" />
            <div className="absolute bottom-[-10%] right-[-10%] w-96 h-96 bg-orange-100/30 rounded-full blur-[100px] pointer-events-none" />

            <div className="relative z-10">
                {/* Premium Glass Header */}
                <div className="bg-slate-900 text-white relative overflow-hidden px-10 py-12 rounded-b-[2.5rem] shadow-xl">
                    <div className="absolute inset-0 bg-gradient-to-br from-indigo-600/20 via-slate-900 to-black/80 z-0" />
                    <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 brightness-100 contrast-150 z-0 mix-blend-overlay" />
                    <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-indigo-500/20 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/3 pointer-events-none" />
                    
                    <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6 pb-2 border-b border-white/10">
                        <div>
                            <div className="flex items-center gap-2 mb-3">
                                <span className="px-3 py-1 bg-white/10 rounded-full text-xs font-medium tracking-widest uppercase text-indigo-200 border border-white/10 backdrop-blur-sm">
                                    Official Document
                                </span>
                                <span className="px-3 py-1 bg-white/10 rounded-full text-xs font-medium tracking-widest uppercase text-orange-200 border border-white/10 backdrop-blur-sm">
                                    {data.requestType}
                                </span>
                            </div>
                            <h2 className="text-4xl sm:text-5xl font-extrabold tracking-tight flex items-center gap-4 text-white drop-shadow-lg">
                                Final Review
                                <div className="relative w-8 h-8 flex items-center justify-center bg-emerald-500/20 rounded-full">
                                    <CheckCircle2 className="w-6 h-6 text-emerald-400 relative z-10 animate-[bounce_2s_infinite]" />
                                    <div className="absolute inset-0 bg-emerald-400 rounded-full blur opacity-40 animate-ping" />
                                </div>
                            </h2>
                            <p className="text-slate-300 mt-4 text-lg font-light max-w-2xl leading-relaxed">
                                Please verify the accuracy of the information compiled below. Once confirmed, this document will be securely submitted to Human Resources for processing.
                            </p>
                        </div>
                        {/* Decorative Badge */}
                        <div className="hidden lg:flex flex-col items-end opacity-80">
                            <div className="w-16 h-16 rounded-2xl bg-white/10 border border-white/20 backdrop-blur-md flex items-center justify-center transform rotate-12 hover:rotate-0 transition-all duration-500">
                                <FileText className="w-8 h-8 text-white/80" />
                            </div>
                        </div>
                    </div>
                </div>

                <CardContent className="p-8 md:p-12 space-y-10 relative z-10">
                    {/* Requester Details */}
                    <Section title="Requester Profile" icon={User}>
                        <Item label="Full Name" value={data.requesterName} />
                        <Item label="Email Address" value={data.requesterEmail} />
                        <Item label="Phone Number" value={data.requesterPhone} />
                        <Item label="Classification" value={data.requestType} />
                    </Section>

                    {data.requestType === 'Bank Details' && (
                        <Section title="Banking Information" icon={Briefcase}>
                            <Item label="Banking Institution" value={data.bankName} />
                            <Item label="Branch / Location" value={data.branchLocation} />
                            <Item label="Branch Address" value={data.address} />
                            <Item label="Beneficiary Name" value={data.accountName} />
                            <Item label="Account Number" value={data.accountNo} />
                            <Item label="IBAN" value={<span className="font-mono text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded text-sm">{data.iban}</span>} />
                            <Item label="Swift Code" value={<span className="font-mono">{data.swiftCode}</span>} />
                            <Item label="Sort Code" value={<span className="font-mono">{data.sortCode}</span>} />
                            <Item label="Signature Date" value={data.signatureDate} />
                        </Section>
                    )}

                    {data.requestType === 'Personal Data' && (
                        <>
                            <Section title="Identity Information" icon={Info}>
                                <Item label="Title" value={data.title} />
                                <Item label="First Name" value={data.firstName} />
                                <Item label="Preferred Name" value={data.preferredName} />
                                <Item label="Surname" value={data.surname} />
                                <Item label="Other Surname" value={data.otherSurname} />
                                <Item label="Nationality" value={data.nationality} />
                                <Item label="Place of Birth" value={data.placeOfBirth} />
                                <Item label="Date of Birth" value={data.dateOfBirth} />
                                <Item label="Marital Status" value={<span className="px-3 py-1 bg-slate-100 rounded-full text-xs font-semibold">{data.maritalStatus}</span>} />
                                <Item label="Religion" value={data.religion} />
                            </Section>

                            <Section title="Contact Records" icon={Phone}>
                                <Item label="Personal Email" value={data.personalEmail} />
                                <Item label="Mobile Phone" value={data.mobilePhone} />
                                <Item label="Home Phone" value={data.homePhone} />
                                <Item label="Physical Address" value={data.physicalAddress} />
                                <Item label="Overseas Address" value={data.overseasAddress} />
                                <Item label="Overseas Phone" value={data.overseasHomePhone} />
                            </Section>

                            <Section title="Family Dependents" icon={Users}>
                                <Item label="Father's Name" value={data.fatherName} />
                                <Item label="Mother's Name" value={data.motherName} />
                                <Item label="Spouse's Name" value={data.spouseName} />
                                <Item label="Spouse Date of Birth" value={data.spouseDateOfBirth} />

                                <ArrayItem label="Children Details" items={data.children} renderItem={(item) => (
                                    <div className="flex flex-col gap-2">
                                        <div className="font-bold text-slate-800 text-lg flex items-center gap-2">
                                            {item.name}
                                        </div>
                                        <div className="flex items-center gap-4 text-sm text-slate-500 mt-2 bg-slate-50 p-3 rounded-lg border border-slate-100/50">
                                            {item.gender && <span className="flex flex-col"><span className="text-[10px] uppercase font-bold tracking-wider text-slate-400">Gender</span> <span className="font-medium text-slate-700">{item.gender}</span></span>}
                                            {item.gender && item.dateOfBirth && <div className="w-px h-8 bg-slate-200" />}
                                            {item.dateOfBirth && <span className="flex flex-col"><span className="text-[10px] uppercase font-bold tracking-wider text-slate-400">Date of Birth</span> <span className="font-medium text-slate-700">{item.dateOfBirth}</span></span>}
                                        </div>
                                    </div>
                                )} />
                            </Section>

                            <Section title="Education & Credentials" icon={GraduationCap}>
                                <ArrayItem label="Academic History" items={data.education} renderItem={(item) => (
                                    <div className="group/edu">
                                        <div className="font-extrabold text-slate-800 text-lg mb-1 leading-tight">{item.university}</div>
                                        <div className="font-semibold text-indigo-600 mb-4">{item.degreeType} {item.majorSubject && <span className="text-slate-500 font-medium">in {item.majorSubject}</span>}</div>
                                        {item.gradeGpa && (
                                            <div className="inline-flex mb-4 items-center bg-slate-100 px-3 py-1 rounded-full text-sm font-medium text-slate-600 group-hover/edu:bg-indigo-50 group-hover/edu:text-indigo-700 transition-colors">
                                                Grade/GPA: <strong className="ml-1 text-slate-900 group-hover/edu:text-indigo-900">{item.gradeGpa}</strong>
                                            </div>
                                        )}
                                        <div className="flex justify-between items-center text-xs text-slate-500 border-t border-slate-100/80 pt-4">
                                            <div className="flex items-center gap-2">
                                                <span className="font-mono bg-slate-50 px-2 py-0.5 rounded">{item.startDate}</span>
                                                <span>&rarr;</span>
                                                <span className="font-mono bg-slate-50 px-2 py-0.5 rounded">{item.endDate}</span>
                                            </div>
                                            <span className="text-slate-400">Class of {item.graduationDate}</span>
                                        </div>
                                    </div>
                                )} />

                                <ArrayItem label="Professional Qualifications" items={data.qualifications} renderItem={(item) => (
                                    <div>
                                        <div className="font-bold text-slate-800 text-lg mb-2">{item.description}</div>
                                        <div className="flex flex-col gap-2 text-sm">
                                            <div className="flex items-center gap-2 bg-slate-50 p-2 rounded border border-slate-100">
                                                <span className="text-slate-500">ID:</span>
                                                <span className="font-mono font-medium text-slate-700">{item.certificateNumber}</span>
                                            </div>
                                            <div className="text-slate-500 flex items-center gap-2 px-2">
                                                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                                                Issued: <span className="font-medium text-slate-700">{item.dateIssued}</span>
                                            </div>
                                        </div>
                                    </div>
                                )} />
                            </Section>

                            <Section title="Emergency Dispatch" icon={HeartPulse}>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 divide-y md:divide-y-0 md:divide-x divide-slate-100">
                                    <div className="space-y-4 md:pr-4">
                                        <h4 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 flex items-center gap-2">
                                            Primary Next of Kin
                                        </h4>
                                        <Item label="Name" value={data.nextOfKinName} />
                                        <Item label="Relation" value={data.nextOfKinRelationship} />
                                        <Item label="Address" value={data.nextOfKinAddress} />
                                        <Item label="Home" value={data.nextOfKinHomePhone} />
                                        <Item label="Mobile" value={data.nextOfKinMobilePhone} />
                                        <Item label="Work" value={data.nextOfKinWorkPhone} />
                                    </div>
                                    <div className="space-y-4 pt-8 md:pt-0 md:pl-4">
                                        <h4 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 flex items-center gap-2">
                                            Secondary Contact
                                        </h4>
                                        <Item label="Name" value={data.emergencyContactName} />
                                        <Item label="Relation" value={data.emergencyContactRelationship} />
                                        <Item label="Address" value={data.emergencyContactAddress} />
                                        <Item label="Home" value={data.emergencyContactHomePhone} />
                                        <Item label="Mobile" value={data.emergencyContactMobilePhone} />
                                        <Item label="Work" value={data.emergencyContactWorkPhone} />
                                    </div>
                                </div>
                            </Section>

                            <Section title="Professional Background" icon={Briefcase}>
                                <ArrayItem label="Language Capabilities" items={data.languageProficiency} renderItem={(item) => (
                                    <div className="flex flex-col gap-3">
                                        <div className="font-extrabold text-xl text-slate-800 tracking-tight">{item.language}</div>
                                        <div className="grid grid-cols-2 gap-4">
                                            <div className="bg-slate-50 p-3 rounded-lg border border-slate-100/50">
                                                <div className="text-[10px] uppercase font-bold tracking-wider text-slate-400 mb-1">Proficiency</div>
                                                <div className="font-medium text-slate-700">{item.skill}</div>
                                            </div>
                                            <div className="bg-slate-50 p-3 rounded-lg border border-slate-100/50">
                                                <div className="text-[10px] uppercase font-bold tracking-wider text-slate-400 mb-1">Level</div>
                                                <div className="font-medium text-slate-700">{item.level}</div>
                                            </div>
                                        </div>
                                    </div>
                                )} />

                                <div className="mt-8">
                                    <h4 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 px-3">Recent Employment</h4>
                                    <Item label="Company" value={data.previousCompany} />
                                    <Item label="Job Title" value={data.previousJobTitle} />
                                </div>
                                
                                {(data.hrDateOfHire || data.hrJobTitle || data.hrDepartment || data.hrOfficeLocation) && (
                                    <div className="mt-8 relative overflow-hidden rounded-2xl group/hr">
                                        <div className="absolute inset-0 bg-gradient-to-br from-slate-800 to-slate-900 z-0" />
                                        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-10 z-0 mix-blend-overlay" />
                                        <div className="relative z-10 p-6 md:p-8">
                                            <div className="flex items-center gap-3 mb-6 border-b border-white/10 pb-4">
                                                <div className="p-2 bg-white/10 rounded-lg backdrop-blur-sm shadow-inner break-words">
                                                    <Target className="w-5 h-5 text-indigo-300" />
                                                </div>
                                                <h4 className="text-sm font-bold text-white tracking-widest uppercase">Internal Use Only (HR)</h4>
                                            </div>
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-4">
                                                <div className="flex flex-col gap-1">
                                                    <span className="text-slate-400 text-xs uppercase font-semibold tracking-wider">Date of Hire</span>
                                                    <span className="text-white font-medium">{data.hrDateOfHire}</span>
                                                </div>
                                                <div className="flex flex-col gap-1">
                                                    <span className="text-slate-400 text-xs uppercase font-semibold tracking-wider">Job Title</span>
                                                    <span className="text-white font-medium">{data.hrJobTitle}</span>
                                                </div>
                                                <div className="flex flex-col gap-1">
                                                    <span className="text-slate-400 text-xs uppercase font-semibold tracking-wider">Department</span>
                                                    <span className="text-white font-medium">{data.hrDepartment}</span>
                                                </div>
                                                <div className="flex flex-col gap-1">
                                                    <span className="text-slate-400 text-xs uppercase font-semibold tracking-wider">Office Location</span>
                                                    <span className="text-white font-medium">{data.hrOfficeLocation}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )}
                            </Section>
                        </>
                    )}

                    <Section title="Supplementary Materials" icon={FileText}>
                        <Item label="Notes & Comments" value={
                            data.notes && (
                                <div className="bg-amber-50/50 border border-amber-100 p-4 rounded-xl text-slate-700 italic">
                                    "{data.notes}"
                                </div>
                            )
                        } />
                        <AttachmentItem files={data.attachment} />
                    </Section>
                </CardContent>

                {/* Error Banner */}
                {submitError && (
                    <div className="px-8 md:px-12 pb-6 relative z-10">
                        <div className="bg-red-50/80 backdrop-blur-sm border-l-4 border-red-500 text-red-800 p-5 rounded-xl flex items-start gap-4 shadow-sm animate-shake">
                            <AlertCircle className="w-6 h-6 flex-shrink-0 mt-0.5 text-red-500" />
                            <div>
                                <h4 className="font-bold text-base mb-1">Submission Failed</h4>
                                <span className="font-medium text-sm opacity-90">{submitError}</span>
                            </div>
                        </div>
                    </div>
                )}

                {/* Action Bar (Fixed at bottom inner, floating effect) */}
                <div className="absolute bottom-0 left-0 right-0 p-6 md:p-8 z-20">
                    <div className="bg-slate-900/90 backdrop-blur-xl border border-white/10 shadow-2xl rounded-2xl p-4 flex flex-col sm:flex-row justify-between items-center gap-4 transition-all hover:bg-slate-900/95">
                        <Button
                            variant="ghost"
                            onClick={onEdit}
                            disabled={isSubmitting}
                            className="w-full sm:w-auto text-slate-300 hover:text-white hover:bg-white/10 font-medium px-8 py-6 rounded-xl transition-all duration-300 group"
                        >
                            <Edit2 className="w-5 h-5 mr-3 transition-transform group-hover:-translate-x-1" />
                            Return to Edit
                        </Button>
                        <Button
                            onClick={onSubmit}
                            disabled={isSubmitting}
                            className="w-full sm:w-auto relative group overflow-hidden bg-white text-slate-900 hover:text-indigo-600 font-bold px-10 py-6 rounded-xl shadow-[0_0_40px_-10px_rgba(255,255,255,0.3)] hover:shadow-[0_0_60px_-15px_rgba(255,255,255,0.5)] transition-all duration-300 transform hover:-translate-y-1"
                        >
                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-indigo-100/50 to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
                            <div className="relative flex items-center justify-center text-lg">
                                {isSubmitting ? (
                                    <>
                                        <div className="w-5 h-5 border-2 border-slate-900/30 border-t-slate-900 rounded-full animate-spin mr-3" />
                                        Processing...
                                    </>
                                ) : (
                                    <>
                                        Confirm & Submit
                                        <Send className="w-5 h-5 ml-3 transition-transform duration-300 group-hover:translate-x-1 group-hover:-translate-y-1" />
                                    </>
                                )}
                            </div>
                        </Button>
                    </div>
                </div>
            </div>
        </Card>
    );
};


```