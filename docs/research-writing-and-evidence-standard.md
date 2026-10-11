# Research writing and evidence standard

The purpose of this repository is to investigate human cybersecurity behavior, not to generate impressive-sounding progress. These principles apply to manual and assisted contributions.

## Voice and readability

- Write directly, in a thoughtful, curious voice. Explain the research question before the method or interpretation.
- Prefer plain, specific language over inflated significance claims or generic AI-style phrasing.
- Use first person for the researcher's genuine interests and questions, **not** to imply that the researcher personally read a paper, ran an automation, or performed a test when they did not.
- Explain concrete examples and the most important limitation. Short paragraphs and descriptive headings are preferable to filler.
- Keep terms consistent: a **grey/context-dependent choice is not, by itself, an incident report**. Do not assume an independent reporting button exists. Differentiate elapsed decision time from time-to-report.

## Evidence ladder

1. **Directly verified:** Exact source, full text or executable evidence checked, and a reproducible citation/test.
2. **Abstract-only:** Paper discovery or summary based only on abstract/metadata, labeled as such.
3. **Constructed synthetic demonstration:** Arithmetic or behavioral counterexample, clearly not participant data.
4. **Working hypothesis:** Plausible research question requiring empirical testing.
5. **Unverified:** Missing evidence, inaccessible methods, uncertain interpretation, or unresolved discrepancy.

Never promote a lower-evidence statement to a factual or causal finding. Include study design, sample, measures, controls, limitations and page/section evidence when available. Separate paper authors' conclusions from our interpretation and from questions for future work.

## Before adding or editing a paper note

- Check the actual paper identity, date, original URL/DOI, peer-reviewed versus preprint status and duplicates.
- Read the full text when it is accessible, otherwise explicitly label **abstract-only** and restrict claims accordingly.
- Record who/what was measured and what comparison supports the stated outcome. Report missing sample/method details as missing.
- Include at least one meaningful limitation and one precise question or methodological lesson.
- Prefer deep examination of one well-supported source to superficial recaps of many sources.
- Never fabricate citations, reading status, user endorsement, participant results, or commit activity.

## Publication and intellectual-property review

Public contributions may include literature synthesis, transparent synthetic descriptive examples and research questions. Do **not** publish unpublished VISHWAR algorithms, scoring formulas or weights, implementation details, proprietary architecture, security configurations, confidential third-party material, real participant data, or patent-sensitive method descriptions. A high-level graph can also disclose methods indirectly, so review figures and code as well as prose. If unsure, keep material private pending IP review.

Deleting published material from the latest revision does not erase the historical Git record. Preserve historical disclosure dates for legal advice.

## Consistency checklist

A reader should be able to tell: **What is the question? What source or data supports this? What exactly did the source establish? What is only our interpretation? What is still unknown? What could be tested next?**

Do not create a commit when nothing meaningful, verified and safe to publish has changed.
