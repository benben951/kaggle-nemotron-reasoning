# Next Kaggle Playbook

Purpose: turn the Nemotron experience into a reusable operating loop for the next Kaggle competition.

## Default Loop

```text
Rules -> medal math -> prior art -> reproduce strong baseline -> calibrate validation -> improve -> submit with budget -> retro
```

## Day 0: Scope And Medal Math

Record these before any model work:

| Item | Required evidence |
| --- | --- |
| Competition slug | Kaggle URL or CLI output |
| Category | Featured / Research / Playground / other |
| Team count | Kaggle CLI or leaderboard download |
| Award eligibility | Competition overview |
| Medal rules | Kaggle progression page |
| Public score bands | Leaderboard snapshot |
| Official artifact format | Sample submission or rules |
| Submission limit | Rules / competition page |
| Deadline | Absolute UTC and local time |

Medal cutoff rule for Kaggle competition medals:

| Team count | Bronze | Silver | Gold |
| ---: | ---: | ---: | ---: |
| `0-99` | Top `40%` | Top `20%` | Top `10%` |
| `100-249` | Top `40%` | Top `20%` | Top `10` |
| `250-999` | Top `100` | Top `50` | Top `10 + 0.2%` |
| `1000+` | Top `10%` | Top `5%` | Top `10 + 0.2%` |

Use the local skill script after it is installed:

```powershell
python C:\Users\jie13\.codex\skills\kaggle-competition-playbook\scripts\kaggle_medal_cutoffs.py 4330
```

## Day 0-1: Prior-Art First

Do this before self-owned training:

1. Search public notebooks, discussions, datasets, and model artifacts.
2. Build a route table with claimed score, required sources, runtime cost, artifact format, and risk.
3. Reproduce the strongest public baseline exactly.
4. Save logs, output files, and submission refs.
5. Only then start self-owned experiments.

Decision rule:

```text
If a public route is near the medal line, reproduce it before inventing a custom route.
```

## Validation Proxy

A useful proxy must be calibrated against official submissions.

Minimum proxy fields:

- Exact answer score.
- Strict output-format score.
- Empty/partial-answer rate.
- Family/category coverage.
- Regression sentinel set.
- Known-strong baseline preservation.

Calibration rule:

```text
After 2-3 official submissions, compare proxy prediction to leaderboard movement.
If the proxy is not predictive, fix the proxy before spending more GPU.
```

## Submission Budget

Maintain a submission ledger from the first official submission:

| Field | Required |
| --- | --- |
| Version | Yes |
| Kernel slug and exact version | Yes |
| Output file | Yes |
| Artifact hash or structural fingerprint | Yes |
| Description | Yes |
| Submit ref | Yes |
| Public score | Yes |
| Rank snapshot | Yes |
| Decision / next action | Yes |

Budget rules:

- Keep final-week attempts for high-signal probes.
- Do not submit duplicate artifact hashes.
- Do not submit unchanged artifacts after scorer `ERROR`.
- Do not spend more than 2-3 submissions in the same rounded-score band unless rank movement proves value.
- Preserve a known-good score before risky probes.

## Plateau Rules

Stop a route family when any of these are true:

- Three materially different variants tie the same rounded score with no rank movement.
- Two variants from the same artifact family produce `SubmissionStatus.ERROR`.
- A public-title route underperforms its claim by at least one score band.
- Local validation improves but official score regresses twice.
- The same route requires a packaging-only retry without new structural evidence.

Pivot options:

- Stronger public baseline reproduction.
- New validation proxy.
- Higher visible score-band route.
- Controlled self-owned delta from a known-good anchor.
- Stop and write a retro if the competition is over or submission budget is exhausted.

## Kaggle Kernel Guardrails

Before pushing a kernel:

```powershell
python C:\Users\jie13\.codex\skills\kaggle-submission-guardrails\scripts\kaggle_kernel_preflight.py <kernel_dir> --check-remote
```

After pushing:

```powershell
kaggle kernels status <owner>/<kernel>
kaggle kernels logs <owner>/<kernel>
kaggle kernels files <owner>/<kernel>
```

Before official submission:

- Confirm exact kernel version.
- Confirm output file exists.
- Confirm logs include source evidence and output artifact evidence.
- Confirm artifact structure matches the rules.
- Confirm user approval in the current context.

## Retro Template

Create one final retro with:

- Final public/private score and rank.
- Correct medal math.
- Route ledger.
- What worked.
- What failed.
- Proxy correlation findings.
- Submission budget analysis.
- Reusable scripts/skills/checklists created.
- Next competition changes.

## Nemotron Carry-Forward Rules

- Public high-score reproduction should happen earlier.
- Do not spend most of the schedule on weak self-owned SFT before matching strong public baselines.
- Rounded leaderboard scores can hide huge tie bands.
- Source-owner rank inside a rounded score band may not transfer through artifact relay.
- Scorer `ERROR` is a validation/load failure, not a low model score.
- Every process failure should become a guardrail.
