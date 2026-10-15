# From recognizing a threat to deciding what to do

**Research agenda note — 15 October 2026**  
**Status:** Questions and testable alternatives, not a completed study or a validated behavioral model.

A phishing exercise often records whether someone clicked. That is useful, but it leaves an important gap: what did the person recognize, what options did they believe they had, and what happened after they became uncertain?

## Two different problems

**Recognition:** Does the person correctly distinguish suspicious from legitimate requests? An apparent improvement might instead be a more conservative tendency to reject everything. Both missed threats and false alarms matter.

**Action after recognition:** When someone suspects a request is unsafe, do they verify it, defer it, report it, refuse it, or comply anyway? Recognition and action need not coincide. Neither a click nor a non-click by itself identifies the reasoning behind it.

## Evidence that motivates the distinction

- [Nicholson, Coventry and Briggs, SOUPS 2017](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson): publisher-reported sender-salience detection benefit and poorly calibrated confidence. **Publisher abstract corroborated; no new full-text appraisal here.** This supports distinguishing discrimination from confidence, not a claim about social pressure.
- [Hasegawa et al., SOUPS 2021](https://www.usenix.org/conference/soups2021/presentation/hasegawa): survey of 862 non-native English speakers; the authors report unverified ignoring of English-language messages. **Previously documented full-text working appraisal; no new independent reappraisal here.** The outcomes are hypothetical choices, not observed workplace compliance.
- [Weidhaas, von Preuschen and Distler, SOUPS 2026](https://doi.org/10.60882/cispa.32775066): qualitative simulated-workplace research with 41 participants; the publisher abstract describes reputational concerns about not clicking. **ABSTRACT-ONLY.** It does not show that authority pressure caused compliance after recognition.
- [Distler, CHI 2023](https://doi.org/10.1145/3544548.3581170): in-situ deception and workplace context. **ABSTRACT-ONLY in this agenda; full methods not re-extracted.**
- [Li et al., SOUPS 2026](https://www.usenix.org/conference/soups2026/presentation/li): publisher abstract reports differences in scam responses among university student groups. **ABSTRACT-ONLY.** Check outcome definitions and adjustments before drawing group-level conclusions.

These sources use different populations, tasks and outcomes. Their findings should not be combined into an effect estimate.

## Competing explanations worth testing

1. **Recognition without action:** A person suspects a request is malicious but acts anyway because refusal or delay appears costly. A future study should distinguish perceived authority, time pressure and reputational concerns rather than assuming they are one mechanism.
2. **Recognition without a usable verification route:** A person suspects a problem but cannot identify an accessible, trusted way to check. The prediction is that a usable verification opportunity could change the eventual decision even when initial recognition stays similar.
3. **Avoidance without recognition:** A person ignores suspicious and legitimate requests indiscriminately. Lower interaction rates could conceal more false alarms rather than improved discrimination.
4. **Familiarity without transfer:** Repeated exposure improves performance on recognizable examples but not unfamiliar requests or channels.

These are **proposed explanations**, not conclusions established by the cited papers.

## Measurement questions for future independent research

A study could separately observe initial classification, confidence, attempted verification, deferral, reporting and final action, including legitimate requests. Report correct identification of malicious requests alongside mistaken rejection of legitimate ones. When feasible, compare immediate and later performance on different but comparable material. Record task context, language, accessibility, prior exposure and whether verification was realistically available.

Self-reported motives should be labeled as such; they do not establish the causal reason for an action. A study of social pressure would need a defensible comparison and ethical review, not just an interview question asking why a participant clicked.

## What to read before designing an experiment

Read the full texts of Weidhaas (2026), Distler (2023) and Li et al. (2026); extract recruitment, stimuli, operational definitions, comparisons, coding or statistical analysis, limitations and exact page evidence. Revisit the full Nicholson (2017) and Hasegawa (2021) methods before making cross-study claims. The [reading priority list](full-text-priority.md) tracks these gaps.

## Questions for review in the researcher's own voice

- When someone knows a request looks wrong, what makes refusing it harder than recognizing it?
- Is an increase in non-clicks better judgment, or simply a greater willingness to ignore legitimate work?
- Does a practical route to verification matter more than another warning?

**Public-boundary check:** This document describes open research questions only. It contains no unpublished platform architecture, scoring logic, participant records or confidential project details.
