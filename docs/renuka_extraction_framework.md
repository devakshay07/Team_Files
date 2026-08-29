# Information Extraction Framework

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

| Field | Why it matters | How to identify it | Example | None | None | None | None | None |
| :--- | :--- | :--- | :--- |
| **Activity** | Contextualizes the work being done. | Look for gerunds (-ing) or task names. | "Maintenance", "Scaffolding", "Lifting" | None | None | None | None | None |
| **Location** | Where it happened for trend analysis. | Physical areas, units, platforms. | "Unit 4", "Offshore Platform B" | None | None | None | None | None |
| **Equipment** | Identifying faulty or dangerous machinery. | Tools, machines, vehicles. | "Pump A", "Crane", "Compressor" | None | None | None | None | None |
| **Hazard** | The source of potential harm. | Energy sources, heights, gases. | "Pressure", "H2S", "Gravity" | None | None | None | None | None |
| **Unsafe Act** | The human behavior deviating from rules. | Actions taken without control. | "Opened line without isolation" | None | None | None | None | None |
| **Unsafe Condition** | The physical state posing a threat. | Environmental or equipment states. | "Exposed live wire", "Leaking flange" | None | None | None | None | None |
| **Failed Control** | The barrier that was missing or broken. | Safety systems, procedures, PPE. | "LOTO", "Fall arrest", "Gas monitor" | None | None | None | None | None |
| **Exposure** | Who or what was in danger. | Roles, body parts, environment. | "Mechanic", "Pedestrian", "Eyes" | None | None | None | None | None |
| **Potential Consequence** | What *could* have happened. | Injuries, damage, releases. | "Fatality", "Explosion", "Amputation" | None | None | None | None | None |
| **SIF Precursor** | Is this a SIF risk? (Yes/No) | High-energy exposure with failed control. | "YES" | None | None | None | None | None |
| **Priority** | EHS triage urgency. | Based on SIF + likelihood. | "CRITICAL", "HIGH", "LOW" |
| **Immediate Action Taken** | Response right after observation. | "stopped work", "evacuated" | "Work stopped immediately" | None | None | None | None | None |
| **Intervention** | Who intervened. | "supervisor stepped in", "co-worker yelled" | "Colleague stopped him" | None | None | None | None | None |
| **Corrective Action** | What was done to fix. | "replaced lock", "cleaned spill" | "Replaced harness" | None | None | None | None | None |
| **Preventive Action** | Long term fix. | "updated procedure", "re-trained" | "Updated LOTO SOP" | None | None | None | None | None |
| **Work Stopped** | Was a stop-work authority used? | "stopped", "paused" | "Yes" | None | None | None | None | None |

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

## Section 5 — Incident Classification
* **Unsafe Act:** A worker doing something dangerous. (e.g., "Worker didn't wear safety glasses.")
* **Unsafe Condition:** A dangerous environment. (e.g., "Oil spilled on floor.")
* **Near Miss:** An event occurred, but narrowly missed causing harm. (e.g., "Wrench fell and missed worker by inches.")
* **Incident:** Harm or damage occurred. (e.g., "Worker fell and broke arm.")
* **HiPo (High-Potential):** A near miss or unsafe act that *could* have caused a SIF. (e.g., "Worker caught working inside vessel without gas testing.")
* **SIF Precursor:** The underlying failure of a critical control exposing someone to a SIF hazard.

## Section 6 — 30-50 Report Analysis
*

