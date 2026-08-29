import re

with open('domain/renuka_extraction_framework.md', 'r') as f:
    content = f.read()

def process_example(match):
    block = match.group(0)
    return block + "* **Immediate Action**: None\n* **Intervention**: None\n* **Corrective Action**: None\n* **Preventive Action**: None\n* **Work Stopped**: None\n"

new_content = re.sub(r'^\* \*\*Priority:.*?\n', process_example, content, flags=re.MULTILINE)

with open('domain/renuka_extraction_framework.md', 'w') as f:
    f.write(new_content)
