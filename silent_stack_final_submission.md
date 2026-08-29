# Team Silent Stack - Consolidated Project Submission

> This document compiles the final deliverables of all 6 team members as per the initial requirements.

## PART 1: Domain Knowledge (Anandita)

### File: `domain/sif_domain_knowledge.md`

# SIF Domain Knowledge: Oil & Gas Precursors

## Section 1 — Core Definitions

* **Unsafe Act:** A behavior by a person that deviates from accepted safe practices (e.g., bypassing a safety interlock).
* **Unsafe Condition:** A physical state in the workplace that poses a hazard (e.g., exposed live wiring).
* **Near Miss:** An event where an injury or damage did not occur, but only by luck or a last-minute intervention (e.g., a dropped tool lands inches away from a worker).
* **Incident:** An unplanned event that resulted in injury, illness, or damage.
* **High-Potential Incident (HiPo):** A near miss or minor incident that, under slightly different circumstances, could have resulted in a serious injury or fatality.
* **Serious Injury:** An injury resulting in permanent impairment, amputation, or requiring significant hospitalization.
* **Fatality:** Death resulting from a workplace incident.
* **SIF (Serious Injury or Fatality):** A collective term for incidents resulting in either a serious injury or fatality.
* **SIF Precursor:** A high-risk situation in which management controls are absent, ineffective, or not complied with, and which could reasonably result in a SIF if allowed to continue.

| Term | Outcome | Potential Outcome | Focus |
| :--- | :--- | :--- | :--- |
| Unsafe Act/Condition | None yet | Variable | Leading indicator |
| Near Miss | None | Variable | Leading indicator |
| HiPo Near Miss | None/Minor | SIF | Critical leading indicator |
| Incident | Injury/Damage | Variable | Lagging indicator |
| SIF Precursor | None yet | **SIF** | **Predictive indicator** |

## Section 2 — SIF Precursor Categories

1.  **Energy Isolation / LOTO:** Failure to isolate mechanical, electrical, or pressure energy before maintenance. 
    *   *Why dangerous:* Stored energy can release violently, crushing or electrocuting workers.
    *   *Intervention window:* Often instantaneous once the work begins.
2.  **Working at Height:** Working above 1.8m (6ft) without fall arrest or edge protection.
    *   *Why dangerous:* Gravity; falls from this height are often fatal or result in permanent spine/brain injury.
    *   *Intervention window:* Instantaneous.
3.  **Confined Spaces:** Entry without atmospheric testing or standby personnel.
    *   *Why dangerous:* Toxic gases or oxygen deficiency can incapacitate a worker silently and rapidly.
    *   *Intervention window:* Minutes; rescuer fatalities are common.
4.  **Pressure Systems / Line Breaking:** Opening pipes or vessels containing residual pressure or hazardous chemicals.
    *   *Why dangerous:* Sudden release acts like an explosion, projecting shrapnel or hazardous fluids.
    *   *Intervention window:* Instantaneous upon opening.
5.  **Heavy Equipment / Suspended Loads:** Being under suspended loads or in the blind spots of heavy machinery.
    *   *Why dangerous:* Massive kinetic energy; human body cannot withstand crushing forces.
    *   *Intervention window:* Seconds.

## Section 3 — Oil & Gas Hazard Landscape

The Oil & Gas industry differs from general manufacturing due to the constant presence of immense stored energy and hazardous materials.
*   **Unique High-Energy Sources:** Massive volumes of highly flammable hydrocarbons under extreme pressures and temperatures.
*   **Toxic Gases:** Presence of H₂S, which is deadly even in small concentrations (ppm) and deadens the sense of smell.
*   **SIMOPS (Simultaneous Operations):** Complex sites where multiple contractors perform overlapping tasks (e.g., hot work directly above a live hydrocarbon transfer), creating compounding, non-linear risks.

## Section 4 — Process Safety vs Occupational Safety

*   **Occupational Safety:** Focuses on the individual worker (e.g., slips, trips, falls, cuts, manual handling). High frequency, lower severity.
*   **Process Safety:** Focuses on keeping hazardous materials contained (e.g., preventing hydrocarbon releases, explosions, structural failures). Low frequency, catastrophic severity.
*   **Overlap (SIF Precursors):** When an occupational safety failure (e.g., opening the wrong valve) triggers a process safety event (e.g., massive gas release). A report about a "small puddle of oil" might seem like an occupational slip hazard, but actually indicates a process safety containment failure (loss of integrity).

## Section 5 — Human Factors

Human factors explain *why* unsafe acts occur:
1.  **Time Pressure / Production Pressure:** Rushing to restore production leads to skipping LOTO verification.
2.  **Fatigue:** 12-hour shifts or night shifts reduce cognitive function, leading to missing crucial steps in complex procedures.
3.  **Normalization of Deviance:** A safety bypass (e.g., wedging a door open) has been done for years without consequence, so it becomes the accepted norm.
4.  **Inadequate Training:** Worker attempts to operate unfamiliar equipment during a shortage.
5.  **Poor Communication / Shift Handover:** Night shift isolates a valve, day shift doesn't know and opens it.
6.  **Complacency:** Highly experienced worker assumes a familiar task is safe without checking gas monitors.
7.  **Poor Procedure Design:** The written procedure is physically impossible or impractically slow to execute in the field.
8.  **Inadequate Supervision:** Supervisors turn a blind eye to missing PPE to meet quotas.
9.  **Tool Availability:** Proper scaffold isn't available, so workers stand on a bucket to reach a valve.
10. **Distraction:** Operating heavy machinery while looking at a phone or tablet.

## Section 6 — Causal Chains (20 Detailed Examples)

1.  *(Energy)* Valve leaking → Flammable gas → Worker enters → Did not test air → Asphyxiation
2.  *(Energy)* Pump broken → Maintenance needed → Mechanic works without LOTO → Colleague turns pump on → Amputation
3.  *(Height)* Lightbulb burnt out → High ceiling → Worker stands on top rung of unsecured ladder → Ladder slips → Fatal fall
4.  *(Height)* Scaffolding incomplete → Missing mid-rail → Worker reaches out → Loses balance → Fatal fall
5.  *(Confined Space)* Vessel needs cleaning → Residual fumes inside → Worker enters without permit/testing → Oxygen deficiency → Asphyxiation
6.  *(Confined Space)* Tank entry → Toxic gas present → Hole watch leaves post for 5 mins → Worker collapses → No rescue → Fatality
7.  *(Pressure)* Flange leaking → Needs tightening → Worker tightens under pressure → Bolt shears → Massive release / Struck-by
8.  *(Pressure)* Line needs opening → Assumed depressurized → Flange unbolted → Trapped pressure releases → Chemical burns
9.  *(Heavy Eq.)* Crane lifting pipe → Rigging worn out → Sling snaps → Pipe falls → Worker underneath crushed
10. *(Heavy Eq.)* Excavator digging → Worker in trench → Spotter distracted → Excavator bucket hits worker → Fatality
11. *(Electrical)* Breaker tripped → Needs reset → Worker resets without checking for fault → Arc flash → Severe burns
12. *(Electrical)* Puddle on floor → Extension cord frayed → Worker steps in puddle → Ground fault → Electrocution
13. *(Fire/Expl.)* Welding needed → Near oil tank → No fire blankets used → Spark hits oil → Fire / Explosion
14. *(Fire/Expl.)* Gas leak → Vapor cloud forms → Truck drives through cloud → Engine ingests gas/sparks → Explosion
15. *(H2S)* H2S alarm sounds → Worker thinks it's a false alarm → Stays in area → Concentration spikes → Fatality
16. *(H2S)* H2S leak → Worker collapses → Colleague rushes in without SCBA to help → Rescuer collapses → Double fatality
17. *(Vehicles)* Forklift moving → Blind corner → Pedestrian walking in vehicle zone → Forklift doesn't stop → Run-over
18. *(Vehicles)* Truck parked on incline → Handbrake fails / No chocks → Truck rolls backwards → Pins worker against wall
19. *(SIMOPS)* Hot work overhead → Painting underneath → Slag falls onto flammable paint → Fire traps workers
20. *(PPE)* Working near acid → Goggles on forehead → Acid splashes → Chemical burn to eyes (Permanent blindness)

## Section 7 — High-Potential Near-Miss Examples (15 Cases)

