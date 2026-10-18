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
