import joblib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import NLPFeatureObject, PredictionObject

class SIFModel:
    def __init__(self, model_path: str = None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models", "sif_model.pkl")
        self.pipeline = joblib.load(model_path)
        
    def predict(self, features: NLPFeatureObject) -> PredictionObject:
        # Pass the pre-processed (hybrid NLP) text to TF-IDF
        text = features.feature_metadata.get("cleaned_text", "")
        
        probs = self.pipeline.predict_proba([text])[0]
        classes = self.pipeline.classes_
        
        yes_idx = list(classes).index("YES")
        sif_prob = probs[yes_idx]
        
        human_review = False
        
        if sif_prob > 0.8:
            risk_level = "CRITICAL"
        elif sif_prob > 0.6:
            risk_level = "HIGH"
        elif sif_prob > 0.4:
            # 0.4 to 0.6 is the ambiguous zone, request human review
            risk_level = "MEDIUM"
            human_review = True
        else:
            risk_level = "LOW"
            
        # Also request human review if the model flags high risk but NLP found zero hazards
        if risk_level in ["CRITICAL", "HIGH"] and len(features.hazard_features) == 0:
            human_review = True
            
        # Add safety fallback: if ML says LOW but NLP explicitly found a hazard, request review
        if risk_level == "LOW" and len(features.hazard_features) > 0:
            human_review = True
            
        return PredictionObject(
            sif_risk_level=risk_level,
            confidence=float(sif_prob),
            precursor_categories=features.hazard_features,
            human_review_recommended=human_review,
            model_version="1.1.0-Hybrid"
        )