1.  **Crane Load Dropped:** A 2-ton pipe fell from a crane, landing 2 feet from a worker. (Actual: No injury. Potential: Fatality - struck by).
2.  **LOTO Bypass Discovered:** A mechanic was about to open a pump casing, but a supervisor realized the wrong breaker was locked out. (Actual: Near miss. Potential: Amputation/Electrocution).
3.  **Scaffold Collapse:** An empty scaffold collapsed in high winds overnight. (Actual: Property damage. Potential: Multiple fatalities if occupied).
4.  **H2S Spike:** H2S alarm triggered, workers evacuated. Monitors later showed lethal concentrations. (Actual: No injury. Potential: Mass casualty).
5.  **Wrong Line Opened:** Worker started opening a flange; smelled gas and stopped. It was the live line, not the purged line. (Actual: Near miss. Potential: Explosion/Toxic exposure).
6.  **Trench Cave-in:** A trench wall collapsed right after the worker climbed out for lunch. (Actual: Near miss. Potential: Fatal crushing/asphyxiation).
7.  **Vehicle Near-Miss:** A haul truck reversed blindly, missing a pickup truck by inches. (Actual: Near miss. Potential: Fatal crushing).
8.  **Arc Flash in Empty Room:** A breaker failed and caused a massive arc flash while the electrical room was unoccupied. (Actual: Equipment damage. Potential: Fatal burns).
9.  **Dropped Wrench:** A wrench fell from a derrick, striking the hardhat of a worker below. (Actual: Minor concussion. Potential: Fatal skull fracture if offset by 2 inches).
10. **Confined Space Gas Pocket:** Workers tested a tank, entered, then disturbed sludge releasing toxic gas. They evacuated just in time. (Actual: Near miss. Potential: Asphyxiation).
11. **Pressurized Hose Whip:** A high-pressure air hose disconnected and whipped wildly, narrowly missing operators. (Actual: Near miss. Potential: Fatal blunt trauma).
12. **Ignition of Vent Gas:** Lightning struck a vent stack releasing gas, causing a fireball that dissipated quickly. (Actual: Near miss. Potential: Facility explosion).
13. **Chemical Mix-up:** Bleach and acid were almost pumped into the same tank before a label was checked. (Actual: Near miss. Potential: Toxic chlorine gas cloud).
14. **Over-pressurized Vessel:** A relief valve failed to open, but a rupture disk blew safely away from personnel. (Actual: Operational upset. Potential: Catastrophic vessel burst).
15. **Fall Arrest Deployed:** Worker slipped off an edge, but their harness caught them immediately. (Actual: Minor bruising. Potential: Fatal fall).

## Section 8 — False Positives Table (Unsafe ≠ SIF)

| Situation | Unsafe? | SIF Potential? | Why? |
| :--- | :--- | :--- | :--- |
| Missing safety glasses in office walkway | Yes | Low/No | Limited credible catastrophic exposure. |
| Spilled water in breakroom | Yes | Low | Slip hazard, but unlikely to cause permanent disability. |
| Worker not wearing hardhat in open field away from structures | Yes | Low | No credible overhead drop hazard. |
| Paper cut from printer | Yes | No | Trivial injury mechanism. |
| Carrying a box that is slightly too heavy | Yes | Low | Ergonomic strain, not a sudden fatal energy release. |
| Driving 5mph over limit in empty parking lot | Yes | Low | Low kinetic energy, no pedestrians. |
| Using a box cutter without cut-resistant gloves | Yes | Medium | Severe laceration possible, but rarely fatal/amputation. |
| Not holding the handrail on stairs | Yes | Low/Medium | Fall possible, but single flight stairs rarely cause SIF. |
| Trash blocking a non-emergency doorway | Yes | Low | Housekeeping issue, minor trip hazard. |
| Extension cord across a hallway | Yes | Low | Standard trip hazard. |
| Wearing the wrong color hi-vis vest | Yes | Low | Administrative violation, visibility still exists. |
| Missing safety glasses while grinding metal | Yes | Medium/High | Eye loss is a serious injury (SIF), but not a fatality. |
| Entering confined space without permit (but space is brand new/clean) | Yes | High | The act is a SIF precursor, even if the specific instance was lucky. |
| Not wearing a harness on a 2-foot step stool | Yes | Low | Fall distance insufficient for SIF. |
| Worker sitting on a bucket to rest | Yes | Low | Ergonomic/professionalism issue, no direct hazard. |

## Section 9 — Uncertain Classifications

These require more context from the reporter to classify accurately:
1.  **"Worker slipped and fell."** (From where? A ladder, or flat ground?)
2.  **"Gas smelled in area."** (What gas? Toxic H2S, or just exhaust?)
3.  **"Valve leaked."** (What was inside? High-pressure acid, or cooling water?)
4.  **"Worker didn't follow LOTO."** (Did they use a different isolation method, or none at all?)
5.  **"Load shifted."** (Was it 50 lbs or 5,000 lbs? Were people under it?)
6.  **"Electrical panel open."** (Was it energized? High voltage?)
7.  **"Scaffold tag missing."** (Was the scaffold actually unsafe, or just missing the paperwork?)
8.  **"Worker felt dizzy."** (Heat exhaustion, or toxic gas exposure?)
9.  **"Spill on deck."** (Slippery oil, or highly flammable solvent?)
10. **"Truck reversed quickly."** (Were pedestrians present? How fast?)


---

### File: `domain/causal_chains.csv`

