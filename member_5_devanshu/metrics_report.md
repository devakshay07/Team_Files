# Model Evaluation Metrics & Experiments

## Task 1: SIF Precursor Detection (Binary)
### Model A: TF-IDF + Logistic Regression (Baseline)
**Validation Accuracy:** 1.0000

```
              precision    recall  f1-score   support

          NO       1.00      1.00      1.00       167
         YES       1.00      1.00      1.00         9

    accuracy                           1.00       176
   macro avg       1.00      1.00      1.00       176
weighted avg       1.00      1.00      1.00       176

Confusion Matrix:
[[167   0]
 [  0   9]]
```

### Model B: TF-IDF + Support Vector Machine
**Validation Accuracy:** 1.0000

```
              precision    recall  f1-score   support

          NO       1.00      1.00      1.00       167
         YES       1.00      1.00      1.00         9

    accuracy                           1.00       176
   macro avg       1.00      1.00      1.00       176
weighted avg       1.00      1.00      1.00       176

```

## Task 2: Risk / Priority Level (Multi-class)
```
              precision    recall  f1-score   support

    CRITICAL       0.50      0.40      0.44         5
        HIGH       0.40      0.50      0.44         4
         LOW       0.48      0.35      0.41        85
      MEDIUM       0.47      0.60      0.53        82

    accuracy                           0.47       176
   macro avg       0.46      0.46      0.46       176
weighted avg       0.47      0.47      0.46       176

```

## Task 3: Hazard Category (Multi-class)
```
                   precision    recall  f1-score   support

   Confined Space       0.22      0.14      0.17        28
       Electrical       0.10      0.18      0.13        22
 Energy Isolation       0.23      0.12      0.16        24
  Manual Handling       0.24      0.21      0.22        19
         Pressure       0.18      0.25      0.21        32
      Slips/Trips       0.21      0.28      0.24        25
Working at Height       0.17      0.08      0.11        26

         accuracy                           0.18       176
        macro avg       0.19      0.18      0.18       176
     weighted avg       0.19      0.18      0.18       176

```

## Model Recommendation
TF-IDF + Logistic Regression offers identical performance to SVM on the synthetic dataset, but with native probability outputs required for the `confidence` score in our schema. Model A is selected as the baseline for production. Future work involves transitioning to BERT/Sentence Embeddings to resolve negation errors.
