# QT-001 — Verification while still exposed

**Earlier documented context:** 15 October 2026 — Related verification-and-transfer working note dated 15 October 2026; the exact first conversation date has not been established.  
**Origin:** Earlier researcher discussion about a suspicious caller and whether remaining on the call while searching for confirmation should count as caution or continued exposure. This note is a reconstruction of the research question, **not a verbatim transcript or a validated experiment**.  
**Status:** Open; conceptual analysis.

## Brief

Someone can be trying to verify a suspicious claim and still be exposed to the person making it. Those are two different dimensions. Calling the behavior simply “cautious” overlooks the continued opportunity for manipulation; calling it simply “risky” overlooks the decision to seek independent evidence. The interesting question is what the person actually verifies, and whether the attacker can keep influencing that process.

## Question chain

| Step | Question | Working answer | What it opens up |
| --- | --- | --- | --- |
| Q1 | If a person keeps a suspicious caller on the line while searching for confirmation, is that caution or risk? | Potentially both. Verification intent and ongoing exposure are not opposites. | What makes the check genuinely independent? |
| Q2 | Does searching online while the caller continues speaking count as independent verification? | Not necessarily. The caller may suggest search terms, websites, names or explanations. | How much control does the caller retain over the evidence? |
| Q3 | What changes if the person ends the call and contacts the institution through a separately obtained channel? | It can reduce the caller's direct influence over the next step; it does not automatically guarantee the new channel is authentic. | What evidence establishes channel independence? |
| Q4 | Is a successful refusal enough to classify the entire interaction as safe? | No. A final refusal and the intermediate exposure are distinct observations. | Should outcomes and process be measured separately? |
| Q5 | What would disprove the claim that staying connected increases manipulation risk? | Comparative evidence showing no difference under appropriately matched scenarios, or evidence that some verification methods reliably neutralize continued influence. | How could a controlled study distinguish time, verification quality and persuasion? |

## Reasoning in more detail

The difficult part is that an observer sees one continuous interaction but several decisions inside it. The person might have noticed something suspicious, searched for an institutional phone number, listened to a new explanation and then declined the request. Treating that whole sequence as either “safe” or “unsafe” loses the point at which the caller still had influence. The search itself could be independent, or the caller could have directed the person to a convincing but attacker-controlled page. Those are materially different actions despite looking similar from the outside.

A useful counterexample is a person who stays connected solely to collect details while refusing to disclose information or follow instructions. Duration alone would overstate risk in that case. Conversely, a person who ends the call but uses a number supplied by the caller has broken contact without establishing independent verification. The two observations should not be conflated. The linked phishing literature helps frame context and usability, but it does not establish how often either behavior occurs during real calls.

## Competing explanations

**Exposure mechanism:** Continued interaction gives a manipulator additional chances to reframe the story, introduce urgency or steer the person's verification. This is plausible, not established here as a quantified effect.

**Active-checking mechanism:** A person who remains engaged may be deliberately collecting inconsistencies and may be less likely to comply. That too is plausible; staying on the line does not by itself reveal intent or susceptibility.

**Context mechanism:** Differences could be driven by scenario difficulty, prior experience, available contact methods or whether the suspicious caller can see and react to the verification attempt.

## Evidence and boundaries

- [NIST Phish Scale research note](../literature-review/full-text-appraisals/steves-greene-theofanos-2020.md) supports attention to scenario difficulty and audience context **in email-phishing exercises**. It does not directly test live suspicious calls.
- [Zheng and Becker 2023 appraisal](../literature-review/full-text-appraisals/zheng-becker-2023.md) addresses the usability of email verification tools, not the effect of keeping a caller on the line.
- [Legitimate trust and verification](../research-notes/legitimate-trust-and-verification.md) is a conceptual companion, not a source of new experimental evidence.

**Evidence status:** Conceptual synthesis with related, non-equivalent empirical literature. No caller-specific experiment has been verified for this note.

## Provisional position

Don't collapse verification intent, verification quality, continued exposure and final decision into one label. Record the distinctions first. **Confidence:** Moderate in the conceptual distinction; low in any causal claim about whether staying connected changes actual outcomes.


**Public boundary:** No private scoring rules or unpublished VISHWAR implementation are disclosed.
