# Nemotron Public Route Retro and Self-Owned Push Plan

Date: 2026-06-12 CST

Scope: Kaggle NVIDIA Nemotron Model Reasoning Challenge only.

## Current Position

- Current best public score: `0.86`.
- Best scoring artifacts so far:
  - v62 Mirza public artifact relay: `0.86`.
  - v68 VNG Refine clean relay: `0.86`.
- Latest known rank after v68: `459 / 4207`.
- Approximate top-10%-style line: rank `421`, still score `0.86`.
- Gap to line: about `38` ranks.
- Practical implication: we are in the medal-contending tie band, but not safely inside it. A true `0.87` is the clean path to a safe bronze.

## Official Transfer Table

| Version | Route | Public claim / intent | Our official public score | Transfer verdict |
|---|---|---:|---:|---|
| v59 | Huikang LB0.85 faithful repro | `0.85` baseline | `0.67` | Failed transfer |
| v60 | Mohamed replay 0.86 faithful repro | `0.86` replay training | `0.84` | Partial transfer |
| v61 | Kienngx Tinker adapter artifact | strong public adapter | `0.85` | Useful but below frontier |
| v62 | Mirza public adapter artifact | `0.86` artifact | `0.86` | Best transfer |
| v63 | Kuang 0.87 training output relay | `0.87` title/output | `0.84` | Failed transfer |
| v65 | Hammad/Cocoa 0.87 SVD clean relay | `0.87` SVD/medal route | `0.85` | Failed to reach frontier |
| v67 | Habanwer ATLAS clean relay | independent ATLAS SFT route | `0.62` | Severe regression |
| v68 | VNG Refine nested clean relay | public refine artifact, packaging fixed | `0.86` | Ties best, no breakthrough |
| v66 | Biohack D3 sparse clean relay | sparse trust finisher | pending | Final exploratory probe |

## What Actually Worked

1. Public artifact relay worked better than faithful retraining.
   - v62 and v68 reached `0.86`.
   - Fresh or continued training routes often underperformed their advertised titles.

2. Strong base formatting and broad target coverage matter.
   - v62 uses `r=32`, `lora_alpha=64`, and target modules including `gate_proj` and `lm_head`.
   - v68 uses `r=32`, `lora_alpha=32`, includes `lm_head`, and fixes packaging around a strong adapter.

3. Packaging correctness is real but not enough.
   - v68 fixed a nested zip into a valid root-only submission and recovered to `0.86`.
   - This shows packaging can hide score, but packaging alone does not create `0.87`.

4. The `0.86` band is a structural plateau.
   - Several distinct-looking public routes converge around `0.84-0.86`.
   - Breaking `0.87` likely requires a real behavior improvement, not just a repack, SVD, or tiny SFT tweak.

## Why Routes Failed

1. Public titles are not official score guarantees.
   - Some notebooks are named `0.87`, but direct relays scored `0.84` or `0.85`.
   - The title can reflect an author's private state, a stale score, a different artifact, or optimism rather than the actual output we relay.

2. Local validation is weakly correlated.
   - Earlier fixed validation checks predicted gains that did not transfer.
   - Some routes improve formatting or train loss while harming exact final-answer behavior.

3. Extra SFT can destroy the answer distribution.
   - v67 ATLAS trained a real large adapter but scored only `0.62`.
   - Likely failure mode: the adapter learned solver-trace style or internal validation quirks, but lost the exact answer behavior expected by official scoring.

4. Compression/SVD/sparse finishing mostly reshuffles an existing family.
   - v65 landed at `0.85`.
   - v68 tied `0.86`.
   - v66 likely shares the same adapter-model size as v68 (`3,554,384,888` bytes), so it may be a related weight family with config/package differences.

5. Duplicate artifacts are common.
   - v69 looked new but matched v62 source zip bytes and config shape.
   - Submitting duplicate wrappers wastes official attempts.

## Bottom-Level Logic of the Strong Public Routes

### v62 Mirza family

- This is the strongest confirmed family.
- It uses a large LoRA adapter with `r=32`, `alpha=64`, and broad module targeting.
- It likely improves answer formatting and multiple reasoning task families without over-specializing.
- It is currently the best anchor for any self-owned route.

### v68 / VNG / Biohack-like family

