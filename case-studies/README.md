# Documented cases and what they can actually tell us

**Prepared 13 October 2026.** The cases here are *published empirical research cases*, not unverified breach narratives. This avoids treating podcast anecdotes as established incident reconstructions.

## Case A: Email context and detection difficulty

**Primary record:** [Steves, Greene & Theofanos, Categorizing Human Phishing Detection Difficulty (2020)](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final).

**What is documented:** A proposed scale built from phishing cues and the alignment of a message's premise with the target audience, applied to enterprise phishing exercise datasets. The authors say more validation is needed across varied messages.

**Trust question:** How does a request that fits a person's ordinary work change what they regard as plausible?

**Cannot conclude:** That any individual click proves a stable personality weakness; that the scale works for phone calls, physical access or AI agents.

## Case B: Sender details and misleading confidence

**Primary record:** [Zheng & Becker, Presenting Suspicious Details in User-Facing E-mail Headers Does Not Improve Phishing Detection (SOUPS 2022)](https://www.usenix.org/conference/soups2022/presentation/zheng).

**What is documented:** The researchers tested email judgment under different information-presentation conditions. The publisher summary reports poor detection for many phishing emails and particularly weak performance with header-only presentation.

**Trust question:** Why might technically informative sender fields fail to help when presented without supporting interpretation?

**Cannot conclude:** That headers are universally useless, or that the study identifies a single psychological cause for every incorrect decision.

## Case C: Verification controls in a familiar interface

**Primary record:** [Zheng & Becker, Checking, Nudging or Scoring? (SOUPS 2023)](https://www.usenix.org/conference/soups2023/presentation/zheng).

**What is documented:** A formative usability evaluation of three proposed email security tools with 27 professional users. The publisher reports favorable responses to a check button and suspicion score.

**Trust question:** Does a practical way to check legitimacy change decisions more effectively than simply presenting warning cues?

**Cannot conclude:** That these tools prevented fraud in a deployed field trial.

## Incident-reconstruction admission rule

A future real-world case should name the incident, original reporting or court/investigation source, confirmed sequence, affected actors, what remains disputed, and what human behavior is directly evidenced. Do not infer motivations or reproduce sensitive details from a podcast alone.

Related: [Podcast cross-references](../podcast-notes/cross-references.md) and [research questions](../research-questions/README.md).

## Additional public records

- [FBI 2023 business-email-compromise advisory](business-email-compromise-2023.md) — documented pattern, not one reconstructed victim.
- [DOJ February 2023 prosecution record](doj-prosecution-record-2023.md) — named proceeding from an official press release; underlying court docket not inspected.
