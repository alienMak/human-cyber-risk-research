# When click rates change, did people change or did the exercise?

**Primary paper:** Michelle Steves, Kristen Greene and Mary Theofanos, [Categorizing human phishing difficulty: a Phish Scale](https://doi.org/10.1093/cybsec/tyaa009), *Journal of Cybersecurity* 6(1), tyaa009, published 14 September 2020. [Original full text hosted by NIST](https://csrc.nist.gov/csrc/media/projects/Usable-Cybersecurity/images-media/Categorizing%20human%20phishing%20difficulty.pdf). **FULL TEXT APPRAISED** (16-page journal paper, especially pp. 3–6, 11–13; Tables 1, 13–14).  
**Version check:** [Steves et al., USEC 2019](https://doi.org/10.14722/usec.2019.23028), [original workshop paper at NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=927333), **FULL TEXT CHECKED for overlap**: seven workplace exercises. The 2020 journal paper extends the same line of work to ten exercises. **Do not count these as independent validation studies.**  
**Context only:** [Dawkins, Jacobs and Greene, M3AAWG 2021](https://www.nist.gov/publications/nist-phish-scale-method-rating-human-phishing-detection-difficulty), NIST conference/practitioner guidance, **ABSTRACT/RECORD ONLY**; [Ho et al., IEEE S&P 2025](https://doi.org/10.1109/SP61157.2025.00076), peer-reviewed field experiment, **ABSTRACT-ONLY for this comparison**; [Rozema and Davis 2025](https://arxiv.org/abs/2506.19899), **PREPRINT, ABSTRACT-ONLY**. Neither 2025 study was independently appraised in full here. No news or podcasts were used.  
**Added:** 24 October 2026. **Deduplication:** The 2020 paper was already in the evidence matrix at abstract level; this note upgrades its appraisal, not its publication count.

## What was actually studied

This was exploratory method development using ten simulated-phishing exercises conducted at NIST in ordinary workplace conditions over a multi-year program. Eight exercises targeted an operating unit of roughly 60–75 employees; two targeted thousands of staff. Some exercise data had appeared in earlier publications. Exercises were unannounced and deployed at irregular intervals, but participants in the smaller unit knew they were part of the longer trial (journal pp. 6–7, *Application of the Phish Scale*). This is not a randomized comparison of training treatments.

The proposed difficulty judgment considers visible message cues alongside how closely the request fits the recipient group's work. Ratings were assigned by the researchers with implementer input, then compared with observed exercise click rates (pp. 3–6, 11, Tables 1 and 13). **Primary outcome:** interaction with the simulated lure, usually a click or attachment interaction. In one credential-request exercise the paper separately reports 107 data entries among 439 clickers, compared with 5,024 recipients overall (p. 12). That illustrates why a click and subsequent disclosure cannot be treated as equivalent. The authors explicitly state that concurrent reporting data were unavailable for these exercises (*Future work*, p. 13).

The most difficult-rated exercises had the highest observed click rates in this small set; the authors present this as promising descriptive alignment, not definitive external validation. The 2020 journal paper extends the 2019 workshop analysis rather than replicating it in a new organization.

## Eight-domain methodological appraisal

| Domain | Judgment and checked evidence |
| --- | --- |
| Research design | **Partial.** Exploratory calibration against existing field exercises; no randomized difficulty manipulation or held-out validation set (pp. 3, 6, 11–13). |
| Sampling | **Partial.** One organization; eight small operating-unit campaigns and two institute-wide campaigns, with potentially overlapping recipients (pp. 2, 6–7; Table 13). |
| Outcome definition | **Partial.** Clicks and one downstream credential-entry outcome are separated; no simultaneous reporting endpoint (pp. 11–13). |
| Confounding | **Partial.** Context, role, prior training, lure type, audience size and campaign timing can vary together; not isolated causally (pp. 6–7, 12–13). |
| Measurement | **Partial.** Cue inventory and premise alignment are described, but rater agreement and cue salience are not established as validated measures (pp. 3–6, *Limitations*). |
| Analysis | **Partial.** Descriptive exercise comparisons; rating boundaries were informed by the same observed click data, limiting independent predictive claims (p. 11, Table 13). |
| Generalization | **Limited.** One federal research workplace and only ten distinct lures; some proposed difficulty cells were unobserved (pp. 11–12, Table 14). |
| Ethics/reproducibility | **Partial.** NIST human-subjects approval and recreated example messages are described; no independent reanalysis of underlying employee records was performed (p. 7, supplementary-material references). |

These judgments are qualitative, not an overall numerical quality score.

## A source-table discrepancy worth preserving

The journal's **Table 13, p. 11**, prints the Valentine exercise as **n=4,097** but reports **549/4,977** for its 11.0% click rate. The latter fraction rounds to 11.0%; the printed sample size does not match it. Both values are visible in the original NIST-hosted PDF, so this is not a text-extraction artifact. **Do not resolve the discrepancy by guessing which denominator is correct.** A clarification or comparison with the underlying campaign record is needed before using that exercise's sample size in secondary calculations.

## Interpretation, not a finding established by the study

A changing click rate can reflect different task demands even if people's underlying skills have not changed. Equally, similar click rates can conceal different decision paths. A role-relevant request may be persuasive for reasons that have little to do with how much security training the recipient remembers.

There is a methodological circularity risk when category boundaries are adjusted using the same exercise outcomes against which the categories are then judged. That does not invalidate the paper's exploratory contribution. It does mean that apparent fit on these ten campaigns should not be described as independently validated prediction.

## Proposed future questions, not completed experiments

1. Would an independently rated difficulty judgment retain its usefulness on unfamiliar campaigns and in different workplace roles, without adjusting the categories to the new click rates?
2. Can an evaluation separate recognition, initial interaction, subsequent verification, reporting and actual disclosure, rather than letting a click stand for the entire decision?
3. If repeated simulations become easier for a particular group, is the change retained on unfamiliar scenarios, or is it familiarity with a recurring exercise format?

**Public-IP gate:** This note describes published research, its methodological limits and general future research questions. It does not disclose unpublished VISHWAR implementation, scoring rules, weights, private architecture, confidential PR3CORIA information, credentials or actual participant-level data.
