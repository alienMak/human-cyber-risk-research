# When do more reports make the organization safer?

**Primary sources:** Daniele Lain, Kari Kostiainen and Srdjan Čapkun, [Phishing in Organizations: Findings from a Large-Scale and Long-Term Study](https://arxiv.org/abs/2112.07498), IEEE Symposium on Security and Privacy 2022, pp. 842–859, DOI: 10.1109/SP46214.2022.9833766; Bushra A. Alahmadi, Louise Axon and Ivan Martinovic, [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi), USENIX Security 2022, pp. 2783–2800.  
**Evidence status:** Original publisher record and abstract for Alahmadi et al.; original author preprint abstract and independent publication citation for Lain et al. This is ABSTRACT-LEVEL cross-study synthesis, not a full-text methodological appraisal.  
**Recorded:** 21 October 2026.

## The evidence

Lain and colleagues report a 15-month phishing study involving more than 14,000 employees at one organization. They observed simulated phishing interactions and employee reporting, and describe collective employee reporting as a practical way to detect new phishing campaigns. The abstract reports that operational load was acceptable in that setting. That does not establish a universal capacity threshold for reporting queues or a causal effect of increasing report volume.

Alahmadi and colleagues studied SOC practitioners' perspectives on security alarms using a survey (n=20) and a separate qualitative investigation (n=21). They found that alarms described as false positives can include real signals of legitimate organizational activity, and that validation imposes work on analysts. Their paper concerns SOC security alarms broadly, not a controlled experiment on employee phishing-report buttons. It therefore cannot supply a phishing-report false-positive rate.

## My reading

Encouraging people to report uncertainty is useful, but reporting volume alone cannot tell us whether the system is becoming more effective. We also need to understand what happens after a report is submitted, how accurately those reports are handled, and whether the process can sustain the additional workload.

The studies point to two distinct parts of the problem: whether employees can contribute useful observations, and whether the receiving security team can interpret those observations in context. A report can be appropriate even if the message later proves benign. Conversely, a high count of reports is not evidence that genuinely malicious requests are being caught quickly.

I would not treat a user report, a detector alert, a validated incident and a resolved case as interchangeable units. I also would not infer individual competence from a report that turned out to be benign without considering what information the person had when deciding.

## A future comparison, not an implemented method

A consented evaluation could distinguish: reports submitted, unique messages or campaigns, confirmed suspicious reports, benign reports, review time, time to action, missed malicious messages and reporting feedback. Ground truth and follow-up procedures would have to be defined in advance. The analysis should check whether increased reporting improves coverage or speed without obscuring analyst burden and legitimate-message disruption. These are proposed measurement categories, not an operational scoring formula.

**Next question:** If an employee reports an uncertain but legitimate message, should that be treated as a mistake, or as appropriate use of a verification channel under uncertainty? The answer depends on what was reasonably knowable at the time and what the organization expects reporting to accomplish.

This note contains only public literature interpretation and proposed research questions, with no private algorithms, confidential organizational information, unpublished results or participant records.
