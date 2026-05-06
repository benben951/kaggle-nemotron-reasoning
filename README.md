# NVIDIA Nemotron Model Reasoning Challenge Lab

This repository is a reproducible workspace for the Kaggle NVIDIA Nemotron Model Reasoning Challenge.

Goal:

- Build a public, resume-worthy reasoning-evaluation project.
- Track experiments with clear data, metrics, prompts, submissions, and failures.
- Develop a practical route toward Kaggle medal contention while producing reusable AI-agent evaluation artifacts.

Competition:

- Kaggle: `nvidia-nemotron-model-reasoning-challenge`
- Deadline from Kaggle CLI: 2026-06-15 23:59:00
- Reward from Kaggle CLI: 106,388 USD
- Local data: `data/raw/train.csv`, `data/raw/test.csv`

## Current Assessment

The first downloaded dataset contains:

- `train.csv`: 9,500 rows with `id`, `prompt`, and `answer`.
- `test.csv`: 3 rows with `id` and `prompt`.

The public test ids currently overlap with train ids, so the first baseline is a sanity-check submission, not evidence of hidden leaderboard quality.

## Project Structure

```text
data/raw/                 Kaggle-downloaded data
docs/                     Strategy, experiment notes, resume packaging
scripts/                  Reproducible command-line utilities
src/nemotron_reasoning/   Project code
submissions/              Generated Kaggle submissions
```

## Quick Start

Generate a sanity-check answer file for the tiny public test file:

```powershell
python scripts/make_baseline_submission.py
```

Inspect the data:

```powershell
python scripts/inspect_data.py
```

## Strategy

This competition is not a normal tabular CSV-prediction race. Public competition material and Kaggle behavior indicate that the real deliverable is a model-improvement artifact, such as a compatible LoRA adapter, plus notebook/write-up evidence. The local answer-file baseline is therefore only a data sanity check.

This project will not chase a single prompt trick. The intended route is:

1. Categorize task families from prompts.
2. Build deterministic solvers for structured families where possible.
3. Use model-assisted reasoning only where deterministic solvers fail.
4. Track every experiment with local validation and submission evidence.
5. Prepare a lightweight fine-tuning / data-curation / LoRA workflow if local or cloud compute is available.
6. Package the final work as an agentic reasoning evaluation system, not just a Kaggle score.

## Resume Angle

Chinese:

> 参与 NVIDIA/Kaggle 推理挑战，构建可复现的推理任务解析、规则求解、实验追踪和提交校验工作流，将 LLM 推理问题拆解为可评估的任务族与错误类型。

English:

> Built a reproducible reasoning-challenge lab for the NVIDIA/Kaggle Nemotron competition, including task-family analysis, deterministic solver baselines, experiment tracking, and submission validation.