| Report Text | Activity | Hazard | Unsafe Act / Condition | Failed Control | SIF? | Priority | Immediate Action | Intervention | Corrective Action | Preventive Action | Work Stopped |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| "Mechanic opened flange; residual pressure sprayed." | Line breaking | Pressure | Opened flange under pressure | Depressurization | YES | CRITICAL | None | None | None | None | None |
| "Worker on roof without harness." | Maintenance | Height | No fall protection | Fall arrest | YES | CRITICAL | None | None | None | None | None |
| "Spilled water in breakroom." | N/A | Slip | Water on floor | Housekeeping | NO | LOW | None | None | None | None | None |
| "Welding near open oil drum." | Hot work | Fire | Welding near flammables | Hot work permit | YES | CRITICAL | None | None | None | None | None |
| "Forklift drove through pedestrian zone." | Logistics | Vehicle | Driving in wrong zone | Traffic management | YES | HIGH | None | None | None | None | None |
| "Electrician worked on live 480V panel." | Maintenance | Electrical | Live work without PPE | LOTO | YES | CRITICAL | None | None | None | None | None |
| "Missing guard on grinder." | Grinding | Mechanical | Missing guard | Machine guarding | YES | HIGH | None | None | None | None | None |
| "Worker entered tank before sniffer test." | Inspection | Confined Space | Entry without gas test | Atmospheric monitoring | YES | CRITICAL | None | None | None | None | None |
| "Trash blocking fire exit." | N/A | Fire escape | Blocked exit | Housekeeping | NO | MEDIUM | None | None | None | None | None |
| "Scaffold missing mid-rail on 3rd tier." | Scaffolding | Height | Missing fall protection | Scaffold inspection | YES | HIGH | None | None | None | None | None |
| "Worker found sleeping in truck." | Rest | Fatigue | Sleeping on job | Supervision | NO | MEDIUM | None | None | None | None | None |
| "Crane lifted load over busy walkway." | Lifting | Suspended Load | Lifted over pedestrians | Lift Plan | YES | CRITICAL | None | None | None | None | None |
| "H2S monitor alarmed, worker continued working." | Maintenance | Toxic Gas | Ignored alarm | Gas Monitoring | YES | CRITICAL | None | None | None | None | None |
| "Loose tools left on top tier of scaffold." | Scaffolding | Dropped Object | Unsecured tools | Housekeeping | YES | HIGH | None | None | None | None | None |
| "Papercut from printer." | Office | Sharp object | N/A | N/A | NO | LOW | None | None | None | None | None |
| "Driver reversed truck without a spotter." | Logistics | Vehicle | No spotter | Spotter | YES | CRITICAL | None | None | None | None | None |
| "Puddle of oil on the rig floor." | Drilling | Slip | Oil spill | Containment | NO | LOW | None | None | None | None | None |
| "Started pump while mechanic was still checking alignment." | Maintenance | Mechanical | Unexpected startup | LOTO | YES | CRITICAL | None | None | None | None | None |
| "Missing fire extinguisher at hot work site." | Hot work | Fire | Missing equipment | Hot work permit | YES | HIGH | None | None | None | None | None |
| "Unsecured ladder slipped, worker fell 3 ft." | Access | Height | Unsecured ladder | Ladder safety | NO | MEDIUM | None | None | None | None | None |
| "Entered excavation without shoring." | Digging | Trench collapse | Unshored entry | Shoring | YES | CRITICAL | None | None | None | None | None |
| "Safety glasses worn on forehead while grinding." | Grinding | Mechanical | Improper PPE | PPE compliance | NO | MEDIUM | None | None | None | None | None |
| "Bypassed door interlock to speed up machine." | Operation | Mechanical | Bypassed safety | Machine guarding | YES | CRITICAL | None | None | None | None | None |
| "Found frayed extension cord in puddle." | Maintenance | Electrical | Damaged equipment | Inspection | YES | HIGH | None | None | None | None | None |
| "Smelled gas near compressor, did not report." | Operation | Gas release | Failure to report | Gas detection | YES | HIGH | None | None | None | None | None |
| "Worker used a bucket as a step stool." | Access | Height | Makeshift elevation | Proper access | NO | MEDIUM | None | None | None | None | None |
| "Dropped a heavy wrench from the derrick." | Drilling | Dropped object | Dropped tool | Tool securing | YES | CRITICAL | None | None | None | None | None |
| "Opened wrong valve, released hot steam." | Operation | Pressure | Incorrect valve | Procedure | YES | CRITICAL | None | None | None | None | None |
| "Not wearing gloves while handling rough lumber." | Carpentry | Splinters | No gloves | PPE compliance | NO | LOW | None | None | None | None | None |
| "Tied fall arrest lanyard to a weak pipe." | Maintenance | Height | Improper anchor | Anchor selection | YES | CRITICAL | None | None | None | None | None |
| "Confined space hole watch was looking at phone." | Confined Space | Asphyxiation | Distracted standby | Hole watch | YES | HIGH | None | None | None | None | None |


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
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
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
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
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
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Slip on flat ground lacks the energy required to cause a SIF.

