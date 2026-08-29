import re

with open('domain/renuka_extraction_framework.md', 'r') as f:
    content = f.read()

# Add columns to header
content = content.replace(
    "| Report Text | Activity | Hazard | Unsafe Act / Condition | Failed Control | SIF? | Priority |",
    "| Report Text | Activity | Hazard | Unsafe Act / Condition | Failed Control | SIF? | Priority | Immediate Action | Intervention | Corrective Action | Preventive Action | Work Stopped |"
)
content = content.replace(
    "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
)

# Fix rows - append 5 dummy columns to each data row
def process_row(match):
    row = match.group(0)
    if "Priority" in row or ":---" in row:
        return row
    return row.rstrip() + " None | None | None | None | None |\n"

# Match markdown table rows starting with | and ending with | followed by newline
new_content = re.sub(r'^\|.*\|\n', process_row, content, flags=re.MULTILINE)

with open('domain/renuka_extraction_framework.md', 'w') as f:
    f.write(new_content)
