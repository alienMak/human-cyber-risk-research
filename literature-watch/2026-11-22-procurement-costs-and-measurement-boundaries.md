# Procurement effort is not training effectiveness

**Paper:** [Brunken, Buckmann, Hielscher & Sasse, “To Do This Properly, You Need More Resources”: The Hidden Costs of Introducing Simulated Phishing Campaigns](https://www.usenix.org/system/files/usenixsecurity23-brunken.pdf)  
**Publication:** USENIX Security 2023, 9–11 August 2023, pp. 4105–4122; [publisher record](https://www.usenix.org/conference/usenixsecurity23/presentation/brunken); [ACM indexing DOI](https://doi.org/10.5555/3620237.3620467)  
**Type:** Peer-reviewed conference case study  
**Access:** FULL TEXT APPRAISED, original USENIX PDF, §§3–4.3, Table 1, Figure 2, limitations §3.5; remaining sections not extracted in detail  
**Review date:** 2026-11-22

## What the authors investigated

The authors followed procurement of a phishing-simulation and awareness-training service in one European corporation with more than 30,000 employees. An embedded researcher documented five months of procurement work; the team examined 73 observation-log entries, 20 documents, 26 artifacts, a survey, and five semi-structured interviews with six key stakeholders. The five-month observation window is not the entire procurement timeline: the wider selection process took approximately 14 months (Figure 2, §§3.1–3.3, 4.3).

**Intervention/comparison:** This is an organizational procurement case study, **not** a randomized training intervention or a comparison of learning outcomes. Two providers underwent proof-of-concept evaluation, but no causal estimate of one provider's training effectiveness was reported in the sections checked.

**Measured outcome:** Estimated stakeholder work hours and associated labor cost during procurement, plus qualitative observations of workload and friction. Table 1 reports 1,794.5 hours and €54,245. The authors multiplied estimated hours by rounded salary estimates, excluding license price, infrastructure, operating expense and opportunity costs (§4.1). This is a conservative, context-specific estimate, **not** a general deployment price or demonstrated net benefit.

**Population and setting:** One large, internationally distributed European employer, with procurement stakeholders in IT and other business units. Six interviewees were purposively selected key actors, not a representative employee sample (§§3.1–3.2).

**Analysis:** Predominantly deductive qualitative coding with additional inductive themes; the embedded observer's log and interview transcripts were analyzed by different researchers and discussed together (§3.3). No inter-rater reliability statistic is claimed here.

## What the evidence supports and does not support

**Author finding:** Procurement required substantial coordination across stakeholder groups and generated costs beyond the product price (Table 1; §§4.1–4.3).

**Analysis:** Counting simulation clicks without accounting for implementation workload risks describing only one side of an intervention. This study documents procurement burden, but does **not** demonstrate that simulations improve or worsen employee behavior.

**Limits and confounds:** A single unusually large organization, previous unsuccessful pilot, multilingual requirements, certification pressure and legacy systems all shape the observed costs. One embedded researcher could miss or misinterpret interactions; not every department was interviewed (§3.5). Salary assumptions are rounded and time accounting incomplete (§4.1). No learner-level outcomes, legitimate-message false alarms or long-term behavior are measured.

## Eight-domain appraisal

| Domain | Judgment | Basis |
| --- | --- | --- |
| Design | Yes for describing one procurement; No for training efficacy | §§3.1–3.2 |
| Sampling | Partial | One organization, six purposively selected actors; §§3.1–3.2 |
| Outcome definition | Yes | Estimated hours and labor costs, not clicks or learning; §4.1, Table 1 |
| Confounding | Partial | Prior pilot, certification and organizational scale; §§3.1, 3.5, 4.2 |
| Measurement | Partial | Observation logs and estimated hours; §§3.2, 4.1 |
| Analysis | Partial | Multiple researchers and coding synthesis, no independent cost audit; §3.3 |
| Generalization | No for universal cost estimates | Explicit single-site limits; §3.5 |
| Ethics/reproducibility | Partial | Ethics protocol referenced in Appendix A and interview guide in replication package; these materials not independently checked; §§3.2, 3.4 |

## Where this leaves the question

1. In a prospective comparison, can organizational labor and employee disruption be recorded alongside behavioral outcomes, without assuming either predicts the other?
2. How much do multilingual support, reporting workflows and existing infrastructure change the burden of introducing simulations?
3. Does a program that generates more reports also impose more triage effort, and what fraction of those reports correctly identify malicious messages?

These are **proposed future tests**, not results from this study. No private product mechanisms, participant records or proprietary implementation details are included.
