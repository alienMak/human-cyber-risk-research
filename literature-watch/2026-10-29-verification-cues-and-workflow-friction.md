# A verification cue can be useful without making the decision more accurate

**Primary paper:** Sarah Y. Zheng and Ingolf Becker, [*Checking, nudging or scoring? Evaluating e-mail user security tools*](https://www.usenix.org/conference/soups2023/presentation/zheng), SOUPS 2023, pp. 57–76. [Original 21-page USENIX PDF, including cover and appendix](https://www.usenix.org/system/files/soups2023-zheng.pdf). No DOI is supplied in the publisher's citation; the USENIX proceedings record is the canonical identifier.  
**Source type:** Peer-reviewed conference research. **Status:** **FULL TEXT APPRAISED** on 29 October 2026, especially §§3.1–3.4, 4.1–4.2, 5.1–5.4, Table 1 and Appendix A.  
**Deduplication:** This 2023 paper was already indexed at **abstract** level in the repository's secondary evidence-matrix table and full-text priority list. This note upgrades that same study rather than adding a second publication. The authors' [2022 header-presentation experiment](https://www.usenix.org/conference/soups2022/presentation/zheng) is a distinct study, not a replication of the 2023 qualitative evaluation.

## What the authors investigated

The question was whether security information presented within ordinary email processing could help users judge message legitimacy without disrupting their main work. The researchers developed three interface concepts: a verification/check button, a colleague-report warning and a suspicion-score warning. These were **research prototypes**, not a deployed organizational reporting system (§§1, 3.3, pp. 57–62).

Twenty-seven staff members from the researchers' institution were recruited by email. They included administrative and academic roles; 19 had STEM backgrounds and 18 recalled prior mandatory cybersecurity training. Each participant attended a 45–60-minute in-person session, received a £20 voucher and processed messages as a fictional health-informatics professor in simulated Outlook inboxes. The participant was not told beforehand that phishing detection was the purpose of the exercise (§§3.1–3.2, pp. 59–60; §4, p. 62).

Each participant saw **four inboxes**: a baseline inbox without added security tools **always first**, followed by three tool inboxes in randomized order. The inboxes contained 33 legitimate and six phishing messages across the four sets, adapted to the workplace context. The interface allowed actions such as replying, deleting, forwarding, archiving and moving to junk. Participants thought aloud while working; each inbox appeared for seven minutes. This was an **iterative formative usability study**, not a randomized test of intervention efficacy or a longitudinal field experiment (§3.2, pp. 59–60).

The researchers revised the presentation of tools across **four successive participant cohorts** (8, 7, 5 and 7 people), following recurring usability feedback. The first author coded the transcripts using reflexive thematic analysis after two researchers discussed an initial transcript. The authors explicitly declined statistical detection-accuracy comparison because the fixed-time design prioritized qualitative usability (§§3.3–3.4, p. 62; Table 1; §3.2, p. 60).

## Outcomes and operational definitions

- **Observed task behavior:** Which inbox actions people selected and which cues they discussed in the simulated environment; not real incoming mail or real reporting to an IT team (§§3.2, 4.1).
- **Perceived usefulness and adoption:** Participant comments, interactions with tools, and post-task preference votes. These are usability indicators, **not** estimates of reduced phishing compromise or increased reporting (§4.2, pp. 64–66).
- **Recognition and discrimination:** Not established as an independently powered quantitative outcome. The authors explicitly say efficacy was to be described qualitatively, not through statistical comparison (§3.2, p. 60).
- **Reporting:** The colleague-report nudge displayed a warning *about* a purported colleague's report; it did **not** experimentally measure employees' own reporting frequency or a real security-team response (§3.3.2, pp. 60–61).

The authors report that nine participants preferred the suspicion-score feature, seven the check feature, four both, one the colleague-report nudge, four all three, and two none. These sum to 27 and describe preferences, not effectiveness. In earlier design iterations, 15 users did not use the check button until the researcher drew attention to it. Those observations are sensitive to tool placement and iterative changes (§§4.2, 4.2.4, pp. 64–66).

## Findings that matter, and a caution

**Authors' observations:** Participants often attended to message relevance and perceived sender relationships, yet interpreted similar cues differently. Many simply deleted suspicious or unwanted messages instead of using the junk function (§§4.1.1–4.1.4, pp. 63–64). Technical details presented by the early check-button designs were often confusing or ignored; a simplified check of past correspondence felt useful. The colleague-report nudge was often ignored or considered disruptive. The suspicion-score nudge drew attention, but some participants worried that automated warnings could produce false positives (§§4.2.1–4.2.4, pp. 65–66).

**A crucial boundary:** Past correspondence was reassuring, but it is not proof of current sender authenticity. The authors themselves warn that compromised or spoofed accounts could make this heuristic misleading, and their email set did **not** include spoofed-sender examples for that particular test (§5.1, p. 67). Also, a tool that feels productive or reassuring has not thereby demonstrated improved discrimination between benign and malicious messages.

**Analysis:** The study gives a plausible explanation for why a visible verification option may go unused: participants are occupied with ordinary communication, and they may not know how to interpret what the option reveals. It also illustrates a possible trade-off: making a cue intuitive can improve acceptance while encouraging reliance on a shortcut that fails in some threat conditions. The paper does not quantify that trade-off.

## Eight-domain appraisal

| Domain | Assessment | Source-grounded reason |
| --- | --- | --- |
| Research design | **Yes for formative usability; no for causal efficacy** | Baseline always first; tools presented later; evolving prototypes; no randomized efficacy endpoint (§§3.2–3.4, pp. 59–62). |
| Sampling | **Partial** | N=27 from one institution, volunteer staff, many with STEM backgrounds; limited representativeness (§3.1, p. 59; §4, p. 62). |
| Outcome definition | **Partial** | Think-aloud actions and preferences are defined; detection improvement, actual reporting and compromise are not quantified (§§3.2, 4.2). |
| Confounding | **Partial** | Tool order randomized after baseline, but baseline order, differing inbox messages, researcher prompts and cohort-specific design changes remain (§§3.2–3.3; Table 1). |
| Measurement | **Partial** | Simulated interface and observable task actions; seven-minute limit, researcher proximity and verbalization may affect behavior (§3.2, pp. 59–60). |
| Analysis | **Partial** | Reflexive thematic analysis and documented iterative coding; no causal estimates, accuracy CIs or quantitative tool comparison (§3.4, p. 62). |
| Generalization | **Limited** | One workplace, fictional recipient, simulated messages and no extended follow-up (§5.4, p. 68). |
| Ethics and reproducibility | **Partial** | Departmental ethics approval and consent reported; authors say transcripts, codebook and simulated materials are available through OSF/GitHub, not independently reanalyzed in this note (§§3.1, 3.4; §1). |

The 2023 study's **four tool iterations** should not be described as four independently randomized treatment arms. Preference counts must not be converted into detection-effect sizes.

## Relation to other verified sources

- **Distinct earlier paper:** [Zheng and Becker (SOUPS 2022)](https://www.usenix.org/conference/soups2022/presentation/zheng), **ABSTRACT-ONLY in this comparison**. The publisher reports that exposing suspicious header details did not improve detection; the 2023 study investigates different, more contextual tool concepts, with qualitative usability outcomes.
- **Distinct older peer-reviewed paper:** [Nguyen, Jensen, Durcikova and Wright (2021), *A comparison of features in a crowdsourced phishing warning system*](https://doi.org/10.1111/isj.12318), *Information Systems Journal* 31(3), 473–513, first published online **11 March 2021**, **ABSTRACT-ONLY**. The publisher abstract describes 438 participants evaluating emails with mock crowdsourced warning features and reports effects on judgment accuracy, adherence and anxiety. Its full-text design and effect sizes were **not** appraised; it is not evidence that the 2023 check button improved reporting.
- **Distinct randomized field study already appraised:** [Bender et al. (first online 2024; 2026 issue)](https://doi.org/10.1017/bpp.2024.19), [existing full-text note](2026-10-28-feedback-timing-and-behavioral-outcomes.md). That study measures subsequent simulated interactions and reports following feedback, not the usability of a verification button. Its results should not be pooled with this qualitative study.

No preprints, news articles or podcasts were used to support the empirical claims here.

## Lessons and open tests

1. **Noticing a cue and knowing what to do with it are separate outcomes.** A future consented study could record whether a participant notices, understands and acts on a verification cue rather than assuming that its presence implies use.
2. **Reassurance is not the same as correctness.** Compare judgment and confidence for familiar legitimate messages and plausible impersonations, including messages that appear to come from an established contact. Measure mistaken trust and mistaken rejection separately. This is a **proposed test**, not a tested intervention.
3. **Workflow fit matters, but has to be tested against accuracy.** An unobtrusive control might receive more use without necessarily improving decisions. A comparison should record task completion, unnecessary disruption, reporting or verification, and correct discrimination, with comparable messages and pre-specified endpoints.

**Open question:** If a verification aid makes someone more confident in a message, how can we tell whether that confidence is justified rather than simply easier to obtain?

**Public-IP gate:** This is a literature appraisal of published research and non-proprietary research questions. It contains no private scoring rules, proprietary implementation details, unpublished participant data, confidential organizational material, credentials or production changes.
