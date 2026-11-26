# MedSecure Cloud Ltd. — Simulated ISO/IEC 27001:2022 ISMS Portfolio

**Status: educational simulation; draft records; no management approval or certification claimed.**

MedSecure Cloud Ltd. is a fictional Malta-based healthcare SaaS provider. This independent portfolio demonstrates selected ISMS documentation and data-quality activities. It is not a real client engagement, operational ISMS, independent audit or certification assessment.

## Contents

- Company context, interested parties and legal/compliance register
- Proposed ISMS scope
- 27-row asset inventory
- Risk methodology and two separate risk datasets
- Risk treatment plan and a 27-control starter SoA
- Draft security policies
- Two evidence trackers, an access-review register and GRC evidence tracker
- Internal audit checklist/programme, simulated findings and open simulated CAPA
- Management-review draft
- Python data-quality validator and GitHub Actions workflow

## Important: two independent risk datasets

The repository contains two risk registers. They are **not one approved canonical risk baseline**. Repeated IDs R001–R010 do not mean the records describe the same scenario.

| Dataset | Records | Related records |
|---|---:|---|
| `04-Risk-Assessment/Risk_Assessment_Register.csv` | 10 assessed scenarios | Treatment plan, SoA related-risk references and GRC evidence tracker |
| `04-Risk-Assessment/Risk_Register.csv` | 20 asset-specific scenarios | Legacy evidence tracker |

The `Risk Register Source` column is included in the treatment plan, SoA and both evidence trackers to make their intended lineage explicit. The record-by-record comparison is in [Risk_Register_Crosswalk.csv](04-Risk-Assessment/Risk_Register_Crosswalk.csv). Read the [risk-baseline reconciliation log](04-Risk-Assessment/RISK_BASELINE_RECONCILIATION.md) before joining or changing records.

## Known open decisions

- The assessment-register R003 backup/restoration scenario and master-register R003 document-permission disclosure scenario are different risks on the same asset.
- Other repeated IDs also refer to different assets/events; see the crosswalk. Do not merge based on ID alone.
- R005 has a likelihood conflict (3 in the assessment register, 4 in the master register). Both values are preserved pending a documented owner decision.
- Master-register R018 (Vulnerability Assessment Reports) and R020 (Customer Support Tickets) are now mapped to newly added simulated assets A026 and A027. Their owners, classifications and locations are draft assumptions pending fictional project-owner review.
- Residual risk in the assessment register remains `Not Assessed`. Treatment actions remain `Not Started`; evidence remains pending/not collected as recorded.
- The SoA contains 27 selected controls. It is not a completed review of all 93 Annex A controls.
- Audit findings and CAPA records are simulated and remain open unless a record explicitly states otherwise. No closure or effectiveness is claimed.
- Policies, methodology, scope and management-review records remain drafts or pending approval where indicated.

## A026 case study — vulnerability report access and employee offboarding

This focused simulated case study follows a restricted information asset through access-control design, audit testing, finding documentation and corrective-action tracking.

**Scenario summary:** A hypothetical sample of 10 former employees contains 2 accounts that remained active for three days after departure. The scenario identifies delayed HR-to-IT departure notifications as the stated root cause and proposes a formal or automated offboarding workflow. A separate illustrative follow-up sample reports 10/10 timely revocations. These are constructed learning scenarios, not real test results or collected organizational evidence.

Related artifacts:

1. [A026 access-control procedure](07-Policies/A026_Vulnerability_Report_Access_Control_Procedure.md) — proposed procedure; draft and not approved or implemented.
2. [A026 internal audit test workpaper](09-Internal-Audit/A026_Internal_Audit_Test_Workpaper.md) — objective, scope, sample-based test method, illustrative exceptions, root cause, proposed corrective action and limitations.
3. [Internal audit checklist](09-Internal-Audit/Internal_Audit_Checklist.csv) — entry IA-016, linked to FIND-A026-01.
4. [NCR/CAPA register](10-NCR-CAPA/NCR_CAPA_Register.csv) — NCR-004, open and simulated.
5. [Audit-to-NCR cross-reference](10-NCR-CAPA/Audit_NCR_Cross_Reference.csv) — links IA-WP-A026-01 / FIND-A026-01 to NCR-004.

### A026 extension — evidence integrity and security logging

