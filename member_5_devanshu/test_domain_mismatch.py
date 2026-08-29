import sys
import os
import unittest
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.synthetic_data import generate_synthetic_data
from src.data.cleaner import clean_dataset

class TestDomainMismatch(unittest.TestCase):
    def test_metadata_not_in_training(self):
        # Generate a small sample
        raw_df = generate_synthetic_data(50)
        clean_df = clean_dataset(raw_df)
        
        # Verify no '[Oct' style prefixes made it into the cleaned text
        for text in clean_df['cleaned_text'].dropna():
            self.assertNotIn("[oct", text.lower(), f"Metadata prefix leaked into training text: {text}")

if __name__ == "__main__":
    unittest.main()
