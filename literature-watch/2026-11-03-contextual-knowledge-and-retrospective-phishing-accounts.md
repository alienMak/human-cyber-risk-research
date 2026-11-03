# What can remembered phishing incidents tell us about contextual judgment?

**Paper:** Rick Wash, Norbert Nthala, and Emilee Rader, [Knowledge and Capabilities that Non-Expert Users Bring to Phishing Detection](https://www.usenix.org/conference/soups2021/presentation/wash).  
**Published:** SOUPS, August 2021, pp. 377–396.  
**Source type:** Peer-reviewed conference paper. **Status:** FULL TEXT APPRAISED on 2026-11-03, [original proceedings PDF](https://www.usenix.org/system/files/soups2021-wash.pdf).  
**Other evidence types:** No preprints, news or podcasts used to corroborate this paper.

## Study and operational definitions

The authors used a retrospective Qualtrics-panel survey conducted in February 2020. Respondents without technical expertise were prompted to recall **one** suspicious or potentially harmful email and describe what they noticed, expected, suspected, investigated, decided and did. The sample comprised **297 valid US respondents** selected with approximate age, gender and ethnicity quotas; 315 otherwise eligible respondents could not recall a qualifying email and were excluded. This is a selected sample of *remembered suspicious incidents*, not a prevalence estimate or random sample of all received emails (§§3.1–3.2, 4, pp. 379–382).

The study did **not** assign phishing interventions or compare treatment and control groups. The implicit comparison was descriptive: reported non-expert processes were compared with an earlier expert interview model, not with simultaneously recruited experts. Measured outcomes were retrospective self-reports, structured response frequencies and manually coded incident narratives, **not** verified phishing detection accuracy, observed clicking, reporting logs or longitudinal change.

Two research assistants independently coded 297 stories using a developed codebook; 13 stories were deemed not to describe a specific incident and excluded from manual-code statistics. The authors report that three codes with low agreement were dropped and disagreements reconciled. The paper describes its agreement statistic as Cronbach's alpha; that choice and its applicability to categorical coding warrant further scrutiny (§3.3, p. 381). Survey materials and replication data are linked from the paper at [OSF](https://osf.io/82sd9/).

## What the authors found

In respondents' accounts, **76%** noticed that the message requested action (§4.2, p. 382); **18%** reported asking another person for a second opinion (§4.6, p. 385). Respondents also reported investigating outside the email, including visiting the purported sender's site or contacting them by phone (§4.6.1, p. 385). **80%** reported reaching a decision about the selected incident, with a mean confidence of **8.9/10** (§4.7, p. 385). The authors argue that people use expectations about their own communications and relationships that automated filtering cannot readily capture (§§5.1–5.3, pp. 387–388).

These are conditional frequencies among selected recollections, not rates of success in detecting phishing. The paper cannot verify whether each remembered message was malicious or whether the remembered investigation happened as described.

## Quality and interpretation

- **Selection:** Exclusion of people who could not remember a suspicious email, plus the choice of an incident easy to recall, favors salient experiences; employment representation was lower than the US population (§§3.1–3.2, 4).
- **Measurement:** Retrospective self-report, recall error and social desirability may affect accounts; no message ground truth or independent action logs (§§3, 6).
- **Comparison and confounding:** No randomization, contemporaneous expert comparison or controlled task; prior incident exposure and context may affect reported behavior.
- **Analysis:** Structured frequencies and coded stories are informative for hypothesis generation, but do not estimate causal effects. Agreement methodology needs independent statistical review (§3.3).
- **Generalizability and reproducibility:** US panel respondents able to recall suspicious emails, not representative of all inbox decisions. The published survey and OSF link improve auditability; underlying message ground truth remains absent (§§3.2, 6).

## Synthesis and questions, not authors' measured outcomes

**Interpretation:** A recipient's knowledge of what they were expecting may provide evidence that a generic suspicious-cue checklist misses. But recalling that they verified a suspicious message does not show that verification was accurate, timely or safe. High reported confidence cannot be interpreted as calibrated confidence without independently known outcomes.

**Proposed tests:** (1) In consented, unfamiliar scenarios, compare accurate context-based verification against incorrect reassurance from familiar-looking senders, measuring both false alarms and unsafe compliance. (2) Compare contemporaneously observed verification actions with subsequent recollections to estimate recall distortion. Neither test has been conducted here.

**Open limitations:** Ground truth, chronological ordering of cognitive steps, actual workplace behavior, and the accuracy of reported decisions remain unresolved. This paper is already indexed in the evidence matrix; the update is a full-text status upgrade, not a newly discovered independent study.
