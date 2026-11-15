# Language, requests for help, and what a click can establish

**Paper:** [Spero et al., *Language as Lure: A Naturalistic Study on Pasifika Phishing Susceptibility*](https://www.usenix.org/conference/soups2025/presentation/spero)  
**Authors:** Eric Spero, Isa Seow, Lucas Betts, Eddie Fuatimau, Robert Biddle, Danielle Lottridge, Giovanni Russello  
**Publication:** SOUPS 2025, August 2025, pp. 19–35; peer-reviewed conference paper  
**Original full text:** https://www.usenix.org/system/files/soups2025-spero.pdf  
**Review date:** 2026-11-15  
**Status:** FULL TEXT APPRAISED, §§4–8, Tables 1–4 and Appendix A. Earlier [15 October note](2026-10-15-language-and-verification.md) had only screened the abstract; this is an upgrade of the same paper, not a second study.

## What the authors investigated

A government partner selected 2,000 employees in one Melanesian country. Over four months, each employee received one simulated phishing email per month. Participants were randomly assigned to English or the country's national language in each campaign, with language alternating so each person received two messages in each language. The four email types were presented in successive months: two commercial-looking messages and two requests for personal assistance. Translation was checked by a local linguistics professor. Employees did not receive advance notice; clicks led to a debriefing survey. The researchers report ethics approval and an agreement that employees would not be penalized (§§4.1–4.5, pp. 21–24).

**Intervention/comparison:** Language version (English versus national language) within each of four message types; repeated language exposure across employees. Email type was also a predictor, but each type occurred in a different month, so type and campaign time are not independently separable.

**Measured outcomes:** Recorded link clicks (primary), tracked email opens (descriptive), and optional post-click attitudes and explanations. A click does not establish credential disclosure, actual compromise, or failure to recognize a suspicious message. Opens depend on tracking pixels; first-campaign opens were not recorded because of a configuration error (§§4.2–5.1, pp. 22–25).

**Analysis:** The authors used generalized estimating equations (GEE) logistic regression with an exchangeable within-person correlation structure, including language-by-email interactions (§4.6, p. 24). They explicitly caution that supplemental chi-squared comparisons do not account for repeated measures.

## What the results support

Table 1 (p. 25) reports click rates for English versus national language: commercial-order message 15.2% versus 17.4%; airline message 1.5% versus 3.0%; budget help request 14.6% versus 23.1%; church-related help request 13.2% versus 30.5%. Each language condition contained 1,000 recipients per campaign. These are **campaign-specific rates**, not individual risk scores.

In Table 2 (p. 26), the national-language main coefficient at the commercial-order reference message was not significant (estimate 0.16, p=.18). The language-by-budget interaction was positive (0.40, p=.01), as was language-by-church (0.90, p<.001); the airline interaction was not significant (p=.11). This supports a **message-dependent language association in observed clicks**, not a universal language effect. The authors' additional airline chi-squared result (p=.03) conflicts with the repeated-measures GEE inference; they explicitly attribute that discrepancy to limitations of the simpler test (§5.1.2).

The voluntary survey recorded 115 responses, restricted to people who clicked, with optional questions and possible repeat responses from the same person. Survey responses were anonymized and not linked to simulation records (§5.2.1, p. 26). This prevents using survey explanations as population-level evidence of the mechanisms causing clicks. The authors propose emotional resonance, cultural norms and in-group familiarity as possible explanations, **not measured mediators** (§6, pp. 27–29).

## Eight-domain methodological appraisal

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Research design | Partial | Randomized language variants and repeated observations support within-campaign comparison; message type is confounded with month (§4.3) |
| Sampling | Partial | 2,000 government-selected employees in one organization; selection criteria and broader representativeness not established (§4.1) |
| Outcome definition | Yes | Click and open events distinguished; neither equals compromise (§§4.2, 5.1, 7) |
| Confounding | Partial | Repeated-measures model; possible coworker information sharing after debriefing, changing campaign contexts, language familiarity and order (§§4.3, 6, 7) |
| Measurement | Partial | Event tracking documented; first-month opens missing; optional post-click survey cannot represent non-clickers (§§4.2, 5.1, 5.2) |
| Analysis | Partial | GEE accounts for correlated repeated observations, but no preregistration or independent reanalysis established here; chi-squared caveat acknowledged (§§4.6, 5.1.2) |
| Generalization | Partial | Actual work inbox interactions improve ecological relevance; one government, four specific lures and no actual compromise outcome (§§4, 7) |
| Ethics and reproducibility | Partial | Ethics clearance, anonymization and non-penalization reported; identifiable country withheld for protection; no independently verified reusable participant dataset (§§4.5, 7) |

## What remains uncertain

The study cannot isolate emotional resonance, cultural expectations, sender familiarity or language proficiency as causal mediators. Its help-request comparison also differs in format, apparent sender and campaign timing from the commercial emails. No legitimate-message controls, verified reporting, verification actions, false alarms or long-term transfer were measured. The authors note possible contamination through coworkers after debriefing and that clicks are only a precursor to compromise (§7, p. 29). The optional survey cannot repair those gaps.

**Cross-study distinction:** [Hasegawa et al. (SOUPS 2021)](https://www.usenix.org/conference/soups2021/presentation/hasegawa) used hypothetical message-handling choices across countries; Spero records clicks in work inboxes. Their outcomes and populations should not be pooled. [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) remains ABSTRACT-ONLY in this review, despite its relevant discussion of perceived consequences.

## Where this leaves the question

**Analysis:** The observed difference appears concentrated in requests for assistance rather than uniformly across messages. A language-specific click rate should not be interpreted as a fixed characteristic of a language community or an individual.

**Proposed future tests, not established results:**
1. Cross language with request type and independently matched legitimate and suspicious messages, separating correct rejection, mistaken rejection, verification and unsafe compliance.
2. Measure language familiarity and perceived social obligation independently, rather than assuming either explains the interaction.
3. Repeat with unfamiliar messages after a delay to test whether the pattern transfers beyond the four original campaigns.

**Source boundaries:** No preprints, news or podcasts are used as corroborating empirical evidence in this appraisal. No private platform design, algorithms, confidential data or participant records are included. This note records a source-based appraisal and does not imply that the repository owner personally read or endorsed it.
