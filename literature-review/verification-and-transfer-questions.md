# Verification and transfer: questions answered provisionally

**15 October 2026 — research working note.** Questions are answered using the skeptical “Twin” method: identify the observation, propose competing explanations, ask what would falsify each one, and separate results from conjecture. No claim of an experiment or proprietary model.

## Q1. Is keeping a suspicious caller on the line while checking cautious or risky?

**Provisional answer: both descriptions can apply.** The checking is evidence of uncertainty or initiative, not proof of an independently verified decision. Continued interaction leaves an opportunity for persuasion, but does not prove manipulation occurred. To discriminate, observe where the evidence comes from, whether contact continues, what is disclosed, and the eventual action. **Confidence: conceptual distinction high; causal effect of continued exposure not established by these sources.**

## Q2. Is a “check” button proof that independent verification works?

**No.** [Zheng and Becker (SOUPS 2023)](https://www.usenix.org/conference/soups2023/presentation/zheng) designed two nudges and a check feature; in a formative, simulated email-interface evaluation with **27 professional email users**, the check feature and suspicion-score nudge were considered useful. Participants sometimes interpreted identical email details differently. This is usability evidence, not a field trial proving that checking reduces compromise. **Status: publisher summary and accessible PDF introduction inspected; full methods and results not independently appraised in this note.**

**Twin's challenge:** A check button could improve judgments, encourage over-reliance on the interface, or merely increase confidence. Those outcomes require separate testing.

## Q3. Does phishing-detection performance predict real-world safety?

**Not automatically.** [Canfield et al. (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/canfield) replicated a signal-detection task and compared it with data from the Security Behavior Observatory. Task scores correlated with security intentions, but the authors found **no evidence of predictive validity** for the observed malicious software, URLs and files outcomes in their sample. That is not proof that detection tests have no value: the field outcomes capture broader computer-security exposures and protections, not a direct count of the same phishing decisions. **Status: original paper abstract and introductory discussion inspected; numerical full-text appraisal still pending.**

**Twin's challenge:** The null association could reflect a weak test, poorly aligned external outcomes, restricted variation, inadequate power, or genuine failure to transfer. Inspect the full methods and estimates before deciding.

## Q4. What should a better comparison actually separate?

A future independently designed study could distinguish:
- Recognition of suspicious cues, including correct acceptance of legitimate messages.
- Initial verification intention versus observed verification action.
- Independently sourced verification versus relying on material supplied by the suspicious requester.
- Continuing contact, disclosure sequence, and final disposition.
- Immediate performance versus later behavior in a different context.

**These are candidate constructs, not a validated scoring system.** A realistic comparison would require ethical review, clear outcome definitions, and attention to legitimate-message false alarms.

## Q5. What would change our minds?

- Evidence that continued contact does *not* alter outcomes under controlled, comparable verification conditions would weaken the exposure hypothesis.
- Evidence that independently sourced checking does *not* improve decisions relative to attacker-supplied checking would weaken the independence hypothesis.
- A well-powered prospective association between detection tasks and aligned real-world phishing outcomes would qualify Canfield's negative predictive-validity result.

## Next reading priorities

1. Canfield et al. 2017: reconcile the previously reported full-text reading with a durable eight-domain appraisal before treating that review as archived; the original publisher abstract confirms the null predictive-validity finding, but this note does not independently reproduce the full numerical analysis.
2. Zheng and Becker 2023 full text: exact check-button functionality, task outcomes and what “useful” means.
3. Previously indexed Tabassum 2024 and Chen 2024: verification behavior and perceived consequences; avoid duplicate entries.

**Publishing boundary:** Only public research questions and cited studies. No VISHWAR implementation, proprietary metrics, participant records or confidential organizational material.


## Follow-up: a correct rejection may be recognition or blanket avoidance (18 October 2026)

**Twin question:** If two people reject the same suspicious email, what evidence would show that one recognized deception while the other simply rejects unfamiliar messages?

**Provisional answer:** The single rejection does not distinguish those explanations. A comparison must also include legitimate messages, because refusing everything can produce perfect rejection of attacks while imposing false-alarm costs. This is an established signal-detection distinction, not a new construct or a validated scoring approach.

**Primary-source cross-checks:**

- [Canfield et al., SOUPS 2017](https://www.usenix.org/system/files/conference/soups2017/soups2017-canfield.pdf), Introduction and signal-detection task: distinguishes sensitivity to phishing versus legitimate emails from response bias. The publisher reports that task performance did not predict the particular observed malicious-software, URL and file outcomes in the Security Behavior Observatory. **Status for this follow-up: publisher abstract and PDF introduction checked; previous full-text numerical reading not independently repeated.** This is not proof that behavioral assessments cannot predict appropriately matched phishing decisions.
- [Nicholson, Coventry and Briggs, SOUPS 2017](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson): publisher abstract reports improved phishing detection from sender salience without an unwanted response bias, and poorly calibrated confidence, particularly for phishing messages. **Status here: ABSTRACT-ONLY.** The paper's intervention and sample must be checked in full before extending its result to other contexts.
- [Lastdrager et al., SOUPS 2017](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/lastdrager): publisher abstract reports that children's overall phishing-classification score improved by 14% after training, with most of the gain in phishing recognition; recognition of legitimate emails was not improved. The publisher also reports that the phishing gain was no longer evident after four weeks. **Status here: ABSTRACT-ONLY.** This illustrates why changes in attack rejection and legitimate acceptance should not be collapsed into a single training narrative.

**Competing explanations:** (1) improved discrimination between legitimate and suspicious messages; (2) a more conservative response threshold with more false alarms; (3) variation in message difficulty, familiarity or opportunity to respond. These sources do not establish which mechanism explains a particular individual's decision.

**Possible future test, not an implemented system:** Compare responses to consented legitimate and suspicious communications of appropriately matched difficulty. Report mistaken acceptance and mistaken rejection separately; investigate whether an apparent improvement in attack rejection coincides with greater rejection of legitimate requests. Repeat with unfamiliar examples to distinguish retention from recognition of previously seen material. This is a general methodological question, not a proprietary implementation or scoring formula.

**Researcher review question:** If someone never clicks a suspicious message, are they recognizing threats or simply refusing to engage with anything unfamiliar?


## Follow-up: retention, transfer and reporting are different claims (18 October 2026)

**Twin question:** If performance improves after training, is it better judgment, familiarity with the task, or a shift in how people respond to uncertain messages?

Two already indexed studies provide contrasting evidence; this is **not** a new source count or a pooled effect.

- [Lastdrager et al., *How Effective is Anti-Phishing Training for Children?* (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/lastdrager): Dutch primary-school experiment with a control group and a later retest. The publisher abstract reports a 14% improvement in overall classification, mainly phishing recognition; legitimate-email recognition did not improve. The phishing-detection gain returned to its earlier level after four weeks. **Status this follow-up: ABSTRACT-ONLY; full-text details of allocation, exact follow-up denominators and stimuli not re-extracted.**
- [Chen et al., *The Effects of Group Discussion and Role-playing Anti-phishing Training* (SOUPS 2024 poster)](https://www.usenix.org/conference/soups2024/presentation/chen-poster): preregistered mixed-design experiment, N=105, three time points, a control group and three in-situ phishing tests. Publisher poster abstract reports within-group improvements in self-efficacy and support-seeking intention for both trainings; only role-playing improved support-seeking intention versus control. It also reports more phishing-test reporting and vigilance in training groups than control. **Status: POSTER ABSTRACT-ONLY; not a full journal/conference paper appraisal.**

**What the authors actually measured differs:** schoolchildren's email classification and later retest versus employees' self-efficacy, intentions and in-situ phishing-test behavior. A classification score, stated intention and reporting event cannot be treated as interchangeable endpoints. Neither abstract alone establishes generalization to a different attack channel.

**Competing explanations:** A later score can change because of retained knowledge, memory of stimulus patterns, differences in item difficulty or changed willingness to report. Repeated observations from the same participants also require an analysis that accounts for dependence. The accessible abstracts do not provide enough detail to resolve those explanations or audit the models.

**Proposed future test, not a completed study:** Distinguish performance on previously encountered examples from appropriately matched unfamiliar examples; measure recognition of both legitimate and malicious requests; report reporting behavior separately from classification and intentions. Predefine which comparison represents retention and which represents transfer. Do not infer a causal effect from cross-study contrasts.

**Open for full-text review:** allocation and attrition in Lastdrager et al.; Chen et al.'s exact intervention, unit of randomization, timing, outcome denominators and analysis of repeated measures. No numerical synthesis until these are checked.

**Researcher review question:** When a participant performs better later, did they learn to recognize the underlying deception or to recognize the assessment's patterns?

**Public-IP check:** Published abstracts and general methodological questions only; no unpublished technical methods, proprietary scoring, participant data or confidential material.


## Follow-up: a plausible explanation is not an observed decision sequence (18 October 2026)

**Twin question:** When someone explains *why* they accepted or rejected a message after the event, which parts of that account can the study actually verify?

**Evidence already appraised, not a new independent literature search:**

- [Wash, Nthala and Rader, SOUPS 2021](https://www.usenix.org/system/files/soups2021-wash.pdf), §§3–6: 297 U.S. respondents retrospectively described a memorable suspicious email. The authors analyzed self-reported expectations, investigation and action. Their design does **not** independently reconstruct the full decision sequence or verify the true legitimacy of every recalled message. See [full-text working appraisal](../literature-watch/2026-10-18-when-suspicion-is-correct-but-the-email-is-legitimate.md).
- [Häring et al., SOUPS 2024](https://www.usenix.org/system/files/soups2024-haring.pdf), §§3.2–3.3: a laboratory authentication study captured think-aloud behavior, interaction recordings and post-task accounts. Seven of 18 main-study participants transmitted simulated sensitive material to impersonators. Such contemporaneous records can document what participants *did* more directly than retrospective recall, but think-aloud and researcher presence may alter behavior. See [full-text working appraisal](../literature-watch/2026-10-18-verification-after-mismatch.md).

**What these designs do and do not establish:** A retrospective account gives access to what a participant remembers and is willing to describe; an interaction trace establishes observable steps, not the full private reasoning behind them. Think-aloud data are contemporaneous verbalizations, not a transparent recording of cognition. Neither paper directly randomizes people to retrospective versus contemporaneous reporting to estimate the causal effect of recall.

**Competing explanations for a polished after-the-fact account:** (1) accurate memory of the original reasoning; (2) reconstruction influenced by the known outcome; (3) selective reporting of steps that sound defensible; (4) omission of mundane actions that were not memorable. These are hypotheses, not diagnoses of the people in either study.

**Methodological question for future work:** For consented security simulations, distinguish timestamped observed actions, contemporaneous verbalizations and post-task explanations as separate evidence types. Compare agreement and disagreement between them, without assuming the trace reveals intent or that disagreement proves dishonesty. Consider observation effects, privacy safeguards and what cannot be recorded ethically. This is a public research question, not a proprietary instrumentation specification.

**Boundary:** These two studies involve different populations, tasks and evidence collection. No shared effect size, causal comparison or validated inference about individual cognition follows from juxtaposing them.

**Researcher review question:** If the action log and the participant's later explanation disagree, which conclusion is justified—and what additional evidence would actually resolve it?

**Public IP check:** Only cited published studies and general methodological questions; no unpublished formulas, private implementation, participant records or confidential material.


## Q: Does refusing more suspicious requests mean someone learned to discriminate better? (18 October 2026)

**Short answer:** Not without measuring decisions on legitimate requests too. An increase in rejections could indicate improved attack recognition, a more conservative response threshold, or both.

**Primary research anchor:** [Canfield et al., *Replication: Challenges in Using Data from Phishing Experiments to Measure Security Behavior* (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/canfield). The study compared phishing email judgments and other security-behavior measures; its key limitation for this question is that a laboratory classification score did not establish predictive validity for the independently observed security actions in that sample. **Evidence status here:** existing repository appraisal and original publisher record; not a fresh complete-paper reanalysis.

**Second anchor:** [Nicholson, Coventry and Briggs, *Can We Fight Social Engineering Attacks by Social Means? Assessing Social Salience as a Means to Improve Phish Detection* (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson). This work examined detection and confidence in a phishing-classification task. The repository has previously recorded publisher-level evidence about confidence calibration and salience; **not a new full-text appraisal in this cycle**.

### Worked example — synthetic, not a result from either paper

Suppose a balanced test has 10 malicious and 10 legitimate requests. We call “reject as suspicious” a positive detection.

| Decision counts | Participant A | Participant B |
| --- | ---: | ---: |
| Malicious requests rejected (true positives) | 9 | 9 |
| Malicious requests accepted (false negatives) | 1 | 1 |
| Legitimate requests rejected (false positives) | 9 | 0 |
| Legitimate requests accepted (true negatives) | 1 | 10 |
| Detection rate on malicious requests | 90% | 90% |
| False-alarm rate on legitimate requests | 90% | 0% |
| Overall classification accuracy | 50% | 95% |

Both participants have the **same malicious-request rejection rate**, yet their overall ability to distinguish legitimate from malicious requests differs sharply. Participant A might be deliberately cautious, confused, or responding to high perceived consequences; these counts alone cannot identify the motivation.

### Signal detection, without pretending the example is validated

- **Sensitivity / discrimination** concerns separating malicious from legitimate stimuli.
- **Response criterion / bias** concerns the tendency to label a stimulus suspicious when uncertain.
- A hit rate and a false-alarm rate jointly provide more information than either alone. Under a suitable signal-detection model, they can be used to estimate sensitivity and criterion; model assumptions, class balance and extreme-rate corrections matter.
- An overall accuracy score depends on the proportion of malicious and legitimate cases. If that proportion changes, accuracy can change even when a participant's underlying decisions do not.
- In real workflows, **independent verification, deferral and reporting** may be reasonable alternatives to immediate accept/reject; a binary task omits them. “Reject legitimate” is not necessarily harmful if it means a temporary pause followed by successful verification.

### What would discriminate the competing explanations?

**Hypothesis A — genuine discrimination:** With unfamiliar, comparably difficult cases, malicious requests are more often identified while legitimate requests continue to be handled appropriately.

**Hypothesis B — blanket avoidance:** Malicious requests are more often rejected, but legitimate requests are rejected at a similar or greater rate.

**Hypothesis C — scenario or base-rate change:** Apparent gains come from easier lures, a different mix of legitimate cases or changes in participant expectations rather than learning.

A credible future study should preregister the relevant outcomes, independently establish ground truth, include both classes, consider task order and familiarity, report uncertainty, and analyze repeated decisions without treating them as independent participants. It should also consider the cost of errors in the relevant setting, not assume that all false positives and false negatives have equal consequences.

### Eight-domain checkpoint for this *synthesis*, not a new primary-paper appraisal

| Domain | What is established here | Outstanding work |
| --- | --- | --- |
| Design | Conceptual comparison of two classifications | Prospectively test retention and transfer |
| Sampling | Synthetic 20-request illustration only | Recruit an appropriate, diverse sample |
| Outcome definition | True/false positives and negatives defined | Distinguish reject, defer, verify and report |
| Confounding | Criterion and scenario composition explicitly separated | Control lure difficulty and context |
| Measurement | Fully reproducible synthetic confusion matrices | Validate real scenario labels and logging |
| Analysis | Arithmetic checked; no inferential estimates claimed | Estimate uncertainty, within-person dependence and calibration |
| Generalization | No external validity claimed for synthetic counts | Test unfamiliar channels and real consequences |
| Ethics/reproducibility | Synthetic counts; no human data | Consent, privacy, deception and accessibility review |

**Researcher review question:** If a participant rejects every request, is that good security performance, a failure to discriminate, or a reasonable strategy in an environment where the costs of accepting are exceptionally high? The answer depends on ground truth, available verification routes and consequences.

**Public IP check:** General published methodological ideas and synthetic numbers only; no unpublished scoring formula, proprietary assessment rules, architecture or private participant data.
