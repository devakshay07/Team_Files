# Dataset Inventory & Analysis

## Overview
- **Total Cleaned Reports**: 1171
- **Data Source**: Synthetic generation (simulating OIL reports)

## Class Distribution (SIF vs Non-SIF)
This highlights the class imbalance challenge for the model development team.
- **NO**: 1116 (95.3%)
- **YES**: 55 (4.7%)

## Hazard Category Distribution
- **Working at Height**: 196
- **Pressure**: 190
- **Energy Isolation**: 189
- **Electrical**: 178
- **Manual Handling**: 145
- **Slips/Trips**: 140
- **Confined Space**: 133

## Report Type Distribution
- **Unsafe Act**: 576
- **Unsafe Condition**: 566
- **Near Miss**: 29

## Known Limitations & Biases
- Data is currently synthetic and generated via templated patterns.
- Near-duplicates might still exist if they vary slightly in wording (exact duplicates are removed).
- Lexical diversity is lower than in real-world messy data.

## Annotation Pipeline / Readiness
Since this is synthetic data, labels are perfectly matched to text. For real data, an annotation UI and inter-annotator agreement (e.g., Cohen's Kappa) workflow must be implemented.
