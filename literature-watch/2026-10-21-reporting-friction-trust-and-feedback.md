# If reporting is easy, why might someone still choose not to report?

**Paper:** Xiaowei Chen, Sophie Doublet, Anastasia Sergeeva, Gabriele Lenzini, Vincent Koenig and Verena Distler, [What Motivates and Discourages Employees in Phishing Interventions: An Exploration of Expectancy-Value Theory](https://www.usenix.org/system/files/soups2024-chen.pdf), SOUPS 2024, pp. 487–506.  
**Type:** Peer-reviewed qualitative study. **Access:** FULL TEXT APPRAISED against the original USENIX PDF, particularly §§3, 4.2, 4.3, 5.4 and 6. **Recorded:** 21 October 2026.  
**Deduplication:** This paper already appears in the repository's evidence matrix at abstract level. This note adds a focused full-text appraisal rather than presenting it as a newly found study.

## What the authors actually investigated

The researchers conducted seven focus groups with 34 employees of one European university between November 2022 and January 2023. Recruitment produced 45 expressions of interest; 34 participated. The sample comprised 19 researchers, 12 administrative staff and three software developers (§3.2, p. 490). The sessions explored motivations, deterrents and desired improvements for phishing training and email reporting using expectancy-value theory. These were discussions of participants' experiences and expectations, not an experiment assigning people to different reporting interfaces.

The organization already ran monthly simulated phishing messages. Reporting a simulation generated a rapid automated response, while staff manually checked other reported emails, typically replying within one or two working days (§3.1, pp. 489–490). That context matters: participants' beliefs were shaped by a particular existing reporting system.

## Findings that sharpen the question

The paper identifies several reasons participants said they might not report: not knowing whether reporting made a difference, receiving no meaningful feedback, expecting extra messages or questions, worrying about burdening IT, privacy concerns, fear of being judged, and difficulty reporting on certain devices (§4.2.2, pp. 493–494). Some participants described a missing report button after a software update or uncertainty about the preferred submission format. Others said they tended to delete suspicious messages on phones because reporting was cumbersome.

Participants also described reasons to report: helping colleagues, improving filtering, getting reassurance from IT and contributing to organizational protection (§4.2.1, p. 493). These are accounts of perceived benefits, not verified measurements of how often reports prevented harm.

One particularly useful distinction is between **effort** (how hard the process is), **trust or perceived effectiveness** (whether it helps), and **social cost** (whether the person expects judgment or extra work). The authors discuss all three, but did not experimentally isolate their independent effects.

## Eight-domain appraisal

| Domain | Judgment | Evidence |
| --- | --- | --- |
| Design | Yes for exploratory perceptions; no causal intervention test | §3 |
| Sampling | Partial: voluntary participation from one university, 34 of 45 interested employees | §§3.1–3.2, 6 |
| Outcomes | Partial: motivations and intentions, not directly observed reporting rates | §§3–4 |
| Confounding | Partial: role, prior exposure, existing campaign and group dynamics may shape responses | §§3.1–3.3, 6 |
| Measurement | Partial: refined focus-group protocol and theory-led analysis; self-report and group discussion | §§3.3–3.4 |
| Analysis | Partial: qualitative thematic/theory-guided analysis; no estimated causal effect or population prevalence | §§3.4, 4, 6 |
| Generalization | Limited: single European university and distinctive reporting workflow | §§3.1, 6 |
| Ethics and reproducibility | Partial: described participant procedures and supporting materials; raw transcripts not independently replicated in this note | §§3, 6; appendices |

The authors themselves note possible self-selection, dominant speakers, perceived power differences and limited transferability (§6, p. 498). A finding that participants *describe* fear of judgment should not be rewritten as proof that judgment caused a particular non-reporting event.

## What I think follows

A verification route can be easy to find without feeling safe to use. Equally, a trusted reporting team may still be difficult to reach during a busy workday. Treating both situations as the same failure of awareness obscures the intervention that might help.

**Proposed test, not conducted:** Compare a clearly available reporting channel with one that additionally explains what happens to a report and offers non-punitive feedback. Measure perceived effort, trust, expectations about consequences, verification attempts, actual reporting choices and false reports of legitimate messages separately. Pre-register primary outcomes and consider the effects of job role, device and workload.

**Next question:** If employees report more often after receiving reassuring feedback, are they becoming better at recognizing suspicious requests, or merely more willing to send uncertain cases to IT? Those are not the same outcome.

This is a public literature appraisal and future research question. It contains no private VISHWAR scoring, confidential implementation, unpublished results or participant records.
