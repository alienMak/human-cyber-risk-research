# Does peer-delivered phishing training transfer across populations?

**Paper:** [Marsden et al., *Facts and Stories in Phishing Training: A Replication and Extension*](https://doi.org/10.1145/3334480.3381435)  
**Authors:** John Marsden, Zachary Albrecht, Paula Berggren, Jessica Halbert, Kyle Lemons, Anthony Moncivais and Matthew Thompson  
**Publication:** CHI 2020 Extended Abstracts, Student Research Competition, pp. 1–6, April 2020  
**Type:** ACM conference extended abstract; empirical field replication/extension, not a full-length journal paper  
**Access:** **FULL TEXT APPRAISED**, author-uploaded six-page paper, Methods, Results, Discussion and Conclusion, pp. 3–6; [author-uploaded full text](https://www.researchgate.net/publication/341783825_Facts_and_Stories_in_Phishing_Training_A_Replication_and_Extension)  
**Review date:** 18 November 2026

## What the authors investigated

Marsden and colleagues adapted [Wash and Cooper (2018)](https://doi.org/10.1145/3173574.3174066) from university staff to students. They randomly selected 2,000 students from roughly 4,500 at Abilene Christian University, assigned five conditions (expert facts, expert story, peer facts, peer story, no-training control), and retained 1,968 after 32 withdrawals. Four simulated phishing messages arrived on days 0, 2, 7 and 30, with email order counterbalanced by a Latin-square schedule. A click led to the assigned training page once; subsequent clicks were observed without repeated training. The apparent expert and peer were represented by named, pictured local individuals. The intervention was a training presentation, not an independently verified change in knowledge or risk. **Outcome:** clicks on simulated phishing links, including clicking again after an initial click. No legitimate-email discrimination, reporting, credential disclosure or actual compromise outcome was measured (Methodology, pp. 3–4).

## What the authors reported

Across retained participants, 64.43% clicked at least once; campaign click percentages declined from 43.14% to 12.80% across the four sends (Results, pp. 3–4). Those trends alone cannot establish learning because messages and exposure order also changed.

Table 2 (p. 5) reports repeat-click proportions *among people who clicked* of 149/246 (60.5%) in control, 109/256 (42.5%) for expert facts, 113/261 (43.3%) for expert story, 94/244 (38.5%) for peer facts, and 80/261 (30.6%) for peer story. The authors also report a pooled expert-versus-peer comparison of 28.17% versus 22.11%, t(1563)=2.778, p=.006, with Cohen's d=.140, a very small effect (Results, p. 4). They conclude peer-presented material was associated with fewer repeat clicks among students, unlike their reading of the earlier staff study; they found no overall story-versus-facts difference (Conclusion, p. 6).

**Numerical and analytic caution:** Table 2's conditional denominators are not the same as the reported pooled percentages, and its five 'Clicked' counts total 1,268, not the full retained sample. Table 1 categories as printed sum to more than 1,968 (700+723+545+48=2,016), so they cannot be interpreted as mutually exclusive participant counts. The article prints some p-values as zero, which is not an exact probability. Its t-test degrees of freedom and repeated observations are not sufficiently explained in the six-page report to independently confirm participant-level independence or reconstruct the tests. Do not combine these estimates into a single causal effect or silently correct the inconsistencies.

## Eight-domain quality appraisal

| Domain | Judgment | Evidence and concern |
| --- | --- | --- |
| Research design | Partial | Five-arm assignment and counterbalanced lures, but click-triggered training and limited causal analysis (Methodology, p. 3) |
| Sampling | Partial | Random student selection at one private university; 32 withdrawals; not representative of all students (pp. 3–4) |
| Outcome definition | Partial | Simulated link clicks observed; no reporting, legitimate-message controls or actual compromise (pp. 3–5) |
| Confounding | Partial | Email order counterbalanced; baseline exposure, differing click opportunities and institutional context remain (pp. 3–5) |
| Measurement | Partial | Click logging described, but no independent validation of behavioral transfer (p. 3) |
| Analysis | Partial | Reported tests and tiny standardized effect; table inconsistency and repeated-measures uncertainty remain (pp. 4–5) |
| Generalization | No | One campus, student-specific social identities, four email lures; cannot extrapolate to employees or other channels (pp. 3–6) |
| Ethics and reproducibility | Partial | IRB/IT involvement, debriefing, withdrawal and no password collection described; no independently inspected dataset or analysis code (p. 3) |

## Interpretation and research questions

**Author finding:** The observed student pattern favors peer-presented training; the authors propose that student identification with peers might explain the difference. This explanation was not directly tested.

**Analysis:** The result is not a clean contradiction of Wash and Cooper. The populations, campus environments, message exposure and analysis may differ. The earlier Wash and Cooper five-group omnibus comparison was not statistically significant (see [17 November appraisal](2026-11-17-training-source-and-nonsignificant-click-differences.md)). A third-party replication-atlas label of 'failed' is not itself a statistical test of the original interaction.

**Proposed future tests, not implemented methods:**
1. Randomize source identity independently of content and test the source-by-population interaction in a preregistered study with adequate power.
2. Distinguish subsequent clicks from correct rejection of legitimate requests, reporting and verification, with unfamiliar matched messages at follow-up.
3. Measure whether perceived credibility or identification with the presenter mediates behavior rather than assuming age or peer status explains it.

**Boundary:** This is a source-grounded appraisal of a public paper, not evidence of any completed private platform experiment. No private scoring, architecture, participant records or proprietary mechanisms are described. No preprints, news or podcasts were used as primary empirical corroboration.
