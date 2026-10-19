# QT-009 — Can a good average hide unequal protection?

**Earlier documented context:** October 2026 — Public research notes on differential access to security support and on the gap between a specified control and a usable one. The first personal discussion date is not established.  
**Origin:** A new research question arising from published usable-security studies and the existing verification-access trail. This is a reasoned reconstruction, not a quotation from a private conversation.  
**Status:** Open; methodological analysis, not a completed subgroup study.

## Brief

An organization can report strong overall security performance while some people have much less practical access to the protection being measured. That is not a paradox: an average can describe the whole sample accurately and still obscure a consequential difference within it. But a subgroup gap is not automatically evidence of discrimination, deficient knowledge or a defective control. We need to understand who faced which tasks, what they could reasonably do and how uncertain the estimate is.

This trail extends [QT-005](QT-005-what-does-a-risk-score-mean.md), which asks whether aggregate scores mean what we think, and [QT-008](QT-008-verifying-an-account-versus-the-request.md), which distinguishes verification from authorization. Its distinct question is **how protection and opportunity are distributed across people and contexts**.

## Question chain

| Step | Question | Working answer | Why the next question follows |
| --- | --- | --- | --- |
| Q1 | Could an apparently good organization-wide result coexist with poor outcomes for a smaller group? | Yes, as a mathematical possibility. A weighted average can be dominated by the larger group. | Are the groups even facing comparable decisions? |
| Q2 | Does a subgroup difference prove one group has less security knowledge? | No. Scenario difficulty, language, accessible interfaces, job role, workload and verification opportunity can differ. | Could a control exist but protect groups unequally? |
| Q3 | If everyone has the same written procedure, does everyone have the same protection? | Not necessarily. Discoverability, assistive-technology compatibility, support and practical authority may differ. | How would we distinguish access from actual use? |
| Q4 | If a group rarely uses verification, does that establish that its members are careless? | No. They may not know the route, may not be able to use it or may face a disproportionate cost. Equally, a route could be accessible but unused for other reasons. | What evidence distinguishes those explanations? |
| Q5 | Is a high attack-rejection rate sufficient to call a subgroup protected? | No. It might reflect rejecting legitimate work indiscriminately. Legitimate and malicious cases, false alarms and safe escalation all matter. | How should outcomes be compared fairly? |
| Q6 | Can a small subgroup's apparent gap be interpreted confidently? | Not without uncertainty and adequate independent observations. Ten responses from one person are not ten independent people. | What claim could the current literature actually support? |
| Q7 | Do the available studies show a quantified organization-wide gap in phishing protection? | No. They document barriers and experiences in different settings; they do not supply the same organizational subgroup outcome comparison. | The hypothesis remains open rather than confirmed. |

## Reasoning in more detail

**Hypothetical numerical counterexample — constructed numbers, not participants or study results.** Suppose a report pools 100 decisions. Group A makes 86 safe decisions out of 90 opportunities, while group B makes four safe decisions out of ten. The overall result is **90/100 = 90%**, yet the within-group rates are about **95.6%** and **40%**. The overall figure is arithmetically correct; it is simply incomplete as a description of who was protected.

Those numbers alone do not establish a real difference in ability or control effectiveness. The groups may have faced different lures, had different exposure opportunities, or been observed too few times to support a reliable comparison. If each person contributed repeated decisions, the denominator also conceals dependence. The right response is not to replace one misleading average with an equally misleading league table.

A second counterexample is important: a lower interaction rate could look protective even if it came from avoiding legitimate communications. Without legitimate examples, we could praise a group for behavior that blocks ordinary work. That is why the definition of “safe” must be justified before subgroup comparisons.

## Competing explanations

**Unequal control access:** Some participants cannot reach or use the independent verification route in the relevant moment. This predicts differences in discoverability, completion and abandonment even when initial recognition is similar.

**Unequal task exposure:** Groups encounter different messages, language demands or job pressures. This predicts gaps that narrow when scenarios and opportunities are made comparable.

**Different strategies:** Some people reject unfamiliar requests broadly while others verify selectively. A simple non-click metric could favor the former despite higher legitimate-work costs.

**Measurement and sampling artifacts:** Small groups, missing follow-up, repeated observations and imperfect instrumentation can exaggerate or conceal apparent differences.

These mechanisms can coexist. The current evidence does not rank them by prevalence.

## Evidence ledger

| Source | Access actually established | Supports | Does not establish |
| --- | --- | --- | --- |
| [Buckmann, Nold, Acar and Zou, SOUPS 2025](https://www.usenix.org/conference/soups2025/presentation/buckmann) | Original publisher abstract independently checked; the [repository appraisal](../literature-watch/2026-10-18-access-to-verification.md) records a previous full-text review of 47 interviews | The authors' concept of differential access: security resources and support vary with social and material circumstances | A numerical organizational phishing gap or causal estimate for a verification control |
| [Napoli, Baig, Maqsood and Chiasson, SOUPS 2021](https://www.usenix.org/conference/soups2021/presentation/napoli) | Original publisher abstract independently checked; PDF available but **not newly appraised in full** for this note | Observed security/privacy tasks and interviews with users with visual disabilities identified accessibility barriers and risky trade-offs | A general population rate, or the subgroup comparison illustrated above |
| [Control existence versus effective use](../literature-watch/2026-10-18-control-existence-versus-effective-use.md) | Existing public conceptual synthesis; not a new empirical source | Separates specified, usable and effective controls | Proof that a particular organization has unequal protection |
| [QT-005](QT-005-what-does-a-risk-score-mean.md) | Existing conceptual trail with synthetic measurement examples | Aggregation, difficulty and missingness can obscure interpretation | A validated individual or subgroup risk score |

## Provisional position and confidence

**High confidence in the mathematical point:** an aggregate can conceal a large subgroup difference. **Moderate confidence that access deserves explicit measurement:** the cited qualitative and observed-task research documents real barriers, but in different settings. **Low confidence in any specific organizational prevalence or causal attribution:** no aligned subgroup outcome study has been conducted or extracted here.

A fair assessment should ask whether people had comparable opportunities to recognize, verify and act safely before interpreting a group-level difference as an individual deficit. That does not mean every gap is caused by the environment. It means the outcome alone cannot settle the attribution.

**Public boundary:** No participant records, private group-level metrics, confidential organizational evidence, proprietary assessment formulas or unpublished implementation details.
