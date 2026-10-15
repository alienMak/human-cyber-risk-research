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

1. Canfield et al. 2017 full text: sample, statistical power, endpoint alignment, effect estimates and confidence intervals.
2. Zheng and Becker 2023 full text: exact check-button functionality, task outcomes and what “useful” means.
3. Previously indexed Tabassum 2024 and Chen 2024: verification behavior and perceived consequences; avoid duplicate entries.

**Publishing boundary:** Only public research questions and cited studies. No VISHWAR implementation, proprietary metrics, participant records or confidential organizational material.
