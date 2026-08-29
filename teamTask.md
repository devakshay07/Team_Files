# Team Silent Stack - SIH 2026 Tasks

## Team Members Overview
1. **Anandita** - Domain Expert (SIF Precursors in Oil & Gas)
2. **Renuka** - Data Extractor (Safety Report Information Extraction)
3. **Manish** - Product & UX Designer (EHS Officer Workflow)
4. **Aditya** - Technical Team (R&D / Technical Research & System Architecture)
5. **Devanshu** - Technical Team (Model Development & Experimentation)
6. **Akshay** - Technical Team (Dataset / Data Engineering & Training Pipeline)

---

Team Silent Stack -  SIH 2026 Tasks 


## Anandita ⭐

Your Task — Understand SIF Precursors in Oil & Gas Operations
You have 2 days: today and tomorrow.
Your job is to understand what kinds of dangerous situations, behaviors, and conditions in an oil & gas environment can precede a Serious Injury or Fatality (SIF).
You are NOT responsible for:
- Model development
- NLP research
- Dataset collection
- Training models
- Building the application
- Studying how to extract information from reports
Other members are handling those areas.
Your responsibility is the SAFETY DOMAIN.
You need to become the person on our team who can answer:
"Is this situation genuinely dangerous enough to be considered a potential SIF precursor, why is it dangerous, what control failed, and what could realistically happen?"

### 1. First understand the core concepts
Start by understanding the difference between:
- Unsafe Act
- Unsafe Condition
- Near Miss
- Incident
- High-Potential Incident / High-Potential Near Miss
- Serious Injury
- Fatality
- SIF
- SIF Precursor
Don't just memorize definitions.
For each concept, find realistic examples and understand how they differ.
Especially focus on:
A situation where nobody was injured, but the potential consequence could have been catastrophic.
That is extremely important to our project.

### 2. Understand SIF precursors
Your main question is:
What patterns can appear before a serious injury or fatality?
Study the idea of precursor → exposure → consequence.
For example:
Failure to isolate equipment
          ↓
Worker exposed to stored energy
          ↓
Unexpected energization
          ↓
Potential serious injury/fatality

Or:
Worker enters confined space
          ↓
No atmospheric testing
          ↓
Exposure to toxic/oxygen-deficient atmosphere
          ↓
Potential asphyxiation/fatality

You need to understand these chains for different operational hazards.

### 3. Investigate these major areas
You should investigate each of the following.
Energy Isolation / LOTO
Understand situations such as:
- Failure to isolate
- Incorrect isolation
- Isolation not verified
- LOTO bypass
- Missing lock/tag
- Stored energy
- Unexpected energization
- Residual pressure/energy
- Starting maintenance before isolation
Ask:
What can happen if this control fails?

Working at Height
Investigate:
- No fall protection
- Improper harness use
- Unprotected edges
- Unsafe scaffolding
- Unsafe ladders
- Improper anchorage
- Objects/tools at height
Understand which situations have potential for fatal consequences.

Confined Spaces
Investigate:
- Entry without permit
- No atmospheric testing
- Oxygen deficiency
- Toxic gases
- No standby person
- No rescue arrangement
- Improper ventilation
- Unauthorized entry
Understand why confined-space failures can rapidly become fatal.

Pressure Systems / Line Breaking
Investigate:
- Opening pressurized equipment
- Trapped pressure
- Failure to depressurize
- Incorrect isolation
- Unexpected release
- Line breaking without proper controls
- Wrong valve operation
Understand the energy involved and potential consequences.

Heavy Equipment / Suspended Loads / Dropped Objects
Investigate:
- Working under suspended loads
- Unsecured tools
- Objects falling from height
- Crane operations
- Improper lifting
- Equipment movement
- Crushing/pinch points
- Struck-by hazards
Focus on situations where a small failure can produce catastrophic consequences.

Electrical Hazards
Investigate:
- Live electrical work
- Exposed conductors
- Missing grounding
- Incorrect isolation
- Arc flash
- Unauthorized electrical work
- Improper PPE
- Energized equipment
Understand both injury and fatality potential.

Fire / Explosion
Investigate:
- Ignition sources
- Hydrocarbon release
- Gas leaks
- Hot work near flammable material
- Poor gas detection
- Improper isolation
- Accumulation of flammable vapors
Think about:
Release → ignition → escalation → major consequence.

H₂S / Toxic Exposure
Investigate:
- H₂S exposure
- Toxic gas release
- No gas detection
- Incorrect respiratory protection
- Poor ventilation
- Entry without atmospheric monitoring
- Emergency response failures
Understand why these hazards can create multiple casualties.

Vehicles / Mobile Equipment
Investigate:
- Vehicle-pedestrian interaction
- Reversing
- Blind spots
- Unsafe driving
- Failure of vehicle controls
- Seatbelt violations
- Poor traffic management
- Mobile equipment movement
Look particularly at situations where workers are exposed to moving equipment.

Hot Work
Investigate:
- Welding/cutting near hydrocarbons
- Missing gas testing
- Poor isolation
- Ignition sources
- Inadequate fire watch
- Flammable atmosphere
Understand how a seemingly normal task can escalate into fire/explosion.

Excavation
Investigate:
- Unprotected excavation
- Collapse
- Underground utilities
- Worker entry without controls
- Heavy equipment near excavation
- Water accumulation
Understand the mechanisms that can lead to serious injury/fatality.

SIMOPS
Understand:
Simultaneous Operations.
Research situations where multiple activities happen simultaneously and create unexpected interactions.
For example:
Hot work
   +
Hydrocarbon transfer
   +
Maintenance
   ↓
Unexpected interaction
   ↓
Major hazard

Focus on why individually safe activities can become dangerous when performed together.

PPE / Safety Procedure Failures
Investigate:
- Required PPE not used
- Incorrect PPE
- PPE unavailable
- Procedure skipped
- Safety procedure bypassed
- Permit requirements ignored
- Safety interlocks bypassed
But don't treat "PPE violation" automatically as SIF.
Your job is to understand:
When does a control failure actually create credible SIF potential?

