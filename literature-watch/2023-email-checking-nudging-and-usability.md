# A security check is useful only when it fits the task

**Paper:** [Checking, nudging or scoring? Evaluating e-mail user security tools](https://www.usenix.org/conference/soups2023/presentation/zheng) ([publisher PDF](https://www.usenix.org/system/files/soups2023-zheng.pdf))  
**Authors:** Sarah Y. Zheng and Ingolf Becker  
**Published:** SOUPS 2023, August 2023, pp. 57–76  
**Type:** Peer-reviewed conference paper; no DOI listed by USENIX  
**Status:** FULL TEXT APPRAISED, 13 October 2026 (21-page publisher PDF)  
**Attribution:** Source-based review; not a claim that the repository owner personally read or endorsed it.

## What was tested

This was a **formative qualitative usability evaluation**, not a randomized field trial of phishing prevention. **27 professional e-mail users** recruited at one research institution completed 45–60-minute in-person think-aloud sessions. Everyone first used a simulated Outlook inbox without new features, then three inboxes with a **check button**, **colleague-report nudge** or **suspicion-score nudge** in randomized order. Across inboxes, there were 33 legitimate and six phishing messages adapted to the workplace setting. See §3.1–3.3, pp. 59–62.

The authors iterated the interface designs over four groups of participants and used reflexive thematic analysis of transcripts and observations. Each inbox was presented for seven minutes. The paper explicitly says this method traded off measuring detection accuracy for reproducible qualitative observation. **Measured outcomes** were interaction, reasoning, usability feedback and tool preference; not verified attack resistance, longitudinal learning or actual reporting to an organization. See §3.2, §3.4, pp. 59–62.

## What the authors observed

Participants often judged e-mails by task relevance first and moved to security reasoning when something appeared unexpected. The same cue could lead different users to opposite judgments. Many deleted suspicious e-mails instead of selecting *Junk*. That does not establish whether they would report a real incident. See §4.1, pp. 63–64.

In post-task preferences, **nine** selected only the suspicion-score nudge as most useful, **seven** only the check button, **four** both, **one** only the colleague-report nudge, **four** all three and **two** none. These are **preference counts, not effect sizes**. The check button was initially overlooked: **15** participants did not use it before the researcher prompted them. Past-correspondence information was often considered useful; the colleague-report nudge was commonly ignored or disruptive. See §4.2 and Table 1, pp. 62–66.

The authors' §5.4 is explicit: the designs were not tested with live users over time, and demographic differences in design effectiveness were not established. See pp. 67–68.

## Eight-domain appraisal

| Domain | Assessment | Basis |
| --- | --- | --- |
| Design | Yes for formative usability; no for causal efficacy | Baseline always first, later tool order randomized, iterative redesign and researcher prompts (§3.2–3.3). |
| Sampling | Partial | N=27 from one institution, many with technical backgrounds (§3.1; §4). |
| Outcome definition | Yes for usability; no for real-world effectiveness | Think-aloud, observation and preference; accuracy comparison not intended (§3.2; §4.2). |
| Confounding | Partial | Researcher presence, prompting, order and evolving designs (§3.2–3.3). |
| Measurement | Partial | Transcripts and codebook, no field losses or long-term behavior (§3.4; §5.4). |
| Analysis | Yes for stated qualitative method | Reflexive thematic analysis; no statistical intervention comparison (§3.4). |
| Generalization | Partial | Simulated institutional inbox and narrow participant group (§5.4). |
| Ethics/reproducibility | Partial | Departmental ethics approval and materials reported; independent replication not verified (§3.1; §1). |

## Interpretation and next question

**Interpretation, not an author finding:** Providing a verification feature and getting someone to use it are separate problems. A person may delete a suspicious e-mail without using the reporting channel. Conversely, past correspondence can be reassuring without proving the sender's account is safe; the study did not test account compromise.

**Proposed tests, not completed studies:** (1) Measure noticing a verification feature, using it, interpreting the result, reporting and avoiding an unsafe action as distinct outcomes. (2) Compare verification support with and without time pressure while recording task interruption. (3) Evaluate in a live or ecologically valid workflow before claiming reduced phishing susceptibility.

**Boundary:** The paper's *suspicion score* was an interface nudge, not a validated personal behavioral-risk measure. No private platform methods are described.
