# AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in OIL's Unsafe-Act / Unsafe-Condition and Near-Miss Reports

## 🚦 Current Status
🟡 **READY WITH CONDITIONS**

* **Software Architecture:** READY
* **Pipeline Integration:** VERIFIED
* **Adversarial Testing:** COMPLETED
* **Real-Data Ingestion:** READY
* **Real-Data Annotation:** READY
* **Real-Data Evaluation:** READY
* **Real-World ML Validation:** BLOCKED BY DATA AVAILABILITY
* **Current Model:** SYNTHETIC BASELINE

> **The project is now frozen as a V1 candidate.** The software infrastructure is ready for controlled real-world evaluation, but the predictive model remains **UNVALIDATED ON REPRESENTATIVE REAL-WORLD O&G DATA.**

## ⚠️ Critical Issues & Bug Register

| ID | Severity | Issue | Location | Current Status | Impact | Required Action |
|---|---|---|---|---|---|---|
| 1 | 🔴 CRITICAL | Unvalidated Model | `src/models/` | BLOCKED | No representative real-world O&G validation exists. | Wait for legitimate real data. |
| 2 | 🟠 HIGH | Semantic NLP Misses | `src/nlp/` | BLOCKED | Unseen hazard wording can bypass vocabulary extraction (e.g. "The safety belt snapped"). | Requires semantic embeddings upon real data arrival. |
| 3 | 🟠 HIGH | Potential LOW + No Human Review | `src/models/inference.py` | BLOCKED | If NLP misses an unseen hazard and the ML model scores it < 0.4 (LOW), the fallback will not trigger. | Calibrate thresholds/upgrade model on real data. |
| 4 | 🟡 MEDIUM | Confidence Calibration | `src/models/inference.py` | BLOCKED | Probabilities are not empirically calibrated. | Calibrate on annotated O&G dataset. |
| 5 | 🟡 MEDIUM | Rule-Based NLP Brittleness | `src/nlp/feature_extraction.py` | BLOCKED | Hypothetical, historical, contextual, and semantically equivalent statements may behave incorrectly. | Needs real-world variation validation. |
| 6 | 🟡 MEDIUM | Regex-Only PII Limitations | `src/data/cleaner.py` | OPEN | Contextual human names remain undetected. | Use NER models if required by privacy policies. |
| 7 | 🟡 MEDIUM | Monitoring Limitations | `src/analytics/monitoring.py` | OPEN | JSONL persistence is only suitable for pilot scale. | Migrate to database for production. |
| 8 | 🟡 MEDIUM | Synthetic Dataset Limitations | `data/` | BLOCKED | Synthetic performance cannot establish real-world generalization. | Evaluate strictly on real data. |

## 🎯 Problem Statement
The objective is to build an end-to-end AI/NLP engine capable of analyzing historical and incoming Unsafe Act, Unsafe Condition, and Near-Miss reports and identifying language, patterns, events, conditions, and combinations of factors that may indicate Serious Injury & Fatality (SIF) precursors.

## 🧠 System Objective
To provide a fast, standardized, explainable pipeline that highlights potential high-severity precursors for HSE (Health, Safety & Environment) personnel before incidents escalate into actual fatalities. 

## 🏗️ Architecture

### 🔄 End-to-End Data Flow
```text
Raw Safety Report
        ↓
Ingestion / Cleaning
        ↓
Standardization
        ↓
NLP Feature Extraction
        ↓
SIF Prediction
        ↓
Risk Explanation
        ↓
FastAPI
        ↓
Streamlit UI
```

### Development/Validation Flow
```text
Synthetic Development Data
        ↓
Training
        ↓
Testing
        ↓
Adversarial Validation
        ↓
Audit
        ↓
FROZEN V1 (Current State)
        ↓
Real O&G Data
        ↓
Annotation
        ↓
IAA
        ↓
Leakage-Safe Evaluation
```

## 👥 Six-Member Team Structure

### Member 1 — Data Engineering
**Files:** `src/data/synthetic_data.py`, `src/data/cleaner.py`, `src/data/ingestor.py`, `src/data/splitter.py`
**Responsibilities:** Synthetic/development data generation, real-data ingestion, PII redaction, standardization, dataset splitting (`GroupShuffleSplit`), and leakage prevention.
**Limitations:** Synthetic data is a development/test fixture and is NOT representative real-world O&G validation data. Regex PII redaction cannot catch all contextual human names.