### 4. Understand Process Safety vs Occupational Safety
This distinction is important.
Research the difference between:
Occupational Safety
Examples:
- Slips/trips
- Cuts
- Manual handling
- PPE
- Falls
- Machinery injuries
Process Safety
Examples:
- Hydrocarbon release
- Explosion
- Fire
- Loss of containment
- Pressure release
- Toxic gas release
- Major equipment failure
Understand how both can lead to serious injury/fatality and where they overlap.
For our project, identify situations where a report may look like a normal unsafe condition but actually indicates a major process-safety risk.

### 5. Investigate Human Factors
Don't simply blame:
"Worker did not follow procedure."
That's too shallow.
Investigate why unsafe acts happen.
Look for factors such as:
- Fatigue
- Time pressure
- Poor communication
- Inadequate training
- Inexperience
- Poor supervision
- Misunderstanding
- Normalization of deviation
- Poor procedure design
- Conflicting priorities
- Complacency
- Production pressure
- Inadequate planning
The question is:
What human/organizational factors can contribute to SIF precursors?

### 6. Build the SIF Precursor Taxonomy
This is your main deliverable.
Create a structured taxonomy.
Something like:
SIF PRECURSORS
│
├── Energy
│   ├── Electrical
│   ├── Mechanical
│   ├── Pressure
│   └── Stored energy
│
├── Fall from Height
│   ├── Missing fall protection
│   ├── Unprotected edge
│   └── Unsafe access
│
├── Confined Space
│   ├── No gas testing
│   ├── No permit
│   └── No rescue arrangement
│
├── Fire / Explosion
│   ├── Hydrocarbon release
│   ├── Ignition source
│   └── Hot work failure
│
├── Mobile Equipment
│   ├── Pedestrian interaction
│   ├── Reversing
│   └── Crushing
│
└── ...

Don't just copy this structure.
Build your own taxonomy based on your research.

### 7. Create the main taxonomy table
This is the most important table you need to produce.
Use these columns:
Hazard
Unsafe behavior / condition
Potential consequence
SIF potential
Evidence words / patterns

For example:
Hazard
Unsafe behavior / condition
Potential consequence
SIF potential
Evidence words / patterns
Energy Isolation
Maintenance started without verified isolation
Unexpected energization, severe injury/fatality
Critical
"not isolated", "LOTO not followed", "still energized"
Confined Space
Entry without atmospheric testing
Toxic exposure, asphyxiation
Critical
"no gas test", "atmosphere not checked"
Working at Height
Worker without fall protection
Fatal fall
Critical
"no harness", "without fall protection"
Dropped Object
Tools unsecured at height
Fatal struck-by injury
High
"tool fell", "object dropped"
Pressure
Line opened with residual pressure
High-energy release
Critical
"residual pressure", "line under pressure"

Aim for at least 50–75 strong entries.
Quality matters more than blindly hitting a number.

### 8. For every precursor, understand the causal chain
Don't just write:
"No harness = dangerous."
Explain:
Unsafe condition:
Worker exposed at height without fall protection

        ↓

Hazard:
Potential fall from height

        ↓

Exposure:
Worker

        ↓

Failed control:
Fall arrest / fall prevention

        ↓

Potential consequence:
Severe injury / fatality

Create around 20 detailed causal chains across different hazard categories.
This will help us understand the reasoning behind SIF detection.

### 9. Find "false positives"
This is VERY important.
Not every unsafe act is necessarily a SIF precursor.
For example:
"Worker forgot to wear safety glasses while walking through an office."
That's an unsafe act.
But it doesn't necessarily represent the same SIF potential as:
"Worker performed live electrical work without appropriate protection."
So find examples where:
Unsafe ≠ automatically SIF.
Create a small table:
Situation
Unsafe?
SIF potential?
Why?
Missing safety glasses in low-risk area
Yes
Low/No
Limited credible catastrophic exposure
Live electrical work
Yes
High
High-energy exposure
Working at height without fall protection
Yes
High/Critical
Fatal fall possible

This will help prevent our AI from simply learning:
"Safety violation = SIF."

### 10. Find high-potential near-miss examples
Specifically look for cases where:
The outcome was minor or nothing happened, but the potential consequence was catastrophic.
For example:
Suspended load shifted
       ↓
Worker was nearby
       ↓
Worker moved away
       ↓
No injury
       ↓
Potential fatal struck-by event

Collect at least 15 examples.
For each one, explain why the potential was much more serious than the actual outcome.

### 11. Identify evidence patterns
While researching, notice what kind of language indicates a dangerous situation.
Examples:
- "without isolation"
- "not verified"
- "bypassed"
- "failed to"
- "without permit"
- "no gas test"
- "still energized"
- "under pressure"
- "unprotected"
- "exposed"
- "unauthorized"
- "suspended load"
- "leak detected"
- "hydrocarbon release"
- "no standby"
- "procedure not followed"
Create a list of these patterns under the appropriate hazard category.
Do not treat these words as automatic proof of SIF.
They are evidence signals that need to be interpreted in context.

### 12. Final deliverable
At the end of the two days, submit one organized document + one master table.
Document
Section 1
SIF, SIF precursor, High-Potential Incident, Near Miss — definitions and distinctions.
Section 2
Major SIF precursor categories.
Section 3
Oil & gas hazard landscape.
Section 4
Process safety vs occupational safety.
Section 5
Human factors contributing to SIF precursors.
Section 6
Causal chains:
Unsafe condition/behavior → exposure → failed control → potential consequence
Section 7
High-potential near-miss examples.
Section 8
False positives:
Unsafe ≠ automatically SIF
Section 9
Questions/uncertainties where classification is unclear.

Master Table
Create a spreadsheet with:
Hazard
Unsafe behavior / condition
Potential consequence
SIF potential
Evidence words / patterns

Target:
50–75+ high-quality entries.
Try to cover all major categories rather than having 50 variations of the same hazard.

