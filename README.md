# MedSecure Cloud Ltd. — Simulated ISO/IEC 27001:2022 ISMS Portfolio

**Status: educational simulation; draft records; no management approval or certification claimed.**

MedSecure Cloud Ltd. is a fictional Malta-based healthcare SaaS provider. This independent portfolio demonstrates selected ISMS documentation and data-quality activities. It is not a real client engagement, operational ISMS, independent audit or certification assessment.

## Contents

- Company context, interested parties and legal/compliance register
- Proposed ISMS scope
- 25-row asset inventory
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
- Master-register R018 (Vulnerability Assessment Reports) and R020 (Customer Support Tickets) have `TBD` asset IDs because the current asset inventory has no corresponding asset records. No substitute asset has been guessed.
- Residual risk in the assessment register remains `Not Assessed`. Treatment actions remain `Not Started`; evidence remains pending/not collected as recorded.
- The SoA contains 27 selected controls. It is not a completed review of all 93 Annex A controls.
- Audit findings and CAPA records are simulated; three CAPA items remain `Open - Simulated`. No closure or effectiveness is claimed.
- Policies, methodology, scope and management-review records remain drafts or pending approval where indicated.

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