- This family appears to produce or transform a `r=32`, `alpha=32` adapter around a Kienngx/SVD/finisher lineage.
- It can reach `0.86`, but so far it does not beat v62.
- The main value is that it is a second `0.86` anchor with different config/target-module shape.

### Training-heavy routes

- Faithful retrains and continuation SFT are fragile.
- They can generate plausible logs and valid LoRA files but still miss official exact answers.
- The official metric is final-answer exact match under hidden prompts, so any route that changes response style or overfits generated traces is dangerous.

## Self-Owned Route Proposal

Goal: build a controlled `0.86 -> 0.87` candidate instead of relaying more public titles.

### Route A: Anchor-Preserving Adapter Merge

Use v62 as the primary anchor and add only small, controlled deltas from v68/v66-like adapters.

Core idea:
- v62 is known public `0.86`.
- v68 is also public `0.86` but likely captures a different part of the solution space.
- Instead of full replacement, test small adapter arithmetic:
  - `candidate = v62 + lambda * (v68 - compatible_projection(v62))`
  - Try small `lambda`: `0.05`, `0.10`, `0.15`, `0.20`.
  - Preserve v62 files/config wherever possible.
  - Only merge compatible tensor keys and shapes.
  - Keep LoRA rank `<=32`.

Why this is better than blind SFT:
- It starts from a confirmed `0.86` artifact.
- It minimizes behavior drift.
- It tests whether v68 contains complementary wins without sacrificing v62's formatting and broad coverage.

Risk:
- Adapter tensors may not be shape-compatible across target-module sets.
- A naive merge can silently degrade.
- Needs validation and probably official probes, but it is more principled than another public-title relay.

### Route B: Packaging-Equivalent Differential Audit

Before merging, prove whether v66 and v68 are actually the same underlying adapter.

Checks:
- Compare adapter model byte sizes from logs.
- If possible in Kaggle without local multi-GB download, compute SHA-256 of `adapter_model.safetensors` for v66 and v68 source outputs.
- If hashes match, v66 is effectively redundant with v68 except config/package.
- If hashes differ despite same byte size, v66 may still be worth analyzing as an alternate delta source.

### Route C: Conservative Format-Preserving Micro-SFT

Only consider this after Route A/B.

Rules:
- Start from v62, not from base or a weaker public artifact.
- Train on a tiny format-preservation set, not broad solver traces.
- Freeze or heavily reduce learning rate for modules most likely to disrupt reasoning.
- Use answer-only / boxed-answer preservation checks.
- Stop immediately if strict formatting or known public-proxy exact answers regress.

Why this is lower priority:
- Our prior custom SFT attempts and v67 show training can quickly damage official behavior.
- Without a stronger validation proxy, micro-SFT is still risky.

## Validation Needed Before More Official Submissions

We need a harder validation proxy, not just fixed-correct counts.

Recommended proxy:
- Build a small public-train split by task family.
- Evaluate exact final answer, strict boxed output, and empty/partial-answer rate.
- Add "regression sentinels" from cases where v62 is likely strong:
  - binary exact-answer formatting
  - numeral systems
  - unit conversion decimals
  - cipher/string outputs
  - equation-transform symbol outputs
- Score candidates by "do not break v62" first, "add new wins" second.

Acceptance gate for any self-owned candidate:
- No increase in empty answers.
- No strict formatting regression.
- Must preserve v62-style target modules/config unless there is a clear reason.
- Must be materially different from duplicate public artifacts by hash or tensor summary.

## Immediate Next Steps

1. Wait for v66 official result.
2. If v66 is `0.86` or lower, stop public relays unless a genuinely new `0.87+` artifact appears.
3. Build a Kaggle-side analysis kernel that mounts v62, v68, and v66 outputs and computes:
   - adapter_config diff
   - tensor key overlap
   - tensor shape overlap
   - per-tensor norms
   - SHA-256 for adapter files
4. If v62/v68 tensor overlap is sufficient, generate 2-4 conservative merge candidates.
5. Submit only the best one or two merge candidates before deadline.

## Current Recommendation

- Keep v62/v68 `0.86` as the public-score anchor.
- Do not chase more public notebook titles unless they expose a genuinely different large adapter.
- The best self-owned chance is a v62-preserving merge with v68/v66-family deltas, because it attacks the exact problem we have: moving within the `0.86` tie band without breaking the base behavior.
