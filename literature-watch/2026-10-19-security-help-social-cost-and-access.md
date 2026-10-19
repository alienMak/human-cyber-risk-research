# When help is available but asking for it carries a social cost

**Primary paper:** [Gerber and Marky, *The Nerd Factor: The Potential of S&P Adepts to Serve as a Social Resource in the User's Quest for More Secure and Privacy-Preserving Behavior*](https://www.usenix.org/conference/soups2022/presentation/gerber), SOUPS 2022, pp. 57–76. [Original full-text PDF](https://www.usenix.org/system/files/soups2022-gerber.pdf).  
**Source type:** Peer-reviewed primary qualitative research. **Publication:** August 2022. **Review date:** 19 October 2026.  
**Access:** **FULL TEXT APPRAISED** (paper sections 1–6, methods, results, limitations, appendices consulted as needed). No independent reanalysis of interview transcripts.

## What the authors actually studied

The paper investigates the *support-giver's* side of everyday security and privacy advice: when knowledgeable people advise friends or family, why they sometimes refrain, and what might make these conversations easier.

**Study I (§3, pp. 59–63):** Thirteen semi-structured video-call interviews with security/privacy-knowledgeable participants recruited through university lists, professional networks and word of mouth. All lived in Germany or the UK; participants were aged 21–56, with two women and eleven men (§3.1, pp. 59–61). Screening used established self-report scales for security intentions, attitudes, privacy concerns and literacy, plus technical affinity; these were **recruitment checks, not observed behavioral outcomes**. Interviews lasted about one hour, were transcribed and thematically analyzed. One author coded the interviews, another reviewed the coding and disagreements were discussed (§3.1, pp. 59–60).

**Study II (§4, pp. 63–66):** Three online co-creation workshops with **another eleven knowledgeable participants**, in groups of three or four. Participants brainstormed obstacles, generated and discussed possible approaches and voted on ideas. Researchers analyzed workshop boards and transcripts thematically (§4.1, pp. 63–64). This was **ideation**, not deployment or a controlled trial of an advice service.

**Intervention/comparison:** There was **no randomized intervention, no untreated control group, and no before/after measurement of recipients' security behavior**. The interview and workshop stages asked different questions of separately recruited participants; their outputs should not be compared as treatment effects.

**Outcomes/operational definitions:** Themes in reported experiences of giving or withholding advice, perceived social reactions, and workshop-generated ideas. “S&P adepts” were screened knowledgeable people, not a population sample of certified professionals. The paper deliberately avoids precise frequency reporting for most qualitative themes (§3.2, p. 61).

## Findings, with evidence locations

**Authors' finding 1: The social relationship determines whether advice is offered.** Interviewees mainly described advising people close to them, particularly family and friends. Fear of sounding intrusive, critical or preachy discouraged unsolicited intervention; several preferred conversations with other technically knowledgeable people (§§3.2.2–3.2.4, pp. 61–62; §3.2.7, p. 63). This is the support-givers' account, not a direct observation of every conversation.

**Authors' finding 2: The cost of support includes social discomfort and time.** Participants described limited opportunities to raise the topic, concern about negative reactions, difficulty communicating across knowledge levels, and the effort of answering repeated questions (§§3.2.4–3.2.7, pp. 62–63). The authors also report that most interviewees did **not** believe their advice produced a lasting change in recipients, but this was a *support-giver perception*, not a measured follow-up (§3.2.5, p. 62).

**Authors' finding 3: Workshop participants proposed less judgmental, easier-to-access help.** Ideas included creating a constructive conversation space, making knowledgeable contacts more approachable, sharing useful explanations, and reducing the burden of providing support (§§4.2.1–4.2.5, pp. 64–66). These are **proposals from participants**, not interventions proven effective.

## What this adds to the existing research trail

The [Buckmann et al. SOUPS 2025 full-text appraisal](2026-10-18-access-to-verification.md) addresses unequal access to security information and assistance from the perspective of people seeking support. Gerber and Marky add the **other side of that relationship**: someone may know how to help but avoid intervening because the conversation is socially costly. Both studies are qualitative; neither measures a reduction in real phishing incidents.

A related but distinct source, [Zhang et al., *WebAlly* (SOUPS 2021)](https://www.usenix.org/conference/soups2021/presentation/zhang-zhuohao), explores transferring visual CAPTCHA tasks to helpers. **ABSTRACT-ONLY for this run:** the publisher record reports a role-play evaluation with ten pairs of people with visual impairments and trusted contacts, across four configurations. The large full-text PDF was not retrieved for appraisal. Do **not** infer comparative effectiveness, privacy outcomes or longitudinal benefits from its abstract.

**Analysis, not a finding shared by these authors:** A verification route can be technically present yet functionally unavailable when asking for help feels embarrassing, risks criticism, or relies on a person who cannot respond in time. Social cost is a plausible dimension of access. No study above isolates its causal effect on unsafe compliance.

## Eight-domain appraisal of Gerber and Marky

| Domain | Judgment | Evidence and boundary |
| --- | --- | --- |
| Design | **Yes for exploration; no for effectiveness** | Interviews plus workshops address perceptions and ideas, not intervention efficacy (§§3–4). |
| Sampling | **Partial** | Convenience/word-of-mouth recruitment; knowledgeable UK/Germany participants; male-skewed interview sample (§3.1, pp. 59–61; §4.1, p. 64). |
| Outcomes | **Yes for qualitative themes** | Reported experiences and co-created ideas are defined; no recipient click, reporting or verified adoption outcomes (§§3.2, 4.2). |
| Confounding | **Partial** | Self-selection, prior expertise, social desirability and recall may shape accounts; no causal identification (§3.1 limitations, pp. 60–61). |
| Measurement | **Partial** | Screening instruments described; thematic coding reviewed by second author; social behavior largely self-reported (§3.1, pp. 59–60). |
| Analysis | **Partial** | Iterative thematic analysis and discussion of disagreements; no population prevalence or quantitative uncertainty estimate (§§3.1, 4.1). |
| Generalization | **Partial** | Private social networks, not workplace incident response or pressured phishing decisions; authors explicitly limit representativeness (§3.1, p. 61; §4.1, p. 64). |
| Ethics/reproducibility | **Partial** | Consent, confidentiality and recording practices described; appendix points to a codebook; raw transcripts not independently inspected (§3.1, p. 60; §4.1, p. 64; Appendix A.3). |

## Three testable questions

1. **Does social cost change verification attempts?** In a consented study with legitimate and suspicious requests, compare accessible independent help that is private/nonjudgmental with an equally accessible route requiring public escalation. Record attempted verification, safe handling of legitimate requests, response time and perceived cost. This design is **proposed**, not conducted.
2. **Who has access to trusted help when time is limited?** Record route availability and participants' perceived ability to ask for assistance, separately from whether they recognized suspicious cues. Do not assume that asking a friend is equivalent to an authoritative independent check.
3. **Does support lead to later independent action?** Measure delayed behavior on unfamiliar requests, rather than treating favorable feedback about an advice session as evidence of durable learning.

**Provisional conclusion:** “There is someone to ask” is not the same as “asking is practical.” A defensible human-centered assessment should consider the social and operational conditions of verification, while keeping individual recognition, attempted action and outcome separate.

**Open limitations:** No observed phishing outcomes in Gerber and Marky; no representative sampling; the WebAlly corroborating record remains abstract-only; no intervention effect, subgroup risk estimate or cross-vector transfer established.

**Public-IP check:** This note contains published research and general, prospective questions only. No unpublished algorithms, scoring weights, architecture, confidential data or actual participant records.
