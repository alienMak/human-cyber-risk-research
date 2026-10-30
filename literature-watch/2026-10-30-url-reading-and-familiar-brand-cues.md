# A familiar name in a link is not evidence of its destination

**Paper:** Sara Albakry, Kami Vaniea and Maria K. Wolters, [*What is this URL's Destination? Empirical Evaluation of Users' URL Reading*](https://doi.org/10.1145/3313831.3376168), CHI 2020, paper 41, 12 pp. [Author-hosted full paper](https://tulipslab.org/papers/albakry2020.pdf); [ACM publication record](https://doi.org/10.1145/3313831.3376168).  
**Publication:** 23 April 2020 (ACM record); the authors report collecting survey data in April 2017 (§Methods > Recruitment, p. 6).  
**Source type:** Peer-reviewed ACM conference paper. **Review status: FULL TEXT APPRAISED, 30 October 2026**, original 12-page author PDF, pp. 1–10, including Methods, Results, Discussion and Limitations. The author PDF was not byte-compared with ACM's hosted PDF.  
**Deduplication:** This paper was not found in the existing evidence matrix or screening register by title, DOI or author before addition. It is distinct from [Zheng and Becker (SOUPS 2022)](https://www.usenix.org/conference/soups2022/presentation/zheng), previously fully appraised in this repository, and their [SOUPS 2023](https://www.usenix.org/conference/soups2023/presentation/zheng) usability study.

## What the authors investigated

The authors asked whether people can identify the likely destination of a URL, and whether that prediction relates to how safe they *think* the link would be to click. This was an online **survey and repeated URL-judgment task**, not a phishing-training intervention, live inbox experiment or observed click-through study (Introduction and Methods, pp. 1, 4–6).

Participants were recruited from Amazon Mechanical Turk and Prolific. Of 2,030 survey completers, 101 were excluded under the authors' screening rules, leaving **1,929 analyzed respondents**. Each saw **23 URL examples** in randomized order, covering simple domains, recognizable names in domain versus subdomain positions, shortened links and more complex URL forms. The subdomain trials were split into alternative sets to avoid repeating the same organization for a participant. The questionnaire asked for the expected destination and perceived safety on a five-point scale if the link appeared in an email from someone known to the respondent. Respondents did **not** navigate to the links (Methods > Survey Instrument, URLs Tested, Recruitment and Participants, pp. 4–6).

The analysis used latent-class grouping based on self-reported technology use, mixed-effects models for destination judgments and ordinal regression for perceived safety. These groupings are **observational**, not randomized training conditions. The authors ran prestudies to select familiar and less familiar organization names and refine the instrument (Methods, pp. 3–7).

## What the authors found, with denominators

For the **12 single-subdomain judgments**, participants answered an average **6.4/12** correctly. The average was **5.2/6** when the recognizable organization appeared in the domain position, but **1.2/6** when it appeared in the subdomain position. In the Results, the authors report **161 respondents (8.3%)** consistently selecting the correct domain across these questions, versus **623 (32.2%)** consistently selecting the recognizable organization name regardless of its position (Results > Single Subdomain URLs, pp. 8–9, Figure 3 and Table 3).

Participants tended to rate URLs as safer when they believed the link would lead to the familiar named organization. For single-subdomain links the reported median perceived safety was **4/5**, versus **2/5** for shortened links. These are **subjective ratings under a hypothetical email-from-an-acquaintance prompt**, not observed safe or unsafe actions (Results > Perceived Safety, p. 9).

The researchers also report that heavier technology use was associated with only modestly better URL-reading performance. This is a relationship between measured URL judgments and survey-derived technology-use groups, **not** evidence that any demographic characteristic predicts actual victimization (Results > User Groups and Single Subdomain URLs, pp. 7–9).

## What the study does not establish

- **No actual phishing or verification behavior:** Participants predicted destinations and rated safety. They did not receive workplace messages, use an email verification tool, click real links, report suspicious messages or experience a compromise.
- **No causal test of a warning or training intervention:** The study did not randomize participants to URL explanations, warnings or instruction.
- **Limited external validity:** Online crowdworker recruitment, synthetic URL examples, familiar repeated filler terms, and a hypothetical safety prompt differ from an ordinary workday. The authors explicitly note that “safety” could have meant security, privacy or other concerns to different respondents (Methods > Limitations, p. 7).
- **Some numerical presentation needs reconciliation:** The PDF states a final analyzed sample of 1,929, but its three printed latent-class counts (761, 367, 806) sum to **1,934**, and its alternative URL-set allocations (984 and 950) also sum to 1,934 (Methods > Participants and URLs Tested, pp. 5–7). The Introduction gives 32.9% for a consistently brand-based answer while the Results gives 32.2%. These differences are **unresolved in this review**. Do not derive or reuse subgroup denominators from these passages without checking supplementary data or contacting the authors.
- **No independent replication:** This appraisal checked the original full text and publisher metadata; it did not rerun the released data or inspect the complete survey dataset.

## Eight-domain appraisal

| Domain | Assessment | Basis |
| --- | --- | --- |
| Research design | **Yes for descriptive URL judgments; no for intervention efficacy** | Repeated URL tasks and hypothetical ratings, no randomized support intervention (Methods, pp. 4–6). |
| Sampling | **Partial** | Two crowdworker platforms and explicit exclusions, but nonprobability sample and unresolved printed subgroup counts (Participants and Limitations, pp. 6–7). |
| Outcome definition | **Yes for destination choice; partial for safety** | Multiple-choice destination and five-point perceived safety; authors acknowledge variable interpretation of “safety” (Survey Instrument; Limitations, pp. 4, 7). |
| Confounding | **Partial** | Familiarity prestudies, randomized question order and alternative URL sets; repeated filler words and brand familiarity remain relevant (Methods, pp. 3–7). |
| Measurement | **Partial** | URL screenshots and forced-choice responses measure prediction, not real clicking or actual control of a destination (Methods, pp. 4–5). |
| Analysis | **Partial** | Mixed models and latent classes described, but full model coefficients omitted and some subgroup totals conflict (Survey Analysis; Results, pp. 6–9). |
| Generalization | **Limited** | Online survey in 2017, not a natural inbox or a field experiment (Recruitment; Limitations, pp. 6–7). |
| Ethics/reproducibility | **Partial** | Institutional ethics procedure and survey dataset reference reported; independent reproduction not undertaken (Recruitment; Survey Instrument, pp. 4–6). |

## Relation to the existing evidence

[Zheng and Becker (SOUPS 2022)](https://www.usenix.org/system/files/soups2022-zheng_1.pdf), **previously FULL TEXT APPRAISED**, randomized the amount of email header/body information shown in a simulated classification task. It found that header-only display did not improve phishing labeling. Albakry et al. measured a more basic prerequisite: whether the URL's apparent destination was understood at all. The studies **do not share an outcome or a common effect estimate**.

[Zheng and Becker (SOUPS 2023)](https://www.usenix.org/system/files/soups2023-zheng.pdf), **previously FULL TEXT APPRAISED**, studied the usability of email verification and warning concepts with 27 professional users. Preference and perceived reassurance were not validated improvements in phishing discrimination. The three studies together motivate a research distinction; they do not prove that a particular verification aid works.

[Chen, Paxson and Jiang (USENIX Security 2020)](https://www.usenix.org/conference/usenixsecurity20/presentation/chen-jianjun), **PUBLISHER ABSTRACT CHECKED ONLY for this comparison**, describes technical sender-authentication bypasses. It is systems-security evidence, not a behavioral estimate, and cannot be used to infer the frequency of misleading cues in the present survey.

No preprints, news items or podcasts were used as empirical corroboration in this update.

## Research lessons and next questions

1. **Recognizing a brand name is not the same as identifying who controls a destination.** A visible link may be read fluently but interpreted incorrectly. Future work should measure destination comprehension separately from whether a cue was noticed.
2. **Perceived safety can follow a mistaken destination judgment.** This is an association in hypothetical ratings, not evidence that participants would actually click. A consented comparison could measure destination choice, confidence, verification and final action separately for familiar legitimate and misleading-looking links.
3. **Uncertainty deserves its own outcome.** When a shortened or unfamiliar link cannot be judged from the text alone, recognizing that limitation may be more appropriate than guessing. Future research could distinguish justified uncertainty and help-seeking from both mistaken trust and indiscriminate rejection.

**Open question:** When a message contains a recognizable name, does a verification aid improve understanding of the actual destination, or only increase confidence in an existing interpretation?

**Public-IP gate:** This note contains only public-source analysis and non-proprietary research questions. No private algorithms, scoring weights, unpublished architecture, participant records, confidential organizational information, credentials or production code are included.
