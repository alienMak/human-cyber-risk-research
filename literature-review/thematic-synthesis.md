# What ten years of research is telling me so far

I keep coming back to a distinction that is easy to lose in security awareness discussions: recognizing something suspicious is not necessarily the same as responding safely when the environment is working against you.

This review covers work from 2016 through October 2026, but the evidence matrix is still being expanded. These are provisional cross-study interpretations of the sources currently screened, not a systematic verdict on the entire field.

## Training can improve performance without establishing durable behavioral change

Reinheimer and colleagues reported that improvements in email identification persisted for several months but were no longer significant at six months. In contrast, substantial operational studies published in 2025 question whether conventional phishing awareness training changes outcomes in realistic campaigns. They do not measure identical interventions or endpoints. That is the key methodological point: training recall, simulation clicking, reporting, and transfer to a different attack are distinct outcomes.

## Difficulty matters

The NIST Phish Scale work suggests that a changing click rate can reflect a harder or easier lure rather than a corresponding change in people. I would want simulation difficulty and context recorded before comparing behavior over time. Otherwise a trend line can look more meaningful than it really is.

## The surrounding environment matters

The SOUPS work on social salience, organizational motivations, and SMiShing all points toward decisions being shaped by signals beyond message content alone. Sender presentation, expectations, colleague norms, workload, and reporting friction deserve closer attention. Not all these studies establish causality, and many involve small or context-specific samples.

## Interactivity is promising, but outcomes must be named

The role-playing experiment and later feedback-design work give reasons to study interactive learning. But it would be a mistake to treat improved self-efficacy, support-seeking intentions, reporting, and reduced phishing susceptibility as interchangeable evidence of effectiveness.

## A defensible research direction for VISHWAR

The question is not whether VISHWAR has a better score than traditional training. The stronger question is whether well-designed simulations can capture *additional, interpretable behavioral evidence* across scenarios and over time. That requires measuring scenario difficulty, distinguishing exposure from generalization, keeping outcomes separate, and validating any composite measurement rather than assuming the formula gives a ground truth.

## Key source anchors

