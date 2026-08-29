# Dataset Inventory & Analysis

## Overview
- **Total Cleaned Reports**: 1176
- **Data Source**: Synthetic generation (simulating OIL reports)

## Class Distribution (SIF vs Non-SIF)
This highlights the class imbalance challenge for the model development team.
- **NO**: 1116 (94.9%)
- **YES**: 60 (5.1%)

## Hazard Category Distribution
- **Confined Space**: 187
- **Pressure**: 187
- **Working at Height**: 185
- **Energy Isolation**: 158
- **Electrical**: 155
- **Manual Handling**: 155
- **Slips/Trips**: 149

## Report Type Distribution
- **Unsafe Act**: 573
- **Unsafe Condition**: 571
- **Near Miss**: 32

## Known Limitations & Biases
- Data is currently synthetic and generated via templated patterns.
- Near-duplicates might still exist if they vary slightly in wording (exact duplicates are removed).
- Lexical diversity is lower than in real-world messy data.

## Annotation Pipeline / Readiness
Since this is synthetic data, labels are perfectly matched to text. For real data, an annotation UI and inter-annotator agreement (e.g., Cohen's Kappa) workflow must be implemented.
