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

## Longitudinal retention is not behavioral transfer (26 October 2026)

A [full-text appraisal of Reinheimer et al. (SOUPS 2020)](../literature-watch/2026-10-26-training-retention-versus-behavior.md) clarifies an existing abstract-level claim. The 409-person workplace evaluation found better *screenshot classification sensitivity* immediately after instruction and at four months compared with the pre-training group, but not statistically significant improvement at six or eight months. This does **not** identify an exact forgetting point, since different volunteers were assessed at most time points and nonsignificance is not proof of no remaining effect. The paper did not measure actual clicks, reporting, verification or compromise. It also did not find a statistically significant difference among the three qualifying reminder formats at the immediate reminder comparison (§§5–7).

The related [Berens et al. (USEC 2022)](https://doi.org/10.14722/usec.2022.23075) university study found better five-month classification among **16 linked completers**, but repeated the same screenshot items at each measurement and lost many participants. That is evidence about a particular retained test performance, not an independent demonstration of generalized learning or a universally optimal reminder interval. The [Ho et al. (IEEE S&P 2025)](https://doi.org/10.1109/SP61157.2025.00076) publisher abstract describes limited effects of common training on operational simulated-phishing outcomes; **ABSTRACT-ONLY** here and not directly comparable to the earlier classification studies.

**Cross-study interpretation, not an authors' combined finding:** A durable improvement on an explicit security test may coexist with little change in routine inbox decisions. Future delayed evaluations should distinguish familiar from new stimuli, keep discrimination and response tendency separate, and measure help-seeking and actual response without assuming that a six-month calendar interval is itself a validated behavioral threshold.

## A small randomized benefit can coexist with weak engagement (27 October 2026)

The [full-text appraisal of Ho et al. (IEEE S&P 2025)](full-text-appraisals/ho-et-al-2025.md) adds an important qualification to the previous abstract-level comparison. In a single health system with 19,789 active employees, random assignment to embedded-training content produced lower adjusted odds of clicking than a 404-page control (OR 0.905, 95% CI 0.863–0.950), but the aggregate difference was only about **1.7 percentage points**. Across ten lures, observed failure rates varied from **1.82% to 30.80%**. Annual-training *recency* was observational and not significantly associated with later clicks (OR 0.998 per 30 days, p=.06); it was not a randomized comparison of training against none (§§3–5, Tables 1–2).

Training exposure and engagement also require their own denominators: only people who clicked encountered embedded material, and the study recorded an acknowledgment-button completion in 24% of sessions (§6, Tables 3–4). The better subsequent outcomes among interactive-session completers were **not** randomized by completion; self-selection remains possible (§6.2, Table 5). This sharpens, rather than overturns, the earlier distinction between classification gains, training exposure and field behavior. It also leaves reporting, verification, credential submission and actual incident prevention unmeasured.

**Research question, not a validated method:** Can a study separately establish whether a person received an intervention, engaged with it, recognized an unfamiliar request, and acted appropriately in an ordinary task? Future comparisons should preserve an independent control, account for task difficulty, and report absolute as well as relative changes. No single click or completion metric is a validated proxy for all these outcomes.


## Feedback can change short-term actions without identifying the mechanism (28 October 2026)

A [full-text appraisal of Bender et al. (first online 2024; 2026 journal issue)](../literature-watch/2026-10-28-feedback-timing-and-behavioral-outcomes.md) adds a randomized feedback-versus-none comparison to the existing evidence on training engagement. Among 992 employees who interacted with the first simulated lure, feedback was associated with **40% versus 50%** interacting with a second lure; the reporting difference (**19% versus 15%**) was **not statistically significant**. Among 8,697 employees who neither interacted nor reported initially, feedback was associated with **20% versus 22%** interacting and **10% versus 7%** reporting two weeks after the first lure (*Results*, pp. 534–536; Table 1). These are distinct subgroup comparisons, not a head-to-head experiment on immediate versus delayed feedback.

**Synthesis, not an authors' combined finding:** This does not negate [Ho et al. (2025)](full-text-appraisals/ho-et-al-2025.md), whose randomized embedded-training intervention had a smaller average effect in another health system. Intervention content, eligibility, exposure, baseline behavior and comparison conditions differ. Both papers leave recognition and durable transfer unmeasured. The open question is whether feedback changes recognition, willingness to report, or expectations about the consequences of reporting; a future controlled comparison would have to measure those outcomes separately and follow people beyond a single two-week reassessment.

## A verification aid can increase confidence without establishing accuracy (29 October 2026)

The [full-text appraisal of Zheng and Becker (SOUPS 2023)](../literature-watch/2026-10-29-verification-cues-and-workflow-friction.md) adds a closer look at the point between *seeing* security information and *using* it. In a formative study of 27 staff members using simulated inboxes, participants often relied on message relevance and perceived sender relationships. A suspicion warning and a simplified check of past correspondence were generally preferred over more technical details or a disruptive colleague-report warning (§§4.1–4.2, pp. 63–66). The study did **not** estimate changes in detection accuracy or real reporting behavior; the baseline inbox always came first, tools were revised across four cohorts, and the authors prioritized qualitative usability over statistical efficacy (§§3.2–3.4, pp. 59–62).

**Interpretation, not an authors' causal finding:** A control that reassures someone may fit their workflow better while still being wrong in particular cases. The authors themselves note that past correspondence could create false confidence when an established sender account is compromised or spoofed (§5.1, p. 67). The older [Nguyen et al. (2021)](https://doi.org/10.1111/isj.12318) publisher abstract describes 438 participants assessing mock crowdsourced warnings and reports that warning accuracy mattered for judgment and adherence, but that paper is **ABSTRACT-ONLY** in this checkpoint. Its results should not be pooled with Zheng and Becker's usability observations or with [Bender et al.'s randomized feedback field study](../literature-watch/2026-10-28-feedback-timing-and-behavioral-outcomes.md).

**Proposed future test, not conducted:** With appropriate consent, compare judgments for legitimate familiar communications and plausible impersonations, measuring whether verification information was noticed, understood and used, alongside confidence, correct discrimination and avoidable disruption. The central question is whether a tool produces *justified* confidence rather than confidence alone.

## Familiarity can influence perceived safety without establishing destination accuracy (30 October 2026)

A [new full-text appraisal of Albakry, Vaniea and Wolters (CHI 2020)](../literature-watch/2026-10-30-url-reading-and-familiar-brand-cues.md) adds an earlier empirical anchor for the distinction between seeing a familiar cue and understanding it. In an online URL-reading survey of 1,929 analyzed respondents, participants averaged **5.2/6** correct when a recognizable organization appeared in the domain, versus **1.2/6** when it appeared in the subdomain. They also tended to rate links as safer when they believed the destination was the familiar organization (Results, pp. 8–9). These were **predicted destinations and hypothetical safety ratings**, not actual clicks or phishing reports. Printed subgroup counts in the author PDF do not reconcile with the reported total; the detailed appraisal preserves that limitation.

This complements, but cannot be pooled with, the previously appraised [Zheng and Becker (SOUPS 2022)](full-text-appraisals/zheng-becker-2022.md) classification experiment and [Zheng and Becker (SOUPS 2023)](../literature-watch/2026-10-29-verification-cues-and-workflow-friction.md) formative verification-tool study. The first varied what email information was visible; the second explored how people used and perceived proposed controls; the CHI study asked whether people could parse a URL and how safe it felt. **Cross-study interpretation:** cue visibility, cue comprehension, subjective reassurance and subsequent action must remain distinct. None of these studies independently validates a particular verification aid as improving real-world security outcomes.

**Open test, not an implemented method:** In consented, matched tasks, compare comprehension and confidence when a familiar organization name appears in a legitimate domain versus a misleading position. Record uncertainty and verification decisions separately from final action. A link's apparent familiarity should not be used as a substitute for an independently established destination.
