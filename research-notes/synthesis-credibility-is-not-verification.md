# Credibility is not verification

The problem is not simply that people trust the wrong things. In many systems, the signs that make communication convenient are also the signs that can be imitated. A familiar sender name, an ordinary-looking invoice, a polished interface or an apparently confident explanation can make a request easy to process. None of those qualities, by itself, proves that the underlying claim is authentic.

This distinction appears in different kinds of evidence. The [FBI's 2023 business email compromise alert](https://www.ic3.gov/PSA/2023/psa230324) describes misuse of corporate identities in purchasing workflows. That is an official account of a criminal pattern, not a psychological experiment. In a different setting, [Zheng and Becker's 2022 experiment](https://www.usenix.org/system/files/soups2022-zheng_1.pdf) tested whether exposing sender information improved phishing judgments. It did not, in the tested conditions. Their [2023 usability study](https://www.usenix.org/system/files/soups2023-zheng.pdf) explored ways to make checking more accessible, but also found that a verification feature can go unnoticed and that prior correspondence may provide misleading reassurance if an account is compromised.

Together, these sources support a narrower conclusion than 'people are bad at security': **an available cue is not the same as an interpretable cue, and an interpretable cue is not necessarily independent verification**. The sources use different methods and cannot be combined into one causal effect estimate.

The distinction matters equally for legitimate communication. A bank, school, employer or AI tool may have good reasons to communicate quickly, but asking recipients to act creates a design obligation: there should be a practical way to confirm the claim without relying exclusively on the same channel that delivered it. That is a normative proposal, not a measured intervention effect.

## Where the evidence stops

We do not yet know how consistently this distinction holds across email, telephone, messaging, synthetic media and AI assistants. Nor do we know whether making verification more visible reliably improves decisions without creating false alarms or unnecessary delay. These require comparisons that measure actual checking and outcomes, not just confidence or stated intentions.

The more interesting research question may therefore be: **When does a system make a claim look trustworthy, and when does it make the claim genuinely easier to verify?** That difference is worth measuring.

**Evidence status:** Original full papers inspected for the two SOUPS studies; official FBI alert inspected for the described pattern. This essay is an analytical synthesis, not a systematic review or report of a new experiment.
