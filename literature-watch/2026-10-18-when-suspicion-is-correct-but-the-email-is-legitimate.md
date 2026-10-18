# A suspicious email can still be legitimate

**Study:** [Rick Wash, Norbert Nthala and Emilee Rader, *Knowledge and Capabilities that Non-Expert Users Bring to Phishing Detection*](https://www.usenix.org/system/files/soups2021-wash.pdf). SOUPS 2021, pp. 377–396.  
**Type:** Peer-reviewed primary empirical paper. **Review status:** FULL TEXT APPRAISED, §§3–6. **Added:** 18 October 2026.

## What the authors investigated

The researchers surveyed **297 U.S. non-expert email users** recruited through a Qualtrics panel in February 2020. Age, gender and ethnicity quotas approximately matched the U.S. population; employment differed (§3.2, p. 380). Respondents were asked to recall **one** suspicious or potentially harmful email and describe what they noticed, expected, investigated, decided and did. **315 otherwise eligible respondents who could not recall such an email were screened out** (§§3.1, 4, pp. 380–382). There was no randomized intervention or contemporaneous observation of inbox behavior.

The survey included structured self-report and narratives. Two coders independently coded 297 stories using a 39-code scheme, reconciled differences and excluded 13 narratives that did not describe an incident (§3.3, p. 381). The paper distinguishes coded stories from responses to survey questions. Replication materials: https://osf.io/82sd9/.

**Outcomes:** reported expectations, suspicious cues, investigation actions, final classification and actions after the decision. There was **no independently verified ground truth for all emails**, no actual attack-rate denominator and no observed prospective transfer or training effect (§6, p. 388).

## What changes the interpretation

**Authors' findings:** 95% of respondents said their recalled suspicious email was unexpected, while 72% said it resembled emails they had received before (§4.3, p. 384). Nearly all respondents identified a requested action (§4.4, p. 385). The authors argue that ordinary users possess context unavailable to technical filters: whether a message fits their relationships, history and expectations (§§5.2–5.3, pp. 387–388).

One participant's account describes receiving a fraud-alert message, doubting its authenticity, ending an unproductive call to the number in the email, then contacting the firm through a familiar number and learning that the email **was legitimate** (§4.4, pp. 384–385). This is a *self-reported case*, not independently verified proof of the sender's identity.

**Twin's challenge:** An initial suspicion can be justified even when a message is genuine. Treating every suspicious message as a true attack would make cautious checking look like false judgment. Conversely, accepting a legitimate message after verification can be appropriate; safe behavior is not equivalent to blanket rejection.

## Competing explanations and evidence limits

1. **Context-sensitive judgment:** a user compares the request against prior interactions and resolves uncertainty through an independent route.
2. **Generalized suspicion:** a user rejects anything unexpected, including legitimate communication.
3. **Retrospective reconstruction:** the remembered story overstates how systematic or successful the original investigation was.

The paper supports that people *report* contextual comparison and investigation. Its retrospective design cannot distinguish these explanations reliably for an individual case, reconstruct the order of cognition, or show that a particular checking step caused safety (§§5.2, 6, pp. 387–388). The authors explicitly acknowledge selection and recall bias.

## Eight-domain appraisal

| Domain | Assessment | Evidence |
| --- | --- | --- |
| Research design | Partial | Retrospective survey fits reported practices, not causal inference (§3). |
| Sampling | Partial | Quota panel, 297 valid responses; recall-based exclusion of 315 eligible respondents (§§3.1–3.2). |
| Outcome definition | Partial | Six reported activities, no independent ground truth or prospective outcome (§§3.1, 6). |
| Confounding | Partial | Incident memorability, elapsed time and prior experience may influence accounts (§§4.1, 6). |
| Measurement | Partial | Structured questions and narrative coding; recall and social-desirability limitations (§§3.1, 3.3, 6). |
| Analysis | Partial | Dual-coded stories and reconciled discrepancies; no causal effect estimate (§3.3). |
| Generalization | Partial | U.S. panel and remembered suspicious emails, not all incoming messages (§§3.2, 6). |
| Ethics/reproducibility | Partial | Replication materials linked; participant incentives described; independent replication not performed (§§3.2–3.3). |

## Research questions, not established effects

1. Can a study distinguish **correct rejection of a malicious request** from **correct acceptance of a legitimate request after independent confirmation**?
2. Do people make different decisions when they can use their own contextual knowledge instead of only the message's visible technical cues?
3. How accurately do retrospective accounts describe the actual sequence of suspicion, checking and final action?

A future prospective comparison could include legitimate and suspicious communications, separately observe verification routes and eventual decisions, and assess false alarms. It would need ethical review and independent validation of message legitimacy. This is a general research proposal, not a published method or proprietary scoring design.

**Related existing coverage:** [verification and transfer questions](../literature-review/verification-and-transfer-questions.md) and [verification after mismatch](2026-10-18-verification-after-mismatch.md). Unlike the adversarial Signal laboratory study, this study relies on participants' recollections; the two should not be pooled.

**Question for researcher review:** If someone initially distrusts a legitimate request, then verifies it independently and proceeds, should that count as a security mistake or a successful decision?

**Public-IP review:** Only published evidence and general research questions; no proprietary implementation, algorithms, confidential information or participant data.
