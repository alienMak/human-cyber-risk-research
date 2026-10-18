# If the safe route is unavailable, whose failure are we measuring?

**Research trail:** Individual prediction → context-sensitive decisions → practical access to independent verification.  
**Date:** 18 October 2026.  
**Evidence status:** Cross-study methodological synthesis, based on previously appraised research; **not a new intervention or an estimate of causal effects**.

## The problem with calling every unsafe decision a knowledge failure

Suppose someone recognizes a request as unusual and wants to check it. The organization's approved directory is inaccessible, the named contact is unavailable, and the workflow penalizes delay. If they proceed, their decision has consequences. But their action alone does not identify whether they misunderstood the risk, lacked a workable control, faced an unreasonable trade-off, or some combination.

The opposite is also possible: a reliable verification route exists, yet the participant never considers using it. That points to a different research and design question. We should not collapse these cases into the same explanation.

## What the sources actually support

- [Buckmann et al., *More than Usability: Differential Access to Digital Security and Privacy* (SOUPS 2025)](https://www.usenix.org/system/files/soups2025-buckmann.pdf) used **47 qualitative interviews in Germany**. The [full-text appraisal in this repository](2026-10-18-access-to-verification.md) records uneven access to security advice, knowledgeable support and usable resources. It does **not** establish that a missing verification route caused a measured phishing click.
- [Alromaih, Flechais and Chalhoub, *Beyond the Office Walls: Understanding Security and Shadow Security Behaviours in a Remote Work Context* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/alromaih) used **20 interviews** to examine remote work and shadow security. The [earlier appraisal](2026-10-18-shadow-security-and-policy-deviation.md) cautions that reported policy interpretations were not independently checked against every actual organizational policy. Workarounds can reflect practical constraints, but the interview design does not quantify a causal effect.
- [Chen et al., *What Motivates and Discourages Employees in Phishing Interventions* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/chen) used **seven focus groups with 34 university employees** to examine perceptions, motivations and barriers. The [prior note](2026-10-18-recognition-without-reporting.md) distinguishes identifying a suspicious message from reporting it. These are accounts and interpretations, not an experimental measure of control availability.

These studies are **qualitative evidence for plausible mechanisms**. They do not justify allocating numerical shares of responsibility to employees versus organizations.

## A decision-outcome matrix (illustrative, not empirical)

| Risk recognized? | Independent route usable? | What the observation might mean | What it does not prove |
| --- | --- | --- | --- |
| Yes | Yes | Person may verify, defer, report or still comply | Recognition guarantees safe behavior |
| Yes | No | Control access, timing or incentives may constrain action | Person lacks knowledge |
| No | Yes | Recognition, attention or relevance may be limiting | A working control alone is sufficient |
| No | No | Multiple barriers may interact | A single root cause can be inferred |

**Route usable** needs an operational definition: independent of the suspicious request, discoverable, accessible in the actual context, timely enough to be practical and authoritative for the decision. A phone number supplied by the suspicious caller is not independent verification simply because it is a phone number.

## A sharper research design

Rather than only recording whether a participant accepted or rejected a request, a future study could observe:

1. **Recognition:** Did they notice and describe a relevant warning sign before feedback?
2. **Intention:** Did they try to verify, defer or report?
3. **Opportunity:** Was a genuinely independent route available and realistically usable?
4. **Action:** What did they do, including delay, escalation and safe handling of legitimate requests?
5. **Consequence:** Did the decision produce an unsafe outcome or an unnecessary disruption?

An ethical study could compare equivalent scenarios with clearly defined, non-harmful variations in verification accessibility, while balancing scenario difficulty, order, workload and legitimate-case consequences. Such a study would need oversight and prespecified analysis. **No such experiment has been run for this note.**

### Competing explanations that must survive scrutiny

- The participant recognized the danger but could not reach an approved source in time.
- The route was available, but difficult to discover or understand.
- The participant preferred a faster but less reliable method.
- The participant misclassified a legitimate request as malicious.
- The request was sufficiently ambiguous that reasonable people differed.
- The observed result reflected scenario difficulty, familiarity, fatigue or assessment awareness rather than control design.

An interview after the fact can help interpret a decision, but retrospective explanations are not direct observation of the reasoning at the time.

## Eight-domain checkpoint

| Domain | Status | Limitation |
| --- | --- | --- |
| Design | Proposed comparison of access conditions | No randomized study performed |
| Sampling | Cross-role access differences are relevant | No recruited cohort for this question |
| Outcomes | Recognition, intent, access, action, consequence separated | Coding reliability not tested |
| Confounding | Difficulty, urgency and incentives identified | No empirical adjustment yet |
| Measurement | Independence and practical usability defined | Actual availability requires observation |
| Analysis | Repeated people and items must be accounted for | No model, effect size or confidence interval |
| Generalization | Potential relevance beyond phishing | Cross-vector transfer untested |
| Ethics/reproducibility | Avoids unsafe real-world manipulation | Protocol, consent and preregistration outstanding |

## Twin's provisional conclusion

A poor outcome does not by itself establish a knowledge deficit. A correct explanation does not prove the organization supplied an actionable path. The evidence we need is **whether the person recognized the risk, what safe options existed, and what prevented or enabled their use**.

The attribution question should be framed as testable competing explanations, not as a moral division of blame. A human-risk assessment that measures only the final click can miss both the employee's attempted caution and the organization's failure to make caution practicable.

**Next question:** If a control technically exists but is too slow, inaccessible or socially costly to use under normal work conditions, should we count it as an effective control at all?

**Publishing boundary:** Publicly available research, transparent hypotheses and general measurement design only. No proprietary scoring rules, confidential organization details or participant data.
