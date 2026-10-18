# A recorded action does not record the reason

**Primary study:** [Bonné, Peddinti, Bilogrevic and Taft, *Exploring Decision Making with Android's Runtime Permission Dialogs Using In-Context Surveys*](https://research.google/pubs/exploring-decision-making-with-androids-runtime-permission-dialogs-using-in-context-surveys/), SOUPS 2017. **Access this cycle:** ORIGINAL PUBLISHER ABSTRACT, not full text.  
**Methods context:** [Distler et al., *A Systematic Literature Review of Empirical Methods and Risk Representation in Usable Privacy and Security Research*](https://doi.org/10.1145/3469845), ACM TOCHI 2021, open-access full article, especially §4.2.4. **Access this cycle:** FULL TEXT SECTION REVIEWED, not a fresh complete-paper appraisal.  
**Added:** 18 October 2026.

## The question

If a system records that someone allowed a permission, clicked a link, or checked a sender, can we conclude that the person trusted the request, understood the implications or followed a particular line of reasoning?

**No.** The recorded action and its timing can establish the observable event; the motive requires additional evidence and remains subject to uncertainty.

## What the sources establish

**Bonné et al. (SOUPS 2017):** A longitudinal in-context survey asked **157 Android users** about permission decisions immediately after those decisions over **six weeks**. The publisher abstract reports that participants granted **84%** of permission requests and said they were comfortable with **90% of granted permissions**. Expectations about whether an app should need a permission and the ability to change permissions later were among reported reasons. **Interpretation:** granting a permission and feeling comfortable about it are not identical. The abstract does not independently validate each reported reason, establish the psychological cause of granting or demonstrate that in-context surveys perfectly recover cognition. **Status: ABSTRACT-ONLY.**

**Distler et al. (TOCHI 2021):** The authors systematically reviewed **284 human-subjects studies** selected from 633 initially identified security/privacy-and-usability-related papers published in five venues in 2014–2018. They categorized response measurement as observational, self-reported or a combination. In their Table 10, **131 of 284 studies (46%)** combined observation and self-report, while **119 (42%)** used self-report alone. The authors caution against assuming that combining methods is automatically preferable: the appropriate choice depends on whether a study seeks subjective perceptions, observed behavior or both (§4.2.4). This is a methods review, not a causal test of how accurately people explain their decisions. **Status: ORIGINAL OPEN-ACCESS ARTICLE, §4.2.4 REVIEWED; NOT a full eight-domain appraisal.**

## Twin's competing explanations

A participant who grants access but later expresses discomfort might have acted because of urgency, perceived necessity, a mistaken belief that the action was reversible, or an entirely different reason. The study abstract alone cannot identify the causal mechanism for an individual.

Likewise, a security simulation's click trace can show what happened and when, but not whether the participant recognized the danger, felt pressured, misunderstood the request or intended to verify later. An immediate self-report provides useful contextual evidence, **not** a privileged view into cognition.

## What a careful research report would separate

| Evidence type | Can support | Cannot alone establish |
| --- | --- | --- |
| Timestamped action trace | Observable sequence and timing in the instrumented environment | Private motivation or off-platform checking |
| Immediate in-context question | Participant's contemporaneous reported reason or comfort | Objective truth of that reason or freedom from demand effects |
| Later interview | Remembered interpretation and meaning assigned to the event | Exact original sequence or absence of hindsight reconstruction |
| Independently verified outcome | Whether the particular action was appropriate under known ground truth | Why the participant chose it |

**Proposed methodological test, not an implemented feature:** With consent, compare observed task actions, immediate self-reports and later accounts for the same event. Record agreement and disagreement separately; account for missing traces, participant reactivity, privacy and unequal observation opportunities. Do not interpret disagreement automatically as deception or error.

## Appraisal boundaries and next reading

The Bonné source is **abstract-only** here; full-text methods, sampling and attrition, event counts, prompts and analyses remain unverified. For Distler, the article's methods taxonomy and Table 10 were inspected, but its entire review has **not** been newly appraised. The two studies answer different questions and cannot be pooled.

**Researcher review question:** If someone says they felt unsafe granting a permission but granted it anyway, should the record call that trust, compliance, resignation, or an unresolved motive?

**Public-IP check:** Published methodological evidence and generic research questions only. No unpublished assessment mechanisms, proprietary formulas, internal architecture, private participant records or confidential organizational information.