The most important rule
Don't spend two days making a giant theory document.
Your job is to develop domain judgment.
At the end, if I give you a report saying:
"Technician commenced maintenance on a pressurized line without confirming isolation. Residual pressure was released when the flange was opened."
I want you to be able to immediately reason:
What is the hazard?
What unsafe behavior/condition exists?
What control failed?
Who was exposed?
What could realistically have happened?
Why does this have SIF potential?
What evidence in the report supports that conclusion?
That's the skill we're trying to build.
You are essentially becoming our team's SIF/domain expert — the person who gives the technical team the safety logic they need to build the AI correctly.
Don't worry about BERT, Transformers, embeddings, model architectures, etc.
Your output is the safety knowledge and reasoning framework that the AI team will eventually try to automate.




## Renuka ⭐
Your Task — Understand What Information Exists Inside OIL Safety Reports
You are NOT responsible for model development or dataset collection. Other members are already handling that.
Your job is to understand the actual content of a safety report and figure out what information our AI should be able to extract and understand from it.
Think of yourself as the bridge between:
Raw human-written safety report → Information our AI needs → Useful output for EHS officer

### 1. First understand the problem
Our system will receive reports like:
"During maintenance activity, a technician attempted to open a flange without confirming proper isolation. Residual pressure was observed and the activity was immediately stopped."
This is just a paragraph.
But hidden inside that paragraph are many different pieces of information.
For example:
- What activity was happening?
- Who was exposed?
- What hazard existed?
- What unsafe action happened?
- Was there an unsafe condition?
- Which safety control failed?
- What could have happened?
- Was there an intervention?
- Is this potentially a SIF precursor?
- How serious is it?
Your job is to figure out all the important information that is hidden inside reports like this.

### 2. Your first deliverable: Create an "Information Extraction Framework"
Create a document/spreadsheet containing the important fields that we should be able to extract from a safety report.
Start with these fields, but don't blindly use them. Research and decide whether more fields are needed.
Basic event information
- Activity being performed
- Location
- Equipment involved
- Department/operation
- People involved
- Worker role
Safety information
- Hazard
- Unsafe Act
- Unsafe Condition
- Near-Miss indicator
- Exposure
- Failed/Missing Safety Control
- PPE issue
- Procedure violation
- Environmental condition
Consequence information
- What actually happened?
- What could have happened?
- Potential injury
- Potential fatality
- Potential damage
- Potential process/environmental consequence
Response information
- Immediate action taken
- Intervention
- Corrective action
- Preventive action
- Whether work was stopped
Risk information
- SIF precursor?
- Hazard category
- Potential severity
- Priority
- Reason for classification
Your job is to research this and decide:
What should our AI extract?

### 3. Now take real/sample safety reports
Find around exact 50 realistic safety reports.
They can come from publicly available oil & gas / industrial safety reports or other appropriate sources.
You don't need to build the dataset.
You are using these reports only to understand their structure and language.
For every report, break it down.
For example:
Raw report
"During maintenance of a pump, the technician started removing the coupling guard without isolating the equipment. Another worker noticed that the equipment was still energized and stopped the activity."
Now convert it into:
Field
Extracted Information
Activity
Pump maintenance
Equipment
Pump
Unsafe Act
Removing guard without isolation
Hazard
Unexpected energization
Exposure
Technician
Failed Control
Energy isolation / LOTO
Intervention
Another worker stopped activity
Potential Consequence
Serious injury/fatality
SIF Precursor
Yes
Hazard Category
Energy Isolation
Priority
Critical

Do this for all 30–50 reports.

### 4. Your second major task: Find different ways people describe the SAME hazard
This is extremely important for our AI.
People don't always use standardized terminology.
For example, the concept:
"Equipment was not isolated"
could appear as:
- Equipment was not isolated
- Isolation was not carried out
- LOTO was not followed
- Lock was not applied
- Energy was not isolated
- Equipment remained energized
- Zero-energy state was not verified
- Breaker remained live
- Maintenance started before isolation
- Isolation was not confirmed
These sentences are different, but they describe essentially the same underlying safety problem.
So create a table like:
Safety Concept
Different ways it may appear in text
No isolation
equipment not isolated; isolation not done; LOTO not followed; equipment remained energized...
No gas testing
gas test not conducted; atmosphere not checked; gas monitoring not performed...
Fall protection failure
no harness; harness not used; worker without fall arrest; unprotected edge...
Pressure exposure
line under pressure; residual pressure; pressure not released; trapped pressure...
Confined-space violation
entered vessel without permit; entered confined space without testing...

Try to identify at least 15–20 important safety concepts and their different linguistic variations.
This will help us understand how messy real-world safety language is.

### 5. Identify the "reason" behind a SIF precursor
Don't just write:
SIF precursor = YES
We need to understand WHY.
For every dangerous report, identify:
Hazard
What can hurt the worker?
Exposure
Who/what is exposed?
Failed control
What barrier or safety control failed?
Potential consequence
What could realistically happen?
For example:
"Worker entered a confined space without atmospheric testing."
Break it down:
Hazard: Toxic/oxygen-deficient atmosphere
Exposure: Worker inside confined space
Failed control: Atmospheric testing
Potential consequence: Toxic exposure, unconsciousness, asphyxiation, fatality
SIF precursor: Yes
This is important because our final AI should ideally be able to explain its decision instead of simply saying:
"SIF = YES, confidence = 94%."

### 6. Find the difference between "dangerous" and "actually happened"
This is another important thing I want you to investigate.
Consider:
Report A
"Worker slipped while walking but suffered no injury."
Report B
"Worker was working at height without fall protection. No fall occurred."
Report C
"Worker fell from height and suffered a fracture."
All three are safety-related, but they're different.
We need to understand:
Incident vs Near Miss vs Unsafe Act vs Unsafe Condition vs SIF precursor
Research this distinction and give examples.
Especially investigate cases where:
Nothing bad happened, but the potential consequence was extremely serious.
Those cases are particularly important to our project.