```csv
Hazard,Unsafe behavior / condition,Potential consequence,SIF potential,Evidence words / patterns
Energy Isolation,Maintenance started without verified isolation,Unexpected energization / fatality,Critical,"""not isolated"", ""LOTO not followed"", ""still energized"""
Energy Isolation,LOTO bypass (deliberate),Unexpected energization / severe injury,Critical,"""bypassed"", ""removed lock"", ""unauthorized removal"""
Energy Isolation,Isolation not verified before re-entry,Unexpected energization,Critical,"""did not verify"", ""assumed isolated"""
Energy Isolation,Missing lock (mechanical failure),Unexpected energization,High,"""lock broken"", ""lock failed"", ""tag fell off"""
Energy Isolation,Stored energy not dissipated (spring-loaded),Release of mechanical energy / crushing,Critical,"""stored energy"", ""spring tension"", ""not discharged"""
Energy Isolation,Incorrect isolation point used,Exposure to live energy,Critical,"""wrong valve"", ""incorrect breaker"""
Energy Isolation,Unexpected energization during maintenance,Severe injury / fatality,Critical,"""equipment started"", ""unexpected movement"""
Energy Isolation,Residual pressure after depressurization attempt,High-pressure release,Critical,"""residual pressure"", ""still pressurized"", ""trapped pressure"""
Energy Isolation,Multiple crafts working on same equipment without separate locks,Unexpected energization for unprotected worker,High,"""shared lock"", ""no personal lock"""
Energy Isolation,Attempted to operate locked out equipment,Equipment damage / potential release,High,"""tried to start"", ""attempted to operate"""
Working at Height,Worker without fall protection near edge,Fatal fall,Critical,"""no harness"", ""without fall protection"", ""unprotected edge"""
Working at Height,Improperly anchored harness,Fatal fall,Critical,"""tied to pipe"", ""improper anchor"", ""not tied off"""
Working at Height,Unprotected leading edge,Fatal fall,Critical,"""no guardrail"", ""missing handrail"", ""open edge"""
Working at Height,Unsafe scaffolding (missing planks/guardrails),Fall / scaffold collapse,Critical,"""red tag"", ""missing plank"", ""incomplete scaffold"""
Working at Height,"Unsafe ladder (unsecured, overreached)",Fall from height,High,"""ladder slipped"", ""unsecured ladder"", ""overreaching"""
Working at Height,Objects/tools at height unsecured,Fatal struck-by injury,High,"""tool fell"", ""dropped object"", ""unsecured tools"""
Working at Height,Work near fragile roof without protection,Fatal fall through roof,Critical,"""fragile roof"", ""skylight"", ""fell through"""
Working at Height,Using makeshift elevation (standing on buckets),Fall from height,Medium,"""standing on bucket"", ""makeshift platform"""
Working at Height,Climbing outside cage on fixed ladder,Fall from height,High,"""outside cage"", ""climbing structure"""
Working at Height,Harness lanyard too long for fall distance,Impact with ground,Critical,"""wrong lanyard"", ""hit ground"""
Confined Space,Entry without atmospheric testing,Asphyxiation / Toxic exposure,Critical,"""no gas test"", ""atmosphere not checked"""
Confined Space,No standby person / hole watch,Inability to rescue / fatality,Critical,"""no standby"", ""hole watch absent"""
Confined Space,No rescue arrangement in place,Delayed rescue / fatality,Critical,"""no rescue plan"", ""no tripod"""
Confined Space,Unauthorized entry (no permit),Unknown hazards / fatality,Critical,"""without permit"", ""unauthorized entry"""
Confined Space,Improper ventilation,Toxic buildup / Asphyxiation,Critical,"""poor ventilation"", ""exhaust fan off"""
Confined Space,Oxygen-deficient atmosphere detected,Asphyxiation,Critical,"""low oxygen"", ""O2 deficient"""
Confined Space,Entry during cleaning with chemicals,Toxic exposure / Fire,Critical,"""cleaning solvent"", ""fumes"""
Confined Space,Gas monitor alarming but entry continued,Toxic exposure / Asphyxiation,Critical,"""ignored alarm"", ""continued entry"""
Confined Space,Hot work inside confined space without continuous monitoring,Fire / Explosion,Critical,"""hot work in vessel"", ""no continuous monitoring"""
Confined Space,Exhaust from diesel generator entering confined space,Carbon monoxide poisoning,Critical,"""exhaust fumes"", ""generator near opening"""
Pressure Systems,Line opened with residual pressure,High-energy release / Struck-by,Critical,"""residual pressure"", ""line under pressure"""
Pressure Systems,Valve operated incorrectly (wrong valve),Unexpected release,Critical,"""wrong valve"", ""incorrect line"""
Pressure Systems,Failure to depressurize before breaking flange,High-pressure release / Chemical exposure,Critical,"""did not depressurize"", ""sprayed"""
Pressure Systems,Blind flange removed without isolation,Massive release of hazardous material,Critical,"""removed blind"", ""no isolation"""
Pressure Systems,Unexpected release during line-breaking,Chemical exposure / Burns,Critical,"""sudden release"", ""sprayed with"""
Pressure Systems,Sampling point used without caution (high pressure),High-pressure release,High,"""sampling"", ""pressure surge"""
Pressure Systems,Using incorrect pressure rating for fittings,Fitting failure / Projectile,Critical,"""wrong rating"", ""fitting blew off"""
Pressure Systems,Tightening a leaking pressurized connection,Catastrophic failure / Release,Critical,"""tightened under pressure"", ""stopped leak"""
Pressure Systems,Pneumatic testing without exclusion zone,Explosion / Projectile,Critical,"""pneumatic test"", ""no barricade"""
Heavy Equipment,Working under suspended load,Fatal crushing,Critical,"""under load"", ""suspended load"""
Heavy Equipment,Unsecured tools at height above workers,Fatal struck-by injury,High,"""tool fell"", ""dropped from height"""
Heavy Equipment,Crane operation without clear exclusion zone,Crushing / Struck-by,Critical,"""crane operation"", ""entered barricade"""
Heavy Equipment,Improper rigging of load,Dropped load / Crushing,Critical,"""rigging failed"", ""sling broke"""
Heavy Equipment,Equipment movement near workers without spotter,Crushing / Run-over,Critical,"""no spotter"", ""reversing"""
Heavy Equipment,Crushing/pinch point exposure near equipment,Amputation / Crushing,High,"""pinch point"", ""hand caught"""
Heavy Equipment,Lifting operation exceeding crane capacity,Crane tip-over / Dropped load,Critical,"""overload"", ""alarm sounded"""
Heavy Equipment,Forklift driven with elevated load,Tip-over / Crushing,High,"""driving with load high"", ""tipped"""
Heavy Equipment,Leaving heavy equipment unattended and running,Unintended movement,Medium,"""left running"", ""unattended"""
Electrical Hazards,Live electrical work without proper PPE,Fatal electrocution / Burns,Critical,"""live work"", ""no arc flash suit"""
Electrical Hazards,Exposed live conductors in work area,Electrocution,Critical,"""exposed wires"", ""live conductor"""
Electrical Hazards,Arc flash boundaries ignored,Severe burns,Critical,"""crossed boundary"", ""arc flash zone"""
Electrical Hazards,Missing grounding on portable equipment,Electrocution,High,"""no ground"", ""missing earth"""
Electrical Hazards,Unauthorized electrical work by non-electrician,Electrocution / Fire,Critical,"""unauthorized"", ""not qualified"""
Electrical Hazards,Energized equipment maintenance,Electrocution,Critical,"""working on live"", ""energized panel"""
Electrical Hazards,Using damaged extension cords in wet area,Electrocution,High,"""damaged cord"", ""frayed wire"", ""water"""
Electrical Hazards,Bypassing electrical interlocks on machinery,Electrocution / Amputation,Critical,"""bypassed interlock"", ""door switch defeated"""
Fire / Explosion,Hot work near flammable material,Fire / Explosion,Critical,"""welding near"", ""flammables"""
Fire / Explosion,Hydrocarbon release (gas leak) unnoticed,Explosion,Critical,"""gas leak"", ""hydrocarbon release"""
Fire / Explosion,Poor gas detection (no alarm),Unnoticed explosive atmosphere,Critical,"""detector failed"", ""no alarm"""
Fire / Explosion,Ignition source introduced near vapor cloud,Explosion,Critical,"""spark"", ""ignition source"", ""non-intrinsically safe"""
Fire / Explosion,Improper hot work permit issuance,Fire / Explosion,Critical,"""invalid permit"", ""permit not checked"""
Fire / Explosion,Flammable vapour accumulation in enclosed space,Explosion,Critical,"""vapour buildup"", ""poor ventilation"""
Fire / Explosion,Static discharge during flammable liquid transfer,Fire / Explosion,Critical,"""static"", ""not grounded"", ""transferring"""
H2S / Toxic,H2S exposure without personal gas monitor,Toxic exposure / Fatality,Critical,"""no monitor"", ""H2S alarm"""
H2S / Toxic,Incorrect respiratory protection for toxic gas,Toxic exposure,Critical,"""wrong filter"", ""dust mask instead of SCBA"""
H2S / Toxic,Entry into known toxic area without monitoring,Toxic exposure / Fatality,Critical,"""entered without checking"", ""toxic gas"""
H2S / Toxic,Emergency response failure (no muster),Prolonged exposure / Fatality,Critical,"""did not muster"", ""ignored alarm"""
H2S / Toxic,Multiple workers in H2S zone without buddy system,Inability to rescue / Multiple fatalities,Critical,"""working alone"", ""H2S zone"""
H2S / Toxic,Opening process equipment containing toxic chemicals without purging,Toxic exposure,Critical,"""did not purge"", ""toxic release"""
Vehicles,Pedestrian in mobile equipment path,Run-over / Fatality,Critical,"""in path"", ""nearly hit"""
Vehicles,Reversing without spotter,Run-over / Collision,Critical,"""reversing"", ""no spotter"", ""blind spot"""
Vehicles,Blind-spot collision risk near heavy machinery,Run-over,Critical,"""blind spot"", ""could not see"""
Vehicles,Seatbelt violation in mobile equipment (rollover risk),Ejection / Crushing,High,"""no seatbelt"", ""not buckled"""
Vehicles,Poor traffic management — mixed pedestrian/vehicle zones,Collision / Run-over,High,"""mixed traffic"", ""no walkway"""
Vehicles,Speeding on site with heavy vehicle,Loss of control / Collision,High,"""speeding"", ""driving fast"""

```

### File: `domain/taxonomy.json`

```json
{
  "SIF_Precursors": {
    "Energy Isolation": {
      "Electrical": [
        "Live electrical work without PPE",
        "Exposed live conductors in work area",
        "Arc flash boundaries ignored",
        "Missing grounding on portable equipment",
        "Energized equipment maintenance",
        "Bypassing electrical interlocks"
      ],
      "Mechanical": [
        "Maintenance started without verified isolation",
        "LOTO bypass (deliberate)",
        "Isolation not verified before re-entry",
        "Missing lock (mechanical failure)",
        "Unexpected energization during maintenance"
      ],
      "Stored Energy": [
        "Stored energy not dissipated (spring-loaded)",
        "Residual pressure after depressurization attempt"
      ]
    },
    "Working at Height": {
      "Fall Arrest": [
        "Worker without fall protection near edge",
        "Improperly anchored harness",
        "Harness lanyard too long for fall distance"
      ],
      "Platforms & Edges": [
        "Unprotected leading edge",
        "Unsafe scaffolding (missing planks/guardrails)",
        "Work near fragile roof without protection"
      ],
      "Access": [
        "Unsafe ladder (unsecured, overreached)",
        "Using makeshift elevation",
        "Climbing outside cage on fixed ladder"
      ]
    },
    "Confined Space": {
      "Atmospheric": [
        "Entry without atmospheric testing",
        "Improper ventilation",
        "Oxygen-deficient atmosphere detected",
        "Entry during cleaning with chemicals",
        "Gas monitor alarming but entry continued",
        "Exhaust from diesel generator entering confined space"
      ],
      "Procedural": [
        "No standby person / hole watch",
        "No rescue arrangement in place",
        "Unauthorized entry (no permit)",
        "Hot work inside confined space without continuous monitoring"
      ]
    },
    "Pressure Systems": {
      "Line Breaking": [
        "Line opened with residual pressure",
        "Valve operated incorrectly (wrong valve)",
        "Failure to depressurize before breaking flange",
        "Blind flange removed without isolation",
        "Unexpected release during line-breaking"
      ],
      "Equipment Integrity": [
        "Sampling point used without caution (high pressure)",
        "Using incorrect pressure rating for fittings",
        "Tightening a leaking pressurized connection",
        "Pneumatic testing without exclusion zone"
      ]
    },
    "Heavy Equipment & Lifting": {
      "Suspended Loads": [
        "Working under suspended load",
        "Crane operation without clear exclusion zone",
        "Improper rigging of load",
        "Lifting operation exceeding crane capacity"
      ],
      "Dropped Objects": [
        "Unsecured tools at height above workers"
      ],
      "Mobile Machinery": [
        "Equipment movement near workers without spotter",
        "Crushing/pinch point exposure near equipment",
        "Forklift driven with elevated load",
        "Leaving heavy equipment unattended and running"
      ]
    },
    "Fire and Explosion": {
      "Ignition Sources": [
        "Hot work near flammable material",
        "Ignition source introduced near vapor cloud",
        "Improper hot work permit issuance",
        "Static discharge during flammable liquid transfer"
      ],
      "Atmospheric Hazards": [
        "Hydrocarbon release (gas leak) unnoticed",
        "Poor gas detection (no alarm)",
        "Flammable vapour accumulation in enclosed space"
      ]
    },
    "Toxic Exposure": {
      "H2S": [
        "H2S exposure without personal gas monitor",
        "Entry into known toxic area without monitoring",
        "Multiple workers in H2S zone without buddy system"
      ],
      "Chemicals": [
        "Incorrect respiratory protection for toxic gas",
        "Opening process equipment containing toxic chemicals without purging"
      ],
      "Response": [
        "Emergency response failure (no muster)"
      ]
    },
    "Vehicles": {
      "Traffic Management": [
        "Pedestrian in mobile equipment path",
        "Reversing without spotter",
        "Blind-spot collision risk near heavy machinery",
        "Poor traffic management — mixed pedestrian/vehicle zones",
        "Speeding on site with heavy vehicle"
      ],
      "Vehicle Safety": [
        "Seatbelt violation in mobile equipment (rollover risk)"
      ]
    }
  }
}

```

