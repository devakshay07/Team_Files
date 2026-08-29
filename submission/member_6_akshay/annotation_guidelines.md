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
