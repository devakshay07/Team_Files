import pandas as pd
import re
import logging
from typing import List

logger = logging.getLogger(__name__)

def remove_pii(text: str) -> str:
    if not isinstance(text, str):
        return text
        
    # Redact Emails
    text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[EMAIL_REDACTED]', text)
    # Redact flat 10-12 digit sequences (e.g. 9876543210) first so they aren't partially matched
    text = re.sub(r'\b\d{10,12}\b', '[PHONE_REDACTED]', text)
    # Redact standard formatted phone numbers (+1 555-123-4567 or (555) 123-4567)
    text = re.sub(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '[PHONE_REDACTED]', text)
    # Redact SSN or generic 9-digit IDs
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[ID_REDACTED]', text)
    
    return text

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    text = remove_pii(text)
    return text

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    initial_count = len(df)
    
    if 'raw_text' not in df.columns:
        logger.error("Column 'raw_text' missing from dataset.")
        return df
        
    df = df.dropna(subset=['raw_text'])
    empty_removed = initial_count - len(df)
    
    df['cleaned_text'] = df['raw_text'].apply(clean_text)
    
    before_dedup = len(df)
    df = df.drop_duplicates(subset=['cleaned_text'])
    dupes_removed = before_dedup - len(df)
    
    logger.info("Data Cleaning Summary:")
    logger.info(f" - Initial records: {initial_count}")
    logger.info(f" - Empty records removed: {empty_removed}")
    logger.info(f" - Too short records removed: 0")
    logger.info(f" - Duplicates & near-duplicates removed: {dupes_removed}")
    logger.info(f" - Final clean records: {len(df)}")
    
    return df