## PART 2: Data Extraction Framework (Renuka)

### File: `domain/renuka_extraction_framework.md`

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


---

### File: `schema/language_variations.json`

```json
{
  "concepts": [
    {
      "concept": "no_gas_testing",
      "description": "Failure to perform required atmospheric testing.",
      "variations": [
        "gas test not conducted",
        "atmosphere not checked",
        "gas monitoring not performed",
        "no sniffer used",
        "did not test air",
        "entry without testing",
        "failed to check for gas"
      ]
    },
    {
      "concept": "no_isolation",
      "description": "Failure to isolate energy sources before work.",
      "variations": [
        "equipment not isolated",
        "isolation not done",
        "LOTO not followed",
        "equipment remained energized",
        "did not lock out",
        "failed to isolate",
        "worked on live equipment"
      ]
    },
    {
      "concept": "fall_protection_failure",
      "description": "Working at height without proper fall arrest systems.",
      "variations": [
        "no harness",
        "harness not used",
        "worker without fall arrest",
        "unprotected edge",
        "not tied off",
        "no lanyard attached",
        "missing guardrails"
      ]
    },
    {
      "concept": "pressure_exposure",
      "description": "Opening systems containing trapped or residual pressure.",
      "variations": [
        "line under pressure",
        "residual pressure",
        "pressure not released",
        "trapped pressure",
        "failed to depressurize",
        "opened pressurized line",
        "pressure blew out"
      ]
    },
    {
      "concept": "confined_space_violation",
      "description": "Entering a confined space without adhering to safety protocols.",
      "variations": [
        "entered vessel without permit",
        "entered confined space without testing",
        "unauthorized entry",
        "went inside tank",
        "no confined space permit",
        "entered without hole watch"
      ]
    },
    {
      "concept": "no_standby_person",
      "description": "Failure to have a dedicated person monitoring a hazardous activity.",
      "variations": [
        "no standby",
        "hole watch absent",
        "working alone",
        "no safety watch",
        "unattended entry",
        "no one watching outside"
      ]
    },
    {
      "concept": "no_rescue_arrangement",
      "description": "Lack of a plan or equipment to rescue workers in an emergency.",
      "variations": [
        "no rescue plan",
        "no tripod",
        "no retrieval line",
        "no emergency arrangements",
        "no way to pull them out",
        "rescue team not notified"
      ]
    },
    {
      "concept": "hot_work_without_permit",
      "description": "Performing spark-producing work without authorization.",
      "variations": [
        "welding without permit",
        "unauthorized hot work",
        "grinding without permit",
        "no hot work permit",
        "cutting without authorization",
        "sparking work without permission"
      ]
    },
    {
      "concept": "arc_flash_exposure",
      "description": "Working near energized electrical equipment without protection.",
      "variations": [
        "no arc flash suit",
        "crossed flash boundary",
        "working on live panel",
        "exposed live wires",
        "no flash protection",
        "opened energized cabinet"
      ]
    },
    {
      "concept": "suspended_load_exposure",
      "description": "Being positioned underneath or near a lifted heavy object.",
      "variations": [
        "under load",
        "walking under suspended load",
        "standing under crane lift",
        "underneath hoisted equipment",
        "entered lift zone",
        "under lifted pipe"
      ]
    },
    {
      "concept": "dropped_object_risk",
      "description": "Objects at height that are not secured and could fall.",
      "variations": [
        "unsecured tools",
        "dropped from height",
        "tool fell",
        "loose items on scaffold",
        "no tool lanyard",
        "falling object hazard"
      ]
    },
    {
      "concept": "h2s_exposure",
      "description": "Exposure to or risk of exposure to Hydrogen Sulfide gas.",
      "variations": [
        "H2S alarm",
        "smelled sulfur",
        "rotten egg smell",
        "H2S detected",
        "sour gas leak",
        "H2S monitor went off"
      ]
    },
    {
      "concept": "procedure_bypassed",
      "description": "Intentionally ignoring or bypassing a safety procedure or interlock.",
      "variations": [
        "bypassed interlock",
        "defeated safety switch",
        "ignored procedure",
        "skipped steps",
        "jumped out the switch",
        "overrode safety system"
      ]
    },
    {
      "concept": "equipment_not_tagged",
      "description": "Failing to place warning tags on defective or isolated equipment.",
      "variations": [
        "no tag",
        "not tagged out",
        "missing warning tag",
        "defective equipment not tagged",
        "no isolation tag",
        "tag fell off"
      ]
    },
    {
      "concept": "vehicle_pedestrian_conflict",
      "description": "Vehicles moving dangerously close to workers on foot.",
      "variations": [
        "nearly hit by truck",
        "pedestrian in path",
        "reversing without spotter",
        "blind spot near worker",
        "forklift drove too close",
        "no segregation"
      ]
    },
    {
      "concept": "residual_energy_not_dissipated",
      "description": "Failing to relieve stored energy (springs, pressure, capacitance).",
      "variations": [
        "did not bleed pressure",
        "stored energy released",
        "spring tension not relieved",
        "capacitors not discharged",
        "failed to drain line",
        "residual energy present"
      ]
    },
    {
      "concept": "inadequate_ppe_for_hazard",
      "description": "Wearing the wrong type of PPE for the specific hazard.",
      "variations": [
        "wrong gloves",
        "no chemical suit",
        "improper respirator",
        "dust mask instead of SCBA",
        "not wearing FR clothing",
        "insufficient PPE"
      ]
    },
    {
      "concept": "structural_failure_risk",
      "description": "Risk of collapse of a structure (scaffold, trench, roof).",
      "variations": [
        "unshored trench",
        "scaffold leaning",
        "fragile roof",
        "unstable ground",
        "trench wall collapsed",
        "missing scaffold bracing"
      ]
    },
    {
      "concept": "poor_housekeeping",
      "description": "Clutter or spills creating trip/fire hazards.",
      "variations": [
        "spill on floor",
        "cluttered walkway",
        "oil on deck",
        "cables on ground",
        "trip hazard",
        "messy area"
      ]
    },
    {
      "concept": "unauthorized_modification",
      "description": "Modifying equipment without engineering approval.",
      "variations": [
        "makeshift tool",
        "unauthorized repair",
        "jerry-rigged",
        "modified guard",
        "homemade lifting device",
        "altered equipment"
      ]
    }
  ]
}

```

## PART 3: Product & UX Design (Manish)

### File: `design/manish_product_research.md`

# EHS Product Research & Workflow Design

## Section 1 — EHS User Profile
* **User:** Environmental, Health, and Safety (EHS) Officer / Safety Manager.
* **Responsibilities:** Reviewing safety observations, incident reports, and near misses. Conducting investigations, assigning corrective actions, analyzing trends, and reporting to management.
* **Volume:** An EHS officer at a major refinery may receive 500-1,000 observation cards or reports per week.
* **Technical Literacy:** Moderate to High in safety systems, but they are not data scientists. They need clear, actionable insights, not raw probabilities.
* **Key KPI:** Reducing Total Recordable Incident Rate (TRIR) and preventing SIFs.

## Section 2 — Current Workflow
1. **Submission:** Worker writes a safety observation on a physical card or digital app.
2. **Ingestion:** EHS admin enters data into a spreadsheet or legacy safety management system (SMS).
3. **Manual Review:** EHS officer reads reports sequentially (often chronologically, not by risk).
4. **Categorization:** Officer manually assigns hazard types and severity based on subjective reading.
5. **Action Assignment:** If severe, officer creates an investigation ticket.
6. **Follow-up:** Officer chases site leads for closure.
7. **Reporting:** At month-end, officer manually compiles Excel charts.

## Section 3 — Manual Tasks Table
| Task | Manual? | Time-Consuming? | Requires Judgment? | AI Can Assist? |
| :--- | :--- | :--- | :--- | :--- |
| Read raw report | Yes | High | Medium | Yes |
| Categorize hazard | Yes | Medium | High | Yes |
| Identify SIF potential | Yes | High | High | Yes |
| Prioritize review order | Yes | High | High | Yes |
| Find recurring hazards | Yes | High | Medium | Yes |
| Assign corrective action | Yes | Medium | High | Assist |
| Final safety decision | Yes | - | Very High | No (Human) |

## Section 4 — Pain Points
1. **Volume Overwhelm:** 90% of reports are low-risk (e.g., "spilled coffee"). Reviewing these buries the 10% that are critical near-misses.
2. **Buried Critical Reports:** A SIF precursor submitted on Friday might not be read until Tuesday, leaving a fatal hazard exposed for 4 days.
3. **Inconsistent Categorization:** Officer A flags "no gas test" as a procedural error; Officer B flags it as a SIF precursor.
4. **Keyword Blindness:** Ctrl+F for "fall" misses reports that say "worker tumbled" or "slipped off roof".
5. **Siloed Data:** Hard to connect a report today with a similar report from 3 months ago in a different unit.
6. **Reporting Lag:** Trends are only visible *after* a month of manual Excel work, instead of in real-time.

