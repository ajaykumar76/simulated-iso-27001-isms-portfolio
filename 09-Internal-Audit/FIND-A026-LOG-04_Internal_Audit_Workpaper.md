# FIND-A026-LOG-04 — Internal Audit and Corrective-Action Verification Workpaper

> **Simulation notice:** This is a fictional educational case study. The investigation facts, test results, sample sizes and management decisions below are constructed exercise data. No production system was accessed, no real administrator activity was investigated, and no corrective action was implemented or tested. This is not a real audit or certification assessment.

## 1. Document control

| Field | Detail |
|---|---|
| Workpaper ID | IA-WP-A026-04 |
| Finding | FIND-A026-LOG-04 — Privileged deletion of approval amendment history and inadequate emergency-session attribution |
| Related case | A026 — Evidence integrity, privileged access and security logging |
| Version | 0.1 |
| Status | Draft — simulated case conclusion |
| Related NCR | NCR-008 |
| Evidence tracker reference | EV015 |
| Proposed control owner | Logging / Platform Administrator |
| Proposed reviewer | Internal auditor independent of implementation |

## 2. Finding summary

The simulated investigation identified privileged deletion of approval amendment history. The investigation also exposed an emergency-access attribution weakness: a shared emergency account was used, network records identified a workstation available to three administrators, and no individual authentication or session record reliably identified the operator.

The shift roster was insufficient to attribute the action to one administrator. All three administrators denied performing it. The defensible conclusion was that the action occurred but the individual responsible could not be reliably established from available evidence.

**Risk:** Loss of approval accountability, reduced reliability of audit evidence, and inability to attribute privileged actions to an individual.

**Initial severity:** Critical in the illustrative scenario, based on the fictional approved matrix (likelihood 4 × impact 5 = 20/25). This rating is not a universal ISO rating.

## 3. Evidence assessment and attribution limitation

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Shared emergency account log | The shared account performed the recorded action | Which person operated the account |
| Network log | The workstation used for the action | Which of the three workstation users performed it |
| Shift roster | One administrator was scheduled | That the scheduled administrator performed the action |
| Administrator interviews | Each person's stated account of events | Independent proof of who performed the action |

**Conclusion:** Preserve the original records and explicitly document the attribution limitation. Do not assign the action to the scheduled administrator or another person without reliable corroborating evidence. Any later statement must be recorded with its actual entry time and must not overwrite or backdate the original record.

Management's request to name the scheduled administrator based on the roster alone is not supported by the evidence. The analyst should document the request and decline to make an unsupported attribution.

## 4. Root-cause and corrective-action approach

The simulated control weakness is that a shared emergency credential remained capable of direct use outside an individually attributable privileged-access workflow. The case does not establish malicious intent by any administrator.

Proposed corrective actions:

1. Block direct authentication using the shared emergency credential through an authorised and documented change.
2. Retain a controlled emergency-access capability through individually authenticated PAM checkout, named authorisation and time-limited access.
3. Enforce MFA for each authorised administrator and emergency-access checkout.
4. Record unique operator identity, session ID, start/end time, approval and actions in session records.
5. Protect session and approval-amendment records in independently administered, tamper-evident retention.
6. Automatically expire and revoke emergency access; alert independently on failed expiry or attempted bypass.
7. Review privileged-account inventory and remove or formally authorise undocumented accounts.

The organisation should not simply remove disaster-recovery access without an approved alternative. The objective is controlled and attributable emergency access.

## 5. Simulated verification results

The following results are exercise assumptions only; they are not actual test evidence.

| Test area | Illustrative result | Interpretation |
|---|---:|---|
| Five named administrator accounts and MFA | 5/5 passed | Tested accounts met the stated criteria |
| PAM checkout and named authorisation | 10/10 passed | Tested checkout scenarios passed |
| Session recording and individual attribution | 10/10 passed | Tested sessions were attributable |
| Automatic expiry and revocation | 10/10 passed | Tested expiry scenarios passed |
| Independent log retention | 10/10 passed | Tested retained records remained available |
| Direct login with old shared credential — initial retest | Failed | A bypass remained; closure was not justified |
| Direct shared-account login — post-remediation retest | 10/10 passed | Tested bypass attempts were blocked |
| Final MFA, PAM, attribution, retention and revocation retests | All stated tests passed | Defined scenario acceptance criteria were met |

A successful test demonstrates only the scenario and sample tested. It does not guarantee permanent effectiveness. The simulated final recommendation relies on the stated test scope, documented evidence review and ongoing monitoring.

## 6. Residual-risk assessment and closure recommendation

| Field | Simulated conclusion |
|---|---|
| Initial risk | 20/25 — Critical (illustrative matrix) |
| Residual risk | Medium under the fictional approved matrix |
| Risk acceptance | Signed and recorded by the authorised fictional management authority |
| Risk register | Updated to reflect treatment and residual risk |
| NCR cross-reference | Updated to link FIND-A026-LOG-04 to NCR-008 |
| Verification | Defined tests passed in the constructed scenario |
| Recommendation | Recommend closure, subject to authorised closure approval |

**Final recommendation:** Based on the constructed scenario results, recommend closure of NCR-008 because the defined corrective-action criteria have been met, the bypass was blocked and retested, individual attribution was demonstrated in the test sample, residual risk was reassessed and formally accepted, and the relevant records were updated. The authorised role—not the analyst acting alone—makes the closure decision.

**Ongoing monitoring:** Continue periodic privileged-access reviews, emergency-access expiry checks, session-attribution sampling, independent log-integrity checks and review of changes to PAM and retention configurations.

## 7. Closure checklist

- [x] Original evidence limitation documented without unsupported attribution.
- [x] Management pressure to infer identity rejected and recorded.
- [x] Proposed root-cause corrective actions defined.
- [x] Initial shared-account bypass failure recorded.
- [x] Post-remediation bypass test passed in the constructed scenario.
- [x] Defined MFA, PAM, attribution, retention and revocation tests passed in the constructed scenario.
- [x] Residual risk reassessed and authorised acceptance recorded in the scenario.
- [x] Risk register and NCR cross-reference updated in the scenario.
- [ ] Actual implementation and testing in a real environment — not performed; outside this simulation.

## 8. Related portfolio records

- [A026 Corrective Action Verification Workpaper](A026_Corrective_Action_Verification_Workpaper.md) — general verification method for NCR-005 to NCR-007.
- [Evidence Tracker](../08-Control-Evidence/Evidence_Tracker.csv) — EV015; required evidence remains not collected and not reviewed.
- [NCR/CAPA Register](../10-NCR-CAPA/NCR_CAPA_Register.csv) — NCR-008, simulated.
- [Audit NCR Cross-Reference](../10-NCR-CAPA/Audit_NCR_Cross_Reference.csv) — IA-WP-A026-04 / FIND-A026-LOG-04 / NCR-008.

**End of simulated workpaper.**
