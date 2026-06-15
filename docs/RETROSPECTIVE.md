# Retrospective - Kaggle NVIDIA Nemotron Reasoning

Last updated: 2026-05-29

## What Worked

- The project developed useful tooling around artifact validation, log summarization, and submission gating.
- The team moved away from weak prompt-only patches toward a reference-corpus SFT approach.
- The recovered public Progress Prize pipeline gave a clearer direction: deterministic reasoning traces, masked completion loss, and family-level metrics.
- The dataset-mounted v50A path fixed the large-notebook payload problem and is ready for a real quota window.

## What Did Not Work

- Early prompt/format patches did not generalize.
- Several runs learned to repeat instructions or reason too long instead of emitting the final boxed answer.
- v40 compact still concentrated correctness in `numeral`, which is not enough for a medal route.
- Kaggle GPU quota and kernel creation quirks consumed a lot of operational time.

## Core Lesson

The challenge is not only reasoning quality. It is also answer latency, final-answer extraction, family coverage, and artifact discipline.

For this competition, a candidate that looks better in one family is not enough. The model must produce stable boxed answers across families.

## Current Medal Probability

Low unless v50A or a larger masked-corpus route produces broad cross-family correctness after GPU quota returns.

The project is still valuable as an Agent workflow case study because it has:

- repeatable corpus building;
- validation-gated submissions;
- artifact verification;
- clear failure analysis.

## Next Research Questions

1. Does masked completion loss on reference-tail reasoning improve non-`numeral` families?
2. Is max sequence length 2048 enough, or does the reference-tail route need 4096/8192?
3. Can the corpus be mounted as a Kaggle dataset and trained within quota without OOM?
4. Which families remain zero-correct after v50A?
5. Is rank16 sufficient, or must we return to rank32 after proving the data path?

## Resume Packaging

Strongest framing:

```text
Built a Kaggle reasoning-model fine-tuning pipeline for NVIDIA Nemotron using LoRA artifact validation, family-level generation checks, masked SFT corpus construction, and strict submission gates to reduce leaderboard waste.
```

Avoid claiming:

- medal-level performance before scores support it;
- general reasoning improvement from format-only runs;
- leaderboard readiness without cross-family validation.

