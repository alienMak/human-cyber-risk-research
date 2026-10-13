# Zheng and Becker (2022): are visible sender details enough?

**Original paper:** [Presenting Suspicious Details in User-Facing E-mail Headers Does Not Improve Phishing Detection](https://www.usenix.org/system/files/soups2022-zheng_1.pdf), SOUPS 2022, pp. 253–271.  
**Access:** Full open-access conference paper, sections 1–4 inspected on 13 October 2026; this is a targeted methodological appraisal, not an independent reanalysis of data.

## Design and task

Between-subjects assignment to full email (Control), message/subject without headers (Headerless), or header information without body (Bodyless). Each condition had 84 participants, N=252 total. Participants were recruited through Prolific, age/gender matched to the UK population, and performed an executive-assistant email filtering task in which phishing detection was secondary (paper §3.1–3.3, printed pp. 255–256).

The task used 47 messages: 37 legitimate emails, eight phishing emails and two spam messages, around 17% phishing. Legitimate material was adapted from an Enron email corpus and phishing examples from researchers' collections and online examples (§3.4, pp. 256–258). Outcomes included classification of messages, phishing precision and recall, and limited observable URL hovering (§3–4).

## What the results show

The header-only condition did not outperform the others as hypothesized. Detection varied greatly across phishing messages, and for several lures was low in all conditions (§4.1, pp. 258–260). The study also reports few URL-hover interactions; hovering did not reliably lead to correct labeling (§4.2, printed p. 260). The results are not evidence that a single trait reliably predicts susceptibility.

## Appraisal

- **Design:** Random allocation strengthens comparison of display conditions; task remains simulated.
- **Sampling:** Age/gender matching does not imply representativeness on job role, culture, technical experience or security habits.
- **Outcomes:** Email labeling and precision/recall are observed task decisions, not real-world credential loss or later reporting.
- **Confounding:** Email-specific detectability varies; some attacks were explicitly not reasonably identifiable under certain display conditions (§3.4).
- **Measurement:** Real rendered emails and link-hover logging improve realism relative to screenshots; the executive-assistant cover task is still constructed.
- **Analysis:** The paper reports message-level tests and regression analyses (§4). This note does not independently recalculate estimates or assess all assumptions.
- **Generalization:** UK-recruited adults and email only; not a validation for voice, physical attacks or conversational AI.
- **Ethics/reproducibility:** Paper reports ethics review, compensation and a linked OSF materials repository (§3.1, §3.5).

## What follows

Providing an authenticity cue is not equivalent to helping someone interpret it. A subsequent study should separate **cue availability**, **cue comprehension** and **independent verification**. Do not infer that hiding email bodies is an effective intervention or that participants possess stable individual risk scores.

**Source-location check:** original paper §§3.1–3.6 and 4.1–4.3. The broader eight-domain rubric in [quality appraisal](../quality-appraisal.md) remains applicable; this targeted appraisal does not claim full statistical replication.
