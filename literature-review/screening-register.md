# Search and screening register

This is the audit trail for expanding the 2016–2026 review. It starts now, not retroactively. Earlier matrix entries were selected through exploratory searching, so no historical number of records screened, excluded, or deduplicated is claimed.

## Screening log

| Search date | Source/platform | Query or navigation route | Year filter | Records returned | Records screened | Included | Excluded | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-10 | NIST | Original Phish Scale paper, supporting NIST publications | 2016–2026 | Not systematically enumerated | Selected records | Selected records in evidence matrix | Not recorded | Exploratory publisher-record verification |
| 2026-10-10 | USENIX SOUPS | Source papers and proceedings on phishing detection, reporting, accessibility and interventions | 2016–2026 | Not systematically enumerated | Selected records | Selected records in evidence matrix | Not recorded | Exploratory publisher-record verification |

| 2026-10-23 | Publisher/institutional records: SAGE, Macquarie/Adelaide, PubMed; USENIX/NIST cross-check | Targeted titles/DOIs: “The roles of phishing knowledge, cue utilization, and decision styles in phishing email detection”; “Like Shooting Phish in a Barrel”; “Quantifying Phishing Susceptibility for Detection and Behavior Decisions”; plus phishing false-alarm / signal-detection searches | 2016–2026 | Not systematically enumerable in ranked web results | 5 named primary records checked | 3 newly indexed canonical papers | 2 already indexed (Zheng & Becker 2022; Steves et al. 2020), **DUPLICATE** | Sturman 2024 and Morrison 2025-issue **FULL TEXT**; Canfield 2016 **ABSTRACT-ONLY**. Separate Canfield 2017 replication already covered. No PRISMA count or exhaustive-search claim. |

## New search checklist

For a future database search, record:
1. Date, database, exact query and filter.
2. Raw result count before deduplication.
3. Canonical paper title, author, year, URL and DOI where available.
4. Inclusion decision and a short exclusion reason.
5. Whether the abstract or entire paper was assessed.
6. Whether the record duplicates an existing publication, thesis, workshop paper or preprint.
7. When the study entered the matrix and synthesis.

## Exclusion reason codes

- **OUT-SCOPE:** No human security-decision or behavioral outcome relevant to the question.
- **OUT-DATE:** Outside the chosen 2016–2026 publication window.
- **DUPLICATE:** Same research as an existing canonical record.
- **NON-PRIMARY:** News or commentary without a primary research contribution; may be kept in literature-watch instead.
- **UNVERIFIED:** Identity, publication status or evidence cannot be confirmed.
- **INSUFFICIENT:** Not enough accessible methodological detail for the claim being considered.

This register is not a PRISMA flow diagram. That would require complete tracked search and screening counts.

### Targeted screening decisions, 23 October 2026

- **INCLUDE, FULL TEXT:** [Sturman et al. 2024](https://doi.org/10.1016/j.apergo.2024.104309), original published 11-page PDF reviewed; task, sampling, measured outcomes, regressions and limitations extracted.
- **INCLUDE, FULL TEXT:** [Morrison et al. 2025 issue, first online 2024-10-27](https://doi.org/10.1177/15553434241296170), original open publisher article reviewed; controlled versus later inbox simulation, outcomes and limitations extracted.
- **INCLUDE, ABSTRACT-ONLY:** [Canfield et al. 2016](https://doi.org/10.1177/0018720816665025), publisher abstract and PubMed record verified; original full-text methods and estimates not independently appraised. The 2017 replication is a **different study** already documented in the repository.
- **DUPLICATE, no new entry:** [Zheng & Becker 2022](https://www.usenix.org/conference/soups2022/presentation/zheng) and [Steves et al. 2020](https://doi.org/10.1093/cybsec/tyaa009) are already in the evidence matrix. Their records were consulted for context, not newly appraised.
- **Source types:** All included items are peer-reviewed journal papers. No preprints, news or podcasts entered the scholarly synthesis in this run.

Searches were targeted, not a reproducible database-wide enumeration; the raw ranked-result denominator is unavailable. The [detailed appraisal](../literature-watch/2026-10-23-classification-errors-and-reasonable-reporting.md) records the two full-text reviews and the abstract-only boundary.
