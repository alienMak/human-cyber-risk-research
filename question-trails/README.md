# Question trails: how an answer changes as I keep asking

I rarely get to a useful research question in one jump. An answer exposes an assumption, that assumption opens another question, and sometimes the final answer is less certain than the first. I want to preserve that sequence rather than publish only the polished conclusion.

This is a **public research-question log**, not a transcript of private conversations or a claim that every question was personally asked on the date of the GitHub commit. The **recorded** date is when the trail was written into this repository. **Earlier documented context** identifies a dated related discussion or research note, not necessarily the first time I asked the question. I won't backdate GitHub entries or invent a question's original date.

## Trail register

| ID | Earlier documented context | Recorded here | Starting question | Follow-up direction | Current position | Status | Detailed note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QT-001 | 15 Oct 2026 | 18 Oct 2026 | Does staying on a suspicious call while checking make someone safer? | Exposure time, independent verification, channel separation, outcomes | Verification can be cautious; staying exposed is a separate risk variable | Open: needs empirical evidence | [QT-001](QT-001-verification-while-exposed.md) |
| QT-002 | 6 Aug 2026 | 18 Oct 2026 | Does recognizing a threat lead to safe action? | Recognition, verification, false alarms, final action | Separate knowing from doing | Open: mechanism and transfer | [QT-002](QT-002-recognition-versus-action.md) |
| QT-003 | 9 Sep 2026 | 18 Oct 2026 | Is improvement learning or scenario familiarity? | Novel tasks, delay, context, control groups | Repeated-task gains alone do not establish transfer | Open: needs comparative evidence | [QT-003](QT-003-learning-and-transfer.md) |
| QT-004 | 13 Oct 2026 | 18 Oct 2026 | When is credibility mistaken for proof? | Sender cues, independent channels, confidence | Believable is not authenticated | Open: intervention effects | [QT-004](QT-004-credibility-versus-independent-proof.md) |
| QT-005 | 11 Oct 2026 | 18 Oct 2026 | What does a behavioral risk score actually mean? | Scenario difficulty, missingness, reliability, validity | Numeric precision does not establish validity | Open: validation | [QT-005](QT-005-what-does-a-risk-score-mean.md) |
| QT-006 | 13 Oct 2026 | 18 Oct 2026 | Does the apparent source of advice change reliance? | Human vs software vs AI, correctness, confidence | Source effects need controlled tests | Open: proposed AI extension | [QT-006](QT-006-ai-advice-and-human-reliance.md) |

## How to add to the register

Each substantive daily research run should check whether an existing question trail has advanced or a new one is warranted. Add a row for a genuinely new trail; update a row when its evidence or position changes. Under the table, link a separate note containing:

1. **Trigger and original question:** identify whether this came from a conversation, a paper, a hypothetical, or a newly proposed research question. Never fabricate a quotation or claim the user personally asked a generated question.
2. **Question chain:** Q1, Q2, Q3 ... in order, each with a substantive, specific answer, the reasoning behind it, and what it made us ask next. Avoid short generic answers that could apply to any topic. Preserve uncertainty, counterarguments and changes of mind.
3. **Brief:** a focused explanation of the concrete situation, the key distinction and why the question matters. Expand where necessary instead of padding.
4. **Competing explanations:** at least two plausible mechanisms, not a foregone conclusion.
5. **Evidence ledger:** source, access level (full text, abstract, official record, conceptual only), what it actually supports and what it cannot.
6. **Provisional position and confidence:** explain what is supported, what remains uncertain and why. If evidence is missing, mark **OPEN**. Do not add a separate next-steps or future-test section.
7. **Connections:** cross-link relevant existing research, but don't duplicate an entire paper appraisal.

One row can represent a long question chain. Don't create a row for every rhetorical question; keep the individual questions in the detail note. Preserve earlier wording when possible, but never claim an automated reconstruction is a verbatim personal thought process.

## Depth and consistency rules

A trail is not complete just because it has five questions. The chain should expose the reasoning: why each question follows from the previous answer, where an assumption breaks down, and what would count against the current position. Use as many substantive questions as the argument requires, without manufacturing a fixed count.

- Give a concrete scenario or counterexample where it clarifies a distinction, and label hypothetical examples as hypothetical.
- In the detailed note, explain the *why* behind the answers in prose, not just a one-line table. A short **Reasoning in more detail** section is useful when the table cannot carry the argument.
- Contrast alternative explanations fairly and say what evidence discriminates between them; do not choose a winner without support.
- Attribute empirical findings to the exact study and setting. Do not treat an abstract as full-text scrutiny, or evidence from email phishing as a direct result about calls or AI advice.
- Separate the question's earlier documented context from the date the note was actually recorded; never fabricate a personal chronology.
- Keep the writing direct and curious, without repetitive stock phrasing or exaggerated certainty.
- Preserve the existing headings for the brief, chain, competing explanations, evidence and provisional position. **No standalone Next steps, Next test, Next questions worth testing or action-plan sections.** The chain itself can end with unresolved questions.
- Before committing, inspect the entire edited note and index for correct links, consistent dates, no unsupported claims and no private/proprietary details.

## Daily update discipline

- Check this index and all existing trails before adding another.
- Prefer extending an unresolved chain over manufacturing a new one to satisfy a daily commit target.
- Commit only if there is a substantive, safe, traceable update; otherwise record no change in the daily report.
- Keep patent-sensitive VISHWAR methods, proprietary PR3CORIA information, private messages and participant data outside this public repo.
- Make each trail readable on its own, and write plainly rather than in a generic research-report voice.
