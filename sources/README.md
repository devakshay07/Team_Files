# SIH Intelligence Vault — Source Registry & Provenance Standard

This directory serves as the centralized, immutable registry of all sources, official government gazettes, institutional press releases, peer-reviewed publications, and verified public repositories referenced throughout the SIH Intelligence Vault.

---

## 🎯 Provenance & Evidence Standard

To ensure maximum credibility and prevent the propagation of unverified claims, all factual assertions in this vault are governed by a 4-tier taxonomy:

### 1. Epistemic Classification

| Tier Tag | Classification | Definition & Evidentiary Standard | Example |
| :--- | :--- | :--- | :--- |
| `[OFFICIAL FACT]` | Official Primary Record | Verified directly from Ministry Innovation Cell (MIC), AICTE, PIB India, or official SIH portal documentation. | SIH 2026 prize money is ₹1,50,000 per Problem Statement. |
| `[VERIFIED SECONDARY EVIDENCE]` | Verified Public Artifact | Verified from public source code repositories, institutional press releases, or accredited news reporting with direct attribution. | Team Legal Ledger utilized Polygon L2 and IPFS for evidence custody (GitHub: `kunalkeshan/eVault-SIH-2023`). |
| `[RESEARCH INFERENCE]` | Deductive Analysis | Architectural deductions, statistical patterns, or domain generalizations synthesized from cross-edition project analysis. | "Winning teams typically choose offline-first SQLite over cloud-only databases due to venue Wi-Fi contention." |
| `[STRATEGIC RECOMMENDATION]` | Actionable Guidance | Operational advice, pitching heuristics, or tactical suggestions for prospective teams. | "Enforce an absolute code freeze at Hour 28 of the 36-hour sprint." |

---

## 🔍 Confidence Scoring Model

Every case study, architecture teardown, and rule summary is tagged with an explicit confidence level:

* **`HIGH`**: Corroborated by official government documentation (PIB / AICTE / SIH Portal) or direct public source code repository.
* **`MEDIUM`**: Corroborated by reputable institutional announcements, accredited press articles (The Hindu, Times of India), or verified finalist testimonials without full source code release.
* **`LOW`**: Anecdotal report, historical oral archive, or inferred architecture where full repository or official gazette is not publicly accessible. Marked explicitly as `Unverified / Community Reported`.

---

## 📁 Registry Structure

* **[`official_sources.md`](./official_sources.md)**: Government ministries, AICTE, MIC, PIB releases, National Acts (DPDP Act 2023, IT Act), and official SIH guidelines.
* **[`historical_sources.md`](./historical_sources.md)**: Verified winning team repositories (2017–2025), institutional announcements, and nodal center archives.

---

## 🏷️ Citation Schema

When citing a source within any case study or intelligence document, use the standardized source identifier format:

```markdown
- **Source ID**: `SRC-OFF-XXX` (for official sources) or `SRC-HIST-XXX` (for historical sources)
- **Source Type**: Official Government / Verified Repo / Institutional Announcement / Press Report
- **Confidence**: HIGH / MEDIUM / LOW
- **Last Verified**: YYYY-MM-DD
```
