# Submission Ledger - Kaggle NVIDIA Nemotron Reasoning

Last updated: 2026-05-29

Purpose: track leaderboard submissions and submission-eligible artifacts. Do not treat a Kaggle kernel run as a submission unless it produced and submitted a valid `submission.zip`.

## Current Leaderboard Anchor

| Item | Value |
| --- | --- |
| Current public baseline noted locally | `0.54` |
| Target band | about `0.86` |
| Best preserved real artifact | `nemotron-rule-distill-v35-v3/submission.zip` |
| Current quality status | blocked by validation gate |

## Known Submission / Artifact Records

| Version | Artifact / Kernel | Local validation | Submit status | Decision |
| --- | --- | --- | --- | --- |
| v23 | rank-32 LoRA baseline | not fully reconstructed here | submitted historically | current weak public baseline around `0.54` |
| v35-v3 | `outputs/kaggle/submissions/nemotron-rule-distill-v35-v3/submission.zip` | `fixed_correct=9/144`, `strict_single_boxed=9/144`, only `numeral` signal | do not submit again | structurally valid but quality-blocked |
| v38 | `v38-formatfix-medium-60steps` | `fixed_correct=2/24`, `strict_single_boxed=0/24` | not submitted | blocked |
| v40 compact | `v40-compact-corpus-tiny-r16-40steps` | `fixed_correct=8/61`, only `numeral` correct | not submitted | blocked |
| v50A | dataset-mounted masked SFT candidate | not run yet due quota | not submitted | first run when GPU quota recovers |

## Submit Rules

Submit only after all are true:

1. Kernel finished and log contains the expected `run_label`.
2. Validation summary was extracted from the actual run log.
3. `submission_gate.py` returns `ALLOW`, or we explicitly record why the gate is too conservative.
4. `submission.zip` passes `validate_lora_submission.py`.
5. Artifact is copied under `outputs/kaggle/submissions/<name>/` with a manifest/hash.

## Do Not Submit

- dummy smoke zips with tiny weights;
- adapters that only improve `numeral`;
- candidates with unstable boxed-answer extraction;
- candidates from stale logs or stale output files.

## Next Submission Candidate

`v50A` dataset-mounted masked SFT, if it clears local validation after GPU quota recovers.

