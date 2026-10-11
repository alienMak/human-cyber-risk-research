# Experiment 002 — Does a proposed composite score distinguish cases with identical CTR?

**Status:** Deterministic synthetic sensitivity demonstration (2026-10-11). **Not a human study, risk predictor, or validation of the weights.**

## Question

Given two **constructed** examples with identical risky-choice rate (CTR), can a weighted score reflecting time-to-report, quiz results and repeat events produce different outputs? This is a test of the *formula's behavior*, not evidence of better real-world risk measurement.

## Definitions and formula

- CTR: fraction of risky choices in eligible decision opportunities (0–1).
- TTR: a hypothetical time-to-report in seconds; not general decision response time.
- Quiz: score fraction (0–1).
- Repeats: hypothetical nonnegative repeat-event count; categories versus event counts must be defined before practical use.

Proposed exploratory score:

```
100 * (0.35 * CTR + 0.20 * min(TTR / 300, 1)
       + 0.25 * (1 - Quiz) + 0.20 * min(Repeats / 3, 1))
```

Unobserved TTR is **missing**, not zero. The implementation returns an unavailable composite when any component is missing, rejects out-of-range inputs, and caps time and repeats. The proposed weights and direction of time effects are assumptions, not empirical estimates.

## Reproduce

```bash
python3 experiments/composite-vs-ctr-synthetic/experiment.py
```

Python standard library only; the script includes assertions and does not require access to VISHWAR, an API or participant records.

## Constructed outputs

| Scenario | CTR-only score | Proposed composite |
| --- | ---: | ---: |
| A: CTR .5, TTR 30s, quiz .9, repeats 0 | 50 | 22 |
| B: CTR .5, TTR 240s, quiz .3, repeats 3 | 50 | 71 |
| C: CTR .5, TTR missing, quiz .5, repeats 0 | 50 | Unavailable |
| D: Fully safe / quiz 1 / no time or repeats | 0 | 0 |
| E: Fully risky / quiz 0 / 300s / three repeats | 100 | 100 |

Scenarios A and B have identical CTR but differ in *three* other variables. Thus their different scores are mathematically expected and **do not isolate the causal contribution of any single component**. Controlled one-factor-at-a-time and ablation tests are needed to assess sensitivity more precisely.

## Interpretation, limitations, and next tests

The formula is sensitive to inputs omitted by CTR. That sensitivity alone does not establish whether those inputs actually measure vulnerability, predict incidents, or fairly compare people. A slow report could reflect scenario complexity, workload, unfamiliarity, access needs or policy, not heightened risk. No learner rankings, calibration, reliability, fairness, predictive validity or improvement claims are supported.

This exercise differs from Experiment 001, which uses constructed **decision elapsed time** rather than **time-to-report**. Those concepts should not be substituted.

Next: formalize reporting opportunity and missingness; reconcile the operational definition of repeated risk; vary single inputs and weights; pre-specify a target outcome; then evaluate reliability, calibration and incremental utility over CTR on appropriately approved human-participant data.

## Visual explanation

![Experiment 002: CTR-only and proposed composite scores for two constructed cases](../../figures/experiment-002-comparison.svg)

![Illustrative composite score sensitivity to hypothetical time-to-report](../../figures/experiment-002-sensitivity.svg)

*Synthetic formula outputs only. Neither plot demonstrates predictive accuracy, causal effects, nor validated human-risk measurement. The second graph holds CTR at 0.5, quiz at 0.7 and hypothetical repeats at 1, and changes only report time.*
