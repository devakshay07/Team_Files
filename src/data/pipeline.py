import os
import logging
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.synthetic_data import generate_synthetic_data
from src.data.cleaner import clean_dataset
from src.data.splitter import split_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline():
    os.makedirs("data", exist_ok=True)
    
    logger.info("Generating synthetic data...")
    raw_df = generate_synthetic_data(1200)
    raw_df.to_csv("data/raw_data.csv", index=False)
    
    logger.info("Cleaning dataset...")
    clean_df = clean_dataset(raw_df)
    clean_df.to_csv("data/clean_data.csv", index=False)
    
    logger.info("Splitting dataset into train/val/test...")
    train_df, val_df, test_df = split_data(clean_df)
    
    train_df.to_csv("data/train.csv", index=False)
    val_df.to_csv("data/val.csv", index=False)
    test_df.to_csv("data/test.csv", index=False)
    
    logger.info("Pipeline completed successfully! Artifacts saved in 'data/' directory.")

if __name__ == "__main__":
    run_pipeline()
