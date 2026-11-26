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
- Audit findings and CAPA records are simulated; three CAPA items remain `Open - Simulated`. No closure or effectiveness is claimed.
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

**Portfolio boundary:** The case study demonstrates documentation and reasoning only. It does not establish that the fictional controls were implemented, that a real audit occurred, or that corrective action was effective in an operating organization. Any follow-up effectiveness conclusion is limited to the hypothetical sample described in the workpaper.

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
- CSV validation and GitHub Actions automation

## Disclaimer

This is a fictional educational portfolio. It does not constitute ISO/IEC 27001 certification, legal advice, professional audit delivery, or evidence that a real organisation conforms to the standard. Do not upload real patient, customer, employee or secret data.
