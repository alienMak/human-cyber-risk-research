# When security-conscious behavior breaks security policy

**Paper:** [Sarah Alromaih, Ivan Flechais and George Chalhoub, *Beyond the Office Walls: Understanding Security and Shadow Security Behaviours in a Remote Work Context*](https://www.usenix.org/conference/soups2024/presentation/alromaih). SOUPS 2024, pp. 507–525.  
**Original full text:** https://www.usenix.org/system/files/soups2024-alromaih.pdf  
**Type:** Peer-reviewed primary qualitative study. **Access:** FULL TEXT APPRAISED on 18 October 2026 (methods §§3.1–3.6, findings §§4.1–4.4, discussion §§5–6). Earlier abstract-only note expanded after checking the original PDF. **Added:** 18 October 2026.

## What the authors investigated

The authors used Grounded Theory and **20 interviews with remote workers** to explore how personal security practices relate to organizational security expectations. They describe *shadow security*: actions by security-conscious people that depart from official policy. Their reported model explains how perceived alignment or misalignment between personal and organizational security models can produce compliance, noncompliance or shadow security (publisher abstract).

The publisher summary highlights informal security communication, consistency of security interactions and user-centered design of remote-work security solutions as implications. These are recommendations grounded in qualitative analysis, not controlled estimates of intervention effectiveness.

## Twin's challenge

If a worker uses a non-approved process, did they ignore security, adapt to an unusable rule, or introduce an unrecognized vulnerability while trying to protect themselves?

**The policy deviation alone cannot decide.** The worker's intention, the official rule, the actual risk consequences and the practical alternatives are different evidence types. Security-conscious intent is not proof that a workaround is safe. Likewise, policy compliance is not proof that the outcome was safe.

This connects to [Chen et al. (SOUPS 2024)](2026-10-18-recognition-without-reporting.md), where employees discussed reporting barriers, feedback and consequences. The two studies examine different settings and outcomes; their themes should not be combined into a prevalence estimate or a single causal model.

## What this evidence can and cannot support

- **Supports:** remote workers in the interviewed sample described security-related behavior shaped by both personal and organizational understandings; the authors identified a conceptual category of shadow security.
- **Does not support:** a percentage of remote workers who practice shadow security, a comparative safety effect of violating versus following policy, or an inference that any individual deviation is justified.
- **Not verified this cycle:** detailed participant recruitment, interview protocol, coding reliability, negative cases, exact quotations, ethics treatment and limitations in the full text.

## Eight-domain appraisal status

**Deferred — ABSTRACT-ONLY.** A full appraisal requires checking (1) interview and sampling design, (2) participant context, (3) definitions of compliant/noncompliant behavior, (4) researcher positionality and contextual confounding, (5) coding procedures, (6) analysis and negative cases, (7) transferability, and (8) ethics and available materials. No unsupported Yes/No scores are assigned.

## Open research questions

1. Can a study distinguish **policy adherence** from **actual security outcome**, especially when a participant deliberately uses a workaround?
2. Does a worker perceive the official control as inaccessible, inconsistent, too costly, or less protective than their alternative? Those are hypotheses to investigate, not observed explanations for every case.
3. How should researchers record disagreements between an individual's account of a workaround and the organizational security team's interpretation without assuming either side is automatically correct?

**Researcher review question:** When someone breaks a security rule because they think their alternative is safer, what evidence would establish whether that decision improved or worsened security?

**Public IP gate:** This note contains only published high-level research, explicitly labeled inference and general future questions. No private formulas, unpublished assessment mechanisms, architecture, participant records or confidential organizational information.


## Full-text follow-up: what the paper actually allows us to infer

**Sampling and observation (printed pp. 509–511):** The authors recruited 20 volunteers using purposive and snowball sampling via online platforms. Eleven worked fully remotely and nine in hybrid settings (§3.1). Semi-structured interviews were conducted over Zoom or Teams, recorded and anonymized; the three-person pilot was not included in analysis (§§3.2–3.3). This is **self-reported practice**, not observed file transfers, policy audits or incident outcomes.

**Qualitative analysis (printed pp. 510–511):** Two researchers used constructivist Grounded Theory, iteratively coding transcripts into a 217-code codebook. The paper reports average Cohen's kappa of 0.85, a third-researcher cross-check, and member checking with three participants (§3.4). Those steps support transparency and consistency but do not remove selection, recall or interpretation bias. The authors report saturation between interviews 18 and 20; this is a qualitative judgment, not proof that every possible workaround was captured.

**Examples from findings (printed pp. 511–516):**
- Some participants described inspecting sender details, using bookmarked websites and separating work and personal activity as proactive practices (§4.1.1).
- A participant described password reuse related to restrictions on device login, and another described reluctance to use a company VPN because of speed and privacy concerns (§4.4.2). These were **reported practices and explanations**, not independent security measurements.
- Another participant described choosing an alternative file-sharing platform despite an organizational prohibition because they perceived the official option as inadequate (§4.4.2). This is an example of **security-motivated noncompliance**, not proof that the alternative was safe.
- A different participant described emailing documents to a personal account to work around printing restrictions (§4.4.3). The authors distinguish convenience-driven deviations from security-motivated ones, rather than treating all violations as equivalent.

**Most consequential limitation (printed p. 511, §3.6):** The authors did **not** independently compare participants' understanding of policy with their employers' actual policies. They acknowledge that misunderstandings, wording or changed rules could explain some apparent breaches. That directly limits any claim about verified noncompliance. They also identify social-desirability bias, sample size and diversity, and researcher interpretation as limitations.

## Eight-domain full-text appraisal

| Domain | Assessment | Basis |
| --- | --- | --- |
| Design | Yes for exploratory explanation | Constructivist Grounded Theory and interviews fit reported security practices, not risk-effect estimation (§§3, 4). |
| Sampling | Partial | Purposive/snowball recruitment; 20 volunteers, 11 remote and 9 hybrid; not representative (§3.1). |
| Outcome definition | Partial | Categories reflect participants' reported behavior and perceived policy; no independently measured security outcome (§§3.2, 3.6, 4.4). |
| Confounding | Partial | Job role, workplace policy, remote arrangements and perceived friction not causally separated (§§3.1, 3.6). |
| Measurement | Partial | Interview guide and recorded accounts; social desirability and policy misunderstanding remain (§§3.2, 3.6). |
| Analysis | Yes for documented qualitative process | Iterative coding, 217 codes, reported kappa 0.85 and three member checks (§3.4); does not establish population prevalence. |
| Generalization | Partial | Young, self-selected multi-industry sample and retrospective self-report (§3.6). |
| Ethics/reproducibility | Partial | Ethics approval, consent, anonymization and interview guide/codebook in appendices (§§3.5, appendices); raw accounts not independently reanalyzed here. |

**Interpretive correction:** A self-reported workaround can reveal friction and employee reasoning, but the study cannot establish whether it reduced security risk. Any future empirical comparison should distinguish documented policy requirements, employee understanding, work-task constraints and independently assessed consequences. Do not collapse those into a single compliance label.

**Next question:** If a policy is misunderstood, should the resulting behavior be interpreted as a knowledge gap, a communication failure, an unusable control, or some combination? The study identifies plausible mechanisms but cannot adjudicate a particular workplace without checking the policy and consequences.
