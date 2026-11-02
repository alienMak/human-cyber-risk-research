# Can social caution protect someone in one scam and obstruct support-seeking in another?

**Primary source:** Martin Dechant, Victoria Woo, Florence Tomlin, Bettina Moltrecht and Mark Warner, [*Anxious and Aware: Examining the Effects of Social Anxiety on Social Engineering Resilience and Vulnerability*](https://www.usenix.org/conference/soups2026/presentation/dechant). *Twenty-Second Symposium on Usable Privacy and Security* (SOUPS 2026), pp. 313–332, August 2026. [Published full text deposited at UCL](https://discovery.ucl.ac.uk/id/eprint/10230240/1/soups2026-dechant.pdf) (21 PDF pages including cover; 20 proceedings pages). No DOI is supplied in the checked USENIX record.  
**Type/status:** Peer-reviewed primary qualitative conference paper; **FULL TEXT APPRAISED 2 November 2026**. Checked §§2.4–5.2, Tables 1 and A2–A5, and ethics statement; especially proceedings pp. 315–324 (PDF pp. 4–13).  
**Deduplication:** No existing canonical Dechant entry found in the repository matrix/register or targeted repository search. Distinct from the previously indexed [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas), which remains **ABSTRACT-ONLY** in this review, and the previously appraised [McGill et al. (2026)](https://doi.org/10.1016/j.cose.2026.104872), which measured questionnaire associations rather than scenario narratives.

## What the authors actually investigated

The authors asked how characteristics of trait social anxiety might affect responses to different social-engineering situations and what support participants would find useful. This was **two linked exploratory studies, not a randomized intervention or a measurement of actual fraud victimization**.

**Study 1, source of scenarios (§3.1–3.2; proceedings pp. 315–317):** An online UK recruitment survey collected 67 responses in June 2025. After exclusions for ineligible or suspicious entries, insufficient descriptions and a duplicate, the researchers analyzed **42 respondents'** self-described prior social-engineering experiences. They used inductive qualitative coding to identify three scenario families: trust/desire, extortion, and empathy/urgency. Table 1 reports **27, 5 and 11 mentions** respectively; these are *story/theme counts*, not mutually exclusive counts of participants, and should not be divided by 42 to infer prevalence. The study used the Liebowitz Social Anxiety Scale (LSAS), alongside PHQ-9 and GAD-7 screening, and reported ethics approval (UCL LMS REC 2025-0470-961; §2.5).

**Study 2, main comparison (§§4.1–4.3; proceedings pp. 317–319):** Twenty adults (ages 19–51; nine men, 11 women) participated in remotely conducted, semi-structured role-playing interviews, July–August 2025. Six came from Study 1 follow-up; **14 came from the researchers' networks**. Ten were classified as higher trait social anxiety (LSAS ≥55; group mean 68.3) and ten as lower (LSAS ≤54; mean 35.6). They were told the study's purpose and discussed **three scripted, two-stage scenarios** involving a job scam, extortion, and romance scam. The scenarios were built from Study 1 accounts and expert review, with fictional material, and **were presented in a fixed order**. Interviews lasted 60–120 minutes, were transcribed and coded using reflexive thematic analysis. No randomized anxiety assignment, unexposed control arm, or longitudinal follow-up existed.

**Operational outcomes:** Narrated intentions, perceived cues, emotional responses, anticipated verification/disengagement, willingness to share or report, and suggestions for support tools. These are **hypothetical role-play statements and qualitative themes**, not observed phishing clicks, money transfers, independently verified detection accuracy, reporting logs, or measured intervention efficacy (§§4.1–4.5). Group comparisons are thematic, not population estimates or causal effects.

## Findings, and their boundaries

**Authors' qualitative findings (§4.4; proceedings pp. 319–322):** Both groups described reluctance to report scams to authorities, citing uncertainty about reporting routes, effort, or doubts that reporting would help (§4.4.1). Participants with higher LSAS scores more often described fear of judgment as a barrier to sharing experiences; lower-LSAS participants more often framed non-sharing as privacy preference. These distinctions come from a small purposive/convenience sample and cannot establish population prevalence.

The same higher-LSAS group sometimes identified unusual tone, pressure, missing information and breached social norms in the job or extortion scenarios (§4.4.3), **but** also described being reassured by unsolicited praise in a job approach or being curious about alleged compromising content (§4.4.2). Thus, caution and susceptibility were not mutually exclusive; their apparent direction depended on the scenario. The authors did not test whether these narrated responses would occur during real attacks.

**Participant suggestions (§4.5; proceedings pp. 322–323):** Respondents proposed automated warnings, accessible guidance, anonymous peer support and simpler reporting. These are *ideas elicited during interviews*, not evaluated products or demonstrated effective interventions.

**Source-based interpretation:** Treating a psychological characteristic as a fixed individual cyber-risk label would overstate this evidence. A stronger question is which features of a request make someone pause, seek reassurance, disengage, or avoid asking for help. The costs and availability of reporting also need to be distinguished from recognition.

## Eight-domain quality appraisal

| Domain | Judgment | Evidence and limitation |
| --- | --- | --- |
| Research design | **Partial** | Two-stage qualitative exploration fits hypothesis generation; cannot estimate causal effects of anxiety or interventions (§§3–4). |
| Sampling | **Partial** | Study 1: 42 retained; Study 2: 20, including 14 recruited via personal networks; purposive high/low LSAS split, not representative (§§3.1.1–3.1.4, 4.1.1). |
| Outcome definition | **Yes for qualitative intentions; No for observed protection** | Narrated hypothetical actions and themes are clear; no real clicking, reporting or victimization endpoint (§§4.1–4.5). |
| Confounding | **Partial** | Job, extortion and romance scenarios differ in many ways; fixed order, social context, recruitment source, prior experience and comorbidity could influence themes (§5.2). |
| Measurement | **Partial** | Established LSAS/PHQ-9/GAD-7 measures described; interview themes are interpretive, not validated susceptibility scores (§§3.1.2, 4.1–4.2). |
| Analysis | **Partial** | Two coders, reflexive thematic analysis and conceptual checking reported; no statistical between-group test, and qualitative frequency should not be read as an effect size (§§3.1.3, 4.1.2, 4.4). |
| Generalization | **No for field behavior** | Disclosed, fixed-order role-play allows reflection without actual pressure; small academic/network sample and variable reporting infrastructure (§5.2). |
| Ethics/reproducibility | **Partial** | UCL ethics approval, consent, pseudonyms, de-identification and support resources described (§2.5); materials/scenario excerpts described, but no independent replication or raw interview-data reanalysis undertaken. |

**Numerical caution:** The study-1 theme counts in Table 1 total 43 although 42 respondents were retained; the text states some people described multiple experiences. Do not mislabel these as mutually exclusive participant categories (§§3.1.3, 3.2; Table 1). A small discrepancy in the reported LSAS skewness between §3.1.4 and Figure 1 is not resolved here and is not used analytically.

## What remains open

1. **Proposed test, not an author finding:** In consented, unfamiliar scenarios, does the same person respond differently to pressure, praise and ambiguous requests? Compare *observed* verification, disengagement and unsafe compliance while accounting for scenario difficulty, rather than classifying individuals by a single trait.
2. **Proposed test:** If reporting is private, low-friction and nonjudgmental, does help-seeking increase without increasing mistaken reports of legitimate communication? Randomize the reporting interface while keeping scenario content comparable; measure both actual reporting and false alarms.
3. **Proposed test:** Does a participant's stated willingness to seek help predict later behavior when the task is unexpected? Separate role-play intentions, real opportunities to ask for help, and reporting completion.

**Other source lanes:** [Weidhaas, von Preuschen and Distler (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) is a distinct peer-reviewed workplace-emotion study (**ABSTRACT-ONLY** here: N=41; PDF too large for reliable full-text retrieval in this run). [Eiger et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/eiger) is a distinct peer-reviewed study of scams after incarceration (**ABSTRACT-ONLY** here: publisher reports N=48 unique respondents and reporting-stigma concerns). Their samples and outcomes must not be pooled with Dechant's. No preprints, news or podcasts are used as empirical corroboration.

**Public publication boundary:** Only published, cited study descriptions and non-proprietary research questions appear here. No platform implementation, private scoring rules, unpublished participant data, confidential organizational information or credentials. This note does not imply the repository owner personally read or endorsed these conclusions.
