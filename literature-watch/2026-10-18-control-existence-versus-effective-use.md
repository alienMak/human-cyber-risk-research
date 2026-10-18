# A control can exist on paper and still fail in practice

**Research trail:** Recognition → verification access → practical control usability → demonstrated effectiveness.  
**Date:** 18 October 2026.  
**Evidence status:** Methodological synthesis drawing on previously appraised qualitative studies; no new intervention or quantitative effect estimate.

## The question

If an organization provides a verification procedure that takes longer than the work allows, depends on an unavailable colleague, or carries a social penalty for delaying an urgent request, should its presence in policy count as evidence that the risk is controlled?

**My working answer:** Count it as a *specified control*, not yet as an *effective control*. That is a hypothesis about assessment practice, not a conclusion that every inconvenient control fails.

## Three different claims

1. **Specified:** The policy, procedure or technical mechanism exists and its owner and intended action can be identified.
2. **Usable in context:** A person facing the relevant decision can discover, access and complete the control within realistic time, authority and resource constraints.
3. **Effective:** There is credible evidence that using the control reduces the intended harm without unacceptable displacement or collateral costs.

Evidence at one level does not automatically establish the next. A policy document establishes neither routine access nor outcome effectiveness. Conversely, one person's failure to use a control does not establish that the control never works.

## What earlier evidence can and cannot tell us

- [Buckmann et al., *More than Usability: Differential Access to Digital Security and Privacy* (SOUPS 2025)](https://www.usenix.org/system/files/soups2025-buckmann.pdf): **47 interviews in Germany** describe unequal access to security information and support. The repository's [full-text appraisal](2026-10-18-access-to-verification.md) supports studying practical access. It does **not** provide an organizational control-effectiveness rate.
- [Alromaih, Flechais and Chalhoub, *Beyond the Office Walls* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/alromaih): **20 interviews** describe remote-work security practices and workarounds. The [existing appraisal](2026-10-18-shadow-security-and-policy-deviation.md) records limits of self-reported policy interpretations. Workarounds merit investigation; they do not automatically prove negligence or good judgment.
- [Chen et al., *What Motivates and Discourages Employees in Phishing Interventions* (SOUPS 2024)](https://www.usenix.org/conference/soups2024/presentation/chen): **34 employees in seven focus groups** discussed barriers and motivations around phishing interventions. The [earlier note](2026-10-18-recognition-without-reporting.md) separates recognizing a suspicious message from reporting it. Reported friction does not itself estimate prevented incidents.

These are complementary qualitative observations, not interchangeable quantitative measures or a pooled causal estimate.

## An illustrative control review (hypothetical)

| Observation | What it supports | What remains unproven |
| --- | --- | --- |
| Procedure is approved and published | Control is specified | Staff can find or execute it |
| Verification number is independently maintained | A potentially trustworthy route exists | It is reachable during actual decisions |
| Staff successfully verify in a scheduled test | Usability under test conditions | Routine use under workload or urgency |
| Staff frequently bypass the route | Possible friction, incentives or awareness gap | Which mechanism caused the bypass |
| Fewer unsafe decisions occur after a change | Possible benefit | Causal effect without a credible comparison |

The final row is especially important: an apparent improvement could also reflect easier scenarios, seasonal workload, repeated exposure, selection or a change in measurement.

## What I would want to observe

A defensible assessment should distinguish:

- **Availability:** Is the approved route accessible at the moment of need?
- **Discoverability:** Can the employee locate it without relying on details supplied by the suspicious request?
- **Authority:** Can the person pause, reject or escalate without unreasonable penalty?
- **Completion cost:** How much time and coordination does it require in normal work?
- **Actual use:** Do people invoke it, abandon it, or substitute another route?
- **Consequences:** Are malicious requests handled more safely while legitimate work remains possible?

The last measure prevents blanket refusal from being mistaken for successful security. Independent verification should be assessed separately from staying engaged with the original suspicious sender.

## A study that could challenge the claim

Compare comparable, ethically constructed scenarios before and after an approved route becomes easier to access, or randomize non-harmful route-usability conditions where oversight permits. Include legitimate and malicious requests. Prespecify outcomes, account for repeated decisions nested within people and items, and record workload and opportunity to verify. A before/after improvement alone is not enough to attribute causality.

A competing result would matter too: if a well-used, accessible route does not reduce unsafe outcomes, usability alone is not evidence of effectiveness. If outcomes improve but legitimate requests are unnecessarily blocked, the trade-off must be reported.

## Eight-domain methodological checkpoint

| Domain | Current position | Remaining gap |
| --- | --- | --- |
| Design | Clear distinction between specified, usable and effective | No causal study conducted |
| Sampling | Relevant roles and situations identified | Representative deployment settings untested |
| Outcomes | Verification, safe action and legitimate-work costs separated | Operational measures not validated |
| Confounding | Workload, item difficulty, authority and incentives identified | No adjustment or randomization performed |
| Measurement | Access and completion cost explicitly considered | Observational reliability unknown |
| Analysis | Calls for clustered/repeated-measures treatment | No fitted model, interval or effect estimate |
| Generalization | Potential relevance across security controls | Cross-setting transfer untested |
| Ethics/reproducibility | Proposes non-harmful comparisons and transparent reporting | Protocol, oversight and preregistration outstanding |

## Twin's provisional conclusion

A control should not be described as effective solely because it appears in a policy, audit checklist or system inventory. We need evidence that it is reachable, workable and associated with the intended protective result under the conditions where decisions are actually made.

Equally, we should not excuse every unsafe decision by invoking friction. The evidence must distinguish a person who did not recognize the risk, a person who recognized it but lacked a viable route, and a person who had a viable route but chose not to use it.

**Next question:** If a verification process is effective for one group but inaccessible to another, can an organization-level average conceal unequal protection?

**Publishing boundary:** General research methodology, public literature and hypothetical examples only. No proprietary scoring logic, private architecture, participant data or confidential organizational evidence.
