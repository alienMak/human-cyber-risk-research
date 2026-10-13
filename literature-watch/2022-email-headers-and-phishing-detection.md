# Seeing sender details is not the same as understanding them

**Paper:** [Presenting Suspicious Details in User-Facing E-mail Headers Does Not Improve Phishing Detection](https://www.usenix.org/conference/soups2022/presentation/zheng) ([publisher PDF](https://www.usenix.org/system/files/soups2022-zheng_1.pdf))  
**Authors:** Sarah Y. Zheng and Ingolf Becker  
**Published:** SOUPS 2022, August 2022, pp. 253–271  
**Type:** Peer-reviewed conference paper; no DOI listed by USENIX  
**Status:** FULL TEXT APPRAISED, 13 October 2026 (20-page publisher PDF)  
**Attribution:** Source-based review; not a claim that the repository owner personally read or endorsed it.

## Design, population and outcomes

The authors tested whether people detect phishing better when suspicious sender details are isolated from persuasive message content. **252 UK Prolific participants**, 84 per group, were randomly assigned to a simulated executive-assistant task. The conditions were full e-mail (**Control**), subject and body (**Headerless**), or user-facing header and subject (**Bodyless**). Recruitment targeted UK age/gender representation; it was not a natural workplace sample. See §3.1–3.3, pp. 255–256.

All participants classified **47 messages**: 37 legitimate, eight phishing and two spam. First they decided whether to discard a message or pass it to their fictitious boss; discard revealed labels including *phishing* and *spam*. Legitimate e-mails were adapted from Enron messages; phishing messages came from several sources. There was no live attack outcome. See §3.3–3.5, pp. 255–258.

**Operational definitions:** Per-message detection was the share of participants explicitly labeling a phishing message *phishing*. Participant recall was the share of eight phishing messages correctly labeled; precision was the share of messages labeled *phishing* that were actually phishing. The authors also re-coded *spam* as a positive label in a sensitivity analysis. These are classification outcomes, not field compromise rates. See §3.7 and §4.3, pp. 258–261.

## Findings

Mean recall was **0.46** for Control, **0.37** for Headerless and **0.25** for Bodyless; mean precision was **0.93**, **0.81** and **0.73**. Performance varied sharply by item: phishing message p3 was detected by **87%** in Control and **16%** in Bodyless, while p8 was detected by **6%, 4% and 2%** across the three groups. See §4.1–4.3 and Table 2, pp. 259–261.

Only **seven participants** hovered over a phishing URL, and two of those cases were labeled phishing. Personal traits and message features did not consistently predict detection across conditions, though isolated regression terms were significant. The paper did not directly observe whether people looked at specific header fields. See §4.2–4.3 and §5.1, pp. 260–263.

## Eight-domain appraisal

| Domain | Assessment | Basis |
| --- | --- | --- |
| Design | Yes for display comparison; partial for attention mechanism | Random allocation; individual-field gaze not observed (§3.1; §5.1). |
| Sampling | Partial | Prolific panel, age/gender matching, role-play context (§3.2). |
| Outcome definition | Yes for classification; partial for real-world behavior | Recall/precision defined; *spam* coding affects interpretation (§3.7; §4.3). |
| Confounding | Partial | Same stimuli across groups, but item difficulty and task familiarity vary (§3.3–3.4; §5.1). |
| Measurement | Partial | Rendered HTML and link-hover logs, no granular gaze measure (§3.3; §5.1). |
| Analysis | Partial | Item tests and exploratory regressions on only eight phishing stimuli (§3.7; §4). |
| Generalization | Partial | Simulated, fictitious work environment (§5.1). |
| Ethics/reproducibility | Partial | Ethics approval, anonymous data and supplementary materials; replication not independently verified (§3; §3.5). |

## Interpretation and proposed tests

**Interpretation:** Showing a cue does not guarantee understanding. But a *spam* label instead of *phishing* does not necessarily mean someone would act unsafely. The study cannot distinguish ignoring a header from seeing and misunderstanding it.

**Future questions, not completed work:** (1) Can a study separately observe *noticing*, *interpreting* and *verifying* a suspicious cue? (2) Would point-of-decision guidance improve classification without increasing false alarms or interrupting the main task? (3) Does any benefit persist when message difficulty and context change?

**Boundary:** No inference here validates a person-level risk score or generalizes to other attack channels.
