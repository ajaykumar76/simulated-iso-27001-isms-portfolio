# A026 Internal Audit Test Workpaper — Vulnerability Report Access and Offboarding

**Organization:** MedSecure Cloud Ltd. (fictional)  
**Workpaper ID:** IA-WP-A026-01  
**Version:** 0.1  
**Status:** Draft — Simulated Portfolio Exercise  
**Prepared by:** Portfolio author (simulated auditor)  
**Review / approval:** Not assigned; not approved  
**Related asset:** A026 — Vulnerability Assessment Reports  
**Classification:** Restricted (proposed classification)  
**Related procedure:** `07-Policies/A026_Vulnerability_Report_Access_Control_Procedure.md`  
**Related risk:** A026 access-control risk; confirm the applicable risk-register ID before formal cross-referencing  
**Related audit programme:** `09-Internal-Audit/Internal_Audit_Programme.txt`

> **Simulation notice:** MedSecure Cloud Ltd. is fictional. The samples, dates, results, interviews, logs and outcomes in this workpaper are illustrative scenario data created for learning. No real audit, employee sampling, system access, control operation, corrective action or evidence collection has taken place. Do not present this workpaper as proof of an actual audit or implemented control.

## 1. Audit objective

Assess, through an illustrative sample-based test, whether access to A026 vulnerability reports is revoked promptly when personnel leave the organization, and whether a proposed corrective action addresses the identified process weakness.

## 2. Scope and criteria

**Scope:** The simulated HR-to-IT employee-exit notification process and revocation of former employees' access to the repository containing A026 reports.

**Proposed test criterion:** Access should be revoked no later than the employee's final working time, with the revocation recorded and independently verified. This is a proposed portfolio criterion and would need authorization by the fictional organization's designated management before real testing.

**Reference documents:**
- Proposed A026 access-control procedure (draft, not approved or implemented).
- Draft internal audit programme (approval pending).
- Simulated HR departure records and IT account-revocation log entries described in this scenario.

## 3. Test method

1. Define the population of employee departures for the period under review.
2. Select a documented sample and record the selection method.
3. Compare each sampled employee's final working time with the corresponding IT access-revocation timestamp.
4. Identify exceptions and retain traceable evidence references.
5. Investigate the cause of each exception and assess potential access or data activity.
6. After corrective action, select a separate follow-up sample and repeat the comparison.
7. Record limitations and conclude only on the sample tested.

## 4. Initial test — illustrative scenario

| Field | Illustrative result |
|---|---|
| Sample size | 10 former employees |
| Exceptions | 2 accounts remained active for three days after departure |
| Exceptions in sample | 2/10 (20%) |
| Initial conclusion | Control failure identified in the illustrative sample |
| Finding reference | FIND-A026-01 (portfolio scenario reference) |

**Finding:** Two sampled former employees retained access to the A026 report repository for three days after departure.

**Risk:** Former employees could access Restricted vulnerability reports after their business need had ended. The scenario does not establish that either account was used to access, download or modify reports.

## 5. Root-cause analysis — illustrative scenario

**Identified root cause:** IT received employee departure notifications from HR three days late.

**Process weakness:** The employee-exit process did not reliably notify IT in time to revoke access by the required deadline.

This is the scenario's stated root cause. In a real audit, it would need to be supported by notification timestamps, interviews and process records rather than assumed.

## 6. Corrective action — proposed

| Field | Proposed action |
|---|---|
| Corrective action ID | CA-A026-01 |
| Action | Establish a formal or automated HR-to-IT offboarding notification workflow |
| Required elements | Defined trigger, accountable roles, notification deadline, access-revocation deadline, escalation path and verification |
| Responsible roles | HR Manager and IT Administrator; Security Lead to oversee the control |
| Verification | Compare HR departure records with IT revocation logs and verify removal of repository access |
| Status | Proposed in this simulated scenario; not implemented in a real organization |

## 7. Follow-up effectiveness test — illustrative scenario

A separate sample of 10 subsequent employee departures is described in the scenario after the proposed workflow is said to have been implemented.

| Field | Illustrative result |
|---|---|
| Follow-up sample | 10 employee departures |
| Accounts revoked by final working time | 10/10 |
| Exceptions in follow-up sample | 0/10 |
| Conclusion | Corrective action appears effective for this illustrative sample only |
| Ongoing monitoring | Required; this sample does not prove permanent or organization-wide effectiveness |

**Important limitation:** The 10/10 result is scenario data, not a real retest. A real effectiveness conclusion would require authentic HR records, IT logs, evidence references, sample selection details and an appropriately independent reviewer.

## 8. Evidence register

The following are evidence types to obtain in a real audit. They are not attached or claimed to have been collected for this portfolio exercise.

| Evidence reference | Evidence required | Current status |
|---|---|---|
| EV-A026-01 | HR-approved employee departure records | Not collected — simulated exercise |
| EV-A026-02 | HR-to-IT notification timestamps or workflow logs | Not collected — simulated exercise |
| EV-A026-03 | IT account and repository access-revocation logs | Not collected — simulated exercise |
| EV-A026-04 | Evidence of review for access after departure (where available) | Not collected — simulated exercise |
| EV-A026-05 | Corrective-action implementation and follow-up test records | Not collected — simulated exercise |

## 9. Workpaper conclusion

The illustrative initial sample identified two exceptions among ten records, and the scenario attributed them to delayed HR-to-IT notifications. The proposed corrective action addresses that stated process weakness. The illustrative follow-up sample had no exceptions, suggesting improvement within that sample.

**No real control effectiveness conclusion can be made from this portfolio scenario.** The workpaper remains a draft learning artifact. A real conclusion requires genuine source records, authorized testing, documented evidence, review and approval.

## 10. Reviewer sign-off

- Prepared by: Not signed — simulated portfolio exercise
- Reviewed by: Not assigned
- Review date: Pending
- Approval: Not applicable; draft only

## 11. Portfolio learning points

- Separate a control's design from evidence that it operated.
- Distinguish an observed condition from a validated root cause.
- Record sample size, exceptions, evidence references and test limitations.
- Do not extrapolate a sample exception rate to the full population without a defensible sampling basis.
- A successful follow-up sample supports a limited conclusion; it does not prove permanent effectiveness.
- Keep simulated records clearly labelled and never represent them as evidence from a real organization.
