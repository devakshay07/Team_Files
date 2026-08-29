import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, average_precision_score
import joblib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.nlp.feature_extraction import NLPFeatureExtractor
from src.data.contracts import StandardizedReportObject

def main():
    try:
        train_df = pd.read_csv('data/train.csv')
        val_df = pd.read_csv('data/val.csv')
    except FileNotFoundError:
        print("Data not found. Run src/data/pipeline.py first.")
        sys.exit(1)
        
    extractor = NLPFeatureExtractor()
    
    def process_texts(texts):
        processed = []
        for text in texts:
            # We wrap it in the StandardizedReportObject just to pass to the extractor
            report = StandardizedReportObject(
                report_id="dummy",
                report_type="Unsafe Act",
                raw_text=str(text),
                cleaned_text=str(text)
            )
            features = extractor.extract_features(report)
            processed.append(features.feature_metadata.get("cleaned_text", ""))
        return processed

    print("Extracting Hybrid NLP Features for Train/Val sets...")
    X_train = process_texts(train_df['cleaned_text'].fillna(""))
    y_train = train_df['sif_label']
    
    X_val = process_texts(val_df['cleaned_text'].fillna(""))
    y_val = val_df['sif_label']
    
    # Task 1: SIF Precursor Detection (Model A: TF-IDF + LR)
    print("Training Hybrid TF-IDF + Logistic Regression Model...")
    pipeline_lr = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1,2))),
        ('clf', LogisticRegression(class_weight='balanced', random_state=42))
    ])
    pipeline_lr.fit(X_train, y_train)
    
    # Validation & Evaluation metrics
    y_pred = pipeline_lr.predict(X_val)
    y_pred_proba = pipeline_lr.predict_proba(X_val)
    
    acc_lr = accuracy_score(y_val, y_pred)
    # y_pred_proba has shape (n_samples, 2). Assuming 'YES' is class 1.
    yes_idx = list(pipeline_lr.classes_).index('YES')
    pr_auc = average_precision_score((y_val == 'YES').astype(int), y_pred_proba[:, yes_idx])
    
    print(f"Validation Accuracy: {acc_lr:.4f}")
    print(f"Validation PR-AUC: {pr_auc:.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_val, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_val, y_pred))
    
    # Analyze False Negatives specifically
    print("\n--- False Negative Analysis ---")
    fn_count = 0
    for i, (actual, pred) in enumerate(zip(y_val, y_pred)):
        if actual == 'YES' and pred == 'NO':
            print(f"FN Output [{i}]: {val_df.iloc[i]['cleaned_text']}")
            fn_count += 1
    if fn_count == 0:
        print("No false negatives found (likely due to synthetic data perfection).")
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(pipeline_lr, 'models/sif_model.pkl')
    
    print("\nModel trained and saved to models/sif_model.pkl")

if __name__ == '__main__':
    main()
