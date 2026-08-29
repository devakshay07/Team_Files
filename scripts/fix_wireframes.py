with open("design/wireframes.md", "r") as f:
    content = f.read()

replacement = """## Screen 1 — EHS Dashboard
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
  |  Pressure:   ████ 15                              |  |                         |"""

import re
content = re.sub(r'## Screen 1 — EHS Dashboard.*?\|  Pressure:   ████ 15                              \|  \|                         \|', replacement, content, flags=re.DOTALL)
with open("design/wireframes.md", "w") as f:
    f.write(content)
