# Can coping with phishing anxiety support protective action without proving that action occurred?

**Paper:** [McGill, Thompson and Narula, “Not all bad”: Determinants and impacts of emotion-focused and problem-focused coping in information security behavior](https://doi.org/10.1016/j.cose.2026.104872)  
**Publication:** *Computers & Security* 165, article 104872; available online **26 February 2026**.  
**Type:** Peer-reviewed empirical journal article.  
**Access/review status:** **FULL TEXT APPRAISED 2026-11-01**, [13-page author-hosted publisher-layout PDF](https://nikthompson.com/PDF/McGill-Thompson-Narula-2026.pdf), §§3–7, Tables 1–5, Appendix Table A.1.  
**Related source:** [Thompson, McGill and Narula (2024), “No point worrying”](https://doi.org/10.1016/j.cose.2024.103897), [original PDF](https://nikthompson.com/PDF/Thompson-McGill-Narula-2024.pdf), **methods/results cross-check only** (§§4–5), not a fresh full-text appraisal of that paper.

## What the authors investigated

The paper examines whether two emotion-focused coping responses to phishing threats relate differently to self-reported protective practices. *Positive reappraisal* means treating a threatening situation as a possible learning or growth opportunity. *Threat devaluation* means acknowledging the threat while reducing its perceived seriousness to manage stress (2026 paper §3, Table 1).

**Design, population and comparison:** Cross-sectional, nonrandomized online questionnaire of **518 Australian adults** recruited through PollFish; 53 questions administered through Qualtrics, with a ten-person wording pretest. The authors report ethics approval and consent. There was **no assigned intervention, no randomized control group, no phishing-message classification task, and no observed follow-up**. The comparison is between associations among measured psychological constructs, not experimental conditions (§4, p. 6 of the PDF; Table 2).

**Operational outcomes:** All constructs used five-point self-report items. Crucially, the construct called “phishing protection behavior” was measured using statements about efforts to scan or concentrate on email, not independently logged clicks, reports, credential disclosure, or observed verification. Positive reappraisal and threat devaluation were also questionnaire constructs (Appendix Table A.1, PDF pp. 10–11). PLS structural-equation modeling with 5,000 bootstrap samples tested the proposed paths; some items with weak loadings were removed (§§4–5, Tables 3–4).

**Reported associations:** Positive reappraisal was associated with higher self-reported protection (standardized path β = **0.198**, p < .001). The threat-devaluation path was close to zero (β = **0.001**, p = .978). Response cost was associated with more threat devaluation (β = **0.426**, p < .001). The fitted model explained **39.2%** of the variance in the self-reported protection construct (§5, PDF pp. 6–7, Fig. 2/Table 4). These are model-based associations, **not causal intervention effects or observed reductions in phishing susceptibility**.

## A consequential overlap check

The earlier [2024 *Computers & Security* article](https://doi.org/10.1016/j.cose.2024.103897) by the same three researchers also reports **518 valid Australian survey responses, 54.8% female/45.2% male, PollFish/Qualtrics recruitment, a ten-person pretest, 5,000 bootstrap samples, and exactly 18.80% variance in the first factor of its common-method check** (2024 §§4–5, PDF pp. 5–6). The 2026 paper reports those same figures (2026 §§4–5, PDF p. 6), and explicitly builds on the earlier model. This is **strong evidence of potentially reused survey data**, but the reviewed text does not explicitly confirm identical participant records. Until clarified, **do not treat the 2024 and 2026 papers as independent samples or replications**, and do not pool their estimates as independent evidence.

A second statistical boundary matters: the 2026 authors mark null hypotheses about no effect (H9 and H16) as “supported” when the paths were nonsignificant (§5, Table 4). Nonsignificance alone does not establish equivalence or absence of an effect; no equivalence bounds were reported in the checked sections.

## Eight-domain appraisal

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Research design | **Partial** | Cross-sectional PLS model can examine associations, not temporal ordering or causal effects (§§4–5). |
| Sampling | **Partial** | N=518, Australian adults from a survey panel; recruitment and demographics reported, but panel selection and national representativeness are not established (§4, Table 2). |
| Outcome definition | **Partial** | Constructs are defined (Table 1), but “protection behavior” is self-report rather than observed protective action (Appendix Table A.1). |
| Confounding | **Partial** | Multiple psychological paths modeled, but unmeasured security experience, prior training, work context and shared response tendencies remain possible; no randomization (§§4–6). |
| Measurement | **Partial** | Adapted items, CR/AVE/HTMT and item removal reported; self-report and construct overlap remain important (Tables 3, A.1–A.2). |
| Analysis | **Partial** | Bootstrap 5,000 and path estimates reported; null paths interpreted as supported no-effect hypotheses; no independent replication (Tables 4–5). |
| Generalization | **No for observed behavior** | Australian survey attitudes cannot validate real inbox decisions, reporting, repeated simulations or other attack channels (§6.1, limitations, PDF p. 10). |
| Ethics/reproducibility | **Partial** | Ethics and consent described (§4); authors state data cannot be shared (Data availability, PDF p. 12). |

The authors acknowledge self-report and possible common-method bias despite statistical checks, and recommend objective behavioral measures (2026 §6.1, PDF p. 10). Gender analyses were exploratory; group differences should not be treated as immutable traits or individual-level risk predictors (§§5–6).

## What the evidence changes, and what it does not

**Author finding:** In this survey model, positive reappraisal and threat devaluation had different associations with self-reported protective practices. The results suggest that not all emotion-focused responses should be collapsed into a single “maladaptive” category.

**Interpretation:** The key distinction is between **feeling able to respond constructively**, **saying one takes protective action**, and **actually doing so in a particular situation**. This paper measures the first two through the same questionnaire, not the third. The likely relationship to the 2024 dataset makes it especially important not to count these as independent confirmations.

**Proposed future tests, not conducted here:**
1. Randomize a brief constructive-reappraisal message against a neutral control, then measure actual verification and reporting on **unfamiliar** consented tasks rather than only questionnaire agreement.
2. Test whether perceived response cost changes the choice between pausing to verify and dismissing the threat, while recording legitimate-message disruption as well as missed attacks.
3. Follow participants across different contexts and times to ask whether coping language predicts behavior beyond baseline confidence, training and scenario difficulty.

**Other source lanes:** The [SOUPS 2026 Weidhaas et al. study](https://www.usenix.org/conference/soups2026/presentation/weidhaas) was checked at **ABSTRACT-ONLY** level for emotional/workplace context; its large PDF was not reliably retrieved here. No preprints, news, or podcasts were used as empirical support.

**Open limitations:** Confirm possible 2024/2026 sample reuse with authors or deposited study metadata; assess objective behavior in a new design; avoid interpreting a null path as evidence of no effect. This is a source-based analytical note, not a statement that the repository owner personally read or endorsed the paper.
