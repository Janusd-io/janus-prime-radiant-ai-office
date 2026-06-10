---
type: source
title: IMS Process Visualization Standard
slug: diag-ims-visualization-standard
created: 2026-06-09
updated: 2026-06-09
source_type: document
source_origin: Google Drive — ISO/IMS department (Simon Tarskih)
document_id: DIAG-IMS-ProcessVisualizationStandard
document_version: v1.0
document_status: DRAFT
captured_by: jehad-altoutou
departments: [ai-office, ims-compliance]
related: [ims-digital-twin, iso-ims-puls, three-iso-standards, ims-enrolment, simon-tarskih]
ingested_in_full: true
---

> Full-fidelity ingest of the ISO/IMS source document `DIAG-IMS-ProcessVisualizationStandard v1.0` (DRAFT), received from Simon (IMS & Compliance) via Google Drive, 2026-06-09. Content preserved verbatim (pandoc/xlsx → markdown); not summarized.

**IMS Process Visualization Standard**

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Document ID</strong></td>
<td style="text-align: left;">DIAG-IMS-ProcessVisualizationStandard</td>
<td style="text-align: left;"><strong>Version</strong></td>
<td style="text-align: left;">v1.0</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Title</strong></td>
<td style="text-align: left;"><strong>IMS Process Visualization
Standard</strong></td>
<td style="text-align: left;"><strong>Status</strong></td>
<td style="text-align: left;"><strong>DRAFT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Date</strong></td>
<td style="text-align: left;">2026-06-05</td>
<td style="text-align: left;"><strong>Owner</strong></td>
<td style="text-align: left;">IMS / Compliance (1I)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>IMS Standards</strong></td>
<td colspan="3" style="text-align: left;">ISO 9001 cl. 4.4, ISO
5807</td>
</tr>
</tbody>
</table>

|                        |
|:-----------------------|
| **1. Purpose & Scope** |

This standard defines the visual notation, layout rules, and file
management requirements for all IMS process diagrams produced at Janus
Digital. It applies to every process map diagram created as part of the
IMS documentation set. Compliance ensures consistency, auditability, and
compatibility with the IMS digital twin environment.

|                        |
|:-----------------------|
| **2. Visual Elements** |

All diagrams must use the following symbols. No other shapes are
permitted without updating this standard.

|  |  |  |  |
|:---|:---|:---|:---|
| **Symbol Name** | **Shape Description** | **ISO 5807 / BPMN Ref** | **Usage** |
| **Start / End** | Oval (filled light grey) | ISO 5807 §4.4.1 | Process start and termination points — one Start, one or more End per diagram |
| **Activity** | Rectangle (white, dark border) | ISO 5807 §4.4.2 | Any process step or action performed by an actor |
| **Decision / Gate** | Diamond (white, dark border) | ISO 5807 §4.4.5 | Binary or multi-path decision point; label the condition; label each outgoing branch |
| **Document / Record** | Rectangle with wavy bottom (light yellow fill) | ISO 5807 §4.4.7 | Document or record created or updated at this step; label with document name and Form_ID |
| **Data Store** | Cylinder (light blue fill) | BPMN 2.0 §10.3.3 | Persistent data repository (registry, database, file store); label with system name and Source_ID |
| **Sub-process** | Rectangle with \[+\] marker at bottom centre (light grey fill) | BPMN 2.0 §10.3.5 | Step that triggers a defined separate process; label with Process Name and Process_ID |
| **Input / Output** | Parallelogram (light green fill) | ISO 5807 §4.4.6 | Data or artifact entering or leaving the process; label with name and Object_ID or Source_ID |
| **Message / Notification** | Rounded rectangle with envelope icon or envelope shape (light orange fill) | BPMN 2.0 §10.3.1 | Communication sent to an actor (Slack message, email, notification); label with channel and recipient |
| **Swimlane** | Vertical column with actor label at top (white background) | BPMN 2.0 §10.3.6 | Responsibility boundary for one actor; all activities in a lane are performed by that actor |
| **Annotation** | Dashed bracket with text (no fill) | ISO 5807 §4.4.9 | Supplementary note — ISO clause reference, §TBD marker, or important constraint |

