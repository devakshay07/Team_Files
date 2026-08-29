from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import ExplainableRiskResult, StandardizedReportObject
from src.nlp.feature_extraction import NLPFeatureExtractor
from src.models.inference import SIFModel
from src.explainability.explainer import RiskExplainer
from src.data.cleaner import clean_text
from src.analytics.monitoring import monitor

app = FastAPI(title="SIF Precursor Analysis API", version="2.1.0-Hybrid")

extractor = NLPFeatureExtractor()
model = SIFModel()
explainer = RiskExplainer()

class AnalyzeRequest(BaseModel):
    text: str
    report_id: str = None
    report_type: str = "Unsafe Act"
    location: str = None
    equipment: str = None

@app.post("/analyze", response_model=ExplainableRiskResult)
def analyze_report(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
        
    try:
        report = StandardizedReportObject(
            report_id=req.report_id or str(uuid.uuid4()),
            report_type=req.report_type,
            location=req.location,
            equipment=req.equipment,
            raw_text=req.text,
            cleaned_text=clean_text(req.text)
        )
        
        features = extractor.extract_features(report)
        prediction = model.predict(features)
        explanation = explainer.explain(report, features, prediction)
        
        # Log to monitoring service
        monitor.log_prediction(explanation.risk_level, explanation.human_review_recommended)
        
        return explanation
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok", "monitoring": monitor.check_drift()}
