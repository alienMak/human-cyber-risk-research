# Does a convincing phone scam depend more on the voice or the situation?

**Paper:** [Users Really Do Answer Telephone Scams](https://www.usenix.org/conference/usenixsecurity19/presentation/tu) ([publisher full text](https://www.usenix.org/system/files/sec19-tu.pdf))  
**Authors:** Huahong Tu, Adam Doupé, Ziming Zhao and Gail-Joon Ahn  
**Publication:** USENIX Security 2019, pp. 1327–1340 (August 2019)  
**Type:** Peer-reviewed conference paper; no DOI established from the publisher record  
**Access and review:** FULL TEXT APPRAISED against the publisher PDF on 12 October 2026  
**Scope:** Source-grounded research note prepared for this archive; not a claim that the repository owner personally conducted this review.

## What the authors investigated

The researchers tested how features of unsolicited telephone calls affect responses to a simulated request for sensitive information. In late March 2017, they placed calls to 3,000 randomly selected university staff/faculty work numbers, randomly assigned to ten conditions (300 numbers each). Conditions varied caller-number presentation, a directory-listed caller name, synthesized versus recorded voice, voice gender/accent, impersonated institution and scenario. Calls were distributed across a working week; each number was contacted once. This was a deceptive field study conducted with institutional review-board approval and debriefing. **Source:** §3.1–3.6, pp. 1328–1332.

**Comparison:** Attribute contrasts used selected, fixed background conditions rather than a full factorial design. The internal-institution impersonation and associated payroll scenario were not independently manipulated. **Source:** §3.2 and Table 1, pp. 1329–1330; §4, p. 1335.

**Measured outcomes:** Continued after the recorded announcement; called back; pressed a digit when asked for the last four Social Security number digits; post-debrief statements of being convinced or unconvinced. The system did **not** record any actual digits. The authors constructed a proxy called *possibly tricked* by excluding participants who entered a digit but later reported being unconvinced. This is not verified disclosure of a real identifier. **Source:** §3.4–3.5, pp. 1330–1331; §4 and Tables 2–3, pp. 1332–1333.

## What the paper reports

Across 3,000 dialed numbers, 256 recipients (8.53%) continued, 148 (4.93%) pressed at least one digit at the sensitive-information prompt, and 111 (3.70%) met the authors' *possibly tricked* proxy. These percentages use **all dialed numbers**, not only people who answered and listened. **Source:** §4, Tables 2–3, pp. 1332–1333.

The strongest reported comparison involved the **combined institutional identity and scenario** (Table 5: 3/600 versus 39/600; Holm-adjusted p = 1.09 × 10⁻⁷). The toll-free versus Washington, DC number comparison was also significant in that table (2/300 versus 12/300; adjusted p = 0.0410). The displayed directory caller-name contrast alone did **not** reach significance after adjustment (21/300 versus 31/300; adjusted p = 0.588). The same table did not support independent conclusions for voice production, accent, gender or fear-versus-reward framing. **Source:** §4, Table 5, p. 1335.

An important reading caution: Table 5 and the surrounding prose do not consistently label the adjusted p-values; the prose also names a different internal-scenario experiment combination from the table. The exact comparison should be resolved before using the effect as a precise quantitative benchmark. The abstract's emphasis on caller-ID spoofing should not be read as proof that displaying a familiar caller **name by itself** caused the observed difference. **Source:** §4, pp. 1334–1336.

## Appraisal: what the design can and cannot establish

| Domain | Assessment | Evidence or qualification |
| --- | --- | --- |
| Research design | Partial | Random assignment to ten groups, but selected comparisons and intertwined institution/scenario (§3.2; §4). |
| Sampling | Partial | 3,000 staff/faculty work numbers from one university; not mobile users or a general-population sample (§3.3; §6). |
| Outcome definition | Partial | Observable keypresses distinguished from a constructed *possibly tricked* proxy; no true SSN verified (§3.4–3.5; §4). |
| Confounding | Partial | Internal identity, scenario and some number cues overlap; call blocking, complaints and an internal warning occurred during deployment (§3.6; §4). |
| Measurement | Partial | Several behavioral steps recorded, but the main proxy can over- or underestimate genuine disclosure (§4; §6). |
| Analysis | Partial | Holm-Bonferroni correction reported; table/prose discrepancies and limited factorial coverage warrant caution (§4, Table 5). |
| Generalization | Partial | Office telephones, a specific institution and payroll/tax scripts; other channels and populations untested (§6). |
| Ethics and reproducibility | Partial | IRB review, debriefing, one call per recipient and no storage of digits; scripts and aggregate tables are published, but individual data/reproduction status was not verified (§3.4–3.5; appendices). |

## What the evidence suggests, and a future test

**Interpretation, not an author finding:** A credible organizational context may matter more than a stereotypically convincing voice. But the paper does not isolate institutional familiarity from the payroll pretext or caller-number presentation. It also shows why an apparently precise outcome can depend on how researchers define a proxy.

**Proposed research questions (not completed studies):**

1. Holding the requested action constant, does institutional familiarity still influence verification behavior when caller display, voice and scenario urgency are independently varied?
2. How differently would results look if *answered*, *continued*, *attempted disclosure* and *verified disclosure* were reported as separate outcomes with clear denominators?
3. Can a safe simulation record an explicit verification or refusal decision without collecting sensitive information, while still retaining enough validity to compare scenarios?

**Boundary:** No inference here validates a person-level risk score or establishes how participants would behave outside this experiment. Replication of deceptive calls would require independent ethics, privacy and institutional review.
