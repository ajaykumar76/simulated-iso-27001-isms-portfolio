# Risk Baseline Reconciliation Log

**Status: open — no canonical risk baseline has been approved.**

This log prevents conflicting working copies from being silently combined. It is a simulated portfolio control, not evidence of management approval.

## Current published snapshot

- `Risk_Register.csv` contains 20 records (R001–R020).
- `Risk_Assessment_Register.csv` contains a separate 10-record set (R001–R010).
- The assessment register records residual likelihood and impact as `Not Assessed` and existing controls as `To Validate`.
- The latest project working notes describe a proposed 23-risk baseline. That baseline has not yet been published or approved.

Do not treat any one of these versions as the approved master register until the source records have been reconciled and the project owner has explicitly approved the baseline.

## Known decisions still required

| Item | Known discrepancy or proposal | Safe handling until resolved |
|---|---|---|
| R003 | Backup-related score appears as 20 (Critical) in one working version and 15 (High) in another | Preserve both source values; verify likelihood, impact and scoring rule before selecting one |
| R004 | May represent a distinct risk rather than a duplicate | Keep separate provisionally; compare asset, threat, vulnerability and event before merging |
| R005 | Likelihood appears as 3 in one version and 4 in another | Preserve both values; document the evidence and rationale for the selected rating |
| R021 / R023 | Proposed asset mappings involve A014 and A010 | Treat mappings as provisional; confirm each risk-to-asset relationship from source records |

The 23-risk working baseline is described in project notes as proposed and unapproved. No approval, risk-owner acceptance or final score is implied by this log.

## Reconciliation procedure

1. Freeze copies of all candidate registers; do not overwrite source versions during comparison.
2. Compare each record using risk ID, asset, threat, vulnerability, event/consequence, existing controls, likelihood, impact, score, owner and treatment.
3. Identify exact duplicates separately from risks that share an asset but describe different events.
4. Recalculate scores from the documented methodology; never resolve a conflict by choosing the higher or lower value without rationale.
5. Record every merge, split, ID change or field correction in a decision log with source version and reason.
6. Check every risk-to-asset, risk-to-treatment, risk-to-control and risk-to-evidence reference after reconciliation.
7. Obtain explicit simulated project-owner approval before labelling a register canonical.
8. Until approval, label the consolidated output **Draft — Pending Review** and keep residual risk as **Not Assessed** unless supported by completed treatment and evidence review.

## Publication acceptance criteria

- [ ] One version-controlled master risk register is identified.
- [ ] All 23 proposed records are accounted for, including documented duplicates or exclusions.
- [ ] R003, R004 and R005 discrepancies have evidence-based decisions.
- [ ] R021 and R023 asset mappings are confirmed or explicitly left unresolved.
- [ ] Inherent scores are recalculated consistently using the published methodology.
- [ ] Risk owners, treatment decisions and due dates are traceable.
- [ ] Residual ratings are not populated without treatment evidence and review.
- [ ] SoA, treatment plan, evidence tracker, audit findings and CAPA references are checked against the approved risk IDs.
- [ ] Approval status and date are recorded; otherwise the register remains draft.

## Scope and integrity note

All records in this repository belong to a fictional educational scenario. This log documents unresolved data-quality issues; it does not assert that the ISMS is implemented, audited, certified or approved.


## Record-level comparison of the two published registers

The following comparison is based on the two CSV files currently available on the repository's default branch. Matching IDs are **not** proof that the records refer to the same risk.

