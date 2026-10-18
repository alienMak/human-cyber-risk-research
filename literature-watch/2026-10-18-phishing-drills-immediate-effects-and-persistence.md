# Does a phishing drill teach a durable skill or temporarily change attention?

**Trail:** policy friction → perceived risk of acting → observed behavior → intervention effects → persistence and transfer.  
**Added:** 18 October 2026. **Evidence status:** Two original open-access journal records inspected; 2019 article methods/results sections inspected; 2025 article abstract, introduction and reported design inspected. This is a **comparative reading note**, not two completed full-text eight-domain appraisals.

## Sources

1. [Baillon et al., *Informing, simulating experience, or both: A field experiment on phishing risks*](https://doi.org/10.1371/journal.pone.0224216), PLOS ONE, 2019. **Original article; methods, results and conclusion checked.**
2. [*Falling and failing (to learn): Evidence from a nation-wide cybersecurity field experiment with SMEs*](https://doi.org/10.1016/j.jebo.2024.106868), *Journal of Economic Behavior & Organization*, volume 230, February 2025. **Original article abstract and introduction checked; detailed models and appendix not fully appraised.**

## What the first study found

The 2019 study describes a field experiment involving **10,929 employees** of the Dutch Ministry of Economic Affairs. It compared information about phishing, exposure to a simulated phishing experience, their combination, and a control. Outcomes included clicking a suspicious link and providing credentials. The article reports approximately one third of controls clicked and **22%** provided a password. Compared with control, information reduced clicking by **7 percentage points** and credential disclosure by **6 points**; experience reduced clicking by **9 points** and disclosure by **8 points**. The combination did **not** substantially improve outcomes beyond the experience condition.

Those are intervention contrasts in that organizational context, **not** an estimate of lifelong security skill. The result should not be restated as a universal reduction in risk across attack vectors or organizations.

## What the later study adds

The 2025 article describes a field experiment involving **33,016 employees at 667 Dutch SMEs** in its introduction; the abstract rounds this to approximately 33,000 employees and 670 SMEs. The researchers examined whether prior simulated phishing experience affected later click behavior over several months and related responses to individual characteristics. The abstract reports **non-systematic, short-term effects**, rather than reliable sustained reductions. It also reports heterogeneity involving patience, trust and risk seeking; these associations should not be interpreted as validated individual risk predictions.

**Important:** The abstract alone does not establish which exact effect estimates remained significant at each follow-up, the precise allocation process, or whether every campaign's difficulty was comparable. Those require a full methods-and-results appraisal before stronger claims.

## Twin's alternative explanations

An initial decline in clicks might reflect:
- Learning a generalizable detection strategy.
- Heightened attention after a recent drill, without durable transfer.
- Recognition of similar lures rather than recognition of new attack mechanisms.
- Different lure difficulty or exposure opportunities.
- Organizational context and changes in participants over time.

Neither a one-time improvement nor an inconsistent later effect distinguishes all these explanations on its own. The two studies also differ in employers, scale, interventions and follow-up; comparing their headline percentages as if they were one common effect would be misleading.

## Eight-domain checkpoint

| Domain | 2019 article | 2025 article | What remains to check |
| --- | --- | --- | --- |
| Design | Field experiment with intervention arms | Field experiment with repeated phishing exposure | Allocation, spillovers, cluster effects |
| Sampling | Government employees in one ministry | Employees across Dutch SMEs | Exclusions, coverage and representativeness |
| Outcomes | Clicking and credential submission | Clicking in later campaigns | Identical outcome definitions and denominators |
| Confounding | Experimental contrasts reported | Individual heterogeneity reported | Campaign difficulty, calendar timing, job roles |
| Measurement | Simulated phishing actions | Repeated simulated phishing actions | Instrumentation and exposure comparability |
| Analysis | Reported point differences | Full model estimates not extracted | Confidence intervals, attrition, dependence |
| Generalization | One public employer | Many SMEs in one country | Transfer to voice, physical and conversational attacks |
| Ethics/reproducibility | Article and supporting files linked | Open-access article | Consent/deception handling and full appendices |

**These are extraction checkpoints, not completed Yes/No quality ratings.**

## What should be followed next

1. Appraise the 2025 full text for allocation, timing, campaign comparability, attrition and confidence intervals.
2. Check whether the 2019 paper tested transfer or only responses to subsequent email phishing in the study setting.
3. Compare the later study with the separate 2025 healthcare randomized trial already tracked in this repository, without pooling unlike designs.
4. Trace how simulation difficulty, repeated measures and reporting opportunities could change apparent improvement.
5. Preserve the distinction between *initial intervention effect*, *retention*, *cross-context transfer* and *real incident prevention*.

**Twin's next question:** If training reduces clicks in the next campaign but not months later, did the training fail, or did the study only measure a short-lived behavior change? Which evidence would separate those possibilities?

**Public boundary:** Only publicly reported study details, explicit uncertainties and general research questions; no proprietary scoring formulas, unpublished platform design or private participant data.


## Verification pass and deeper extraction (18 October 2026)

**Why this addition:** The first version named the right studies but left the actual experimental contrasts, threats to inference and unanswered statistical questions too compressed. This section records what was rechecked against the original publisher records and what still needs full-text verification.

### Identity and data audit

- **Baillon, de Bruin, Emirmahmutoglu, van de Veer and van Dijk (2019)**, PLOS ONE 14(12), e0224216, DOI 10.1371/journal.pone.0224216. Publisher methods/results and linked supplementary files were identified; full-text article sections were checked. The authors state that data are deposited at DOI **10.25397/eur.10500029**. The dataset was **not reanalyzed** here.
- **Falling and failing (to learn) (2025)**, *Journal of Economic Behavior & Organization* 230, article 106868, DOI 10.1016/j.jebo.2024.106868. Publisher abstract, introduction and displayed methods were checked. The publisher identifies data at DOI **10.25397/eur.28123376**. The data were **not downloaded or reanalyzed** here. A subsequent attempt to retrieve the entire publisher article returned an access error, so detailed tables, appendices and model estimates remain **unverified**.
- **Count correction:** The later paper's rounded abstract refers to 670 SMEs and 33,000 employees; the introduction specifies **667 SMEs and 33,016 employees**. Treat these as rounded versus exact descriptions of the same study, not separate samples.

### Study design: what was actually compared

**2019:** A Dutch ministry experiment assigned employees to control, information only, prior simulated phishing experience only, or both. The intervention timeline used an earlier simulated lure and debrief for experience groups, information messages for information groups, and a later common phishing outcome. The authors excluded some employees for technical or seniority reasons: **10,929 of 12,567** official employees were analyzed. Main outcomes were **Visit** (clicked through to the phishing website), **Fill** (entered a password), and **Fill conditional on Visit**. The authors recorded whether a form was filled but did not retain the entered content for privacy. The publisher reports approximate control rates of one-third visiting and 22% entering a password, with information lowering those outcomes by about **7 and 6 percentage points**, and experience by about **9 and 8 percentage points**, respectively. The combination did not substantially improve on experience alone. The paper also reports a sensitivity analysis excluding one ministry division (7,994 employees), so robustness must be checked by outcome rather than assuming all subgroup findings hold. These are **percentage-point contrasts**, not relative percentage reductions.

**2025:** The publisher introduction describes **667 Dutch SMEs**, each with **8–250 employees**, that opted into a program; 626 firms had complete company-level information. Firms, not individual workers, were randomly assigned to **four treatment groups** that varied the spacing and content of two phishing emails. The study used **three lure types**, described as an online gift, a data-leak check and free home-office supplies. All 33,016 workers were exposed to two drills at different times, with comparisons exploiting whether a particular lure was encountered as a first or second email. The authors describe an approximately **one-month** window for the observed short-term effect, but say effects were not systematic and did not persist reliably. These details raise two critical appraisal issues: the **company is an assignment unit**, and **lure content and timing must be accounted for** before interpreting a change as learning. The publisher introduction says preference measures were collected after treatment; associations with patience, trust and risk seeking should therefore not be read as experimentally established causes of susceptibility.

### What would count as evidence of transferable learning?

**A sequence of increasingly demanding claims:**

1. **Task performance:** fewer clicks on the measured email after an intervention.
2. **Retention:** improvement remains after a prespecified delay using comparably difficult, unfamiliar lures.
3. **Transfer:** improvement generalizes to new social-engineering mechanisms or channels not practiced during training.
4. **Security impact:** an independently defined harmful outcome becomes less likely outside the testing artifact.

Neither the 2019 one-organization result nor the 2025 repeated-email design alone establishes all four. Avoid interpreting a failed persistence test as proof that *no* knowledge was learned: behavior may be shaped by competing demands, exposure, difficulty or response opportunities.

### Eight-domain appraisal: what can be rated now?

| Domain | 2019 evidence and status | 2025 evidence and status |
| --- | --- | --- |
| Research design | **Yes** for a short-run field intervention contrast; **No** for cross-vector transfer | **Yes** for randomized SME-level drill sequences; **Partial** for durability until full models checked |
| Sampling | **Partial**: one ministry, 10,929 included of 12,567 | **Partial**: opt-in SMEs, 667 firms, 33,016 workers; 626 firms with complete firm data |
| Outcome definition | **Yes**: Visit, Fill and Fill given Visit separately specified | **Partial**: clicking in repeated email drills; exact denominator/handling needs table review |
| Confounding | **Partial**: allocation and division sensitivity described; remaining context and spillover possible | **Partial**: firm assignment, timing and lure type relevant; full adjustments not yet checked |
| Measurement | **Partial**: instrumented phishing actions, not mental states or real incidents | **Partial**: instrumented drill clicks; cross-campaign difficulty equivalence unverified |
| Analysis | **Partial**: publisher reports contrasts and regression/sensitivity; no independent reanalysis | **Not fully appraised**: model coefficients, clustered uncertainty, missingness and interactions not extracted |
| Generalization | **Partial**: one public-sector workplace and one email context | **Partial**: multiple Dutch SMEs but only simulated email drills |
| Ethics/reproducibility | **Partial**: privacy handling and dataset DOI identified; supplementary materials not independently checked | **Partial**: company consent and third-party data handling described; dataset DOI identified, not reanalyzed |

**Why “Partial” matters:** a published study may be sound for its stated estimand while remaining insufficient for a stronger claim about durable individual judgment. No numerical quality score is inferred.

### Contradiction and replication register

- **Apparent tension:** the 2019 experiment reports an immediate reduction in risky email responses; the 2025 experiment finds short-term, inconsistent benefits from prior drills.
- **Reconciliation hypothesis:** immediate alertness and longer-term retention are different outcomes. Different organizations, email lures, treatment schedules and statistical units also prevent direct pooling.
- **Still untested:** whether people learned a generalizable skill but failed to deploy it later; whether differences in scenario difficulty account for some of the temporal variation; whether reporting behavior changed even where clicking did not.
- **Next source check:** the full 2025 tables and appendices for randomized sequence balance, lure-by-treatment contrasts, interval definitions, confidence intervals, clustered standard errors, missing outcomes and sensitivity analyses. The earlier healthcare trial should be compared only after its allocation and endpoint definitions are aligned.

**Twin's next question:** If two participants both avoid clicking, but one identifies the deception and the other avoids all unfamiliar requests, what independent evidence could distinguish genuine discrimination from blanket avoidance without assuming either behavior is always safe?

**IP check:** Published designs and generic methodological questions only; no unpublished platform mechanisms, formulas, participant records or confidential operational material.
