# A026 Corrective Action Verification Workpaper

> **Simulation notice:** This is a fictional portfolio case study. NCRs, findings, test scenarios and identifiers are illustrative. No production environment was accessed, no real corrective action was implemented, and no actual audit evidence was collected. This workpaper does not demonstrate certification or a real audit.

## 1. Document control

| Field | Detail |
|---|---|
| Workpaper ID | IA-WP-A026-03 |
| Related case | A026 — Evidence Integrity and Logging |
| Version | 0.1 |
| Status | Draft — simulated; verification pending |
| Proposed verifier | Internal auditor independent of corrective-action implementation |
| Related NCRs | NCR-005, NCR-006, NCR-007 |
| Related findings | FIND-A026-LOG-01, FIND-A026-LOG-02, FIND-A026-LOG-03 |

## 2. Purpose and verification approach

This workpaper defines how an auditor would verify whether proposed corrective actions for three simulated A026 findings have been implemented and are operating effectively.

The verifier should distinguish:
- **Correction:** immediate action to address the detected condition.
- **Root-cause corrective action:** action intended to prevent recurrence.
- **Implementation evidence:** evidence that the action was completed.
- **Effectiveness evidence:** results demonstrating that the control works under defined test conditions.

A configuration screenshot or management confirmation alone is not sufficient to conclude operating effectiveness. The verifier should inspect relevant configuration, perform or witness authorised tests, examine resulting records and investigate exceptions.

## 3. Independence and test safeguards

Before testing:
1. Confirm written authorisation, scope, test accounts, systems and permitted test methods.
2. Use controlled test data and non-production environments where feasible.
3. Ensure the verifier is not the person who implemented the corrective action.
4. Agree test windows, rollback steps, incident contacts and evidence handling.
5. Preserve original evidence and record timestamps, tester identity and evidence references.
6. Do not delete production logs or disrupt live security monitoring to simulate a failure.

## 4. Verification plan — NCR-005: privileged audit-log protection

**Evidence tracker link:** EV012 — audit-log integrity and privileged access evidence. Keep the tracker status as Not collected / Not reviewed until supporting records are actually obtained and assessed.

**Finding:** A privileged administrator could delete audit logs without independent detection in the illustrative TC-03 scenario.

**Verification objective:** Determine whether privileged log deletion and alteration are prevented or independently detected, and whether protected records remain available.

| Test ID | Verification procedure | Expected result | Evidence to collect | Result |
|---|---|---|---|---|
| CA-005-01 | Inspect roles and permissions for system administration, log administration and retention management. | Least privilege and separation of duties are defined and approved. | Current role export, access approval and role design. | Pending |
| CA-005-02 | In an authorised test environment, attempt log deletion using an ordinary administrator test account. | Attempt is blocked or independently detected; protected copy remains intact. | Test record, source and central log samples, alert. | Pending |
| CA-005-03 | In an authorised test environment, attempt a privileged log deletion or alteration using the designated test role. | Action is prevented or produces an independent, tamper-evident record and alert; retained copy remains available. | Test account role, event record, alert and retained-copy comparison. | Pending |
| CA-005-04 | Inspect audit records for changes to logging, retention and administrator permissions. | Changes are attributable, time-stamped, authorised and monitored. | Configuration-change history and approvals. | Pending |
| CA-005-05 | Retrieve a sample of retained logs and compare integrity indicators or event counts with the protected copy. | Records are retrievable and no unexplained alteration or deletion is identified. | Retrieval output and comparison record. | Pending |

**Closure condition:** All critical tests pass, exceptions are resolved, and evidence supports the conclusion that privileged log deletion cannot occur silently. If a deletion action is technically possible but independently detected, assess whether the approved control objective permits detection as a compensating safeguard; document the risk and approval rather than assuming equivalence.

## 5. Verification plan — NCR-006: missing-event detection

**Evidence tracker link:** EV013 — log-forwarding and missing-event detection evidence. Keep the tracker status as Not collected / Not reviewed until supporting records are actually obtained and assessed.

**Finding:** A deliberately removed central audit event did not generate a sequence-gap alert in illustrative TC-05.

**Verification objective:** Determine whether missing critical events are detected, escalated and reconciled.

| Test ID | Verification procedure | Expected result | Evidence to collect | Result |
|---|---|---|---|---|
| CA-006-01 | Inspect event sequencing or completeness-monitoring design and configuration. | Critical event sources and detection logic are defined; monitoring failures are covered. | Approved design, source inventory and configuration export. | Pending |
| CA-006-02 | Generate a controlled test event and verify it reaches the central platform. | Event is received with expected source, timestamp and identifier. | Source event and central event record. | Pending |
| CA-006-03 | In an authorised test environment, omit or remove a controlled test event from the central stream. | Sequence gap or equivalent missing-event condition is detected. | Test event identifiers, monitoring output and alert. | Pending |
| CA-006-04 | Observe alert routing and response. | Alert reaches designated responders; acknowledgement, investigation and escalation are recorded within approved internal targets. | Alert timestamps, acknowledgement and incident/ticket record. | Pending |
| CA-006-05 | Reconcile source and central event records after the test. | All in-scope events are accounted for, or each gap is explicitly investigated and documented. | Reconciliation report and exception log. | Pending |

