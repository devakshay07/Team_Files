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
