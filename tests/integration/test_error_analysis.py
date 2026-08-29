import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.api.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

TEST_CASES = [
    {"label": "Clear SIF Precursor", "text": "Worker fell from 20ft scaffold. Harness failed."},
    {"label": "Non-SIF Report", "text": "Papercut in office."},
    {"label": "Ambiguous", "text": "Loud noise near the pump."},
    {"label": "Short", "text": "Tripped."},
    {"label": "Long", "text": "On Tuesday morning around 10 AM, the worker was walking down the hallway. He stopped to tie his shoe, and then proceeded to the control room. Nothing else happened."},
    {"label": "Missing Info", "text": "Incident occurred."},
    {"label": "Spelling Variations", "text": "Wrker did not wear harns and almost fel."},
    {"label": "Terminology Variation", "text": "Lanyard was not tied off."},
    {"label": "Multiple Hazards", "text": "Spill on floor led to slip, worker fell into energized panel."},
    {"label": "Negation", "text": "Worker safely descended using full fall protection. LOTO was correctly applied."},
    {"label": "Misleading Keywords", "text": "We had a safety meeting about fatalities and critical risks."},
    {"label": "Implied Danger", "text": "He stepped on the skylight."}
]

def run_error_analysis():
    print("=== DEEP ERROR ANALYSIS ===")
    results = []
    for tc in TEST_CASES:
        res = client.post("/analyze", json={"text": tc["text"]})
        if res.status_code == 200:
            data = res.json()
            print(f"[{tc['label']}]")
            print(f"  Text: {tc['text']}")
            print(f"  Risk: {data['risk_level']} (Conf: {data['confidence']:.2f})")
            print(f"  Precursors: {data['detected_precursors']}")
            print(f"  Keywords: {data['supporting_evidence'].get('keywords', [])}")
            print("-" * 50)
            results.append(data)
        else:
            print(f"ERROR on {tc['label']}: {res.text}")
            
if __name__ == "__main__":
    run_error_analysis()
