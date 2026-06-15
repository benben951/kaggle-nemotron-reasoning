# Project Memory - Kaggle NVIDIA Nemotron Reasoning

Last updated: 2026-06-16

Scope: NVIDIA Nemotron Model Reasoning Challenge only.

## Current Objective

The Nemotron competition has ended. Preserve the final state, route ledger, and lessons so the next Kaggle competition starts with correct medal math, prior-art-first execution, calibrated validation, and stricter submission budgeting.

## Final Position

- Final checked public score: `0.86`.
- Final checked public rank: `475 / 4330`.
- Final latest submission: v84 ref `53714795`, `SubmissionStatus.COMPLETE`, public score `0.86`.
- Final public bronze cutoff estimate under Kaggle 1000+ team competition rules: rank `433`.
- Public gap to bronze cutoff: about `42` ranks.
- Final medals still depend on private/final leaderboard movement and eligibility.

## Latest State

Final docs have been created:

- `docs/NEMOTRON_FINAL_RETRO_20260616.md`
- `docs/NEXT_KAGGLE_PLAYBOOK.md`

Key evidence:

- v23 started around `0.54`.
- Public artifact replication eventually reached repeated `0.86`.
- v62/v68/v71-v75/v78/v79/v84 all tied visible `0.86`.
- v82/v83 both produced `SubmissionStatus.ERROR` and were stopped as a route family.
- Final visible `0.86` band covered ranks `67-1675`, so visible score was not enough for medal placement.

## Primary Lesson

The main miss was strategy timing, not effort.

We should have locked medal math and reproduced the strongest public route earlier. Custom SFT and same-band artifact search consumed too much of the schedule before we had a calibrated official-score proxy.

## Next Move

For the next Kaggle competition:

1. Start with `docs/NEXT_KAGGLE_PLAYBOOK.md`.
2. Use the local `kaggle-competition-playbook` skill to compute medal cutoffs and force prior-art-first execution.
3. Use `kaggle-submission-guardrails` before every Kaggle push or official submission.
4. Build a submission ledger from the first official attempt.
5. Stop same-band variants quickly when leaderboard rank does not move.

## Submission Gate

Do not submit a candidate unless:

- validation is meaningfully better than the current `0.54` baseline;
- correctness is not concentrated only in `numeral`;
- boxed/final-answer format is stable;
- `scripts/validate_lora_submission.py` passes on the downloaded `submission.zip`;
- the artifact is preserved with hash/manifest.

Current gate references from docs:

```text
fixed_correct >= 26
strict_single_boxed >= 20
```

For larger v50-style runs, also require cross-family non-zero correctness.

## Known Negative Directions

- Prompt-only patching without better training data.
- Long reasoning targets that never reach final boxed output.
- Submitting adapters that only solve `numeral`.
- Downloading multi-GB adapters before validation logs justify it.
- Treating `COMPLETE` kernel status as sufficient without log-derived validation.

## Useful Commands

```powershell
python -B scripts\summarize_kaggle_kernel_log.py outputs\kaggle\<run>.log --json > outputs\kaggle\<run>\validation_summary.json
python -B scripts\submission_gate.py outputs\kaggle\<run>\validation_summary.json --min-fixed-correct 26 --min-strict-single-boxed 20
python -B scripts\validate_lora_submission.py outputs\kaggle\<run>\submission.zip
```

## Resume Angle

This project is a reasoning-model fine-tuning and evaluation workflow:

- family-balanced validation;
- output-format reliability;
- LoRA artifact validation;
- masked SFT corpus construction;
- strict no-submit gates to prevent leaderboard waste.
