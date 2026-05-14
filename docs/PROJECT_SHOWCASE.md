# Project Showcase

This repository tracks a reproducible approach to the NVIDIA/Kaggle Nemotron reasoning challenge. The goal is to demonstrate reasoning-task evaluation, post-training data preparation, and experiment discipline.

## Why This Project Matters

The competition is not a normal tabular CSV task. The useful public portfolio story is:

- identify reasoning task families;
- build deterministic baselines where possible;
- curate training and validation data;
- test LoRA or distillation workflows;
- track failed runs instead of hiding them;
- produce evidence that connects evaluation to post-training.

## Current Workstreams

| Workstream | Purpose |
| --- | --- |
| Task-family analysis | Split prompts into structured reasoning types. |
| Deterministic solvers | Build reliable baselines for tasks such as conversion, equations, and symbolic transformations. |
| SFT data pipeline | Convert examples into instruction-style JSONL for small post-training attempts. |
| LoRA smoke training | Validate adapter artifact creation and submission compatibility. |
| Experiment ledger | Record run settings, validation signals, failures, and submit/do-not-submit decisions. |

## Resume Angle

This project supports three claims:

1. I can turn an ambiguous LLM competition into a structured evaluation problem.
2. I can prepare post-training style datasets and run adapter-based experiments.
3. I can document negative results and avoid overclaiming weak submissions.

## Next Improvements

- Publish a sanitized experiment table.
- Add task-family distribution charts.
- Add baseline solver examples with unit tests.
- Add a short model-card style report for the strongest adapter attempt.
- Add final leaderboard or submission evidence when available.
