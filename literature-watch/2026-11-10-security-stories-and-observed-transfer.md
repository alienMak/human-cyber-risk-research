# Do security stories change decisions, or mainly how people describe them?

**Paper:** [Pfeffer, Mai, Weippl, Rader & Krombholz, *Replication: Stories as Informal Lessons about Security*](https://www.usenix.org/conference/soups2022/presentation/pfeffer)  
**Original full text:** https://www.usenix.org/system/files/soups2022-pfeffer.pdf  
**Publication:** SOUPS 2022, August 2022, pp. 1–18 (peer-reviewed proceedings; no DOI asserted)  
**Access:** **FULL TEXT APPRAISED** on 2026-11-10; original proceedings PDF, §§3–8, Tables 1–10 and Appendix 9.1.  
**Related original study:** [Rader, Wash & Brooks (SOUPS 2012)](https://whispr.ischool.wisc.edu/papers/2012/03/27/security-stories.html), outside this review's 2016–2026 inclusion window. The 2022 paper is a replication with a different sample and modified instrument, not a second analysis of the same respondents.

## Design, population, measures and comparison

Cross-sectional mixed-methods survey of adults recruited through SurveyMonkey, with US age/gender quotas, not a probability sample. Of 622 responses, 299 were retained after excluding unusable responses, attention-check failures, autobiographical incidents and advice instead of stories. Survey pretest n=16. Respondents recalled one story about a security incident affecting someone else, then reported its source, context, seriousness, perceived emotions, retelling, change in thinking and whether they had changed protective behavior. No story was experimentally assigned and no subsequent action was observed. The comparison was primarily between story attributes and reported outcomes, and with the separate 2012 student survey (n=301); questionnaire wording and coding also differed. **Evidence:** §§3.1–3.3, pp. 3–4, Table 1; Appendix 9.1, pp. 15–16.

Two coders developed inductive themes and independently coded responses; reported Cohen's κ=0.89 after codebook refinement. Logistic regressions modeled binary outcomes such as reported behavior change and retelling; OLS regressions modeled scaled thinking and emotion outcomes. **Evidence:** §3.3, p. 4; §6, pp. 9–11.

## Findings attributable to the authors

Table 2 (p. 5) reports that 52% **said** they changed behavior after hearing a story (also 52% in the 2012 sample); 48% said they retold the story, 71% described a lesson and 96% believed the story was true. These are retrospective responses, not verified behavior or evidence that the story was actually true. The content model associates stories containing a lesson with approximately doubled odds of *reported* behavior change; seriousness is associated with 31% higher odds per scale point (§6.1, Table 3, p. 9). Emotion ratings of anxiety and anger correlate with reported change and retelling (§§6.1–6.2, Tables 5 and 8, p. 10). A casual-versus-formal setting association differs in direction from the 2012 study (§6.1, Table 4, pp. 9–10), so the contextual result should not be described as replicated. Tables show regression estimates and significance markings, but no independent reanalysis or multiplicity correction was performed here.

## Eight-domain quality appraisal

| Domain | Assessment and basis |
| --- | --- |
| Design | **Partial:** suitable for associations and replication of survey patterns; not causal effects of stories (§§3, 6). |
| Sampling | **Partial:** quotas for age/gender, but convenience panel, substantial exclusions and no probability sampling (§3.2, Table 1). |
| Outcomes | **Yes for operational clarity:** story retelling and self-reported thinking/behavior explicitly defined; **no observed security outcome** (§3.1, Appendix 9.1). |
| Confounding | **Partial:** source/context and demographics modeled, but memory salience, baseline practices, prior experiences and unmeasured context remain (§§3, 6–7). |
| Measurement | **Partial:** questionnaire and qualitative coding described, κ=0.89; retrospective self-attribution and modified web-skills questions lack behavioral validation (§§3.1, 3.3). |
| Analysis | **Partial:** logistic/OLS models and significance marks reported; multiple comparisons, missing-data sensitivity and model calibration not independently established (§6, Tables 3–10). |
| Generalization | **No for real-world behavioral change:** one recalled story, US online panel, no verified transfer or prospective observation (§7, p. 12). |
| Ethics/reproducibility | **Partial:** compensation and questionnaire available; original-study anonymized data shared with authors, but independent data/code replication and complete privacy documentation not established from checked sections (§§3.2–3.3, Appendix 9.1). |

## Interpretation and future questions (not findings)

1. **Recall versus transfer:** A reported lesson and a reported change in behavior are not an independently observed protective decision. A future consented study could compare a concrete story with matched non-narrative guidance and test unfamiliar decisions later, separately recording correct action and false alarms.
2. **Emotional salience versus useful instruction:** Associations involving fear, anger and perceived seriousness do not establish that inducing distress improves protection. A future test could hold factual advice constant while varying narrative framing, measuring understanding, appropriate verification and unintended anxiety.
3. **Replication boundaries:** The 2012 and 2022 samples support some repeatability of *self-report patterns*, not replication of a causal training effect. Different recruitment and questionnaire versions, plus a reversal in the context association, limit strong generalization.

**Review boundary:** The 2012 paper is historical context only; no preprint, news or podcast is used as empirical corroboration. No proprietary scoring, application internals, organizational data, participant records or private research methods are included.