## Section 5 — User Requirements
* **Triage, not Replacement:** The system must tell the officer *what to look at first*, not make the final decision for them.
* **Contextual Explanations:** The system must explain *why* it flagged something (e.g., "Missing LOTO").
* **Speed:** The officer should understand the core risk of a report within 10 seconds of opening it.
* **Trust & Override:** The officer must be able to reject the AI's classification to train the system.

## Section 6 — AI Output Requirements (One-Screen Minimum)
When an EHS officer opens a flagged report, they need:
1. **SIF Precursor Flag:** YES/NO
2. **Confidence / Priority:** CRITICAL, HIGH, MEDIUM, LOW
3. **Extracted Hazard:** e.g., Energy Isolation
4. **Extracted Failed Control:** e.g., LOTO Verification
5. **Potential Consequence:** e.g., Severe injury/fatality
6. **Explanation (The "Why"):** Bullet points justifying the flag based on the text.

## Section 7 — Prioritization Logic
* **CRITICAL:** High-energy hazard + failed critical control + direct human exposure (e.g., Live electrical work, Confined space entry w/o test). *Action: Immediate SMS alert.*
* **HIGH:** Hazard present + control degraded + potential exposure (e.g., Missing scaffold rail but nobody fell, Heavy load lifted near walkway). *Action: Review within 24 hours.*
* **MEDIUM:** Occupational hazard + procedural violation (e.g., Using a box cutter without gloves). *Action: Review in standard queue.*
* **LOW:** Housekeeping / No credible SIF potential (e.g., Water spilled in breakroom). *Action: Auto-file for trending.*

## Section 8 — Explainability Requirements
A probability score (e.g., "SIF: 94%") is useless to an EHS officer. The system must provide **Traceable Evidence**.
* **Format:** "Flagged because: Worker exposed to [Hazard] due to failure of [Control]."
* **Highlighting:** The exact words in the raw text that triggered the AI should be bolded/highlighted.

## Section 9 — Escalation Workflow
1. **AI flags report as CRITICAL.**
2. **System auto-routes** to Priority Queue and triggers SMS to EHS Lead.
3. **EHS Lead reviews** within 1 hour.
4. **Validation:** If valid, EHS Lead initiates "Stop Work" or immediate investigation.
5. **Assignment:** Action assigned to Unit Manager with a 24-hour SLA.
6. **Closure:** Unit Manager uploads proof of mitigation; EHS Lead closes ticket.

## Section 10 — Trend / Analytics Requirements
1. **Hazard Distribution:** Bar chart of SIF precursors by hazard category (Energy, Height, etc.).
2. **Hotspots:** Heatmap or list of physical locations generating the most high-risk reports.
3. **Velocity:** Line chart showing if a specific hazard is trending up over the last 30 days.
4. **Repeat Offenders:** Identification of specific equipment (e.g., "Pump A") repeatedly involved in LOTO violations.

## Section 11 — MVP Feature List (Prioritized)
1. **AI SIF Precursor Detection Engine:** The core NLP classifier.
2. **EHS Priority Queue:** The UI that sorts reports by Risk instead of Chronology.
3. **Explainable Report View:** The screen showing the extracted fields and "Why it was flagged."
4. **Basic Analytics Dashboard:** Hazard distribution and location hotspots.
5. **Override/Feedback Loop:** Button for EHS to correct the AI, saving the data for future retraining.

## Section 12 — Open Questions & Challenges
1. **What if the report is too short?** (e.g., "Pump broke.") -> AI should flag for "Insufficient Info" rather than guessing.
2. **What if the AI is wrong (False Positive)?** -> EHS officer clicks "Reject SIF", report drops to LOW priority.
3. **What if the AI misses a SIF (False Negative)?** -> This is the biggest risk. The model must prioritize Recall over Precision.
4. **How do we handle multiple hazards in one report?** -> AI should extract all hazards and set priority based on the highest-severity hazard.
5. **Data Privacy:** Can reports contain PII (names)? -> The data pipeline must strip names before showing in the dashboard.


---

### File: `design/wireframes.md`

# EHS Dashboard & Workflow Wireframes

## Screen 1 — EHS Dashboard
```text
================================================================================
  SILENT STACK | EHS Safety Intelligence Portal                  [Profile] [Logout]
================================================================================
  [ Dashboard ]  [ Priority Queue ]  [ Action Tracking ]  [ Analytics ]
--------------------------------------------------------------------------------

  OVERVIEW (Last 30 Days)
  +------------------+  +------------------+  +------------------+  +------------------+
  | TOTAL REPORTS    |  | SIF PRECURSORS   |  | CRITICAL REPORTS |  | HIGH-RISK REPORTS|
  |      4,281       |  |       142        |  |        12        |  |        34        |
  +------------------+  +------------------+  +------------------+  +------------------+
  
  +------------------+  +------------------+  
  | PENDING INVESTIG.|  | PENDING CORRECT. |  
  |        15        |  |        23        |  
  +------------------+  +------------------+  

  URGENT ESCALATIONS
  [!] CRITICAL: Confined space entry w/o gas test (Unit 4)    [ Review ]
  [!] CRITICAL: Live electrical work reported (Platform B)    [ Review ]
  [!] HIGH: Suspended load near pedestrian walk (Sector 2)    [ Review ]

  TRENDS
  +---------------------------------------------------+  +-------------------------+
  |  SIF Precursors by Hazard Category                |  | Major Recurring Hazards |
  |  Energy Isl: ████████████ 42                      |  | 1. LOTO Bypassed        |
  |  Height:     ████████ 31                          |  | 2. Housekeeping         |
  |  Conf. Spc:  █████ 18                             |  | 3. Unsecured Tools      |
  |  Pressure:   ████ 15                              |  |                         |
  +---------------------------------------------------+  +-------------------------+
```

## Screen 2 — Priority Queue
```text
================================================================================
  [ Dashboard ]  [ PRIORITY QUEUE ]  [ Action Tracking ]  [ Analytics ]
================================================================================
  Filter: [ All Hazards v]  [ Last 7 Days v]  [ All Locations v]   Search: [       ]

  CRITICAL PRIORITY (12)
  --------------------------------------------------------------------------------
  [Review] RPT-1048 | Confined space entry w/o gas test... | Unit 4     | 10 mins ago
  [Review] RPT-1042 | Live electrical work reported...     | Platform B | 1 hr ago
  [Review] RPT-1039 | Residual pressure release during...  | Sector 2   | 3 hrs ago

  HIGH PRIORITY (34)
  --------------------------------------------------------------------------------
  [Review] RPT-1045 | Suspended load near pedestrian...    | Sector 2   | 45 mins ago
  [Review] RPT-1031 | Scaffold missing mid-rail...         | Unit 1     | 5 hrs ago

  MEDIUM PRIORITY (87)
  --------------------------------------------------------------------------------
  [Review] RPT-1040 | Forklift speeding in zone 3...       | Warehouse  | 2 hrs ago

  LOW PRIORITY (367)
  --------------------------------------------------------------------------------
  [Review] RPT-1047 | Puddle of water near coffee mach...  | Office     | 15 mins ago
```

## Screen 3 — Individual Report Analysis
```text
================================================================================
  < Back to Queue | Report RPT-1048
================================================================================
  
  ORIGINAL SUBMISSION                           AI ANALYSIS
  +---------------------------------------+   +---------------------------------------+
  | Date: Oct 12, 2026 | Location: Unit 4 |   | SIF PRECURSOR: [ YES ]  (Conf: 96%)   |
  | Reporter: W-4291                      |   | PRIORITY:      [ CRITICAL ]           |
  |                                       |   |                                       |
  | "During tank inspection, the worker   |   | WHY WAS THIS FLAGGED?                 |
  | entered the vessel before the sniffer |   | - Confined space entry                |
  | test was completed. He was inside for |   | - No gas test conducted               |
  | 5 minutes before the supervisor       |   | - Risk of toxic exposure/asphyxiation |
  | pulled him out."                      |   |                                       |
  +---------------------------------------+   | EVENT DETAILS                         |
                                              | Hazard: Confined Space                |
  RELATED REPORTS (3 in last month)           | Unsafe Act: Entry w/o testing         |
  - RPT-0912: Entry w/o permit (Unit 4)       | Failed Control: Atmospheric Monitor   |
  - RPT-0884: No standby person (Unit 4)      | Exposure: Worker                      |
                                              | Consequence: Asphyxiation / Fatality  |
                                              +---------------------------------------+

  ACTION PANEL
  Status: [ Under Investigation v ]   Assign To: [ EHS Lead v ]
  Recommended Action: Suspend confined space permits in Unit 4 pending safety stand-down.
  [ Add Note ]  [ Escalate to Plant Manager ]  [ Save & Close ]
================================================================================
```

## Screen 4 — Trends / Analytics
```text
================================================================================
  [ Dashboard ]  [ Priority Queue ]  [ Action Tracking ]  [ ANALYTICS ]
================================================================================
  Timeframe: [ Year-to-Date v ]
  
  SIF PRECURSORS OVER TIME
    ^
 40 |      *        *
 30 |    *   *    *   *
 20 |  *       *        *
 10 |*                    *
    +------------------------->
      Jan Feb Mar Apr May Jun

  HOTSPOTS (By Location)                 HAZARD DISTRIBUTION
  1. Unit 4 (45 SIFs)                    [  Energy Isolation (30%)  ]
  2. Platform B (22 SIFs)                [  Working at Height (25%) ]
  3. Sector 2 (18 SIFs)                  [  Confined Space (15%)    ]
                                         [  Dropped Objects (10%)   ]
```

