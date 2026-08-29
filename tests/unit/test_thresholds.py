import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.models.inference import SIFModel
from src.data.contracts import NLPFeatureObject

class TestThresholds(unittest.TestCase):
    def setUp(self):
        self.model = SIFModel()
        # Mock the pipeline prediction
        self.model.pipeline = MagicMock()
        self.model.pipeline.classes_ = ["NO", "YES"]
        
    def test_medium_threshold_triggers_review(self):
        # 0.45 is MEDIUM (>0.4), so it should trigger human review
        self.model.pipeline.predict_proba.return_value = [[0.55, 0.45]]
        
        features = NLPFeatureObject()
        features.hazard_features = [] # 0 hazards
        prediction = self.model.predict(features)
        
        self.assertEqual(prediction.sif_risk_level, "MEDIUM")
        self.assertTrue(prediction.human_review_recommended)
        
    def test_high_threshold(self):
        # 0.70 is HIGH (>0.6)
        self.model.pipeline.predict_proba.return_value = [[0.30, 0.70]]
        
        # Test fallback: High risk but 0 hazards triggers review
        features = NLPFeatureObject()
        features.hazard_features = []
        prediction = self.model.predict(features)
        
        self.assertEqual(prediction.sif_risk_level, "HIGH")
        self.assertTrue(prediction.human_review_recommended)

    def test_low_risk_conflict_triggers_review(self):
        # 0.20 is LOW
        self.model.pipeline.predict_proba.return_value = [[0.80, 0.20]]
        
        # But NLP found a hazard
        features = NLPFeatureObject()
        features.hazard_features = ["fall_protection_failure"]
        prediction = self.model.predict(features)
        
        self.assertEqual(prediction.sif_risk_level, "LOW")
        self.assertTrue(prediction.human_review_recommended) # Safety fallback

if __name__ == "__main__":
    unittest.main()
