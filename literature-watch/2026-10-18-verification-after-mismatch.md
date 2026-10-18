# A mismatch was noticed. Why did verification still fail?

**Paper:** [Häring, Grohs, Tiefenau, Smith and Tiefenau, *Can Johnny be a whistleblower? A qualitative user study of a social authentication Signal extension in an adversarial scenario*](https://www.usenix.org/system/files/soups2024-haring.pdf)  
**Venue:** SOUPS 2024, pp. 259–278. **Type:** Peer-reviewed primary empirical study. **Access:** FULL TEXT APPRAISED (Sections 3–5). **Date added:** 18 October 2026.

## What was studied

The researchers examined authentication ceremonies for end-to-end encrypted messaging under an impersonation attack, comparing safety-number checks, QR-code checks and a social-account-based authentication mechanism. A role-play asked participants to contact journalists and transmit simulated sensitive documents only when secure. The researchers used a preceding pilot (nine analyzed participants) to revise the interface, then ran a main lab study with **18 participants** (Sections 3.1–3.2, printed pp. 262–265).

The participants received business cards containing reference information, and all intended contacts were impersonated. Their actions were recorded through think-aloud, screen/audio capture, a follow-up survey and interviews. **Primary observed endpoint:** whether a participant sent the documents to an impersonator. Other outcomes included whether participants attempted checks, detected discrepancies, and how they perceived each method (Sections 3.2.4–3.2.5, printed pp. 265–266). This was a scenario with deliberately adversarial contacts, not a balanced classification test containing legitimate and fraudulent correspondents.

## Findings and competing explanations

**Authors' results:** Seven of 18 participants sent the material to at least one impersonator. Four failures were attributed to **in-band safety-number comparisons**: participants noticed mismatches but then relied on information provided within the same untrusted conversation. The other three failures involved rapid clicking, gambling for the scenario reward and emotional stress (Section 3.3.1, printed pp. 266–268). In the revised interface, only one participant's failure was specifically attributed to the social-authentication mechanism, while six failed for other reasons (Introduction and Section 3.3).

**What the result does not mean:** It does not show that attempting verification makes people less safe. Participants faced a contrived no-win scenario; the study did not randomize people to independent versus attacker-supplied checking and did not measure real-world scam losses.

**Twin's challenge:** When a participant continues checking after a mismatch, at least three explanations deserve testing: (1) they recognized the risk but trusted an attacker-controlled source; (2) they misunderstood what the comparison established; (3) the scenario incentives or the research setting encouraged them to keep trying rather than stop. The study documents instances of the first two patterns, but cannot estimate their prevalence in other populations or isolate a causal effect.

## Eight-domain appraisal

| Domain | Assessment | Evidence and caveat |
| --- | --- | --- |
| Design | Partial | Adversarial lab task can expose decision sequences, not naturalistic attack rates (Sections 3.2, 5). |
| Sampling | Partial | Nine analyzed in revised-interface pilot and 18 in main study; convenience and student-linked recruitment limit generality (Section 3.2.2). |
| Outcome definition | Yes | Failure defined as sending material to an impersonator; no direct real-world harm (Section 3.2.5). |
| Confounding | Partial | Interface revised after pilot; scenario reward, unfamiliarity with Signal and attacker behavior complicate comparisons (Sections 3.2–3.3, 5). |
| Measurement | Partial | Recorded actions and think-aloud triangulate decisions, but prompting and researcher presence can affect behavior (Sections 3.2.4–3.2.5, 5). |
| Analysis | Partial | Descriptive counts and qualitative failure accounts; small sample and no causal effect estimate (Section 3.3). |
| Generalization | Partial | Whistleblower role-play and restricted communication channels differ from everyday workplace messages (Section 5). |
| Ethics/reproducibility | Partial | IRB clearance, consent and GDPR handling reported; study documents and interface materials referenced (Sections 3.2.3–3.2.4, Appendix). |

## What this changes in the research questions

The earlier [verification-and-transfer note](../literature-review/verification-and-transfer-questions.md) distinguished noticing a threat from taking a safe action. This paper provides **observed decision sequences** where people detected mismatches yet continued toward unsafe disclosure. It also reinforces the distinction between verifying with an independent reference and relying on information supplied by the suspicious contact.

**Future test 1:** Compare verification using an independently established source against a source introduced during the suspicious interaction, without treating effort or confidence as proof of accuracy.

**Future test 2:** Record the sequence of recognition, checking, renewed reassurance and final action. A final click or non-click alone cannot explain the intervening reasoning.

**Unresolved:** Does continued engagement cause additional risk, or does it simply occur more often among people who are already uncertain? This paper cannot separate those mechanisms.

**Researcher review question:** If someone notices a mismatch but accepts the other person's explanation for it, was the problem recognition, verification, or trust in the source of evidence?

**Public publishing check:** No proprietary scoring, implementation, unpublished architecture, participant data or confidential organizational information.
