import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.splitter import split_data

def test_leakage():
    print("Testing Dataset Leakage Prevention (GroupShuffleSplit)...")
    
    # 5 reports, but 2 of them share an incident ID
    data = [
        {"incident_id": "A", "cleaned_text": "text A", "sif_label": "NO"},
        {"incident_id": "A", "cleaned_text": "text A duplicate", "sif_label": "NO"},
        {"incident_id": "B", "cleaned_text": "text B", "sif_label": "YES"},
        {"incident_id": "C", "cleaned_text": "text C", "sif_label": "NO"},
        {"incident_id": "D", "cleaned_text": "text D", "sif_label": "NO"},
        {"incident_id": "E", "cleaned_text": "text E", "sif_label": "YES"}
    ]
    df = pd.DataFrame(data)
    
    train, val, test = split_data(df, group_col="incident_id")
    
    # Check if Incident A leaked across boundaries
    train_ids = set(train['incident_id'].tolist())
    val_ids = set(val['incident_id'].tolist())
    test_ids = set(test['incident_id'].tolist())
    
    overlap = train_ids.intersection(val_ids) | train_ids.intersection(test_ids) | val_ids.intersection(test_ids)
    
    if overlap:
        print(f"FAILED: Found overlapping incident IDs across splits: {overlap}")
        sys.exit(1)
    else:
        print("SUCCESS: No incident IDs leaked across splits.")

if __name__ == "__main__":
    test_leakage()
