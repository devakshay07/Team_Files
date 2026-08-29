import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.nlp.feature_extraction import NLPFeatureExtractor
from src.data.contracts import StandardizedReportObject

def test_nlp_adversarial():
    extractor = NLPFeatureExtractor()
    
    cases = [
        # True Positives
        ("Worker was not wearing a harness and fell.", True, "fall_protection_failure"),
        ("H2S alarm went off.", True, "h2s_exposure"),
        
        # Safe Negations (Should be ignored)
        ("Worker safely descended using full fall protection.", False, "fall_protection_failure"),
        ("LOTO was correctly applied so equipment remained de-energized.", False, "no_isolation"),
        
        # Double Negation / Complex Context (Will likely fail, need to document)
        ("It is not true that the worker was safely tied off.", True, "fall_protection_failure"),
        
        # Hypothetical / Historical
        ("In last week's safety meeting, we discussed what to do if a tool fell from height.", False, "dropped_object_risk")
    ]
    
    print("=== NLP ADVERSARIAL TESTING ===")
    for text, should_flag, target_hazard in cases:
        report = StandardizedReportObject(report_id="1", report_type="Near Miss", raw_text=text, cleaned_text=text.lower())
        features = extractor.extract_features(report)
        flagged = target_hazard in features.hazard_features
        
        status = "PASS" if flagged == should_flag else "FAIL"
        print(f"[{status}] Text: '{text}'")
        print(f"       Expected: {should_flag}, Got: {flagged}")
        if flagged:
            print(f"       Extracted text for model: {features.feature_metadata['cleaned_text']}")

if __name__ == "__main__":
    test_nlp_adversarial()
