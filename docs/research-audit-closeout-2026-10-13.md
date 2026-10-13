# Research backlog: verification closeout and exceptions

**Date:** 13 October 2026. This document is a status ledger, **not a claim that all source verification has been completed**.

## Completed

- Root research navigation, conceptual definitions, evidence provenance rules, public historical source notes and two interpretive synthesis notes.
- Original-paper targeted appraisals for Zheng and Becker (2022 and 2023) and the NIST Phish Scale (2020).
- Partial methodological notes for Reinheimer et al. (2020) and the IEEE S&P 2025 training paper; these remain incomplete statistical appraisals.
- Two publisher transcript notes for Darknet Diaries episodes 143 and 144; **transcript-reviewed, audio not listened**.
- Official FBI advisory pattern note and a DOJ prosecution-record note; original court dockets not inspected.
- Targeted internal-link verification of 35 unique paths in four Markdown files.
- A reusable repository-wide Markdown link checker in scripts/audit_research_links.py and a weekly/manual GitHub Actions workflow in .github/workflows/research-link-audit.yml. **The new workflow's execution has not been observed or its artifacts reviewed.**

## Exceptions requiring source work

| Item | Status | What completion would require |
| --- | --- | --- |
| Entire-repository external link audit | OPEN | Execute the checker in GitHub Actions, inspect artifact, manually recheck anti-bot errors, correct broken citations |
| DOI metadata audit | PARTIAL | Compare every DOI with publisher or Crossref metadata, including authors, title, year and version |
| All podcast notes | PARTIAL | Publisher transcripts or audio for the remaining discovery episodes; do not imply listening |
| 2020 longitudinal and 2025 field-study statistics | PARTIAL | Detailed extraction of full methods, attrition, assignment, absolute outcomes and uncertainty |
| Named incident forensic chronology | PARTIAL | Underlying court filings, dated investigative records, and careful attribution of defendant versus victim actions |
| Historical 1990s–2010s identity technologies | PARTIAL | Dated primary standards and institutional archives with separate behavioral evidence |

## Scientific and confidentiality boundaries

Publisher records are not full-text appraisal. Transcript accounts are not independent verification of the events described. A law-enforcement press release is not a psychological experiment. Internal-link existence is not an external URL or DOI certification. Keep the 2016–2026 empirical scoping review distinct from earlier historical source notes. Do not publish proprietary product scoring, employer materials, private participant data or patent-sensitive implementation details.

**Conclusion:** The documentation and repeatable audit mechanism are in place. The exceptions above are not closed merely because they have a tracking document.
