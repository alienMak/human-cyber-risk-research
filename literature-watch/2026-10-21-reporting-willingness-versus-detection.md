# If reporting increases, has detection improved?

**Evidence:** [Chen et al., SOUPS 2024](https://www.usenix.org/conference/soups2024/presentation/chen); [Li et al., SOUPS 2026](https://www.usenix.org/conference/soups2026/presentation/li).  
**Evidence status:** Publisher abstracts verified for this comparison; Chen has a separate full-text appraisal in this repository, and Li has a separate full-text appraisal. This note does not claim a new full-text reading.  
**Date:** 21 October 2026.

More reports might mean that people recognize suspicious messages better. They might also mean that people are more willing to ask for help when uncertain. Those are different changes, and I do not want to call both an improvement in detection without testing them.

Chen and colleagues used seven focus groups with 34 university employees. Their abstract reports that feedback, perceived usefulness, privacy concerns and social context shaped attitudes toward phishing interventions and reporting. The study explores motivations; it does not establish a causal effect of feedback on detection.

Li and colleagues surveyed 1,074 students at five US universities. Their publisher abstract reports differences in responses to scam scenarios between international and domestic students despite no observed difference in suspicious-cue detection. The comparisons concern student groups and reported scenario responses, not the effects of an experimental reporting intervention.

## What should be measured separately?

- **Recognition:** Did the person identify relevant suspicious cues? Include legitimate examples to measure mistaken suspicion.
- **Reporting willingness:** Did the person choose to seek help or alert a reporting channel?
- **Reporting precision:** Of the messages reported, how many were actually suspicious?
- **Reporting coverage:** Of the suspicious messages encountered, how many were reported?
- **Verification:** Did the person attempt to establish authenticity before acting?
- **Response:** What action followed, and was it appropriate for the true status of the request?

These are conceptual outcome definitions, not results or a proprietary scoring method. Precision and coverage require known ground truth and complete observation of the relevant messages; neither should be inferred from raw report counts alone.

## The next research test

A consented study could vary the clarity and reassurance of reporting feedback while keeping message sets comparable. It should include legitimate and suspicious requests and record recognition, reporting and verification separately. A rise in reporting with unchanged recognition would support a different interpretation from improved recognition with unchanged reporting. Workload, reporting access, prior training and scenario difficulty would remain potential confounders.

**Next question:** If reporting becomes easier and employees submit more uncertain cases, how do we evaluate the benefit to collective detection against the extra review burden and the risk of false alarms?

This note is a public research question, not an implemented system or a claim of validated predictive performance. It contains no private architecture, scoring weights, unpublished results or participant data.
