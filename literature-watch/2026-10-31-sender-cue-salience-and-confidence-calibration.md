# Does drawing attention to sender details improve judgment, or just suspicion?

**Primary paper:** James Nicholson, Lynne Coventry and Pam Briggs, [*Can we fight social engineering attacks by social means? Assessing social salience as a means to improve phish detection*](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson), SOUPS 2017, proceedings pp. 285–298. [Original USENIX PDF](https://www.usenix.org/system/files/conference/soups2017/soups2017-nicholson.pdf). The USENIX citation supplies no DOI; none is inferred.  
**Publication:** July 2017. **Type:** Peer-reviewed primary conference study.  
**Review status:** **FULL TEXT APPRAISED on 31 October 2026**; original 15-page proceedings PDF including cover, §§3–5, Tables 1–6, Figures 2–3 and limitations. The 2017 study was already present in the evidence matrix at abstract level; this is an **upgrade**, not a new study or an independent replication.  
**Other evidence checked:** [Canfield, Fischhoff and Davis (2016)](https://doi.org/10.1177/0018720816665025), journal publisher **ABSTRACT-ONLY**; [Zheng and Becker (SOUPS 2022)](https://www.usenix.org/conference/soups2022/presentation/zheng), **previously appraised** in this repository, publisher record rechecked; [Weidhaas, von Preuschen and Distler (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas), **ABSTRACT-ONLY** in this run (full PDF could not be retrieved through the available research interface). No preprints, news or podcasts are treated as empirical corroboration.

## What the authors actually tested

The researchers recruited **281 adult Mechanical Turk workers** for an online email-classification experiment, with a priori sample planning. Inclusion required English proficiency and at least 50 approved platform tasks; mobile users were excluded. Participants were randomly allocated to a **2 × 2 between-participant design**: no highlight (n=65), sender details highlighted (n=64), number of fellow recipients highlighted (n=79), or both highlighted (n=73). Each judged **18 static email images: six phishing and twelve legitimate**. Messages were based on real university correspondence and known problematic phishing emails but adapted by the researchers. Participants were explicitly told they were identifying phishing after entering the task (§§3.1–3.5, proceedings pp. 287–288; Table 1).

**Intervention:** The sender cue highlighted the sender name, email address and time received; the recipient cue showed the proportion of colleagues receiving the message. **Comparison:** Unmodified email images in the control group. **Measured outcomes:** Binary genuine/phishing classification, decision time per message, self-rated confidence from 0% to 100% in 10-point steps, and a short impulsivity questionnaire. The authors evaluated discrimination (signal-detection sensitivity, d') separately from response tendency (beta); in this task a *false alarm* means labelling a legitimate email as phishing, not filing a workplace report (§§3.4, 4.1, pp. 288–289).

## Findings with denominators and sections

- **Discrimination:** Mean d' was **0.59** (control, n=65), **0.98** (sender, n=64), **0.87** (recipient, n=79), and **0.92** (combined, n=73). The authors report sender versus control **t(127)=2.080, p=.020**, recipient versus control **t(142)=1.498, p=.068**, and combined versus control **t(142)=1.667, p=.049** (§4.2, Table 2, p. 289). They describe sender and combined conditions as improvements and recipient-only as not significant.
- **Response tendency:** Mean beta was **1.90** (control), **1.47** (sender), **1.87** (recipient), and **1.65** (combined); the reported group-versus-control tests were not statistically significant (§4.3, Table 3, p. 289). A nonsignificant difference is **not** proof that the intervention cannot change response bias.
- **Time:** Mean decision time per email was **19.91 seconds** (control), **20.28** (sender), **18.18** (recipient), and **18.79** (combined), with no significant group-versus-control difference reported (§4.4, Table 4, p. 289). This is timing within a static classification task, not workplace productivity.
- **Confidence:** Mean confidence across groups was **68.73%**; the authors' calibration plots suggest overconfidence for phishing and underconfidence for legitimate emails. They do not establish that the highlighting improved confidence calibration (§4.5, Table 5 and Figures 2–3, pp. 289–290).
- **Individual differences:** Higher dysfunctional-impulsivity scorers had lower discrimination and faster decisions in a post-hoc extreme-group comparison; allocation was **not stratified** on that characteristic, and the authors declined an inferential treatment-by-trait interaction analysis (§4.6, Table 6, pp. 290–291).

**Numerical/statistical check requiring follow-up:** The printed p-values for the three discrimination contrasts are consistent with **one-sided** t-test tails (e.g., t=2.080, df=127 gives approximately .020 one-sided and .040 two-sided). The excerpted methods/results do not clearly specify the sidedness or any multiplicity adjustment. For the combined-versus-control sensitivity comparison, Table 1 implies conventional two-group df=65+73−2=**136**, while §4.2 prints **142**; §4.3 uses 136 for a different combined comparison. These are unresolved reporting issues, **not corrected effect estimates**. The conclusion about the combined cue is especially sensitive to how significance is assessed. Do not use its p=.049 as independently validated evidence of a robust additional effect.

## Eight-domain methodological appraisal

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Design | **Yes for task-specific randomized cue comparison** | Four randomized groups; same classification task (§3.1, p. 287). Not a training or real-inbox trial. |
| Sampling | **Partial** | n=281 crowdworkers, platform eligibility, time-based rejection and replacement; nonprobability recruitment (§3.2, Table 1, pp. 287–288). |
| Outcomes | **Yes for classification; no for reporting/compliance** | Binary labels, decision time, confidence and signal detection (§§3.4, 4.1, pp. 288–289). |
| Confounding | **Partial** | Stimulus features partially matched; message familiarity and real task context unknown; impulsivity imbalance not controlled (§§3.3, 4.6, 5.5). |
| Measurement | **Partial** | Static images; confidence increments; impulsivity subscales report Cronbach alpha .670 and .856 (§3.4). No actual checking or click behavior. |
| Analysis | **Partial** | d' and beta distinguish discrimination from criterion; group contrasts reported, but sidedness, multiplicity and one df require clarification (§§4.1–4.3, Table 2). |
| Generalization | **Limited** | Participants knew to look for phishing, could not inspect links or independently verify; the email was not their own (§5.5, p. 292). |
| Ethics/reproducibility | **Partial / not fully reported in checked sections** | Recruitment/payment described; no independent dataset reanalysis or verification of ethics approval completed (§§3.2–3.5). |

## Interpretation, not an additional author finding

This experiment is more informative than a simple accuracy comparison because it distinguishes **better discrimination** from **a greater tendency to reject everything**. However, highlighting existing sender details and presenting *only* headers are not the same intervention. The later [Zheng and Becker (2022)](https://www.usenix.org/conference/soups2022/presentation/zheng) study found that header-only presentation did not improve phishing classification. These findings need not conflict: changing **salience** of information inside a full message differs from removing other information. Neither study shows that the effect persists during real work or that people will verify a suspicious sender.

The [Canfield et al. (2016) abstract](https://doi.org/10.1177/0018720816665025) also separates identifying phishing from deciding what action to take. The [Weidhaas et al. (2026) abstract](https://www.usenix.org/conference/soups2026/presentation/weidhaas) adds that perceived reputational consequences can matter in simulated workplace phishing. Those are contextual connections only; neither was newly appraised in full here.

## Lessons and proposed tests, not completed experiments

1. **Measure discrimination and indiscriminate caution separately.** A higher phishing rejection rate could reflect improved recognition or simply more legitimate messages being rejected. A consented study could include both message types and report each error type rather than treating all suspicion as improvement.
2. **Do not assume visibility creates understanding.** Test whether a participant can explain why sender information matters and use it when it conflicts with a familiar brand or plausible request. Separate noticing, interpretation, confidence, verification and final action.
3. **Keep task cost and context in view.** The absence of a timing difference in a short screenshot task does not establish that the cue is cost-free during real work. Compare unfamiliar communications in realistic workflows, including appropriate verification options, and report uncertainty.

**Open question:** If sender information is made easier to notice, does it improve *justified confidence* and subsequent verification, or merely classification in an unusually vigilant test setting?

**Public-IP review:** Public-source methodological interpretation only. No VISHWAR algorithms, weights, implementation architecture, unpublished participant data, confidential PR3CORIA information, credentials or patent-sensitive mechanisms are included. No production software changes.
