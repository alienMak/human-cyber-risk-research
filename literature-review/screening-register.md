# Search and screening register

This is the audit trail for expanding the 2016–2026 review. It starts now, not retroactively. Earlier matrix entries were selected through exploratory searching, so no historical number of records screened, excluded, or deduplicated is claimed.

## Screening log

| Search date | Source/platform | Query or navigation route | Year filter | Records returned | Records screened | Included | Excluded | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-10 | NIST | Original Phish Scale paper, supporting NIST publications | 2016–2026 | Not systematically enumerated | Selected records | Selected records in evidence matrix | Not recorded | Exploratory publisher-record verification |
| 2026-10-10 | USENIX SOUPS | Source papers and proceedings on phishing detection, reporting, accessibility and interventions | 2016–2026 | Not systematically enumerated | Selected records | Selected records in evidence matrix | Not recorded | Exploratory publisher-record verification |

| 2026-10-23 | Publisher/institutional records: SAGE, Macquarie/Adelaide, PubMed; USENIX/NIST cross-check | Targeted titles/DOIs: “The roles of phishing knowledge, cue utilization, and decision styles in phishing email detection”; “Like Shooting Phish in a Barrel”; “Quantifying Phishing Susceptibility for Detection and Behavior Decisions”; plus phishing false-alarm / signal-detection searches | 2016–2026 | Not systematically enumerable in ranked web results | 5 named primary records checked | 3 newly indexed canonical papers | 2 already indexed (Zheng & Becker 2022; Steves et al. 2020), **DUPLICATE** | Sturman 2024 and Morrison 2025-issue **FULL TEXT**; Canfield 2016 **ABSTRACT-ONLY**. Separate Canfield 2017 replication already covered. No PRISMA count or exhaustive-search claim. |

| 2026-10-24 | NIST/Oxford original journal PDF; USEC 2019 original PDF; NIST M3AAWG 2021 record; IEEE S&P 2025 publisher abstract; arXiv 2025 record | Targeted: Phish Scale difficulty, click-rate calibration, workplace context, validation, longitudinal training | 2016–2026 | Ranked web results not exhaustively enumerable | 5 named source records | 1 existing 2020 matrix entry upgraded to full-text; 2019 predecessor checked for overlap | No new independent matrix entry | 2019/2020 share exercises; 2021 guidance is not a new validation study; 2025 IEEE already indexed, abstract-only here; 2025 arXiv preprint already indexed, abstract-only here. [Full appraisal](../literature-watch/2026-10-24-phishing-difficulty-and-click-rate-interpretation.md). |

| 2026-10-26 | USENIX SOUPS original paper and PDF; NDSS USEC original paper and PDF; IEEE S&P publisher abstract; institutional DOI cross-check | Targeted: phishing training retention, reminder timing, repeated stimuli, classification versus field behavior | 2016–2026 | Ranked search denominator not systematically enumerable | 3 named primary papers, plus institutional identity checks | Reinheimer 2020 existing row upgraded; Berens 2022 new row; Ho 2025 context only | No paper excluded as duplicate; Reinheimer already indexed | Reinheimer and Berens **FULL TEXT**; Ho **ABSTRACT-ONLY**; no news/podcast/preprint evidence |

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

### Targeted screening decisions, 24 October 2026

