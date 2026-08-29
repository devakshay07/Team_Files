import sys
import os
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.api.app import app

client = TestClient(app)

def test_invalid_inputs():
    print("Testing API Contracts and Robustness...")
    
    # 1. Empty Text
    res = client.post("/analyze", json={"text": ""})
    assert res.status_code == 400
    
    # 2. Missing Text Field
    res = client.post("/analyze", json={"report_type": "Near Miss"})
    assert res.status_code == 422 # FastAPI standard validation error
    
    # 3. Wrong Types
    res = client.post("/analyze", json={"text": 12345})
    # FastAPI casts int to string for text fields, so it might pass, let's see.
    
    # 4. Extremely Large Request
    res = client.post("/analyze", json={"text": "A" * 100000})
    assert res.status_code == 200 # Should handle it gracefully
    
    # 5. Unexpected Fields
    res = client.post("/analyze", json={"text": "Test", "hacked_field": True})
    assert res.status_code == 200 # Pydantic ignores extra fields by default
    
    print("✅ API Robustness & Contract tests PASSED.")

if __name__ == "__main__":
    test_invalid_inputs()
