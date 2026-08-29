from pydantic import BaseModel, ConfigDict
from typing import Optional

class SafetyReportSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    report_id: str
    report_text: str
    report_type: str
    sif_label: str
    hazard_category: str
    severity: str
    unsafe_act: Optional[str] = None
    unsafe_condition: Optional[str] = None
    potential_consequence: Optional[str] = None
    failed_control: Optional[str] = None
    location: Optional[str] = None
    equipment: Optional[str] = None
    source: str = "synthetic"
    immediate_action: Optional[str] = None
    intervention: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    work_stopped: Optional[bool] = None

from typing import Optional, List

class ModelPrediction(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    sif_precursor: bool
    confidence: float
    hazard_category: str
    failed_control: str
    explanation: str
    priority: str
    evidence_keywords: List[str] = []
    immediate_action: Optional[str] = None
    intervention: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    work_stopped: Optional[bool] = None
