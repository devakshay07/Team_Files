import pandas as pd
import json
import logging
import os
import sys
from typing import Dict, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.cleaner import clean_dataset

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestor:
    def __init__(self, mapping_config: Dict[str, str]):
        """
        mapping_config defines how to map real-world columns to the pipeline columns.
        Expected keys: 'id', 'text', 'type', 'label'
        """
        self.mapping = mapping_config
        
    def ingest(self, file_path: str) -> pd.DataFrame:
        logger.info(f"Ingesting real-world data from {file_path}")
        
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV, JSON, or XLSX.")
            
        # Rename columns to standard pipeline schema
        rename_map = {}
        if 'id' in self.mapping: rename_map[self.mapping['id']] = 'report_id'
        if 'text' in self.mapping: rename_map[self.mapping['text']] = 'raw_text'
        if 'type' in self.mapping: rename_map[self.mapping['type']] = 'report_type'
        if 'label' in self.mapping: rename_map[self.mapping['label']] = 'sif_label'
        
        df = df.rename(columns=rename_map)
        
        # Ensure mandatory columns exist
        for col in ['report_id', 'raw_text']:
            if col not in df.columns:
                raise ValueError(f"Mandatory mapped column '{col}' missing from data.")
                
        # Generate Data Quality Report
        self._generate_dq_report(df)
        
        # Clean & PII Redact
        df = clean_dataset(df)
        
        return df
        
    def _generate_dq_report(self, df: pd.DataFrame):
        logger.info("=== DATA QUALITY REPORT ===")
        logger.info(f"Total Records: {len(df)}")
        if 'report_type' in df.columns:
            logger.info(f"Report Types:\n{df['report_type'].value_counts()}")
        
        missing = df.isnull().sum()
        logger.info(f"Missing Fields:\n{missing[missing > 0]}")
        
        if 'sif_label' in df.columns:
            logger.info(f"Class Distribution:\n{df['sif_label'].value_counts()}")
            
        logger.info("===========================")

if __name__ == "__main__":
    # Example usage for testing the infrastructure
    print("Ingestor ready. Waiting for real data.")
