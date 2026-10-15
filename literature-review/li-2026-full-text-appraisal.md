# Li et al. (2026): scam recognition, engagement and reporting

**Primary source:** [Li et al., *Quantifying Risk Perception and Scam Response Among International and Domestic US University Students*](https://www.usenix.org/system/files/soups2026-li.pdf), SOUPS 2026, pp. 333–355.  
**Review date:** 15 October 2026. **Status: FULL TEXT APPRAISED** (24-page original PDF, including proceedings cover). This is an evidence-extraction note, not a claim that the repository owner personally read or endorsed the paper. No DOI asserted.

## Study design and population

Cross-sectional online survey, **N=1,074**, recruited from five US universities: **391 international** and **683 domestic** students. Recruitment used mailing lists, social media, flyers and university contacts. Eligibility required adult, full-time, in-person enrollment. Compensation: $5. The authors note self-selection and non-representative group proportions (paper §3.1, §3.5, §4.1, printed pp. 335, 339).

## Tasks, comparison and operational definitions

Participants saw a common benign warm-up email followed by four randomized channel scenarios (phone, text, email and rental), each independently assigned a suspicious or benign variant. These were **hypothetical choices**, not observed scam interactions (§3.3.2, pp. 336–338). The authors defined three action categories: *fully engage* without outside help; *cautiously engage* while checking with others or searching; *disengage* by ignoring, blocking or reporting. Participants explained their choices.

The primary comparison was **international versus domestic student status**, not randomized membership in those groups. The authors randomized scenario versions and order, but did not experimentally assign social pressure, identity or language proficiency (§3.3, §3.4).

The analysis used scenario-specific multinomial logistic regressions for suspicious scenarios, binary logistic regressions for benign scenarios, and signal detection theory for discrimination and response bias. Models adjusted for age, gender, technical background and scenario order (§3.4.1, pp. 338–339). The paper defines a *hit* as disengagement from a suspicious scenario, a *false alarm* as disengagement from a benign one, and a *miss* as engagement or cautious engagement with a suspicious scenario. **Important construct limitation:** treating cautious engagement as a miss can obscure legitimate verification efforts; the authors' operational definition is not an independently validated measure of unsafe compliance.

## Findings and limits of inference

The authors report **no detected group difference in identifying suspicious cues**, but different patterns of intended engagement across channels. International students were more likely to indicate engagement with suspicious phone/text scenarios yet more likely to disengage from the suspicious rental email. This is not evidence that all international students are more susceptible (§4.2; abstract, printed p. 333).

Reporting history also differed: **73.9% domestic versus 64.5% international** indicated having used at least one listed reporting channel (Table 2, printed p. 342). This is *self-reported past reporting*, not an observed intervention effect. Participants' qualitative explanations included inconvenience and uncertainty about reporting routes (§4.3.2, pp. 341–342).

## Eight-domain appraisal

| Domain | Judgment | Evidence and concern |
| --- | --- | --- |
| Design | Partial | Cross-sectional survey supports comparisons of stated responses, not actual pressure-induced compliance (§3.3, §3.5). |
| Sampling | Partial | Five universities, recruitment channels and eligibility specified; self-selection and disproportional recruitment limit representativeness (§3.1, §3.5). |
| Outcomes | Partial | Three engagement categories and signal detection definitions specified; cautious engagement combines different verification behaviors (§3.3.2, §3.4.1). |
| Confounding | Partial | Covariates included; unmeasured differences in circumstances, experience and institutional context may remain (§3.4). |
| Measurement | Partial | Paired benign/suspicious scenarios; intended actions and recalled experience may diverge from behavior (§3.3, §3.5). |
| Analysis | Partial | Regression, SDT and qualitative coding described; coding agreement for reporting reasons was 0.79, below the team's 0.8 threshold, and responses were dual-coded (§3.4). |
| Generalization | Partial | Specific student sample and five scenarios; authors caution against extrapolation to other situations (§3.5). |
| Ethics/reproducibility | Partial | IRB approvals, consent and separation of compensation identifiers reported; independent replication and materials availability not verified here (§3.2). |

## Synthesis: authors' results versus new research questions

**Authors' results:** Recognition of suspicious cues did not differ detectably between the two student groups in their analysis, while intended engagement and reporting histories differed in context-specific ways.

**Analysis:** Recognizing a cue and choosing an action are not interchangeable outcomes. However, this paper does not prove *why* they diverge, nor does it establish a causal effect of authority, urgency or verification access.

**Proposed future test:** Distinguish initial recognition, verification attempts, temporary deferral, eventual compliance and correct handling of legitimate requests. Evaluate whether the opportunity to verify changes decisions under appropriately controlled conditions. This is a general methodological question, not an unpublished implementation.

## Comparability and next reading

[Nicholson et al. (SOUPS 2017)](https://www.usenix.org/conference/soups2017/technical-sessions/presentation/nicholson) uses classification/confidence; [Hasegawa et al. (SOUPS 2021)](https://www.usenix.org/conference/soups2021/presentation/hasegawa) uses hypothetical email handling; [Weidhaas et al. (SOUPS 2026)](https://www.usenix.org/conference/soups2026/presentation/weidhaas) uses a qualitative simulated workplace scenario (**ABSTRACT-ONLY here**). Do not pool effects or infer a single causal mechanism.

**Researcher review question:** If cautious engagement includes checking a request, when should that count as a mistake, and when is it exactly the behavior security education should encourage?

## Clarification: cautious engagement is not necessarily safe verification (15 October 2026)

The paper's **§3.3.2 (printed p. 336)** explicitly defines cautious engagement as consulting others or searching online *while maintaining the communication*, with examples including not hanging up or blocking the sender. It is therefore inappropriate to treat all cautious engagement as either safe independent verification or unsafe compliance. The category describes continued contact plus a checking step; it does not directly measure whether sensitive information was disclosed before, during or after that step.

**Methodological consequence:** A future study should distinguish the *channel of verification* (independent trusted contact versus remaining within the suspect interaction), *sequence* (before versus after sharing information), and *resolution* (whether the request was eventually accepted or refused). These are proposed general measurement distinctions, not a proprietary instrument or a claim about the Li participants' actual behavior.

**Evidence:** [Original PDF, §3.3.2, p. 336](https://www.usenix.org/system/files/soups2026-li.pdf). The study elicits hypothetical response choices; it does not observe these later verification steps.
