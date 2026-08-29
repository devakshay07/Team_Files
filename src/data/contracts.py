from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class StandardizedReportObject(BaseModel):
    """Output from Member 1 (Data Engineering)"""
    report_id: str
    report_type: str  # Unsafe Act, Unsafe Condition, Near Miss
    timestamp: Optional[datetime] = None
    location: Optional[str] = None
    department: Optional[str] = None
    equipment: Optional[str] = None
    raw_text: str
    cleaned_text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    available_labels: Dict[str, Any] = Field(default_factory=dict)

class NLPFeatureObject(BaseModel):
    """Output from Member 2 (NLP Feature Extraction)"""
    text_embedding: Optional[List[float]] = None
    extracted_entities: Dict[str, List[str]] = Field(default_factory=dict)
    hazard_features: List[str] = Field(default_factory=list)
    consequence_features: List[str] = Field(default_factory=list)
    exposure_features: List[str] = Field(default_factory=list)
    control_failure_features: List[str] = Field(default_factory=list)
    semantic_features: Dict[str, float] = Field(default_factory=dict)
    feature_metadata: Dict[str, Any] = Field(default_factory=dict)

class PredictionObject(BaseModel):
    """Output from Member 3 (SIF Detection Model)"""
    sif_risk_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    confidence: float
    precursor_categories: List[str] = Field(default_factory=list)
    model_version: str
    human_review_recommended: bool = False
    prediction_metadata: Dict[str, Any] = Field(default_factory=dict)

class ExplainableRiskResult(BaseModel):
    """Output from Member 4 (Explainability & Risk Scoring)"""
    risk_level: str
    confidence: float
    detected_precursors: List[str] = Field(default_factory=list)
    supporting_evidence: Dict[str, Any] = Field(default_factory=dict)
    contributing_factors: List[str] = Field(default_factory=list)
    similar_reports: List[str] = Field(default_factory=list)
    human_review_recommended: bool = False
    analytics_metadata: Dict[str, Any] = Field(default_factory=dict)
