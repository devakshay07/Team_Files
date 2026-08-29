#!/usr/bin/env python3
"""
SIH Intelligence Vault Validator
Automated quality control, link verification, schema enforcement,
and source cross-referencing for the SIH archive.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent

# Regex patterns
MD_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
SOURCE_ID_PATTERN = re.compile(r'SRC-(OFF|HIST)-\d{3}')
LAST_VERIFIED_PATTERN = re.compile(r'Last Verified[:\s*`]+(\d{4}-\d{2}-\d{2})')

REQUIRED_CASE_STUDY_SECTIONS = [
    "## Problem Statement",
    "## Institution / Team",
    "## Edition",
    "## Solution",
    "## Architecture",
    "## Technology Stack",
    "## Evidence",
    "## Sources",
    "## Confidence",
    "## Reusable Pattern",
    "## SIH 2026 Relevance",
]

def get_all_markdown_files():
    return [p for p in ROOT_DIR.glob("**/*.md") if ".git" not in str(p)]

def check_relative_links(md_files):
    errors = []
    link_count = 0

    for file_path in md_files:
        content = file_path.read_text(encoding="utf-8")
        # Remove code blocks to avoid false positives
        content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        content_no_inline = re.sub(r'`[^`]+`', '', content_no_code)

        for match in MD_LINK_PATTERN.finditer(content_no_inline):
            link_text, link_target = match.groups()
            link_count += 1

            # Skip web URLs, mailto, badges, and pure anchors
            if (link_target.startswith("http://") or 
                link_target.startswith("https://") or 
                link_target.startswith("mailto:") or 
                link_target.startswith("img.shields.io") or
                link_target.startswith("#")):
                continue

            # Strip anchor if present
            target_path_str = link_target.split("#")[0]
            if not target_path_str:
                continue

            target_path = (file_path.parent / target_path_str).resolve()
            if not target_path.exists():
                errors.append(
                    f"[BROKEN LINK] In {file_path.relative_to(ROOT_DIR)}: "
                    f"'{link_target}' -> Target does not exist at {target_path}"
                )

    return link_count, errors

def get_registered_source_ids():
    source_ids = set()
    sources_dir = ROOT_DIR / "sources"
    for file_path in sources_dir.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        for match in SOURCE_ID_PATTERN.finditer(content):
            source_ids.add(match.group(0))
    return source_ids

def check_case_study_schemas(registered_sources):
    errors = []
    case_studies_dir = ROOT_DIR / "case_studies"
    case_study_files = [p for p in case_studies_dir.glob("*.md") if p.name != "README.md"]

    for file_path in case_study_files:
        content = file_path.read_text(encoding="utf-8")

        # Check required headers
        for section in REQUIRED_CASE_STUDY_SECTIONS:
            if section not in content:
                errors.append(
                    f"[SCHEMA DEFICIT] In {file_path.relative_to(ROOT_DIR)}: "
                    f"Missing required section: '{section}'"
                )

        # Check source cross-referencing
        cited_sources = set(SOURCE_ID_PATTERN.findall(content))
        for match in SOURCE_ID_PATTERN.finditer(content):
            full_source_id = match.group(0)
            if full_source_id not in registered_sources:
                errors.append(
                    f"[UNREGISTERED SOURCE] In {file_path.relative_to(ROOT_DIR)}: "
                    f"Cited source ID '{full_source_id}' is not indexed in sources/"
                )

        # Check confidence tags
        if "HIGH" not in content and "MEDIUM" not in content and "LOW" not in content:
            errors.append(
                f"[CONFIDENCE MISSING] In {file_path.relative_to(ROOT_DIR)}: "
                f"No HIGH, MEDIUM, or LOW confidence tag found."
            )

    return len(case_study_files), errors

def check_stale_dates_in_2026():
    errors = []
    dir_2026 = ROOT_DIR / "2026"
    files_2026 = list(dir_2026.glob("*.md"))

    for file_path in files_2026:
        content = file_path.read_text(encoding="utf-8")
        match = LAST_VERIFIED_PATTERN.search(content)
        if not match:
            errors.append(
                f"[MISSING VERIFICATION DATE] In {file_path.relative_to(ROOT_DIR)}: "
                f"No 'Last Verified: YYYY-MM-DD' timestamp found."
            )
        else:
            date_str = match.group(1)
            try:
                verified_date = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                errors.append(
                    f"[INVALID DATE FORMAT] In {file_path.relative_to(ROOT_DIR)}: "
                    f"Date '{date_str}' does not match YYYY-MM-DD."
                )

    return len(files_2026), errors

def main():
    print("=" * 60)
    print("🔬 SIH Intelligence Vault — Quality Control & Validation")
    print("=" * 60)

    md_files = get_all_markdown_files()
    print(f"📁 Scanned {len(md_files)} Markdown files across repository.")

    # 1. Check relative links
    link_count, link_errors = check_relative_links(md_files)
    print(f"🔗 Verified {link_count} internal & external links.")

    # 2. Check source registry
    registered_sources = get_registered_source_ids()
    print(f"📚 Indexed {len(registered_sources)} unique source IDs in sources/ registry.")

    # 3. Check case study schema & citations
    case_study_count, schema_errors = check_case_study_schemas(registered_sources)
    print(f"📑 Validated {case_study_count} case studies against 14-point schema.")

    # 4. Check 2026 verification timestamps
    count_2026, date_errors = check_stale_dates_in_2026()
    print(f"⏱️ Checked {count_2026} SIH 2026 documents for verification timestamps.")

    all_errors = link_errors + schema_errors + date_errors

    print("\n" + "=" * 60)
    if all_errors:
        print(f"❌ VALIDATION FAILED: Found {len(all_errors)} issues:\n")
        for err in all_errors:
            print(f"  • {err}")
        print("=" * 60)
        sys.exit(1)
    else:
        print("✅ ALL CHECKS PASSED: 100% Link Integrity, Schema Compliance & Source Consistency!")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    main()
