from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.api.app import app

client = TestClient(app)

def test_api():
    print("Testing API /analyze endpoint...")
    response = client.post(
        "/analyze",
        json={
            "text": "While working at Unit B, worker was at height without fall protection. Serious risk of fatal fall.",
            "report_type": "Near Miss",
            "location": "Unit B"
        }
    )
    assert response.status_code == 200, f"Error: {response.text}"
    data = response.json()
    print("API Response:")
    print(data)
    assert "risk_level" in data
    assert "confidence" in data
    assert "supporting_evidence" in data
    
    print("\n✅ API Integration test PASSED.")

if __name__ == "__main__":
    test_api()
