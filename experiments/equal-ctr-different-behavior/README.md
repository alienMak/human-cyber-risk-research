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
