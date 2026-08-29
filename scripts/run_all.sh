#!/bin/bash
set -e
echo "=========================================="
echo "    SILENT STACK MLOPS PIPELINE TEST      "
echo "=========================================="

echo "1. Running Data Pipeline (Member 1)..."
source .venv/bin/activate && python3 src/data/pipeline.py

echo -e "\n2. Training Model (Member 3)..."
source .venv/bin/activate && python3 src/models/train.py

echo -e "\n3. Running Integration Test (End-to-End)..."
source .venv/bin/activate && python3 tests/integration/test_end_to_end.py

echo -e "\n4. Running API Integration Test..."
source .venv/bin/activate && python3 tests/integration/test_api.py

echo -e "\n5. Running Error Analysis Audit..."
source .venv/bin/activate && python3 tests/integration/test_error_analysis.py > docs/error_analysis_report.txt

echo -e "\n6. Running NLP Unit Tests..."
source .venv/bin/activate && python3 tests/integration/test_nlp_extraction.py

echo -e "\n7. Running API Contracts Security Audit..."
source .venv/bin/activate && python3 tests/integration/test_contracts.py

echo -e "\n=========================================="
echo "✅ ALL PIPELINES AND TESTS PASSED SUCCESSFULLY."
echo "=========================================="
