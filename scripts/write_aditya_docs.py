import os

content_formulation = """# Technical Problem Formulation & Approach

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
"""

content_architecture = """# System Architecture & Technical Risk Register

## 1. System Architecture Diagram

```mermaid
graph TD
    A[Raw Safety Report] -->|Text| B(Preprocessing Node)
    B -->|Clean Text| C{Information Extraction Engine}
    
    C -->|Extracted Entities| D[Domain Taxonomy Matcher]
    D -->|Hazard, Control| E[SIF Classification Model]
    
    C -->|Semantic Context| E
    
    E -->|SIF: YES/NO + Confidence| F{Explainability Module}
    F -->|Evidence Keywords| G[Priority Assignment Engine]
    
    G -->|JSON Payload| H((FastAPI Backend))
    H -->|REST API| I[EHS Dashboard UI]
    
    subgraph Data Pipeline
    B
    end
    
    subgraph NLP Engine
    C
    D
    E
    F
    end
    
    subgraph Application Layer
    G
    H
    I
    end
```

## 2. Technical Risk Register

| Risk | Why It Matters | Proposed Mitigation | Severity |
| :--- | :--- | :--- | :--- |
| **Class Imbalance (Rare SIFs)** | Model may achieve 95% accuracy by simply predicting "NO" for everything, missing the actual SIFs. | Use SMOTE, class weighting, or Focal Loss. Evaluate using Recall/F1, not Accuracy. | Critical |
| **Few SIF Training Examples** | Deep learning models will overfit on a tiny positive class. | Use a simpler baseline (TF-IDF+LR) or transfer learning (few-shot LLM) until data grows. | High |
| **Noisy / Vague Labels** | If annotators disagree on what a SIF is, the model will learn confused boundaries. | Implement strict annotation guidelines and adjudicate disagreements. | High |
| **Short Reports (Insufficient Context)** | "Pump broke" gives the model nothing to analyze. | Model should flag reports as "Insufficient Info" rather than guessing. | Medium |
| **Domain-Specific Vocabulary** | Generic models (BERT) don't understand terms like "LOTO", "SIMOPS", "H2S". | Fine-tune the language model on unsupervised O&G manuals/reports first (Domain Adaptation). | High |
| **False Negatives** | Missing a genuinely dangerous report defeats the purpose of the system. | Tune the decision threshold to favor High Recall; accept some false positives. | Critical |
| **False Positives (Alert Fatigue)** | If the system flags every minor issue as CRITICAL, EHS will ignore it. | Implement an active-learning feedback loop where EHS overrides adjust the model. | High |
| **Data Leakage** | Near-duplicate reports across train/test splits artificially inflate performance metrics. | Implement strict exact and fuzzy deduplication before splitting the dataset. | Critical |
| **Synthetic Data Contamination** | Evaluating the model on synthetic data gives a false sense of real-world readiness. | The final Test set must be 100% human-written, real-world reports. | Critical |
| **Explainability Gap** | EHS officers will not act on a black-box 98% probability score. | Output top influential keywords (TF-IDF weights) or use SHAP for complex models. | High |
| **Negation Handling** | "LOTO was applied" vs "LOTO was bypassed" — TF-IDF treats "LOTO" identically. | Rely on bi-grams/n-grams in TF-IDF, or transition to contextual embeddings (BERT). | High |
| **Code-Mixing / Typos** | Reports often contain misspellings or regional slang. | Use subword tokenization (BPE/WordPiece) and robust text cleaning. | Medium |

## 3. Evaluation Strategy
* **Primary Metric:** Recall on the SIF (Positive) Class. We must minimize False Negatives.
* **Secondary Metric:** F1-Score on the SIF Class (balances Recall against Precision).
* **Rule:** Overall Accuracy is explicitly banned as a primary metric due to the 95/5 class imbalance.
"""

os.makedirs("domain", exist_ok=True)
with open("domain/aditya_technical_formulation.md", "w", encoding="utf-8") as f:
    f.write(content_formulation)

with open("domain/aditya_architecture.md", "w", encoding="utf-8") as f:
    f.write(content_architecture)
