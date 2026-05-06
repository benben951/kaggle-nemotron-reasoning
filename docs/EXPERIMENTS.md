# Experiments

Best public/validation result: TBD

| Run | Date | Method | Local Evidence | Submission | Result | Notes |
|---|---|---|---|---|---|---|
| baseline-lookup-v0 | 2026-05-07 | Join public test ids to train answers when ids overlap | Generates 3 answers for current public test file | `submissions/baseline_lookup.csv` | CSV submission rejected | Useful discovery: this is not a normal CSV-prediction competition |
| taxonomy-v0 | 2026-05-07 | Rule-based prompt taxonomy | Writes task-family counts | `docs/task_family_counts.csv` | Local only | First taxonomy under-counts several hidden families because the generic Alice wording needs richer parsing |

## Rules

- Record every submission before spending a Kaggle attempt.
- Never treat public-test leakage or id overlap as hidden leaderboard evidence.
- Separate deterministic solvers, model prompts, and post-processing in the notes.
- Preserve failure cases; they are useful for interview stories.
- Do not spend leaderboard/model submissions before confirming the accepted artifact type.
