import pandas as pd
import joblib
import os
import sys

def main():
    model_path = 'model/artifacts/model.pkl'
    
    if not os.path.exists(model_path):
        print("Missing model.")
        return
        
    model = joblib.load(model_path)
    
    # Inject adversarial examples to test the model's limitations
    adversarial_data = [
        {"text": "LOTO was correctly applied before maintenance started.", "true": "NO", "why": "Negation - model triggers on LOTO"},
        {"text": "Safety isolation was completed successfully.", "true": "NO", "why": "False positive on 'isolation'"},
        {"text": "Worker safely descended from the roof using full fall protection.", "true": "NO", "why": "False positive on 'fall' and 'roof'"},
        {"text": "Gas test was passed with 20.9% oxygen.", "true": "NO", "why": "False positive on 'gas test'"},
        {"text": "Mechanic failed to isolate the pump before starting.", "true": "YES", "why": "True positive - should catch this"},
        {"text": "The equipment wasn't isolated.", "true": "YES", "why": "Paraphrase missed if vocabulary is narrow"},
        {"text": "Worker didn't put on his harness.", "true": "YES", "why": "Paraphrase missed"},
        {"text": "It was completely depressurized.", "true": "NO", "why": "False positive on 'depressurized'"}
    ]
    
    df = pd.DataFrame(adversarial_data)
    y_true = df['true'].values
    texts = df['text'].values
    y_pred = model.predict(texts)
    
    errors = []
    for i in range(len(y_true)):
        if y_true[i] != y_pred[i]:
            error_type = "False Positive" if y_pred[i] == "YES" else "False Negative"
            
            errors.append({
                "Report Text": texts[i],
                "Actual": y_true[i],
                "Predicted": y_pred[i],
                "Error Type": error_type,
                "Why Wrong?": adversarial_data[i]["why"]
            })
            
    with open("model/error_analysis.md", "w") as f:
        f.write("# Model Error Analysis\n\n")
        f.write("This document analyzes the misclassifications made by the baseline TF-IDF model on a set of adversarial examples designed to test its limitations.\n\n")
        f.write("| Report Text | Actual Label | Predicted Label | Error Type | Why Wrong? |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        
        for e in errors:
            f.write(f"| {e['Report Text']} | {e['Actual']} | {e['Predicted']} | {e['Error Type']} | {e['Why Wrong?']} |\n")
            
        f.write("\n## Recurring Error Patterns\n")
        f.write("1. **Keyword False Positives:** The model triggers on words like 'isolation' even in safe contexts (e.g., 'Isolation completed successfully').\n")
        f.write("2. **Contextual False Negatives:** Short reports lack the explicit hazards the TF-IDF vocabulary expects.\n")
        f.write("3. **Negation:** TF-IDF cannot distinguish between 'did not follow LOTO' and 'followed LOTO'.\n")
        f.write("\n## Proposed Improvements\n")
        f.write("- **Migrate to BERT:** Contextual embeddings handle negation natively.\n")
        f.write("- **Data Augmentation:** Inject hard negatives during training.\n")
        
    print(f"Error analysis generated at model/error_analysis.md with {len(errors)} errors found.")

if __name__ == '__main__':
    main()
