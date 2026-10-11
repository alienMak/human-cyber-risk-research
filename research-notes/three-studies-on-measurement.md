# Three results that change how I would design a VISHWAR study

The temptation is to put all phishing-training papers on one graph and compare whether training “works.” I don't think that's an honest comparison until we first ask what participants were actually doing and what the researchers measured.

This note compares three original research records. I checked the publisher-hosted summaries and reported statistics on 10 October 2026. It is a **source-level comparison**, not a full-text quality appraisal.

## A six-month effect is not a permanent effect

[Reinheimer and colleagues, SOUPS 2020](https://www.usenix.org/conference/soups2020/presentation/reinheimer), examined an awareness program in a German public-administration organization involving 409 employees. Correct identification of phishing and legitimate emails improved immediately and remained improved at four months, but not at six months. The authors also investigated reminders, with video and interactive-example reminders performing best among those compared.

The outcome here was email identification over time. It gives a reason to investigate how often a participant needs reinforcement, but it does not tell us that the same participant would resist an urgent phone impersonation attempt or a physical access pretext.

## A difficult lure can change a click rate without changing the person

[Steves, Greene and Theofanos, Journal of Cybersecurity 2020](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final), introduced the NIST Phish Scale as a way of rating phishing-detection difficulty using characteristics of the lure and its relationship to the target user's work context. Their scale was applied to organizational phishing data, and the authors themselves called for validation against a wider range of phishing emails.

A falling click rate could be an improvement. It could also reflect a change in message difficulty. A longitudinal analysis that cannot tell those explanations apart will struggle to support a strong claim.

For VISHWAR, this argues for treating scenario difficulty as a design and validation problem before interpreting a participant's risk trend. The published Phish Scale is about phishing email; adapting it to multi-vector storylines would require its own evidence.

## Hiding the content did not improve detection

[Zheng and Becker, SOUPS 2022](https://www.usenix.org/conference/soups2022/presentation/zheng), tested whether showing user-facing email header information rather than full messages helped people recognize impersonation. Their conference summary reports that most phishing emails were detected by fewer than 30% of participants regardless of presentation, and that performance was worst with headers alone.

This is more subtle than telling people to inspect sender information. A signal can be present without being understood. If our simulation measures only whether the user opened a verification screen, we may miss whether the person interpreted its contents correctly.

## Where these studies disagree — and where they don't

They do not directly contradict one another. They ask different questions: whether educational effects persist, how difficult a phishing message is to detect, and whether changing the information shown improves detection. Their samples, interventions and outcome variables differ.

The common lesson is methodological. We should not treat **recognition, clicking, reporting, response time, or simulated choice** as interchangeable measurements. A useful future VISHWAR study would specify a primary outcome, record scenario difficulty independently, and test whether improvement generalizes to unfamiliar settings.

## Evidence limitations and next check

This account is drawn from the linked publisher records and abstracts, **not** line-by-line appraisal of the full papers. Before making stronger claims, review the experimental conditions, recruitment details, statistical models, effect sizes, attrition and precise definitions of success in the full publications.

These ideas are directions for study design, not proof that VISHWAR already improves behavior.
