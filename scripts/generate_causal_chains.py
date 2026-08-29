import csv
import os

data = [
    # Energy Isolation / LOTO (10)
    ["Energy Isolation", "Maintenance started without verified isolation", "LOTO verification", "Unexpected energization / fatality", "Critical", '"not isolated", "LOTO not followed", "still energized"'],
    ["Energy Isolation", "LOTO bypass (deliberate)", "LOTO enforcement", "Unexpected energization / severe injury", "Critical", '"bypassed", "removed lock", "unauthorized removal"'],
    ["Energy Isolation", "Isolation not verified before re-entry", "Re-verification", "Unexpected energization", "Critical", '"did not verify", "assumed isolated"'],
    ["Energy Isolation", "Missing lock (mechanical failure)", "Equipment integrity", "Unexpected energization", "High", '"lock broken", "lock failed", "tag fell off"'],
    ["Energy Isolation", "Stored energy not dissipated (spring-loaded)", "Stored energy release", "Release of mechanical energy / crushing", "Critical", '"stored energy", "spring tension", "not discharged"'],
    ["Energy Isolation", "Incorrect isolation point used", "Procedure adherence", "Exposure to live energy", "Critical", '"wrong valve", "incorrect breaker"'],
    ["Energy Isolation", "Unexpected energization during maintenance", "Zero energy state", "Severe injury / fatality", "Critical", '"equipment started", "unexpected movement"'],
    ["Energy Isolation", "Residual pressure after depressurization attempt", "Bleed valve operation", "High-pressure release", "Critical", '"residual pressure", "still pressurized", "trapped pressure"'],
    ["Energy Isolation", "Multiple crafts working on same equipment without separate locks", "Group LOTO procedure", "Unexpected energization for unprotected worker", "High", '"shared lock", "no personal lock"'],
    ["Energy Isolation", "Attempted to operate locked out equipment", "LOTO awareness", "Equipment damage / potential release", "High", '"tried to start", "attempted to operate"'],

    # Working at Height (10)
    ["Working at Height", "Worker without fall protection near edge", "Fall arrest system", "Fatal fall", "Critical", '"no harness", "without fall protection", "unprotected edge"'],
    ["Working at Height", "Improperly anchored harness", "Anchorage point selection", "Fatal fall", "Critical", '"tied to pipe", "improper anchor", "not tied off"'],
    ["Working at Height", "Unprotected leading edge", "Guardrails / barriers", "Fatal fall", "Critical", '"no guardrail", "missing handrail", "open edge"'],
    ["Working at Height", "Unsafe scaffolding (missing planks/guardrails)", "Scaffold inspection", "Fall / scaffold collapse", "Critical", '"red tag", "missing plank", "incomplete scaffold"'],
    ["Working at Height", "Unsafe ladder (unsecured, overreached)", "Ladder safety", "Fall from height", "High", '"ladder slipped", "unsecured ladder", "overreaching"'],
    ["Working at Height", "Objects/tools at height unsecured", "Dropped object prevention", "Fatal struck-by injury", "High", '"tool fell", "dropped object", "unsecured tools"'],
    ["Working at Height", "Work near fragile roof without protection", "Fragile surface identification", "Fatal fall through roof", "Critical", '"fragile roof", "skylight", "fell through"'],
    ["Working at Height", "Using makeshift elevation (standing on buckets)", "Proper access equipment", "Fall from height", "Medium", '"standing on bucket", "makeshift platform"'],
    ["Working at Height", "Climbing outside cage on fixed ladder", "Ladder safety", "Fall from height", "High", '"outside cage", "climbing structure"'],
    ["Working at Height", "Harness lanyard too long for fall distance", "Fall clearance calculation", "Impact with ground", "Critical", '"wrong lanyard", "hit ground"'],

    # Confined Space (10)
    ["Confined Space", "Entry without atmospheric testing", "Gas testing", "Asphyxiation / Toxic exposure", "Critical", '"no gas test", "atmosphere not checked"'],
    ["Confined Space", "No standby person / hole watch", "Confined space permit", "Inability to rescue / fatality", "Critical", '"no standby", "hole watch absent"'],
    ["Confined Space", "No rescue arrangement in place", "Emergency response plan", "Delayed rescue / fatality", "Critical", '"no rescue plan", "no tripod"'],
    ["Confined Space", "Unauthorized entry (no permit)", "Permit to work", "Unknown hazards / fatality", "Critical", '"without permit", "unauthorized entry"'],
    ["Confined Space", "Improper ventilation", "Ventilation control", "Toxic buildup / Asphyxiation", "Critical", '"poor ventilation", "exhaust fan off"'],
    ["Confined Space", "Oxygen-deficient atmosphere detected", "Atmospheric monitoring", "Asphyxiation", "Critical", '"low oxygen", "O2 deficient"'],
    ["Confined Space", "Entry during cleaning with chemicals", "Chemical hazard assessment", "Toxic exposure / Fire", "Critical", '"cleaning solvent", "fumes"'],
    ["Confined Space", "Gas monitor alarming but entry continued", "Alarm response", "Toxic exposure / Asphyxiation", "Critical", '"ignored alarm", "continued entry"'],
    ["Confined Space", "Hot work inside confined space without continuous monitoring", "Continuous gas testing", "Fire / Explosion", "Critical", '"hot work in vessel", "no continuous monitoring"'],
    ["Confined Space", "Exhaust from diesel generator entering confined space", "Equipment placement", "Carbon monoxide poisoning", "Critical", '"exhaust fumes", "generator near opening"'],

    # Pressure Systems / Line Breaking (9)
    ["Pressure Systems", "Line opened with residual pressure", "Depressurization", "High-energy release / Struck-by", "Critical", '"residual pressure", "line under pressure"'],
    ["Pressure Systems", "Valve operated incorrectly (wrong valve)", "Valve identification", "Unexpected release", "Critical", '"wrong valve", "incorrect line"'],
    ["Pressure Systems", "Failure to depressurize before breaking flange", "Depressurization verification", "High-pressure release / Chemical exposure", "Critical", '"did not depressurize", "sprayed"'],
    ["Pressure Systems", "Blind flange removed without isolation", "Double block and bleed / Blinding", "Massive release of hazardous material", "Critical", '"removed blind", "no isolation"'],
    ["Pressure Systems", "Unexpected release during line-breaking", "Hazard identification", "Chemical exposure / Burns", "Critical", '"sudden release", "sprayed with"'],
    ["Pressure Systems", "Sampling point used without caution (high pressure)", "Sampling procedure", "High-pressure release", "High", '"sampling", "pressure surge"'],
    ["Pressure Systems", "Using incorrect pressure rating for fittings", "Material specification", "Fitting failure / Projectile", "Critical", '"wrong rating", "fitting blew off"'],
    ["Pressure Systems", "Tightening a leaking pressurized connection", "Safe work practices", "Catastrophic failure / Release", "Critical", '"tightened under pressure", "stopped leak"'],
    ["Pressure Systems", "Pneumatic testing without exclusion zone", "Pressure testing safety", "Explosion / Projectile", "Critical", '"pneumatic test", "no barricade"'],

    # Heavy Equipment / Suspended Loads / Dropped Objects (9)
    ["Heavy Equipment", "Working under suspended load", "Suspended load exclusion zone", "Fatal crushing", "Critical", '"under load", "suspended load"'],
    ["Heavy Equipment", "Unsecured tools at height above workers", "Dropped object prevention", "Fatal struck-by injury", "High", '"tool fell", "dropped from height"'],
    ["Heavy Equipment", "Crane operation without clear exclusion zone", "Barricades / Access control", "Crushing / Struck-by", "Critical", '"crane operation", "entered barricade"'],
    ["Heavy Equipment", "Improper rigging of load", "Rigging inspection", "Dropped load / Crushing", "Critical", '"rigging failed", "sling broke"'],
    ["Heavy Equipment", "Equipment movement near workers without spotter", "Spotter usage", "Crushing / Run-over", "Critical", '"no spotter", "reversing"'],
    ["Heavy Equipment", "Crushing/pinch point exposure near equipment", "Machine guarding / Positioning", "Amputation / Crushing", "High", '"pinch point", "hand caught"'],
    ["Heavy Equipment", "Lifting operation exceeding crane capacity", "Lift plan adherence", "Crane tip-over / Dropped load", "Critical", '"overload", "alarm sounded"'],
    ["Heavy Equipment", "Forklift driven with elevated load", "Forklift safety", "Tip-over / Crushing", "High", '"driving with load high", "tipped"'],
    ["Heavy Equipment", "Leaving heavy equipment unattended and running", "Equipment securement", "Unintended movement", "Medium", '"left running", "unattended"'],

    # Electrical Hazards (8)
    ["Electrical Hazards", "Live electrical work without proper PPE", "Arc flash PPE", "Fatal electrocution / Burns", "Critical", '"live work", "no arc flash suit"'],
    ["Electrical Hazards", "Exposed live conductors in work area", "Electrical isolation / Guarding", "Electrocution", "Critical", '"exposed wires", "live conductor"'],
    ["Electrical Hazards", "Arc flash boundaries ignored", "Arc flash boundary enforcement", "Severe burns", "Critical", '"crossed boundary", "arc flash zone"'],
    ["Electrical Hazards", "Missing grounding on portable equipment", "Grounding / GFCI", "Electrocution", "High", '"no ground", "missing earth"'],
    ["Electrical Hazards", "Unauthorized electrical work by non-electrician", "Competency / Authorization", "Electrocution / Fire", "Critical", '"unauthorized", "not qualified"'],
    ["Electrical Hazards", "Energized equipment maintenance", "LOTO", "Electrocution", "Critical", '"working on live", "energized panel"'],
    ["Electrical Hazards", "Using damaged extension cords in wet area", "Equipment inspection", "Electrocution", "High", '"damaged cord", "frayed wire", "water"'],
    ["Electrical Hazards", "Bypassing electrical interlocks on machinery", "Machine safeguarding", "Electrocution / Amputation", "Critical", '"bypassed interlock", "door switch defeated"'],

    # Fire / Explosion (7)
    ["Fire / Explosion", "Hot work near flammable material", "Hot work permit / Housekeeping", "Fire / Explosion", "Critical", '"welding near", "flammables"'],
    ["Fire / Explosion", "Hydrocarbon release (gas leak) unnoticed", "Gas detection", "Explosion", "Critical", '"gas leak", "hydrocarbon release"'],
    ["Fire / Explosion", "Poor gas detection (no alarm)", "Gas detector maintenance", "Unnoticed explosive atmosphere", "Critical", '"detector failed", "no alarm"'],
    ["Fire / Explosion", "Ignition source introduced near vapor cloud", "Hazardous area classification", "Explosion", "Critical", '"spark", "ignition source", "non-intrinsically safe"'],
    ["Fire / Explosion", "Improper hot work permit issuance", "Permit to work", "Fire / Explosion", "Critical", '"invalid permit", "permit not checked"'],
    ["Fire / Explosion", "Flammable vapour accumulation in enclosed space", "Ventilation", "Explosion", "Critical", '"vapour buildup", "poor ventilation"'],
    ["Fire / Explosion", "Static discharge during flammable liquid transfer", "Grounding and bonding", "Fire / Explosion", "Critical", '"static", "not grounded", "transferring"'],

    # H2S / Toxic Exposure (6)
    ["H2S / Toxic", "H2S exposure without personal gas monitor", "Personal gas monitoring", "Toxic exposure / Fatality", "Critical", '"no monitor", "H2S alarm"'],
    ["H2S / Toxic", "Incorrect respiratory protection for toxic gas", "PPE selection", "Toxic exposure", "Critical", '"wrong filter", "dust mask instead of SCBA"'],
    ["H2S / Toxic", "Entry into known toxic area without monitoring", "Area monitoring", "Toxic exposure / Fatality", "Critical", '"entered without checking", "toxic gas"'],
    ["H2S / Toxic", "Emergency response failure (no muster)", "Emergency procedures", "Prolonged exposure / Fatality", "Critical", '"did not muster", "ignored alarm"'],
    ["H2S / Toxic", "Multiple workers in H2S zone without buddy system", "Buddy system", "Inability to rescue / Multiple fatalities", "Critical", '"working alone", "H2S zone"'],
    ["H2S / Toxic", "Opening process equipment containing toxic chemicals without purging", "Equipment purging", "Toxic exposure", "Critical", '"did not purge", "toxic release"'],

    # Vehicles / Mobile Equipment (6)
    ["Vehicles", "Pedestrian in mobile equipment path", "Traffic management / Segregation", "Run-over / Fatality", "Critical", '"in path", "nearly hit"'],
    ["Vehicles", "Reversing without spotter", "Spotter usage", "Run-over / Collision", "Critical", '"reversing", "no spotter", "blind spot"'],
    ["Vehicles", "Blind-spot collision risk near heavy machinery", "Visibility / Mirrors / Segregation", "Run-over", "Critical", '"blind spot", "could not see"'],
    ["Vehicles", "Seatbelt violation in mobile equipment (rollover risk)", "Seatbelt enforcement", "Ejection / Crushing", "High", '"no seatbelt", "not buckled"'],
    ["Vehicles", "Poor traffic management — mixed pedestrian/vehicle zones", "Site layout", "Collision / Run-over", "High", '"mixed traffic", "no walkway"'],
    ["Vehicles", "Speeding on site with heavy vehicle", "Speed limits", "Loss of control / Collision", "High", '"speeding", "driving fast"'],
]

filepath = os.path.join("domain", "causal_chains.csv")
with open(filepath, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Hazard", "Unsafe_Condition_or_Behavior", "Failed_Control", "Potential_Consequence", "SIF_Potential", "Evidence_Words_Patterns"])
    writer.writerows(data)

print(f"Generated {len(data)} causal chain entries.")
