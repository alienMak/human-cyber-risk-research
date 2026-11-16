# When reporting improves, what happens to false alarms?

**Paper:** [Caputo, Danley & Ratcliff, *Employee risk recognition and reporting of malicious elicitations: longitudinal improvement with new skills-based training*](https://doi.org/10.3389/fpsyg.2024.1410426)  
**Published:** 31 July 2024, *Frontiers in Psychology* 15, article 1410426  
**Type:** Peer-reviewed primary empirical study  
**Review date:** 16 November 2026  
**Access:** **FULL TEXT APPRAISED**; original [publisher HTML](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1410426/full), §§1–4, Tables 2–6, and ethics/data statements. Supplementary/raw data not independently analyzed.

## What the authors investigated

A randomized, two-group longitudinal workplace experiment recruited **72 volunteers at MITRE**, 36 per group. Recruitment favored employees with public-facing or networking activity; three left the organization during follow-up (§2.1, Table 2). Both groups received the same awareness slides. The skills-based group additionally received approximately five weeks of practice with simulated suspicious and benign professional-networking messages, plus periodic personalized feedback; the comparison group did not (§2.3). Thus, this compares a **package of practice, additional exposure, time and feedback** against slides alone, not feedback as an isolated ingredient.

The researchers created 40 messages, piloted them with 41 other employees, and selected 26 for practice and testing, including malicious and benign communications (§2.2.1). Participants received messages through their usual work channels, with some SMS exposure. During the approximately 12-month test period, reporting to organizational security channels and replying to messages were recorded. The authors defined **correct malicious reporting**, **benign-message reporting (false alarms)** and **replying** separately (§§2.3–3.3). Reporting is an observable action, but is not equivalent to all forms of recognition or to prevention of actual compromise.

## Findings checked in the full text

Across test occasions, the authors report a higher rate of reporting malicious messages in the skills-based group than in the awareness-only group: **54.7% versus 31.0%** (Table 5; §3.3.1). Their repeated-measures GEE estimates an overall group association of **OR 2.58, 95% CI [1.42, 4.68], p=0.002** (§3.3.1). At the final reported occasion (week 54), rates were **42.9% versus 17.6%**, but that single occasion should not be treated as a continuous year-long effect estimate (Table 5).

The trade-off matters. The skills-based group also reported **more benign networking messages**: the adjusted analysis reports **18.2% versus 8.5%**, p=0.042 (§3.3.2); Table 6 gives a separate overall descriptive aggregation of 20.0% versus 8.3%. These are different summaries and should not be silently merged. The authors' signal-detection comparison favored the skills-based group, but their weighting and transformation choices warrant independent methodological scrutiny (§3.3.3). Replies to malicious messages were uncommon; the adjusted difference in replies was not statistically conclusive (p=0.085, §3.3.1). Therefore the evidence most directly supports improved **reporting of simulated malicious messages**, not a proven reduction in actual data disclosure.

## Eight-domain appraisal

| Domain | Judgment | Evidence and caution |
| --- | --- | --- |
| Research design | **Partial** | Random assignment improves comparison, but practice, feedback, extra exposure and time were bundled (§2.3; §4.2). |
| Sampling | **Partial** | Single employer, self-selected networking-oriented volunteers, N=72; three attritions (§2.1, Table 2). |
| Outcome definition | **Yes** | Malicious reporting, benign false alarms and message replies separated (§§3.1–3.3). |
| Confounding | **Partial** | Prior reporting, tenure, gender and clearance considered; unequal training exposure and one accidentally blocked test message remain (§§3.3.1, 4.2). |
| Measurement | **Partial** | Workplace reporting captured, messages pilot-rated; detailed pilot calibration not available in the article (§2.2.1). |
| Analysis | **Partial** | GEE, regression, confidence intervals and occasion-specific estimates; small sample, multiple occasion tests, and differing aggregate estimators require caution (§3.3, Tables 5–6). |
| Generalization | **Partial** | Relevant work-context messages, but specialized employee population and security reporting infrastructure (§§2.1, 4.2). |
| Ethics/reproducibility | **Partial** | IRB and consent reported; raw data available only on request subject to funding-agency approval (Statements). |

## What can and cannot be concluded

**Authors' finding:** Skills-based training with practice and feedback improved reporting of simulated malicious elicitation messages compared with slides alone, including at the final 12-month test occasion. It also increased some false alarms.

**Analysis:** The added reporting benefit cannot be attributed specifically to feedback, repetition or practice without a time/exposure-matched comparator. A larger reporting count alone could reward indiscriminate reporting. The missed malicious test delivery in one arm and the limited single-employer sample also constrain interpretation.

**Proposed future tests, not implemented methods:**

1. Compare active practice plus feedback with an equal-time exposure condition to separate rehearsal from feedback.
2. Include legitimate and suspicious messages, reporting opportunities and independent verification outcomes; track correct reports and false alarms together.
3. Use unfamiliar messages at delayed follow-up to distinguish durable discrimination from remembering the training examples.

## Comparison and source status

[Bender et al. (first online 2024; 2026 issue)](https://doi.org/10.1017/bpp.2024.19) is **previously full-text appraised** in this repository and concerns just-in-time phishing feedback in a different setting; it is not a replication of this study. [Jensen et al. (2022)](https://doi.org/10.1080/07421222.2022.2096551) is **ABSTRACT-ONLY for this comparison**, addressing gamified reporting incentives and possible false alarms. [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) remains **ABSTRACT-ONLY**; the large publisher PDF was not read. No preprints, news or podcasts are used to corroborate the empirical estimates above.

This note is a public literature appraisal only. It contains no application implementation, proprietary scoring, unpublished methods, participant records or organizational confidential information.
