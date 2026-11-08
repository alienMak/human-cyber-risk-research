# Repeated phishing outcomes do not establish fixed individual risk

**Paper:** [Canham, Posey, Strickland & Constantino, *Phishing for Long Tails: Examining Organizational Repeat Clickers and Protective Stewards*](https://doi.org/10.1177/2158244021990656)  
**Published:** 1 February 2021, *SAGE Open* 11(1)  
**Type:** Peer-reviewed primary observational research  
**Access:** **FULL TEXT APPRAISED** on 8 November 2026, publisher HTML, *Data Collection and Analysis*, *Findings* (Tables 1–4), *Discussion*, *Conclusion and Future Research*.  
**Canonical full text:** https://journals.sagepub.com/doi/full/10.1177/2158244021990656

## What the authors investigated

The authors analyzed anonymized employee-level responses to **20 simulated phishing campaigns over 19 months** (June 2018–early December 2019) at one southeastern US university. The four cluster counts total **6,126 employees** (344+1,361+4,050+371). Participants received up to 20 campaigns using templates randomly selected from more than 60 lures of differing difficulty and context. This was an observational analysis of operational simulations, **not** a randomized training or feedback trial. There is no benign-email comparison and no independent observation of real compromises. (*Data Collection and Analysis*.)

The recorded outcomes were **click**, **reply**, **data entry**, and **report**. A campaign **failure** meant at least one of click, reply, or data entry; multiple unsafe actions in one campaign counted as one failure. Only **three of the twenty campaigns** permitted data entry, so this outcome had unequal opportunity. Reporting was separately recorded; some reports occurred after a failure. The authors used descriptive frequencies, hierarchical clustering (Ward method, squared Euclidean distances), then four-cluster k-means. The number of clusters was selected by inspection of a scree plot. (*Data Collection and Analysis*; *Findings > Frequency Analysis / Cluster Analysis*.)

**Authors' findings:** Employees with more than three campaign failures represented approximately **6% of the sample and 29% of failures** (Table 1). The authors report that the high-reporting group represented **33% of the population and 92% of reports** (Table 2). Four descriptive clusters had sizes **344, 1,361, 4,050, and 371** (Table 3). The quarter-by-quarter descriptive series shows different patterns of clicking and reporting, without an intervention contrast (Table 4). These percentages are rounded; Table 1's population percentages total 101%, not an independently reconciled count.

**Comparison:** Descriptive within-organization groupings and four time periods, not matched interventions or causal controls. No effect estimate for training or psychological traits should be inferred. The paper does not report a validated prospective prediction model or out-of-sample cluster stability in the inspected sections.

## What the evidence supports, and what it does not

The published data show that repeated simulation outcomes are unevenly distributed across employees, and that reporting behavior is informative alongside unsafe interactions. They **do not show why** any employee repeatedly clicks or reports. Exposure opportunity, lure difficulty, job role, reporting affordances, feedback, time and task context may affect the observed distribution. The authors explicitly acknowledge unknown underlying causes in *Conclusion and Future Research*. Their practical suggestion that persistent failures are unlikely to be context-driven is stronger than this observational design can establish (*Practical Implications*).

The authors' term “risk factor” in Table 1 is a **descriptive ratio of shares**, not a validated individual probability of future compromise. A zero-failure record does not establish immunity, and no-report records cannot distinguish failure to notice from deliberate deletion or inaccessible reporting. Cluster membership derived from the same observations cannot itself validate future prediction. Repeated simulations also do not establish transfer to voice, SMS or real attacks.

## Eight-domain appraisal

| Domain | Assessment | Evidence and reason |
| --- | --- | --- |
| Research design | **Partial** | 20 campaigns across 19 months describe patterns, not causal determinants; *Data Collection and Analysis*. |
| Sampling | **Partial** | One university, mixed employee roles; no representative sampling or full exposure denominator by employee; *Data Collection and Analysis*. |
| Outcome definition | **Partial** | Failure and report operationalized, but data-entry opportunity limited to three campaigns; *Data Collection and Analysis*. |
| Confounding | **No** for causal attribution | Varying lure difficulty, context and potential exposure/role differences not controlled in the reported descriptive clusters; *Data Collection and Analysis; Findings*. |
| Measurement | **Partial** | Platform records actual simulation interactions; no real-attack validation, no benign-message false-alarm denominator; *Data Collection and Analysis*. |
| Analysis | **Partial** | Descriptive clustering with scree-selected four groups; no inspected external validation, uncertainty intervals or stability tests; *Findings > Cluster Analysis*. |
| Generalization | **Partial** | One employer and simulated email; cross-vector and real incident transfer untested; *Conclusion and Future Research*. |
| Ethics/reproducibility | **Partial** | Anonymized records and IRB exemption described; raw data and executable analysis not established as publicly accessible; *Data Collection and Analysis; Footnote*. |

## Research interpretation and proposed tests

1. **Analysis:** Repeated failure counts should be treated as exposure- and task-dependent observations, not fixed individual traits. **Future test:** Hold opportunity and scenario difficulty comparable, then test whether earlier responses predict decisions on unfamiliar later lures with confidence intervals and a held-out sample.
2. **Analysis:** Reporting and unsafe interaction can coexist, including reporting after an unsafe action. **Future test:** Distinguish timely reporting, delayed reporting after interaction, and appropriate non-reporting of benign communications.
3. **Analysis:** Descriptive clusters can summarize a cohort without explaining mechanism. **Future test:** Evaluate whether groupings persist after accounting for job demands, feedback and reporting access; report instability rather than imposing durable employee labels.

**Source relationship:** Distinct from [Canham, Dawkins & Jacobs (2024)](https://www.nist.gov/publications/not-all-victims-are-created-equal-investigating-differential-phishing-susceptibility), previously noted in this repository. The 2021 study is not an independent experimental validation of the 2024 work. [Jensen et al. (2022)](https://doi.org/10.1080/07421222.2022.2096551) is a distinct peer-reviewed gamification paper, checked at **ABSTRACT-ONLY** level in this review; its simulated-workplace experiments and false-alarm findings should not be pooled with these observational clusters. [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) remains **ABSTRACT-ONLY**.

**Public boundary:** This note uses only published third-party evidence and non-proprietary research questions. It contains no private implementation, scoring weights, participant records or confidential organizational data.
