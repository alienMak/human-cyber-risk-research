# When training effects last for months, what has actually been retained?

**Date added:** 26 October 2026. **Review type:** Focused scoping-review appraisal, not a systematic review or an account of research performed by the repository owner.

**Primary sources and access**
- Benjamin Reinheimer et al., [An investigation of phishing awareness and education over time: When and how to best remind users](https://www.usenix.org/system/files/soups2020-reinheimer_0.pdf), SOUPS 2020, pp. 259–284; [conference record](https://www.usenix.org/conference/soups2020/presentation/reinheimer), DOI [10.5555/3488905.3488920](https://doi.org/10.5555/3488905.3488920). **PEER-REVIEWED; FULL TEXT APPRAISED**, particularly §§3–7, Figures 1 and 3–5, pp. 261–270.
- Benjamin Berens, Katerina Dimitrova, Mattia Mossano and Melanie Volkamer, [Phishing awareness and education – When to best remind?](https://www.ndss-symposium.org/wp-content/uploads/usec2022_23075_paper.pdf), USEC 2022, 28 April 2022, DOI [10.14722/usec.2022.23075](https://doi.org/10.14722/usec.2022.23075). **PEER-REVIEWED WORKSHOP PAPER; FULL TEXT APPRAISED**, especially §§IV–VI, Tables I–II, pp. 3–9.
- Grant Ho et al., [Understanding the Efficacy of Phishing Training in Practice](https://doi.org/10.1109/SP61157.2025.00076), IEEE S&P 2025 (conference 12–15 May 2025). **PEER-REVIEWED; ABSTRACT-ONLY for this checkpoint**. The publisher abstract describes an eight-month randomized workplace study with ten campaigns and more than 19,500 employees. Its operational endpoints must not be pooled with screenshot-classification scores.

**Deduplication:** Reinheimer 2020 was already indexed in the evidence matrix at abstract level and listed as a full-text priority. Berens 2022 was not found by author/title in the matrix or screening register. Berens adapts the earlier teaching content and measurement approach; it is a distinct sample and publication, not an independent test of transfer to actual inbox decisions. No preprints, news reports or podcasts were used as empirical evidence in this note.

## Reinheimer et al. (2020): what was studied

**Design and sample.** A German public-administration organization with approximately 2,200 employees introduced a mandatory, instructor-led awareness program. Participation in the *evaluation* was voluntary. Employees were assigned across offices to separate measurement groups, mostly between-subjects; a subset of reminder recipients was linked between months six and twelve. Of 439 survey completions, four all-phishing responders and 26 participants who reported external assistance were excluded, leaving **409 analyzed participants**. The paper does not provide participant-level demographic data because of workplace privacy constraints. See §§3, 5.3, 5.6 and 6.1; Figure 1 (pp. 261, 264–267).

**Intervention and comparison.** The mandatory tutorial covered general security, phishing and passwords. The phishing material was adapted to the organization. Survey groups were tested before, immediately after, and at four, six, eight or twelve months; at six months separate groups received one of four short reminders (text, shortened text, video or interactive email examples). There was no concurrent randomized no-training arm for the initial tutorial. Assignment to timing/reminder groups helps comparability but does not eliminate voluntary-response bias or external changes. See §§4–5 and Figure 1 (pp. 261–266).

**Operational outcome.** Participants classified **20 screenshots, ten phishing and ten legitimate**, while security identification was explicitly their main task. The study used signal-detection sensitivity (d-prime) to represent discrimination and criterion to represent response tendency, plus separate phishing and legitimate hit rates. Screenshots displayed the link destination without requiring a real hover or a reporting decision. This is **classification under test conditions**, not clicks, real reporting, credential disclosure or incident prevention. See §§5.2, 5.4–5.5, 6.2 (pp. 264–267).

**Results.** Mean sensitivity was 1.11 before training, 2.13 immediately afterward and 1.60 at four months. The immediate and four-month groups differed significantly from baseline (reported p<.001 and p=.034); the six- and eight-month comparisons did not show significant improvement. The overall between-group ANOVA was F(4,227)=5.457, p<.001, omega-squared=.093. A nonsignificant result at six months **does not establish that every participant's learning disappeared at that point**. See §6.3 and Figure 3 (pp. 267–268).

At six months, the full-text, video and interactive reminders each differed from the original pre-training baseline in sensitivity, whereas the shortened-text reminder did not. The authors reported **no statistically significant difference among the three qualifying reminder formats** in their direct comparison (§6.4, p. 268). In the twelve-month linked subset, reported group sizes were 20 without reminder, 17 text, 17 video and 12 interactive. The paper reports text, video and interactive reminder groups all significantly above the original pre-training baseline in the relevant post-hoc comparison, although the authors' concluding preference emphasizes video and interactive examples (§6.5, p. 268; §7.2, p. 269). The results do **not** prove video is superior to text or establish a universally optimal six-month schedule.

**Confounds and limitations.** The organization was one technically oriented public-sector workplace; survey participation was voluntary and demographic covariates unavailable. Different instructors taught sessions. A 50:50 phishing/legitimate screenshot task made security the explicit goal, unlike normal inbox work. Link destinations were pre-displayed; real verification, reporting and help-seeking were not measured. Excluding people who sought outside help was consistent with the assessment instructions, but removes a behavior that could be appropriate in actual work. Four all-phishing responders were also removed, which matters when interpreting response tendencies. The interactive condition had a shorter required engagement time than planned due to a technical error. The month-twelve linked subsets were small. See §§5.2, 6.1, 7 and 7.5 (pp. 264–270).

## Berens et al. (2022): a related five-month check

**Design and population.** A separate German university study adapted the earlier content into self-paced e-learning with mandatory exercises after chapters. **46** students started, **20** completed all phases and only **16** could be linked reliably across the pre-test, post-test and five-month follow-up. Participants were recruited through university channels, compensated, and were not randomly assigned to training versus no training. The same screenshot items were shown at all three times in different orders. See §§III–IV, V.A (pp. 2–5).

**Measured outcome and results.** The primary outcome was again classification of phishing versus legitimate email screenshots, analyzed with sensitivity and response criterion, not actual inbox action. For the 16 linked participants, overall correct classification was **71.63% pre**, **90.81% immediately after** and **89.34% at five months**; reported sensitivity was **1.28**, **2.66** and **2.47** respectively. Pre-to-post and pre-to-five-month sensitivity comparisons were significant; post-to-five-month was not (reported p=.292). See §V.B–C, Table I (p. 5).

**Limits.** Severe attrition, a tiny final sample, repeat exposure to the *same* classification items, absence of an untrained comparator, security-focused task conditions and differences from the 2020 workplace sample prevent causal claims about durable generalized learning. The authors themselves acknowledge repeated screenshots as a possible explanation (§VI, pp. 7–8). The paper is a related follow-on in a different setting, **not proof that a six-month reminder interval is universally correct**.

## Eight-domain appraisal

| Domain | Reinheimer 2020 | Berens 2022 |
| --- | --- | --- |
| Research design | **Partial:** timing/reminder groups; no concurrent no-tutorial control (§§5–6) | **Partial:** repeated measures without an untrained comparison (§IV) |
| Sampling | **Partial:** 409 voluntary evaluators from one employer; demographics unavailable (§§3, 5.3, 6.1) | **Partial:** 16 linked students from 46 starters (§V.A) |
| Outcome definition | **Yes for classification; no for behavior:** sensitivity, criterion and hit rates, no real reporting (§§5.4, 6.2) | **Yes for classification; no for behavior:** same type of judgment task (§§IV–V) |
| Confounding | **Partial:** instructors, group composition, external events and selected follow-up (§§5, 7) | **Limited:** practice with repeated items, attrition, self-selection and no control (§§IV, VI) |
| Measurement | **Partial:** 20 screenshots and a known 50:50 base rate; no ordinary inbox interaction (§5.4) | **Partial:** repeated screenshot test; known task and limited realism (§§IV, VI) |
| Analysis | **Partial:** group ANOVA and post-hoc comparisons; limited precision for linked subsets (§6) | **Partial:** repeated-measures ANOVA and paired tests; n=16 (§V) |
| Generalization | **Limited:** one public employer, deliberately security-focused task (§7.5) | **Limited:** small university sample, e-learning and repeat testing (§VI) |
| Ethics/reproducibility | **Partial:** workplace council approval and anonymization; no independent raw-data reanalysis (§5.6) | **Partial:** informed consent and pseudonymous linking; no independent raw-data reanalysis (§IV.F) |

## What follows, and what does not

**Authors' findings:** Reinheimer et al. observed stronger screenshot discrimination soon after instruction and at four months, but not a statistically significant difference from baseline at six or eight months. Berens et al. observed improved classification on repeated items at five months among 16 linked students. Ho et al.'s publisher abstract reports limited practical benefit from common enterprise training on simulated-phishing outcomes, a *different* behavioral endpoint.

**Analysis:** Retaining a better classification score on familiar or constrained stimuli is not the same as retaining a safer response to an unfamiliar request during ordinary work. Moreover, an absence of statistical significance is not a directly observed moment of forgetting. The two earlier studies are valuable precisely because their outcome and task conditions are explicit; they should not be treated as evidence that any training format prevents real-world compromise.

**Proposed future tests (not conducted):**
1. Compare performance on familiar and *new, independently characterized* messages at delayed follow-up, without interpreting reuse of identical items as transfer.
2. Measure discrimination, response tendency, verification/reporting and consequential actions separately; include legitimate requests so that a shift toward general suspicion is not mistaken for better detection.
3. Test reminder timing across multiple settings with a contemporaneous comparison group and sufficient retention, rather than adopting six months as a fixed causal threshold.

**Open audit issues:** The 2020 paper's six-month null comparison is not an equivalence test; the 2022 five-month study has only 16 linked participants and repeated stimuli. Full-text methodological comparison of the 2025 IEEE workplace experiment remains outstanding.

**Public-IP check:** This note contains public bibliographic material, published study methods and generic future research questions only. No proprietary algorithms, scoring weights, private implementation or architecture, confidential organizational material, credentials, unpublished results or actual participant records.