### 7. Build a SIF indicator checklist
From your research, create a practical checklist of signals that might indicate a SIF precursor.
For example:
Energy
- Unexpected energization
- Failure to isolate
- LOTO bypass
- Stored energy
- Pressurized equipment
Height
- Working without fall protection
- Open/unprotected edge
- Improper scaffolding
- Unsafe ladder use
Confined space
- Entry without permit
- No atmospheric testing
- No standby person
- No rescue arrangement
Dropped objects
- Unsecured tools
- Objects stored at height
- People working below suspended loads
Vehicles
- Pedestrian-vehicle interaction
- Reversing without control
- Unsafe driving
- Failure of vehicle controls
Electrical
- Live electrical work
- Exposed conductors
- Improper isolation
- Missing grounding
Don't stop at these examples.
Research and expand the list based on the oil & gas environment.

### 8. Think like the AI
After doing the research, ask yourself:
"If I gave this report to an AI, what should I expect it to understand?"
For example:
Input
"During line maintenance, the worker opened the flange without verifying isolation. Residual pressure was released and the worker immediately moved away."
The AI should ideally understand:
Activity:
Line maintenance

Hazard:
Stored pressure

Unsafe Act:
Flange opened without isolation verification

Failed Control:
Energy isolation / verification

Exposure:
Worker

Event:
Residual pressure release

Potential Consequence:
Serious injury/fatality

SIF Precursor:
YES

Hazard Category:
Energy / Pressure

Priority:
CRITICAL

Reason:
Worker was exposed to uncontrolled stored energy.

Create 10–15 such examples yourself.

### 9. Final deliverable
At the end of the internal hackathon, I expect you to give us one organized document, not random notes.
It should contain:
Section 1 — Safety Report Structure
What information exists inside a typical report?
Section 2 — Information Extraction Framework
What fields should our AI extract?
Section 3 — Safety Language Variations
Different ways workers may describe the same hazard/control failure.
Section 4 — SIF Precursor Indicators
What textual/eventual signals indicate potential SIF exposure?
Section 5 — Incident Classification
Difference between:
- Unsafe Act
- Unsafe Condition
- Near Miss
- Incident
- SIF precursor
- High-potential event
Section 6 — 30–50 Report Analysis
Break down the sample reports using your framework.
Section 7 — 10–15 Detailed Examples
Raw report → extracted information → SIF reasoning.
Section 8 — Questions / Uncertainties
Anything you couldn't confidently classify.
Do NOT hide uncertainty.
If you're unsure whether something should be considered a SIF precursor, write:
"Uncertain — need domain validation."
That's actually useful for us.

Most important rule
Don't spend the entire time reading articles and making a theory document.
Your job is to investigate the actual reports.
I don't care if you can explain Transformers, BERT, embeddings, etc.
The R&D team is handling that.
What I need from you is:
"If someone gives us a messy OIL safety report, I can tell you exactly what information is inside it, which parts matter for SIF detection, how people may phrase those things differently, and what the AI should ultimately extract."
If you can do that, you've genuinely contributed to the project and you'll understand the problem deeply enough to work with the technical team later.

Sorry Renuka, we have to work hard !!! We know you can do it. 😀

















## Manish ⭐
Your Task — Understand the EHS Officer & Design the Product Around Them
You have 2 days: today and tomorrow.
Your job is to understand what an EHS officer actually does with safety reports and figure out exactly how our system can help them.
You are NOT responsible for:
- NLP/model development
- Dataset collection
- SIF domain taxonomy
- Training AI models
- Building the backend
- Coding the final application
Other members are handling those.
Your responsibility is the PRODUCT + USER SIDE.
You need to become the person on our team who can answer:
"If OIL's EHS officer receives hundreds of Unsafe Act, Unsafe Condition and Near-Miss reports, what does he/she actually need to do, where does the current process become painful, and what should our software do to make that process significantly better?"

### 1. First understand who the user actually is
Our end user is not "the AI."
Our end user is an EHS / Safety professional who has to review safety observations and incidents and decide what deserves attention.
You need to understand their responsibilities.
Research what an EHS officer typically handles in an oil & gas environment:
- Safety observations
- Unsafe Acts
- Unsafe Conditions
- Near Misses
- Incidents
- Investigations
- Risk assessment
- Corrective actions
- Preventive actions
- Safety inspections
- Compliance
- Follow-ups
- Safety trends
- Escalation
- Reporting to management
Don't just list these.
Try to understand:
What decisions do they have to make every day?

### 2. Map the complete journey of a safety report
Take a report and follow what would happen to it from beginning to end.
For example:
Worker observes something
        ↓
Report submitted
        ↓
EHS receives report
        ↓
Report reviewed
        ↓
Report categorized
        ↓
Risk/severity assessed
        ↓
Priority determined
        ↓
Investigation required?
        ↓
Corrective action assigned
        ↓
Responsible person assigned
        ↓
Action tracked
        ↓
Action closed
        ↓
Trend / recurring issue analyzed
        ↓
Management reporting

But don't assume this flow is correct.
Research how safety reporting and incident-management workflows actually work and improve this flow.

### 3. Identify what the EHS officer has to manually do
This is one of your biggest tasks.
For every step in the workflow, ask:
"What is the human currently doing manually?"
For example:
Report arrives
They may have to:
- Read the report
- Understand what happened
- Identify the hazard
- Determine report type
- Determine severity
- Decide whether escalation is needed
- Compare with previous incidents
- Assign corrective action
Find as many manual steps as you can.
Then classify each one:
Task
Manual?
Time-consuming?
Requires judgment?
Could AI assist?
Read report
Yes
High
Medium
Yes
Categorize hazard
Yes
Medium
High
Yes
Identify SIF potential
Yes
High
High
Yes
Assign corrective action
Yes
Medium
High
Assist
Find recurring hazards
Yes
High
High
Yes
Final safety decision
Yes
—
Very High
Human

This table is extremely important.

