# Trust mechanisms: cues, claims and decisions

**Evidence status:** Analytical taxonomy grounded in cited publisher abstracts and public guidance; not a validated psychological instrument. A mechanism is a proposed explanatory category, not a diagnosis of an individual.

| Mechanism | Observable cue or context | What it may encourage | What the evidence actually supports |
| --- | --- | --- | --- |
| Apparent authority | Institutional name, professional role, official-looking interface | Accepting an instruction without independently checking the issuer | [Zheng & Becker 2022](https://www.usenix.org/conference/soups2022/presentation/zheng) investigates source impersonation and difficulty interpreting headers; it does **not** isolate a universal authority effect. |
| Contextual fit | A request that plausibly matches a recipient's work | Treating a message as routine rather than suspicious | [Steves et al. 2020](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final) incorporates premise alignment and message cues into phishing difficulty; broader validation is needed. |
| Visible technical reassurance | A secure-looking web page, email metadata or familiar UI | Confusing the appearance of a legitimate channel with a verified sender | [Zheng & Becker 2022](https://www.usenix.org/conference/soups2022/presentation/zheng) reports that presenting header details alone did not improve phishing detection in its tested conditions. |
| Verification friction | The cost of finding a reliable way to check a claim | Proceeding without verification when the path is inconvenient | [Zheng & Becker 2023](https://www.usenix.org/conference/soups2023/presentation/zheng) reports users' preferences for a check button and suspicion score in a formative usability study, not measured real-world fraud prevention. |
| Learned expectations | Past exposure to training or reminders | Applying a familiar detection strategy | [Reinheimer et al. 2020](https://www.usenix.org/conference/soups2020/presentation/reinheimer) observed differences in email identification over time in one organizational field study; generalization remains limited. |
| Algorithmic credibility | A system's fluent or confident-looking output | Treating AI-generated advice as authoritative | A **research hypothesis** for this collection, not established by the sources above. [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) supplies governance context, not a behavioral estimate. |

## Important distinctions

A convincing interface is not proof of a legitimate source. Likewise, suspicion, confidence, clicking, reporting and independently verifying are different outcomes. The same cue may be useful for legitimate communication and for impersonation. Do not infer that a victim acted from a specific psychological mechanism unless the incident record or research design actually supports it.

## Evidence needed next

Experiments varying one credibility cue at a time; direct observation of verification behavior; tests across phone, email and AI interfaces; and studies that record participant context, language, prior experience and reporting opportunities.

Related: [research questions](../research-questions/README.md) and [case-study methodology](../case-studies/README.md).
