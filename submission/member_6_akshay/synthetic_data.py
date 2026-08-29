import random
import uuid
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from schema.extraction_schema import SafetyReportSchema as SafetyReport

# Predefined templates to generate synthetic text
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
        is_sif = random.random() < 0.05 # 5% SIF class imbalance
        
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
        
        # Add some noise (empty texts, HTML tags, exact duplicates to test deduplication)
        noise_roll = random.random()
        
        # Increase text entropy to prevent over-deduplication
        worker_id = random.randint(1000, 9999)
        day = random.randint(1, 28)
        text = f"[Oct {day}] Report by W-{worker_id}: {text}"

        if noise_roll < 0.02:
            text = "" # empty
        elif noise_roll < 0.05:
            text = f"<div><p>{text}</p></div>" # HTML noise
            
        report = SafetyReport(
            report_id=str(uuid.uuid4()),
            report_text=text,
            report_type=report_type,
            sif_label=sif_label,
            hazard_category=hazard,
            severity=severity,
            location=location,
            equipment=equipment,
            immediate_action=random.choice(["stopped work", "reported to supervisor", None]),
            intervention=random.choice(["colleague intervened", "supervisor intervened", None]),
            corrective_action=random.choice(["replaced equipment", "cleaned up", None]),
            preventive_action=random.choice(["updated procedures", "retrained staff", None]),
            work_stopped=random.choice([True, False, None])
        )
        records.append(report)
        
        # Inject exact duplicates to test data leakage prevention
        if random.random() < 0.03:
            duplicate = report.model_copy(update={'report_id': str(uuid.uuid4())})
            records.append(duplicate)
            
    # Convert to DataFrame
    df = pd.DataFrame([r.model_dump() for r in records])
    return df

if __name__ == "__main__":
    df = generate_synthetic_data(1000)
    df.to_csv("synthetic_reports.csv", index=False)
    print(f"Generated {len(df)} synthetic reports and saved to synthetic_reports.csv")
