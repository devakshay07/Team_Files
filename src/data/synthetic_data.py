import random
import uuid
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import StandardizedReportObject

SIF_TEMPLATES = [
    "During maintenance of the {equipment} at {location}, the technician started work without isolating the equipment. The {equipment} was still energized.",
    "Worker entered the confined space at {location} without conducting a gas test. No standby person was present.",
    "While working at {location}, worker was at height without fall protection. Serious risk of fatal fall.",
    "Line opened with residual pressure on the {equipment}. High-energy release narrowly missed the operator."
]

NON_SIF_TEMPLATES = [
    "Worker observed not wearing safety glasses at {location}.",
    "Trip hazard due to loose cables near {equipment}. Cables were immediately organized.",
    "Small oil spill near {equipment} at {location}. Cleaned up promptly.",
    "Worker used incorrect gloves for manual handling task. Supervisor corrected the action."
]

HAZARDS = ["Energy Isolation", "Confined Space", "Working at Height", "Pressure", "Electrical", "Slips/Trips", "Manual Handling"]
LOCATIONS = ["Unit A", "Unit B", "Offshore Platform 1", "Refinery Sector 4"]
EQUIPMENTS = ["Pump", "Compressor", "Heat Exchanger", "Valve", "Electrical Panel"]

def generate_synthetic_data(num_records: int = 1000) -> pd.DataFrame:
    records = []
    
    for _ in range(num_records):
        is_sif = random.random() < 0.05 
        
        hazard = random.choice(HAZARDS)
        location = random.choice(LOCATIONS)
        equipment = random.choice(EQUIPMENTS)
        
        if is_sif:
            sif_label = "YES"
            report_type = random.choice(["Unsafe Act", "Near Miss"])
            severity = random.choice(["HIGH", "CRITICAL"])
            text = random.choice(SIF_TEMPLATES).format(equipment=equipment, location=location)
            hazard = random.choice(["Energy Isolation", "Confined Space", "Working at Height", "Pressure"])
        else:
            sif_label = "NO"
            report_type = random.choice(["Unsafe Act", "Unsafe Condition"])
            severity = random.choice(["LOW", "MEDIUM"])
            text = random.choice(NON_SIF_TEMPLATES).format(equipment=equipment, location=location)
        
        noise_roll = random.random()
        worker_id = random.randint(1000, 9999)
        
        # FIX: Do not inject '[Oct X] Report by W-XXXX:' as it creates a domain mismatch 
        # where the model learns metadata artifacts instead of genuine safety language.
        raw_text = text
        cleaned_text = text 

        if noise_roll < 0.02:
            raw_text = "" 
            cleaned_text = ""
        elif noise_roll < 0.05:
            raw_text = f"<div><p>{raw_text}</p></div>"
            
        report = StandardizedReportObject(
            report_id=str(uuid.uuid4()),
            report_type=report_type,
            location=location,
            equipment=equipment,
            raw_text=raw_text,
            cleaned_text=cleaned_text,
            available_labels={
                "sif_label": sif_label,
                "hazard_category": hazard,
                "severity": severity,
                "immediate_action": random.choice(["stopped work", "reported to supervisor", None]),
                "intervention": random.choice(["colleague intervened", "supervisor intervened", None]),
                "corrective_action": random.choice(["replaced equipment", "cleaned up", None]),
                "preventive_action": random.choice(["updated procedures", "retrained staff", None]),
                "work_stopped": random.choice([True, False, None])
            }
        )
        records.append(report)
        
        if random.random() < 0.03:
            duplicate = report.model_copy(update={'report_id': str(uuid.uuid4())})
            records.append(duplicate)
            
    # Flatten the dict for pandas
    flattened = []
    for r in records:
        d = r.model_dump()
        labels = d.pop('available_labels', {})
        d.update(labels)
        flattened.append(d)
        
    df = pd.DataFrame(flattened)
    return df

if __name__ == "__main__":
    df = generate_synthetic_data(1000)
    df.to_csv("data/synthetic_reports.csv", index=False)
    print(f"Generated {len(df)} synthetic reports and saved to data/synthetic_reports.csv")
