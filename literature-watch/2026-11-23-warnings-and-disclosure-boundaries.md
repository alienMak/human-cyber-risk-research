# A warning is not the same as a safer disclosure decision

**Paper:** Junger, M., Montoya, L., & Overink, F.-J. (2017). [Priming and warnings are not effective to prevent social engineering attacks](https://doi.org/10.1016/j.chb.2016.09.012). *Computers in Human Behavior*, 66, 75–87. First available online 24 September 2016; journal issue 2017.  
**Original full text:** [University of Twente hosted published PDF](https://ris.utwente.nl/ws/portalfiles/portal/6741431/Junger_Montoya_Overink_Priming.pdf).  
**Type:** Peer-reviewed primary empirical article. **Access:** FULL TEXT APPRAISED 23 November 2026 (pp. 80–85, Methods §§2.1–2.2, Results §§3.1–3.2, Discussion §4 and limitations). No independent data reanalysis.  
**Deduplication:** Previously mentioned as abstract-level context in the 28 October screening register, not a new publication or independent replication.

## What the authors investigated

In a Dutch shopping district, passersby were invited to complete a questionnaire. The three conditions were (a) four cybercrime/privacy priming questions, (b) a warning leaflet before the questionnaire plus a reminder on each page, and (c) a questionnaire without either intervention. The article does not establish a clearly documented individual random-allocation procedure; do not label this a randomized controlled trial. Data were collected across five days with attention to condition distribution across times (Methods §§2.1–2.2, pp. 80–81).

Of 290 completed questionnaires, two were excluded for infrequent internet use and ten for missing covariates, leaving **278** analyzed (control 96; priming 94; warning 88). The online-shopping subgroup was **256**. Group ages differed: the warning group was older and priming group younger, prompting adjustment for age and age squared (Results §3.1, Table 1, pp. 81–82). This is a convenience sample, not a representative population sample.

**Outcomes:** Whether participants wrote down an email address; nine of eighteen bank-account digits; and, among prior online shoppers, the type of item purchased and the shop's name. Each was coded disclosed/not disclosed. The authors also summed the four binary disclosures as a descriptive 'total risk' outcome, not a validated cyber-risk score. No phishing email, credential compromise, reporting, longitudinal follow-up or genuine attacker was observed (Methods §2.2.2, pp. 80–81). Importantly, email address was requested **before** the priming questions but **after** the warning leaflet. Thus email disclosure cannot test the effect of priming in the same way as the later questions (p. 80).

## Findings, with statistical boundaries

Across analyzed respondents, 79.1% supplied an email address and 43.5% supplied partial bank information. Among online shoppers, 89.8% gave the purchased product type and 91.4% gave the shop name (Abstract; Results §3.2 and Discussion §4.1, pp. 81–83). These are disclosure rates in a research questionnaire, **not** phishing-success rates.

Unadjusted comparisons showed fewer email addresses disclosed in the warning condition (67% versus 81.3% control and 88.3% priming). Conversely, 98.7% in the warning condition named their online shop, versus 87.4% control and 89.1% priming. The age-adjusted logistic models did not establish a reduction in email, bank or product disclosure. The warning association for naming a shop was in the adverse direction (reported OR 11.43, 95% CI 1.39–94.09); its very wide interval warrants caution (Results §3.2, Fig. 4, Table 2, pp. 82–83). The Poisson model did not establish an intervention-related reduction in the four-item disclosure count (Table 3, p. 82). Failure to detect benefit is **not** proof that all warnings are ineffective.

## Eight-domain appraisal

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Research design | Partial | Three contemporaneous conditions in a field questionnaire; individual random assignment not clearly established; §§2.1–2.2 |
| Sampling | Partial | Shopping-district convenience recruitment; 290 questionnaires, 278 analyzed; nonparticipants uncharacterized; §3.1, §4 limitations |
| Outcome definition | Yes, narrow | Four recorded disclosure decisions; no observed phishing or longer-term behavior; §2.2.2 |
| Confounding | Partial | Age and age squared adjusted, but condition age imbalance and other unmeasured differences remain; §3.1, Tables 1–3 |
| Measurement | Partial | Binary recorded answers, but no validated link to actual attack harm; email request precedes priming; §2.2 |
| Analysis | Partial | Logistic/Poisson regression and intervals reported; sparse shop non-disclosure gives wide warning CI; Tables 2–3 |
| Generalization | No for phishing effectiveness | Face-to-face Dutch survey setting differs from inbox, SMS and workplace decisions; §4 limitations |
| Ethics/reproducibility | Partial | Faculty ethical permission and debrief reported, partial bank digits collected for privacy; underlying participant data not independently checked; p. 80 |

## Interpretation and next tests

**Author finding:** Neither intervention reliably reduced overall disclosure in this setting; one warning-related shop-name association was adverse.

**Analysis:** The study challenges the assumption that a brief warning automatically changes behavior. It cannot distinguish whether participants noticed the warning, understood it, trusted the requester, or considered the requested information sensitive. The authors' claim that the warning was noticed is not independently established through an attention measure (Discussion §4.3.1). An apparently adverse subgroup effect should not be generalized to all warnings.

**Proposed future tests, not implemented methods:**
1. Compare identical legitimate and deceptive information requests with and without a warning, measuring disclosure and mistaken refusal separately.
2. Measure warning comprehension and perceived sensitivity before attributing an unchanged decision to deliberate disregard.
3. Test whether any short-term change persists in unfamiliar communication contexts rather than assuming transfer from a questionnaire to phishing.

**Open limitations:** Allocation mechanism, refusals to participate, unmeasured trust and requester effects, sparse-event uncertainty, and no follow-up or independent dataset replication. This paper is distinct from the SOUPS email-classification and workplace simulation studies; do not pool its percentages with click rates.

**Other source lanes:** No preprints, news or podcasts used as empirical corroboration. Original publisher identity and DOI cross-checked against the University of Twente record.
