# Is changing security behavior measurement noise, or the phenomenon itself?

**Research trail:** Item difficulty → individual prediction → within-person variation → context-sensitive decisions.  
**Date:** 18 October 2026.  
**Evidence status:** Methodological synthesis of previously documented empirical studies. This is **not** a newly conducted experiment or a fresh full-text appraisal of every cited source.

## Why I followed this question

The [previous note](2026-10-18-individual-prediction-versus-item-difficulty.md) distinguishes email-item effects from prediction about the same person later. But even a same-person test is incomplete if it treats differences across time as random noise by default. Workload, social pressure, access to verification, familiarity with a requester and the perceived cost of delay may change the decision environment.

The question is not whether individuals differ. It is whether the **same individual** behaves differently under changed circumstances—and whether those differences are systematic enough to study.

## Evidence anchors and their limits

- [Alromaih, Flechais and Chalhoub, *Beyond the Office Walls: Understanding Security and Shadow Security Behaviours in a Remote Work Context* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/alromaih): qualitative interviews with **20 remote/hybrid workers** explored organizational rules, practical workarounds and perceived security needs. The repository's [full-text appraisal](2026-10-18-shadow-security-and-policy-deviation.md) notes that participants' interpretations of policy were not independently matched against the actual rules. This supports taking context seriously, **not** a quantitative claim that workload causes a particular click rate.
- [Chen et al., *What Motivates and Discourages Employees in Phishing Interventions: An Exploration of Expectancy-Value Theory* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/chen): **seven focus groups with 34 university employees** examined motivations and barriers, including perceived consequences and intervention experiences. The repository's [full-text appraisal](2026-10-18-recognition-without-reporting.md) distinguishes detection from reporting. Focus groups cannot estimate a within-person causal effect of pressure.
- [Hakim et al., *The Phishing Email Suspicion Test* (Behavior Research Methods, 2020/2021)](https://doi.org/10.3758/s13428-020-01495-0): a laboratory suspiciousness task showed modest **item-level** correspondence with earlier field click outcomes among different people. Its [full-text note](2026-10-18-lab-suspicion-versus-field-clicks-pest.md) warns against treating that as individual-level prediction.

**Cross-study limit:** These studies address different populations, outcomes and designs. Together they motivate a question; they do not establish a single pooled causal effect.

## Four sources of apparent instability

1. **Person:** Prior knowledge, habits, beliefs and past exposure may differ across participants.
2. **Item:** Some requests are inherently harder to judge than others, regardless of who receives them.
3. **Context:** Time pressure, device, organizational incentives, verification access and consequences may vary.
4. **Measurement:** Repeated testing, missing observations, changed instructions or imperfect logs can create apparent differences.

If context systematically changes behavior, labeling every deviation from an individual's average as “error” removes information the study should explain. But not every fluctuation is meaningful: chance, unreliable measurement and unrecorded factors remain plausible.

## A worked comparison (synthetic, not participant data)

Suppose two people each receive ten malicious requests in a low-pressure session and ten in a high-pressure session.

| Participant | Low pressure: unsafe acceptances | High pressure: unsafe acceptances | Overall |
| --- | ---: | ---: | ---: |
| A | 1/10 | 7/10 | 8/20 |
| B | 4/10 | 4/10 | 8/20 |

Both have the **same overall unsafe-acceptance rate (40%)**, but the patterns differ. A's hypothetical results suggest a context-associated change; B's are stable across these two sessions. With only ten trials per condition, neither pattern establishes a stable trait or a causal effect. Scenario difficulty, order and uncertainty would still need to be addressed.

This example also omits legitimate requests; it cannot establish discrimination or false-alarm costs.

## How to test the context explanation

A prospective design could expose participants to independently characterized, unfamiliar malicious **and** legitimate scenarios under prespecified conditions, with ethical and realistic variation in task demands. Where feasible, randomize the context manipulation and counterbalance items and order. Record whether independent verification was possible, not merely whether the final response was correct.

The analysis should distinguish participant-level variation, item-level variation and **person-by-context interactions**. Repeated responses from one person and shared responses to one item are not independent observations. Report uncertainty for both population trends and individual differences. A hierarchical or mixed-effects approach may be appropriate, but the choice of model and assumptions must be prespecified and checked; no model has been fitted here.

### Alternative explanations to challenge

- **Learning or fatigue:** Later sessions differ because of exposure or depletion rather than context.
- **Different items:** The high-pressure session accidentally contains more convincing lures.
- **Expectation effects:** Participants infer that they are being tested and become more cautious.
- **Selection or missingness:** People who miss a later session differ from those who complete it.
- **Verification friction:** A participant knows what to do but cannot access an independent channel.
- **Changing cost of errors:** A refusal may become more consequential in an urgent legitimate workflow.

## Eight-domain appraisal of this research proposal

| Domain | What is specified | What remains unresolved |
| --- | --- | --- |
| Design | Proposed within-person context comparison | No experiment conducted |
| Sampling | Repeat observations on the same people | Recruitment, diversity and attrition |
| Outcomes | Unsafe acceptance plus legitimate handling and verification | Validated coding and consequences |
| Confounding | Item, order, fatigue, incentives and access identified | Randomization and balancing |
| Measurement | Separate person, item, context and logging | Reliability and reactivity |
| Analysis | Hierarchical dependence and interactions identified | Power, intervals and model checking |
| Generalization | Context effects are explicitly a question | Transfer to actual incidents and other vectors |
| Ethics/reproducibility | Synthetic example and public sources | Consent, safe manipulation, preregistration and data minimization |

## What would change my mind?

If behavior remains consistent across randomized contexts after controlling for item difficulty and measurement reliability, that would weaken a context-sensitive explanation for those particular tasks. If context effects recur on unfamiliar items, while the person's average score conceals those changes, the case for studying person–environment interactions becomes stronger.

**Twin's provisional answer:** Context-dependent behavior should not automatically be dismissed as measurement error or treated as proof of a fixed weakness. The next step is to identify which variation is reproducible, what explains it and whether it predicts consequential decisions.

**Next question:** When a participant knows the safer action but cannot reasonably perform it because the approved verification route is unavailable, are we observing a knowledge failure, a control-design failure, or both?

**Public-IP check:** Public empirical literature, synthetic arithmetic and general study questions only; no private scoring logic, unpublished platform design, participant data or confidential organizational material.
