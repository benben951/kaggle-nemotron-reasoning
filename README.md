# NVIDIA Nemotron Model Reasoning Challenge Lab

Reproducible workspace for the Kaggle NVIDIA Nemotron Model Reasoning Challenge.

## Portfolio Snapshot

This repository is positioned as a reasoning-evaluation and post-training preparation lab. It tracks task-family analysis, deterministic baselines, adapter attempts, failed-run evidence, and submission validation rather than pretending a reasoning competition is just a prompt hack exercise.

- Portfolio angle: LLM reasoning evaluation, experiment discipline, and post-training data workflow
- Core evidence: data inspection, task-family framing, baseline scripts, submission validation, and experiment notes
- Showcase doc: [docs/PROJECT_SHOWCASE.md](docs/PROJECT_SHOWCASE.md)

## What This Project Is Actually About

The value of this repository is not a public leaderboard screenshot. The value is the workflow:

- inspect the dataset and competition constraints
- group prompt families and identify where deterministic logic helps
- separate sanity-check baselines from real model-improvement work
- document failed runs and dead ends as evidence, not embarrassment

That makes it a stronger portfolio artifact than a one-off competition notebook.

## Competition Framing

- Kaggle competition: `nvidia-nemotron-model-reasoning-challenge`
- Local workspace includes `train.csv` and `test.csv`
- Early public test overlap means the first baseline is a sanity check, not a hidden-score signal

## Practical Strategy

1. Categorize prompt families and reasoning types
2. Build deterministic solvers where structured logic is possible
3. Use model-based reasoning only where deterministic methods break down
4. Track every run with validation, notes, and submission evidence
5. Prepare adapter or post-training artifacts only when the evidence justifies the extra cost

## Quick Start

```powershell
python scripts/inspect_data.py
python scripts/make_baseline_submission.py
```

## Project Structure

```text
data/raw/                 downloaded competition data
docs/                     strategy and showcase notes
scripts/                  reproducible utilities
src/nemotron_reasoning/   project code
submissions/              generated outputs
```

## Resume Angle

Built a reproducible reasoning-challenge lab for the NVIDIA/Kaggle Nemotron competition, including task-family analysis, deterministic solver baselines, experiment tracking, and submission validation as a bridge toward post-training and adapter workflows.
## Post-Competition Retro

Final Nemotron retrospective and reusable Kaggle workflow assets:

- [Nemotron final retro](docs/NEMOTRON_FINAL_RETRO_20260616.md)
- [Next Kaggle playbook](docs/NEXT_KAGGLE_PLAYBOOK.md)
- [Kaggle submission guardrails](docs/KAGGLE_SUBMISSION_GUARDRAILS.md)
- [Full experiment ledger](docs/EXPERIMENTS.md)
