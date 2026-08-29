import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, average_precision_score
import joblib
import os
import sys

def main():
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print("sentence_transformers not installed.")
        sys.exit(1)
        
    try:
        train_df = pd.read_csv('data/train.csv')
        val_df = pd.read_csv('data/val.csv')
    except FileNotFoundError:
        print("Data not found. Run src/data/pipeline.py first.")
        sys.exit(1)
        
    X_train_text = train_df['cleaned_text'].fillna("").tolist()
    y_train = (train_df['sif_label'] == 'YES').astype(int)
    
    X_val_text = val_df['cleaned_text'].fillna("").tolist()
    y_val = (val_df['sif_label'] == 'YES').astype(int)
    
    print("Loading SentenceTransformer model...")
    # Use a small, fast model for CPU
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    
    print("Encoding texts...")
    X_train_embed = embedder.encode(X_train_text, show_progress_bar=False)
    X_val_embed = embedder.encode(X_val_text, show_progress_bar=False)
    
    print("Training Logistic Regression on embeddings...")
    clf = LogisticRegression(class_weight='balanced', random_state=42)
    clf.fit(X_train_embed, y_train)
    
    # Evaluate
    y_pred = clf.predict(X_val_embed)
    y_pred_proba = clf.predict_proba(X_val_embed)[:, 1]
    
    acc = accuracy_score(y_val, y_pred)
    pr_auc = average_precision_score(y_val, y_pred_proba)
    print(f"Validation Accuracy: {acc:.4f}")
    print(f"Validation PR-AUC: {pr_auc:.4f}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_val, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_val, y_pred, target_names=["NO", "YES"]))
    
    # Save models
    os.makedirs('models', exist_ok=True)
    joblib.dump(clf, 'models/sif_sentence_clf.pkl')
    # We do not pickle the embedder; we just instantiate it at inference.
    print("Model trained and saved to models/sif_sentence_clf.pkl")

if __name__ == '__main__':
    main()