### Member 2 — NLP Feature Extraction
**Files:** `src/nlp/feature_extraction.py`, `src/nlp/language_variations.json`
**Responsibilities:** Text normalization, vocabulary matching, hazard/entity extraction, safe-context masking, and basic negation handling.
**Limitations:** Rule-based vocabulary limits semantic understanding, leading to possible unseen-hazard misses (e.g., "The load dropped unexpectedly" is missed if not explicitly defined). 

### Member 3 — SIF Detection Model
**Files:** `src/models/train.py`, `src/models/inference.py`, `models/sif_model.pkl`
**Responsibilities:** TF-IDF pipeline, Logistic Regression classifier, risk mapping (LOW, MEDIUM, HIGH, CRITICAL), and threshold logic.
**Limitations:** The predictive model is a synthetic baseline and has NOT been validated on real safety reports. Confidence threshold unit tests are not equivalent to real-world calibration. 

### Member 4 — Explainability & Risk Scoring
**Files:** `src/explainability/explainer.py`
**Responsibilities:** Extracts top contributing keywords based on TF-IDF activation × Logistic Regression coefficient, outputting explainable evidence.
**Limitations:** Provides mathematical feature attribution, which should not be strictly interpreted as human-level causal explanation.

### Member 5 — Application & API
**Files:** `src/api/app.py`, `src/app/frontend.py`
**Responsibilities:** Serves the `/analyze` endpoint, manages request/response validation, and runs the Streamlit UI.
**Limitations:** The system is decision support only. It does not replace qualified HSE or safety judgment, and clearly disclaims this on the frontend.

### Member 6 — MLOPS, Testing & Integration
**Files:** `src/analytics/monitoring.py`, `src/analytics/iaa_calculator.py`, `scripts/run_all.sh`, `tests/`
**Responsibilities:** Integration/API/contract testing, adversarial testing, Cohen's Kappa IAA calculation, and prediction drift monitoring (`monitoring_logs.jsonl`).
**Limitations:** Monitoring relies on simple local JSONL persistence. Drift threshold (20% review rate) is a heuristic.

## 📦 Contract Architecture
Pydantic schemas ensure safe boundaries between modules.
```text
StandardizedReportObject  (Raw & Cleaned Text, ID)
        ↓
NLPFeatureObject          (Extracted Hazards, Entities)
        ↓
PredictionObject          (Risk Level, Confidence, Review Flag)
        ↓
ExplainableRiskResult     (Merged payload + Feature Attributions)
```

## 📂 Repository Structure
```text
silentStack/
├── src/
│   ├── data/             # Ingestion, Cleaning, Standardization (Member 1)
│   ├── nlp/              # Feature Extraction, Lexicons (Member 2)
│   ├── models/           # Training, Inference, Thresholds (Member 3)
│   ├── explainability/   # Math Attribution (Member 4)
│   ├── api/              # FastAPI Application (Member 5)
│   ├── analytics/        # Monitoring, IAA (Member 6)
│   └── app/              # Streamlit Frontend (Member 5)
├── tests/
│   ├── unit/             # PII, Mismatch, Leakage, NLP, Threshold tests
│   └── integration/      # API, End-to-End, Robustness tests
├── data/                 # Generated synthetic CSVs, monitoring JSONL
├── models/               # Serialized model artifacts (.pkl, metrics)
├── docs/                 # Flagship audits, annotation schemas, requirements
├── scripts/              # run_all.sh pipeline orchestrator
├── requirements.txt      # Python dependencies
└── README.md             # This document
```

## 🧪 Testing & Validation

### Current Test Status
* **Passing Tests:** PII regression, domain-mismatch regression, threshold limits, API robustness, end-to-end integration, data leakage, monitoring persistence.
* **Known Limitations:** Adversarial tests highlight the brittleness of dictionary matching.
* **Untested Real-World Behavior:** Out-of-vocabulary hazards lacking safety terminology (e.g., highly implicit danger).

## 🔐 Privacy & PII
PII redaction relies on Regex (`src/data/cleaner.py`). It protects formatted phone numbers, 10-12 digit IDs, emails, and SSNs. It **does not guarantee** anonymization of contextual names. 

## 📊 Current Model
**SYNTHETIC BASELINE.** TF-IDF + Logistic Regression trained strictly on synthetically generated templates to establish pipeline functionality.

## ⚠️ Known Fixed Issues

