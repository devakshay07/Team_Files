import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.nlp.feature_extraction import NLPFeatureExtractor
from src.data.contracts import StandardizedReportObject

def test_nlp():
    print("Testing NLP Feature Extraction...")
    extractor = NLPFeatureExtractor()
    
    # 1. Multiple variations of same hazard
    report = StandardizedReportObject(report_id="1", report_type="x", raw_text="", cleaned_text="No harness was used and worker without fall arrest.")
    features = extractor.extract_features(report)
    assert len(features.hazard_features) == 1
    assert features.hazard_features[0] == "fall_protection_failure"
    
    # 2. Case insensitivity
    report = StandardizedReportObject(report_id="2", report_type="x", raw_text="", cleaned_text="NO HARNESS")
    features = extractor.extract_features(report)
    assert features.hazard_features[0] == "fall_protection_failure"
    
    # 3. Multiple hazards
    report = StandardizedReportObject(report_id="3", report_type="x", raw_text="", cleaned_text="no harness and no sniffer used")
    features = extractor.extract_features(report)
    assert "fall_protection_failure" in features.hazard_features
    assert "no_gas_testing" in features.hazard_features
    
    print("✅ NLP Feature Extraction tests PASSED.")

if __name__ == "__main__":
    test_nlp()
