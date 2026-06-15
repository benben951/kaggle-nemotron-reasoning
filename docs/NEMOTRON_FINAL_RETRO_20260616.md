# Nemotron Final Retro - 2026-06-16 CST

Scope: Kaggle NVIDIA Nemotron Model Reasoning Challenge only.

## Executive Summary

We finished the public leaderboard at:

| Field | Value |
| --- | --- |
| Team | `guozhaojie` |
| Final checked public rank | `475 / 4330` |
| Final checked public score | `0.86` |
| Final latest submission | v84, ref `53714795` |
| Final latest submission status | `SubmissionStatus.COMPLETE` |
| Final latest submission score | `0.86` |
| Official submission count | `20` |

Correct medal math for a 1000+ team Kaggle competition:

| Medal | Kaggle competition rule | Cutoff at 4330 teams |
| --- | ---: | ---: |
| Gold | Top `10 + 0.2%` | about rank `18` |
| Silver | Top `5%` | rank `216` |
| Bronze | Top `10%` | rank `433` |

Public-state conclusion:

- We were approximately `top 10.97%`.
- We were about `42` public ranks outside the bronze cutoff.
- Final medals depend on private/final leaderboard movement and eligibility, not the public snapshot.
- The earlier `gold top 10% / silver top 20% / bronze top 30%` interpretation was not the Kaggle competition-medal rule for this team count.

## What We Actually Achieved

The project moved from a weak public baseline to a stable high public band:

- Initial anchor: v23 public score around `0.54`.
- Best final visible score: repeated `0.86`.
- Final public rank: `475 / 4330`.
- Public score band diagnostic: `0.86` covered ranks `67-1675` in the final checked snapshot, so visible score alone was not enough for medal placement.

This was a strong engineering recovery, but not a medal-safe competition outcome.

## Route Ledger

| Route | Versions | Evidence | Outcome |
| --- | --- | --- | --- |
| Initial rank-32 LoRA baseline | v23 | Existing anchor | `0.54` public |
| Custom format / answer-only / masked SFT attempts | v31-v58 | Fixed validation and kernel logs | Did not transfer to a stronger official score; v53 official was `0.51` |
| Huikang faithful public baseline repro | v59 | Official submission | `0.67` public |
| Mohamed replay public baseline repro | v60 | Official submission | `0.84` public |
| Kienngx/Tinker adapter artifact | v61 | Official submission | `0.85` public |
| Mirza public adapter artifact relay | v62 | Official submission | `0.86` public; first frontier anchor |
| Kuang `0.87` output relay | v63 | Official submission | `0.84` public; title did not transfer |
| Hammad/Cocoa `0.87` SVD clean relay | v65 | Official submission | `0.85` public |
| Biohack D3 sparse relay | v66 | Official submission | `0.84` public |
| Habanwer ATLAS route | v67 | Official submission | `0.62` public; severe regression |
| VNG Refine clean relay | v68 | Official submission | `0.86` public; second frontier anchor |
| Self-owned v62/v68 merge and delta-SVD family | v71-v75 | Official submissions | All tied `0.86`; no visible breakthrough |
| Huikang v27 direct convert | v77 | Official submission | `0.51` public; structural compatibility was not enough |
| 3-way DSVD variants | v78-v79 | Official submissions | Both tied `0.86` |
| Svanik engine/stream relays | v82-v83 | Official submissions | Both `SubmissionStatus.ERROR`; scorer could not produce a score |
| Ayomide rank-309 artifact relay | v84 | Official submission | `0.86`; did not transfer rank-309 tie ordering |

## Self-Developed Work We Should Preserve

1. Validation and artifact tooling
- `scripts/summarize_kaggle_kernel_log.py`
- `scripts/extract_validation_checks_from_kaggle_log.py`
- `scripts/submission_gate.py`
- `scripts/validate_lora_submission.py`

2. Custom corpus/SFT attempts
- Reference-tail and solver-distill corpora.
- Masked completion loss experiments.
- Format-first, answer-only, and `</think>` close-box variants.
- Fixed validation checks by task family.

