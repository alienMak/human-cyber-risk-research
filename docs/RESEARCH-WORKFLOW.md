# Keeping a research history without rewriting the past

I started planning this research in February 2025 and began building VISHWAR during my capstone in August 2025. GitHub is only one way of recording the work, and it does not capture those earlier months.

The entries in `research/history.json` describe historical milestones. They are not dated commits. When a specific day isn't supported by notes or source material, I use a month or year.

## How the automated review works

1. Add a real milestone to `research/history.json` with its original period, concise description, and evidence.
2. Mark it `documented` and `public: true` only when its wording and disclosure are ready for public release.
3. Each day the workflow generates `docs/research-history.md` from the reviewed entries.
4. If the generated archive has changed, the workflow opens a pull request for review. Otherwise it does nothing.
5. Review the pull request for factual accuracy, writing style, and IP boundaries before merging.

This runs independently of the daily documentation check. It does not change the VISHWAR product repository, create random commits, impersonate a human contributor, or promise daily green contribution squares.

If GitHub Actions cannot open a pull request because of repository settings, an administrator may need to enable **Allow GitHub Actions to create and approve pull requests** in repository Actions settings.

## Research additions beyond the timeline

Use ordinary commits or reviewable pull requests for actual literature notes, experiment designs, synthetic datasets, reproducible notebooks, and results. A daily check is a useful reminder to do maintenance, not a substitute for doing the research.
