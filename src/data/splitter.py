import pandas as pd
from sklearn.model_selection import train_test_split, GroupShuffleSplit
import logging

logger = logging.getLogger(__name__)

def split_data(df: pd.DataFrame, group_col: str = None) -> tuple:
    """
    Splits the dataset. If group_col is provided, uses GroupShuffleSplit 
    to ensure records from the same group (e.g. incident_id) do not leak 
    across train/val/test boundaries.
    """
    logger.info("Starting robust split...")
    
    if group_col and group_col in df.columns:
        logger.info(f"Using GroupShuffleSplit on {group_col} to prevent leakage.")
        gss = GroupShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
        train_idx, temp_idx = next(gss.split(df, groups=df[group_col]))
        train_df = df.iloc[train_idx]
        temp_df = df.iloc[temp_idx]
        
        gss_val = GroupShuffleSplit(n_splits=1, test_size=0.5, random_state=42)
        val_idx, test_idx = next(gss_val.split(temp_df, groups=temp_df[group_col]))
        val_df = temp_df.iloc[val_idx]
        test_df = temp_df.iloc[test_idx]
    else:
        logger.info("Using standard stratified split.")
        stratify_col = df['sif_label'] if 'sif_label' in df.columns else None
        train_df, temp_df = train_test_split(df, test_size=0.3, stratify=stratify_col, random_state=42)
        
        stratify_temp = temp_df['sif_label'] if 'sif_label' in temp_df.columns else None
        val_df, test_df = train_test_split(temp_df, test_size=0.5, stratify=stratify_temp, random_state=42)
        
    logger.info("Split results:")
    logger.info(f" - Train: {len(train_df)} records")
    logger.info(f" - Validation: {len(val_df)} records")
    logger.info(f" - Test: {len(test_df)} records")
    
    return train_df, val_df, test_df