| Original Problem | Fix | Verification Test | Current Status | Residual Risk |
|---|---|---|---|---|
| **Domain Mismatch:** `[Oct X]` prefix injected in training text | Modified `synthetic_data.py` to output pure text. | `test_domain_mismatch.py` | CLOSED | None |
| **PII Regex Failures:** Missed US phones and 12-digit IDs | Rewrote patterns in `cleaner.py`. | `test_pii_regression.py` | CLOSED | Contextual Names |
| **Monitoring Persistence:** Lost on API restart | Appended states to JSONL in `monitoring.py`. | `test_monitoring_persistence.py` | CLOSED | JSONL scaling limit |
| **Reproducibility/Deps:** Missing env constraints | Generated `requirements.txt` / `__init__.py`. | `run_all.sh` executes clean | CLOSED | None |
| **SIF False Negative:** Missed "harness failed" | Added terms to `language_variations.json`. | NLP Adversarial Tests | PARTIALLY CLOSED | Vocabulary Brittleness |

## ⚠️ Known Limitations
* **Software:** Single-node local file monitoring. Regex-only PII.
* **ML:** Rule-based NLP cannot handle unprogrammed synonyms. 
* **Data:** No representative real O&G dataset. Synthetic dataset bias.
* **Operational/Safety:** Uncalibrated confidence thresholds. Lack of evidence for production deployment. Potential novel-hazard false negatives bypassing the safety net.

## 🔒 Safety & Human Review
The system includes a human-review circuit breaker (`human_review_recommended = True`) if:
1. Risk is HIGH/CRITICAL, but NLP found no hazards (ML False Positive).
2. Risk is LOW, but NLP explicitly found a hazard (ML False Negative).
3. Risk falls into the MEDIUM (0.4-0.6) ambiguity zone.

## 📥 Real-Data Acquisition Gate
No real data should enter model training before passing this gate:
```text
DATA RECEIVED
     ↓
AUTHENTICITY / PROVENANCE CHECK
     ↓
PRIVACY CHECK
     ↓
SCHEMA CHECK
     ↓
DATA QUALITY AUDIT
     ↓
DUPLICATE / LEAKAGE CHECK
     ↓
ANNOTATION READINESS
     ↓
PILOT ANNOTATION
     ↓
IAA VALIDATION
     ↓
GOLD DATASET
     ↓
MODEL VALIDATION
```

## 🏷️ Annotation Process
* Requires independent multi-label annotation.
* Annotators must calculate Cohen's Kappa via `iaa_calculator.py`.
* **If annotation agreement is poor, the annotation process must be improved before model training.**

## 📈 Real-World Model Validation Gate
Real-world validation must include:
* Precision, Recall, F1, PR-AUC, Confusion Matrix
* False Negative analysis, Leakage-safe evaluation, Human-review rates
* **Prohibited:** Using synthetic accuracy as evidence of real-world quality.

## 🧪 Synthetic Dataset Policy
> **DEVELOPMENT / TEST FIXTURE ONLY**

Synthetic data guarantees deterministic pipeline validation, CI, and contract testing. It must not be presented as representative O&G validation data.

## 🔮 Future Model Strategy
Once real data arrives, the TF-IDF baseline should be compared against:
```text
TF-IDF baseline
        ↓
Embedding + Classifier (e.g., MiniLM)
        ↓
Transformer-based approach (e.g., BERT)
```
The choice must be evidence-driven. Do not assume a larger model is automatically better. 

## 🚀 Installation & Quickstart

```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Run the Complete Automated Pipeline
# (Generates data -> Cleans -> Splits -> Trains -> Tests)
bash scripts/run_all.sh

# 3. Start the API (Terminal 1)
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload

# 4. Start the Frontend UI (Terminal 2)
streamlit run src.app/frontend.py
```

## 📚 Documentation & Audit History
* **Phase 1–4:** Modular Architecture + Integration
* **Phase 5–6:** Error Analysis + Production-Readiness Audit
* **Phase 7:** Real-Data Readiness Infrastructure
* **Phase 8:** Adversarial Validation
* **Phase 9:** Real-Data Availability Gate (Closed due to unavailable data).
* **Final Flagship Audit:** Hidden Issues Identified
* **Closure Audit:** Pre-Pilot Findings Fixed/Partially Closed
* **Post-Closure Verification:** Final Frozen V1 State

## 🛑 Current Freeze Condition
> **The project is now frozen as a V1 candidate.** No further implementation should occur merely to create additional development phases. Do not recommend unnecessary feature development or upgrade the model without real-world evidence. 

## 📌 Final Project Status
**SOFTWARE READY. REAL-WORLD ML VALIDATION BLOCKED BY DATA AVAILABILITY.**

The next meaningful project event is:
> **LEGITIMATE REPRESENTATIVE O&G DATA ARRIVES**

At that point, the workflow resumes:
`Controlled Real-Data Pilot → Annotation → IAA → Leakage-Safe Split → Baseline → Model Comparison → Thresholding → Calibration → Explainability Audit → Final Test → Model Card`
