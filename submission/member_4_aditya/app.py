from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from schema.extraction_schema import ModelPrediction
from model.inference import predict

app = FastAPI(title="SIF Precursor Analysis API", version="1.0.0")

class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze", response_model=ModelPrediction)
def analyze_report(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    try:
        result = predict(req.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
