# Does a phishing simulation measure behavior while changing confidence?

**Paper:** Schöps, Gutfleisch, Wolter & Sasse, [Simulated Stress: A Case Study of the Effects of a Simulated Phishing Campaign on Employees' Perception, Stress and Self-Efficacy](https://www.usenix.org/system/files/usenixsecurity24-schops.pdf)  
**Publication:** USENIX Security 2024, pp. 4589–4606 (August 2024)  
**Type:** Peer-reviewed empirical conference paper  
**Access:** FULL TEXT APPRAISED (original publisher PDF, §§3–5 and appendices)  
**Date added:** 21 October 2026

## What the authors investigated

A large manufacturing company sent three randomly allocated English-language simulated phishing messages to more than 16,000 employees in January 2023. The study recruited only employees who clicked a link or used the Outlook phishing-report button. Of 7,554 eligible interactions (4,520 clicks; 3,034 reports), 408 people completed an immediate voluntary questionnaire (309 clicked; 99 reported), and 21 employees participated in interviews. Employees who ignored messages or reported them through other channels were not included (§§3.1–3.2, pp. 4591–4592).

The study compared **observed interaction categories** (clicked versus reported), **self-reported current and usual-day stress**, **retrospectively perceived stress change**, and a four-item **phishing self-efficacy** scale. The 1–10 immediate stress item asked about stress *at the time of answering*, not objectively measured physiological stress; self-efficacy was rated on a 1–5 agreement scale. There was no pre-interaction baseline and no randomized assignment to clicking versus reporting (§3.3, pp. 4592–4593). Random assignment concerned the phishing email variants, not the behavioral groups.

In Table 1 (§4.1, p. 4595), the clicked group reported greater current stress (mean 5.40 versus 3.39; adjusted p<.001, r=.288) and lower phishing self-efficacy (mean 3.56 versus 4.10; adjusted p<.001, r=.302). Authors used Mann–Whitney U tests with Holm correction; the self-efficacy scale had Cronbach alpha .86 (§4.1). The qualitative interviews and open responses add accounts of stress, relief and perceived competence (§§4.2–4.3), but cannot establish their population prevalence.

## What the comparison can and cannot show

The findings establish an association between interaction category and immediate self-reported stress/self-efficacy **among voluntary respondents**. They do not establish that clicking *caused* lower confidence or greater stress, nor that the campaign improved or harmed later detection. The clicked group saw a training page while reporters received a congratulatory pop-up, making the immediate feedback experience a plausible confound (§§3.1–3.2). Other reporting routes were not captured. Only 5.4% of eligible clickers/reporters answered, the study involved one company, and the authors did not observe long-term effects (§3.5, p. 4594).

## Eight-domain appraisal

| Domain | Assessment | Evidence |
| --- | --- | --- |
| Design | Partial: useful post-event observational comparison, not causal | §§3.1–3.4 |
| Sampling | Partial: one employer, voluntary response, 408/7,554 | §§3.2, 3.5 |
| Outcomes | Yes for distinguishing clicks, reports, stress and self-efficacy; other reporting channels omitted | §§3.1, 3.3 |
| Confounding | Partial: different feedback and recruitment routes, no pretest | §§3.2, 3.5 |
| Measurement | Partial: stated scales and self-efficacy reliability, retrospective change | §3.3; §4.1 |
| Analysis | Yes for specified group tests and multiplicity correction; no causal adjustment | §§3.4, 4.1 |
| Generalization | Limited: one organizational campaign, short-term response | §3.5 |
| Ethics/reproducibility | Partial: consent, anonymization, worker-council approval and questionnaire appendices; no independent raw-data replication claimed | §3.6; appendices |

## Where this leaves the question

**Authors' finding:** In this responding sample, clicking was associated with higher immediate stress and lower reported phishing self-efficacy than reporting.

**Analytical interpretation:** A click-rate-only evaluation misses how employees experience the exercise. The measured emotional difference might reflect prior confidence, the click itself, feedback framing, selection into the questionnaire, or a combination.

**Proposed future tests (not conducted):**
1. Measure confidence and stress *before* and *after* consented simulations, with comparable feedback and separate behavioral outcomes. Test whether changes persist beyond the immediate response.
2. Compare later reporting and verification after supportive versus neutral feedback while holding message difficulty and reporting access constant. Record correct handling of legitimate messages as well as suspicious ones.
3. Include non-interactors and alternative reporting routes so that a click/report dichotomy does not silently omit meaningful behavior.

This note describes published evidence and open methodological questions only. It does not specify any private scoring mechanism, architecture, weights, confidential organizational data or participant records.
