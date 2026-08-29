import sys
import os
import uuid
import warnings
warnings.filterwarnings('ignore')

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import StandardizedReportObject
from src.nlp.feature_extraction import NLPFeatureExtractor
from src.models.inference import SIFModel
from src.explainability.explainer import RiskExplainer
from src.data.cleaner import clean_text

def test_full_pipeline():
    print("Testing End-to-End Pipeline Integration...")
    
    # 1. Initialize all modules
    print("Initializing modules...")
    extractor = NLPFeatureExtractor()
    model = SIFModel()
    explainer = RiskExplainer()
    
    raw_text = "Worker entered the confined space at Unit A without conducting a gas test. No standby person was present."
    
    # 2. Member 1: Standardization
    print("\n--- STEP 1: Standardization ---")
    report = StandardizedReportObject(
        report_id=str(uuid.uuid4()),
        report_type="Unsafe Act",
        location="Unit A",
        raw_text=raw_text,
        cleaned_text=clean_text(raw_text)
    )
    print("Standardized Text:", report.cleaned_text)
    
    # 3. Member 2: NLP Features
    print("\n--- STEP 2: NLP Feature Extraction ---")
    features = extractor.extract_features(report)
    print("Extracted Entities:", features.extracted_entities)
    print("Hazard Features:", features.hazard_features)
    assert len(features.hazard_features) > 0
    
    # 4. Member 3: Prediction
    print("\n--- STEP 3: SIF Prediction ---")
    prediction = model.predict(features)
    print("Risk Level:", prediction.sif_risk_level)
    print("Confidence:", prediction.confidence)
    assert prediction.sif_risk_level in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    
    # 5. Member 4: Explanation
    print("\n--- STEP 4: Risk Explanation ---")
    explanation = explainer.explain(report, features, prediction)
    print("Detected Precursors:", explanation.detected_precursors)
    print("Contributing Factors:", explanation.contributing_factors)
    print("Supporting Evidence Keywords:", explanation.supporting_evidence["keywords"])
    assert len(explanation.supporting_evidence["keywords"]) > 0
    
    print("\n✅ End-to-End Pipeline test PASSED.")

if __name__ == "__main__":
    test_full_pipeline()
