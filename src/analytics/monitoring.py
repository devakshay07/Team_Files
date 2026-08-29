import logging
import json
import os
from typing import Dict, Any

logger = logging.getLogger(__name__)

class DriftMonitor:
    """
    Monitors incoming real-world safety reports for dataset shift.
    Persists data to a local JSONL file to survive application restarts.
    """
    
    def __init__(self, log_path: str = None):
        if log_path is None:
            self.log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "monitoring_logs.jsonl")
        else:
            self.log_path = log_path
            
        self.total_predictions = 0
        self.human_reviews_requested = 0
        self.risk_distribution = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}
        
        self._load_state()
        
    def _load_state(self):
        if not os.path.exists(self.log_path):
            return
            
        try:
            with open(self.log_path, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    record = json.loads(line)
                    self.total_predictions += 1
                    risk = record.get("risk_level", "UNKNOWN")
                    self.risk_distribution[risk] = self.risk_distribution.get(risk, 0) + 1
                    if record.get("human_review", False):
                        self.human_reviews_requested += 1
        except Exception as e:
            logger.error(f"Failed to load monitoring state: {e}")

    def log_prediction(self, risk_level: str, human_review: bool):
        self.total_predictions += 1
        self.risk_distribution[risk_level] = self.risk_distribution.get(risk_level, 0) + 1
        if human_review:
            self.human_reviews_requested += 1
            
        # Persist
        try:
            log_dir = os.path.dirname(self.log_path)
            if log_dir:
                os.makedirs(log_dir, exist_ok=True)
            with open(self.log_path, 'a') as f:
                f.write(json.dumps({"risk_level": risk_level, "human_review": human_review}) + "\n")
        except Exception as e:
            logger.error(f"Failed to persist monitoring log: {e}")
            
    def check_drift(self) -> Dict[str, Any]:
        """
        Calculates simple drift metrics. If human reviews exceed 20% of traffic,
        it signals that the NLP vocabulary or ML model is struggling with new data.
        """
        if self.total_predictions < 100:
            return {"status": "insufficient_data"}
            
        review_rate = self.human_reviews_requested / self.total_predictions
        
        status = "healthy"
        if review_rate > 0.20:
            status = "degraded - high ambiguity"
            logger.warning("Data drift detected: Human review rate exceeded 20%.")
            
        return {
            "status": status,
            "total_predictions": self.total_predictions,
            "human_review_rate": round(review_rate, 4),
            "distribution": self.risk_distribution
        }

monitor = DriftMonitor()
