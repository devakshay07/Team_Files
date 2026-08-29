import os

content = """# O&G Data Availability & Migration Plan

## Section 1 — Data Availability Assessment
* **Public Labeled O&G Data:** Highly scarce. The Oil & Gas industry considers safety incident data to be highly proprietary and sensitive. 
* **Available Raw Data:** Thousands of unstructured incident summaries are publicly available from regulatory bodies (OSHA, HSE, CSB), but they lack explicit SIF precursor labels.
* **Conclusion:** We cannot rely on finding a pre-labeled "SIF Precursor" dataset. We must aggregate raw public data and construct the labels ourselves using our defined taxonomy (Anandita's work) or an LLM-assisted annotation pipeline.

## Section 2 — Source Inventory Table

| Source | URL | Estimated Size | Domain | Has Text? | Has Labels? | Has SIF Labels? | License | Usable? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OSHA Severe Injury Reports** | osha.gov | ~50,000+ | General Ind. | Yes | Yes (injury type) | No | Public Domain | **Yes** |
| **HSE (UK) Incident Database** | hse.gov.uk | ~10,000 | Ind/O&G | Yes | Yes (general) | No | Open Government Licence (OGL) | **Yes** |
| **CSB Investigation Reports** | csb.gov | ~150 | Chem/O&G | Yes (PDFs) | No | No | Public Domain | **Yes** (Requires OCR) |
| **IADC Safety Alerts** | iadc.org | ~200 | Drilling/O&G | Yes | No | No | Copyrighted | No (Reference only) |
| **Kaggle Industrial Safety** | kaggle.com | ~500 | Assorted | Yes | Yes (Severity) | No | CC-BY | **Yes** |
| **IOGP Safety Alerts** | iogp.org | ~300 | O&G | Yes | No | No | Copyrighted | No (Reference only) |

## Section 3 — Licensing Analysis
* **Public Domain (OSHA, CSB):** Completely unrestricted. We can ingest, modify, and train models on this data for any purpose, including commercial deployment and hackathons.
* **OGL (HSE):** Free to use and adapt, provided we acknowledge the source. Perfectly suitable for SIH.
* **CC-BY (Kaggle):** Usable with attribution. 
* **Copyrighted (IADC, IOGP):** We cannot scrape these in bulk to train a commercial AI without explicit permission. We will exclude them from the automated pipeline and use them only as manual references for taxonomy building.

## Section 4 — Data Collection Strategy
* **Primary Target:** OSHA Severe Injury Reports. It contains thousands of short narratives describing how injuries occurred. 
* **Filtering Strategy:** Filter the OSHA dataset for NAICS codes matching Oil & Gas Extraction (211), Support Activities for Mining (213), and Chemical Manufacturing (324, 325).
* **Annotation Strategy:** Since OSHA data lacks SIF precursor labels, we will use a zero-shot LLM prompt (incorporating Anandita's Causal Chains) to pre-annotate 1,000 reports, then manually adjudicate them to create our high-quality seed dataset.

## Section 5 — Synthetic Data Justification
For the initial 48-hour hackathon, scraping, cleaning, filtering, and manually annotating 1,000 OSHA reports was not feasible. 
The current pipeline uses `synthetic_data.py` to generate templates. 
* **Limitation:** The model currently achieves artificial 100% accuracy because the synthetic data lacks the messy linguistic entropy of real human reporting. 
* **Value:** The synthetic data proved that our *data pipeline architecture* (cleaning, stratified splitting, leakage prevention) and *model training architecture* function correctly end-to-end.

## Section 6 — Migration Plan
To replace synthetic data with real data before production:
1. **Scraping:** Write a Python script to download the OSHA Severe Injury CSVs.
2. **Filtering:** Drop rows outside of relevant NAICS codes.
3. **Mapping:** Rename OSHA column `Final_Narrative` to `report_text`.
4. **Annotation:** Run the filtered CSV through an LLM to generate `sif_label` (YES/NO) and `hazard_category`.
5. **Integration:** Place the annotated `osha_labeled.csv` into `data_pipeline/raw/`.
6. **Execution:** Re-run `data_pipeline/pipeline.py` to clean and split the real data.
7. **Retraining:** Re-run `model/train.py` to train the TF-IDF model on actual human text.
"""

filepath = os.path.join("domain", "akshay_data_sources.md")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
