# Does the apparent source of phishing training change later clicking?

**Paper:** Rick Wash and Molly M. Cooper, [*Who Provides Phishing Training? Facts, Stories, and People Like Me*](https://doi.org/10.1145/3173574.3174066).  
**Published:** CHI 2018, 21 April 2018.  
**Type:** Peer-reviewed primary field experiment.  
**Access:** **FULL TEXT APPRAISED**, [author-hosted original paper](https://rickwash.com/papers/phishing-stories.pdf), pp. 4–9, Methods, Results, Discussion, Tables 3–7 and Figure 3. Appendix training examples inspected; [supplementary regression output](https://osf.io/snh7e/) **not independently appraised**.  
**Review date:** 17 November 2026.

## What was actually tested

Researchers sampled 2,000 non-faculty, non-IT staff at one US university; after duplicate-record correction the analyzed cohort contained **1,945**. Four simulated IT-themed phishing emails were delivered at days 0, 2, 7 and 42, counterbalanced by email order. A participant who clicked for the first time saw one randomly assigned page: facts/advice attributed to an expert, facts/advice attributed to a peer, a story attributed to an expert, a story attributed to a peer, or a no-training control. The training was delivered **only after a click**, and only once. The outcome was subsequent clicks on simulated links, not credential disclosure, reporting, recognition accuracy or actual compromise. See Methods pp. 4–7 and Results pp. 7–8.

The researchers pretested email realism (100 valid crowdworker responses) and lesson coverage of candidate training texts (51 valid responses). They selected one story and one advice text. The texts were matched on six directly relevant lesson ratings but not on all other lesson content (Methods pp. 5–6). The study was approved by an IRB; the paper reports no advance consent or debriefing and describes privacy protections (Ethical Concerns, pp. 6–7).

## Finding, uncertainty and interpretation

**Authors' observed data:** 502 of 1,945 participants clicked at least once. Only **421** first clicked early enough to have a later opportunity to demonstrate post-training behavior. In that subset, Table 7 gives subsequent-click proportions of **14/76 (18%)** for expert advice, **19/81 (23%)** for control, **21/89 (24%)** for peer story, **22/87 (25%)** for peer advice, and **30/88 (34%)** for expert story. These are descriptive conditional proportions, not population-wide treatment effects. The five-group chi-square test is **χ²(4, N=421)=6, p=0.2**, so it does **not** establish a statistically significant difference across groups (Results, Table 7, p. 8). Figure 3 shows model-adjusted probabilities from multilevel logistic regression, but its supplemental coefficients and uncertainty were not checked here.

**Analysis:** The authors describe a source-by-format interaction and suggest expert advice performs best. That pattern is worth testing, but the non-significant omnibus test and unappraised regression details do not support a definitive efficacy claim. Nor does the study establish that peer narratives improve behavior over no training: peer story (24%) and control (23%) are almost identical in Table 7. Randomization strengthens the design, but the analyzable subgroup depends on having clicked and having a subsequent exposure; the same IT theme, one institution, and one text per format constrain generalization. Campaign difficulty was partly addressed by counterbalancing, not independently established as equivalent.

**Related evidence, separately labeled:** [Marsden et al., *Facts and Stories in Phishing Training: A Replication and Extension*](https://doi.org/10.1145/3334480.3381435), CHI 2020 **extended abstract / replication, ABSTRACT-ONLY here**. Its [replication-atlas record](https://forrt.org/flora-replication-atlas/doi/10.1145/3173574.3174066/) labels the replication unsuccessful, but the original 2020 full text and analytic details were **not** appraised, so that label alone is not evidence of a precisely comparable null effect. The 2022 [Pfeffer et al. replication](https://www.usenix.org/conference/soups2022/presentation/pfeffer) examines remembered informal security stories and is **not** an independent replication of this field-training manipulation. No preprints, news or podcasts were used as empirical corroboration.

## Eight-domain appraisal

| Domain | Assessment | Evidence and qualification |
| --- | --- | --- |
| Research design | Partial | Randomized 2×2 plus control; training contingent on first click, later click opportunity varies (Methods pp. 4, 7–8) |
| Sampling | Partial | Random staff selection at one university, excluding faculty/IT; duplicates removed, N=1,945 (Methods p. 4; Results p. 7) |
| Outcome definition | Yes | Click tracking specified; no reporting or actual compromise outcome (Methods pp. 4, 7) |
| Confounding | Partial | Latin-square order balances four lures; single thematic family, one story and one advice text, unequal exposure windows (Methods pp. 4–6) |
| Measurement | Partial | Link clicks instrumented; pretests for realism and lesson coverage, but no independent behavioral ground truth (Methods pp. 4–6) |
| Analysis | Partial | Group denominators and omnibus p-value supplied; adjusted regression referenced but supplemental estimates not checked (Results pp. 7–8) |
| Generalization | Partial | Real staff inboxes, but one institution, IT-themed lures and only clickers eligible for post-training analysis (Methods/Discussion pp. 4, 8–9) |
| Ethics/reproducibility | Partial | IRB approval, privacy controls, no advance consent/debrief; materials linked, supplemental regression unreviewed (Methods pp. 6–7; Results p. 8) |

## Where this leaves the question

1. **Proposed test:** Compare expert- and peer-attributed advice and narratives with a prespecified interaction contrast, adequate power and multiple independently sampled examples of each message format. Do not assume a descriptive interaction is confirmed.
2. **Proposed measurement:** Separate subsequent clicks, legitimate-message false alarms, independent verification and reporting. A lower click count alone does not show that participants distinguish legitimate and malicious requests better.
3. **Proposed follow-up:** Use unfamiliar contexts and equal follow-up opportunities to examine whether any training-source effect persists beyond one organization and one family of IT-themed lures.

This is a source-grounded methodological note, not a claim that the repository owner personally read or endorsed the paper. No proprietary algorithms, scoring rules, implementation architecture, confidential data or participant records are included.