### 4. Identify the biggest pain points
Investigate the problems EHS professionals face when dealing with large numbers of reports.
Look specifically for:
Volume
What happens when hundreds/thousands of reports arrive?
Manual review
How much information has to be read manually?
Inconsistent language
Do different workers describe the same problem differently?
Prioritization
How does an officer decide:
"Which report should I look at first?"
Important reports getting buried
Could a genuinely dangerous near miss get lost among hundreds of routine observations?
Delayed escalation
Could a high-risk report sit unnoticed because of manual review?
Categorization inconsistency
Could two officers classify the same event differently?
Recurring hazards
How does someone discover:
"We've seen this same problem 17 times in the last 3 months"?
Follow-up
How are corrective actions tracked?
Management reporting
How are trends communicated to senior management?
For every pain point, don't just say it exists.
Find evidence/examples where possible.

### 5. Understand what information an EHS officer needs immediately
Imagine the officer opens this report:
"During maintenance, technician attempted to open flange without confirming isolation. Residual pressure released. Activity stopped immediately."
Ask:
What would the officer want to know immediately?
Probably things such as:
What happened?
↓
How dangerous was it?
↓
Is this potentially SIF?
↓
What hazard is involved?
↓
Who/what was exposed?
↓
What control failed?
↓
What could have happened?
↓
Does this require immediate escalation?
↓
Has this happened before?
↓
What action is required?

Build a list of the minimum information an EHS officer needs on one screen.

### 6. Design the AI result, NOT just the dashboard
This is very important.
Don't start by drawing pretty dashboard boxes.
First decide:
"What should our AI tell the EHS officer after analyzing one report?"
For example:
REPORT ANALYSIS

SIF PRECURSOR
CRITICAL

Confidence
94%

Hazard
Energy Isolation

Unsafe Act
Maintenance started without verified isolation

Failed Control
LOTO / isolation verification

Potential Consequence
Unexpected energization → severe injury/fatality

Exposure
Maintenance technician

Recommended Priority
IMMEDIATE

Why?
Worker was exposed to uncontrolled stored energy.

Now ask:
What else would the officer need?
Maybe:
- Similar previous reports
- Location
- Equipment
- Frequency
- Trend
- Recommended action
- Escalation status
- Responsible department
Define this.

### 7. Design the "Priority Queue"
This is one of the most important product features.
Imagine the EHS officer has 500 reports.
They obviously cannot read everything with equal attention.
So design a system that helps them prioritize.
For example:
EHS PRIORITY QUEUE

┌─────────────────────────────────────────────┐
│ CRITICAL — 12 reports                      					 │
│                                            							 │
│ 1. Confined space — no gas testing          					│
│ 2. Live electrical work                     						│
│ 3. Pressurized line opened                 					 │
│ 4. Worker under suspended load              					│
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ HIGH — 34 reports                          					 │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ MEDIUM — 87 reports                      					   │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ LOW — 367 reports                        					   │
└─────────────────────────────────────────────┘

But don't blindly use these exact categories.
Research what information/risk dimensions should determine priority.
Then answer:
What makes one report more urgent than another?

### 8. Design the individual report page
Create a wireframe for what happens when an EHS officer clicks a report.
For example:
--------------------------------------------------
SAFETY REPORT #10482
--------------------------------------------------

Original Report
"During maintenance..."

--------------------------------------------------
AI ANALYSIS

SIF PRECURSOR
CRITICAL

Hazard
Energy Isolation

Potential Consequence
Severe injury / fatality

--------------------------------------------------
WHY WAS THIS FLAGGED?

- Isolation not verified
- Equipment remained energized
- Worker exposed to stored energy

--------------------------------------------------
EVENT DETAILS

Activity:
Equipment maintenance

Equipment:
Pump

Exposure:
Technician

Failed Control:
LOTO / isolation

--------------------------------------------------
RECOMMENDED ACTION

Immediate investigation
Verify isolation procedure
Review LOTO compliance

--------------------------------------------------
RELATED REPORTS

7 similar reports
in the last 90 days

--------------------------------------------------
STATUS

[ ] New
[ ] Under Investigation
[ ] Action Assigned
[ ] Resolved
--------------------------------------------------

Your job is to determine what should actually be there.

### 9. Think about "why would an EHS officer trust the AI?"
This is a BIG issue.
Imagine the AI says:
SIF PRECURSOR — CRITICAL
The EHS officer asks:
"Why?"
If the software only gives a probability score, that's weak.
So investigate what kind of evidence/explanation would make the result useful.
For example:
Flagged because:
- Worker exposed to uncontrolled pressure
- Isolation not verified
- Line opened before zero-energy confirmation
The officer should be able to trace the AI's conclusion back to the actual report text.
Your task:
Design what an explainable AI result should look like from the EHS user's perspective.

### 10. Think about false alarms
This is another critical product problem.
Suppose our AI flags:
"Worker forgot safety glasses."
as:
CRITICAL SIF
That's obviously bad.
The EHS officer will quickly stop trusting the system.
So investigate:
What would make an AI alert useful rather than annoying?
Think about:
- Confidence
- Severity
- Evidence
- Context
- Human review
- Uncertainty
- Override
- Feedback
Design how an EHS officer should be able to say:
"AI got this wrong."
or:
"This should actually be high priority."
That feedback could eventually improve the system.

### 11. Think about recurring patterns
This is where the system becomes more than a classifier.
Imagine OIL has:
January
12 isolation-related reports

February
18 isolation-related reports

March
27 isolation-related reports

The EHS officer should ideally notice:
"Energy isolation problems are increasing."
So think about what trends the dashboard should show.
Examples:
By hazard
LOTO              42
Working at Height 31
Dropped Objects   27
Electrical        19
Confined Space    14

By location
Which site/unit has more high-risk observations?
By time
Are high-risk reports increasing?
By department
Is one department producing more recurring issues?
By equipment
Is the same equipment repeatedly involved?
By precursor
Which SIF precursor is appearing most often?
Your job is to identify which trends would actually help an EHS officer make decisions.

### 12. Think about escalation
Not every report should create the same response.
Design a logical workflow such as:
AI analyzes report
        ↓
Risk/Potential identified
        ↓
Low ───────→ Normal review
        │
Medium ────→ EHS review
        │
High ──────→ Priority investigation
        │
Critical ──→ Immediate escalation

But again:
Research and justify what should determine escalation.
Don't just invent arbitrary rules.

