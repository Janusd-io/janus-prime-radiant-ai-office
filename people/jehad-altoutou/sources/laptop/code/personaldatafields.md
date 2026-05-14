---
type: source
source_type: laptop
title: Desktop Captures — PersonalDataFields
slug: personaldatafields
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/form/sections/PersonalDataFields.jsx
original_size: 29357
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# PersonalDataFields

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/form/sections/PersonalDataFields.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { useFormContext, useFieldArray, Controller } from 'react-hook-form';
import { Input } from '../../ui/input';
import { Label } from '../../ui/label';
import { Select } from '../../ui/select';
import { SearchableSelect } from '../../ui/searchable-select';
import { Button } from '../../ui/button';
import { Card, CardContent } from '../../ui/card';
import { motion } from 'framer-motion';
import { Plus, Trash2 } from 'lucide-react';
import { NATIONALITIES } from '../../../lib/nationalities';
import { FileUpload } from '../FileUpload';

export const PersonalDataFields = () => {
    const { register, control, formState: { errors } } = useFormContext();

    const { fields: childFields, append: appendChild, remove: removeChild } = useFieldArray({
        control,
        name: "children"
    });

    const { fields: eduFields, append: appendEdu, remove: removeEdu } = useFieldArray({
        control,
        name: "education"
    });

    const { fields: qualFields, append: appendQual, remove: removeQual } = useFieldArray({
        control,
        name: "qualifications"
    });

    const { fields: langFields, append: appendLang, remove: removeLang } = useFieldArray({
        control,
        name: "languageProficiency"
    });

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="space-y-8"
        >
            <div className="flex items-center gap-2 mb-2">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Personal Information</h3>
            </div>
            
            <Card>
                <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div className="space-y-2">
                        <Label>Title</Label>
                        <Controller
                            control={control}
                            name="title"
                            render={({ field }) => (
                                <Select
                                    {...field}
                                    options={[
                                        { value: 'Mr', label: 'Mr' },
                                        { value: 'Miss', label: 'Miss' },
                                        { value: 'Mrs', label: 'Mrs' },
                                        { value: 'Other', label: 'Other' }
                                    ]}
                                    placeholder="Select Title"
                                />
                            )}
                        />
                    </div>
                    <div className="space-y-2">
                        <Label required>First Name</Label>
                        <Input {...register('firstName')} error={errors.firstName?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Preferred Name</Label>
                        <Input {...register('preferredName')} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Surname</Label>
                        <Input {...register('surname')} error={errors.surname?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Other Surname</Label>
                        <Input {...register('otherSurname')} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Nationality</Label>
                        <Controller
                            control={control}
                            name="nationality"
                            render={({ field }) => (
                                <SearchableSelect
                                    {...field}
                                    options={NATIONALITIES}
                                    placeholder="Search Nationality..."
                                    error={errors.nationality?.message}
                                />
                            )}
                        />
                    </div>
                    <div className="space-y-2">
                        <Label>Place of Birth</Label>
                        <Input {...register('placeOfBirth')} />
                    </div>
                    <div className="space-y-2 required">
                        <Label required>Date of Birth</Label>
                        <Input {...register('dateOfBirth')} placeholder="DD/MM/YY" error={errors.dateOfBirth?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Marital Status</Label>
                        <Controller
                            control={control}
                            name="maritalStatus"
                            render={({ field }) => (
                                <Select
                                    {...field}
                                    options={[
                                        { value: 'Single', label: 'Single' },
                                        { value: 'Married', label: 'Married' },
                                        { value: 'Other', label: 'Other' }
                                    ]}
                                    placeholder="Select Marital Status"
                                />
                            )}
                        />
                    </div>
                    <div className="space-y-2">
                        <Label>Religion</Label>
                        <Input {...register('religion')} />
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Contact Details</h3>
            </div>
            <Card>
                <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                        <Label required>Personal Email</Label>
                        <Input {...register('personalEmail')} type="email" error={errors.personalEmail?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Mobile Phone No</Label>
                        <Input {...register('mobilePhone')} error={errors.mobilePhone?.message} />
                    </div>
                    <div className="space-y-2 md:col-span-2">
                        <Label>Physical Local Address</Label>
                        <Input {...register('physicalAddress')} />
                    </div>
                    <div className="space-y-2">
                        <Label>Home Phone No</Label>
                        <Input {...register('homePhone')} />
                    </div>
                    <div className="space-y-2 md:col-span-2">
                        <Label>Overseas Address</Label>
                        <Input {...register('overseasAddress')} />
                    </div>
                    <div className="space-y-2">
                        <Label>Overseas Home Phone No</Label>
                        <Input {...register('overseasHomePhone')} />
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Family</h3>
            </div>
            <Card>
                <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                        <Label required>Father's Name</Label>
                        <Input {...register('fatherName')} error={errors.fatherName?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label required>Mother's Name</Label>
                        <Input {...register('motherName')} error={errors.motherName?.message} />
                    </div>
                    <div className="space-y-2">
                        <Label>Spouse's Name</Label>
                        <Input {...register('spouseName')} />
                    </div>
                    <div className="space-y-2">
                        <Label>Spouse's Date of Birth</Label>
                        <Input {...register('spouseDateOfBirth')} placeholder="DD/MM/YY" />
                    </div>
                    
                    <div className="col-span-1 md:col-span-2 space-y-4 pt-4">
                        <div className="flex justify-between items-center">
                            <Label className="text-lg font-medium text-gray-700">Children</Label>
                            <Button type="button" variant="outline" size="sm" onClick={() => appendChild({})}>
                                <Plus className="w-4 h-4 mr-2" /> Add Child
                            </Button>
                        </div>
                        {childFields.map((field, index) => (
                            <div key={field.id} className="grid grid-cols-1 md:grid-cols-4 gap-4 items-end p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div className="space-y-2 md:col-span-2">
                                    <Label>Child Name</Label>
                                    <Input {...register(`children.${index}.name`)} />
                                </div>
                                <div className="space-y-2">
                                    <Label>Gender (M/F)</Label>
                                    <Controller
                                        control={control}
                                        name={`children.${index}.gender`}
                                        render={({ field: selectField }) => (
                                            <Select
                                                {...selectField}
                                                options={[
                                                    { value: 'M', label: 'Male' },
                                                    { value: 'F', label: 'Female' }
                                                ]}
                                                placeholder="Gender"
                                            />
                                        )}
                                    />
                                </div>
                                <div className="space-y-2">
                                    <Label>Date of Birth</Label>
                                    <Input {...register(`children.${index}.dateOfBirth`)} placeholder="DD/MM/YY" />
                                </div>
                                <Button type="button" variant="ghost" className="text-red-500 md:col-span-4 self-center mt-2" onClick={() => removeChild(index)}>
                                    <Trash2 className="w-4 h-4 mr-2" /> Remove
                                </Button>
                            </div>
                        ))}
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Education & Qualifications</h3>
            </div>
            <Card>
                <CardContent className="pt-6 space-y-6">
                    <div className="space-y-4">
                        <div className="flex justify-between items-center">
                            <Label className="text-lg font-medium text-gray-700">University/College</Label>
                            <Button type="button" variant="outline" size="sm" onClick={() => appendEdu({})}>
                                <Plus className="w-4 h-4 mr-2" /> Add Education
                            </Button>
                        </div>
                        {eduFields.map((field, index) => (
                            <div key={field.id} className="grid grid-cols-1 md:grid-cols-3 gap-5 items-end p-5 bg-white shadow-sm rounded-lg border border-gray-200">
                                <div className="space-y-4 md:col-span-3">
                                    <div className="pb-2 border-b border-gray-100 flex items-center justify-between">
                                        <Label className="text-janus-blue-900 font-semibold text-base">Institution Details</Label>
                                        <Button type="button" variant="ghost" className="text-red-500 hover:text-red-600 hover:bg-red-50 h-8 px-2" onClick={() => removeEdu(index)}>
                                            <Trash2 className="w-4 h-4 mr-2" /> Remove Entry
                                        </Button>
                                    </div>
                                    <div className="space-y-2">
                                        <Label>Institution / University Name</Label>
                                        <Input {...register(`education.${index}.university`)} placeholder="e.g. Oxford University" />
                                    </div>
                                </div>
                                
                                <div className="space-y-2">
                                    <Label>Start Date</Label>
                                    <Input {...register(`education.${index}.startDate`)} placeholder="DD/MM/YYYY" />
                                </div>
                                <div className="space-y-2">
                                    <Label>End Date</Label>
                                    <Input {...register(`education.${index}.endDate`)} placeholder="DD/MM/YYYY" />
                                </div>
                                <div className="space-y-2">
                                    <Label>Graduation Date</Label>
                                    <Input {...register(`education.${index}.graduationDate`)} placeholder="DD/MM/YYYY" />
                                </div>

                                <div className="space-y-2 md:col-span-3 pb-2 border-b border-gray-100 mt-2">
                                    <Label className="text-janus-blue-900 font-semibold text-base">Degree Information</Label>
                                </div>
                                
                                <div className="space-y-2">
                                    <Label>Degree Type</Label>
                                    <Input {...register(`education.${index}.degreeType`)} placeholder="e.g. Bachelor of Science" />
                                </div>
                                <div className="space-y-2">
                                    <Label>Major / Subject</Label>
                                    <Input {...register(`education.${index}.majorSubject`)} placeholder="e.g. Computer Engineering" />
                                </div>
                                <div className="space-y-2">
                                    <Label>Grade / CGPA</Label>
                                    <Input {...register(`education.${index}.gradeGpa`)} placeholder="e.g. 3.8 / First Class" />
                                </div>
                            </div>
                        ))}
                    </div>

                    <div className="space-y-4 pt-4 border-t border-gray-100">
                        <div className="flex justify-between items-center">
                            <Label className="text-lg font-medium text-gray-700">Professional Qualifications</Label>
                            <Button type="button" variant="outline" size="sm" onClick={() => appendQual({})}>
                                <Plus className="w-4 h-4 mr-2" /> Add Qualification
                            </Button>
                        </div>
                        {qualFields.map((field, index) => (
                            <div key={field.id} className="grid grid-cols-1 md:grid-cols-3 gap-4 items-end p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div className="space-y-2">
                                    <Label>Description</Label>
                                    <Input {...register(`qualifications.${index}.description`)} />
                                </div>
                                <div className="space-y-2">
                                    <Label>Certificate Number</Label>
                                    <Input {...register(`qualifications.${index}.certificateNumber`)} />
                                </div>
                                <div className="space-y-2">
                                    <Label>Date Issued</Label>
                                    <Input {...register(`qualifications.${index}.dateIssued`)} placeholder="DD/MM/YY" />
                                </div>
                                <Button type="button" variant="ghost" className="text-red-500 md:col-span-3 mt-2" onClick={() => removeQual(index)}>
                                    <Trash2 className="w-4 h-4 mr-2" /> Remove
                                </Button>
                            </div>
                        ))}
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Emergency Contacts</h3>
            </div>
            <Card>
                <CardContent className="pt-6 space-y-6">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="md:col-span-2 pb-2 border-b">
                            <h4 className="font-medium text-gray-800">Next of Kin</h4>
                        </div>
                        <div className="space-y-2">
                            <Label>Name</Label>
                            <Input {...register('nextOfKinName')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Relationship</Label>
                            <Input {...register('nextOfKinRelationship')} />
                        </div>
                        <div className="space-y-2 md:col-span-2">
                            <Label>Address</Label>
                            <Input {...register('nextOfKinAddress')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Home Phone</Label>
                            <Input {...register('nextOfKinHomePhone')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Mobile Phone</Label>
                            <Input {...register('nextOfKinMobilePhone')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Work Phone</Label>
                            <Input {...register('nextOfKinWorkPhone')} />
                        </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4">
                        <div className="md:col-span-2 pb-2 border-b">
                            <h4 className="font-medium text-gray-800">Emergency Contact (If different)</h4>
                        </div>
                        <div className="space-y-2">
                            <Label>Name</Label>
                            <Input {...register('emergencyContactName')} error={errors.emergencyContactName?.message} />
                        </div>
                        <div className="space-y-2">
                            <Label>Relationship</Label>
                            <Input {...register('emergencyContactRelationship')} />
                        </div>
                        <div className="space-y-2 md:col-span-2">
                            <Label>Address</Label>
                            <Input {...register('emergencyContactAddress')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Home Phone</Label>
                            <Input {...register('emergencyContactHomePhone')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Mobile Phone</Label>
                            <Input {...register('emergencyContactMobilePhone')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Work Phone</Label>
                            <Input {...register('emergencyContactWorkPhone')} />
                        </div>
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Language Proficiency & Employment</h3>
            </div>
            <Card>
                <CardContent className="pt-6 space-y-6">
                    <div className="space-y-4">
                        <div className="flex justify-between items-center">
                            <Label className="text-lg font-medium text-gray-700">Languages</Label>
                            <Button type="button" variant="outline" size="sm" onClick={() => appendLang({})}>
                                <Plus className="w-4 h-4 mr-2" /> Add Language
                            </Button>
                        </div>
                        {langFields.map((field, index) => (
                            <div key={field.id} className="grid grid-cols-1 md:grid-cols-3 gap-4 items-end p-4 bg-gray-50 rounded-lg border border-gray-100">
                                <div className="space-y-2">
                                    <Label>Language</Label>
                                    <Input {...register(`languageProficiency.${index}.language`)} />
                                </div>
                                <div className="space-y-2">
                                    <Label>Skill</Label>
                                    <Controller
                                        control={control}
                                        name={`languageProficiency.${index}.skill`}
                                        render={({ field: skillField }) => (
                                            <Select
                                                {...skillField}
                                                options={[
                                                    { value: 'Spoken & Written', label: 'Spoken & Written' },
                                                    { value: 'Spoken Only', label: 'Spoken Only' },
                                                    { value: 'Written Only', label: 'Written Only' },
                                                    { value: 'Reading Only', label: 'Reading Only' }
                                                ]}
                                                placeholder="Skill"
                                            />
                                        )}
                                    />
                                </div>
                                <div className="space-y-2">
                                    <Label>Level</Label>
                                    <Controller
                                        control={control}
                                        name={`languageProficiency.${index}.level`}
                                        render={({ field: levelField }) => (
                                            <Select
                                                {...levelField}
                                                options={[
                                                    { value: 'Native / Bilingual', label: 'Native / Bilingual' },
                                                    { value: 'Advanced / Professional', label: 'Advanced / Professional' },
                                                    { value: 'Intermediate', label: 'Intermediate' },
                                                    { value: 'Beginner / Basic', label: 'Beginner / Basic' }
                                                ]}
                                                placeholder="Level"
                                            />
                                        )}
                                    />
                                </div>
                                <Button type="button" variant="ghost" className="text-red-500 md:col-span-3 mt-2" onClick={() => removeLang(index)}>
                                    <Trash2 className="w-4 h-4 mr-2" /> Remove
                                </Button>
                            </div>
                        ))}
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4 border-t border-gray-100">
                        <div className="md:col-span-2 pb-2">
                            <h4 className="font-medium text-gray-800">Last Previous Employment</h4>
                        </div>
                        <div className="space-y-2">
                            <Label>Company Name</Label>
                            <Input {...register('previousCompany')} />
                        </div>
                        <div className="space-y-2">
                            <Label>Job Title</Label>
                            <Input {...register('previousJobTitle')} />
                        </div>
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-janus-orange-500 rounded-full" />
                <h3 className="text-xl font-semibold text-janus-blue-900">Attachments</h3>
            </div>
            <Card>
                <CardContent className="pt-6">
                    <p className="text-sm text-gray-600 border-l-4 border-janus-orange-500 pl-3 mb-6 bg-janus-orange-50/50 p-3 rounded-r-lg">
                        Please upload required documents including: <strong>Passport copy, University Degree, and Passport-size Personal Picture (white background).</strong><br/>
                        <span className="inline-block mt-2 font-semibold text-janus-orange-600">NOTE: all documents should be in jpeg format and under 1mb size.</span>
                    </p>
                    <div className="space-y-4">
                        <Controller
                            control={control}
                            name="attachment"
                            render={({ field }) => (
                                <FileUpload
                                    label="Upload Documents"
                                    multiple={true}
                                    value={field.value}
                                    onChange={field.onChange}
                                    error={errors.attachment?.message}
                                />
                            )}
                        />
                    </div>
                </CardContent>
            </Card>

            <div className="flex items-center gap-2 mb-2 pt-4">
                <div className="h-8 w-1 bg-gray-400 rounded-full" />
                <h3 className="text-xl font-semibold text-gray-600">Firm Information (HR Use Only)</h3>
            </div>
            <Card className="bg-gray-50 border-dashed border-2">
                <CardContent className="pt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                        <Label>Date of Hire</Label>
                        <Input {...register('hrDateOfHire')} placeholder="DD/MM/YY" />
                    </div>
                    <div className="space-y-2">
                        <Label>Job Title</Label>
                        <Input {...register('hrJobTitle')} />
                    </div>
                    <div className="space-y-2">
                        <Label>Department</Label>
                        <Input {...register('hrDepartment')} />
                    </div>
                    <div className="space-y-2">
                        <Label>Office Location</Label>
                        <Input {...register('hrOfficeLocation')} />
                    </div>
                </CardContent>
            </Card>
        </motion.div>
    );
};

```