# The SIH Idea Analysis Engine & Evaluation Framework

[🏠 Home](../README.md) > [📁 Intelligence Layer](./README.md) > **Idea Evaluation Framework**

> **Purpose**: An actionable, 13-dimensional evaluation engine designed to rigorously score, stress-test, and refine new SIH solution proposals before code is written or the 6-slide idea deck is submitted.

---

## 🎯 1. The 13 Evaluation Dimensions

To avoid fake mathematical precision, each dimension is evaluated on a clear qualitative scale from **1 (Severe Deficit)** to **5 (Exceptional / Production-Ready)**.

```mermaid
radar-chart
    title SIH Idea Viability Profile (13 Dimensions)
    "Problem Impact" : 5
    "Novelty" : 4
    "Feasibility" : 5
    "Gov Fit" : 5
    "Scalability" : 4
    "Deployment Realism" : 4
    "Data Availability" : 5
    "Demoability" : 5
    "Cost & OpEx" : 5
    "Accessibility" : 4
    "Offline Resilience" : 5
    "Competitive Differentiation" : 4
    "Jury Defensibility" : 5
```

---

### Dimension Breakdown & Rubric Guidelines

| # | Dimension | 🔍 What is Evaluated | 1 Point (Reject / Deficit) | 3 Points (Average / Fragile) | 5 Points (Winning Standard) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Problem Impact** | Real-world severity and breadth of citizen/ministry bottleneck. | Trivial inconvenience or theoretical problem. | Noticeable issue affecting a small user niche. | Chronic national bottleneck affecting millions of citizens or ₹100Cr+ in public funds. |
| **2** | **Novelty** | Concrete technical or architectural USP over existing approaches. | Direct clone of standard commercial SaaS or textbook tutorial. | Minor feature addition on top of open-source boilerplate. | Novel algorithmic, edge, or hardware combination solving previously intractable bottlenecks. |
| **3** | **Technical Feasibility** | Deliverability of a working proof-of-concept within a 36-hour sprint. | Requires unreleased AGI models or impossible sensor physics. | Complex multi-system dependencies with high risk of sprint bugs. | Solid, proven open-source foundation models and modular APIs achievable in 36 hours. |
| **4** | **Gov / Stakeholder Fit** | Direct alignment with ministry workflow and Indian statutory acts. | Solves a corporate use-case ignoring public department structure. | Fits ministry goals but requires radical restructuring of department operations. | Plugs seamlessly into existing NIC/department workflows, DPDP Act 2023, and IT Act norms. |
| **5** | **Scalability** | Architecture behavior under 10x to 100x user/data volume surges. | Monolith crashing under concurrent requests; unbounded memory leaks. | Cloud-dependent scaling requiring linearly increasing cloud compute budgets. | Stateless microservices, edge offloading, database partitioning, and low-cost event queues. |
| **6** | **Deployment Realism** | Practicality of physical/cloud rollout in Indian public infrastructure. | Requires $10,000 servers in every remote village outpost. | Works in urban offices but fails under rural power/hardware constraints. | Runs on legacy PCs, sub-₹10,000 phones, or low-cost ESP32/mini-PC edge hardware. |
| **7** | **Data Availability** | Existence of authentic training/testing datasets to seed the demo. | Zero accessible data; requires months of field data gathering. | Small synthetic or generic Western dataset (e.g. US traffic data). | Verified open Indian datasets (`data.gov.in`, Kaggle India, CPCB, ISRO Bhuvan) ready to seed. |
| **8** | **Demoability** | Visual clarity, interactive impact, and speed of live demonstration. | Command-line script with slow, invisible background processing. | Web dashboard requiring 5 minutes of complex manual setup. | Visually stunning, instantaneous 90-second live user flow with clear before/after outputs. |
| **9** | **Cost & OpEx Viability** | Recurring operational expenditure per transaction. | Costly per-API pricing ($0.05/call) creating fiscal deficits. | Moderate cloud hosting costs viable only with venture funding. | Quantized edge computing delivering near-zero recurring OpEx (<₹0.05 per transaction). |
| **10** | **Accessibility & Inclusion** | Usability for non-English literate citizens and persons with disabilities. | Dense English developer dashboard with small tap targets. | Basic web localization in Hindi with standard keyboard navigation. | Full voice-first Bhashini multi-dialect interaction and WCAG 2.1 AA compliant UI. |
| **11** | **Offline Resilience** | System operability during zero-connectivity or network blackout. | Total crash or blank screen without active high-speed broadband. | Read-only cache without local write persistence or conflict resolution. | Full offline read/write capability via local SQLite with automated background sync. |
| **12** | **Competitive Differentiation** | Clear, mathematical rebuttal to *"Why not Google Forms / SAP / ERP?"* | Inability to articulate why existing commercial SaaS fails. | Generic "our solution is cheaper" argument without technical proof. | Clear 3-pillar proof showing commercial tools fail on cost, offline resilience, and DPDP privacy. |
| **13** | **Jury Defensibility** | Ability to defend code depth, algorithms, and tradeoffs under grilling. | Defensive arguments without data or mathematical justification. | Able to answer basic questions but stumbles on concurrency or edge cases. | Calm, data-backed defense citing benchmarks, IEEE papers, and architectural tradeoffs. |