### 13. Think beyond "AI says SIF"
Our final system should ideally help answer:
"So what should I do now?"
For example:
AI Detection
      ↓
Explanation
      ↓
Priority
      ↓
Investigation
      ↓
Corrective Action
      ↓
Assignment
      ↓
Follow-up
      ↓
Closure

Think about where our product can help at each stage.
The AI should assist the EHS officer's decision-making, not pretend to replace the safety professional.

### 14. Create the complete product workflow
Your final workflow should look something like:
                SAFETY REPORT
                      ↓
                AI ANALYSIS
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
   SIF PRECURSOR?              NO / LOW
        ↓                           ↓
   Severity / Risk              Normal Queue
        ↓
   Explainable Result
        ↓
   EHS Priority Queue
        ↓
    EHS Review
        ↓
 ┌──────┴─────────┐
 ↓                ↓
Escalate       Normal Action
 ↓                ↓
Investigation   Corrective Action
 └──────┬─────────┘
        ↓
   Action Tracking
        ↓
      Closure
        ↓
 Trend / Recurrence Analysis
        ↓
 Management Insights

Improve this based on your research.

### 15. Build the dashboard/wireframe
You don't need to code it.
Use Figma, Canva, PowerPoint, paper, or even a simple diagram.(don’t over do here, just keep it simple). 
Design at least these screens:
Screen 1 — EHS Dashboard
Show:
- Total reports
- Critical reports
- High-risk reports
- SIF precursor count
- Pending investigations
- Pending corrective actions
- Major recurring hazards
- Trends
Screen 2 — Priority Queue
Show:
- Critical
- High
- Medium
- Low
- Filters
- Search
- Status
Screen 3 — Individual Report
Show:
- Original report
- AI analysis
- SIF result
- Evidence
- Hazard
- Failed control
- Potential consequence
- Explanation
- Recommended next step
Screen 4 — Trends / Analytics
Show:
- Hazard trends
- SIF precursor trends
- Location
- Department
- Time
- Recurring patterns
Screen 5 — Investigation / Action Tracking
Show:
- Assigned action
- Responsible person
- Deadline
- Status
- Closure
- Escalation

### 16. Challenge your own product
After designing it, attack your own idea.
Ask:
"Would an EHS officer actually use this?"
"Are we showing too much information?"
"What information would they need in 10 seconds?"
"What if there are 1,000 reports?"
"What if the AI is wrong?"
"What if two reports describe the same event?"
"What if a critical report has low confidence?"
"What if the report doesn't contain enough information?"
"What if the EHS officer disagrees with the AI?"
"What action happens after the AI flags something?"
"How do we know whether our system actually saved time?"
These questions are more valuable than making the UI look fancy.

### 17. Define our MVP
At the end, decide:
If we only had time to build 5 features for SIH, what are the 5 that actually matter?
For example, you might arrive at:
- AI SIF precursor detection
- Explainable risk analysis
- EHS priority queue
- Similar/recurring hazard detection
- Corrective-action workflow
But don't blindly use these five.
Your research should tell us what the MVP should actually contain.

Final Deliverables
At the end of the 2 days, give us one product research document + wireframes.
Document
### 1. EHS User Profile
Who is using the system and what are their responsibilities?
### 2. Current Workflow
How does a safety report move from submission to closure?
### 3. Manual Tasks
What does the EHS officer currently have to do manually?
### 4. Pain Points
Where does the current process break down?
### 5. User Requirements
What does an EHS officer actually need from our system?
### 6. AI Output Requirements
What information should the AI present after analyzing a report?
### 7. Prioritization Logic
What should make a report urgent/high/medium/low?
### 8. Explainability Requirements
What evidence should accompany an AI prediction?
### 9. Escalation Workflow
What happens after a high-risk report is detected?
### 10. Trend/Analytics Requirements
What patterns should management/EHS be able to see?
### 11. MVP
What are the 5–7 features that actually matter?
### 12. Open Questions
What are you still unsure about?

Wireframes
Create at least:
### 1. EHS Dashboard
### 2. Priority Queue
### 3. Individual Report Analysis
### 4. Trends/Analytics
### 5. Investigation & Corrective Action
They don't have to look beautiful.
They need to make the workflow obvious.

The most important rule
Don't spend two days making a beautiful dashboard.
And don't spend two days reading generic articles about EHS.
Your job is to understand:
What happens when an EHS officer receives a safety report, what decisions they have to make, what information they need, what slows them down, and exactly where our software can remove that friction.
At the end, if I hand you 500 safety reports and ask:
"You are the EHS officer. What do you want this system to do for you?"
You should have a concrete answer.
Our goal isn't:
"Let's build an AI that detects SIF."
Our goal is:
"Let's build a system that helps an EHS officer find the dangerous signals hidden inside hundreds of safety reports, understand why they matter, prioritize them, take action, and identify recurring problems before they become serious incidents."
That difference is what turns an AI demo into an actual product.

## Aditya, Devanshu & Akshay Tasks ⭐

Technical Team — R&D, Models, Training & Dataset
There are 3 of you working on the technical side of the project.
You have 2 days: today and tomorrow.
Your job is to figure out:
How are we actually going to build the AI/NLP engine that takes OIL's unstructured safety reports and detects SIF precursors?
You will work in three parallel areas:
- R&D / Problem Formulation & Architecture
- Model Development & Experiments
- Dataset / Data Engineering & Training Pipeline
You need to work closely with each other, but each person owns one area.

### MEMBER 1 — R&D / Technical Research & System Architecture
**Mission**
Figure out how this problem should technically be formulated and what the complete AI architecture should look like.
You are responsible for answering:
"What exactly are we asking AI to do, and what is the best technical approach to solve it?"

### 1. Formulate the NLP problem
Break our problem into actual ML/NLP tasks.
Don't just call it:
"SIF classification."
Figure out whether we need:
Classification
Example:
Input:
Safety report

Output:
SIF precursor = YES / NO

Multi-class classification
For example:
Report Type:
Unsafe Act
Unsafe Condition
Near Miss
Incident

