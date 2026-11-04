# Does a phishing simulation measure behavior while also changing how employees feel about security?

**Paper:** [Schöps, Gutfleisch, Wolter & Sasse, *Simulated Stress: A Case Study of the Effects of a Simulated Phishing Campaign on Employees' Perception, Stress and Self-Efficacy*](https://www.usenix.org/system/files/usenixsecurity24-schops.pdf)  
**Publication:** USENIX Security 2024, August 2024, proceedings pp. 4589–4606  
**Type:** Peer-reviewed primary empirical paper  
**Review status:** FULL TEXT APPRAISED, original 19-page proceedings PDF, §§3.1–3.6, 4.1–4.3, 5 and Table 1  
**Review date:** 4 November 2026

## What the authors investigated

This mixed-methods case study accompanied an unannounced phishing simulation at one multinational manufacturing company with more than 16,000 employees. Three English-language lures were randomly distributed in January 2023. Of employees reached, 4,520 clicked (26.8%) and 3,034 reported through a recently introduced one-click button (18.0%). Other reporting channels were not captured. Only those who clicked or used that reporting button were invited to the survey. Of 7,554 eligible employees, 408 (5.4%) responded: 309 clickers and 99 reporters. Twenty-one employees participated in semi-structured interviews; 281 provided open-ended survey answers, of which 268 were interpretable (§§3.1–3.3, 4.1–4.3).

The comparison was **observational**, not randomized between clicking and reporting. The intervention was the employer's phishing simulation, including immediate disclosure and brief training after a click; the study did not compare this against an unexposed control group or collect a true pre-simulation baseline. Clickers saw an invitation on the disclosure page; reporters saw a congratulatory pop-up and a survey invitation. These **different feedback and recruitment experiences** complicate interpreting the group contrast (§§3.1–3.2).

Operational outcomes: click and one-click report were campaign logs; *stress now* and *average workday stress* were single-item self-reports on 1–10 scales; perceived change in stress was retrospective on a five-point scale; phishing self-efficacy was a four-item 1–5 agreement scale (Cronbach's alpha .86). The study also measured perceived importance/effectiveness of interventions and qualitatively coded interviews and open responses (§§3.3–3.4, 4.1). Reporting is not a verified indicator of correct discrimination on legitimate messages, and the survey does not independently measure future behavior.

## Findings and interpretation

**Authors' results:** Responding clickers reported greater immediate stress (mean 5.40 vs 3.39) and lower phishing self-efficacy (3.56 vs 4.10) than responding reporters; both adjusted p < .001 in Table 1. Average workday stress differed less (5.50 vs 4.81; adjusted p = .050). The authors used Mann–Whitney U tests with Holm adjustment (§§3.4.1, 4.1). These are *between-group associations*, not causal estimates of a simulation's effect. Among 268 interpretable open responses, 224 (83.6%) described the campaign as effective, which measures perceived effectiveness rather than demonstrated prevention (§4.2.1).

**Analysis:** An exercise can generate both a recorded decision and a reaction to discovering the result. Those outcomes should not be collapsed into one claim about learning. The difference in survey feedback between clickers and reporters is a plausible alternative explanation for some post-interaction differences, alongside pre-existing confidence and stress.

## Eight-domain quality appraisal

1. **Question/design:** Clearly defined descriptive and group-comparison questions; no randomization of the groups being compared.
2. **Selection:** Only clickers/button-reporters eligible; 5.4% survey participation, strong volunteer/nonresponse concern.
3. **Measurement:** Observed click/button-report events; stress and self-efficacy self-reported after the event; no true baseline.
4. **Comparison:** Click versus report, without non-interactors, alternate reporting methods or no-simulation control.
5. **Confounding:** Pre-existing security confidence, role, lure type, language, baseline stress, and different feedback may affect results; demographics not collected.
6. **Analysis:** Nonparametric tests with multiple-testing correction; self-efficacy reliability reported; no causal adjustment for the listed confounders.
7. **Transfer:** One employer and one campaign; cannot establish long-term effects or generalize to other organizations or attack vectors.
8. **Transparency/ethics:** Study describes work-council/privacy approvals and a replication package with instruments/codebooks (§§3.4–3.6, Appendix); raw individual campaign outcomes not independently reanalyzed here.

## What remains unresolved

The study cannot tell whether clicking *caused* distress, whether more stressed people were likelier to click, or whether the immediate corrective message shaped survey responses. The respondents are a small, selected subset, and employees who ignored the message are missing. The authors acknowledge these limits in §3.5 and §5. A further caution: Table 1 reports a mean of 0.25 and -0.23 for a variable described earlier as a 1–5 perceived-change scale; the table apparently uses a centered representation, but its transformation should be checked before numerical reuse (§3.3.1, Table 1). No causal or clinical interpretation is justified.

## Where this leaves the research question

1. **Proposed test:** In an ethically consented evaluation, measure stress and confidence *before* a simulation and after feedback, with a suitable comparison condition. This could separate pre-existing differences from reactions to feedback.
2. **Proposed test:** Record reporting opportunities and alternate reporting channels, including participants who neither click nor report. Otherwise a report-versus-click comparison misses important decisions.
3. **Proposed test:** Examine whether short-term discomfort predicts subsequent verification, disengagement or help-seeking in unfamiliar situations, rather than treating discomfort or self-efficacy alone as a security outcome.

These are proposed questions, not completed experiments or claims about any proprietary platform. No preprints, news or podcasts are used as empirical evidence in this appraisal.