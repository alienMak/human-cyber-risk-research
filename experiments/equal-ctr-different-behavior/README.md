# Experiment 001 — Equal CTR, different behavior

**Status:** Reproducible synthetic demonstration, not a human-participant study.  
**First executed:** 2026-10-11.  
**Research question:** What behavioral differences are hidden when we summarize ten decisions with the same risky-choice rate?

## Design

Construct two fictional learners, each making ten decisions across five attack categories, with three risky choices apiece. The data are deliberately designed examples (not sampled from participants). Each row of `data.csv` contains the learner, attack category, risky-choice flag and elapsed decision time.

The result is a **constructive counterexample**: equal aggregate rates need not imply equal distributions of risky choices. It is not a statistical test and has no sampling uncertainty.

## How to reproduce

Requires Python 3 standard library only:

```bash
python3 experiments/equal-ctr-different-behavior/analyze.py
```

## Observed synthetic output

| Measure | Learner A | Learner B |
| --- | ---: | ---: |
| Decisions | 10 | 10 |
| Risky choices | 3 | 3 |
| Risky-choice rate (CTR) | 0.30 | 0.30 |
| Attack categories with risky choices | 1 | 3 |
| Attack categories with 2+ risky choices | 1 | 0 |
| Mean time, all decisions | 32.2 s | 28.0 s |
| Mean time, risky decisions | 17.67 s | 58.0 s |

In learner A, the three risky choices are all within phishing. Learner B has one each in phishing, physical, and web categories. A acts faster on risky decisions than B. These differences are invisible in the shared 30% CTR.

## Interpretation and limits

The calculation shows an **information-loss problem**, not which learner is more vulnerable. A higher decision time is not automatically worse, and a repeated risky choice is not necessarily more severe than distinct risky choices. Different category difficulties, experience levels, interpretation of cues, and accessibility needs could all affect comparisons. The examples are intentionally constructed, so this is not evidence that such patterns occur at particular rates among real learners.

Do not equate decision time with VISHWAR's **time-to-report (TTR)**. This experiment measures elapsed decision time; TTR may be defined differently and requires its own validation. `repeat_type_count` is explicitly a count of attack categories with at least two risky choices, not the number of excess risky events.

## Next research steps

1. Test sensitivity to category difficulty and unequal category exposure.
2. Evaluate competing operational definitions of repeated risk and consistency.
3. Pre-register hypotheses and collect ethically approved, consented observations before making participant-level generalization claims.
4. Reconcile these prototype measures against implemented VISHWAR report calculations, rather than silently treating them as identical.

## Follow-up sensitivity analysis (2026-10-11)

Run `python3 experiments/equal-ctr-different-behavior/sensitivity.py` to reproduce this deterministic, synthetic sensitivity analysis. No human observations were used. The script contains executable assertions checking each constructed case.

| Controlled change | Result | Interpretation |
| --- | --- | --- |
| Original data | Both learners have CTR 3/10 = 0.30; A has 1 risky category, B has 3 | Equal CTR does not determine where risky choices occur |
| Add four *safe* phishing observations to learner A | A's CTR becomes 3/14 ≈ 0.2143 while the number of risky categories remains 1 | Exposure and denominators can change the aggregate without changing the originally observed risky decisions |
| Recode one of A's three risky choices as safe | CTR becomes 2/10 = 0.20; category remains the same | Coding decisions and ambiguous labels affect quantitative conclusions |
| Only one observed attack category | Across-category CTR variance is undefined in this analysis, not zero | Insufficient variety should not be interpreted as perfect consistency |

The script also computes *macro category CTR* (mean of category-specific rates) and *category CTR population variance*. Macro and micro aggregation differ when categories have unequal observation counts. These quantities are descriptions, not calibrated vulnerability scores.

The additional safe events and recoding are **counterfactual manipulations**, not newly observed behaviors or effects of a training intervention. Label changes must not be selected after seeing the result in a real study.

**Next:** design predeclared difficulty strata, balanced exposure schedules, scoring-key reliability checks and longitudinal participant analyses with appropriate ethics review. Avoid treating a synthetic counterexample as validation of a composite index.

## Visual explanation

![Experiment 001: the same aggregate CTR conceals different category distributions](../../figures/experiment-001-risk-patterns.svg)

*Constructed examples from this experiment's CSV. Both learners have 3 risky decisions out of 10; there are no participant observations.*
