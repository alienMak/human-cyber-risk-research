# Human Cyber Risk Research

**Research notes and experiments connected to [VISHWAR](https://vishwar.com).**

A lot of cybersecurity work focuses on whether someone knows the right answer. I am more interested in what happens when that person has to make a decision under pressure, with incomplete information and an attacker trying to influence the environment around them.

That question sits behind my work on VISHWAR, a simulation-based platform for studying human decisions in cybersecurity situations.

I am using this repository to keep the public side of that research in one place: the questions I am exploring, the assumptions I want to test, and any experiments or results that can be shared responsibly.

## Start here — for prospective PhD supervisors and research collaborators

I am studying **human-centered cybersecurity**, particularly social-engineering decisions, how to measure behavior under uncertainty, and whether simulation-based observations can meaningfully complement conventional awareness measures. My longer-term aim is to develop testable, ethically grounded methods for studying human cyber risk.

**If you have five minutes:**

1. [Research questions](docs/research-questions.md) — the questions motivating this work.
2. [Question trails](question-trails/README.md) — how one question leads to another, including the assumptions and competing explanations along the way.
3. [Literature review and evidence map](literature-review/README.md) — the evidence base, method and limitations.
4. [Experiment 001](experiments/equal-ctr-different-behavior/README.md) — a transparent synthetic counterexample illustrating information lost through aggregation.
5. [Experiment 002](experiments/composite-vs-ctr-synthetic/README.md) — a synthetic decision-sequence comparison, **not** a validated behavioral risk measure.
6. [Research gaps](literature-review/research-gaps.md) — where stronger empirical studies are needed.

**Evidence status:** Current experiments use constructed or synthetic data. They establish reproducible calculations and methodological questions, not predictive validity or effectiveness among real people. Implementation and sensitive technical details remain outside this public research repository.

---


My approach to evaluating evidence and writing about it is explained in [How I approach research](docs/research-writing-and-evidence-standard.md). The literature notes, experiments and research reflections follow the same principle: ask a clear question, show the evidence, and acknowledge what is still uncertain.

## What I'm trying to understand

- How does a person's decision change when the surrounding context makes an attack feel credible?
- What can repeated simulation sessions tell us that a single awareness quiz cannot?
- Which signals might help describe human cyber risk without reducing people to one score?
- How should we distinguish an actual improvement in behavior from someone simply remembering a scenario?

These are research questions, not claims that I have already answered them.

I also keep [question trails](question-trails/README.md) for the questions that don't stop at the first answer. They show the follow-ups, alternative explanations and evidence that might change my mind. Some trails reconstruct earlier research discussions rather than quote them word for word.

## What belongs here

Public research notes, experimental designs, synthetic-data examples, measurement discussions, and documentation of findings once they are ready to share. Some work may lead to code; some may not. I don't want a commit history that suggests progress where there wasn't any.

Start with [the research history](docs/research-history.md), [the research questions](docs/research-questions.md), and [the publishing boundaries](docs/publishing-boundaries.md). The [history workflow](docs/RESEARCH-WORKFLOW.md) explains how earlier work is recorded and checked.

## Literature review (2016–2026)

The [living evidence review](literature-review/README.md) brings together a source matrix, review method, thematic synthesis, and research questions. It is still being expanded, with abstracts distinguished from full-text critical reviews.

## Research notes

- [Three studies on measurement and transfer](research-notes/three-studies-on-measurement.md)


- [From a capstone to a research question](research-notes/from-capstone-to-research.md)
- [What the early pilot can and cannot show](research-notes/what-the-pilot-can-and-cannot-show.md)
- [Measuring a decision without overclaiming](research-notes/measurement-without-overclaiming.md)

## Reading and research watch

I also keep a [literature watch](literature-watch/README.md) for new papers, incident analyses, articles and podcasts connected to the research questions. Assistant-generated interpretations are labelled as drafts until I review them.

## Related literature

[The literature watch](literature-watch/README.md) collects research commentaries on phishing, social engineering, training effectiveness and human decision-making. [Browse the source index](literature-watch/sources.md).

## Relationship to VISHWAR

This is a separate research repository associated with VISHWAR. It is **not** the VISHWAR application source code, a production dependency, or an official release channel. Nothing in this repository should be treated as a complete description of VISHWAR's implementation.

## Updates

Two automated checks run daily: one for documentation issues and another to verify that the published history still matches the recorded milestones. It does not invent research, change files just to create activity, or push to the default branch. Research updates will be added when there is something real to record.

## Contact

For project background, see [vishwar.com](https://vishwar.com).

## New synthetic measurement work (October 2026)

- [Experiment 002 — same risky-choice rate, different decision patterns](experiments/composite-vs-ctr-synthetic/README.md): reproducible synthetic choice-sequence analysis, not predictive validation.
- [Synthetic staging progress note](research-notes/synthetic-staging-progress-2026-10-11.md): engineering progress, scope and unresolved measurement questions.

## Research visuals

![Experiment 001 constructed category distribution](figures/experiment-001-risk-patterns.svg)

![Experiment 002 constructed choice distributions](figures/experiment-002-comparison.svg)

All examples are synthetic; these charts do not establish predictive validity or reveal system implementation.

## Writing and evidence standards

See [research writing and evidence standards](docs/research-writing-and-evidence-standard.md) for source verification, natural research voice, limitations, and public IP safeguards.

## Trust, technology and human decisions: research map

This broader historical research question complements, but does not expand, the **2016–2026 scoping-review inclusion period**: how has technology changed the ways people establish, extend and verify trust, and how do institutions and systems create an appearance of credibility?

- [Historical technology-and-trust timeline](research-timeline/README.md) — selective dated developments, with missing periods explicitly noted.
- [Trust-mechanisms atlas](trust-mechanisms/README.md) — contextual cues, verification friction and explanatory limits.
- [Constructs and measurement](constructs-and-measurement/README.md) — trust, credibility, reliance, verification, confidence and decision quality are different constructs.
- [Human–AI trust](human-ai-trust/README.md) — public conceptual questions about reliance and accountable systems.
- [Research debates](research-debates/README.md) — disagreements and differences in outcome definition.
- [Case studies](case-studies/README.md) — research-grounded cases; not unverified incident reconstructions.
- [Public research-question register](research-questions/README.md) — testable questions and potential confounds.
- [Podcast episode index](podcast-notes/INDEX.md) and [podcast-to-paper links](podcast-notes/cross-references.md) — contextual sources, not peer-reviewed evidence.
- [Legitimate trust and verification](research-notes/legitimate-trust-and-verification.md) — why justified reliance matters alongside deception.
- [Source-audit status and outstanding checks](docs/source-audit.md) — partial audit, not a claim of comprehensive verification.

The historical material and podcasts are separate evidence lanes from the scoped empirical literature review. All synthetic experiments remain illustrations rather than participant-validated results. See [publishing boundaries](docs/publishing-boundaries.md).

For the latest source checks, new paper appraisals and remaining verification gaps, see [research verification status (13 October 2026)](docs/research-verification-status-2026-10-13.md).

## Evidence checks and new source work (October 2026)

- [Full-text NIST Phish Scale appraisal](literature-review/full-text-appraisals/steves-greene-theofanos-2020.md)
- [2025 IEEE S&P training-study appraisal — partial](literature-review/full-text-appraisals/ho-et-al-2025.md)
- [Publisher-transcript review of Darknet Diaries 144](podcast-notes/transcript-reviews/darknet-diaries-144.md)
- [Named DOJ prosecution source note](case-studies/doj-prosecution-record-2023.md)
- [Publisher metadata spot checks](literature-review/publisher-metadata-check-2026-10-13.md)
- [Reproducible Markdown link auditor](scripts/audit_research_links.py) — checks repository paths; optional network checks require running it with --external and manually investigating failures.

Not all podcast episodes have been transcript-reviewed, and an end-to-end external-link audit has not been executed. The notes label these limits rather than implying completed verification.