The case study was extended to examine whether audit evidence itself is protected, complete and recoverable. Three additional simulated findings are tracked: privileged log deletion without independent detection (NCR-005), missing-event detection failure (NCR-006), and unrecoverable events after a forwarding interruption (NCR-007).

Related artifacts:

1. [A026 evidence integrity and logging test matrix](09-Internal-Audit/A026_Evidence_Integrity_Test_Matrix.md) — test scenarios TC-01 to TC-08, illustrative outcomes, findings and evidence requirements.
2. [A026 corrective-action verification workpaper](09-Internal-Audit/A026_Corrective_Action_Verification_Workpaper.md) — proposed independent verification procedures for NCR-005, NCR-006 and NCR-007, including test steps, expected results, evidence requirements and closure conditions.
3. [NCR/CAPA register](10-NCR-CAPA/NCR_CAPA_Register.csv) — NCR-005 to NCR-007, all open and simulated.
4. [Audit-to-NCR cross-reference](10-NCR-CAPA/Audit_NCR_Cross_Reference.csv) — links the logging findings to their respective NCRs.

**Verification status:** The corrective-action verification workpaper is a test plan, not a record of completed testing. Its tests are marked pending. A proposed design, screenshot, management statement or configuration export alone does not establish operating effectiveness. Results should only be marked Pass after authorised testing and review of supporting evidence. The zero-unexplained-gap criterion in this case study is a proposed scenario acceptance criterion, not a universal numeric ISO requirement.

**Portfolio boundary:** The case study demonstrates documentation and reasoning only. It does not establish that the fictional controls were implemented, that a real audit occurred, or that corrective action was effective in an operating organization. All sample sizes, outcomes, timings and test results identified as illustrative are hypothetical.

## Run data-quality checks

From the repository root:

```bash
python scripts/validate_portfolio.py
```

GitHub Actions runs the same structural checks on pushes and pull requests to `master`. A passing workflow means only that the programmed data-quality checks passed. It does not approve risk ratings, prove control implementation, validate evidence effectiveness, or establish ISO conformity.

## Learning objectives

- ISMS context and scope documentation
- Asset inventory and ownership
- Risk assessment, evaluation and treatment traceability
- SoA preparation and control-evidence planning
- Evidence-gap analysis and access-review design
- Internal audit preparation and simulated corrective-action tracking
- Evidence integrity, audit-log completeness and recovery verification
- CSV validation and GitHub Actions automation

## Disclaimer

This is a fictional educational portfolio. It does not constitute ISO/IEC 27001 certification, legal advice, professional audit delivery, or evidence that a real organisation conforms to the standard. Do not upload real patient, customer, employee or secret data.


### A026 extension — approval-history integrity and emergency-access attribution

A further simulated finding, FIND-A026-LOG-04 / NCR-008, addresses privileged deletion of approval amendment history and the inability to reliably attribute a shared emergency-account action. The workpaper documents the evidence limitation, rejects unsupported attribution based only on a shift roster, defines individually attributable PAM-based emergency access and records a simulated closure recommendation after the constructed retest results.

- [FIND-A026-LOG-04 internal audit workpaper](09-Internal-Audit/FIND-A026-LOG-04_Internal_Audit_Workpaper.md) — investigation conclusion, attribution limitation, corrective-action approach, illustrative retest results, residual-risk decision and closure recommendation.
- [NCR-008 risk acceptance decision record](09-Internal-Audit/NCR-008_Risk_Acceptance_Decision_Record.md) — separate exercise variant where an executive accepts a remaining Critical residual risk; sets out authority checks, acceptance conditions and why acceptance alone does not establish finding closure.
- [Evidence Tracker](08-Control-Evidence/Evidence_Tracker.csv) — EV015, required evidence not collected / not reviewed.
- [NCR/CAPA register](10-NCR-CAPA/NCR_CAPA_Register.csv) — NCR-008, Open - Simulated.
- [Audit-to-NCR cross-reference](10-NCR-CAPA/Audit_NCR_Cross_Reference.csv) — IA-WP-A026-04 / FIND-A026-LOG-04 / NCR-008.

**Status limitation:** The workpaper's test results and management acceptance are hypothetical exercise assumptions. EV015 remains not collected and not reviewed; NCR-008 remains Open - Simulated in the portfolio register. The simulated closure recommendation is not a real closure or evidence of implemented controls.
