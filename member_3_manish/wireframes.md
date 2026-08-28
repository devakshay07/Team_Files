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
