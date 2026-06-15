---
name: kaggle-competition-playbook
description: Use when planning, auditing, running, or postmorteming a Kaggle competition, especially medal pushes, Featured competitions, public baseline reproduction, validation calibration, leaderboard plateau decisions, submission budgeting, or turning competition failures into reusable guardrails.
---

# Kaggle Competition Playbook

Use this skill to avoid repeating the Nemotron failure pattern: lots of effort, late prior-art pivot, weak validation correlation, and a misunderstood medal line.

## Default Loop

```text
Rules -> medal math -> prior art -> reproduce strong baseline -> calibrate validation -> improve -> submit with budget -> retro
```

## 1. Lock Scope And Rules

Before building anything, record:

- competition slug and URL;
- competition category;
- deadline in UTC and local time;
- team count;
- award and medal eligibility;
- official artifact/submission format;
- official submission limit;
- current public leaderboard score bands.

Never mix unrelated competitions in one experiment log, submission ledger, or decision thread.

## 2. Compute Medal Cutoffs

Use the official Kaggle competition medal table, not a generic `10/20/30%` table.

For competition medals:

- `0-99` teams: bronze top `40%`, silver top `20%`, gold top `10%`.
- `100-249` teams: bronze top `40%`, silver top `20%`, gold top `10`.
- `250-999` teams: bronze top `100`, silver top `50`, gold top `10 + 0.2%`.
- `1000+` teams: bronze top `10%`, silver top `5%`, gold top `10 + 0.2%`.

Run:

```powershell
python C:\Users\jie13\.codex\skills\kaggle-competition-playbook\scripts\kaggle_medal_cutoffs.py <team_count>
```

Write the cutoff ranks into the project README or strategy doc on day 0.

## 3. Prior-Art First

Before self-owned training:

1. Search public notebooks, discussions, datasets, and model artifacts.
2. Build a route table: claimed score, actual author rank if visible, sources, runtime, artifact format, and risk.
3. Reproduce the strongest public baseline exactly.
4. Submit once if the reproduction is structurally valid and expected to establish a score anchor.
5. Only then start custom training or merges.

Decision rule:

```text
If a public route is near the medal line, reproduce it before inventing a custom route.
```

## 4. Calibrate Validation

A validation proxy is not trusted until it predicts official leaderboard movement.

Minimum proxy:

- exact final-answer score;
- strict output-format score;
- empty/partial-answer rate;
- family/category coverage;
- regression sentinels where the current best is known strong;
- preservation score against the best official anchor.

After 2-3 official submissions, compare local proxy prediction with leaderboard movement. If correlation is weak, fix the proxy before spending more GPU or submissions.

## 5. Budget Submissions

Maintain a submission ledger with:

- version;
- kernel slug and exact version;
- output file;
- artifact hash or structural fingerprint;
- description;
- submission ref;
- status;
- public score;
- rank snapshot;
- decision and next action.

Rules:

- Preserve a known-good score before risky probes.
- Reserve final-week submissions for high-signal candidates.
- Do not submit duplicate hashes.
- Do not resubmit unchanged artifacts after `SubmissionStatus.ERROR`.
- Do not spend more than 2-3 submissions in the same rounded-score band unless rank movement proves value.

## 6. Stop Plateaus

Stop a route family when:

- three materially different variants tie the same rounded score without rank movement;
- two variants from the same artifact family produce `SubmissionStatus.ERROR`;
- a public-title route underperforms its claimed score by at least one score band;
- local validation improves but official score regresses twice;
- another attempt is only packaging churn without new structural evidence.

Pivot to:

- a stronger public baseline;
- a better validation proxy;
- a higher visible score-band route;
- a controlled delta from a known-good anchor;
- or a retro if the competition is over or budget is exhausted.

## 7. Use Kaggle Submission Guardrails

When pushing or submitting Kaggle kernels, also use `kaggle-submission-guardrails`.

Minimum evidence before official submission:

- exact kernel version;
- output file visible in `kaggle kernels files`;
- logs proving source mounts and output artifact structure;
- artifact format validation;
- explicit user approval in the current context.

## 8. Retro Every Competition

At the end, create a retro with:

- final public/private score and rank;
- correct medal math;
- route ledger;
- what worked;
- what failed;
- validation correlation;
- submission budget analysis;
- process failures and new guardrails;
- next-competition changes.
