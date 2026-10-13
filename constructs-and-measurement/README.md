# What do we mean by trust?

This is a conceptual measurement note, **not a validated instrument**. The first task is to stop using trust, credibility, reliance, verification and safe behavior as synonyms.

| Construct | Working meaning | Potential observation | What it cannot establish |
| --- | --- | --- | --- |
| Perceived credibility | How believable a claim or source seems to a person in context | Credibility rating with the exact question recorded | That the claim is true |
| Trust | Willingness to accept vulnerability to a particular source in a defined situation | Context-specific trust judgment, alongside task and stakes | A stable personality trait |
| Reliance | Whether someone uses a source's recommendation or delegates a decision | Choice, action, acceptance or override | Whether the source was accurate or trusted |
| Verification | An attempt to check a claim through an appropriately independent channel | Observable check, channel used, result and timing | That checking was effective or feasible |
| Decision quality | Whether a decision meets a stated criterion given available evidence | Prespecified decision outcome and evidence quality | General cybersecurity competence from one task |
| Confidence | How certain a person feels about a judgment | Calibrated confidence report | Correctness or willingness to verify |

## Why the distinctions matter

A participant can rate a message as credible but refuse to act. Someone can distrust an AI recommendation yet follow it under time pressure. A person may verify through a second website that merely repeats the same underlying claim; that is activity, but not necessarily independent corroboration.

The [2022 Zheng and Becker SOUPS paper](https://www.usenix.org/conference/soups2022/presentation/zheng) concerns phishing detection with sender information; the [2023 follow-up](https://www.usenix.org/conference/soups2023/presentation/zheng) studies proposed checking and nudging tools. These are relevant to different observations, not evidence that the constructs are interchangeable.

## Minimum measurement specification

For any future public research proposal, state the decision task, legitimate ground truth, unit of analysis, observable action, comparison condition, time window, missingness, and whether a source-check is genuinely independent. Distinguish knowledge tests, self-report, simulated behavior and field behavior. Record accessibility and reporting opportunities before interpreting a non-action as a failure.

## Validity questions

- **Construct:** Does the measure reflect the named behavior or merely a convenient proxy?
- **Internal:** Could message difficulty, order, familiarity or role explain the difference?
- **External:** Does the task generalize to other channels and populations?
- **Consequential:** Could labels derived from the measure stigmatize or unfairly penalize people?

See [outcomes and study design](../literature-review/outcomes-and-study-design.md) and [quality appraisal](../literature-review/quality-appraisal.md). This file discloses no private scoring formula or platform implementation.
