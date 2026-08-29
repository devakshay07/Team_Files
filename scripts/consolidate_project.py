import os

output_file = "silent_stack_final_submission.md"

members = [
    {
        "name": "PART 1: Domain Knowledge (Anandita)",
        "files": [
            "domain/sif_domain_knowledge.md",
            "domain/causal_chains.csv",
            "domain/taxonomy.json"
        ]
    },
    {
        "name": "PART 2: Data Extraction Framework (Renuka)",
        "files": [
            "domain/renuka_extraction_framework.md",
            "schema/language_variations.json"
        ]
    },
    {
        "name": "PART 3: Product & UX Design (Manish)",
        "files": [
            "design/manish_product_research.md",
            "design/wireframes.md"
        ]
    },
    {
        "name": "PART 4: Architecture & Formulation (Aditya)",
        "files": [
            "domain/aditya_technical_formulation.md",
            "domain/aditya_architecture.md",
            "backend/app.py"
        ]
    },
    {
        "name": "PART 5: Model Engine (Devanshu)",
        "files": [
            "model/artifacts/metrics_report.md",
            "model/error_analysis.md",
            "model/train.py",
            "model/robustness_tests.py"
        ]
    },
    {
        "name": "PART 6: Data Pipeline & Schema (Akshay)",
        "files": [
            "domain/akshay_data_sources.md",
            "schema/extraction_schema.py",
            "data_pipeline/annotation_guidelines.md",
            "data_pipeline/output/dataset_inventory.md",
            "data_pipeline/pipeline.py"
        ]
    }
]

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("# Team Silent Stack - Consolidated Project Submission\n\n")
    outfile.write("> This document compiles the final deliverables of all 6 team members as per the initial requirements.\n\n")
    
    for member in members:
        outfile.write(f"## {member['name']}\n\n")
        for filepath in member['files']:
            if os.path.exists(filepath):
                outfile.write(f"### File: `{filepath}`\n\n")
                ext = filepath.split('.')[-1]
                if ext in ['py', 'json', 'csv']:
                    outfile.write(f"```{ext}\n")
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                    outfile.write("\n```\n\n")
                else:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")
            else:
                outfile.write(f"### File: `{filepath}` (MISSING)\n\n")

print(f"Consolidated file written to {output_file}")