3. Public artifact repair and relay methods
- Root-only `submission.zip` packaging repair.
- `adapter_config.json` normalization.
- Base model path normalization to `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Lightweight runtime evidence: source path, candidate files, output zip entries, tensor counts, and config summaries.

4. Adapter arithmetic experiments
- v62/v68 direct merge.
- Selective effective-delta SVD.
- Projection delta-SVD.
- Projection plus `lm_head` delta-SVD.
- MLP-lite delta-SVD.
- 3-way DSVD variants.

5. Leaderboard tie-band analysis
- We learned that a rounded public score like `0.86` can hide a huge rank interval.
- Source-owner rank within the same displayed score did not reliably transfer through artifact relay.
- Tie-band movement requires either a real hidden precision improvement or a different official/private behavior, not just the same visible artifact class.

## Why We Missed The Medal Line

1. Medal math was not locked early enough.
- For a 1000+ team Kaggle competition, bronze is top `10%`, not top `30%`.
- We were much closer than most teams, but public rank `475` was outside the approximate bronze cutoff `433`.

2. The high-leverage pivot came late.
- Public artifact routes eventually moved us from `0.54` to `0.86`.
- We spent too many cycles on weak custom SFT before fully prioritizing public high-score reproduction.

3. Local validation was not calibrated to official score.
- Some fixed validation improvements predicted gains that did not transfer.
- The official metric cared about exact hidden final answers, while local checks often over-weighted formatting or a narrow family.

4. The `0.86` band was a plateau.
- Many different-looking routes converged to `0.86`.
- Once we had several `0.86` submissions with no rank movement, more same-family relays had low expected value.

5. Public notebook titles were not score guarantees.
- Several `0.87`-labeled routes scored `0.84-0.85` when relayed or reproduced.
- A public title can reflect a stale artifact, private state, different packaging, or author-side context that does not transfer.

6. Official submission budget became compressed near the end.
- The final week should have been reserved for a small number of high-signal score-band probes.
- Late artifact exploration consumed attempts but did not reach a new visible score band.

## What Worked

- Prior-art-first eventually worked: public artifact relay was the only route that reached `0.86`.
- Packaging audits mattered: fixing root entries and config fields recovered real score in several routes.
- Submission guardrails prevented repeated unchanged scorer failures after v82/v83.
- Leaderboard snapshots were valuable: they showed that `0.86` covered more than 1600 ranks.
- The final documentation and experiment ledger made the decision trail recoverable.

## What Did Not Work

- Long custom SFT without a strong validation proxy.
- Treating fixed validation correctness as a reliable leaderboard predictor.
- Continuing to search inside a saturated rounded-score band after repeated ties.
- Trusting public notebook score claims without exact artifact/leaderboard transfer evidence.
- Assuming Kaggle-visible source files would mount at runtime without broad `/kaggle/input` diagnostics.
- Resubmitting near-identical artifact families after `SubmissionStatus.ERROR`.

## Guardrails For The Next Kaggle Run

1. Day 0 medal math
- Confirm competition category.
- Compute medal cutoffs from official Kaggle progression rules.
- Write the target rank and target score band into the project README.

2. Day 0 prior-art map
- List top public notebooks, artifacts, discussion clues, and claimed scores.
- Reproduce the strongest public route before starting large self-owned training.

3. Score-band ladder
- First objective: match strong public baseline.
- Second objective: reproduce a higher visible score band.
- Third objective: self-owned improvement only after the baseline is reproduced.

4. Proxy calibration
- Use the first official submissions to measure whether local validation correlates with leaderboard score.
- If the proxy is not predictive, redesign the proxy before spending more training cycles.

5. Submission budget
- Keep a ledger from the first official submission.
- Reserve final-week attempts.
- Do not submit duplicate hashes or near-identical packaging retries.

6. Plateau rule
- If three materially different candidates land in the same rounded score band and rank does not move, stop same-band variants.
- Move to a new public route, a stronger validation proxy, or a higher visible score-band reproduction.

7. Process failures become artifacts
- Every Kaggle process failure needs a recorded symptom, root cause, guardrail, and next action.
- If the same failure can recur, add it to a skill, script, or checklist.

## Resume / Portfolio Framing

Accurate framing:

```text
Built a Kaggle reasoning-model competition workflow for NVIDIA Nemotron, improving a LoRA submission pipeline from a 0.54 public baseline to a stable 0.86 public score and top-11% public rank among 4330 teams. Developed validation gates, adapter packaging audits, public baseline reproduction, artifact relay, and postmortem guardrails for future competitions.
```

Avoid claiming:

- A medal before final/private leaderboard confirms it.
- A `0.87` result.
- General reasoning improvement without official score evidence.

## Final Lesson

This was not a wasted competition. It was an expensive lesson in Kaggle strategy:

```text
In Featured competitions, the medal route is not "try many ideas."
It is: compute the medal line, reproduce the strongest public route early,
calibrate validation against official score, preserve submissions for high-signal probes,
and pivot out of rounded-score plateaus quickly.
```
