# A small engineering step toward better measurement

*Research progress note — 11 October 2026*

The question driving this work remains whether a single aggregate risky-choice rate hides meaningful differences in how people respond to social-engineering scenarios.

I have been building a **separate synthetic testing environment** for VISHWAR to explore how scoring definitions behave. The current public exercise compares constructed sequences of risky, safe, and context-dependent decisions. Identical aggregate risky-choice rates can conceal different choice distributions and ordering; this is a property of the constructed examples, not an empirical finding about people.

Some application engineering tests have exercised synthetic session persistence and access isolation. A full authenticated browser-to-database test of a new core module was **not yet independently completed** at the time of this note. No candidate proprietary scoring algorithm is published in the revised exercise.

The next research questions concern measurement: what constitutes a comparable decision opportunity, how to distinguish different actions without inventing a separate reporting feature, whether repeated-category risk is the intended repeat-event quantity, and whether the extra signals add any reliable, calibrated information about future behavior.

Related reproducible exercise: [Experiment 002](../experiments/composite-vs-ctr-synthetic/README.md). No real participant outcomes or private infrastructure details are shared here.
