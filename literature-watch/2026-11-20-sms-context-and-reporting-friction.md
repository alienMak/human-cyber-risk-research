# SMS legitimacy cues, reporting friction and limits of training inference

**Paper:** [Tabassum, Faklaris & Richter Lipford, *What Drives SMiShing Susceptibility? A U.S. Interview Study of How and Why Mobile Phone Users Judge Text Messages to be Real or Fake*](https://www.usenix.org/system/files/soups2024-tabassum-sarah.pdf)  
**Publication:** SOUPS 2024, August 2024, pp. 393–411; [USENIX record](https://www.usenix.org/conference/soups2024/presentation/tabassum-sarah)  
**Type:** Peer-reviewed conference empirical qualitative study  
**Review date:** 2026-11-20  
**Access/status:** FULL TEXT APPRAISED; original proceedings PDF, §§3–7 and Appendix/codebook identified. No independent reanalysis of interview transcripts.

## What the authors investigated

In-person interviews with **29 adult mobile-phone users** recruited through university announcements, local flyers and online advertisements in a southeastern US metropolitan area (§3.1–3.2, pp. 395–396). Fifteen participants were aged 18–24 (§3.2). The interview combined recalled experiences and think-aloud classification of **three pairs** of legitimate/fraudulent SMS per person, selected from six pairs using interviewer counterbalancing (§3.3, p. 396). Four pairs were simulated bank-themed messages; two were real-life examples; the visual presentation varied between iMessage and Android. This is **not** a randomized training trial or an observation of subsequent real-world attacks.

The researchers asked about suspicious and legitimate cues, verification, reporting and prior cybersecurity training. Audio interviews were transcribed; the first author coded the complete dataset and the first and second authors discussed the codebook (§3.4, pp. 396–397). No independent inter-rater reliability statistic was reported.

**Outcomes/operational definitions:** Qualitative themes and participant descriptions of message credibility, interview-task judgments, and self-reported reporting/verification. There is no prospective click, credential disclosure, confirmed compromise or longitudinal outcome. The comparison is between described cues and presented message examples, not an experimentally controlled intervention.

## What the paper reports

- Participants described checking message content, links, format, personalization and whether they expected the text, rather than consistently relying on sender identifiers (§§4, 5.1, pp. 397–403).
- **16/29** said they generally did not report suspicious SMS; **7/29** said they occasionally reported (§4.5, p. 402). These are interview responses, not verified reporting logs. Some preferred deletion or ignoring; participants requested simpler reporting and feedback.
- **14/29** reported no formal cybersecurity education. The authors observed that some previously trained participants appeared more cautious about fraudulent messages **and** more suspicious of legitimate ones (§4.6, p. 403). The paper explicitly does not statistically establish a training effect. Prior training was not assigned, standardized or controlled.

## Eight-domain critical appraisal

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Design | Partial | Qualitative inquiry fits exploration of perceived cues; cannot estimate training effectiveness (§3) |
| Sampling | Partial | Recruitment and demographics reported; small local volunteer sample, youth-heavy (§§3.1–3.2; §6) |
| Outcome definition | Partial | Interview statements and prompted judgments identifiable; no independently verified real-world behavior (§§3.3, 4) |
| Confounding | No | Training, age, background, phone familiarity and message style not experimentally separated (§§3.3, 4.6, 6) |
| Measurement | Partial | Three pairs per participant and think-aloud described; item difficulty and interface differ (§3.3; §6) |
| Analysis | Partial | Inductive codebook and team discussions described; first author coded all transcripts, no independent reliability estimate (§3.4) |
| Generalization | Partial | Real mobile users, but primarily financial-themed examples and one urban area (§6) |
| Ethics/reproducibility | Partial | Consent, IRB approval and $25 compensation reported; transcripts not independently reanalyzed (§3.3) |

## Interpretation, not an author finding

The study is useful for identifying **which cues people say they consider** and why they might not report a suspicious message. It does not demonstrate that those cues predict actual attack susceptibility, that training caused better judgments, or that an easier reporting interface increases reports. Apparent training-related caution may also produce mistaken rejection of legitimate texts. The message-format and platform differences make direct accuracy comparisons difficult (§6, p. 404).

## Questions worth testing

1. With matched legitimate and malicious SMS, does prior context (such as an expected delivery) alter **verification, unsafe compliance and mistaken rejection** separately?
2. Does a simpler reporting option increase accurate reporting without increasing unnecessary reports, measured using actual actions rather than stated intention?
3. Does a decision pattern observed in email transfer to SMS when interface affordances and message difficulty are independently controlled?

These are proposed future studies, not existing features or validated methods. No private scoring, architecture, organizational information or participant records are included.

**Source-type boundary:** Primary peer-reviewed SOUPS paper only. No preprint, news or podcast was used as empirical support.
