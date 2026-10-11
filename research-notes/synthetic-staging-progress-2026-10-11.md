# A small engineering step toward better measurement

*Research progress note — 11 October 2026*

The question driving this work remains whether a single aggregate risky-choice rate hides meaningful differences in how people respond to social-engineering scenarios.

I have been building a **separate synthetic testing environment** for VISHWAR to explore how scoring definitions behave. The current work compares a CTR-only calculation with a candidate formula that also includes time-to-report, quiz performance and repeated risky choices. Simple constructed examples already show different candidate scores at equal CTR; that is a property of the formula, not an empirical finding about people.

Some application engineering tests have exercised synthetic session persistence and access isolation. A full authenticated browser-to-database test of a new core module was **not yet independently completed** at the time of this note. The candidate composite is experimental and has not replaced deployed scoring.

The next research questions concern measurement: what constitutes a comparable decision opportunity, what missing report time means, whether repeated-category risk is the intended repeat-event quantity, and whether the extra signals add any reliable, calibrated information about future behavior.

Related reproducible exercise: [Experiment 002](../experiments/composite-vs-ctr-synthetic/README.md). No real participant outcomes or private infrastructure details are shared here.