**Closure condition:** The controlled missing-event test generates an alert, the alert reaches the responsible person, response is recorded, and reconciliation identifies the event gap. A successful comparison in a different test does not compensate for a failed missing-event detection test.

## 6. Verification plan — NCR-007: log buffering and recovery

**Evidence tracker link:** EV014 — log-buffering and recovery-completeness evidence. Keep the tracker status as Not collected / Not reviewed until supporting records are actually obtained and assessed.

**Finding:** An earlier illustrative forwarding interruption resulted in three minutes of audit events missing from central records and unrecoverable from local storage.

**Verification objective:** Determine whether events generated during a defined forwarding interruption are retained locally, forwarded after recovery and reconciled without unexplained gaps.

| Test ID | Verification procedure | Expected result | Evidence to collect | Result |
|---|---|---|---|---|
| CA-007-01 | Inspect local buffer configuration, encryption, access controls, capacity and retention. | Buffer is protected and sized for the approved outage assumptions. | Configuration export, capacity assumptions and access list. | Pending |
| CA-007-02 | In an authorised test environment, interrupt forwarding for an agreed test period and generate controlled events. | Events are retained locally during the interruption. | Test timeline, source event list and buffer records. | Pending |
| CA-007-03 | Restore forwarding and observe automatic retry and delivery. | Buffered events are delivered without silent loss or duplication beyond defined handling rules. | Forwarding logs, delivery status and central records. | Pending |
| CA-007-04 | Reconcile source, local buffer and central records using event identifiers or sequence numbers. | Every in-scope event is accounted for; any gap is reported and investigated. | Three-way reconciliation report. | Pending |
| CA-007-05 | Test an outage exceeding the designed buffer capacity in a controlled environment or review a validated capacity test. | Capacity exhaustion is detected and escalated; defined fallback and evidence-preservation steps operate. | Capacity test, alert and response record. | Pending |

**Closure condition:** The test demonstrates retention, recovery and reconciliation for the approved outage and volume assumptions. No unexplained event gap remains. If an event cannot be recovered, document the limitation, assess potential impact and obtain an authorised risk decision; do not label the recovery control fully effective.

## 7. Verification result summary

| NCR | Required verification | Current status | Closure recommendation |
|---|---|---|---|
| NCR-005 | Privileged deletion prevention/detection and protected retention | Not tested | Do not close |
| NCR-006 | Missing-event detection, alert response and reconciliation | Not tested | Do not close |
| NCR-007 | Local buffering, recovery and event reconciliation | Not tested | Do not close |

All results are **Pending** because this is a proposed simulated verification plan. Do not change a result to Pass until a test has actually been performed in an authorised environment and supporting evidence has been reviewed.

## 8. Exception handling

For every failed or inconclusive test:
1. Record the exact test step, expected result and observed result.
2. Preserve source records, logs, screenshots or exports with timestamps and evidence references.
3. Assess whether the failure indicates a new issue, recurrence or incomplete corrective action.
4. Update the relevant NCR and corrective-action plan.
5. Assign an accountable owner and target date.
6. Retest after the action is completed.
7. Keep the NCR open until its defined closure criteria are met or an authorised disposition is documented.

Do not backdate records, overwrite failed results or treat management acceptance of residual risk as proof that the control is effective.

## 9. Final verification conclusion template

Complete this section only after authorised testing:

- NCR:
- Verification date:
- Verifier:
- Scope and sample:
- Evidence references:
- Tests passed:
- Tests failed or not tested:
- Exceptions and impact:
- Corrective action implementation confirmed:
- Operating effectiveness conclusion:
- Residual risk assessment and authorised decision:
- Recommendation: Close / Keep open / Further action required
- Reviewer approval and date:

## 10. Related portfolio records

- [A026 Evidence Integrity and Logging Test Matrix](A026_Evidence_Integrity_Test_Matrix.md)
- [Evidence Tracker](../08-Control-Evidence/Evidence_Tracker.csv) — EV012 (NCR-005), EV013 (NCR-006) and EV014 (NCR-007); all evidence remains not collected and not reviewed.
- [NCR/CAPA Register](../10-NCR-CAPA/NCR_CAPA_Register.csv) — NCR-005, NCR-006 and NCR-007.
- [Audit NCR Cross-Reference](../10-NCR-CAPA/Audit_NCR_Cross_Reference.csv) — IA-WP-A026-02 findings FIND-A026-LOG-01 to FIND-A026-LOG-03 mapped to NCR-005 to NCR-007.

**End of simulated verification workpaper.**