**Example 4**
* **Input:** "Worker entered the confined space vessel to retrieve a dropped wrench without checking the atmosphere."
* **Hazard:** Toxic gas / Oxygen deficiency
* **Unsafe Act:** Entry without gas testing
* **Failed Control:** Atmospheric monitoring
* **Exposure:** Worker
* **Potential Consequence:** Asphyxiation / Fatality
* **SIF:** YES
* **Priority:** CRITICAL
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Entering a confined space without verifying air quality is a known fatality precursor.

**Example 5**
* **Input:** "Forklift driver was seen reversing out of the loading bay without a spotter. Almost hit a pedestrian."
* **Hazard:** Vehicle-pedestrian collision
* **Unsafe Act:** Reversing without spotter
* **Failed Control:** Spotter / Traffic management
* **Exposure:** Pedestrian
* **Potential Consequence:** Fatal run-over
* **SIF:** YES
* **Priority:** CRITICAL
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Blind reversing near pedestrians frequently leads to fatalities.

**Example 6**
* **Input:** "Employee was using a utility knife to open a box and wasn't wearing cut-resistant gloves."
* **Hazard:** Sharp object
* **Unsafe Act:** Not wearing required gloves
* **Failed Control:** PPE compliance
* **Exposure:** Employee's hands
* **Potential Consequence:** Laceration / Stitches
* **SIF:** NO
* **Priority:** MEDIUM
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Lacerations from small knives are recordable but do not cause serious permanent disability or death.

**Example 7**
* **Input:** "Electrician opened the 480V panel to troubleshoot. He was not wearing an arc flash suit."
* **Hazard:** Electrical / Arc flash
* **Unsafe Act:** Live work without proper PPE
* **Failed Control:** Arc flash boundary / PPE
* **Exposure:** Electrician
* **Potential Consequence:** Fatal burns / Electrocution
* **SIF:** YES
* **Priority:** CRITICAL
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** High-voltage exposure without protective gear is a direct SIF precursor.

**Example 8**
* **Input:** "The crane was lifting a 5-ton pipe bundle. Noticed a worker walking directly underneath the suspended load."
* **Hazard:** Suspended load / Gravity
* **Unsafe Act:** Walking under load
* **Failed Control:** Exclusion zone / Barricade
* **Exposure:** Worker
* **Potential Consequence:** Fatal crushing
* **SIF:** YES
* **Priority:** CRITICAL
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Massive kinetic energy overhead; failure of barricade control.

**Example 9**
* **Input:** "Mechanic unbolted the flange on the cooling water line before checking if it was fully drained."
* **Hazard:** Low pressure liquid
* **Unsafe Act:** Line breaking without verifying zero energy
* **Failed Control:** Verification
* **Exposure:** Mechanic
* **Potential Consequence:** Wet clothing / minor slip
* **SIF:** NO
* **Priority:** LOW
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Cooling water does not have the pressure or toxicity to cause a SIF, unlike a hydrocarbon or high-pressure steam line.

**Example 10**
* **Input:** "Found a heavy crescent wrench left sitting unsecured on the top level of the scaffolding, right above the main entrance."
* **Hazard:** Dropped object
* **Unsafe Act:** Leaving tools unsecured at height
* **Failed Control:** Housekeeping / Tool lanyards
* **Exposure:** Personnel entering the building
* **Potential Consequence:** Fatal struck-by injury
* **SIF:** YES
* **Priority:** HIGH
* **Immediate Action**: None
* **Intervention**: None
* **Corrective Action**: None
* **Preventive Action**: None
* **Work Stopped**: None
* **Reason:** Even without an immediate unsafe act (no one knocked it over *yet*), the unsafe condition poses a direct fatal threat.

## Section 8 — Uncertainties & Open Questions
1. **Context-Dependent Keywords:** "Worker fell" -> Did they fall 1 foot or 20 feet? The text doesn't always say.
2. **Implied Controls:** If a report says "Worker was exposed to H2S," did their personal monitor fail, or did they not have one?
3. **Third-Party Equipment:** How do we categorize hazards from contractor-owned equipment not in our taxonomy?
4. **Vague Language:** "Housekeeping was poor" - does this mean a fire hazard (combustibles) or a trip hazard (boxes)?
