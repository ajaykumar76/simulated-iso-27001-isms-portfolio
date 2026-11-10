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