---

## 📈 2. Scoring Methodology & Decision Gates

$$\text{Total Viability Score} = \sum_{i=1}^{13} \text{Dimension Score}_i \quad (\text{Max: } 65 \text{ Points})$$

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           VIABILITY DECISION GATES                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 🟢 SCORE ≥ 52 / 65 (≥ 80%) : GREEN LIGHT — HIGH VIABILITY                       │
│    • Solution is robust, defensible, and ready for PPT proposal submission.     │
│                                                                                 │
│ 🟡 SCORE 40 – 51 / 65 (60–79%) : AMBER LIGHT — CONDITIONAL PIVOT                │
│    • Identified critical vulnerabilities (e.g. offline sync or cost defense).   │
│    • Must patch low-scoring dimensions before finalizing submission.            │
│                                                                                 │
│ 🔴 SCORE < 40 / 65 (< 60%) : RED LIGHT — DISCARD / PIVOT                        │
│    • High probability of jury rejection or sprint execution failure.           │
│    • Recommend selecting an alternative Problem Statement.                      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 3. Actionable Idea Evaluation Worksheet Template

Copy and fill this markdown table for any prospective SIH 2026 idea:

```markdown
### 📋 SIH Idea Viability Assessment
* **Problem Statement ID**: [e.g. SIH2026-001]
* **Idea Name / Concept**: [Concept Title]
* **Evaluator Name**: [Team Lead / Mentor]
* **Evaluation Date**: YYYY-MM-DD

| # | Dimension | Score (1-5) | Identified Vulnerability / Justification | Required Engineering Patch |
| :-: | :--- | :---: | :--- | :--- |
| 1 | Problem Impact | [ ] | | |
| 2 | Novelty | [ ] | | |
| 3 | Technical Feasibility | [ ] | | |
| 4 | Gov / Stakeholder Fit | [ ] | | |
| 5 | Scalability | [ ] | | |
| 6 | Deployment Realism | [ ] | | |
| 7 | Data Availability | [ ] | | |
| 8 | Demoability | [ ] | | |
| 9 | Cost & OpEx Viability | [ ] | | |
| 10 | Accessibility & Inclusion | [ ] | | |
| 11 | Offline Resilience | [ ] | | |
| 12 | Competitive Differentiation | [ ] | | |
| 13 | Jury Defensibility | [ ] | | |
| **TOTAL** | **VIABILITY SCORE** | **[ / 65]** | **GATE: [GREEN / AMBER / RED]** | |
```
