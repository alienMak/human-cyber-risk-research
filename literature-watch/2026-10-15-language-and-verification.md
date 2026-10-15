# When ignoring an email is not the same as identifying a threat

**Evidence reviewed:** [Hasegawa et al., *Why They Ignore English Emails* (SOUPS 2021)](https://www.usenix.org/conference/soups2021/presentation/hasegawa); [Spero et al., *Language as Lure* (SOUPS 2025)](https://www.usenix.org/conference/soups2025/presentation/spero)  
**Source type:** Peer-reviewed conference papers  
**Publication dates:** August 2021; August 2025  
**Review note added:** 15 October 2026  
**Access and review status:** Hasegawa: full-text appraisal documented in the 14 October research working review (original paper §§3–6, Tables 2, 4–5); Spero: **ABSTRACT-ONLY**, publisher abstract verified. This note does not imply the repository owner personally read either paper.

## What the studies actually measured

Hasegawa and colleagues surveyed 862 full-time workers in Germany, South Korea and Japan. Participants considered screenshots of work emails in English or their native language and chose hypothetical initial actions. The authors distinguish following instructions without checking from ignoring a message without checking. These are *stated decisions*, not observed phishing clicks or verified real-world compromises (paper §§3.1–3.5). The publisher abstract reports a greater tendency to ignore English messages without careful inspection, particularly among participants with lower confidence in English.

Spero and colleagues report a four-month government phishing simulation in a Melanesian country. The publisher abstract says 2,000 employees received a simulated email each month, with opens and clicks recorded. For messages containing personal requests for help, local-language versions received more clicks than English versions. **ABSTRACT-ONLY:** the allocation procedure, effect sizes, uncertainty and detailed limitations have not been checked in the full paper.

## What follows, and what does not

**Authors' findings:** Language and message context can change responses to suspicious communication. The first study measures hypothetical handling of messages; the second measures interactions in a simulation. They cannot be combined into one susceptibility estimate.

**Analysis:** A non-click may mean a threat was recognized, but it may also mean a legitimate message was ignored because verifying it was difficult. Counting every non-click as successful detection would erase that distinction. This interpretation is a research inference, not an experimental result established by either study.

**Proposed future test:** In a consented, independently reviewed study, vary language and request type while including legitimate and malicious messages. Record *correct rejection*, *unverified ignoring*, *verification attempts* and *unsafe compliance* as distinct outcomes. Examine whether these distinctions persist across repeated exposures. This is a general research question, not a description of an existing implementation.

## Limits and follow-up

- Hasegawa's screenshot roleplay cannot establish actual behavior in an inbox; language, context and prior familiarity may interact (paper §5.2).
- Spero's abstract does not support detailed causal claims about cultural mechanisms; retrieve and appraise its full text before extracting effect sizes or study-design details.
- Existing matrix entries already index Hasegawa and Nicholson (2017); this note develops a measurement question rather than claiming new discovery.
- Publisher sources: [Hasegawa full text](https://www.usenix.org/system/files/soups2021-hasegawa.pdf); [Spero publisher record](https://www.usenix.org/conference/soups2025/presentation/spero).

**Question for the next review:** How often does a security study report *correct handling of legitimate messages* alongside phishing detection, and what changes when both error types are measured?
