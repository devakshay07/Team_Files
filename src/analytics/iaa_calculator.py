import pandas as pd
from sklearn.metrics import cohen_kappa_score
import sys

def calculate_iaa(file_a: str, file_b: str, label_col: str = "sif_label"):
    """
    Calculates Inter-Annotator Agreement (Cohen's Kappa) between two annotators.
    Both CSVs must have 'report_id' and the specified label column.
    """
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)
    
    merged = pd.merge(df_a[['report_id', label_col]], df_b[['report_id', label_col]], on='report_id', suffixes=('_A', '_B'))
    
    if len(merged) == 0:
        print("No overlapping records found between annotators.")
        return
        
    kappa = cohen_kappa_score(merged[f"{label_col}_A"], merged[f"{label_col}_B"])
    
    print(f"Total Overlapping Records: {len(merged)}")
    print(f"Cohen's Kappa: {kappa:.4f}")
    
    if kappa < 0.75:
        print("WARNING: IAA is below the 0.75 threshold. Investigate annotation guidelines.")
    else:
        print("SUCCESS: Annotators show strong agreement.")
        
    # Find conflicts
    conflicts = merged[merged[f"{label_col}_A"] != merged[f"{label_col}_B"]]
    if not conflicts.empty:
        print(f"\nFound {len(conflicts)} conflicting records needing adjudication.")
        # Save conflicts for review
        conflicts.to_csv("annotation_conflicts.csv", index=False)
        print("Conflicts saved to annotation_conflicts.csv")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        calculate_iaa(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python3 iaa_calculator.py <annotator_A.csv> <annotator_B.csv>")