Multi-label classification
A report may contain:
LOTO
Pressure
Electrical
Human Factor

at the same time.
Information extraction
Extract:
Hazard
Exposure
Failed Control
Potential Consequence
Unsafe Action
Equipment
Activity

Entity recognition
Identify:
Equipment
Location
Activity
Hazard
Person/role

Severity / risk scoring
Determine whether the report should be:
Low
Medium
High
Critical

Explainability
The model should ideally be able to show:
WHY it flagged the report.
Your job is to determine which of these are actually required.

### 2. Research existing approaches
Compare approaches such as:
- TF-IDF + Logistic Regression
- TF-IDF + SVM
- Random Forest
- XGBoost
- Word embeddings
- Sentence embeddings
- BERT-style models
- Domain-adapted transformer models
- Fine-tuned language models
- LLM-based classification
- Retrieval-Augmented Generation
- Hybrid rule + ML systems
Don't research them academically for the sake of it.
For each approach answer:
Approach
Advantage
Disadvantage
Data required
Explainability
Suitable?
TF-IDF + SVM
Simple baseline
Limited semantics
Low
Good-ish
?
Transformer
Semantic understanding
More compute
Medium
Moderate
?
LLM
Strong reasoning
Cost/consistency
Low/medium
Good
?
Hybrid
Rules + ML
More engineering
Medium
Strong
?

Your goal is to recommend a technical approach.

### 3. Design the complete architecture
Create the proposed pipeline:
Raw Safety Report
        ↓
Preprocessing
        ↓
Text Normalization
        ↓
Information Extraction
        ↓
Hazard / Event Understanding
        ↓
SIF Precursor Detection
        ↓
Severity / Risk
        ↓
Explanation
        ↓
EHS Priority
        ↓
Dashboard/API

Decide what model/component operates at each stage.

### 4. Think about the hardest technical problems
Identify things like:
- Class imbalance
- Very few SIF examples
- Noisy labels
- Short reports
- Long reports
- Domain-specific terminology
- Spelling mistakes
- Abbreviations
- Hindi/English mixing if applicable
- Similar-looking hazards
- Context-dependent severity
- False positives
- False negatives
- Explainability
- Data leakage
- Synthetic data contamination
Create a:
Technical Risk Register
Problem
Why it matters
Proposed solution
Few SIF examples
Model may not learn minority class
...
Class imbalance
Accuracy becomes misleading
...
Domain vocabulary
Generic models may misunderstand terms
...
False negatives
Dangerous reports may be missed
...


### 5. Final deliverable
You must give:
- Problem formulation
- Literature/approach comparison
- Architecture diagram
- Model recommendation
- Evaluation strategy
- Technical risks
- MVP technical pipeline

### MEMBER 2 — Model Development & Experimentation
**Mission**
Build and test the actual NLP models and determine what performs best.
Your job is not to endlessly research models.
Run experiments.

### 1. Establish a baseline
Start simple.
Build something like:
TF-IDF
   ↓
Logistic Regression / SVM
   ↓
SIF classification

Why?
Because we need to know whether sophisticated models actually improve performance.
Don't jump straight to an LLM.

### 2. Build progressively stronger models
Depending on available data/resources, compare:
Model A
TF-IDF + Logistic Regression
Model B
TF-IDF + SVM
Model C
Sentence embeddings + classifier
Model D
Transformer-based classifier
Model E
LLM / prompt-based approach
You don't necessarily need all five fully implemented.
Prioritize the approaches that are realistic with our dataset and hardware.

### 3. Test multiple tasks
At minimum investigate:
Task 1
SIF precursor:
YES / NO

Task 2
Risk:
LOW / MEDIUM / HIGH / CRITICAL

Task 3
Hazard category:
...

Task 4
Extract important fields if feasible.

### 4. Evaluate properly
Do NOT report only:
Accuracy = 95%
That's potentially meaningless.
Especially if:
950 normal reports
50 SIF reports

A model that predicts:
NO SIF
for everything gets:
95% accuracy
while being completely useless.
Measure:
- Precision
- Recall
- F1-score
- Confusion matrix
- Per-class metrics
- PR-AUC if appropriate
For SIF detection, pay special attention to:
Recall for the SIF class.
Because missing a genuinely dangerous report can be much worse than generating a review-worthy false alarm.
But also measure precision because an alert system that flags everything will be ignored.

### 5. Perform error analysis
This is mandatory.
Take incorrect predictions and ask:
Why did the model get this wrong?
Create:
Report
Actual
Prediction
Why wrong?
Example A
SIF
Non-SIF
Indirect language
Example B
Non-SIF
SIF
Keyword triggered false positive

Look for patterns:
- Missing context
- Negation
- Ambiguous wording
- Rare terminology
- Long reports
- Multiple hazards
- Implicit consequences
- Domain-specific language
Then improve the model.

### 6. Test robustness
Create variations of the same report.
Example:
"LOTO was not followed."
vs
"Isolation was not verified."
vs
"Equipment remained energized."
Check whether the model recognizes that these are related situations.
Also test:
Negation
"LOTO was followed correctly."
The model should NOT flag this merely because it sees "LOTO."
Context
"Worker had completed isolation before maintenance."
Different from:
"Worker started maintenance before isolation."
This is extremely important.

### 7. Experiment with explainability
Investigate how we can show:
Why did the model flag this report?
Possible approaches:
- Important words/phrases
- Highlighted evidence
- SHAP
- Attention visualization
- Extracted entities
- Rule-based evidence
- LLM explanation layer
Determine what is technically reliable enough for our prototype.

### 8. Final deliverable
You must provide:
- Baseline model
- Best-performing model
- Experiment results
- Metrics
- Confusion matrix
- Error analysis
- Robustness tests
- Explainability approach
- Recommended final model
And ideally:
A working inference script/API that takes a safety report and returns the model's prediction.

### MEMBER 3 — Dataset / Data Engineering & Training Pipeline
**Mission**
Build the data foundation that allows the model to learn and be evaluated reliably.
Your biggest question is:
"Do we actually have enough usable data to train this system, and if not, how do we construct a credible dataset?"