**Color usage**

|  |  |  |  |
|:---|:---|:---|:---|
| **Element** | **Fill Color** | **Border Color** | **Notes** |
| **Main flow elements (Activity, Sub-process)** | White (#FFFFFF) | Dark grey (#333333) | Default for all activities |
| **Decision / Gate** | White (#FFFFFF) | Dark grey (#333333) | Label condition clearly |
| **Document / Record** | Light yellow (#FFF9E6) | Amber (#C8A800) | Highlights record creation/update events |
| **Data Store** | Light blue (#E1F0FA) | Blue (#0066CC) | Highlights data persistence |
| **Input / Output** | Light green (#E8F4E8) | Green (#339933) | Highlights data flow boundaries |
| **Message / Notification** | Light orange (#FFF0E6) | Orange (#CC6600) | Highlights communications |
| **Rejected / exception path** | Grey (#AAAAAA) | — | All arrows and elements on rejection branches |
| **Start / End** | Light grey (#F5F5F5) | Grey (#666666) | Neutral terminators |

> *Swimlane backgrounds: white. Actor label area: light grey (#F0F0F0).
> No decorative colors. All elements must be legible when printed in
> greyscale — shapes carry meaning, color is secondary.*

|                                      |
|:-------------------------------------|
| **3. Layout & Content Requirements** |

|  |  |
|:---|:---|
| **Rule** | **Specification** |
| **Page orientation** | Landscape (A3 preferred; A4 acceptable for simple processes ≤ 5 swimlanes and ≤ 10 steps) |
| **Flow direction** | Top-to-bottom within each swimlane column; swimlane columns ordered left to right by process sequence |
| **Swimlane structure** | Minimum 2 lanes; maximum 7 lanes; one lane per actor (Person, Department, System, or AI Agent); actor label at top of column |
| **Arrow style** | Solid line with filled arrowhead for main flow; dashed line for exception/rejection paths; label all Decision branches |
| **Spacing** | Minimum 20px between elements; minimum 40px between lanes; consistent element sizes within the same category |
| **Element sizing** | Activity: min 120×60px; Decision: min 80×80px; Document: min 100×60px; Start/End: min 60×40px |
| **Legend** | Required on every diagram — bottom-left corner; show all symbols used in the diagram with their names |
| **Sub-process** | Referenced by name and Process_ID; shown as a collapsed box — detail lives in a separate diagram file |

**Every diagram must include:**

|  |  |  |
|:---|:---|:---|
| **Element** | **Location** | **Content** |
| **Title block** | Top of diagram | Process Name, Process_ID, Version, Date, Status (DRAFT/APPROVED) |
| **Process Owner** | Title block | Role and Dept_ID |
| **Legend** | Bottom-left | All symbols used in this specific diagram |
| **ISO Reference** | Title block or annotation | Applicable ISO clause(s) |

|                        |
|:-----------------------|
| **4. File Management** |

|  |  |
|:---|:---|
| **Item** | **Specification** |
| **File naming** | DIAG-\[ProcessID\]-v\[version\]-\[YYYY-MM-DD\].\[ext\] — example: DIAG-PROC-AIToolEvaluation-v0.1-2026-06-05.drawio |
| **Primary format** | .drawio (editable source — always maintain) |
| **Export formats** | .svg (for embedding in documents); .pdf (for distribution); .png (for quick reference only) |
| **Storage location** | IMS Document Register (Appendix C) — Source_ID and Sub_Location per Data Sources Registry |
| **Versioning** | Increment version on any structural change; note changes in diagram title block |
| **Review cycle** | Reviewed whenever the associated process map document is reviewed |

