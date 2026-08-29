import re

with open('/Users/akshaybhagat/.gemini/antigravity/brain/fbd708e4-76cd-4088-a4c2-bb18dd1fdcc4/scratch/tasks.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
out.append("# Team Silent Stack - SIH 2026 Tasks\n")
out.append("\n## Team Members Overview\n")
out.append("1. **Anandita** - Domain Expert (SIF Precursors in Oil & Gas)\n")
out.append("2. **Renuka** - Data Extractor (Safety Report Information Extraction)\n")
out.append("3. **Manish** - Product & UX Designer (EHS Officer Workflow)\n")
out.append("4. **Aditya** - Technical Team (R&D / Technical Research & System Architecture)\n")
out.append("5. **Devanshu** - Technical Team (Model Development & Experimentation)\n")
out.append("6. **Akshay** - Technical Team (Dataset / Data Engineering & Training Pipeline)\n\n")
out.append("---\n\n")

for line in lines:
    original = line
    line = line.strip()
    if not line:
        out.append("\n")
        continue

    # Member Headers
    if "⭐" in line:
        out.append(f"## {line}\n")
        continue

    # Tasks / Subsections
    if re.match(r'^\d+\.\s+[A-Z]', line):
        out.append(f"### {line}\n")
        continue
    
    # Subheaders for tech team
    if line.startswith("MEMBER 1 —") or line.startswith("MEMBER 2 —") or line.startswith("MEMBER 3 —"):
        out.append(f"### {line}\n")
        continue
    
    if line == "Mission":
        out.append(f"**{line}**\n")
        continue

    # Bullet points
    if line.startswith("•\t") or line.startswith("• "):
        out.append(f"- {line[1:].strip()}\n")
        continue
    
    # Check if line looks like a sub-header (short, capitalized)
    if len(line) < 50 and not line.endswith(".") and not line.endswith(":") and not line.endswith("?") and not line.endswith(",") and line[0].isupper() and " " in line:
        # Avoid treating normal sentences without punctuation as headers
        pass

    out.append(f"{original}")

with open('/Users/akshaybhagat/Documents/silentStack/teamTask.md', 'w', encoding='utf-8') as f:
    f.writelines(out)

