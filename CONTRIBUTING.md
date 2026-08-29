# Contributing to the SIH Intelligence Vault

[🏠 Home](./README.md) > **Contributing Guidelines**

Thank you for contributing to the SIH Intelligence Vault! 🇮🇳

This project is governed by strict evidence and provenance standards. Our mission is to maintain a trusted, high-credibility intelligence database for the Indian student developer ecosystem.

---

## 🎯 Epistemic Classification Requirement

Every contribution (Pull Request, Issue, or Case Study edit) must explicitly classify assertions into one of four categories:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MANDATORY CONTRIBUTION TAGS                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│ [FACT]           Verified by an official government or institutional source.    │
│ [SOURCE]         A traceable citation with a valid link and verification date.  │
│ [INFERENCE]      An architectural deduction or pattern analysis from data.      │
│ [RECOMMENDATION] Actionable tactical or operational advice for student teams.   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

> [!CAUTION]
> **Zero Fabrication Policy**: Never invent winning teams, prize amounts, technology stacks, or source URLs. If a detail cannot be verified, write `"Information not publicly archived"` or `"Unverified / Community Reported"`.

---

## 📝 How to Contribute

### 1. Adding or Updating a Case Study
- Add or update files in `case_studies/`.
- Ensure all 14 sections of the standard schema are completed:
  1. `# Project [Name] — [Short Description]`
  2. `## Problem Statement`
  3. `## Institution / Team`
  4. `## Edition`
  5. `## Official Problem Statement`
  6. `## Solution`
  7. `## Architecture` (Mermaid diagram)
  8. `## Technology Stack`
  9. `## Deployment / Hardware`
  10. `## Why It Won` (Distinguishing facts from inferences)
  11. `## Evidence` (Structured table)
  12. `## Sources` (Linked to `sources/`)
  13. `## Confidence` (HIGH / MEDIUM / LOW)
  14. `## Reusable Pattern`
  15. `## SIH 2026 Relevance`

### 2. Adding a Source to the Registry
- Add an entry to [`sources/official_sources.md`](./sources/official_sources.md) (for government / AICTE sources) or [`sources/historical_sources.md`](./sources/historical_sources.md) (for team repositories / press releases).
- Follow the source schema:
  - **Source ID**: `SRC-OFF-XXX` or `SRC-HIST-XXX`
  - **Title**: Document / Repository Title
  - **Publisher / Organization**: Authority
  - **URL / Document Reference**: Active link or file reference
  - **Publication Date**: `YYYY-MM-DD` (if available)
  - **Relevant Claims**: Bulleted list of verified facts
  - **Verification Date**: `YYYY-MM-DD`
  - **Reliability Tier**: Tier 1 (Official Govt) / Tier 2 (Institutional / Verified Repo) / Tier 3 (Reputable Press)
  - **Confidence**: HIGH / MEDIUM / LOW

### 3. Reporting Corrections or Stale Information
- Open an Issue titled `[CORRECTION] <File Name>: <Summary of Correction>`.
- Provide the conflicting claim, the corrective fact, and the supporting primary source URL.

---

## 📋 Pull Request Submission Template

When submitting a PR, include this checklist in your PR description:

```markdown
### Summary of Changes
- [Brief description of changes]

### Evidence & Provenance
- [ ] Every factual claim is tagged with `[FACT]` and accompanied by a `[SOURCE]`.
- [ ] Source entry added to `sources/official_sources.md` or `sources/historical_sources.md`.
- [ ] Inferences and strategic recommendations are clearly labeled (`[INFERENCE]`, `[RECOMMENDATION]`).
- [ ] No marketing hyperbole or unsupported claims.
- [ ] Passed local validation (`python3 scripts/validate_vault.py`).
```

---

## 🤖 Automated Validation

Before committing, verify all internal links, schema compliance, and source cross-references:

```bash
python3 scripts/validate_vault.py
```