### 1. Find available data
Investigate potential sources such as:
- OIL public material
- Oil & gas safety reports
- Government safety reports
- OSHA
- HSE
- CSB
- Industrial incident databases
- Academic datasets
- Public near-miss datasets
- Kaggle/public repositories
- Other legitimate sources
For every source record:
Source
Size
Domain
Text?
Labels?
SIF labels?
License
Usable?
Source A
5,000
Oil/Gas
Yes
Yes
No
...
...

The most important thing:
Verify licensing/usage restrictions.
Don't blindly scrape something and assume we can use it.

### 2. Determine the data problem
Answer:
How many reports do we actually have?
How many are SIF?
How many are non-SIF?
How many belong to each hazard?
How many are near misses?
How many are unsafe acts?
How many are unsafe conditions?
Create distributions.
Example:
Total reports: 10,000

SIF:
    500

Non-SIF:
    9,500

Hazards:
    LOTO          1200
    Height         900
    Electrical     700
    ...

This tells us whether we're facing severe class imbalance.

### 3. Create the data schema
Define the dataset structure.
For example:
report_id
report_text
report_type
sif_label
hazard_category
severity
unsafe_act
unsafe_condition
potential_consequence
failed_control
location
equipment
source

Do NOT blindly copy these fields.
Coordinate with the other team members and decide what is actually available and useful.

### 4. Build the annotation strategy
If SIF labels don't exist, determine how we can create them.
Design:
Annotation guidelines
What does:
SIF = YES
SIF = NO
UNCERTAIN

mean?
Who labels?
How many annotators?
How do disagreements get resolved?
How do we measure agreement?
For example:
Annotator A ──┐
              ├──→ Adjudication → Final Label
Annotator B ──┘

If possible, use inter-annotator agreement such as Cohen's Kappa.

### 5. Build a high-quality seed dataset
Before trying to train on thousands of noisy examples, create a smaller high-quality labeled set.
For example:
500–1000 carefully reviewed reports

depending on actual availability.
Focus on balanced and representative examples.
Include:
- Positive SIF examples
- Hard negatives
- Near misses
- Routine unsafe observations
- Ambiguous reports
- Different hazard categories
- Different writing styles

### 6. Handle class imbalance
Investigate:
- Class weights
- Oversampling
- Undersampling
- Stratified sampling
- Focal loss
- Data augmentation
- Synthetic examples
But don't randomly duplicate data and call it solved.
Explain which approach makes sense and why.

### 7. Data cleaning
Build preprocessing for:
- Duplicate reports
- Empty reports
- HTML/noise
- Spelling errors
- Abbreviations
- Encoding issues
- Personally identifiable information
- Repeated templates
- Extremely short reports
- Extremely long reports
Keep:
Raw data → Cleaned data
separate.
Never destroy the original dataset.

### 8. Prevent data leakage
This is extremely important.
Make sure nearly identical reports don't appear in both:
Training
   +
Validation
   +
Test

Otherwise we'll get fake high accuracy.
Use appropriate splitting strategies.
For example:
- Duplicate-aware split
- Grouped split
- Time-based split if timestamps exist
The final test set should be genuinely unseen.

### 9. Create the training pipeline
Build:
Raw Data
   ↓
Cleaning
   ↓
Deduplication
   ↓
Annotation
   ↓
Train / Validation / Test
   ↓
Tokenization / Embeddings
   ↓
Training
   ↓
Evaluation

Make it reproducible.
If someone runs the pipeline again, they should get the same dataset split and experiment setup.

### 10. Create the final dataset documentation
Document:
- Where data came from
- How it was cleaned
- How it was labeled
- Label definitions
- Class distribution
- Known biases
- Missing data
- Licensing
- Train/validation/test split
- Limitations
This becomes extremely valuable during the SIH presentation.

Final deliverable
You must provide:
- Dataset inventory
- Data availability assessment
- Dataset schema
- Annotation guidelines
- Seed labeled dataset
- Cleaning pipeline
- Train/validation/test split
- Class distribution
- Leakage checks
- Data limitations
- Reproducible training data pipeline

HOW THE 3 TECHNICAL MEMBERS WORK TOGETHER
Don't work as three isolated people.
The flow should be:
             R&D / ARCHITECTURE
                     │
                     ↓
             What should we build?
                     │
                     ↓
             DATA ENGINEERING
                     │
                     ↓
             What data do we have?
                     │
                     ↓
              MODEL DEVELOPMENT
                     │
                     ↓
             What actually works?
                     │
                     ↓
                ERROR ANALYSIS
                     │
                     ↓
              Back to R&D/Data
                     │
                     ↓
              Improve → Test → Repeat


Your 2-Day Target
TODAY
R&D Member
Produce:
Technical problem formulation + architecture v1
Model Member
Produce:
Baseline model + first experiment
Data Member
Produce:
Dataset inventory + data availability analysis + initial schema

TOMORROW
R&D Member
Finalize:
Technical architecture + model strategy + technical risk analysis
Model Member
Produce:
Model comparison + evaluation + error analysis + recommended model
Data Member
Produce:
Clean/annotated seed dataset + train/test strategy + data pipeline

By the end of tomorrow, we should have this:
                   OUR AI SYSTEM
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
        DOMAIN          DATA           MODEL
       KNOWLEDGE      FOUNDATION      ENGINE
          │              │              │
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  NLP PIPELINE
                         ↓
                 SIF DETECTION
                         ↓
                  EXPLANATION
                         ↓
                RISK / PRIORITY
                         ↓
                    EHS USER

The other 3 members are defining the domain, report understanding, and EHS workflow.
You three are responsible for turning that knowledge into a technically credible AI system.
The goal of these two days is NOT to build the final SIH product.
The goal is to remove the biggest uncertainties:
Can we get enough data?
Can we label the problem properly?
What ML/NLP formulation actually makes sense?
Which model performs best?
What does the architecture look like?
Where will the system fail?
Can we build a working end-to-end prototype?
If we can answer those questions with evidence after these two days, we'll have a much stronger foundation for the actual SIH build.














