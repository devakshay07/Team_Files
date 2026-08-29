# SIF Precursor Detection — Real Data Annotation Framework

## Objective
To establish a rigorous, repeatable human-annotation process for evaluating Unsafe Act, Unsafe Condition, and Near-Miss reports for Serious Injury and Fatality (SIF) precursors.

## 1. SIF Precursor Categories (Multi-Label)
Each report must be evaluated against the following categories:
- **Energy Isolation (LOTO) Failure**
- **Working at Height / Fall Protection Failure**
- **Confined Space Entry Violation**
- **High-Pressure Release Risk**
- **Heavy Lifting / Dropped Object Risk**
- **Mobile Equipment / Pedestrian Conflict**
- **Electrical Exposure (Arc Flash / Shock)**
- **Toxic/Asphyxiating Gas Exposure**

## 2. Labeling Logic
For each category, the annotator must select one of the following labels:
- **POSITIVE (YES):** The text explicitly describes an exposure or failure that historically correlates with a fatality or life-altering injury.
- **NEGATIVE (NO):** The text describes a low-risk issue (e.g., papercut, office trip hazard, proper PPE used correctly).
- **AMBIGUOUS (REVIEW):** The text implies danger but lacks critical details (e.g., "Worker fell" — from 2ft or 20ft?).
- **INSUFFICIENT INFO (REJECT):** The report is too short or garbled to interpret (e.g., "Pump broke").

## 3. Annotation Guidelines
- **Focus on Potential, Not Outcome:** A near-miss where a 2-ton pipe falls 5 feet away from a worker is a POSITIVE SIF precursor, even if no one was hurt.
- **Ignore Bureaucracy:** Missing a signature on a permit is NEGATIVE unless it directly resulted in an uncontrolled high-risk exposure.
- **Multi-Label:** A report can contain multiple precursors (e.g., "Welding inside a tank" = Confined Space + Hot Work).

## 4. Inter-Annotator Agreement (IAA)
- 10% of the real dataset (e.g., 100 reports) must be annotated independently by **two qualified HSE professionals**.
- **Cohen's Kappa** will be calculated to measure agreement.
- Target Kappa: **> 0.75**.
- **Conflict Resolution:** Any disagreements in the 10% overlap set will be adjudicated by a 3rd Senior HSE Lead in a weekly alignment meeting.

## 5. Handling Data Leakage
- Annotators will be assigned batches grouped by **Location** or **Time period** to prevent the model from learning location-specific reporting biases rather than actual safety language.
- Duplicates and near-duplicates will be purged prior to annotation.
