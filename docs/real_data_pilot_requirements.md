# Real-Data Pilot Requirements

This document outlines the strict prerequisites for executing the Phase 9 Empirical Model Validation. The system infrastructure is completely prepared, but real-world Oil & Gas (O&G) safety data must be supplied to proceed.

## 1. Required Dataset Format
- **Acceptable Formats:** CSV, JSON, or XLSX.
- **Ingestion Mapping:** The dataset will be processed via `src/data/ingestor.py` which can map arbitrary column names to the expected schema.

## 2. Required Fields
- **Unique Identifier:** e.g., `report_id` or `incident_id` (mandatory for leakage-safe splitting).
- **Report Text:** e.g., `description`, `incident_summary` (mandatory).
- **Report Type:** e.g., Unsafe Act, Unsafe Condition, Near Miss, Incident (highly recommended).
- **Metadata (Optional):** Location, equipment, date/time, department (useful for drift analysis and temporal splitting).

## 3. Sample Size Requirements
- **Minimum:** 1,000 distinct records.
- **Recommended:** 5,000+ distinct records to ensure adequate representation of the minority class (SIF precursors).
- **Imbalance Consideration:** O&G safety data typically has a 95:5 (Non-SIF:SIF) imbalance. At least 100 positive SIF examples are required for statistically significant PR-AUC evaluation.

## 4. Annotation Guidelines & Workflow
- **Guideline:** Annotators must strictly follow `docs/annotation_schema.md`.
- **Labels:** Multi-label SIF precursor categories (e.g., `fall_protection_failure`, `energy_isolation_failure`).
- **Two-Annotator Workflow:** 
  1. A random 10% sample (min 100 records) must be annotated by two independent HSE professionals.
  2. The system will calculate **Cohen's Kappa** using `src/analytics/iaa_calculator.py`.
  3. **Gate:** Cohen's Kappa MUST be ≥ 0.75 before proceeding to large-scale annotation.
  4. Conflicts must be adjudicated by a third Senior HSE Lead.

## 5. Privacy & Leakage Prevention
- **PII Scrubbing:** The automated `src/data/cleaner.py` scrub will remove generic emails, phones, and IDs. However, the client should ensure the dataset does not contain highly sensitive legal names or medical information.
- **Leakage Prevention:** If duplicate reports exist for a single event, the `incident_id` MUST be provided to enable `GroupShuffleSplit`.

## 6. Evaluation Requirements
- **Primary Metric:** Precision-Recall AUC (PR-AUC) and False Negative Analysis.
- **Acceptance Criteria:** 
  - The model must demonstrate an ability to detect linguistic variations not present in the synthetic baseline without overwhelming False Positives.
  - A strict False Negative Audit (documenting exactly *why* a true SIF precursor was missed) must be completed for every missed record in the validation set.

## 7. Model Evaluation Pipeline
Once the data is ingested, the system will automatically execute:
1. Baseline calculation using the existing Hybrid NLP + TF-IDF model.
2. Threshold optimization on the Validation Set.
3. Final evaluation on the strictly sequestered Test Set.
