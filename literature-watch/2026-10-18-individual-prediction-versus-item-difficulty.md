# Predicting a person is not the same as ranking a phishing email

**Research trail:** PEST email-level correspondence → same-person prediction → unfamiliar-task transfer → stability and calibration.  
**Date:** 18 October 2026.  
**Evidence status:** Methodological synthesis of previously appraised primary studies; **no new longitudinal dataset analyzed**. Source identities and previously recorded access limits are retained.

## The empirical starting point

[Hakim et al., *The Phishing Email Suspicion Test (PEST)*](https://doi.org/10.3758/s13428-020-01495-0) compared suspicion ratings of **84 email items** with their field click effectiveness among **different people**. The published item-level correlation is **rho(82) = −0.22, p = 0.048**. That modest association says something about the *emails*, not whether the laboratory score predicts an individual's later click. The [full-text verification note](2026-10-18-lab-suspicion-versus-field-clicks-pest.md) records the sampling, design and reproducibility limits.

[Canfield et al., *Replication: Challenges in Using Data from Phishing Experiments to Measure Security Behavior* (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/canfield) previously compared experimental phishing responses with separately observed security behaviors and cautioned against treating laboratory classification as an established predictor of broader security behavior. This repository's earlier synthesis discusses the source; the present note does not claim a fresh complete-paper appraisal.

[Tang, Bauer and Christin, *Misuse, Misreporting, Misinterpretation of Statistical Methods in Usable Privacy and Security Papers* (SOUPS 2025)](https://www.usenix.org/conference/soups2025/presentation/tang) raises a methodological issue directly relevant here: repeated judgments by the same person and repeated presentations of an item are not independent observations. The repository previously appraised that paper; no statistical reanalysis is claimed.

## Four different claims that need different evidence

1. **Item-level difficulty:** Some phishing emails elicit more unsafe responses than others. Compare outcomes across independently characterized items.
2. **Cross-sectional individual association:** Some participants perform differently in one controlled assessment. That may reflect task familiarity, ability, motivation or noise.
3. **Longitudinal individual prediction:** A score at time A predicts *the same person's* later choices on held-out tasks at time B.
4. **Stable personal trait:** The prediction reflects an enduring individual characteristic across contexts. This is a much stronger claim and cannot be inferred merely from a successful short-term forecast.

The distinction is not semantic. A study can establish the first claim while supplying no direct evidence for the third or fourth.

## The validation trap: data leakage

Imagine each person answers 20 phishing items. A random **response-level** train/test split could put 15 responses from a participant in training and five in testing. A model could learn that participant's tendencies without demonstrating generalization to *new people*. Similarly, reusing near-identical lures can make it easy to recognize items without demonstrating transfer to unfamiliar attacks.

For a **new-person** claim, hold out entire participants. For a **future-same-person** claim, enforce chronological separation and hold out future items. For a **new-scenario** claim, hold out entire lure families or attack mechanisms. These evaluate different questions; no single split validates them all.

## Proposed validation plan (not conducted)

- **Baseline:** Collect decisions on independently labeled malicious and legitimate cases; record deferral, reporting and independent verification where feasible.
- **Temporal test:** Repeat after a prespecified delay without signaling that another phishing assessment is underway.
- **Novelty test:** Use unseen lure families and a separate context or channel where ethically appropriate.
- **Comparison models:** Compare any individual-history model with simple baselines such as item difficulty and a population-level response rate. If it cannot outperform those, person-level modeling may add little.
- **Analysis:** Account for repeated observations nested within people and items, missing follow-up, calibration, uncertainty and the consequences of false-positive risk labels.
- **Ethics:** Minimize personal traces, avoid individual stigmatization, seek informed oversight for deception and do not interpret a score as an employment or disciplinary judgment.

## What would falsify the individual-prediction claim?

If baseline scores predict performance only when the same email templates recur, but fail on unfamiliar messages or after adjusting for item difficulty, the evidence would favor familiarity or scenario effects over stable individual prediction. If performance changes markedly with workload, available verification routes or task instructions, a trait-only explanation becomes weaker.

A positive association still would not establish causality: an assessment score might be a useful predictor without explaining *why* later decisions occur.

## Eight-domain appraisal of the proposed claim

| Domain | Current evidence | Gap |
| --- | --- | --- |
| Design | PEST supports email-item correspondence | Same-person prospective validation missing |
| Sampling | PEST lab participants were undergraduates | Diverse roles, ages and contexts needed |
| Outcomes | Suspicion ratings and clicks distinguishable | Legitimate handling, reporting and independent verification |
| Confounding | Item difficulty and context identified | Prospective control and prespecified covariates |
| Measurement | Explicit lab suspicion task | Unprompted later behavior |
| Analysis | Published modest item-level association | Out-of-sample prediction, calibration, uncertainty and clustering |
| Generalization | Email-item level only | New people, new scenarios, later times and other vectors |
| Ethics/reproducibility | Public PEST code/data links reported | Future consent, privacy and reproducible validation plan |

**Twin's provisional answer:** Before calling someone high or low risk, demonstrate that their earlier observations predict their own later decisions *beyond scenario difficulty and context*, with uncertainty and external validation. No current note in this trail establishes that standard.

**Next question:** If the same person's security behavior changes when the surrounding conditions change, is the variability measurement error—or is the context itself part of the phenomenon we should study?

**Publishing boundary:** General research methods and published findings only. No unpublished platform architecture, formulas, proprietary scoring or participant data.
