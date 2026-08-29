import sys
import os
import joblib

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import (
    StandardizedReportObject,
    NLPFeatureObject,
    PredictionObject,
    ExplainableRiskResult
)

class RiskExplainer:
    def __init__(self, model_path: str = None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models", "sif_model.pkl")
        self.pipeline = joblib.load(model_path)
        
    def explain(self, 
                report: StandardizedReportObject, 
                features: NLPFeatureObject, 
                prediction: PredictionObject) -> ExplainableRiskResult:
        
        tfidf = self.pipeline.named_steps['tfidf']
        clf = self.pipeline.named_steps['clf']
        
        text = features.feature_metadata.get("cleaned_text", "")
        vec = tfidf.transform([text])
        feature_names = tfidf.get_feature_names_out()
        
        yes_idx = list(clf.classes_).index("YES")
        
        if clf.coef_.shape[0] == 1:
            coef = clf.coef_[0] if yes_idx == 1 else -clf.coef_[0]
        else:
            coef = clf.coef_[yes_idx]
            
        evidence = []
        for col in vec.nonzero()[1]:
            contribution = coef[col] * vec[0, col]
            if contribution > 0:
                evidence.append({"word": feature_names[col], "weight": float(contribution)})
                
        evidence = sorted(evidence, key=lambda x: x["weight"], reverse=True)[:5]
        evidence_words = [e["word"] for e in evidence]
        
        return ExplainableRiskResult(
            risk_level=prediction.sif_risk_level,
            confidence=prediction.confidence,
            detected_precursors=prediction.precursor_categories,
            supporting_evidence={"keywords": evidence_words, "details": evidence},
            contributing_factors=features.hazard_features + features.exposure_features,
            similar_reports=[],
            human_review_recommended=prediction.human_review_recommended,
            analytics_metadata={"model_version": prediction.model_version}
        )
