# Official SIH 6-Slide Idea Presentation Template & Blueprint

[🏠 Home](../README.md) > [📁 Submission Guides](./official_sih_ppt_template.md) > **6-Slide Presentation Blueprint**

> **Standard AICTE / Ministry of Education's Innovation Cell (MIC) Format**  
> *Note: For the official SIH idea submission phase (Deadline: September 15, 2026), teams must strictly adhere to a **maximum of 6 slides** and upload exclusively in **PDF format** (`< 10 MB`).*

---

## 🎯 Quick Rules & Strict Constraints

> [!IMPORTANT]
> - **Slide Count**: Strictly **6 slides**. Submissions with 7+ slides or appendix pages are flagged during automated screening.
> - **Format**: Single compiled `.pdf` file under **10 MB**.
> - **Aspect Ratio**: Standard **16:9** Widescreen format.
> - **Typography**: Clean Sans-Serif font (Inter, Roboto, Arial) — min 14pt body, min 24pt headers.

---

## 🖼️ Slide-by-Slide Visual Blueprint

```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│ SLIDE 1: COVER & TEAM DETAILS         │ SLIDE 2: PROBLEM & PROPOSED SOLUTION  │
│ • PS ID | PS Title | Theme | Category │ • Core Bottlenecks | Solution Pillars │
│ • Ministry Name | Institute Details   │ • Unique Selling Proposition (USP)    │
│ • Leader & 5 Member Names / Emails    │ • Quantified Real-World Inefficiency  │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ SLIDE 3: TECHNICAL ARCHITECTURE       │ SLIDE 4: FEASIBILITY & RISK DEFENSE   │
│ • End-to-End System Block Diagram     │ • Technical Feasibility & Latency PoC │
│ • Tech Stack: Frontend, API, AI, DB   │ • Operational & Hardware BOM Viability│
│ • Step-by-Step Data Flow 1 ➔ 2 ➔ 3    │ • 3 Critical Risks & Mitigation Plan  │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ SLIDE 5: IMPACT, SCALE & OPEX DEFENSE │ SLIDE 6: RESEARCH & TEAM COMPETENCE   │
│ • Direct Beneficiaries & Metrics      │ • 3-4 Academic / Gov Data Citations   │
│ • Scale Plan: 1 District ➔ 700 Dist   │ • Role Mapping for all 6 Members      │
│ • OpEx Cost Formula vs Commercial ERP │ • Preliminary Repo / Benchmark PoC    │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

---

## 📋 Detailed Slide Specifications

### 🏷️ Slide 1: Cover Page & Institutional Details
* **Header Banner**: Smart India Hackathon (SIH 2026) — Idea Submission
* **Problem Statement ID**: e.g. `SIH1556` *(Must match the SIH portal verbatim)*
* **Problem Statement Title**: Full official title from the ministry
* **Theme & Category**: Theme name + `Software` or `Hardware`
* **Ministry / Department**: e.g. *Ministry of AYUSH / Ministry of Defence / India Post*
* **Team Name**: e.g. *SilentStack*
* **Team Composition**:
  * **Team Leader**: Full Name, Branch, Year, Official Email, Phone
  * **Members 1..5**: Full Name, Branch, Year, Email *(Ensure $\ge 1$ female member)*
* **College / Institute Details**: Full Institute Name + AICTE / AISHE Affiliation Code + State

---

### 💡 Slide 2: Problem Articulation & Proposed Solution
* **The Core Bottleneck**:
  * Highlight the primary 2–3 acute bottlenecks of the ministry/target user.
  * Cite specific real-world statistics *(e.g. "Average rural queue wait time 28 mins; manual verification backlog 45 days")*.
* **Proposed Solution**:
  * A clear 2-sentence executive summary of what your software/hardware does.
  * 3 visual bullet pillars explaining the core mechanism.
* **Novelty / Innovation / USP (Unique Selling Proposition)**:
  * Why this approach fundamentally outperforms existing commercial or academic attempts.
  * Highlight offline-first capabilities, edge inference, zero-cost public infra, or proprietary algorithms.

---

### 🏗️ Slide 3: Technical Architecture & Methodology
* **System Architecture Diagram**:
  * High-resolution flowchart or block diagram representing end-to-end data flow:
    $$\text{[Sensors / User Input]} \longrightarrow \text{[API Gateway \& Auth]} \longrightarrow \text{[Core AI / Edge Engine]} \longrightarrow \text{[Database / Storage]} \longrightarrow \text{[Client UI / SMS Bot]}$$
* **Technology Stack Breakdown**:
  * **Frontend**: Framework (Next.js / Flutter / React PWA), state management, offline cache.
  * **Backend & APIs**: Framework (FastAPI / Node.js / Go), Redis caching, Celery / RabbitMQ.
  * **AI / ML Pipeline**: Models, quantization framework (ONNX Runtime / TensorRT), inference latency.
  * **Database & Security**: Primary DB (PostgreSQL / TimescaleDB), encryption (AES-256 GCM), DPDP Act compliance.
  * **Hardware / IoT (if Hardware)**: Microcontroller (ESP32/STM32), sensors, protocols (LoRa, MQTT, BLE).

---

### 🛡️ Slide 4: Feasibility, Viability & Risk Mitigation
* **Technical Feasibility**:
  * Proof of concept validation (algorithms are proven, open-source models exist, latency is sub-200ms).
  * Bill of Materials (BOM) cost breakdown if competing in Hardware edition.
* **Operational Viability**:
  * How grassroots government staff, farmers, or citizens interact with zero learning curve.
* **3 Critical Risks & Mitigation Matrix**:
  * ⚠️ *Risk 1 (Rural Network Dropouts)* $\rightarrow$ *Mitigation: Local SQLite offline caching with bidirectional sync.*
  * ⚠️ *Risk 2 (Adversarial Inputs / Dirty Data)* $\rightarrow$ *Mitigation: Strict schema validation + anomaly thresholding.*
  * ⚠️ *Risk 3 (High Server Compute Cost)* $\rightarrow$ *Mitigation: Quantized on-device edge compute (<₹0.05/transaction).*

---

### 📈 Slide 5: Real-World Impact, Scalability & Commercial Potential
* **Target Beneficiaries**:
  * Primary: Government department, ground field officers, citizens.
  * Secondary: Researchers, third-party logistics, auditing bodies.
* **Quantifiable Impact Metrics**:
  * Projected time reduction *(e.g. 85% drop in manual verification cycle)*.
  * Projected cost reduction *(e.g. ₹12,000 deployment cost vs ₹1.5L existing systems)*.
* **National Scalability Blueprint**:
  * How the solution scales from 1 pilot district to all 700+ districts across India.
* **Commercial Economic Rebuttal**:
  * Cite the mathematical OpEx savings vs commercial enterprise SaaS (SAP / Salesforce) from [Competitive Matrix Template](../competitive_matrix_template.md).

---

### 🔬 Slide 6: Research, Citations & Team Competence
* **Academic Research & Prior Art**:
  * 3–4 IEEE / Springer / Government Whitepaper citations backing your chosen methodology.
  * Official dataset citations (e.g. *data.gov.in, Kaggle, CPCB bulletins*).
* **Team Competence & Role Division**:
  * Explicit role mapping: *Systems Architect, Backend Lead, ML Specialist, Frontend/A11y Lead, Security Lead, Testing Lead*.
* **Preliminary Work Done**:
  * Mention if initial datasets are curated, baseline models benchmarked, or starter repo initialized.

---

## ✅ Pre-Upload Submission Checklist

- [ ] **Slide Count**: Exactly 6 slides (No Slide 7 or appendix).
- [ ] **Format & Size**: Exported as `.pdf` under **10 MB**.
- [ ] **Diagram Clarity**: Architecture diagram text is crisp and readable on a 1080p screen.
- [ ] **Team Eligibility**: Exactly 6 student members from the same college, with $\ge 1$ female member.
- [ ] **PS ID Accuracy**: Problem statement ID exactly matches the SIH portal.
