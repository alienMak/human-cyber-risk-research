# Can a phishing-suspicion task predict what happens outside the lab?

**Source:** [*The Phishing Email Suspicion Test (PEST): a lab-based task for evaluating the cognitive mechanisms of phishing detection*](https://doi.org/10.3758/s13428-020-01495-0), *Behavior Research Methods* (published online 2020; journal publication 2021).  
**Source type:** Peer-reviewed empirical methods paper.  
**Access and verification:** Original publisher full article and [NIH PMC full-text manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC8188181/) checked against the [PubMed bibliographic record](https://pubmed.ncbi.nlm.nih.gov/33078362/). The article text, results, discussion and open-practices statement were inspected. **Full-text appraisal completed at article level; underlying data/code and supplement were not independently rerun.**  
**Added:** 18 October 2026.

## Why this paper matters to the trail

We have been separating correct actions, detection ability, response criterion and eventual real-world consequences. PEST gives us an unusually useful bridge: a lab task in which participants *know* they are evaluating suspiciousness, compared at the **email-item level** with effectiveness observed in a separate field study where people were not expecting a phishing test.

This does **not** establish that a person who scores well in the lab will resist real attacks. That distinction is central, not a footnote.

## What was actually measured

Participants rated the suspiciousness of **160 emails**, including phishing and non-phishing material. The article says **84 simulated phishing emails** had previously been used in the PHIT field experiment with **different participants**. The researchers compared laboratory suspiciousness ratings with the prior field click-through effectiveness of those email items.

The article reports that emails rated as less suspicious in the lab tended to be more effective in the field. A secondary comparison split the 84 items into **44 clicked at least once** and **40 never clicked** in the field dataset; the clicked group was rated less suspicious in the lab (**t(82)=2.09, p=.04**). The article also reports about **62% correct classification** in the lab task. These are reported paper results, **not independent recalculations**.

The reported model distinguishes overall suspicion, ability to distinguish phishing from safe emails, and carryover effects from recently viewed messages. That separation is useful because a participant can become more suspicious without becoming better at distinguishing the two classes.

## What the field comparison does and does not validate

**Supported:** There is initial **item-level correspondence** between how suspicious particular messages look in a lab and how often those messages elicited clicks in a separate field sample.

**Not supported:** Individual-level predictive validity. Different people took part in the lab and field components; the authors explicitly acknowledge that the design cannot determine whether an individual's PEST score predicts that same individual's real-world clicking.

**Also not established:** Transfer to phone scams, physical approaches, conversational manipulation, reporting behavior, or durable improvement after training.

## Competing interpretations

1. **Stable item difficulty:** Some email lures are consistently harder to recognize across settings.
2. **Surface-feature overlap:** Laboratory raters and field recipients respond to similar superficial cues, without necessarily sharing a general security skill.
3. **Context dependence:** Field click behavior also depends on workload, timing, trust, expected consequences and whether the email is relevant to the recipient.
4. **Task-awareness effect:** Explicitly asking for suspiciousness ratings may shift participants' attention or criterion compared with ordinary inbox use.

The first two explanations are compatible with the reported item-level correspondence; the latter two limit how far we should generalize. **The paper does not isolate the causal effect of being told to look for phishing.**

## Eight-domain article-level appraisal

| Domain | Finding | Status |
| --- | --- | --- |
| Design | Laboratory ratings compared with separate field email-level outcomes | **Partial**: suitable for item-level correspondence, not person-level prediction |
| Sampling | Different lab and field participants | **Partial**: recruitment and population coverage need full methods |
| Outcome | Suspicion ratings versus field clicks, plus lab classification | **Yes**: outcomes are distinct; full scoring detail not independently checked |
| Confounding | Email content and context may influence both measures | **Partial**: adjusted analyses require full text |
| Measurement | 160 rated emails; 84 linked to field item history | **Partial**: item construction and reliability need review |
| Analysis | Secondary clicked/not-clicked comparison reported with t and p | **Partial**: full model, intervals and multiplicity not extracted |
| Generalization | Email-item relationship across two settings | **No** for individual prediction or cross-vector transfer |
| Ethics/reproducibility | Original article and field-study references identifiable | **Not fully appraised**: protocols and data availability not independently verified |

These ratings reflect **what this review can establish**, not a numerical quality score for the authors. The fuller article-level check below supersedes the earlier partial-access description.

## The next empirical question

Can an individual's discrimination and response criterion measured in a suspicion-rating task predict **their own** later unprompted choices, after accounting for email difficulty and exposure? A design would need ethically collected linked repeated observations, legitimate controls, a preregistered endpoint, and explicit handling of task-awareness effects. This is a future research question, not a completed study.

**Twin's conclusion:** A laboratory instrument can show promising *item-level* ecological correspondence while remaining unvalidated for *person-level* risk prediction. Mixing those claims would turn useful evidence into an overstatement.

**Public boundary:** Only published findings and general methodological questions; no private platform mechanisms, unpublished scoring logic or participant data.


## Full-text verification and corrections — 18 October 2026

**Primary texts inspected:** [Publisher version](https://doi.org/10.3758/s13428-020-01495-0) and [PMC author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC8188181/). The original paper was **published online 19 October 2020** and appeared in the **June 2021** journal issue; these dates are not competing publications.

**Design:** Participants rated 160 emails on a four-point scale, with 40 each of real phishing, simulated phishing, real safe and simulated safe. Only **84 simulated phishing emails** had comparable prior PHIT field outcomes. Field and laboratory participants were **different individuals**, so the field comparison is at the *email-item* level.

**Reported outcomes checked in the Results:** Mean laboratory classification accuracy was **62%**. The authors report **Spearman rho(82) = −0.22, p = 0.048** for the association between lab suspicion and field click effectiveness across 84 emails; the direction is consistent with more convincing emails receiving lower suspicion ratings. The separate split of 44 field-clicked versus 40 never-clicked email items yielded **t(82) = 2.09, p = 0.04**. These are **modest, near-threshold results** and do not establish strong predictive performance. The paper itself says the effect needs replication.

**Critical distinction:** Neither correlation predicts whether *a particular participant* will click later. The paper explicitly states this limitation and calls for a within-person lab/field validation design.

**Sampling and generalization:** The authors identify the lab sample as University of Arizona undergraduates with a **mean age under 19**. Generalization to working adults and different roles is not established.

**Measurement context:** Participants were expressly instructed to judge suspiciousness in the lab; field participants were not expecting a phishing study. This is a difference in context, **not a randomized test of the effect of awareness or explanation prompts**.

**Reproducibility:** The paper says the experiment was **not formally preregistered**, identifies de-identified data on Dataverse, and links public [task implementation](https://github.com/zmhakim/PEST) and [analysis code/data](https://github.com/bobUA/HakimEtAl_PEST_dataAndCode). The links are reported by the authors; this review did **not** run the code or verify numerical reproduction.

### Updated eight-domain judgments

| Domain | Judgment | Basis and caveat |
| --- | --- | --- |
| Design | **Yes, bounded** | Appropriate initial item-level ecological comparison; no same-person prediction |
| Sampling | **Partial** | Undergraduate laboratory sample, narrow age profile |
| Outcome definition | **Yes** | Suspicion ratings, classification and field click rates distinguished |
| Confounding | **Partial** | Lab/field differ in participant population, setting and awareness |
| Measurement | **Partial** | Explicitly rated suspicion is not ordinary inbox behavior |
| Analysis | **Partial** | Correlation and t-test reported; near-threshold p-values and no independent replication |
| Generalization | **No for person-level prediction** | Only email-item association established |
| Ethics/reproducibility | **Partial** | Open code/data links and no preregistration disclosed; files not rerun |

### Follow-the-trail question

**Does the act of explicitly asking for a suspicion rating change how an email is processed?** This paper cannot answer causally because it did not randomize task awareness. A separate study would need comparable cases under different assessment instructions and later unprompted behavior, with legitimate controls and appropriate participant/item dependence. That is an **open hypothesis**, not a finding attributed to Hakim et al.

**Evidence boundary:** Full article inspected; supplements and raw-data reanalysis outstanding. No proprietary platform design or private participant data.
