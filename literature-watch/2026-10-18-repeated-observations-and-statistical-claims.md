# Ten decisions from one person are not ten independent people

**Paper:** [Tang, Bauer and Christin, *Misuse, Misreporting, Misinterpretation of Statistical Methods in Usable Privacy and Security Papers*](https://www.usenix.org/system/files/soups2025-tang.pdf). SOUPS 2025, pp. 475–493.  
**Type:** Peer-reviewed methodological systematic review. **Access:** FULL TEXT APPRAISED, especially §§1, 3.1–3.2 and reported results. **Added:** 18 October 2026.

## What the authors studied

The authors examined statistical claims in SOUPS publications across ten **even-numbered conference years** from 2005 to 2024. From 223 papers in those years, they included 121 using null-hypothesis significance testing (NHST), coding 479 assertions supported by statistical tests (§3.1, printed p. 478; introduction, p. 476). This is a methodological review of published studies, **not** a participant intervention, phishing experiment, or sample of every SOUPS paper.

One primary coder reviewed the papers. A second coder assessed a stratified subsample of 19 papers; initial agreement was reported as 0.51 before reconciliation (§3.1, p. 478). The authors explicitly **assumed statistical computations were correct** rather than rerunning tests (§1, p. 476). They examined suitability of statistical methods, reporting sufficiency, and interpretation, not independent replication of findings.

## What they found

In their sample, 9% of the coded statistical assertions, spanning 23% of papers, did not properly account for independence/dependence of observations. For 23% of assertions, spanning 58% of papers, reporting was insufficient to determine whether the method supported the claim. Another 21% of assertions, spanning 47% of papers, were not fully substantiated by reported statistics (§1, p. 476). These categories must not be summed as if mutually exclusive.

**Authors' claim:** inadequate attention to data dependence and incomplete reporting can undermine inference. The paper does **not** establish that 23% of all human-security experiments are false or that any specific prior result in this repository is invalid.

## Twin's question

If one participant makes ten decisions, does a study have ten independent people or ten correlated observations?

**Answer:** Ten observations, potentially correlated within the same person. The correct treatment depends on the assignment, outcome, sampling and estimand. A study can legitimately analyze repeated responses, but must model or otherwise account for dependence; it must not inflate its apparent independent sample size.

Three rival explanations for an apparent improvement across sessions remain possible: genuine behavioral change, increased familiarity with the task, or changes in scenario difficulty. Appropriate controls and uncertainty estimates are needed to separate them. The Tang paper evaluates statistical reporting and cannot resolve these causal alternatives.

## Eight-domain appraisal

| Domain | Assessment | Evidence and limits |
| --- | --- | --- |
| Research design | Yes for reporting audit | Systematic coding of NHST assertions, not an intervention study (§§1, 3). |
| Sampling | Partial | Even-numbered SOUPS years, 121 NHST papers out of 223 screened; excludes other venues and non-NHST research (§3.1). |
| Outcome definition | Yes | Assertion-level statistical validity, reporting and interpretation codes (§3.2). |
| Confounding | Partial | Differences in publication year, statistical approach and coding difficulty may affect issue frequencies (§§3.1–3.2). |
| Measurement | Partial | Defined codebook, iterative coding, second-coder subset; judgment calls remain (§3.1). |
| Analysis | Partial | Descriptive frequencies, not a reanalysis of original statistical tests (§1). |
| Generalization | Partial | SOUPS selected years, not a random sample of all usable-security research (§3.1). |
| Ethics and reproducibility | Partial | Published papers used; codebook and examples described, but independent reproduction not performed here (§3.1 and Appendix A). |

## What changes in the research agenda

1. For studies involving repeated simulated decisions, explicitly identify the unit of assignment, unit of observation and unit of inference before interpreting an effect. This is a general statistical safeguard, not a proprietary scoring method.
2. Report effect magnitude, uncertainty, missingness and scenario variation; do not turn a non-significant result into proof of no effect.
3. When comparing training across sessions, challenge whether apparent improvement could reflect task familiarity or unequal scenario difficulty rather than transfer.

**Open question:** Which published repeated-simulation studies provide enough information to verify that their analysis accounts for within-person dependence? A focused audit of individual methods sections is needed; this note does not claim to have completed it.

**Researcher review:** If one person makes ten decisions, are we learning ten things about ten people, or ten related things about one person?

**Public IP check:** Published methodological evidence and general research questions only. No internal implementation, proprietary formulas, unpublished architecture, confidential material or participant data.