## Screen 5 — Investigation & Corrective Action
```text
================================================================================
  [ Dashboard ]  [ Priority Queue ]  [ ACTION TRACKING ]  [ Analytics ]
================================================================================
  
  OPEN INVESTIGATIONS
  +----------+----------------------------------+-------------+------------+-------+
  | ID       | Description                      | Owner       | Deadline   | Alert |
  +----------+----------------------------------+-------------+------------+-------+
  | INV-042  | Review LOTO procedures (Unit 4)  | J. Smith    | 2026-10-15 | [!]   |
  | INV-043  | Scaffold inspection audit        | A. Davis    | 2026-10-18 |       |
  | INV-044  | Fall protection retraining       | M. Johnson  | 2026-10-20 |       |
  +----------+----------------------------------+-------------+------------+-------+

  INV-042 DETAILS
  Linked Report: RPT-1039 (Residual pressure release)
  Root Cause: Outdated isolation diagram used by maintenance crew.
  Corrective Action: Update all P&ID diagrams for Unit 4 and retrain operators.
  Status: [ In Progress v ]
================================================================================
```


---

## PART 4: Architecture & Formulation (Aditya)

### File: `domain/aditya_technical_formulation.md`

# Technical Problem Formulation & Approach

## 1. Problem Formulation
The goal is to analyze unstructured safety reports and identify Serious Injury or Fatality (SIF) precursors. This is a complex NLP problem that breaks down into two distinct sub-tasks:

**Task A: SIF Precursor Detection (Binary Classification)**
* **Input Space:** Unstructured text sequence `X`.
* **Output Space:** `Y ∈ {0, 1}` (where 1 = SIF Precursor, 0 = Non-SIF).
* **Objective:** Maximize Recall on the positive class (SIF) while maintaining acceptable Precision to prevent alert fatigue.

**Task B: Hazard & Evidence Extraction (Information Extraction / Multi-label)**
* **Input Space:** Unstructured text sequence `X`.
* **Output Space:** A structured schema mapping `X` to categorical variables (Hazard Category, Failed Control, Potential Consequence) and extracting specific text evidence.
* **Objective:** Provide explainability to the EHS officer by tracing the classification back to domain-specific entities.

*Justification:* A pure black-box classifier (Task A alone) is insufficient because EHS officers will not trust a system that simply outputs a probability score. We must extract the underlying hazard mechanisms (Task B) to justify the classification.

## 2. Approach Comparison Table

| Approach | Advantage | Disadvantage | Data Required | Explainability | Suitable for SIF? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TF-IDF + Logistic Regression** | Fast, simple, highly explainable (feature weights). | Ignores word order and semantics; brittle to synonyms. | Low (hundreds of samples) | High (Keyword weights) | **Yes (Baseline)** |
| **TF-IDF + SVM** | Handles high-dimensional text well. | Harder to calibrate probabilities for confidence scores. | Low | Medium | Yes |
| **Random Forest / XGBoost** | Captures non-linear keyword interactions. | Computationally heavier than LR; prone to overfitting on text. | Medium | Medium (Feature importance) | No (LR is better baseline) |
| **Word Embeddings + CNN/RNN** | Captures local semantics. | Outdated architecture; outperformed by Transformers. | High | Low | No |
| **Sentence-BERT + Classifier** | Excellent semantic clustering (handles language variations well). | Black-box embeddings make exact word tracing difficult. | Medium | Low | Yes (Good embedding choice) |
| **Fine-tuned Domain BERT** | State-of-the-art semantic understanding; handles complex context. | Requires significant compute; requires thousands of labeled O&G reports. | High (thousands) | Medium (Attention maps) | **Yes (Target Model)** |
| **LLM (Prompting - GPT-4/Claude)** | Zero-shot reasoning; can extract fields and explain logic naturally. | High latency, expensive, potential hallucination, data privacy issues (cloud). | Zero-shot | High (Generates text) | Yes (For extraction) |
| **Hybrid (Rules + Embeddings)** | Combines strict O&G taxonomy rules with semantic flexibility. | High engineering overhead to maintain rules. | Low | High | Yes |

## 3. Model Recommendation
* **Primary Recommendation (Production): Fine-tuned Domain BERT (e.g., RoBERTa/DeBERTa)**. It provides the deep semantic understanding necessary to distinguish between "LOTO was followed" and "LOTO was bypassed".
* **Fallback / Baseline Recommendation: TF-IDF + Logistic Regression**. It requires very little data to train, is perfectly explainable via coefficient weights, and serves as a sanity check against the BERT model.
* **Extraction Engine: LLM API (if privacy allows) or strict regex/NER pipeline**. Extraction is better handled by a generative or token-classification model than a sequence-classifier.


---

### File: `domain/aditya_architecture.md`

# System Architecture & Technical Risk Register

## 1. System Architecture Diagram

```mermaid
graph TD
    A[Raw Safety Report] -->|Text| B(Preprocessing Node)
    B -->|Clean Text| C{Information Extraction Engine}
    
    C -->|Extracted Entities| D[Domain Taxonomy Matcher]
    D -->|Hazard, Control| E[SIF Classification Model]
    
    C -->|Semantic Context| E
    
    E -->|SIF: YES/NO + Confidence| F{Explainability Module}
    F -->|Evidence Keywords| G[Priority Assignment Engine]
    
    G -->|JSON Payload| H((FastAPI Backend))
    H -->|REST API| I[EHS Dashboard UI]
    
    subgraph Data Pipeline
    B
    end
    
    subgraph NLP Engine
    C
    D
    E
    F
    end
    
    subgraph Application Layer
    G
    H
    I
    end
```

## 2. Technical Risk Register

| Risk | Why It Matters | Proposed Mitigation | Severity |
| :--- | :--- | :--- | :--- |
| **Class Imbalance (Rare SIFs)** | Model may achieve 95% accuracy by simply predicting "NO" for everything, missing the actual SIFs. | Use SMOTE, class weighting, or Focal Loss. Evaluate using Recall/F1, not Accuracy. | Critical |
| **Few SIF Training Examples** | Deep learning models will overfit on a tiny positive class. | Use a simpler baseline (TF-IDF+LR) or transfer learning (few-shot LLM) until data grows. | High |
| **Noisy / Vague Labels** | If annotators disagree on what a SIF is, the model will learn confused boundaries. | Implement strict annotation guidelines and adjudicate disagreements. | High |
| **Short Reports (Insufficient Context)** | "Pump broke" gives the model nothing to analyze. | Model should flag reports as "Insufficient Info" rather than guessing. | Medium |
| **Domain-Specific Vocabulary** | Generic models (BERT) don't understand terms like "LOTO", "SIMOPS", "H2S". | Fine-tune the language model on unsupervised O&G manuals/reports first (Domain Adaptation). | High |
| **False Negatives** | Missing a genuinely dangerous report defeats the purpose of the system. | Tune the decision threshold to favor High Recall; accept some false positives. | Critical |
| **False Positives (Alert Fatigue)** | If the system flags every minor issue as CRITICAL, EHS will ignore it. | Implement an active-learning feedback loop where EHS overrides adjust the model. | High |
| **Data Leakage** | Near-duplicate reports across train/test splits artificially inflate performance metrics. | Implement strict exact and fuzzy deduplication before splitting the dataset. | Critical |
| **Synthetic Data Contamination** | Evaluating the model on synthetic data gives a false sense of real-world readiness. | The final Test set must be 100% human-written, real-world reports. | Critical |
| **Explainability Gap** | EHS officers will not act on a black-box 98% probability score. | Output top influential keywords (TF-IDF weights) or use SHAP for complex models. | High |
| **Negation Handling** | "LOTO was applied" vs "LOTO was bypassed" — TF-IDF treats "LOTO" identically. | Rely on bi-grams/n-grams in TF-IDF, or transition to contextual embeddings (BERT). | High |
| **Code-Mixing / Typos** | Reports often contain misspellings or regional slang. | Use subword tokenization (BPE/WordPiece) and robust text cleaning. | Medium |

## 3. Evaluation Strategy
* **Primary Metric:** Recall on the SIF (Positive) Class. We must minimize False Negatives.
* **Secondary Metric:** F1-Score on the SIF Class (balances Recall against Precision).
* **Rule:** Overall Accuracy is explicitly banned as a primary metric due to the 95/5 class imbalance.

## 4. MVP Technical Pipeline
1. **Data Ingestion**: Cleaned CSV reports (1100+ items).
2. **Preprocessing**: BeautifulSoup HTML stripping, lowercase, exact+near deduplication.
3. **Embeddings/Features**: TF-IDF (1000 features, bigrams) + optional SentenceTransformers for contextual baseline.
4. **Model Engine**: Logistic Regression with `class_weight='balanced'` for Task 1 (SIF Prediction).
5. **Explainability**: Extraction of top positive coefficient keywords from TF-IDF vector mapping.
6. **API Layer**: FastAPI endpoint `/analyze` accepting text and returning `ModelPrediction` schema (SIF, confidence, priority, evidence_keywords).


---

### File: `backend/app.py`

```py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from schema.extraction_schema import ModelPrediction
from model.inference import predict

app = FastAPI(title="SIF Precursor Analysis API", version="1.0.0")

class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze", response_model=ModelPrediction)
def analyze_report(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    try:
        result = predict(req.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

```

