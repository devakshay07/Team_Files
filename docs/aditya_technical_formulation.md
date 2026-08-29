# Technical Problem Formulation & Approach

## 1. Problem Formulation
The goal is to analyze unstructured safety reports and identify Serious Injury or Fatality (SIF) precursors. This is a complex NLP problem that breaks down into two distinct sub-tasks:

**Task A: SIF Precursor Detection (Binary Classification)**
* **Input Space:** Unstructured text sequence `X`.
* **Output Space:** `Y ∈ {0, 1}` (where 1 = SIF Precursor, 0 = Non-SIF).
* **Objective:** Maximize Recall on the positive class (SIF) while maintaining acceptable Precision to prevent alert fatigue.

**Task B: Hazard & Evidence Extraction (Information Extraction / Multi-label)**
* **Input Space:** Unstructured text sequence `X`.
* **Output Space:** A structured schema mapping `X` to categorical variables (Hazard Category, Failed Control, Potential Consequence) and extracting specific text evidence.
* **Objective:** Provide explainability to the EHS officer by tracing the classification back to domain-specific entities.

*Justification:* A pure black-box classifier (Task A alone) is insufficient because EHS officers will not trust a system that simply outputs a probability score. We must extract the underlying hazard mechanisms (Task B) to justify the classification.

## 2. Approach Comparison Table

| Approach | Advantage | Disadvantage | Data Required | Explainability | Suitable for SIF? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TF-IDF + Logistic Regression** | Fast, simple, highly explainable (feature weights). | Ignores word order and semantics; brittle to synonyms. | Low (hundreds of samples) | High (Keyword weights) | **Yes (Baseline)** |
| **TF-IDF + SVM** | Handles high-dimensional text well. | Harder to calibrate probabilities for confidence scores. | Low | Medium | Yes |
| **Random Forest / XGBoost** | Captures non-linear keyword interactions. | Computationally heavier than LR; prone to overfitting on text. | Medium | Medium (Feature importance) | No (LR is better baseline) |
| **Word Embeddings + CNN/RNN** | Captures local semantics. | Outdated architecture; outperformed by Transformers. | High | Low | No |
| **Sentence-BERT + Classifier** | Excellent semantic clustering (handles language variations well). | Black-box embeddings make exact word tracing difficult. | Medium | Low | Yes (Good embedding choice) |
| **Fine-tuned Domain BERT** | State-of-the-art semantic understanding; handles complex context. | Requires significant compute; requires thousands of labeled O&G reports. | High (thousands) | Medium (Attention maps) | **Yes (Target Model)** |
| **LLM (Prompting - GPT-4/Claude)** | Zero-shot reasoning; can extract fields and explain logic naturally. | High latency, expensive, potential hallucination, data privacy issues (cloud). | Zero-shot | High (Generates text) | Yes (For extraction) |
| **Hybrid (Rules + Embeddings)** | Combines strict O&G taxonomy rules with semantic flexibility. | High engineering overhead to maintain rules. | Low | High | Yes |

## 3. Model Recommendation
* **Primary Recommendation (Production): Fine-tuned Domain BERT (e.g., RoBERTa/DeBERTa)**. It provides the deep semantic understanding necessary to distinguish between "LOTO was followed" and "LOTO was bypassed".
* **Fallback / Baseline Recommendation: TF-IDF + Logistic Regression**. It requires very little data to train, is perfectly explainable via coefficient weights, and serves as a sanity check against the BERT model.
* **Extraction Engine: LLM API (if privacy allows) or strict regex/NER pipeline**. Extraction is better handled by a generative or token-classification model than a sequence-classifier.
