#!/usr/bin/env python3
"""Validate structural consistency of the simulated MedSecure ISMS CSV records.

Run from the repository root:
    python scripts/validate_portfolio.py

This validator checks data quality only. It does not establish control operation,
risk acceptance, ISO/IEC 27001 conformity, or certification.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANDS = [
    (1, 4, "Low"),
    (5, 9, "Medium"),
    (10, 16, "High"),
    (17, 25, "Critical"),
]


def read_csv(relative_path: str) -> list[dict[str, str]]:
    path = ROOT / relative_path
    if not path.is_file():
        print(f"ERROR: missing file: {relative_path}")
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [row for row in csv.DictReader(handle) if any(v.strip() for v in row.values() if v)]


def band(score: int) -> str:
    for lower, upper, label in BANDS:
        if lower <= score <= upper:
            return label
    return "Invalid"


def ids(rows: list[dict[str, str]], key: str, label: str) -> set[str]:
    values = [row.get(key, "").strip() for row in rows]
    values = [value for value in values if value]
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        print(f"ERROR: duplicate {label}: {', '.join(duplicates)}")
    return set(values)


def main() -> int:
    errors = 0
    assets = read_csv("03-Asset-Inventory/Asset_Inventory.csv")
    master = read_csv("04-Risk-Assessment/Risk_Register.csv")
    assessment = read_csv("04-Risk-Assessment/Risk_Assessment_Register.csv")
    treatment = read_csv("05-Risk-Treatment/Risk_Treatment_Plan.csv")
    soa = read_csv("06-Statement-of-Applicability/Statement_of_Applicability.csv")
    evidence = read_csv("08-Control-Evidence/GRC_Evidence_Tracker.csv")
    master_evidence = read_csv("08-Control-Evidence/Evidence_Tracker.csv")
    crosswalk = read_csv("04-Risk-Assessment/Risk_Register_Crosswalk.csv")

    asset_ids = ids(assets, "Asset ID", "asset IDs")
    master_ids = ids(master, "Risk_ID", "master risk IDs")
    assessment_ids = ids(assessment, "Risk ID", "assessment risk IDs")
    treatment_ids = ids(treatment, "Risk ID", "treatment risk IDs")
    evidence_ids = ids(evidence, "Evidence ID", "evidence IDs")
    ids(master_evidence, "Evidence_ID", "master evidence IDs")
    ids(crosswalk, "Assessment_Register_ID", "crosswalk assessment IDs")

    if not master or not assessment or not treatment or not soa or not evidence or not master_evidence or not crosswalk:
        errors += 1

    for row in master:
        risk_id = row.get("Risk_ID", "").strip()
        asset_id = row.get("Asset_ID", "").strip()
        if asset_id == "TBD":
            print(f"WARNING: {risk_id}: asset mapping unresolved; do not infer an asset ID")
        elif asset_id and asset_id not in asset_ids:
            print(f"ERROR: {risk_id}: asset ID {asset_id} is not present in Asset_Inventory.csv")
            errors += 1
        try:
            likelihood = int(row["Likelihood"])
            impact = int(row["Impact"])
            score = int(row["Inherent_Score"])
            expected = likelihood * impact
            if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
                raise ValueError("likelihood/impact outside 1..5")
            if score != expected:
                print(f"ERROR: {risk_id}: score {score} != {likelihood} x {impact} ({expected})")
                errors += 1
            expected_band = band(score)
            if row.get("Inherent_Rating", "").strip() != expected_band:
                print(f"ERROR: {risk_id}: rating should be {expected_band}, got {row.get('Inherent_Rating')}")
                errors += 1
        except (KeyError, ValueError) as exc:
            print(f"ERROR: {risk_id or '(blank ID)'}: invalid master risk values ({exc})")
            errors += 1

    for row in assessment:
        risk_id = row.get("Risk ID", "").strip()
        try:
            likelihood = int(row["Likelihood"])
            impact = int(row["Impact"])
            score = int(row["Inherent Score"])
            if score != likelihood * impact:
                print(f"ERROR: assessment {risk_id}: score does not equal likelihood x impact")
                errors += 1
            expected_band = band(score)
            if row.get("Inherent Rating", "").strip() != expected_band:
                print(f"ERROR: assessment {risk_id}: rating should be {expected_band}")
                errors += 1
        except (KeyError, ValueError) as exc:
            print(f"ERROR: assessment {risk_id}: invalid values ({exc})")
            errors += 1

    for row in treatment:
        risk_id = row.get("Risk ID", "").strip()
        if row.get("Risk Register Source", "").strip() != "Risk_Assessment_Register.csv":
            print(f"ERROR: treatment {risk_id}: missing or incorrect source-register declaration")
            errors += 1
        if risk_id not in assessment_ids:
            print(f"WARNING: treatment {risk_id} has no matching assessment-register ID")
        if risk_id not in master_ids:
            print(f"WARNING: treatment {risk_id} has no matching master-register ID")

    for row in soa:
        if row.get("Risk Register Source", "").strip() != "Risk_Assessment_Register.csv":
            print(f"ERROR: SoA {row.get('Control ID')}: missing or incorrect source-register declaration")
            errors += 1
        raw = row.get("Related Risk IDs", "").strip()
        if not raw or raw.lower() == "all":
            continue
        for risk_id in (item.strip() for item in raw.split(";")):
            if risk_id and risk_id not in master_ids and risk_id not in assessment_ids:
                print(f"WARNING: SoA control {row.get('Control ID')} references unknown risk {risk_id}")

    for row in evidence:
        if row.get("Risk Register Source", "").strip() != "Risk_Assessment_Register.csv":
            print(f"ERROR: GRC evidence {row.get('Evidence ID')}: missing or incorrect source-register declaration")
            errors += 1
        risk_id = row.get("Related Risk ID", "").strip()
        if risk_id and risk_id not in master_ids and risk_id not in assessment_ids:
            print(f"WARNING: evidence {row.get('Evidence ID')} references unknown risk {risk_id}")

    for row in master_evidence:
        if row.get("Risk Register Source", "").strip() != "Risk_Register.csv":
            print(f"ERROR: legacy evidence {row.get('Evidence_ID')}: missing or incorrect source-register declaration")
            errors += 1
        risk_id = row.get("Related_Risk_ID", "").strip()
        if risk_id and risk_id not in master_ids:
            print(f"ERROR: legacy evidence {row.get('Evidence_ID')} references unknown master risk {risk_id}")
            errors += 1

    crosswalk_ids = {row.get("Assessment_Register_ID", "").strip() for row in crosswalk}
    if crosswalk_ids != assessment_ids:
        print("ERROR: crosswalk assessment IDs do not exactly cover the assessment register")
        errors += 1
    for row in crosswalk:
        if row.get("Master_Register_ID", "").strip() not in master_ids:
            print(f"ERROR: crosswalk row {row.get('Assessment_Register_ID')} references unknown master risk")
            errors += 1

    collisions = sorted(master_ids & assessment_ids)
    if collisions:
        print("WARNING: matching IDs across the two registers are not proof of matching scenarios.")
        print("WARNING: review the record-level crosswalk before joining treatment or evidence data.")

    print(f"Records: assets={len(assets)}, master={len(master)}, assessment={len(assessment)}, treatment={len(treatment)}, SoA={len(soa)}, GRC evidence={len(evidence)}, master evidence={len(master_evidence)}, crosswalk={len(crosswalk)}")
    print(f"Unique evidence IDs checked: {len(evidence_ids)}")
    print(f"Structural errors: {errors}")
    print("NOTE: warnings require human review; this script cannot decide whether risks are duplicates.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
