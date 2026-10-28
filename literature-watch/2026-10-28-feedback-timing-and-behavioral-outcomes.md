# Does feedback change recognition, reporting, or both?

**Study:** Svetlana Bender, Samantha Horn, George Loewenstein and Olivia Roberts, [*Phishing feedback: just-in-time intervention improves online security*](https://doi.org/10.1017/bpp.2024.19), *Behavioural Public Policy* 10(3), 527–539.  
**Publication chronology:** Published online **11 September 2024**; assigned to the **July 2026** journal issue. These are two dates for one paper, not separate studies.  
**Source type:** Peer-reviewed journal article. **Review status:** **FULL TEXT APPRAISED**, publisher's open-access 13-page PDF, 28 October 2026. [Publisher article](https://www.cambridge.org/core/journals/behavioural-public-policy/article/phishing-feedback-justintime-intervention-improves-online-security/4F5DF23A7AB0DC81561A1778E06802E2). Supplementary appendix not independently appraised.  
**Deduplication:** Title/DOI absent from the repository evidence matrix and screening register before this addition. [Ho et al. (2025)](https://doi.org/10.1109/SP61157.2025.00076) is a distinct healthcare field study, not a duplicate or direct replication.

## Design and sample

The researchers randomly selected **11,802 employees** at one Florida health-solutions organization. Data were collected in three waves: July 2021 (3,000 initially), October 2021 (3,999) and March 2022 (4,803). An implementation error placed 957 individuals in multiple waves; retaining only the first appearance left **10,844 unique analyzed employees** (3,000 + 3,874 + 3,970). The paper reports available age data with mean 41.1 years; gender was missing for 43%, and demographic-adjusted analyses were not feasible (*Methods > Participants; Procedures*, printed pp. 532–533, notes 3–5).

Each person received a simulated phishing email and another **two weeks later**. The baseline message used a link in all waves; the assessment message used a link in wave 1 and an attachment in waves 2 and 3. Baseline behavior divided participants into the authors' labels **“Victims”** (clicked/opened), **“Ignorers”** (neither interacted nor reported), and **“Reporters”** (reported without interacting). These are behavioral categories for this experiment, not enduring person types. The authors report baseline percentages separately by wave (*Procedures*, pp. 533–534).

Participants were randomly assigned to **feedback versus no feedback**. For baseline clickers, feedback appeared immediately as a web-page message after interacting. For baseline non-reporting non-clickers, feedback was an email sent **one week later**, praising non-interaction and encouraging reporting. Reporters all received congratulatory feedback; the preregistered randomized comparison for that group was **not implemented** because of reporting-software constraints (*Procedures*, pp. 532–534, note 4).

**Crucial comparison boundary:** Within each baseline-response group, randomized feedback was compared with no feedback. **Immediate versus one-week feedback was not randomized against each other**: the timing, message content and baseline groups differed. This paper therefore cannot establish the optimal timing of feedback.

## Outcomes and reported effects

The two measured kinds of observable outcome at the second simulated email were **interaction** (clicked link or opened attachment; the paper calls this “fell victim”) and **reporting**. Neither is a direct measure of recognizing cues, learning, real compromise or durable behavior beyond the second message. The authors pooled three waves with wave indicators in logistic regressions (*Results*, printed pp. 534–536; Figure 2 and Table 1).

| Baseline response group | Assessment outcome | No feedback | Feedback | Adjusted odds ratio for feedback, Table 1 |
| --- | --- | ---: | ---: | ---: |
| Initial interactors, n=992 | Interacted with second lure | 50% | 40% | **0.660**, SE 0.090, p<.01 |
| Initial interactors, n=992 | Reported second lure | 15% | 19% | **1.268**, SE 0.219, not significant |
| Initial non-reporting non-interactors, n=8,697 | Interacted with second lure | 22% | 20% | **0.870**, SE 0.048, p<.05 |
| Initial non-reporting non-interactors, n=8,697 | Reported second lure | 7% | 10% | **1.463**, SE 0.118, p<.001 |

These are **percentage-point differences**, not relative percentage reductions. The paper reports odds ratios with standard errors, **not confidence intervals** in Table 1; no intervals are manufactured here. The n values are the subgroup analysis denominators, not the full 10,844 participants. All 1,155 baseline reporters were outside these subgroup treatment-effect analyses.

## Eight-domain appraisal

| Domain | Judgment | Basis and limitation |
| --- | --- | --- |
| Design | **Yes** for feedback versus none within eligible baseline groups; **No** for comparing feedback timing | Randomized assignment, but different messages and baseline strata for immediate and delayed feedback (pp. 533–534). |
| Sampling | **Partial** | Random sample from one employer; duplicates corrected; demographics incomplete (p. 532). |
| Outcome definition | **Yes** for simulated interaction/reporting; **No** for recognition or actual compromise | Binary endpoints measured at the second lure (pp. 533–534). |
| Confounding | **Partial** | Wave controls; messages and baseline behavior differ across waves; possible attention effects and unmeasured role differences (pp. 533–537). |
| Measurement | **Partial** | Observed workplace responses; no direct knowledge, uncertainty, verification or false-alarm assessment (pp. 533–534). |
| Analysis | **Partial** | Logistic odds ratios/SEs and wave indicators, but no demographic adjustment and no independently reviewed supplementary analyses (Table 1, p. 536; note 4). |
| Generalization | **Partial** | One US health-solutions employer, two lures per person, two-week endpoint (pp. 532–537). |
| Ethics/reproducibility | **Partial** | First wave preregistered; reporter comparison and demographic analyses deviated from plan; supplementary materials linked but not reviewed here (p. 532, note 4; p. 537). |

The authors also acknowledge that their study **does not isolate timing or mechanism**, that awareness of being studied may change behavior, and that only one later phishing episode was tested (*Conclusion*, printed pp. 537). Feedback could affect knowledge, perceived consequences or other responses; the design does not distinguish these explanations.

## Interpretation and next tests

**Authors' finding:** Compared with no feedback, feedback reduced subsequent simulated interactions in both eligible baseline groups. Reporting increased significantly among baseline non-reporters who had not interacted, but the increase among baseline clickers was not statistically significant.

**Analysis:** This is a counterexample to treating all phishing education as ineffective, but it does not contradict the much smaller average effect of **a different intervention and population** in [Ho et al. (2025)](https://doi.org/10.1109/SP61157.2025.00076). The studies have different eligibility, content, comparison conditions and outcomes. The useful distinction is between *who was eligible*, *what feedback they actually received*, *which later action changed*, and *how long the change lasted*. A nonsignificant reporting result among initial clickers is not evidence of zero reporting effect.

**Proposed future tests, not completed:** (1) Randomize feedback **timing while holding content and initial response category constant**, then compare reporting and interactions on unfamiliar messages. (2) Measure whether increased reporting reflects better discrimination or simply greater willingness to ask for help, including legitimate-message false alarms. (3) Repeat beyond two weeks to test persistence and possible familiarity effects.

**Open question:** Does a short-term increase in reporting reflect better recognition, a change in expectations about reporting, or both? A follow-up needs separate measures; this paper does not identify the mechanism.

**Source-type boundaries:** [Junger, Montoya and Overink (2017)](https://doi.org/10.1016/j.chb.2016.09.012) was checked at **publisher/institutional abstract level** as an older warning/priming comparator. [Schiller et al. (CHI 2026)](https://doi.org/10.1145/3772318.3791490) and [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) were checked at **publisher abstract level** only; their full texts were not appraised in this run. No preprints, news or podcasts were used as empirical corroboration.

**Public disclosure gate:** This note contains published study methods/results and non-proprietary future research questions only. It includes no private system design, scoring algorithm, unpublished participant observations, credentials, confidential organizational data or production changes.
