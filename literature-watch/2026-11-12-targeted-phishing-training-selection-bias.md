# Does mandatory training change repeated phishing decisions?

**Paper:** [Gordon et al., Evaluation of a mandatory phishing training program for high-risk employees at a US healthcare system](https://doi.org/10.1093/jamia/ocz005)  
**Published:** 12 March 2019 online; *Journal of the American Medical Informatics Association* 26(6), 547–552 (June issue)  
**Type:** Peer-reviewed primary observational study  
**Access/review status:** FULL TEXT APPRAISED, 12 November 2026. [Complete open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6515532/), *Materials and Methods*, *Results*, *Discussion* and Figures 1–4; supplementary ZIP not examined.  
**Prior coverage:** Already indexed as ABSTRACT-ONLY in the 27 October screening register and discussed on 11 November. This note upgrades the evidence status, not the count of unique papers.

## What the authors investigated

A retrospective, single-institution evaluation of a mandatory phishing course introduced after campaign 15 for employees who had clicked at least five simulated phishing messages before campaign 16. The healthcare institution used a third-party simulation program, with brief feedback after clicks, and ran 20 campaigns approximately every two to three months between July 2015 and May 2018. None of the simulated emails were spear-phishing messages (*Methods*, *Results*).

Across the institution, 35,580 employees received 390,908 simulated messages. The main consistent-exposure analysis included 5,416 employees who received all 20 campaigns. Of these, 772 met the five-click threshold; 740 completed the mandatory course. The course covered phishing concepts, an example and detection guidance, followed by a ten-question test with unlimited retakes; network access was suspended pending completion (*Methods*, Figure 1, *Results*, Figure 2).

**Outcome:** Whether each employee clicked a simulated email in each campaign. The authors compared per-campaign click-rate trajectories for threshold-defined employees and others before and after training was offered. They did **not** measure reporting, verification, actual compromise, decision latency or transfer to other attack types. The comparison was **not randomized**: the training group was defined by prior clicks, and 32 designated employees did not complete the course but remained in the designated group (*Statistical analysis*, *Results*).

## Findings and boundaries

The authors report that click rates declined across campaigns in both groups, but the mandatory course did not produce a substantial additional improvement in the previously high-click group. In campaigns 16–20, that group continued to show approximately 10–25% campaign click rates, including almost 25% in campaign 17 (*Results*, Figure 4; *Discussion*). These are descriptive comparisons, **not a causal treatment-effect estimate**. The paper reports descriptive analysis rather than an adjusted effect estimate with uncertainty interval.

Campaign click rates varied sharply, and the authors used observed click rate as a proxy for campaign difficulty. That is not an independent validated difficulty measure. Because the group was selected on earlier failures, regression to the mean, unequal prior exposure to click-triggered feedback, message differences and changing organizational context cannot be separated from course effects. The authors explicitly state that quasi-experimental and mixed-effects approaches could not overcome outcome-based group selection (*Statistical analysis*, *Discussion*).

## Eight-domain appraisal

| Domain | Assessment | Evidence |
| --- | --- | --- |
| Design | Partial: suitable for describing repeated campaigns, not isolating training causality | *Study design and setting*; *Discussion* |
| Sampling | Partial: one academic medical center, main analysis restricted to employees present for all 20 campaigns | *Measurements*; *Results*, Figure 2 |
| Outcome definition | Yes for simulated clicks; other security decisions absent | *Measurements* |
| Confounding | No adequate control for selection on past clicks, lure variation, role or language | *Statistical analysis*; *Discussion* |
| Measurement | Partial: campaign clicks tracked; campaign difficulty inferred from click rate itself | *Measurements*; *Results*, Figure 4 |
| Analysis | Partial: descriptive trajectories; no credible adjusted causal estimate or uncertainty interval | *Statistical analysis*; *Discussion* |
| Generalization | Limited: one healthcare institution, non-targeted email simulations | *Study design and setting*; *Results*; *Discussion* |
| Ethics/reproducibility | Partial: IRB approval and anonymization reported; supplementary figures supplied; no independently reproducible employee-level dataset established | *Measurements*; *Statistical analysis*; *Supplementary Material* |

## Where this leaves the question

**Author finding:** In this institution's ongoing campaign program, the additional mandatory course was not associated with a substantial distinct reduction in clicks for the selected group. The authors also observe broad decreases over repeated campaigns.

**Analytical interpretation:** A training program can be evaluated against an inappropriate comparator if intervention eligibility is defined by prior failure. Apparent change may also depend on campaign difficulty and prior feedback. The study cannot establish that mandatory training never works, nor that repeated exposure itself caused the decline.

**Proposed tests, not completed research:** (1) Randomize eligible participants to ethically acceptable alternative training approaches, stratified by prior exposure, and use unfamiliar, independently difficulty-rated scenarios for follow-up. (2) Distinguish unsafe interaction from verification, reporting and false alarms. (3) Test whether improvement persists after a delay rather than interpreting campaign order alone as learning.

**Related but separate primary paper:** [Gordon et al., *Assessment of Employee Susceptibility to Phishing Attacks at US Health Care Institutions*](https://doi.org/10.1001/jamanetworkopen.2019.0393), *JAMA Network Open*, 8 March 2019, examines six institutions and campaign-level associations. Shared authors and organizational context mean its data must not be presumed independent of this single-center study. No pooled effect is calculated.

**Source classification:** Peer-reviewed journal primary evidence above. No preprint, news or podcast used as corroboration. This note is a literature appraisal, not a claim of personal endorsement or original experimental results.
