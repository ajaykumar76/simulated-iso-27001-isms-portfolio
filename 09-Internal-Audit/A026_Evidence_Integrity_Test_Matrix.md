# A026 Evidence Integrity and Logging Test Matrix

> **Simulation notice:** This is a fictional portfolio case study. All scenarios, test results, timestamps, sample outcomes and evidence references below are illustrative. No production system was accessed, no real control was tested, and no actual audit evidence was collected. This document is not proof of implementation, certification or a real internal audit.

## 1. Document control

| Field | Detail |
|---|---|
| Case | A026 — Vulnerability Assessment Reports / electronic backup-key return records |
| Document | Evidence Integrity and Logging Test Matrix |
| Version | 0.1 |
| Status | Draft — simulated |
| Proposed owner | Security Lead |
| Prepared for | Simulated ISO/IEC 27001 ISMS portfolio |
| Assessment approach | Design review and illustrative operating-effectiveness test scenarios |

## 2. Objective

Assess whether electronic records supporting A026 are protected against unauthorised alteration or deletion, attributable to identifiable users, forwarded to a separately administered logging platform, monitored for interruption and missing events, and recoverable after a logging interruption.

The matrix separates:
- **Design effectiveness:** whether the proposed control is appropriately designed.
- **Operating effectiveness:** whether the control operated as intended in the defined test.
- **Evidence sufficiency:** whether the result is supported by reliable, retained evidence.

A proposed control or a successful design walkthrough does not by itself demonstrate operating effectiveness.

## 3. Scope and illustrative criteria

In scope:
- Submitted electronic return and verification records.
- Amendments to submitted records.
- Privileged access to audit logs and forwarding configuration.
- Central log forwarding and interruption alerts.
- Detection of missing events and sequence gaps.
- Local buffering, recovery and reconciliation.
- Retention and retrieval of audit records.

Illustrative acceptance criteria for this case study:
1. Submitted records cannot be silently changed.
2. Any authorised amendment preserves the original value and records the new value, actor, timestamp, reason and approval.
3. Ordinary administrators cannot silently delete or alter protected audit logs.
4. Forwarding interruptions and missing critical events are detected and escalated.
5. Events generated during an interruption are retained and reconciled after recovery.
6. Privileged configuration changes are authorised, attributable and monitored.
7. Records remain retrievable for the approved retention period.

These are proposed case-study criteria, not universal numeric requirements prescribed by ISO/IEC 27001.

## 4. Test matrix

| Test ID | Objective and procedure | Expected result | Illustrative actual result | Status |
|---|---|---|---|---|
| TC-01 | Attempt to edit a submitted return record using an ordinary user account. | Edit is blocked; attempt is logged where required. | Ordinary-user edit blocked. | Pass — simulated |
| TC-02 | Submit a controlled amendment using an authorised amendment process. Inspect the audit history. | Original and revised values, actor, timestamp, reason and approval are retained. | Controlled amendment recorded with traceable history in the scenario. | Pass — simulated |
| TC-03 | Attempt audit-log deletion using a privileged administrator account. Inspect independent log storage and alerts. | Deletion is prevented or independently detected; protected copy remains available. | Privileged administrator successfully deletes audit logs without detection in the initial scenario. | **Fail — simulated** |
| TC-04 | Interrupt log forwarding and observe heartbeat monitoring and alert delivery. | Interruption is detected within the approved monitoring threshold and escalated to designated responders. | Heartbeat missed; alert generated at 14:02 and Security Lead notified at 14:03. | Pass — simulated |
| TC-05 | Deliberately remove a test event from the central log and inspect sequence-gap monitoring. | Missing event or sequence gap generates an alert and investigation record. | One event removed; no sequence-gap alert generated. | **Fail — simulated** |
| TC-06 | Compare locally buffered events with central records after forwarding resumes. Reconcile sequence numbers and event counts. | All in-scope events are accounted for; unexplained gaps are investigated and reported. | Independent comparison identifies the missing-event condition; no claim that the missing event was recovered. | Pass for comparison only — simulated |
| TC-07 | Attempt a privileged forwarding-configuration change and inspect approval and audit records. | Change requires independent authorisation and produces a protected, attributable audit event. | Not yet tested in this scenario. | Not tested |
| TC-08 | Retrieve retained records from a sample period and inspect retention, access and integrity safeguards. | Records are retrievable, protected and retained according to the approved schedule. | Not yet tested in this scenario. | Not tested |

