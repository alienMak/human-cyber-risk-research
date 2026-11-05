# When recognition, clicking and reporting happen in a work context

**Paper:** [Distler (2023), *The Influence of Context on Response to Spear-Phishing Attacks: an In-Situ Deception Study*](https://doi.org/10.1145/3544548.3581170)  
**Original full text:** [Author/institution-hosted CHI 2023 PDF](https://www.unibw.de/usable-security-and-privacy/publikationen/pdf/distler2023chi.pdf)  
**Published:** 19 April 2023 (CHI 2023, article 619, 18 pages)  
**Type:** Peer-reviewed primary qualitative study  
**Review status:** **FULL TEXT APPRAISED**, 5 November 2026. Sections 3–5, Table 1, Figure 4, appendices C–F inspected. This is an analytical literature note, not a claim of personal endorsement or an independent replication.

## What the author investigated

Distler examined how workplace context shapes responses to a simulated spear-phishing email, why employees do or do not report, and what interventions they propose (Section 1). Fourteen volunteers from a European university participated: ten research staff, three administrative staff and one IT employee; mean age 35 (Section 3.2). Approximately 70 employees received recruitment invitations. This is a small self-selected university sample, not a representative employee cohort.

Participants consented to observation of their ordinary work but were initially unaware that phishing was the study focus. During a roughly one-hour observation, a simulated email apparently from a supervisor arrived after 55 minutes. The researcher observed behavior, then debriefed, obtained renewed consent, interviewed participants and collected retrospective experience curves (Sections 3.3–3.4; Appendix C). The lure combined an authority cue and an urgent website-related request. There was **no randomized intervention or unexposed comparison group**. The first three messages were in English; later messages were adapted to the expected sender-recipient language after the first three participants recognized the linguistic mismatch (Section 5.5).

**Operational definitions:** the paper defines a successful phish as **clicking the simulated email link**, not credential submission or compromise (Section 1; Section 3.4). Reporting means informing the IT department, which is distinct from mentioning the email to a colleague. Observation notes, interviews and retrospective curves were analyzed through summarizing content analysis; the author describes a codebook clarification/co-coding exercise, but does not report a quantitative inter-rater agreement statistic (Section 3.5; Table 1).

## Findings, separated from interpretation

**Author's observations:** Four of 14 participants clicked (29% within this selected sample); the author explicitly warns that this is not a population click-rate estimate (Section 4.1.1). Familiarity of the request with current tasks, authority, expectations of rapid email response and language conventions appeared in participants' explanations. Some non-clickers checked with colleagues or used known routes to a website (Sections 4.1–4.1.2). None of the four who clicked discussed their click with anyone during the observed episode; the paper describes reporting uncertainty and perceived consequences (Sections 4.1.2, 4.2, 5.2). **This does not prove a general post-click nonreporting rate.**

**Analytical reading:** An email can be persuasive precisely because it fits a person's immediate task, while a mismatch in language or communication style may trigger verification. This complicates attributing one observed click to a stable personal weakness. Likewise, lack of reporting after clicking might reflect uncertainty about procedures, anticipated blame, or the short observation window; the design does not isolate those mechanisms.

**Proposed future tests (not findings):**
1. In a consented study, vary whether an otherwise comparable request fits an ongoing task, and separately measure recognition, verification, click and reporting. Predefine legitimate-message false alarms.
2. Test whether a clear, non-punitive route to report **after** an unsafe action changes subsequent help-seeking, while measuring perceived consequences and not assuming the effect from this qualitative study.
3. In multilingual settings, match expected sender language or explicitly randomize it; otherwise a language mismatch may confound any comparison attributed to training or scenario difficulty.

## Eight-domain methodological appraisal

| Domain | Assessment | Evidence and reason |
| --- | --- | --- |
| Research design | **Yes for exploratory contextual description; No for causal efficacy** | Sections 3.1, 3.4: in-situ deception, one simulated message, no randomized comparison. |
| Sampling | **Partial** | Section 3.2: 14 volunteers at one university, recruitment through supervisors; self-selection and small sample. |
| Outcome definition | **Yes, narrowly** | Sections 1, 3.4, 4.1: clicking defined as success; IT reporting distinct from other communication; no credential or incident outcome. |
| Confounding | **Partial** | Sections 3.3, 5.5: authority and urgency co-occur; first three messages differed in language; prior simulation exposure not experimentally controlled. |
| Measurement | **Partial** | Sections 3.4–3.5: direct observation triangulated with interviews and UX curves; subjective interpretations and brief observation window remain. |
| Analysis | **Partial** | Section 3.5, Appendix E: inductive/deductive qualitative coding and codebook discussion; no formal quantitative agreement estimate or inferential efficacy analysis. |
| Generalization | **No for population estimates** | Section 5.5: university, advanced-degree employees, desktop office setting, one hour. |
| Ethics/reproducibility | **Partial** | Sections 3.4–3.5, Appendices C–F: ethics review, debrief and renewed consent, protocol/codebook supplied; raw sensitive data not public. |

## Boundaries and unresolved questions

The observer was known to participants, and observation itself may affect behavior. Only a short period after receipt was observed; delayed reporting cannot be ruled out. The initial language mismatch and subsequent change to the lure are particularly important when interpreting the four clicks. The study is qualitative and should not be pooled as a click-rate experiment. It does not test a training intervention, long-term retention or cross-vector transfer.

**Related evidence, not a replication:** [Weidhaas, von Preuschen & Distler (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas), **ABSTRACT-ONLY in this review**, examines emotional and behavioral responses in a different simulated-workplace qualitative study (N=41). Its abstract reports that not clicking could be perceived as a reputational mistake. No full-text extraction or quantitative comparison is claimed here. News, podcasts and preprints were not used as empirical corroboration.

**Question to retain:** When someone suspects a message is malicious but believes ignoring a legitimate request carries social or professional costs, what determines whether they verify, comply or seek help?