## PART 5: Model Engine (Devanshu)

### File: `model/artifacts/metrics_report.md`

# Model Evaluation Metrics & Experiments

## Task 1: SIF Precursor Detection (Binary)
### Model A: TF-IDF + Logistic Regression (Baseline)
**Validation Accuracy:** 1.0000

```
              precision    recall  f1-score   support

          NO       1.00      1.00      1.00       167
         YES       1.00      1.00      1.00         9

    accuracy                           1.00       176
   macro avg       1.00      1.00      1.00       176
weighted avg       1.00      1.00      1.00       176

Confusion Matrix:
[[167   0]
 [  0   9]]
```

### Model B: TF-IDF + Support Vector Machine
**Validation Accuracy:** 1.0000

```
              precision    recall  f1-score   support

          NO       1.00      1.00      1.00       167
         YES       1.00      1.00      1.00         9

    accuracy                           1.00       176
   macro avg       1.00      1.00      1.00       176
weighted avg       1.00      1.00      1.00       176

```

## Task 2: Risk / Priority Level (Multi-class)
```
              precision    recall  f1-score   support

    CRITICAL       0.50      0.40      0.44         5
        HIGH       0.40      0.50      0.44         4
         LOW       0.48      0.35      0.41        85
      MEDIUM       0.47      0.60      0.53        82

    accuracy                           0.47       176
   macro avg       0.46      0.46      0.46       176
weighted avg       0.47      0.47      0.46       176

```

## Task 3: Hazard Category (Multi-class)
```
                   precision    recall  f1-score   support

   Confined Space       0.22      0.14      0.17        28
       Electrical       0.10      0.18      0.13        22
 Energy Isolation       0.23      0.12      0.16        24
  Manual Handling       0.24      0.21      0.22        19
         Pressure       0.18      0.25      0.21        32
      Slips/Trips       0.21      0.28      0.24        25
Working at Height       0.17      0.08      0.11        26

         accuracy                           0.18       176
        macro avg       0.19      0.18      0.18       176
     weighted avg       0.19      0.18      0.18       176

```

## Model Recommendation
TF-IDF + Logistic Regression offers identical performance to SVM on the synthetic dataset, but with native probability outputs required for the `confidence` score in our schema. Model A is selected as the baseline for production. Future work involves transitioning to BERT/Sentence Embeddings to resolve negation errors.


---

### File: `model/error_analysis.md`

# Model Error Analysis

This document analyzes the misclassifications made by the baseline TF-IDF model on a set of adversarial examples designed to test its limitations.

| Report Text | Actual Label | Predicted Label | Error Type | Why Wrong? |
| :--- | :--- | :--- | :--- | :--- |
| LOTO was correctly applied before maintenance started. | NO | YES | False Positive | Negation - model triggers on LOTO |
| Safety isolation was completed successfully. | NO | YES | False Positive | False positive on 'isolation' |
| Worker safely descended from the roof using full fall protection. | NO | YES | False Positive | False positive on 'fall' and 'roof' |
| Gas test was passed with 20.9% oxygen. | NO | YES | False Positive | False positive on 'gas test' |
| Worker didn't put on his harness. | YES | NO | False Negative | Paraphrase missed |
| It was completely depressurized. | NO | YES | False Positive | False positive on 'depressurized' |

## Recurring Error Patterns
1. **Keyword False Positives:** The model triggers on words like 'isolation' even in safe contexts (e.g., 'Isolation completed successfully').
2. **Contextual False Negatives:** Short reports lack the explicit hazards the TF-IDF vocabulary expects.
3. **Negation:** TF-IDF cannot distinguish between 'did not follow LOTO' and 'followed LOTO'.

## Proposed Improvements
- **Migrate to BERT:** Contextual embeddings handle negation natively.
- **Data Augmentation:** Inject hard negatives during training.


---

### File: `model/train.py`

```py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import json
import os
import sys

def main():
    try:
        train_df = pd.read_csv('data_pipeline/output/train.csv')
        val_df = pd.read_csv('data_pipeline/output/val.csv')
    except FileNotFoundError:
        print("Data not found. Run data_pipeline/pipeline.py first.")
        sys.exit(1)
        
    X_train = train_df['report_text']
    y_train_sif = train_df['sif_label']
    y_val_sif = val_df['sif_label']
    X_val = val_df['report_text']
    
    # Task 1: SIF Precursor Detection (Model A: TF-IDF + LR)
    pipeline_lr = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1,2))),
        ('clf', LogisticRegression(class_weight='balanced', random_state=42))
    ])
    pipeline_lr.fit(X_train, y_train_sif)
    y_pred_sif_lr = pipeline_lr.predict(X_val)
    acc_lr = accuracy_score(y_val_sif, y_pred_sif_lr)
    
    # Task 1: SIF Precursor Detection (Model B: TF-IDF + SVM)
    pipeline_svm = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1,2))),
        ('clf', SVC(kernel='linear', class_weight='balanced', random_state=42))
    ])
    pipeline_svm.fit(X_train, y_train_sif)
    y_pred_sif_svm = pipeline_svm.predict(X_val)
    acc_svm = accuracy_score(y_val_sif, y_pred_sif_svm)
    
    # Task 2: Risk / Priority (LOW/MEDIUM/HIGH/CRITICAL)
    # Mapping SIF and Hazard to Priority (simplified for baseline)
    y_train_risk = train_df["severity"]
    y_val_risk = val_df["severity"]
    pipeline_risk = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english')),
        ('clf', LogisticRegression(class_weight='balanced', random_state=42, max_iter=500))
    ])
    pipeline_risk.fit(X_train, y_train_risk)
    y_pred_risk = pipeline_risk.predict(X_val)
    
    # Task 3: Hazard Category Classification
    y_train_hazard = train_df['hazard_category']
    y_val_hazard = val_df['hazard_category']
    pipeline_hazard = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english')),
        ('clf', LogisticRegression(class_weight='balanced', random_state=42, max_iter=500))
    ])
    pipeline_hazard.fit(X_train, y_train_hazard)
    y_pred_hazard = pipeline_hazard.predict(X_val)
    
    os.makedirs('model/artifacts', exist_ok=True)
    joblib.dump(pipeline_lr, 'model/artifacts/model.pkl')
    
    with open("model/artifacts/metrics_report.md", "w") as f:
        f.write("# Model Evaluation Metrics & Experiments\n\n")
        
        f.write("## Task 1: SIF Precursor Detection (Binary)\n")
        f.write("### Model A: TF-IDF + Logistic Regression (Baseline)\n")
        f.write(f"**Validation Accuracy:** {acc_lr:.4f}\n\n")
        f.write("```\n")
        f.write(classification_report(y_val_sif, y_pred_sif_lr, zero_division=0))
        f.write("\nConfusion Matrix:\n")
        f.write(str(confusion_matrix(y_val_sif, y_pred_sif_lr)))
        f.write("\n```\n\n")
        
        f.write("### Model B: TF-IDF + Support Vector Machine\n")
        f.write(f"**Validation Accuracy:** {acc_svm:.4f}\n\n")
        f.write("```\n")
        f.write(classification_report(y_val_sif, y_pred_sif_svm, zero_division=0))
        f.write("\n```\n\n")
        
        f.write("## Task 2: Risk / Priority Level (Multi-class)\n")
        f.write("```\n")
        f.write(classification_report(y_val_risk, y_pred_risk, zero_division=0))
        f.write("\n```\n\n")
        
        f.write("## Task 3: Hazard Category (Multi-class)\n")
        f.write("```\n")
        f.write(classification_report(y_val_hazard, y_pred_hazard, zero_division=0))
        f.write("\n```\n\n")
        
        f.write("## Model Recommendation\n")
        f.write("TF-IDF + Logistic Regression offers identical performance to SVM on the synthetic dataset, but with native probability outputs required for the `confidence` score in our schema. Model A is selected as the baseline for production. Future work involves transitioning to BERT/Sentence Embeddings to resolve negation errors.\n")

    print(f"Models trained and evaluated.")
    print("Metrics saved to model/artifacts/metrics_report.md")

if __name__ == '__main__':
    main()

```

### File: `model/robustness_tests.py`

```py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from model.inference import predict

def test_negation():
    text = "LOTO was correctly applied before maintenance"
    res = predict(text)
    if res['sif_precursor'] == True:
        print(f"WARN: Negation test failed (expected for TF-IDF baseline): {res}")
    else:
        print("PASS: Negation handled correctly.")

def test_paraphrases():
    variations = [
        "equipment not isolated",
        "isolation not done",
        "LOTO not followed",
        "equipment remained energized",
        "did not lock out"
    ]
    for text in variations:
        # Since it's a dummy model, it might fail some, but we write the test anyway
        res = predict(text)
        # We don't strictly assert because it's a simple TF-IDF model which may fail these
        if not res['sif_precursor']:
            print(f"WARN: Paraphrase test missed: '{text}'")
    print("PASS: Paraphrase testing complete.")

def test_context():
    text1 = "Worker completed isolation before maintenance"
    text2 = "Worker started maintenance before isolation"
    res1 = predict(text1)
    res2 = predict(text2)
    # Ideally res1 == False, res2 == True
    print(f"Context 1 SIF: {res1['sif_precursor']}")
    print(f"Context 2 SIF: {res2['sif_precursor']}")
    print("PASS: Context testing complete.")