## 5. Earlier simulated recovery scenario

An earlier illustrative interruption ran from 14:00 to 14:20. The monitoring alert worked, forwarding was restored and buffered events were delivered by 14:22. However, three minutes of audit events were missing and could not be recovered from local storage.

**Conclusion:** Interruption detection and restoration were demonstrated in that scenario, but log completeness and recovery failed. The later revised-design scenario must not be used to erase or conceal this earlier failure. Keep the two test iterations distinguishable.

## 6. Findings and corrective-action requirements

### FIND-A026-LOG-01 — Privileged audit-log deletion

- **Condition:** A privileged administrator could delete audit logs without independent detection.
- **Risk:** Loss or manipulation of audit evidence could impair incident investigation, accountability and detection of unauthorised activity.
- **Required action:** Restrict log administration; separate system administration from log custody; forward logs to separately administered immutable or tamper-evident storage; alert on deletion or integrity failures.
- **Retest:** Attempt deletion and alteration using ordinary and privileged test accounts; verify independent detection, retained copies and complete audit records.
- **Status:** Open — simulated.

### FIND-A026-LOG-02 — Missing-event detection failure

- **Condition:** A deliberately removed central audit event did not trigger a sequence-gap alert.
- **Risk:** Missing security events may remain undetected, reducing confidence in audit-log completeness.
- **Required action:** Correct sequence-gap or equivalent completeness monitoring; alert on missing events; define investigation, escalation and reconciliation responsibilities.
- **Retest:** Remove a controlled test event, verify alert generation and response, and reconcile the source and central records.
- **Status:** Open — simulated.

### FIND-A026-LOG-03 — Earlier recovery and buffering failure

- **Condition:** Three minutes of audit events were missing after an earlier forwarding interruption and could not be recovered from local storage.
- **Risk:** Critical activity during an outage may be unavailable for investigation.
- **Required action:** Validate encrypted local buffering, capacity, retry behaviour, sequence continuity, retention and recovery; define an escalation process for unrecoverable gaps.
- **Retest:** Simulate an interruption of defined duration and volume, restore forwarding, and reconcile every in-scope event.
- **Status:** Open — simulated.

## 7. Evidence register for future real testing

No evidence has been collected for this simulated case study. If this procedure is ever adapted for an authorised real audit, record actual evidence references here; do not substitute screenshots or statements that have not been independently verified.

| Evidence reference | Evidence required | Current status |
|---|---|---|
| A026-EI-01 | Role and permission export for record and log administration | Not collected |
| A026-EI-02 | Submitted-record amendment history showing old/new values, actor, time, reason and approval | Not collected |
| A026-EI-03 | Central log platform configuration and immutable-retention settings | Not collected |
| A026-EI-04 | Controlled privileged deletion/alteration test results and alert records | Not collected |
| A026-EI-05 | Forwarding interruption, heartbeat and notification timestamps | Not collected |
| A026-EI-06 | Source-to-central event reconciliation and sequence-gap test output | Not collected |
| A026-EI-07 | Local buffer, retry and recovery test records | Not collected |
| A026-EI-08 | Retention schedule and sample retrieval results | Not collected |
| A026-EI-09 | Corrective-action records and independent retest results | Not collected |

## 8. Overall simulated conclusion

The illustrative scenarios identify unresolved weaknesses in privileged audit-log protection, missing-event detection and recovery of events generated during a forwarding interruption. The logging and evidence-integrity controls cannot be concluded fully effective on the basis of these scenarios.

Keep the related simulated findings open until corrective actions are implemented in the fictional scenario and the defined retests pass with sufficient evidence. Any real audit conclusion would require authorised testing, actual records, a defined sample and an approved audit methodology.

## 9. Retest and closure rules

A finding should not be marked effective solely because a configuration change was made or management stated that the issue was fixed. The retest should:
1. Use a documented, authorised test procedure and controlled test accounts.
2. Preserve the original test conditions and expected outcomes.
3. Capture timestamped evidence and identify the tester.
4. Record exceptions without overwriting prior results.
5. Confirm that corrective actions address the identified cause.
6. Reassess residual risk and obtain acceptance only from the authorised risk-acceptance authority.
7. Update the relevant audit finding, NCR/CAPA and risk records consistently.

**End of simulated workpaper.**