- [Nicholson et al. (2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson)
- [Reinheimer et al. (2020)](https://www.usenix.org/conference/soups2020/presentation/reinheimer)
- [Steves et al. (2020), NIST](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final)
- [Chen et al. (2024)](https://www.usenix.org/conference/soups2024/presentation/chen)
- [Rozema and Davis (2025)](https://arxiv.org/abs/2506.19899)
- [Understanding the Efficacy of Phishing Training in Practice (2025)](https://doi.org/10.1109/SP61157.2025.00076)
- [Spicer and Nurse (2026)](https://doi.org/10.1016/j.cose.2026.105096)

## The gap between knowing and doing has appeared for a decade

The 2016 password-reuse field study is a reminder that stated intention and observed behavior can diverge, even when people can explain good practice. The 2018 password-expiration work adds another complication: repeating security advice can make it familiar and convincing without necessarily making it well supported.

That gives VISHWAR a useful measurement principle. A participant's explanation of the right choice, their choice inside a simulation, and their choice in an ordinary setting should be treated as separate evidence, not three interchangeable signs of awareness.

Sources: [Wash et al. 2016](https://www.usenix.org/conference/soups2016/technical-sessions/presentation/wash); [Habib et al. 2018](https://www.usenix.org/conference/soups2018/presentation/habib-password).

## Security cues require interpretation, not just visibility

Drury and Meyer's 2019 certificate analysis challenges the old habit of treating HTTPS as proof a site is trustworthy. In 2022, Zheng and Becker found that exposing email headers alone did not improve participants' phishing detection. Their 2023 follow-up explored checking controls and nudges, with a small formative evaluation.

The pattern is worth testing, but it is not proof that any one interface will solve phishing. A useful simulation should distinguish whether the participant noticed a cue, understood what it meant, and chose an appropriate verification action.

Sources: [Drury and Meyer 2019](https://www.usenix.org/conference/soups2019/presentation/drury); [Zheng and Becker 2022](https://www.usenix.org/conference/soups2022/presentation/zheng); [Zheng and Becker 2023](https://www.usenix.org/conference/soups2023/presentation/zheng).

## Human-risk assessment should account for differing contexts

The 2021 research on non-expert phishing detection suggests people bring useful knowledge from their own contexts, not merely deficits to correct. The work on non-native English speakers shows how language and localization affect email handling. Accessibility research involving visually disabled participants points to barriers that can alter both perception of risk and the available response.

This raises a harder question for any organization-level or individual-level score: how much of a difference in measured behavior reflects the person, and how much reflects the environment or accessibility of the task?

Sources: [Wash et al. 2021](https://www.usenix.org/conference/soups2021/presentation/wash); [Hasegawa et al. 2021](https://www.usenix.org/conference/soups2021/presentation/hasegawa); [Napoli et al. 2021](https://www.usenix.org/conference/soups2021/presentation/napoli).

## An intervention has to be described precisely

Franz and colleagues' 2021 taxonomy separates user-oriented phishing interventions by attack vector, timing and user interaction. That is a practical warning against pooling unlike interventions under a single label such as “awareness training.” A simulation with feedback, a warning displayed during a task, and a reminder months later are different things. Their behavioral endpoints may also differ.

Source: [Franz et al. 2021](https://www.usenix.org/conference/soups2021/presentation/franz).

## Scope of these comparisons

These are connections drawn from screened conference summaries and abstracts, not a meta-analysis. Full-text appraisal, consistent outcome coding, and additional source coverage are still necessary before making field-wide claims.


## Detection, caution and real-world transfer: full-text checkpoint (23 October 2026)

Two newly appraised peer-reviewed papers make the distinction between *recognizing phishing* and *generally distrusting email* more concrete. In an online classification task with 145 Australian adults, [Sturman et al. (2024)](https://doi.org/10.1016/j.apergo.2024.104309) found that phishing knowledge was associated with more correct phishing labels **and** more genuine messages incorrectly labelled phishing; cue utilization was the only significant adjusted predictor of discrimination in their model (§§5–7, Tables 6–9). This was an observational task with known 50% phishing prevalence, not an intervention or a reporting study. The paper's printed decision-criterion expression also requires clarification before independent numerical reuse; see the [appraisal](../literature-watch/2026-10-23-classification-errors-and-reasonable-reporting.md).

[Morrison et al. (2025 issue; first online 27 October 2024)](https://doi.org/10.1177/15553434241296170) compared a 40-email controlled task with two analyzed simulated inbox messages in 94 university students. Lower cognitive reflection was associated with more false-positive classifications in the controlled task, but cue-utilization and reflection groupings did not significantly predict engagement with either inbox message (*Results; Limitations*). The small sample, prior warning, 50:50 controlled-task base rate and limited field observations mean these null findings cannot settle whether a measure transfers to workplaces.

**Synthesis, not an authors' combined result:** Incorrectly classifying a genuine email as phishing is not automatically the same as making an unreasonable decision to *report* an uncertain message. The studies measured classification or interaction, not whether reporting was justified with the information available at the time. A future consented evaluation should distinguish initial classification, reasonable verification or reporting, and final action, while considering both missed threats and unnecessary disruption. The older [Canfield et al. (2016)](https://doi.org/10.1177/0018720816665025) detection-versus-behavior paper was verified at **ABSTRACT-ONLY** level in this checkpoint, not independently appraised in full. No cross-study effect size is inferred.

## Difficulty adjustment is necessary, but calibration is not validation (24 October 2026)

A new [full-text appraisal of Steves, Greene and Theofanos (2020)](../literature-watch/2026-10-24-phishing-difficulty-and-click-rate-interpretation.md) strengthens the existing argument that click rates should be interpreted alongside message difficulty and the target audience's work context. The journal article applies its exploratory framework to ten NIST workplace campaigns. The earlier [USEC 2019 paper](https://doi.org/10.14722/usec.2019.23028) analyzes seven exercises from the same line of research, so it is not an independent replication. The 2020 authors report descriptive alignment with click rates, but also say the categories need validation using other messages and populations; the current corpus helped set the rating boundaries. Their contemporaneous reporting outcomes were unavailable. The journal's Table 13 additionally prints inconsistent denominators for the Valentine campaign, which should remain unresolved until checked against underlying records.

**Synthesis, not a new empirical result:** A difficult campaign can yield a high click rate without demonstrating that participants' underlying ability has deteriorated. Equally, a lower rate in a later campaign does not by itself demonstrate training retention. The next defensible comparison is between matched or independently characterized tasks, with recognition, reporting, interaction and disclosure kept distinct. The source supports this as a measurement caution, **not** as a validated cross-vector difficulty model or a causal account of learning.
