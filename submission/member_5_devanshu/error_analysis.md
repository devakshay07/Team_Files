# Model Error Analysis

This document analyzes the misclassifications made by the baseline TF-IDF model on a set of adversarial examples designed to test its limitations.

| Report Text | Actual Label | Predicted Label | Error Type | Why Wrong? |
| :--- | :--- | :--- | :--- | :--- |
| LOTO was correctly applied before maintenance started. | NO | YES | False Positive | Negation - model triggers on LOTO |
| Safety isolation was completed successfully. | NO | YES | False Positive | False positive on 'isolation' |
| Worker safely descended from the roof using full fall protection. | NO | YES | False Positive | False positive on 'fall' and 'roof' |
| Gas test was passed with 20.9% oxygen. | NO | YES | False Positive | False positive on 'gas test' |
| Worker didn't put on his harness. | YES | NO | False Negative | Paraphrase missed |
| It was completely depressurized. | NO | YES | False Positive | False positive on 'depressurized' |

## Recurring Error Patterns
1. **Keyword False Positives:** The model triggers on words like 'isolation' even in safe contexts (e.g., 'Isolation completed successfully').
2. **Contextual False Negatives:** Short reports lack the explicit hazards the TF-IDF vocabulary expects.
3. **Negation:** TF-IDF cannot distinguish between 'did not follow LOTO' and 'followed LOTO'.

## Proposed Improvements
- **Migrate to BERT:** Contextual embeddings handle negation natively.
- **Data Augmentation:** Inject hard negatives during training.
