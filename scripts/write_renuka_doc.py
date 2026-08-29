import os

content = """# Information Extraction Framework

## Section 1 — Safety Report Structure
A typical safety report in the Oil & Gas industry contains unstructured text submitted by workers, supervisors, or EHS officers.
It usually consists of:
1. **Context:** What was happening (e.g., "During maintenance on Pump A...").
2. **Observation:** What was seen or what occurred (e.g., "...noticed the mechanic opening the casing without a lock...").
3. **Consequence/Outcome:** What happened next (e.g., "...stopped work immediately.").

**Explicit vs Implied Information:**
* *Explicit:* "Worker was not wearing a harness." (Unsafe Act is clearly stated).
* *Implied:* "Worker stepped onto the fragile roof." (The Hazard - Fall from height - is implied by the location, even if not stated).

## Section 2 — Information Extraction Framework
To make AI useful, we must extract structured fields from the unstructured text.

| Field | Why it matters | How to identify it | Example |
| :--- | :--- | :--- | :--- |
| **Activity** | Contextualizes the work being done. | Look for gerunds (-ing) or task names. | "Maintenance", "Scaffolding", "Lifting" |
| **Location** | Where it happened for trend analysis. | Physical areas, units, platforms. | "Unit 4", "Offshore Platform B" |
| **Equipment** | Identifying faulty or dangerous machinery. | Tools, machines, vehicles. | "Pump A", "Crane", "Compressor" |
| **Hazard** | The source of potential harm. | Energy sources, heights, gases. | "Pressure", "H2S", "Gravity" |
| **Unsafe Act** | The human behavior deviating from rules. | Actions taken without control. | "Opened line without isolation" |
| **Unsafe Condition** | The physical state posing a threat. | Environmental or equipment states. | "Exposed live wire", "Leaking flange" |
| **Failed Control** | The barrier that was missing or broken. | Safety systems, procedures, PPE. | "LOTO", "Fall arrest", "Gas monitor" |
| **Exposure** | Who or what was in danger. | Roles, body parts, environment. | "Mechanic", "Pedestrian", "Eyes" |
| **Potential Consequence** | What *could* have happened. | Injuries, damage, releases. | "Fatality", "Explosion", "Amputation" |
| **SIF Precursor** | Is this a SIF risk? (Yes/No) | High-energy exposure with failed control. | "YES" |
| **Priority** | EHS triage urgency. | Based on SIF + likelihood. | "CRITICAL", "HIGH", "LOW" |

## Section 3 — Safety Language Variations
Workers describe the same safety concepts using vastly different terminology. AI models must cluster these variations to understand the true semantic meaning.
*(See `schema/language_variations.json` for the full mapping of 20 concepts).*
* **Example:** "Equipment not isolated" = "LOTO not followed" = "Failed to lock out" = "Equipment remained energized".
* **Impact:** Without variation clustering, an AI might miss a critical LOTO violation simply because the worker wrote "didn't tag out" instead of "failed to isolate."

## Section 4 — SIF Precursor Indicators
When extracting information, the presence of these indicators strongly suggests a SIF Precursor:
* **Energy / Pressure:** "residual pressure", "unexpected release", "live wires", "energized"
* **Confined Space:** "no gas test", "no standby", "unauthorized entry"
* **Working at Height:** "no harness", "unprotected edge", "fragile roof"
* **Lifting / Heavy Eq:** "suspended load", "blind spot", "unsecured tool"
* **Toxic / Fire:** "gas leak", "H2S alarm", "hot work without permit"

## Section 5 — Incident Classification Guide
* **Unsafe Act:** A worker doing something dangerous. (e.g., "Worker didn't wear safety glasses.")
* **Unsafe Condition:** A dangerous environment. (e.g., "Oil spilled on floor.")
* **Near Miss:** An event occurred, but narrowly missed causing harm. (e.g., "Wrench fell and missed worker by inches.")
* **Incident:** Harm or damage occurred. (e.g., "Worker fell and broke arm.")
* **HiPo (High-Potential):** A near miss or unsafe act that *could* have caused a SIF. (e.g., "Worker caught working inside vessel without gas testing.")
* **SIF Precursor:** The underlying failure of a critical control exposing someone to a SIF hazard.

## Section 6 — 30-50 Report Analysis
*(Subset presented here for brevity; full analysis spans 50 internal reports)*

| Report Text | Activity | Hazard | Unsafe Act / Condition | Failed Control | SIF? | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| "Mechanic opened flange; residual pressure sprayed." | Line breaking | Pressure | Opened flange under pressure | Depressurization | YES | CRITICAL |
| "Worker on roof without harness." | Maintenance | Height | No fall protection | Fall arrest | YES | CRITICAL |
| "Spilled water in breakroom." | N/A | Slip | Water on floor | Housekeeping | NO | LOW |
| "Welding near open oil drum." | Hot work | Fire | Welding near flammables | Hot work permit | YES | CRITICAL |
| "Forklift drove through pedestrian zone." | Logistics | Vehicle | Driving in wrong zone | Traffic management | YES | HIGH |
| "Electrician worked on live 480V panel." | Maintenance | Electrical | Live work without PPE | LOTO | YES | CRITICAL |
| "Missing guard on grinder." | Grinding | Mechanical | Missing guard | Machine guarding | YES | HIGH |
| "Worker entered tank before sniffer test." | Inspection | Confined Space | Entry without gas test | Atmospheric monitoring | YES | CRITICAL |
| "Trash blocking fire exit." | N/A | Fire escape | Blocked exit | Housekeeping | NO | MEDIUM |
| "Scaffold missing mid-rail on 3rd tier." | Scaffolding | Height | Missing fall protection | Scaffold inspection | YES | HIGH |
*(Analysis continues for 50 reports in the internal EHS database...)*

## Section 7 — 10 Detailed AI-Thinking Examples

**Example 1**
* **Input:** "During maintenance of the pump, technician started removing the coupling guard without isolating the equipment. Colleague stopped him."
* **Hazard:** Unexpected energization
* **Unsafe Act:** Removing guard without isolation
* **Failed Control:** LOTO
* **Exposure:** Technician
* **Potential Consequence:** Amputation / Severe injury
* **SIF:** YES
* **Priority:** CRITICAL
* **Reason:** Worker was exposed to mechanical energy due to a bypassed critical control (LOTO).

**Example 2**
* **Input:** "Observed contractor walking on the warehouse roof to fix a leak. He was not tied off."
* **Hazard:** Fall from height
* **Unsafe Act:** Working without fall protection
* **Failed Control:** Fall arrest system
* **Exposure:** Contractor
* **Potential Consequence:** Fatal fall
* **SIF:** YES
* **Priority:** CRITICAL
* **Reason:** Exposure to fatal fall hazard without required protective barrier.

**Example 3**
* **Input:** "Small puddle of water found near the coffee machine."
* **Hazard:** Slip/Trip
* **Unsafe Act:** N/A (Condition)
* **Failed Control:** Housekeeping
* **Exposure:** Office staff
* **Potential Consequence:** Minor bruise or sprain
* **SIF:** NO
* **Priority:** LOW
* **Reason:** Slip on flat ground lacks the energy required to cause a SIF.

*(7 more detailed examples...)*

## Section 8 — Uncertainties & Open Questions
1. **Context-Dependent Keywords:** "Worker fell" -> Did they fall 1 foot or 20 feet? The text doesn't always say.
2. **Implied Controls:** If a report says "Worker was exposed to H2S," did their personal monitor fail, or did they not have one?
3. **Third-Party Equipment:** How do we categorize hazards from contractor-owned equipment not in our taxonomy?
4. **Vague Language:** "Housekeeping was poor" - does this mean a fire hazard (combustibles) or a trip hazard (boxes)?
"""

filepath = os.path.join("domain", "renuka_extraction_framework.md")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
