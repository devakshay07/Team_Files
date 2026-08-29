import os

filepath = "domain/renuka_extraction_framework.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Section 5 Title
content = content.replace("## Section 5 — Incident Classification Guide", "## Section 5 — Incident Classification")

# Add missing fields to Section 2
new_rows = """| **Immediate Action Taken** | Response right after observation. | "stopped work", "evacuated" | "Work stopped immediately" |
| **Intervention** | Who intervened. | "supervisor stepped in", "co-worker yelled" | "Colleague stopped him" |
| **Corrective Action** | What was done to fix. | "replaced lock", "cleaned spill" | "Replaced harness" |
| **Preventive Action** | Long term fix. | "updated procedure", "re-trained" | "Updated LOTO SOP" |
| **Work Stopped** | Was a stop-work authority used? | "stopped", "paused" | "Yes" |
"""

content = content.replace('| **Priority** | EHS triage urgency. | Based on SIF + likelihood. | "CRITICAL", "HIGH", "LOW" |\n', '| **Priority** | EHS triage urgency. | Based on SIF + likelihood. | "CRITICAL", "HIGH", "LOW" |\n' + new_rows)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