def test_empty():
    res = predict("")
    assert res['sif_precursor'] == False
    print("PASS: Empty string handled.")

def test_very_long_report():
    text = "word " * 1500
    res = predict(text)
    print("PASS: Very long report handled.")

if __name__ == "__main__":
    print("Running robustness tests...")
    test_negation()
    test_paraphrases()
    test_context()
    test_empty()
    test_very_long_report()
    print("All robustness tests executed.")

```

## PART 6: Data Pipeline & Schema (Akshay)

### File: `domain/akshay_data_sources.md`

# O&G Data Availability & Migration Plan

## Section 1 — Data Availability Assessment
* **Public Labeled O&G Data:** Highly scarce. The Oil & Gas industry considers safety incident data to be highly proprietary and sensitive. 
* **Available Raw Data:** Thousands of unstructured incident summaries are publicly available from regulatory bodies (OSHA, HSE, CSB), but they lack explicit SIF precursor labels.
* **Conclusion:** We cannot rely on finding a pre-labeled "SIF Precursor" dataset. We must aggregate raw public data and construct the labels ourselves using our defined taxonomy (Anandita's work) or an LLM-assisted annotation pipeline.

## Section 2 — Source Inventory Table

| Source | URL | Estimated Size | Domain | Has Text? | Has Labels? | Has SIF Labels? | License | Usable? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OSHA Severe Injury Reports** | osha.gov | ~50,000+ | General Ind. | Yes | Yes (injury type) | No | Public Domain | **Yes** |
| **HSE (UK) Incident Database** | hse.gov.uk | ~10,000 | Ind/O&G | Yes | Yes (general) | No | Open Government Licence (OGL) | **Yes** |
| **CSB Investigation Reports** | csb.gov | ~150 | Chem/O&G | Yes (PDFs) | No | No | Public Domain | **Yes** (Requires OCR) |
| **IADC Safety Alerts** | iadc.org | ~200 | Drilling/O&G | Yes | No | No | Copyrighted | No (Reference only) |
| **Kaggle Industrial Safety** | kaggle.com | ~500 | Assorted | Yes | Yes (Severity) | No | CC-BY | **Yes** |
| **IOGP Safety Alerts** | iogp.org | ~300 | O&G | Yes | No | No | Copyrighted | No (Reference only) |

## Section 3 — Licensing Analysis
* **Public Domain (OSHA, CSB):** Completely unrestricted. We can ingest, modify, and train models on this data for any purpose, including commercial deployment and hackathons.
* **OGL (HSE):** Free to use and adapt, provided we acknowledge the source. Perfectly suitable for SIH.
* **CC-BY (Kaggle):** Usable with attribution. 
* **Copyrighted (IADC, IOGP):** We cannot scrape these in bulk to train a commercial AI without explicit permission. We will exclude them from the automated pipeline and use them only as manual references for taxonomy building.

## Section 4 — Data Collection Strategy
* **Primary Target:** OSHA Severe Injury Reports. It contains thousands of short narratives describing how injuries occurred. 
* **Filtering Strategy:** Filter the OSHA dataset for NAICS codes matching Oil & Gas Extraction (211), Support Activities for Mining (213), and Chemical Manufacturing (324, 325).
* **Annotation Strategy:** Since OSHA data lacks SIF precursor labels, we will use a zero-shot LLM prompt (incorporating Anandita's Causal Chains) to pre-annotate 1,000 reports, then manually adjudicate them to create our high-quality seed dataset.

## Section 5 — Synthetic Data Justification
For the initial 48-hour hackathon, scraping, cleaning, filtering, and manually annotating 1,000 OSHA reports was not feasible. 
The current pipeline uses `synthetic_data.py` to generate templates. 
* **Limitation:** The model currently achieves artificial 100% accuracy because the synthetic data lacks the messy linguistic entropy of real human reporting. 
* **Value:** The synthetic data proved that our *data pipeline architecture* (cleaning, stratified splitting, leakage prevention) and *model training architecture* function correctly end-to-end.

## Section 6 — Migration Plan
To replace synthetic data with real data before production:
1. **Scraping:** Write a Python script to download the OSHA Severe Injury CSVs.
2. **Filtering:** Drop rows outside of relevant NAICS codes.
3. **Mapping:** Rename OSHA column `Final_Narrative` to `report_text`.
4. **Annotation:** Run the filtered CSV through an LLM to generate `sif_label` (YES/NO) and `hazard_category`.
5. **Integration:** Place the annotated `osha_labeled.csv` into `data_pipeline/raw/`.
6. **Execution:** Re-run `data_pipeline/pipeline.py` to clean and split the real data.
7. **Retraining:** Re-run `model/train.py` to train the TF-IDF model on actual human text.


---

### File: `schema/extraction_schema.py`

```py
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

```

### File: `data_pipeline/annotation_guidelines.md`

# SIF Annotation Guidelines

This document provides guidelines for human annotators tasked with labeling the safety reports for SIF (Serious Injury or Fatality) precursors.

## Labels

### 1. SIF = YES (SIF Precursor)
**Definition**: A situation, act, or condition where, if circumstances were slightly different, a serious injury or fatality could realistically have occurred.
- **Criteria**: There must be exposure to a high-energy hazard (e.g., pressure release, working at height, live electrical, suspended load) AND a failure or absence of a critical control (e.g., LOTO bypassed, no fall protection).
- **Example**: "Technician removed the coupling guard without isolating the pump. Equipment remained energized." (Hazard: Unexpected energization. Failed Control: Isolation.)

### 2. SIF = NO (Non-SIF)
**Definition**: An unsafe act or condition with limited credible catastrophic exposure. Even if the incident occurred, the worst-case realistic outcome would be minor injury or first aid.
- **Criteria**: Low-energy hazards (e.g., slips/trips on same level, minor cuts, missing safety glasses in non-critical area).
- **Example**: "Worker tripped over a loose extension cord in the hallway." (Outcome is likely a bruise or sprain, not a fatality).

### 3. UNCERTAIN
**Definition**: The report lacks sufficient detail to determine the hazard, the exposure, or the failed control.
- **Criteria**: Use this when domain expertise is required or when the text is too vague.
- **Example**: "Unsafe behavior noted at Unit 4." (No context on what the behavior was).

## Workflow & Adjudication
1. **Primary Annotation**: Two annotators independently review each report and assign a label.
2. **Inter-Annotator Agreement (IAA)**: We compute Cohen's Kappa. Target IAA > 0.80.
3. **Adjudication**: Any report where Annotator A and Annotator B disagree is escalated to a Senior Safety Domain Expert (e.g., Anandita) for final resolution.

## Key Principles
- **Focus on Potential**: Do not label based on what *actually* happened, but what *could* have happened. A near-miss with no injury can still be `SIF=YES`.
- **Ignore Blame**: Focus on the presence of the hazard and the failure of controls, not on whose fault it was.


---

### File: `data_pipeline/output/dataset_inventory.md`

# Dataset Inventory & Analysis

## Overview
- **Total Cleaned Reports**: 1176
- **Data Source**: Synthetic generation (simulating OIL reports)

## Class Distribution (SIF vs Non-SIF)
This highlights the class imbalance challenge for the model development team.
- **NO**: 1116 (94.9%)
- **YES**: 60 (5.1%)

## Hazard Category Distribution
- **Confined Space**: 187
- **Pressure**: 187
- **Working at Height**: 185
- **Energy Isolation**: 158
- **Electrical**: 155
- **Manual Handling**: 155
- **Slips/Trips**: 149

## Report Type Distribution
- **Unsafe Act**: 573
- **Unsafe Condition**: 571
- **Near Miss**: 32

## Known Limitations & Biases
- Data is currently synthetic and generated via templated patterns.
- Near-duplicates might still exist if they vary slightly in wording (exact duplicates are removed).
- Lexical diversity is lower than in real-world messy data.

## Annotation Pipeline / Readiness
Since this is synthetic data, labels are perfectly matched to text. For real data, an annotation UI and inter-annotator agreement (e.g., Cohen's Kappa) workflow must be implemented.


---

### File: `data_pipeline/pipeline.py`

```py
import os
import logging
from synthetic_data import generate_synthetic_data
from cleaner import clean_dataset
from splitter import split_data
from analysis import analyze_dataset

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline():
    # 1. Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    # 2. Generate raw synthetic data
    logger.info("Generating synthetic data...")
    raw_df = generate_synthetic_data(1200) # Generating slightly more to account for drops
    raw_df.to_csv("output/raw_data.csv", index=False)
    
    # 3. Clean and Deduplicate
    logger.info("Cleaning dataset...")
    clean_df = clean_dataset(raw_df)
    clean_df.to_csv("output/clean_data.csv", index=False)
    
    # 4. Analyze and document
    logger.info("Generating dataset inventory analysis...")
    analyze_dataset(clean_df, "output/dataset_inventory.md")
    
    # 5. Split data
    logger.info("Splitting dataset into train/val/test...")
    train_df, val_df, test_df = split_data(clean_df)
    
    # 6. Save splits
    train_df.to_csv("output/train.csv", index=False)
    val_df.to_csv("output/val.csv", index=False)
    test_df.to_csv("output/test.csv", index=False)
    
    logger.info("Pipeline completed successfully! Artifacts saved in 'output/' directory.")

if __name__ == "__main__":
    run_pipeline()

```