| ID | Risk_Register.csv | Risk_Assessment_Register.csv | Reconciliation result |
|---|---|---|---|
| R001 | Patient Database — unauthorised access; excessive privileges; 4×5=20 Critical | Patient Database — unauthorised access; access permissions may be excessive; 4×5=20 Critical | Same broad scenario; wording and control evidence still need review |
| R002 | Clinic Management Web Application — web exploitation; unpatched software; 4×5=20 Critical | Employee Accounts — credential theft; MFA may not be enforced; 4×4=16 High | Different assets and risk events; do not merge by ID |
| R003 | Patient Document Storage — data leakage; incorrect storage permissions; 3×5=15 High | Patient Document Storage — ransomware; backup restoration may be untested; 4×5=20 Critical | Same asset, different threat/event and score; likely separate risk scenarios unless source owner decides otherwise |
| R004 | Employee Laptops — device theft or malware; weak endpoint protection; 3×4=12 High | Clinic Management Web Application — web application attack; testing may be insufficient; 3×5=15 High | Different assets and risk events; do not merge by ID |
| R005 | Microsoft 365 Tenant — account compromise; weak authentication settings; 4×4=16 High | Microsoft 365 Tenant — account compromise; legacy authentication or weak settings; 3×4=12 High | Broadly aligned scenario; likelihood conflicts (4 vs 3); evidence-based decision required |
| R006 | Source Code Repository — unauthorised source-code access; excessive permissions; 3×4=12 High | Source Code Repository — source-code exposure; permissions or secrets handling may be weak; 3×4=12 High | Broadly aligned; confirm whether the vulnerability statement covers the same exposure |
| R007 | Network Firewall — network intrusion; incorrect firewall rules; 3×4=12 High | Employee Laptops — device loss or compromise; encryption/endpoint status unknown; 3×4=12 High | Different assets and risk events; do not merge by ID |
| R008 | Backup System — ransomware or backup deletion; insufficient isolation; 3×5=15 High | Security Event Logs — delayed incident detection; incomplete logging/alerting; 3×4=12 High | Different assets and risk events; do not merge by ID |
| R009 | Employee User Accounts — privilege misuse; delayed access removal; 3×4=12 High | Third-Party Supplier Register — supplier security failure; incomplete due diligence; 3×4=12 High | Different assets and risk events; do not merge by ID |
| R010 | Customer Portal — denial of service; insufficient resilience; 3×4=12 High | Production Environment — service disruption; untested disaster recovery; 3×5=15 High | Related availability theme, but different asset scope, event and score; do not merge without a documented decision |

### Confirmed structural findings from this comparison

1. The two registers share ten IDs but do not share a consistent ten-risk identity set.
2. At least six of the ten same-ID pairs describe different assets and/or different risk events (R002, R004, R007, R008, R009 and R010).
3. R003 describes two different risk scenarios on the same asset; it should not be treated as a simple score correction.
4. R005 has a direct likelihood conflict (3 versus 4), producing scores of 12 and 16 under the stated multiplication method.
5. R011–R020 appear only in the 20-row risk register; the assessment register has no corresponding records for them.
6. The repository tree confirms `05-Risk-Treatment/Risk_Treatment_Plan.csv` exists and contains ten actions (R001–R010). Its IDs align syntactically with the assessment register, but they cannot yet be assumed to align with the 20-row master register because several same-ID scenarios differ.

### Required correction sequence

- Preserve both source CSV files as source snapshots; do not overwrite either one yet.
- Create a crosswalk using the actual scenario fields, not the row IDs alone.
- Assign stable canonical IDs only after duplicate, split and distinct-risk decisions are recorded.
- Reconcile all 20 published risk-register records and all 10 assessment-register records against the proposed working baseline; account for every record.
- Confirm the treatment-plan file's actual repository path and validate its risk IDs before claiming traceability.
- Only then generate a draft consolidated register, label it **Draft — Pending Review**, and request simulated project-owner approval.

**No risk has been merged, deleted, renumbered, rescored or approved by this comparison.**


## Verified treatment-plan traceability finding

The published treatment plan contains ten rows, R001–R010. These identifiers mirror the assessment register, not necessarily the 20-row master risk register. Because same-numbered records can describe different assets and events, the treatment plan must remain linked to its originating assessment-register snapshot until a controlled crosswalk is approved. Do not copy or relabel treatment actions against the master register solely because the IDs match.

## Rating terminology correction

The master risk register uses the methodology's numeric thresholds. Two records previously used the label `Moderate` for scores of 8 and 9, while the methodology defines that band as `Medium` (5–9). The labels for R016 (8) and R018 (9) have been corrected to `Medium`. Treatment terminology in the master register has also been normalised from `Mitigate` to the methodology's `Modify` option. This is a terminology correction only; it does not mean any control has been implemented or any risk reduced.
