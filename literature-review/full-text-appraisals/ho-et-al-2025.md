# Ho et al. (2025): what does conventional phishing training change in the workplace?

**Publication:** Grant Ho, Ariana Mirian, Elisa Luo, Khang Tong, Euyhyun Lee, Lin Liu, Christopher A. Longhurst, Christian Dameff, Stefan Savage and Geoffrey M. Voelker. *Understanding the Efficacy of Phishing Training in Practice*. IEEE Symposium on Security and Privacy 2025, pp. 37–54; conference 12–15 May 2025. [DOI/publisher](https://doi.org/10.1109/SP61157.2025.00076); [original author-hosted 18-page PDF](https://www.sysnet.ucsd.edu/~voelker/pubs/phishtrain-oakland25.pdf).  
**Review:** 27 October 2026. **PEER-REVIEWED; FULL TEXT APPRAISED** (author-hosted version, §§3–7, Tables 1–5 and Figures 2–4). This expands the partial appraisal recorded on 13 October; it is not a second independent study or a new publication. The IEEE publisher record independently confirms title, venue, DOI and conference date. The author PDF was not byte-compared with the publisher PDF.

## Design, sample and what was actually measured

The study analyzed eight months of workplace phishing exercises at UC San Diego Health, January–October 2023, with **19,789 active full-time employees** after account and activity exclusions. Employees included clinical and nonclinical roles. There were eight monthly campaign occasions and **ten distinct phishing email messages**, with one message per user per active month; assignment varied by randomized track. Some lures were repeated in one track, and the authors checked a model excluding the repeated occurrence. The main observed outcome was a **binary click on the link in a simulated email**. This was neither a credential-submission outcome nor a measure of recognition, reporting, verification or actual compromise (§§3, 3.2, pp. 4–6; Table 1, p. 6).

**Two different comparisons must not be conflated.** Annual awareness training was mandatory and assigned through existing HR processes. Its completion recency was *observed*, not randomized. The annual-training analysis compared the time since employees last completed it with subsequent simulated-link clicking, adjusting for lure, track, month, previous failures and repeated observations (§§3.1, 4.1–4.2, pp. 4, 7–8).

Embedded training, by contrast, used **random assignment** to five groups: a control receiving a generic 404 page after a click; generic static; generic interactive; contextual static; and contextual interactive training. Each group was divided into four randomized lure-order tracks, yielding twenty cohorts. Groups initially contained roughly 3,950 users and varied between about 3,700 and 3,950 as employment status changed. Only people who clicked encountered their assigned training page. The authors planned power to detect a 5-percentage-point difference and fitted generalized linear mixed-effects models with relevant covariates (§3.1, pp. 4–5).

Data cleaning excluded inactive and non-full-time accounts and corrected two months of incorrectly quarantined simulations in affected control cohorts. It also removed events attributable to Microsoft link crawlers. These are sensible precautions but create exclusions worth tracking when assessing denominators and comparability (§3.2, pp. 5–6).

## Results, with the relevant denominator and uncertainty

1. **Annual training recency:** The adjusted association between time since completion and simulation failure was not statistically significant: **OR 0.998 per 30-day increase, 95% CI 0.996–1.000, p=0.06** (§4.2, p. 8; Figure 3). This is not a randomized test of taking annual training versus no training, and p=0.06 does not prove equivalence or zero benefit.

2. **Randomized embedded-training assignment:** Across training arms versus the 404 control, the adjusted model gave **OR 0.905, 95% CI 0.863–0.950, p<0.001**, representing lower *odds* of a later simulated click. The paper reports an approximately **1.7-percentage-point** aggregate difference in observed failure rates (Table 2 and §5.2, p. 9). The statistically detectable effect was small relative to the variation among lures: Table 1 ranges from **1.82% to 30.80%** clicking. The control is not completely inert: a 404 page after a suspicious link might still prompt learning (§7, pp. 13–14).

3. **Training exposure and engagement:** Embedded training reached only employees who clicked. Across training sessions, **37–51%** of page visits registered zero seconds depending on training type, and **over 75%** lasted less than a minute. Overall session completion, operationalized as pressing an acknowledgment button, was **24.0%** (Tables 3–4; §6.1, pp. 10–11). Zero-second measurements may partly reflect blocked JavaScript; acknowledgment is not a demonstrated knowledge gain.

4. **Completion is not randomized:** Among those assigned interactive training, previously completing at least one session was associated with lower future clicking (**OR 0.809, 95% CI 0.730–0.896**). Completing more static sessions was associated with *higher* subsequent odds (**OR 1.185 per additional completed session, 95% CI 1.110–1.266**; Table 5, §6.2, p. 12). These are **observational comparisons conditional on exposure and self-selected engagement**, not causal evidence that static content makes employees less safe or that interactive completion necessarily caused improvement. Previous failures were adjusted for, but unmeasured differences in motivation and work context remain plausible.

5. **Repeated exposure:** **11,077 of 19,789 employees (56%)** clicked at least once during the eight occasions (§3.2, Figure 2, p. 6). This cumulative count is not a per-message failure rate or a probability of actual compromise.

## Eight-domain methodological appraisal

| Domain | Assessment | Evidence and unresolved issue |
| --- | --- | --- |
| Design | **Yes for embedded assignment; partial for annual training** | Five randomized embedded arms; annual recency observational (§§3.1, 4–5). |
| Sampling | **Partial** | 19,789 active full-time employees at one healthcare institution; no representative sample of all industries (§3.2). |
| Outcome definition | **Yes for clicks; no for broader security decisions** | Click on simulated link, training time and acknowledgment; no reporting, credential entry or incident prevention (§§3, 6–7). |
| Confounding | **Partial** | Adjusted for lure, month, track, previous failures, repeated users; annual-training recency and self-selected completion retain unmeasured confounding (§§4.2, 5.1, 6.2). |
| Measurement | **Partial** | Real workplace exposures and clear click endpoint; crawler/quarantine corrections; time-on-page and completion are imperfect proxies for learning (§§3.2, 6.1). |
| Analysis | **Yes with qualifications** | Mixed-effects models, ORs/CIs and a priori power calculation; small effects need practical interpretation; engagement subgroup not randomized (§§3.1, 5.2, 6.2). |
| Generalization | **Partial** | One health system, ten email lures, one organizational security context; no evidence here for other attack vectors (§7). |
| Ethics and reproducibility | **Partial** | Institutional approvals, anonymized analysis, no employment consequences; analysis code reported available, individual-level data not public (§§3.1, 3.3). |

## Cross-study context without double-counting

[Gordon et al. (2019), *Journal of the American Medical Informatics Association*](https://doi.org/10.1093/jamia/ocz005) is a **distinct peer-reviewed observational healthcare study**, screened at **ABSTRACT-ONLY** level for this checkpoint. Its publisher abstract describes 5,416 employees present across twenty campaigns and no substantial improvement attributable to additional mandatory training targeted at repeat clickers. It did not use the same randomized comparison as Ho et al.; it should not be treated as replication of Ho's effect estimate.

[Reinheimer et al. (SOUPS 2020)](https://www.usenix.org/conference/soups2020/presentation/reinheimer) and [Berens et al. (USEC 2022)](https://doi.org/10.14722/usec.2022.23075) have already been appraised in full in this repository. They assessed classification of email screenshots, not workplace clicks. [Rozema & Davis (2025)](https://arxiv.org/abs/2506.19899) remains a **PREPRINT, ABSTRACT-ONLY** comparator here; it is not counted as peer-reviewed corroboration. No news or podcasts contributed evidence to this appraisal.

## What the evidence supports and what remains open

**Authors' finding:** Conventional embedded training reduced simulated clicks modestly on average in this randomized workplace comparison; recent annual-training completion did not predict lower clicking in the observational recency analysis. Most exposed users engaged little with training content.

**Analysis:** A large sample can identify a statistically reliable but operationally small change. Training assignment, training exposure, training acknowledgment and later behavior are different events. The variation in lure difficulty was much larger than the average training-group difference, and the annual and completion analyses do not share the causal protection of randomized assignment.

**Proposed future tests, not conducted:** (1) Compare a delayed behavioral outcome across matched but unfamiliar messages, with an explicit control condition and independently characterized task difficulty. (2) Record recognition, verification, reporting and subsequent action separately, including benign requests; do not infer these from clicks. (3) Evaluate the consequences of providing education to everyone versus only people who trigger a simulation, while recording actual exposure and engagement.

**Remaining limitations:** Single employer and email channel; control-page feedback; no reporting or credential-submission endpoint; engagement self-selection; no publicly accessible individual-level reanalysis; author PDF not compared page-for-page with IEEE's publisher version. This appraisal does not establish that training in general is ineffective or that an alternative intervention works.

**Public disclosure check:** Only published methods/results and non-proprietary research questions appear here. No private scoring, architecture, unpublished participant results, customer material or implementation details.