- **UPGRADE, FULL TEXT:** [Steves, Greene & Theofanos (2020)](https://doi.org/10.1093/cybsec/tyaa009), *Journal of Cybersecurity*. Original 16-page NIST-hosted journal PDF and tables appraised. Existing evidence-matrix row updated, not counted as a newly discovered publication. Table 13 denominator discrepancy preserved without correction.
- **VERSION RELATION, FULL TEXT CHECKED:** [Steves et al. (USEC 2019)](https://doi.org/10.14722/usec.2019.23028), seven earlier exercises. The 2020 journal paper extends this research; the two records are not independent replications.
- **CONTEXT, RECORD/ABSTRACT ONLY:** [Dawkins et al. (M3AAWG 2021)](https://www.nist.gov/publications/nist-phish-scale-method-rating-human-phishing-detection-difficulty), practitioner guidance, not independent outcome validation.
- **ALREADY INDEXED, ABSTRACT-ONLY FOR THIS RUN:** [Ho et al. (IEEE S&P 2025)](https://doi.org/10.1109/SP61157.2025.00076), peer-reviewed field experiment; [Rozema & Davis (arXiv 2025)](https://arxiv.org/abs/2506.19899), **preprint**. Neither is treated as full-text appraised here.
- **Other source types:** No news or podcasts included. Searches were targeted rather than exhaustive, so no PRISMA screening denominator is claimed.

### Targeted screening decisions, 26 October 2026

- **UPGRADE, FULL TEXT:** [Reinheimer et al. (SOUPS 2020)](https://doi.org/10.5555/3488905.3488920), original USENIX PDF, §§3–7 and Figures 1, 3–5. Previously indexed at abstract level; not counted as a newly found study. The evaluation concerns 20-item email classification, not observed inbox behavior.
- **INCLUDE, FULL TEXT:** [Berens et al. (USEC 2022)](https://doi.org/10.14722/usec.2022.23075), original NDSS-hosted paper, §§IV–VI, Tables I–II. Distinct university follow-on using related training content, with 16 participants linked across the three tests; not an independent validation of actual inbox behavior.
- **CONTEXT, ABSTRACT-ONLY:** [Ho et al. (IEEE S&P 2025)](https://doi.org/10.1109/SP61157.2025.00076). Already indexed; publisher abstract rechecked for the difference between classification retention and operational campaign outcomes. No new full-text claims.
- **Deduplication:** Reinheimer 2020 and Ho 2025 were already in the matrix. Berens 2022 was not found by title/author in the matrix or this register before addition. Institutional DOI record corroborated Reinheimer's bibliographic identity.
- **Source types:** Two peer-reviewed full-text papers; one peer-reviewed abstract-only comparator. No preprints, news or podcasts incorporated. Search was targeted, not an exhaustive database sweep; no PRISMA denominator is inferred. See [full appraisal](../literature-watch/2026-10-26-training-retention-versus-behavior.md).

### Targeted screening decisions, 27 October 2026

**Search date and routes:** 2026-10-27. IEEE Xplore DOI/publisher record; two author-hosted original PDFs; USENIX/IEEE-focused search; PubMed and Oxford/JAMIA original records; arXiv record. Targeted queries included “Understanding the Efficacy of Phishing Training in Practice PDF”, “phishing training longitudinal field experiment retention click rate 2024 2025”, and “Evaluation of a mandatory phishing training program for high-risk employees DOI”. Year filter: 2016–2026. Ranked search result counts were not exhaustively available; **three named primary records** were checked for this focused comparison, not a systematic database screening denominator.

- **UPGRADE EXISTING ENTRY, FULL TEXT:** [Ho et al. (IEEE S&P 2025)](https://doi.org/10.1109/SP61157.2025.00076), [author-hosted original 18-page PDF](https://www.sysnet.ucsd.edu/~voelker/pubs/phishtrain-oakland25.pdf). §§3–7, Tables 1–5 and Figures 2–4 appraised. Earlier [partial appraisal](full-text-appraisals/ho-et-al-2025.md) expanded in place; this is not a newly found or independent study. The annual-training recency analysis is observational; embedded training assignment is randomized. Click outcome only; reporting and actual compromise not observed. The author PDF was not byte-compared with IEEE's PDF.
- **CONTEXT ONLY, ABSTRACT-ONLY:** [Gordon et al. (JAMIA 2019)](https://doi.org/10.1093/jamia/ocz005), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/30861069/). Distinct older healthcare study of mandatory training for repeat clickers; not pooled with Ho's randomized estimate or represented as full-text appraised.
- **ALREADY INDEXED, PREPRINT, ABSTRACT-ONLY FOR THIS RUN:** [Rozema & Davis (2025)](https://arxiv.org/abs/2506.19899). Preprint remains outside peer-reviewed corroboration; no new full-text appraisal claimed.
- **Deduplication:** The Ho title/DOI already appeared in the evidence matrix, prior 26 October note, 13 October partial appraisal and priority list. Its existing appraisal was updated rather than creating a second file. Gordon and Rozema were consulted only as separate-context records.
- **Other source types:** No news articles or podcasts were used as scholarly evidence. No PRISMA flow or exhaustive screening count is claimed. [Full-text appraisal](full-text-appraisals/ho-et-al-2025.md).


### Targeted screening decisions, 28 October 2026

**Search date:** 2026-10-28. **Routes:** Cambridge Core publisher record and 13-page original PDF; USENIX SOUPS 2026 proceedings; ACM CHI 2026 original record; University of Twente original institutional record; Elsevier article records; prior IEEE S&P appraisal. **Queries included:** “phishing feedback just-in-time intervention improves online security full text”, “SOUPS 2026 emotional behavioral phishing workplace reputational risk”, “organizational norms susceptibility phishing field experiment”, and “2017 priming warnings social engineering DOI”. Year scope: 2016–2026; an earlier study was considered only for historical context. Ranked search results do not yield an auditable raw denominator. **Seven named publication records** were checked for this focused comparison; one new full-text appraisal was added.

- **INCLUDE, FULL TEXT:** [Bender, Horn, Loewenstein & Roberts](https://doi.org/10.1017/bpp.2024.19), *Phishing feedback: just-in-time intervention improves online security*. **First online 2024-09-11; assigned to July 2026 issue**. Cambridge publisher PDF, *Methods, Results, Conclusion*, pp. 532–537 and Table 1 appraised. **One canonical paper**, not two. New [appraisal](../literature-watch/2026-10-28-feedback-timing-and-behavioral-outcomes.md) and evidence-matrix entry.
- **ALREADY INDEXED, PREVIOUSLY FULL TEXT APPRAISED:** [Ho et al. (2025)](https://doi.org/10.1109/SP61157.2025.00076), different randomized embedded-training intervention and population; no new independent appraisal or duplicate row.
- **CONTEXT, ABSTRACT/RECORD ONLY:** [Junger, Montoya & Overink (2017)](https://doi.org/10.1016/j.chb.2016.09.012), older warnings/priming field study; [Petrič & Roer (2022)](https://doi.org/10.1016/j.tele.2021.101766), organizational norms and phishing; [Schiller et al. (CHI 2026)](https://doi.org/10.1145/3772318.3791490), support-system classification; [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas), emotions and workplace phishing; [Madeira & Alves (2026)](https://doi.org/10.1016/j.ijhcs.2026.103861), feedback and training participation. No methods, sample or effect-size extraction beyond verified publisher abstracts for these contextual records; no new matrix row.
- **Limits and deduplication:** Bender was absent by DOI/title in the existing matrix/register. Its three waves belong to **one study**, with overlapping individuals deduplicated by the authors. Timing was **not** experimentally compared head-to-head; the baseline response groups and feedback content differed. First wave preregistration was not fully implemented for baseline reporters. The supplementary appendix was not appraised.
- **Other source types:** No preprints, news or podcasts were incorporated as empirical evidence. This is targeted screening, not a PRISMA flow or exhaustive search.

### Targeted screening decisions, 29 October 2026

**Date/routes:** 2026-10-29. USENIX SOUPS 2023 publisher page and original 21-page PDF; SOUPS 2022 publisher/UCL publication record; Wiley *Information Systems Journal* publisher article/DOI and abstract; existing Cambridge/Bender full-text appraisal used for comparison. **Queries:** “phishing reporting feedback study user reporting experiments”; “Checking nudging or scoring Zheng Becker 2023 PDF”; “crowdsourced phishing warning system Nguyen 2021 DOI”; “presenting suspicious details email headers Zheng Becker 2022”. **Scope:** 2016–2026. Ranked web search did not expose an auditable raw result denominator; **three named canonical records were screened** for the present update, with one already appraised distinct comparator consulted. No PRISMA or comprehensive-screening total is claimed.

- **UPGRADE EXISTING, FULL TEXT:** [Zheng and Becker, *Checking, nudging or scoring?* (SOUPS 2023)](https://www.usenix.org/system/files/soups2023-zheng.pdf), §§3.1–3.4, 4.1–4.2, 5.1–5.4 and Table 1. Already indexed in the secondary matrix and priority list. N=27; formative simulated-inbox evaluation, not a randomized quantitative efficacy trial. Baseline inbox always first; tool order randomized afterward; four successive design iterations. **No measured real reporting rate or statistical detection effect.** [New appraisal](../literature-watch/2026-10-29-verification-cues-and-workflow-friction.md).
- **INCLUDE, ABSTRACT-ONLY:** [Nguyen, Jensen, Durcikova and Wright (2021)](https://doi.org/10.1111/isj.12318), peer-reviewed *Information Systems Journal* 31(3), 473–513, first online 11 March 2021. Publisher abstract: 438 participants, mock crowdsourced warning features and email judgments. The full article was not reliably retrievable for independent methods/effect-size appraisal. New matrix row is **ABSTRACT-ONLY**, not an observed workplace-reporting result.
- **ALREADY INDEXED, DISTINCT STUDY, ABSTRACT-ONLY FOR THIS RUN:** [Zheng and Becker (SOUPS 2022)](https://www.usenix.org/conference/soups2022/presentation/zheng), header-only detection experiment. It is not a second wave or replication of the 2023 formative evaluation.
- **EXISTING COMPARATOR, NO NEW APPRAISAL:** [Bender et al. (first online 2024; 2026 issue)](https://doi.org/10.1017/bpp.2024.19), randomized feedback field study, previously fully appraised 28 October. Different intervention and endpoints; no pooling.
- **Other source types:** No preprints, news or podcasts entered this update's empirical synthesis. The current source record for the 2023 SOUPS paper supplies a stable USENIX URL and proceedings pages 57–76, but no DOI in the publisher's citation.

**Methodological caution:** The 2023 paper's seven-minute inbox limit, think-aloud protocol, researcher prompts, sequential cohorts and always-first baseline limit causal interpretation. Preference counts and qualitative behavior should not be converted into phishing-detection effect sizes.
