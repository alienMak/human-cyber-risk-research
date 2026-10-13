# Research source and cross-reference audit

**Audit initiated:** 13 October 2026. **Status:** Partial, not repository-wide certified. This is an honest record of checks and unresolved verification, not a blanket assurance that every source is correct.

## Scope checked

Reviewed the current repository's root README, writing/evidence standard, scoping-review protocol, quality-appraisal rubric, evidence-matrix excerpt, historical timeline, trust-mechanisms atlas, podcast cross-references and publication boundaries. Confirmed that the scoping review covers **2016–2026**, while the historical timeline may legitimately include earlier material. The two scopes must not be conflated.

## Findings requiring attention

| ID | Finding | Severity | Follow-up |
| --- | --- | --- | --- |
| AUD-01 | Podcast episode discovery notes are explicitly SHOW-NOTES-ONLY; topical links are not transcript-level corroboration | Medium | Review original recordings/transcripts before attributing particular claims to speakers |
| AUD-02 | Existing evidence matrix contains many abstract-only entries | High for definitive synthesis | Prioritize full-text extraction, methods, sample, outcomes and uncertainty |
| AUD-03 | Historical timeline has sparse coverage before 2019, with one 1969 anchor | Medium | Add dated primary archival records for early AI, networking, online identity and the web |
| AUD-04 | The 2023 email verification study is formative usability research, not a deployed fraud-prevention trial | Medium | Preserve the study-design qualifier in all synthesis |
| AUD-05 | Podcast-to-paper comparisons are analogies or topical links, not demonstrated agreement | Medium | Keep relationship labels conservative |
| AUD-06 | No complete automated crawl of all external links, DOI resolution or publisher metadata was performed in this pass | Open | Run a separate systematic URL/metadata audit; do not claim every link verified |
| AUD-07 | Root README previously foregrounded the 2016–2026 scoping review and synthetic experiments, with little navigation to the new historical research lanes | Low | Add a clearly scoped navigation section |

## Claim provenance rules

For a substantive statement record: claim text, original publisher or archival URL, publication date, access level (record/abstract/full text), location in source if checked, research design and population where applicable, outcome, limitations, and date checked. Distinguish original research from NIST guidance, archival history, incident reports, podcasts and preprints.

**Verification levels:** URL listed; publisher record inspected; abstract examined; full text appraised; independently corroborated. Do not upgrade a level because a secondary source cites it.

## Reading priorities

1. [Zheng & Becker, 2022](https://www.usenix.org/conference/soups2022/presentation/zheng): experiment and actual outcomes.
2. [Zheng & Becker, 2023](https://www.usenix.org/conference/soups2023/presentation/zheng): usability setting, participants and what was not measured.
3. [Steves et al., 2020](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final): original Phish Scale development and limitations.
4. [Reinheimer et al., 2020](https://www.usenix.org/conference/soups2020/presentation/reinheimer): training timing, comparison and outcome.
5. [2025 IEEE S&P training study](https://doi.org/10.1109/SP61157.2025.00076): assignment, effect estimates and transfer.

The next audit must check every internal Markdown link and each external citation, rather than infer their validity from file existence. No participant data, unpublished algorithms or confidential employer materials were examined or published here.
