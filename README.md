# MedSecure Cloud Ltd. — Simulated ISO/IEC 27001:2022 ISMS Portfolio

**Portfolio status: educational simulation; documentation is not fully reconciled or approved.**

MedSecure Cloud Ltd. is a fictional Malta-based healthcare SaaS provider used for this independent learning project. The repository demonstrates selected ISMS documentation activities. It is not a client engagement, operational ISMS, certification assessment or professional audit delivery.

## Project contents currently published

- Company context and interested-party records
- Proposed ISMS scope
- Asset inventory with 25 sample assets
- Risk methodology and two risk-related CSV registers
- Risk treatment plan
- Starter Statement of Applicability covering 27 selected Annex A controls
- Draft information-security and access-control policies
- Evidence and access-review trackers
- Internal audit checklist and simulated findings
- Simulated NCR/CAPA register
- Draft management-review and audit-programme documents

## Important reconciliation warning

The files currently published in this repository are **not yet a single reconciled baseline**. The `04-Risk-Assessment/` directory currently contains the reconciliation log, methodology, and two risk CSVs; it does not contain a published risk-treatment-plan CSV:

| File | Current repository state | Required action |
|---|---|---|
| `Risk_Register.csv` | 20 risk records (R001–R020) | Reconcile with the latest working risk baseline before treating as canonical |
| `Risk_Assessment_Register.csv` | 10 different risk records (R001–R010); residual likelihood and impact are `Not Assessed`; existing controls are `To Validate` | Do not infer residual risk or control effectiveness |
| `Risk_Treatment_Plan.csv` | Not present in the published `04-Risk-Assessment/` directory at the time of review | Locate and publish the authoritative treatment-plan source only after confirming its contents and risk-ID references |
| `Statement_of_Applicability.csv` | 27 selected controls; statuses include `Planned` and `In Progress` | This is a starter selection, not the complete Annex A assessment |
| Evidence trackers | Multiple overlapping tracker formats | Select and document one canonical tracker after reconciliation |
| `Evidence_Register.csv` | Empty file | Removed as an empty placeholder; use the populated trackers pending consolidation |
| `NCR_CAPA_Register.csv` | 3 records marked `Open - Simulated` | Do not claim closure or effectiveness |

The latest working project notes describe a 23-risk canonical reconciliation, but that baseline is not present in this GitHub snapshot. Therefore, this repository's 20-row and 10-row risk files must not be presented as reconciled or final.

## Risk baseline reconciliation

See [`04-Risk-Assessment/RISK_BASELINE_RECONCILIATION.md`](04-Risk-Assessment/RISK_BASELINE_RECONCILIATION.md) for the known R003, R004, R005 and R021/R023 discrepancies, the safe handling rules, and the acceptance criteria for approving a single master register. The log deliberately does not select values or claim approval where the source records conflict.

## Risk methodology

The documented exercise uses a 1–5 likelihood scale and a 1–5 impact scale. The inherent score is calculated as likelihood multiplied by impact. Risk ratings and acceptance criteria remain subject to the methodology and approval process documented in the project.

Residual risk must not be invented. It should only be recorded after the proposed treatment has been assessed against evidence and the risk owner has reviewed the result. Until then, use `Not Assessed` rather than a guessed score.

## Audit and evidence status

The audit checklist and NCR/CAPA records are simulated learning artefacts. A finding marked `Needs Improvement` or `Open - Simulated` is not evidence of an actual organisational nonconformity. Proposed controls and evidence requirements do not prove implementation. Evidence that has not been collected or reviewed must remain clearly marked as such.

## Learning objectives demonstrated

- ISMS scope and organisational context
- Asset inventory and ownership
- Information-security risk assessment and treatment planning
- Statement of Applicability preparation
- Policy drafting
- Evidence-gap analysis
- Internal audit checklist design
- Simulated findings and corrective-action tracking
- Documentation quality and traceability

## Known limitations and next work

1. Locate and verify the authoritative treatment-plan source; do not describe an unpublished local file as part of the GitHub repository.\n2. Reconcile the latest local 23-risk baseline with the GitHub files; do not merge conflicting rows by assumption.
3. Resolve known risk mapping/score differences through documented decisions by the project author, not silent edits.
4. Connect each risk to its treatment, applicable controls, evidence requirements and any related simulated finding/CAPA.
5. Consolidate duplicate evidence trackers and remove obsolete backups only after comparing their contents.
6. Complete residual-risk assessments only when the treatment and supporting evidence justify them.
7. Review the selected controls and applicability justifications; do not describe the 27-control starter SoA as a complete Annex A review.
8. Keep approvals, control implementation and effectiveness clearly marked as pending unless evidence supports a change.

## Disclaimer

This is a fictional, educational portfolio exercise. It does not constitute ISO/IEC 27001 certification, legal advice, an independent audit, or evidence that a real organisation conforms to the standard. No real patient or customer data should be stored in this repository.
