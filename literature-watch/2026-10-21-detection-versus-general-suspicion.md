# Is rejecting suspicious email evidence of discrimination, or just suspicion?

**Source:** Casey Canfield, Alex Davis, Baruch Fischhoff, Alain Forget, Sarah Pearman and Jeremy Thomas, [Replication: Challenges in Using Data Logs to Validate Phishing Detection Ability Metrics](https://www.usenix.org/system/files/conference/soups2017/soups2017-canfield.pdf), SOUPS 2017, pp. 271–284.  
**Type:** Peer-reviewed primary research. **Access:** FULL TEXT APPRAISED, §§3–5 and Tables 1, 3, 6–8. **Recorded:** 21 October 2026.  
**Prior coverage:** Not listed as a standalone entry in the evidence matrix at this review; Nicholson et al. (2017), a separate signal-detection paper, was already listed. No claim of exhaustive repository-wide deduplication.

## What the authors actually tested

The study replicated an earlier phishing-judgment experiment with participants from the Security Behavior Observatory (SBO), a longitudinal study of home-computer use. Participants judged 38 emails, half phishing, for a fictional recipient. They separately answered whether each message was phishing, what action they would take, their confidence and perceived consequences (§3.1, p. 273). They first saw a short phishing-education comic. The unusually high phishing proportion was deliberate and differs sharply from ordinary inbox exposure.

The authors distinguished *sensitivity* (discriminating phishing from legitimate emails) from *response bias* (a general tendency to say phishing or avoid links). Stated actions in the email task were not observed real inbox actions. To test external relevance, the researchers compared experimental results with observational indicators from participants' home computers: malicious URLs, installed malware and malicious files (§3.3, pp. 273–274). These indicators are imperfect proxies for actual phishing victimization.

The authors recruited 132 eligible SBO participants; 98 finished the experiment and five were excluded for insufficient logged data, leaving 93 (§4.1, p. 276). The SeBIS comparison involved 84 participants (§3.2, p. 273). The sample was drawn from local volunteer pools with many retirees and students, not a representative workplace cohort (§3.4).

## Findings and interpretation

The replication sample's detection sensitivity was similar to that of the original online sample: mean 0.96 in both groups; behavior sensitivity was 0.42 in the SBO sample and 0.39 in the original sample (Table 3, p. 277). Similar experimental averages do not imply equivalent real-world risk.

Only one of four signal-detection parameters correlated substantially with the proactive-awareness subscale of the Security Behavior Intentions Scale: behavior response bias, r=-.29, p=.008 (§4.3, p. 279). The authors did **not** find evidence that adding experimental signal-detection measures improved prediction of the observed computer-security outcomes (§4.4, pp. 279–281). This is a null finding within a limited sample and with indirect outcomes, not proof that no phishing judgment task can predict future phishing behavior.

## Eight-domain critical appraisal

- **Design — Partial:** useful replication and observational validation attempt; not an intervention or prospective prediction of actual phishing incidents (§§3–4).
- **Sampling — Partial:** 93 retained volunteer participants, restricted population (§§3.4, 4.1).
- **Outcomes — Partial:** detection and stated behavior clearly separated; logged security outcomes do not uniquely identify phishing compromise (§§3.1, 3.3).
- **Confounding — Partial:** exposure and computer-use covariates considered; device protection, attack exposure and the artificial 50% phishing prevalence remain material (§§2.2, 3.3, 4.4).
- **Measurement — Partial:** documented stimuli and indicators, but scanner classifications and incomplete browser visibility introduce uncertainty (§§3.1, 3.3).
- **Analysis — Partial:** replication comparisons, confidence intervals and logistic models documented; limited power for rare observed outcomes (§§3.5–3.6, 4).
- **Generalization — Limited:** fictional inbox judgments and home-computer logs cannot establish workplace or cross-channel predictive validity (§§3.1, 3.4, 5).
- **Ethics/reproducibility — Partial:** IRB approval and published task materials/analysis references; no independent reproduction of raw logged data claimed (§§3.4–3.5).

## The research question that follows

**Authors' finding:** Controlled phishing-judgment performance replicated reasonably well, but did not demonstrate predictive validity for the available logged computer-security outcomes.

**Analytical reading:** Someone who calls every email suspicious might avoid phishing but also reject legitimate work. Discrimination and generalized caution are different claims. A measure can look consistent across samples without predicting the external outcome of interest.

**Proposed test, not completed:** Evaluate legitimate and suspicious requests together, report both missed threats and mistaken rejection of legitimate requests, and check whether judgment performance predicts later consented verification and reporting. Account for differences in exposure and message difficulty before drawing individual-level conclusions.

This note contains only public research findings and general questions. No private methods, scoring weights, architecture, confidential data or actual participant records are disclosed.
