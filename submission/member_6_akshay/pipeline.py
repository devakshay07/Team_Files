import os
import logging
from synthetic_data import generate_synthetic_data
from cleaner import clean_dataset
from splitter import split_data
from analysis import analyze_dataset

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline():
    # 1. Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    # 2. Generate raw synthetic data
    logger.info("Generating synthetic data...")
    raw_df = generate_synthetic_data(1200) # Generating slightly more to account for drops
    raw_df.to_csv("output/raw_data.csv", index=False)
    
    # 3. Clean and Deduplicate
    logger.info("Cleaning dataset...")
    clean_df = clean_dataset(raw_df)
    clean_df.to_csv("output/clean_data.csv", index=False)
    
    # 4. Analyze and document
    logger.info("Generating dataset inventory analysis...")
    analyze_dataset(clean_df, "output/dataset_inventory.md")
    
    # 5. Split data
    logger.info("Splitting dataset into train/val/test...")
    train_df, val_df, test_df = split_data(clean_df)
    
    # 6. Save splits
    train_df.to_csv("output/train.csv", index=False)
    val_df.to_csv("output/val.csv", index=False)
    test_df.to_csv("output/test.csv", index=False)
    
    logger.info("Pipeline completed successfully! Artifacts saved in 'output/' directory.")

if __name__ == "__main__":
    run_pipeline()
