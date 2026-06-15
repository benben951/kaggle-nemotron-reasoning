# Kaggle Experiments (Nemotron Reasoning)

## Tooling note (2026-05-16)

- `scripts/validate_lora_submission.py` includes a default safety gate: adapter weight file(s) must be at least `1024` bytes.
  - This prevents mistaking a dummy/smoke zip for a real trained adapter artifact.
  - For structure-only checks (dummy zip), pass `--min-weight-bytes 0`.

## Automation status (2026-05-15)

Local workspace state:
- This workspace is now a **minimal recovered skeleton** (docs/scripts/outputs exist), but the original project working tree is still missing.
- `.git` is incomplete (only `.git/objects` exists; no `.git/HEAD`, `.git/config`, or refs), so local git history cannot be used to restore files offline.

Kernel / logs:
- No local logs or artifacts for `guozhaojie/nemotron-lora-smoke-training` are available in this environment run.
- `kaggle` CLI polling is historically blocked in this environment (WinError 10013), so this automation run did not fetch live kernel status.

Leaderboard snapshot (coarse context only):
- A local snapshot exists at `D:\CodexProjects\kaggle_status_check\nvidia-nemotron-model-reasoning-challenge.zip`.
- Use snapshot scores only as context; do not submit without validating a local `submission.zip` artifact.

## Local artifact validation (2026-05-15)

Validator smoke check:
- `outputs/_validator_smoke/submission_smoke.zip` is a **dummy structural** zip (weights are 5 bytes) and is only useful to confirm archive layout.
  - With the current validator defaults, it should **fail** the size gate (see below).
  - To validate structure only, run: `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0`.
  - `adapter_config.json` present
  - LoRA rank `r=32`
  - `adapter_model.safetensors` present
- This is **not** a trained adapter from Kaggle.

Public leaderboard snapshot note:
- Snapshot CSV `...publicleaderboard-2026-05-12T14_02_37.csv` records:
  - Team `guozhaojie` score `0.54`, submission count `1`, last submission `2026-05-09 18:18:59` (from local snapshot only).

## Required artifact checklist (before any submission)

For `submission.zip`:
- Contains `adapter_config.json`
- Contains adapter weights (typically `adapter_model.safetensors` or `adapter_model.bin`)
- LoRA rank `<= 32`

Validator:
- `python -B scripts/validate_lora_submission.py path\\to\\submission.zip`
  - Default behavior includes a small safety gate: adapter weight file(s) must be at least `1024` bytes.
  - If you intentionally want *structure-only* validation (e.g., for a dummy smoke zip), pass `--min-weight-bytes 0`.

Recommended (preserve + hash):
- `python -B scripts/ingest_submission_zip.py path\\to\\submission.zip --name nemotron-lora-smoke-training-vXX`

## Next actions

1. Rehydrate this repo (re-clone / restore from backup).
2. Export the latest Kaggle kernel outputs for `nemotron-lora-smoke-training` (or download as dataset) and validate `submission.zip`.
3. Only after artifact validation, continue the official 30B LoRA smoke path: scale training + add held-out validation by task family.

## Automation status (2026-05-15 13:45 CST)

- Still no kernel-exported submission.zip present locally (only outputs/_validator_smoke/submission_smoke.zip).
- Structural validator re-run: `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK (rank 32; weights present).
- This recovered workspace remains non-actionable for training until the real repo working tree (notebooks/scripts) and kernel outputs are restored.

## Automation status (2026-05-16)

Local workspace state:
- Still only `outputs/_validator_smoke/submission_smoke.zip` is present (no real kernel-exported adapter artifact).
- `.git` remains incomplete (no `HEAD`), so the working tree cannot be restored offline here.

Kernel / logs:
- `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` fails in this environment with WinError 10013 (socket access blocked), so this run cannot pull status/logs/outputs.

Verification:
- Structure-only: `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0`.

## Automation status (2026-05-16 04:07 CST)

- No change: still no kernel-exported `submission.zip` present locally.
- Structure-only re-run: `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0`.

## Automation status (2026-05-16 05:58 CST)

Local workspace state:
- No change: still only `outputs/_validator_smoke/submission_smoke.zip` is present (no real kernel-exported adapter artifact).

Kernel / logs:
- `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` still fails in this environment (WinError 10013 socket access denied), so this run cannot pull status/logs/outputs.

Verification:
- Structure-only: `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0`.


## Automation status (2026-05-16 08:02 CST)

- Preserved validator smoke artifact under outputs/kaggle/submissions/validator-smoke-20260516/ (sha256 ECE613FD5BD59C44B67FE88018763DBF3BAECBD978D71C5FDEB548CCF19D0906). This is still **NOT** a trained adapter.
- Still missing real kernel-produced submission.zip from guozhaojie/nemotron-lora-smoke-training; Kaggle API access remains blocked here (WinError 10013 historically).

## Automation status (2026-05-16 09:00 CST)

- Verified both local smoke artifacts are structurally valid (rank `32`, `adapter_config.json`, weights present), but **they are dummy (5B) and will fail the default size gate**:
  - `outputs/_validator_smoke/submission_smoke.zip`
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`
- Structure-only validation command used: `python -B scripts/validate_lora_submission.py <zip> --min-weight-bytes 0`.
- Still no kernel-produced adapter artifact from `guozhaojie/nemotron-lora-smoke-training` is present locally; Kaggle API access remains blocked in this environment (WinError 10013), so this run cannot pull kernel status/logs/outputs.

## Automation status (2026-05-16 13:52 CST)

- No change: still no kernel-produced `submission.zip` present locally (only dummy structural smoke artifacts).
- Kaggle API polling remains blocked here (WinError 10013), so this run cannot fetch kernel status/logs/outputs.
- Structure-only verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK.
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK.

## Automation status (2026-05-16 15:11 CST)

- No change: still only dummy structural smoke artifacts are present; no kernel-produced adapter has been ingested under `outputs/`.
- Kaggle kernel status/log polling remains unavailable here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` fails with WinError 10013 (socket access blocked).
- Verification (structure-only; note these zips have 5B weights and will fail the default size gate):
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK.
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK.

## Automation status (2026-05-16 22:21 CST)

- No change: still no kernel-produced `submission.zip` ingested locally (only dummy 5B-weight smoke artifacts).
- Kaggle CLI is present (`kaggle` 2.1.1) but API access remains blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked).
- Verification (demonstrate size gate behavior):
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK (structure-only).
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip` => fails size gate as expected (exit 2).

## Automation status (2026-05-16 23:23 CST)

- No change: still no kernel-produced `submission.zip` present locally (only dummy 5B-weight smoke artifacts).
- Kaggle API access remains blocked in this environment (WinError 10013), so this run cannot pull kernel status/logs/outputs.
- Verification (structure-only; gate disabled):
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK (rank 32; weights 5B).

## Automation status (2026-05-17 00:24 CST)

- No change: still no kernel-produced submission.zip present locally (only dummy 5B-weight smoke artifacts under outputs/_validator_smoke/ and outputs/kaggle/submissions/validator-smoke-20260516/).
- Environment limitation unchanged: kaggle CLI/API polling is blocked here (WinError 10013 historically), so this run cannot fetch kernel status/logs/outputs.
- Verification:
  - python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0 => OK (structure-only).
  - python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip => fails default size gate (expected; weights are 5B).

Next action:
- Export/download the real kernel-produced submission.zip in a network-enabled environment, then ingest here with:
  - python -B scripts/ingest_submission_zip.py <zip> --name nemotron-lora-smoke-training-vXX (keep default min weight size gate enabled).

## Automation status (2026-05-17 08:20 CST)

- No change: still no kernel-produced `submission.zip` present locally (only dummy 5B-weight smoke artifacts).
- Environment limitation unchanged: Kaggle CLI/API polling is blocked here (WinError 10013 historically), so this run cannot fetch kernel status/logs/outputs.
- Verification:
  - `python -B scripts/validate_lora_submission.py outputs/_validator_smoke/submission_smoke.zip --min-weight-bytes 0` => OK (structure-only).

## Automation status (2026-05-17 10:24 CST)

- Kaggle CLI/API polling still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access denied).
- Local artifacts unchanged: still only dummy structural smoke zips are present; no kernel-produced adapter has been ingested:
  - `outputs/_validator_smoke/submission_smoke.zip` (weights are 5B)
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` (weights are 5B)
- Verification:
  - Structure-only: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK.
  - Default size gate: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => expected fail (min 1024B).

## Automation status (2026-05-17 11:24 CST)

- Kaggle CLI/API polling still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access denied).
- Local artifacts unchanged: still only dummy structural smoke zips are present; no kernel-produced adapter has been ingested:
  - `outputs/_validator_smoke/submission_smoke.zip` (weights are 5B)
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` (weights are 5B)
- Verification:
  - Structure-only: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK.
  - Default size gate: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => expected fail (min 1024B).

## Automation status (2026-05-17 12:46 CST)

- Kaggle API polling still blocked here:
  - kaggle kernels status guozhaojie/nemotron-lora-smoke-training => WinError 10013 (socket access denied).
- Latest local artifact remains only the dummy structural smoke adapter:
  - outputs/kaggle/submissions/validator-smoke-20260516/submission.zip.
- Verification re-run:
  - Structure-only: python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0 => OK (rank 32; weights present).
  - Default size gate: python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip => expected fail (weights 5B < 1024B).

Next unblocker:
- Export/download the real kernel-produced submission.zip in a network-enabled environment, then ingest+validate locally:
  - python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX.


## Automation status (2026-05-17 13:47 CST)

- Kaggle API polling still blocked in this environment:
  - kaggle kernels status guozhaojie/nemotron-lora-smoke-training => WinError 10013 (socket access denied).
- Local artifacts unchanged: still only dummy structural smoke zips are present; no real kernel-produced adapter has been ingested.
- Verification:
  - Structure-only: python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0 => OK (rank 32; weights 5B).
  - Default size gate: python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip => expected fail (min 1024B).

Next unblocker:
- Export/download the real kernel-produced submission.zip in a network-enabled environment, then ingest+validate locally:
  - python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX

## Automation status (2026-05-17 14:47 CST)

- No change: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke artifacts).
- Kaggle CLI/API polling/download remains blocked in this environment (`WinError 10013`), so this run cannot fetch `guozhaojie/nemotron-lora-smoke-training` status/logs/outputs.
- Validator evidence (2026-05-17): structure-only passes, default size gate fails as expected:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; weights present)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights are 5B < 1024B)
- Repo note: `.git` metadata is incomplete here (`.git/HEAD` and `.git/config` missing), so `git status/log` is unavailable; treat this as a workspace snapshot rather than a clean repo.

Next unblocker:
- From a network-enabled machine/session, download the kernel output adapter zip, then ingest here with:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX`

## Automation status (2026-05-17 16:48 CST)

- Kaggle CLI/API polling still blocked in this environment (WinError 10013), so this run cannot fetch `guozhaojie/nemotron-lora-smoke-training` status/logs/outputs:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access denied / cannot connect).
- Local artifacts unchanged; still only dummy structural smoke zips are present; no real kernel-produced adapter has been ingested:
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` (sha256 `ECE613FD5BD59C44B67FE88018763DBF3BAECBD978D71C5FDEB548CCF19D0906`; weights 5B)
  - `outputs/_validator_smoke/submission_smoke.zip` (weights 5B)
- Verification:
  - Structure-only: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; weights present)
  - Default size gate: `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => expected FAIL (weights 5B < 1024B)

Next unblocker:
- From a network-enabled machine/session, download/export the Kaggle kernel output `submission.zip`, then ingest here with:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX`

## Automation status (2026-05-17 20:28 CST)

- Kaggle API access still blocked in this environment (WinError 10013), so this run cannot fetch `guozhaojie/nemotron-lora-smoke-training` status/logs/outputs:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(host='api.kaggle.com', port=443) ... [WinError 10013] ...`
- Local artifacts unchanged; still only dummy structural smoke zips are present; no real kernel-produced adapter has been ingested.
- Verification re-run (demonstrate size gate behavior on the preserved dummy artifact):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; weights present)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- Export/download the real kernel-produced `submission.zip` in a network-enabled environment, then ingest+validate locally:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX`

## Automation status (2026-05-17 21:35 CST)

- No change: still no kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke artifacts).
- Kaggle CLI/API polling remains blocked in this environment (WinError 10013 historically), so this run cannot fetch `guozhaojie/nemotron-lora-smoke-training` status/logs/outputs.
- Verification (2026-05-17 21:35 CST):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; weights 5B)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- From a network-enabled environment, export/download the real kernel output `submission.zip` and ingest it locally:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-vXX`

### Follow-up at 2026-05-18 (local-only)

- `kaggle kernels push -p .` on the v36 wrapper still fails with `Maximum batch GPU session count of 2 reached`.
- Current live Nemotron session still reports `KernelWorkerStatus.RUNNING` for `guozhaojie/nemotron-rule-distill-v35`.
- `kaggle kernels logs guozhaojie/nemotron-rule-distill-v35` returned no fresh log content, and a follow-up status check 8s later still showed RUNNING.
- Conclusion: the pending v35 session must finish or be stopped before v36 can be pushed.

## Automation status (2026-05-18 09:23 CST)

- Kaggle CLI/API access is still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked), so this run cannot fetch live status/logs/outputs.
- Kernel source is now present locally (pulled snapshot):
  - `pulled_kernels/nemotron-lora-smoke-training/nemotron-lora-smoke-training.ipynb` (v24; writes a root-level `/kaggle/working/submission.zip`).
- Added a push-ready wrapper directory for the official LoRA smoke kernel:
  - `kaggle_kernel_v24_lora_smoke_training/` (`kernel-metadata.json` + `notebook.ipynb`)
- Local artifacts unchanged: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke zips).

Next unblocker:
- From a network-enabled environment, push/run the kernel and download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-18 10:22 CST)

- Kaggle CLI/API polling is still blocked here (`kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013), so no live status/logs/outputs could be fetched in this run.
- Local artifacts remain unchanged:
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` (dummy 5B-weight adapter; rank 32; structure OK)
  - `outputs/_validator_smoke/submission_smoke.zip` (dummy 5B-weight adapter; structure OK)
- The push-ready wrapper remains staged locally:
  - `kaggle_kernel_v24_lora_smoke_training/` (`kernel-metadata.json` + `notebook.ipynb`)
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B, expected)
- Next unblocker: from a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it locally with `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`.

## Automation status (2026-05-18 23:01 CST)

- Kaggle CLI/API polling is still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked).
- Local artifacts unchanged: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke zips).
- Re-confirmed the push-ready wrapper is intact and matches the pulled kernel snapshot:
  - `kaggle_kernel_v24_lora_smoke_training/kernel-metadata.json`
  - `kaggle_kernel_v24_lora_smoke_training/notebook.ipynb` (writes `/kaggle/working/submission.zip`).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-20 11:31 CST)

- Kaggle CLI/API polling is still blocked here, so this run cannot fetch live kernel status/logs/outputs for `guozhaojie/nemotron-lora-smoke-training`.
- New local artifact found (already on disk): `outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip`.
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; `adapter_config.json` present; weights present; `adapter_model.safetensors` is ~3.54GB).
- Validation-format/accuracy gate (local-only) is still far from submit-ready:
  - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log --out outputs/kaggle/nemotron-rule-distill-v35-v3/summary.json --json`
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/summary.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).
- Narrow code fix applied (prep for next kernel run): patched `FORMAT_INSTRUCTION` in these notebooks to remove the misleading `\\boxed{ANSWER}` placeholder and require `\\boxed{<final_answer>}`:
  - `kaggle_kernel_v24_lora_smoke_training/notebook.ipynb`
  - `kaggle_kernel_v36_think_close_box/notebook.ipynb`
  - `kaggle_kernel_v37_think_close_box/notebook.ipynb`
  - `kaggle_kernel_v36_push_on_v35/nemotron-rule-distill-v35.ipynb`

Next action:
- From a network-enabled environment, push/run the updated kernel(s), then download logs + outputs and re-run `scripts/summarize_kaggle_kernel_log.py` + `scripts/submission_gate.py` before any leaderboard submission.

## Automation status (2026-05-20 12:26 CST)

- Kaggle CLI/API polling remains blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Re-verified the on-disk adapter artifact and summary gate (no change):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`).
  - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log --out outputs/kaggle/nemotron-rule-distill-v35-v3/summary.json --json`
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/summary.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).

## Automation status (2026-05-20 09:24 CST)

- Kaggle CLI/API polling remains blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- New local artifact present (not from `nemotron-lora-smoke-training`, but still a real LoRA adapter zip):
  - `outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip`
- Verification:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; `adapter_model.safetensors` present; ~3.5GB).
  - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log --out outputs/kaggle/nemotron-rule-distill-v35-v3/validation_summary.json` => wrote UTF-8 JSON summary (avoid PowerShell `>` UTF-16).
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/validation_summary.json` => `BLOCK` (`fixed_correct=9`, `strict_single_boxed=9`).
- Decision: do not submit this adapter yet; pass the format/accuracy gate first.

Next unblocker:
- Improve strict `\\boxed{...}` compliance + correctness, then re-run summarize + gate on the new kernel log.

## Automation status (2026-05-20 10:26 CST)

- Kaggle CLI/API polling still blocked here (WinError 10013), so no live kernel status/log pull was possible.
- Fixed a local workflow blocker: PowerShell output redirection (`>`) writes UTF-16 by default, which previously caused `scripts/submission_gate.py` to crash on `validation_summary.json`.
  - `scripts/summarize_kaggle_kernel_log.py` now supports `--out <path>` to write UTF-8 JSON directly.
  - `scripts/submission_gate.py` now accepts UTF-8 / UTF-8-BOM / UTF-16LE / UTF-16BE JSON.
- Rebuilt summary (with correct family breakdown key mapping from the notebook’s `by_family`):
  - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log --out outputs/kaggle/nemotron-rule-distill-v35-v3/validation_summary.json`
  - Result highlights: only `numeral_system` shows any signal (fixed_correct=9/24); other families are 0/24.
- Gate re-run: still `BLOCK` (fixed_correct=9, strict_single_boxed=9).

Next unblocker:
- Update the next Kaggle notebook run to enforce a single final `\\boxed{...}` line and broaden training/validation coverage beyond `numeral_system`, then re-run `summarize_kaggle_kernel_log.py` + `submission_gate.py`.

## Automation status (2026-05-20 14:32 CST)

- Local-only (no Kaggle API): `kaggle kernels status/logs/output ...` remains blocked here (WinError 10013), so this run could not pull live `guozhaojie/nemotron-lora-smoke-training` outputs.
- Implemented a narrowly-scoped notebook fix to reduce format drift in future runs:
  - `kaggle_kernel_v36_push_on_v35/nemotron-rule-distill-v35.ipynb`: training target canonicalization no longer prefixes `</think>\n` before the boxed answer (now trains `\\boxed{...}` only).
- No new adapter artifact was produced in this environment; re-run the kernel in a network-enabled environment, then re-ingest + re-run `scripts/summarize_kaggle_kernel_log.py` and `scripts/submission_gate.py`.

## Automation status (2026-05-20 08:25 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Local artifacts unchanged: still only the dummy structural smoke adapter exists:
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank `32`; structure OK).

Next unblocker:
- From a network-enabled environment, push/run the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `kaggle kernels push -p kaggle_kernel_v24_lora_smoke_training`
  - `kaggle kernels output guozhaojie/nemotron-lora-smoke-training -p .\\_kaggle_downloads\\nemotron-lora-smoke-training-v24 --force`
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`
  - Or run: `powershell -ExecutionPolicy Bypass -File scripts/pull_kaggle_kernel_output_and_ingest.ps1`

## Automation status (2026-05-19 22:56 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `[WinError 10013]` (socket access blocked).
- Local artifacts unchanged: still only dummy structural smoke adapter exists:
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank `32`; structure OK).

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 12:16 CST)

- Kaggle CLI/API polling is still blocked here (WinError 10013), so this run still cannot fetch live kernel status/logs/outputs for `guozhaojie/nemotron-lora-smoke-training`.
- Local artifacts unchanged: only the dummy validator smoke zip exists under `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`.
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; structure OK)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => exit code `2` (weights 5B < 1024B; expected dummy)
- Packaging logic sanity-check (pulled v24 notebook): `pulled_kernels/nemotron-lora-smoke-training/nemotron-lora-smoke-training.ipynb` uses `LoraConfig(r=LORA_RANK)` and writes `/kaggle/working/submission.zip` with `adapter_config.json` + `adapter_model.*` assertions.

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 10:14 CST)

- Kaggle CLI/API polling remains blocked here, so this run still cannot fetch live kernel status/logs/outputs:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Local artifacts unchanged: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke zips).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 08:10 CST)

- Kaggle CLI/API polling remains blocked here, so this run still cannot fetch live kernel status/logs/outputs:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked).
- Local artifacts unchanged: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke zips).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 00:00 CST)

- Kaggle CLI/API polling remains blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked), so this run cannot fetch live status/logs/outputs.
- Local artifacts unchanged: still no real kernel-produced `submission.zip` ingested under `outputs/` (only dummy 5B-weight smoke zips).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => FAIL (weights 5B < 1024B; expected)

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 11:20 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked).
- Local artifacts still unchanged: no kernel-produced adapter ingested (only dummy 5B-weight smoke zips).
- Verification (default size gate) still fails as expected for the dummy artifact:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => exit code `2` (weights 5B < 1024B).

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 14:21 CST)

- Kaggle CLI/API polling remains blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => WinError 10013 (socket access blocked).
- Local artifacts unchanged:
  - Only the dummy structural smoke adapters exist (5B weight file), so the default validator gate still rejects them.
- Wrapper sanity check (local-only):
  - `kaggle_kernel_v24_lora_smoke_training/kernel-metadata.json` targets `guozhaojie/nemotron-lora-smoke-training`, GPU enabled, internet disabled, and uses the Nemotron 30B model source + offline packages dataset.

Next unblocker:
- From a network-enabled environment, push/run the wrapper, then download `/kaggle/working/submission.zip` and ingest it here:
  - `kaggle kernels push -p kaggle_kernel_v24_lora_smoke_training`
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training`
  - `kaggle kernels logs guozhaojie/nemotron-lora-smoke-training`
  - `kaggle kernels output guozhaojie/nemotron-lora-smoke-training -p .\\_kaggle_downloads\\nemotron-lora-smoke-training-v24 --force`
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 15:23 CST)

- Kaggle CLI/API polling still blocked here (WinError 10013), so this run cannot fetch live kernel status/logs/outputs for `guozhaojie/nemotron-lora-smoke-training`.
- Local artifacts unchanged: only the dummy 5B-weight structural smoke zip exists under `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`.
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; structure OK)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => exit code `2` (weights 5B < 1024B; expected dummy)
- Wrapper sanity check (local-only): `kaggle_kernel_v24_lora_smoke_training/kernel-metadata.json` remains configured for GPU + no internet and points to `notebook.ipynb` (v24).

Next unblocker:
- From a network-enabled environment, push/run the wrapper, download `/kaggle/working/submission.zip`, then ingest it here:
  - `kaggle kernels push -p kaggle_kernel_v24_lora_smoke_training`
  - `kaggle kernels output guozhaojie/nemotron-lora-smoke-training -p .\\_kaggle_downloads\\nemotron-lora-smoke-training-v24 --force`
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-19 19:51 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Local artifacts unchanged: no kernel-produced adapter ingested (only dummy 5B-weight smoke zips).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; structure OK)

Next unblocker:
- From a network-enabled environment, push/run the wrapper, download `/kaggle/working/submission.zip`, then ingest it here:
  - `kaggle kernels push -p kaggle_kernel_v24_lora_smoke_training`
  - `kaggle kernels output guozhaojie/nemotron-lora-smoke-training -p .\\_kaggle_downloads\\nemotron-lora-smoke-training-v24 --force`
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

### Follow-up at 2026-05-19 (local-only)

- Confirmed `guozhaojie/nemotron-rule-distill-v35` previous run is `KernelWorkerStatus.COMPLETE`.
- Pushed the v36 think-close-box code via the v35 track wrapper: `Kernel version 3 successfully pushed`.
- Current run status is now `KernelWorkerStatus.RUNNING`.
- Immediate log fetch is still empty (expected during early startup).
- Next checkpoint: pull logs again after warm-up and capture the first concrete training/runtime lines before deciding whether to wait for completion or intervene.

## Automation status (2026-05-19 20:54 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Local artifacts unchanged: still no kernel-produced adapter ingested (only dummy 5B-weight smoke zips).
- Verification re-run:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank 32; structure OK)
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => exit code `2` (weights 5B < 1024B; expected dummy)

## Automation status (2026-05-19 22:00 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Local artifacts unchanged: still only dummy structural smoke adapter exists:
  - `outputs/kaggle/submissions/validator-smoke-20260516/submission.zip`
- Verification:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip --min-weight-bytes 0` => OK (rank `32`; structure OK).
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => exit code `2` (weights 5B < 1024B; expected dummy).

Next unblocker:
- From a network-enabled environment, run/push the v24 kernel, download the produced `submission.zip`, then ingest it here:
  - `python -B scripts/ingest_submission_zip.py <path-to-submission.zip> --name nemotron-lora-smoke-training-v24`

## Automation status (2026-05-20 13:25 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- New local non-dummy adapter artifact exists (from local distill run, not the official smoke kernel):
  - `outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip`
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; `adapter_model.safetensors` size `3537299144` bytes).
- Preserved ingested copy + manifest:
  - `outputs/kaggle/submissions/nemotron-rule-distill-v35-v3/submission.zip`
  - `outputs/kaggle/submissions/nemotron-rule-distill-v35-v3/manifest.json` (sha256 `CC0E32DFD95F5D84EA896AE3CF03F7FF90D5D05CDC766886FC7251B353796697`).

Next action:
- Keep treating `guozhaojie/nemotron-lora-smoke-training` as "unknown status" in this environment (no API access). Use the validated local adapter zip to continue building family-balanced training/validation runs before spending any leaderboard submission.

## Automation status (2026-05-20 21:58 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Re-verified local adapter artifact:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; weights `adapter_model.safetensors` size `3537299144` bytes).
- Gate re-run:
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/validation_summary_recomputed.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).

Next action:
- Do not submit this adapter; next iteration should lift strict boxed-format compliance + family-balanced correctness, then re-run `summarize_kaggle_kernel_log.py` + `submission_gate.py` on a new artifact from a network-enabled environment.

## Automation status (2026-05-20 22:54 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `HTTPSConnectionPool(... [WinError 10013] ...)` (socket access blocked).
- Verification re-run (unchanged):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/validation_summary_recomputed.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).
- Prepared next controlled kernel change (to improve strict boxed-format compliance):
  - Patched `assistant_text()` in these notebooks to emit only `\\boxed{answer}` (removed hint + `Final answer:` prefix):
    - `kaggle_kernel_v36_think_close_box/notebook.ipynb`
    - `kaggle_kernel_v37_think_close_box/notebook.ipynb`
    - `kaggle_kernel_v36_push_on_v35/nemotron-rule-distill-v35.ipynb`

Next action:
- Push/run the patched kernel in a network-enabled environment, download the new `submission.zip`, ingest it here, then re-run `summarize_kaggle_kernel_log.py` + `submission_gate.py` before any leaderboard submission.

## Automation status (2026-05-20 23:57 CST)

- Kaggle CLI/API polling still blocked here:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `[WinError 10013]` (socket access blocked).
- Local-only verification re-run (unchanged):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; `adapter_model.safetensors` ~3.54GB).
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/log_summary.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).
- Family breakdown (from `outputs/kaggle/nemotron-rule-distill-v35-v3/log_summary.json`): only `numeral_system` has any `fixed_correct`; all other families are `0`, so this artifact is not family-balanced and should not be submitted.

Next action:
- Use a network-enabled environment to run a kernel that produces a new artifact, then ingest and gate it here; do not spend a submission until the family gate clears.

## Automation status (2026-05-21 01:02 CST)

- Kaggle CLI/API polling still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `[WinError 10013]` (socket access blocked).
- Local-only verification re-run (unchanged):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; `adapter_model.safetensors` size `3537299144` bytes).
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/log_summary.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).
- Smoke kernel adapter remains unconfirmed here:
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/validator-smoke-20260516/submission.zip` => still fails default size gate (dummy 5B weights).

Next action:
- Run the patched kernel (v36/v37 think-close-box, or the official v24 smoke wrapper) in a network-enabled environment, download the produced `submission.zip`, then ingest+gate it here before any leaderboard submission.

## Automation status (2026-05-21 02:08 CST)

- Kaggle CLI/API polling still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `[WinError 10013]` (socket access blocked).
- Local artifact integrity check (unchanged):
  - `outputs/kaggle/submissions/nemotron-rule-distill-v35-v3/submission.zip` contains `adapter_config.json` with `base_model_name_or_path=/kaggle/input/models/metric/nemotron-3-nano-30b-a3b-bf16/transformers/default/1`.
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/submissions/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; weights present).
- Log-derived validation summary confirmed from `outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log`:
  - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v35-v3/nemotron-rule-distill-v35.log` => `fixed_correct=9/144`, `strict_single_boxed=9/144` (only `numeral_system` has any signal).

Next action:
- Do not submit; the next run must lift strict boxed-format compliance and correctness across families before spending any leaderboard submission.

## Automation status (2026-05-21 04:49 CST)

- Kaggle CLI/API polling still blocked in this environment:
  - `kaggle kernels status guozhaojie/nemotron-lora-smoke-training` => `[WinError 10013]` (socket access blocked).
- No local kernel-produced outputs for `guozhaojie/nemotron-lora-smoke-training` were found (still only the pulled notebook snapshot under `pulled_kernels/`).
- Local-only verification re-run (unchanged):
  - `python -B scripts/validate_lora_submission.py outputs/kaggle/nemotron-rule-distill-v35-v3/submission.zip` => OK (rank `32`; weights present).
  - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v35-v3/log_summary_recomputed2.json` => `BLOCK` (`fixed_correct=9/144`, `strict_single_boxed=9/144`).

Next action:
- In a network-enabled environment, run the official v24 LoRA-smoke kernel (or the patched v36/v37 think-close-box), download the produced `submission.zip`, ingest it here, then re-run `summarize_kaggle_kernel_log.py` + `submission_gate.py` before any leaderboard submission.

## v37 smoke startup check (2026-05-25)

- Deleted stuck `guozhaojie/nemotron-rule-distill-v31` after it remained `RUNNING` overnight with empty logs and stale 2026-05-11 outputs.
- Prepared short startup run in `kaggle_kernel_v37_smoke_push_on_lora/` using the existing `guozhaojie/nemotron-lora-smoke-training` kernel track.
- Smoke settings: `RUN_LABEL = "v37-smoke-10steps-startup-check"`, `SUBSAMPLE_SIZE = 720`, `MAX_STEPS = 10`, `GEN_MAX_NEW_TOKENS = 96`, per-family cap `144`.
- Push result: `Kernel version 25 successfully pushed`; current status is `KernelWorkerStatus.RUNNING`.
- Immediate logs are still empty and files still show stale 2026-05-09 outputs, which is acceptable only during early startup; if this persists for hours, treat it as another Kaggle scheduler/session issue rather than a model result.
- Result: v25 completed. It confirmed the Kaggle 30B training chain is live, but validation was weak: `fixed_correct=1/144`, `strict_single_boxed=0/144`.
- Diagnosis: prompt wording included the literal placeholder `\\boxed{ANSWER}`; logs showed at least one prediction of the literal string `ANSWER`.
- Decision: do not download/submit the large v25 adapter; use it only as a startup smoke success.

## v38 format-fix medium run (2026-05-25)

- Prepared `kaggle_kernel_v38_formatfix_push_on_lora/` on the working `guozhaojie/nemotron-lora-smoke-training` track.
- Changes from v25:
  - `RUN_LABEL = "v38-formatfix-medium-60steps"`.
  - `MAX_STEPS = 60`, `SUBSAMPLE_SIZE = 1200`, per-family cap `240`.
  - `GEN_MAX_NEW_TOKENS = 192`.
  - Validation split reduced to `4` examples per family for faster feedback.
  - Removed the literal `ANSWER` placeholder from the user instruction.
- Push result: `Kernel version 26 successfully pushed`; current status is `KernelWorkerStatus.RUNNING`.

## Bronze sprint plan (2026-05-24)

- Leaderboard snapshot: `guozhaojie` is rank `2901/3418` with public score `0.54`; approximate bronze/top-10% boundary is rank `342`, score about `0.86`.
- Prize reality check: final leaderboard prizes require top 3; Open Contribution Awards require top 10%, so the practical near-term goal is bronze/top-10%.
- Prepared `kaggle_kernel_v37_think_close_box/notebook.ipynb` as `RUN_LABEL = "v37-bronze-family-method-longval"`.
- Strategy changes:
  - Restore concise family method supervision instead of answer-only SFT.
  - Keep the final line strictly boxed.
  - Upweight all non-`numeral_system` families to reduce single-family collapse.
  - Increase local validation generation budget from `224` to `768` tokens to better approximate the official long-generation metric.
- Submission policy: do not submit unless the validation gate beats the current local floor and shows cross-family correctness, not just `numeral_system`.
- Push result: direct creation of `guozhaojie/nemotron-think-close-box-v37` hit the recurring Kaggle CLI `Notebook not found` issue.
- Workaround: copied the same v37 notebook into the known-good wrapper `kaggle_kernel_v36_push_on_v35/` and pushed through `guozhaojie/nemotron-rule-distill-v35`.
- Kaggle result: `Kernel version 4 successfully pushed`; current status is `KernelWorkerStatus.RUNNING`.
- Follow-up: the v35-track run stayed `RUNNING` for hours with empty logs and stale 2026-05-19 outputs, so it was treated as a stuck Kaggle session and deleted via `kaggle kernels delete -y guozhaojie/nemotron-rule-distill-v35`.
- Direct new slug `guozhaojie/nemotron-bronze-v37` still hit the recurring `Notebook not found` creation error.
- Current active run: copied the same v37 notebook into `kaggle_kernel_v37_push_on_v31/` and pushed through existing kernel `guozhaojie/nemotron-rule-distill-v31`.
- Kaggle result: `Kernel version 2 successfully pushed`; current status is `KernelWorkerStatus.RUNNING`.

## v38 result and v39 answer-only calibration (2026-05-25)

- Pulled v38 logs from `guozhaojie/nemotron-lora-smoke-training` version 26 into `outputs/kaggle/nemotron-lora-smoke-training-v26/`.
- v38 completed and created `/kaggle/working/submission.zip` (~2918 MB), but validation gate blocks it:
  - `run_label`: `v38-formatfix-medium-60steps`
  - `total`: 24
  - `fixed_boxed`: 10
  - `fixed_final_box_line`: 0
  - `strict_single_boxed`: 0
  - `fixed_correct`: 2
- Diagnosis: generations still spend most of the short validation budget repeating/negotiating the format instruction instead of producing the final boxed answer.
- Decision: do not download or submit the v38 adapter.
- Prepared and pushed `kaggle_kernel_v39_answeronly_push_on_lora/` to the known-good kernel track `guozhaojie/nemotron-lora-smoke-training`.
- v39 changes:
  - `RUN_LABEL = "v39-answeronly-format-calibration-80steps"`.
  - `SUBSAMPLE_SIZE = 1600`, `MAX_STEPS = 80`.
  - `FORMAT_INSTRUCTION = "Return only one line: \\boxed{<final_answer>}. Do not explain. Do not repeat these instructions."`
  - Training assistant targets canonicalized to exactly one boxed line (`\\boxed{answer}`), removing method hints from supervision.
  - `GEN_MAX_NEW_TOKENS = 64` for fast validation of format compliance.
- Push result: `Kernel version 27 successfully pushed`; status immediately after push: `KernelWorkerStatus.RUNNING` with empty early logs and stale v38 output files.
- Next checkpoint: poll logs until `run_label v39-answeronly-format-calibration-80steps` appears; if complete, summarize with `summarize_kaggle_kernel_log.py` and gate before downloading the large adapter.

## v40 bronze corpus pipeline prep (2026-05-25)

- Shifted strategy from prompt-only notebook patching to a corpus-SFT pipeline inspired by the public Progress Prize reference `external/tonghuikang-nemotron`.
- Added `docs/BRONZE_SPRINT_PLAN.md` with phase gates for data audit, reasoning corpus, synthetic augmentation, v40 smoke, and v41 bronze candidate.
- Added `scripts/audit_nemotron_corpus.py` and generated:
  - `outputs/audits/nemotron_corpus_audit.json`
  - `outputs/audits/nemotron_corpus_audit.md`
- Audit result from the public reference corpus:
  - train rows: 9500
  - reference corpus rows: 17963
  - total unmasked tokens: 40871870
  - strong rule-found categories: cipher/gravity/numeral/unit_conversion at 100%, bit_manipulation at ~85%.
- Added `scripts/build_bronze_corpus.py` to create simple JSONL SFT corpora from high-confidence reference reasoning traces.
- Fixed an important numeric-label issue: gravity/unit reference reasoning often ends in 3-decimal intermediate boxed values; generated corpus now forces the final boxed answer to use the official `train.csv` answer while accepting numeric traces by tolerance.
- Generated local corpora:
  - `outputs/bronze_corpus/v40_tiny_corpus.jsonl`: 379 rows, format checked (`bad=0`).
  - `outputs/bronze_corpus/v40_smoke_corpus.jsonl`: 1883 rows, main categories capped at 300 rows.
- Prepared Kaggle notebooks:
  - `kaggle_kernel_v40_corpus_sft_smoke/`: 1883-row embedded corpus, 160 steps, notebook ~3.2 MB.
  - `kaggle_kernel_v40_corpus_sft_tiny_newslug/`: 379-row embedded corpus, 80 steps, notebook ~605 KB, new slug `guozhaojie/nemotron-corpus-sft-v40-tiny`.
- Kaggle push observations:
  - Pushing v40 smoke to the existing `nemotron-lora-smoke-training` track returned `400 Bad Request`, likely because the latest v39 run is still `RUNNING`.
  - Pushing v40 tiny new slug was accepted up to scheduling, then blocked by `Maximum batch GPU session count of 2 reached`.
- Current blocker: Kaggle GPU batch slots are occupied. `guozhaojie/nemotron-lora-smoke-training` remains `KernelWorkerStatus.RUNNING` with empty logs/stale v38 output files. Need free one GPU batch slot before v40 tiny can run.

Next action:
- Free a stuck GPU session, then push/run `kaggle_kernel_v40_corpus_sft_tiny_newslug/` first. If it starts and emits `run_label v40-corpus-sft-tiny-newslug-80steps`, use it to validate the corpus-SFT path before attempting the larger v40 smoke.

## v40 tiny rerun syntax fix (2026-05-25)

- First v40 tiny run on `guozhaojie/nemotron-rule-distill-v30` reached Kaggle GPU/model setup and printed `data_summary` for 379 rows, proving the embedded corpus loads.
- It failed before training with `SyntaxError: unterminated f-string literal` in cell 6 fallback chat-template code.
- Fixed cell 6 in both v40 tiny and v40 smoke notebooks by replacing the multiline fallback f-string with explicit string concatenation.
- Local AST syntax check passed for cells 5, 6, and 9.
- Pushed fixed v40 tiny to `guozhaojie/nemotron-rule-distill-v30` as kernel version 3; status is `KernelWorkerStatus.RUNNING`.

## v40 compact result and v41 short-target candidate (2026-05-26 CST)

- v40 compact run on `guozhaojie/nemotron-rule-distill-v30` completed as kernel version 4 with run label `v40-compact-corpus-tiny-r16-40steps`.
- Validation summary from `outputs/kaggle/nemotron-rule-distill-v30-v4-summary.json`:
  - `total=61`
  - `fixed_correct=8`
  - `strict_single_boxed=8`
  - all fixed-correct cases are `numeral`; every other family remains 0 correct.
- Gate decision: `BLOCK`; do not submit or spend leaderboard quota on this adapter.
- Diagnosis: long/compact reasoning still teaches the model to keep reasoning; non-numeral generations often fail to emit a final boxed answer inside the validation budget.
- Prepared v41 candidate:
  - `outputs/bronze_corpus/v41_short_target_tiny_corpus.jsonl`
  - 566 rule-found rows, family-balanced where available, completion p90 about 127 chars.
  - completion format: one short family method line plus final `\boxed{answer}` line.
  - notebook: `kaggle_kernel_v41_short_target_tiny_v30/`
  - run label: `v41-short-target-tiny-r16-80steps`
  - settings: rank16, max sequence 1024, 80 steps, validation max-new-tokens 192.
- v41 goal: test whether short targets fix cross-family boxed emission before attempting a larger bronze candidate.

## v41/v42 quota-blocked execution queue (2026-05-26 CST)

Current blocker:
- `kaggle kernels push -p kaggle_kernel_v41_short_target_tiny_v30` failed with `Maximum weekly GPU quota of 30.00 hours reached.`
- This is a Kaggle GPU quota blocker, not a notebook syntax or corpus blocker.

Ready-to-run candidates:
1. v41 short-target tiny
   - notebook: `kaggle_kernel_v41_short_target_tiny_v30/`
   - push helper: `scripts/push_v41_when_quota_available.ps1`
   - run label: `v41-short-target-tiny-r16-80steps`
   - corpus: `outputs/bronze_corpus/v41_short_target_tiny_corpus.jsonl`
   - target format: short family method line, then final `\boxed{answer}`.
   - purpose: improve non-numeral cross-family correctness while still ending quickly.
2. v42 answer-only tiny
   - notebook: `kaggle_kernel_v42_answer_only_tiny_v30/`
   - push helper: `scripts/push_v42_when_quota_available.ps1`
   - run label: `v42-answer-only-tiny-r16-80steps`
   - corpus: `outputs/bronze_corpus/v42_answer_only_tiny_corpus.jsonl`
   - target format: exactly `\boxed{answer}`.
   - purpose: rescue strict single-boxed emission if v41 still talks too much.

Execution order when quota recovers:
1. Run v41 first because it preserves a minimal method token and has a better chance of improving correctness, not just format.
2. Pull logs and summarize before downloading any large adapter:
   - `kaggle kernels logs guozhaojie/nemotron-rule-distill-v30 > outputs/kaggle/nemotron-rule-distill-v30-v41-latest.log`
   - `python -B scripts/summarize_kaggle_kernel_log.py outputs/kaggle/nemotron-rule-distill-v30-v41-latest.log --json > outputs/kaggle/nemotron-rule-distill-v30-v41-summary.json`
   - `python -B scripts/submission_gate.py outputs/kaggle/nemotron-rule-distill-v30-v41-summary.json --min-fixed-correct 26 --min-strict-single-boxed 20`
3. Only run v42 if v41 improves correctness but still fails boxed/strict format, or if v41 remains long-form and non-numeral boxed rate stays near zero.

Do-not-submit rules:
- Do not submit any candidate with `fixed_correct < 26` on the current local validation summary.
- Do not submit if only `numeral` has non-zero correctness.
- Do not submit if `strict_single_boxed < 20`, unless the log shows official extraction would clearly accept the answers and we explicitly decide the gate is too conservative.
- Do not download a multi-GB adapter unless log-derived validation passes or the artifact is needed for structural debugging.

## v43 short-target medium queued (2026-05-26 CST)

- Kaggle quota check repeated after v41 preparation:
  - `kaggle kernels push -p kaggle_kernel_v41_short_target_tiny_v30` still fails with `Maximum weekly GPU quota of 30.00 hours reached.`
- Prepared a stronger queued candidate for after v41 direction is validated:
  - corpus: `outputs/bronze_corpus/v43_short_target_medium_corpus.jsonl`
  - rows: 1886
  - main families capped at 300 rows each; smaller rare families use all available rule-found rows.
  - completion p90 remains about 127 chars; `bad_final_boxed=0`.
  - notebook: `kaggle_kernel_v43_short_target_medium_v30/`
  - push helper: `scripts/push_v43_when_quota_available.ps1`
  - run label: `v43-short-target-medium-r16-160steps`
  - settings: rank16, max sequence 1024, 160 steps, validation max-new-tokens 192.
- Execution policy:
  - Run v41 first when quota recovers.
  - Run v43 only if v41 shows cross-family boxed/correctness improvement; otherwise use v42 to isolate strict format failure.
  - Do not submit v43 unless it clears the same local gate and has non-zero correctness outside `numeral`.

## v41/v42/v43 placeholder-risk fix (2026-05-26 CST)

- Before spending the next GPU run, removed placeholder-style prompt text from queued corpora:
  - v41 no longer says `\boxed{answer}` in the user prompt.
  - v42 no longer says `\boxed{final_answer}` in the user prompt.
- Reason: v25 previously copied a literal placeholder, so queued runs should not expose a placeholder token that can be copied instead of solving.
- Rebuilt corpora and re-embedded notebooks:
  - `v41-short-target-tiny-r16-80steps-noplaceholder`
  - `v42-answer-only-tiny-r16-80steps-noplaceholder`
  - `v43-short-target-medium-r16-160steps-noplaceholder`
- Local notebook syntax check passed for cells 5, 6, 8, and 9 in all three notebooks.
- Execution order remains v41 -> v42 if strict format fails -> v43 if v41 direction improves cross-family behavior.

## v40 failure mode log audit (2026-05-26 CST)

- Rechecked `outputs/kaggle/nemotron-rule-distill-v30-v4-latest.log` around `validation_generation_checks`.
- Non-`numeral` generations commonly start the right reasoning path but spend the full generation budget explaining/intermediate-solving and never reach the final boxed line.
- Examples observed in the log:
  - `unit_conversion`: identifies a stable multiplicative ratio such as about `1.805` or `1.483`, but continues calculating rather than finalizing.
  - `gravity`: correctly uses `d = 0.5 * g * t^2` and computes `g` from observations, but continues step-by-step and misses the final box.
  - `cipher` and `bit_manipulation`: starts constructing mappings/bit positions but remains verbose.
  - `numeral`: succeeds because the reasoning path is short enough to reach `</think>` and `\boxed{...}`.
- Interpretation: the next high-ROI run should reduce answer latency, not add more long reasoning. This supports the no-placeholder v41/v42/v43 queue:
  - v41 tests short method + boxed final line for cross-family correctness.
  - v42 is a serious strict-format rescue candidate, not just a toy, because it trains immediate boxed emission.
  - v43 should be used only after v41 shows that short-target SFT improves non-numeral behavior.

## Log extraction tooling added (2026-05-26 CST)

- Added `scripts/extract_validation_checks_from_kaggle_log.py` to reconstruct Kaggle streamed stdout JSON chunks and parse `validation_generation_checks`.
- Verified on v40 compact log:
  - output checks: `outputs/kaggle/nemotron-rule-distill-v30-v4-checks.json`
  - output summary: `outputs/kaggle/nemotron-rule-distill-v30-v4-checks-summary.json`
  - summary matches the existing v40 result: `total=61`, `fixed_correct=8`, `fixed_boxed=9`, `fixed_final_box_line=8`, only `numeral` correct.
- Updated `scripts/pull_v30_logs_and_gate.ps1` to pull logs, summarize, extract per-example checks, and run the gate in one command.

## v44 answer-only medium queued (2026-05-26 CST)

- Quota check repeated:
  - `guozhaojie/nemotron-rule-distill-v30` is still `COMPLETE`.
  - pushing v41 still fails with `Maximum weekly GPU quota of 30.00 hours reached.`
- Prepared v44 as the medium-sized answer-only follow-up to v42:
  - corpus: `outputs/bronze_corpus/v44_answer_only_medium_corpus.jsonl`
  - rows: 1886
  - main families capped at 300 rows each; rare categories use all available rule-found rows.
  - target format: exactly one boxed line, `bad_exact_boxed=0`.
  - notebook: `kaggle_kernel_v44_answer_only_medium_v30/`
  - push helper: `scripts/push_v44_when_quota_available.ps1`
  - run label: `v44-answer-only-medium-r16-160steps-noplaceholder`
  - settings: rank16, max sequence 1024, 160 steps, validation max-new-tokens 64.
- Execution policy:
  - Do not run v44 before v42; it is a scale-up only if answer-only improves strict-format validation.
  - If v42 is correct-poor despite strict boxed output, prefer v41/v43 short-target direction instead of v44.

## v45/v46 think-close queue added (2026-05-26 CST)

- Rechecked the validation/gate logic:
  - `extract_final_box()` discards everything before `</think>` and applies strict boxed checks only to the segment after `</think>`.
  - v41 short-target completions (`Method...\n\boxed{...}`) may improve answer latency but are not as directly aligned with this evaluator behavior.
- Prepared a stronger aligned variant:
  - v45 tiny corpus: `outputs/bronze_corpus/v45_think_close_tiny_corpus.jsonl`
  - v46 medium corpus: `outputs/bronze_corpus/v46_think_close_medium_corpus.jsonl`
  - target format: short method line, then `</think>`, then exactly one final `\boxed{answer}` line.
  - no placeholder answer strings in prompts.
  - both corpora have `bad_think_close_boxed=0`.
- Prepared notebooks and push helpers:
  - `kaggle_kernel_v45_think_close_tiny_v30/`, run label `v45-think-close-tiny-r16-80steps`, helper `scripts/push_v45_when_quota_available.ps1`.
  - `kaggle_kernel_v46_think_close_medium_v30/`, run label `v46-think-close-medium-r16-160steps`, helper `scripts/push_v46_when_quota_available.ps1`.
- Local syntax check passed for cells 5, 6, 8, and 9 in both notebooks.
- Revised execution priority when quota recovers:
  1. Run v45 first. It is the best current compromise: short method for correctness plus evaluator-aligned `</think>`/boxed format.
  2. If v45 improves cross-family correctness, run v46 medium.
  3. If v45 has correctness but strict format still fails unexpectedly, run v42 answer-only tiny.
  4. Keep v41/v43 as fallback short-target variants without explicit `</think>` only if v45 underperforms for reasons unrelated to format.

## v50A reference-tail masked SFT prepared (2026-05-29 CST)

Strategic pivot:
- We are moving from format-only variants toward a bronze-oriented approximation of the public Progress Prize pipeline.
- The public run used rank32, max length 8192, masked completion loss, batch64, 1 epoch, and about 6.5M unmasked tokens in the recorded `03-23-00-47` training config. That backend was Tinker, not Kaggle single-GPU, so exact reproduction is not feasible in our current Kaggle kernel path.

Prepared v50A:
- Corpus builder: `scripts/build_v50_reference_tail_corpus.py`.
- Corpus: `outputs/bronze_corpus/v50a_reference_tail_rulefound_corpus.jsonl`.
- Summary: `outputs/bronze_corpus/v50a_reference_tail_rulefound_corpus_summary.md`.
- Rows: 3623 rule-found reference reasoning-tail examples across official families.
- Completion p90: about 2233 chars.
- Format: reference reasoning tail, then `</think>`, then final `\boxed{official_answer}`.
- Notebook: `kaggle_kernel_v50a_reference_tail_masked_v30/`.
- Run label: `v50a-reference-tail-masked-r16-220steps`.
- Training change: custom tokenization and collator mask prompt labels to `-100`; only completion tokens contribute loss. This is closer to the reference corpus masking than prior SFTTrainer full-text runs.
- Settings: rank16, max sequence length 2048, 220 steps, LR `8e-5`, validation generation 768 tokens.
- Push helper: `scripts/push_v50a_when_quota_available.ps1`.

Revised execution priority when quota recovers:
1. Run v50A first if we are optimizing for bronze. It tests the closest feasible approximation of the known 0.85 route.
2. Run v45 only if v50A OOMs or fails before training, because v45 is a diagnostic format/latency run.
3. If v50A improves cross-family but remains undertrained, prepare v50B with either more steps or a dataset-mounted larger corpus rather than returning to prompt patching.
4. Do not submit unless local gate clears and correctness is not concentrated only in `numeral`.

## v50A dataset-mounted path fixed (2026-05-29 CST)

- Initial embedded v50A notebook (`kaggle_kernel_v50a_reference_tail_masked_v30/`) failed to push with `400 Bad Request`, likely due the large embedded base64 corpus payload.
- Created private Kaggle dataset:
  - dataset: `guozhaojie/nemotron-v50a-reference-tail-corpus`
  - local source dir: `kaggle_dataset_v50a_reference_tail_corpus/`
  - file: `v50a_reference_tail_rulefound_corpus.jsonl` (~9.7 MB)
  - Kaggle creation succeeded.
- Built dataset-mounted notebook:
  - notebook: `kaggle_kernel_v50a_reference_tail_dataset_v30/`
  - notebook size: ~23 KB
  - metadata dataset sources include `guozhaojie/nemotron-v50a-reference-tail-corpus` and offline packages.
  - run label: `v50a-reference-tail-dataset-masked-r16-220steps`
  - push helper: `scripts/push_v50a_dataset_when_quota_available.ps1`
- Push result for dataset-mounted notebook:
  - `Kernel push error: Maximum weekly GPU quota of 30.00 hours reached.`
  - This is good evidence that the previous 400 was fixed; the remaining blocker is only GPU quota.
- Updated priority:
  - v50A dataset-mounted masked SFT is now the first run when quota recovers.
  - v45 remains fallback if v50A OOMs or fails before training.

## v50A pushed (2026-05-30 CST)

- Kaggle GPU quota is now available.
- Pushed `kaggle_kernel_v50a_reference_tail_dataset_v30/` to `guozhaojie/nemotron-rule-distill-v30`.
- Push result: `Kernel version 5 successfully pushed`.
- Expected run label: `v50a-reference-tail-dataset-masked-r16-220steps`.
- Next actions: poll logs for dataset mount, data summary, model load, masked loss token stats, and training start. Do not submit or download adapter until validation summary clears gate.

## v50A startup watch (2026-05-30 CST)

- v50A kernel version 5 is RUNNING but early logs are empty and files still show stale v40 outputs after several polling rounds.
- Continue monitoring before deciding whether it is a Kaggle scheduler/startup stall.


## v50A smoke fallback prepared (2026-05-30 CST)

- Current v50A version 5 remains RUNNING with empty logs after repeated polling.
- Prepared fallback notebook kaggle_kernel_v50a_smoke_dataset_v30/ with run label 50a-smoke-dataset-masked-r16-20steps.
- Purpose: if version 5 is judged scheduler-stuck, release it and run this smoke first to validate dataset mount and masked Trainer path before another long run.
- Push helper: scripts/push_v50a_smoke_when_needed.ps1.


## v50A smoke pushed to v26 track (2026-05-30 CST)

- v30 v50A remains RUNNING with empty logs/stale outputs.
- To avoid deleting the v30 kernel track, pushed v50A smoke to existing guozhaojie/nemotron-distilled-trajectory-v26.
- Push result: Kernel version 7 successfully pushed.
- Expected run label: 50a-smoke-dataset-masked-r16-20steps.
- Purpose: validate dataset mount and masked Trainer code path while v30 remains stuck/running.

## v45 and v50A smoke completed: both blocked (2026-05-31 CST)

v30 / v45:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Status: `COMPLETE`.
- Run label: `v45-think-close-tiny-r16-80steps`.
- Log: `outputs/kaggle/nemotron-rule-distill-v30-v6-v45.log`.
- Summary: `outputs/kaggle/nemotron-rule-distill-v30-v6-v45-summary.json`.
- Artifact creation in log: `/kaggle/working/submission.zip 1466.98 MB`.
- Validation:
  - `total=62`
  - `fixed_boxed=6`
  - `fixed_final_box_line=5`
  - `strict_single_boxed=5`
  - `fixed_correct=6`
  - all correct are `numeral`
- Gate: BLOCK.
  - `fixed_correct 6 < 26`
  - `strict_single_boxed 5 < 20`

v26 / v50A smoke:
- Kernel: `guozhaojie/nemotron-distilled-trajectory-v26`.
- Status: `COMPLETE`.
- Run label: `v50a-smoke-dataset-masked-r16-20steps`.
- Log: `outputs/kaggle/nemotron-distilled-trajectory-v26-v7-v50a-smoke.log`.
- Summary: `outputs/kaggle/nemotron-distilled-trajectory-v26-v7-v50a-smoke-summary.json`.
- Artifact creation in log: `/kaggle/working/submission.zip 1519.09 MB`.
- Validation:
  - `total=61`
  - `fixed_boxed=8`
  - `fixed_final_box_line=5`
  - `strict_single_boxed=5`
  - `fixed_correct=7`
  - one non-numeral family (`cryptarithm_deduce`) produced a boxed answer, but correctness remains zero outside `numeral`
- Gate: BLOCK.
  - `fixed_correct 7 < 26`
  - `strict_single_boxed 5 < 20`

Decision:
- Do not submit v45 or v50A smoke.
- Do not spend more GPU on generic format-only or reference-tail continuation variants.
- The failure mode is now consistent across v40, v45, v50A long, and v50A smoke: the adapter mostly preserves or worsens format, but does not learn cross-family solving. Correctness remains concentrated in Roman numeral tasks.
- Next useful route should be family-specific solver-distilled short targets, especially for deterministic families (`unit_conversion`, `gravity`, `cipher`, `bit_manipulation`, and equation-style numeric tasks), rather than copying reference reasoning tails.

## v51 family solver-distill pushed (2026-05-31 CST)

Strategic reason:
- Prior runs overpredicted gains because they optimized answer format or copied reference tails without teaching concrete non-`numeral` solving.
- v51 is the first explicit family-specific solver-distill run: each completion contains concrete short solution steps for the current prompt.
- Training uses masked completion loss, so the adapter learns assistant solving output instead of spending capacity on the prompt.

Prepared:
- Corpus builder: `scripts/build_v51_solver_distill_corpus.py`.
- Corpus: `outputs/bronze_corpus/v51_solver_distill_corpus.jsonl`.
- Summary: `outputs/bronze_corpus/v51_solver_distill_corpus_summary.md`.
- Rows: 1663.
- Completion lengths:
  - p50: 261 chars
  - p90: 396 chars
  - p99: 496 chars
  - bad_format: 0
- Category balance:
  - `bit_manipulation`: 300
  - `cipher`: 300
  - `equation_numeric_deduce`: 300
  - `equation_numeric_guess`: 18
  - `cryptarithm_deduce`: 54
  - `cryptarithm_guess`: 11
  - `gravity`: 300
  - `numeral`: 80
  - `unit_conversion`: 300
- Notebook: `kaggle_kernel_v51_solver_distill_masked_v30/`.
- Run label: `v51-solver-distill-masked-r16-180steps`.
- Settings:
  - rank16
  - max sequence length 1024
  - 180 train steps
  - LR `6e-5`
  - masked completion labels
  - validation max-new-tokens 160
- Push helper: `scripts/push_v51_when_quota_available.ps1`.

Push:
- Pushed to `guozhaojie/nemotron-rule-distill-v30`.
- Result: `Kernel version 7 successfully pushed`.
- Status immediately after push: `KernelWorkerStatus.RUNNING`.

Decision rules:
- Do not submit just because v51 is a new strategic direction.
- Submit only if validation shows non-`numeral` correctness and clears a materially higher local gate.
- If v51 only improves boxed format but non-`numeral` correctness remains near zero, stop SFT variants and pivot toward inference-time solver/plugin packaging instead.

## v51 completed: real direction improvement, still blocked (2026-06-01 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 7.
- Status: `COMPLETE`.
- Run label: `v51-solver-distill-masked-r16-180steps`.
- Output log downloaded via `kaggle kernels output`:
  - `outputs/kaggle/v51_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v7-v51-summary-from-output.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 1526.56 MB`

Validation:
- `total=61`
- `fixed_boxed=51`
- `fixed_final_box_line=50`
- `strict_single_boxed=50`
- `fixed_correct=16`

By family:
- `bit_manipulation`: `0/8` correct, `0/8` boxed
- `cipher`: `0/8` correct, `7/8` boxed
- `cryptarithm_deduce`: `0/8` correct, `7/8` boxed
- `cryptarithm_guess`: `0/2` correct, `2/2` boxed
- `equation_numeric_deduce`: `1/8` correct, `8/8` boxed
- `equation_numeric_guess`: `1/3` correct, `3/3` boxed
- `gravity`: `0/8` correct, `8/8` boxed
- `numeral`: `7/8` correct, `8/8` boxed
- `unit_conversion`: `7/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 16 < 26`.
- `strict_single_boxed 50 >= 20`, so formatting is no longer the main blocker.

Interpretation:
- v51 is the first run that materially validates the new direction: non-`numeral` correctness is now non-zero, and `unit_conversion` is nearly solved.
- It should not be submitted yet because the correctness gap remains large and many families are still at zero.
- The old failure mode ("never emits boxed answers") is mostly fixed for all non-bit families.
- Remaining failures are solver quality and answer formatting/rounding, not generic LoRA plumbing.

Next v52 focus:
- Preserve v51 masked solver-distill structure.
- Increase and sharpen high-transfer deterministic families:
  - keep `unit_conversion` strong
  - fix `gravity` final rounding/format to official answers
  - improve `equation_numeric` answer canonicalization, especially leading zeros/reversal mistakes
- Do not spend more data on `cipher` memorized word mappings unless we can add a real dictionary/substitution-solving objective; current v51 boxed cipher outputs are fluent but often wrong.
- For `bit_manipulation`, either force shorter final boxed emission with answer-only tail or handle it outside SFT; current bit outputs often calculate bits but fail to reach `</think>`/boxed within generation.

## v52 focused solver prepared (2026-06-01 CST)

Purpose:
- Follow v51 evidence rather than intuition:
  - format is mostly solved (`strict_single_boxed=50`)
  - `unit_conversion` is nearly solved (`7/8`)
  - `gravity` is close but loses exact formatting/rounding
  - `bit_manipulation` often calculates bits but fails to reach boxed output
  - `equation_numeric` boxes answers but hallucinates operation details

Prepared v52:
- Corpus builder: `scripts/build_v52_focused_solver_corpus.py`.
- Corpus: `outputs/bronze_corpus/v52_focused_solver_corpus.jsonl`.
- Summary: `outputs/bronze_corpus/v52_focused_solver_corpus_summary.md`.
- Rows: 2423.
- Completion lengths:
  - p50: 177 chars
  - p90: 224 chars
  - p99: 226 chars
  - bad_format: 0
- Category balance:
  - `bit_manipulation`: 600
  - `cipher`: 120
  - `cryptarithm_deduce`: 54
  - `cryptarithm_guess`: 11
  - `equation_numeric_deduce`: 540
  - `equation_numeric_guess`: 18
  - `gravity`: 600
  - `numeral`: 80
  - `unit_conversion`: 400
- Notebook: `kaggle_kernel_v52_focused_solver_masked_v30/`.
- Run label: `v52-focused-solver-masked-r16-220steps`.
- Settings:
  - rank16
  - max sequence length 1024
  - 220 train steps
  - LR `6e-5`
  - masked completion labels
  - validation max-new-tokens 128
- Push helper: `scripts/push_v52_when_quota_available.ps1`.

Expected improvement test:
- If gravity rises materially while unit_conversion stays high, v52 may approach the local submit gate.
- If bit remains 0 but reaches boxed output, v53 should decide whether bit needs answer-only oversampling or should be abandoned for LoRA.
- If v52 still stays under `fixed_correct=20`, the SFT route is probably capped and the next bronze attempt should shift toward an inference-time solver-compatible strategy rather than more adapters.

Push:
- Pushed to `guozhaojie/nemotron-rule-distill-v30`.
- Result: `Kernel version 8 successfully pushed`.
- Status immediately after push: `KernelWorkerStatus.RUNNING`.

## v52 completed: boxed-format win, correctness regression (2026-06-01 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 8.
- Status: `COMPLETE`.
- Run label: `v52-focused-solver-masked-r16-220steps`.
- Output log downloaded:
  - `outputs/kaggle/v52_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v8-v52-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v8-v52-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v8-v52-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 1508.48 MB`

Validation:
- `total=61`
- `fixed_boxed=61`
- `fixed_final_box_line=58`
- `strict_single_boxed=58`
- `fixed_correct=10`

By family:
- `bit_manipulation`: `0/8` correct, `8/8` boxed
- `cipher`: `0/8` correct, `8/8` boxed
- `cryptarithm_deduce`: `0/8` correct, `8/8` boxed
- `cryptarithm_guess`: `0/2` correct, `2/2` boxed
- `equation_numeric_deduce`: `1/8` correct, `8/8` boxed
- `equation_numeric_guess`: `0/3` correct, `3/3` boxed
- `gravity`: `1/8` correct, `8/8` boxed
- `numeral`: `7/8` correct, `8/8` boxed
- `unit_conversion`: `1/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 10 < 26`.
- `strict_single_boxed 58 >= 20`, so v52 solved output closure but not solving.

Interpretation:
- Do not submit v52.
- The all-family short/direct target damaged the best v51 behavior: `unit_conversion` fell from `7/8` to `1/8`.
- v52 confirms that "make every completion shorter" is the wrong general move. It helps boxed emission (`61/61`) but removes the concrete evidence chain the model used for successful unit conversion.
- Next route should replay v51's successful concrete style for solved families, while only locally compressing the failure modes:
  - keep v51 `unit_conversion` and `numeral`
  - keep concrete `bit_manipulation` selected rules but move the final bit string and boxed answer earlier
  - keep concrete `gravity` k-values but use higher precision and explicit "round to 2 decimals, strip trailing zeros"
  - avoid further oversampling generic `cipher`/`cryptarithm` targets unless a real solver/dictionary objective is added

## v53 hybrid replay prepared (2026-06-01 CST)

Purpose:
- Test a narrower repair after v52 regression:
  - replay v51 concrete evidence style for `unit_conversion` and `numeral`
  - preserve concrete bit selected rules but force the final bit string before `</think>`
  - preserve gravity k-values but use the largest-time example as the stable coefficient and format the final answer as two decimals with trailing zeros stripped
- This is a hypothesis test, not a promised improvement: it targets the exact v51/v52 failure contrast.

Prepared v53:
- Corpus builder: `scripts/build_v53_hybrid_replay_corpus.py`.
- Corpus: `outputs/bronze_corpus/v53_hybrid_replay_corpus.jsonl`.
- Summary: `outputs/bronze_corpus/v53_hybrid_replay_corpus_summary.md`.
- Rows: 1863.
- Completion lengths:
  - p50: 261 chars
  - p90: 365 chars
  - p99: 432 chars
  - bad_format: 0
- Category balance:
  - `bit_manipulation`: 420
  - `cipher`: 240
  - `cryptarithm_deduce`: 54
  - `cryptarithm_guess`: 11
  - `equation_numeric_deduce`: 300
  - `equation_numeric_guess`: 18
  - `gravity`: 420
  - `numeral`: 80
  - `unit_conversion`: 320
- Notebook: `kaggle_kernel_v53_hybrid_replay_masked_v30/`.
- Run label: `v53-hybrid-replay-masked-r16-220steps`.
- Settings:
  - rank16
  - max sequence length 1024
  - 220 train steps
  - LR `6e-5`
  - masked completion labels
  - validation max-new-tokens 192
- Push helper: `scripts/push_v53_when_quota_available.ps1`.

Local preflight:
- Notebook code cells compile.
- Embedded corpus decompresses to 1863 rows.
- Embedded run label is `v53-hybrid-replay-masked-r16-220steps`.
- Embedded corpus `bad_format=0`.

Execution policy:
- Push v53 next if Kaggle GPU quota accepts it.
- Do not submit unless validation materially beats v51 (`fixed_correct=16`) and ideally clears the conservative gate (`fixed_correct>=26`, `strict_single_boxed>=20`).
- If v53 stays near or below v51, stop spending GPU on simple SFT target edits and pivot to a stronger solver-compatible route or public-solution-style reproduction.

Push:
- Pushed to `guozhaojie/nemotron-rule-distill-v30`.
- Result: `Kernel version 9 successfully pushed`.
- Status immediately after push: `KernelWorkerStatus.RUNNING`.
- First log poll was still empty, so continue monitoring before drawing any result.

## v53 completed: best local validation so far, still below submit gate (2026-06-01 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 9.
- Status: `COMPLETE`.
- Run label: `v53-hybrid-replay-masked-r16-220steps`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v53_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v9-v53-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v9-v53-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v9-v53-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 1527.70 MB`

Validation:
- `total=61`
- `fixed_boxed=56`
- `fixed_final_box_line=56`
- `strict_single_boxed=56`
- `fixed_correct=23`

By family:
- `bit_manipulation`: `3/8` correct, `8/8` boxed
- `cipher`: `1/8` correct, `8/8` boxed
- `cryptarithm_deduce`: `0/8` correct, `6/8` boxed
- `cryptarithm_guess`: `0/2` correct, `1/2` boxed
- `equation_numeric_deduce`: `4/8` correct, `8/8` boxed
- `equation_numeric_guess`: `0/3` correct, `3/3` boxed
- `gravity`: `2/8` correct, `7/8` boxed
- `numeral`: `7/8` correct, `7/8` boxed
- `unit_conversion`: `6/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 23 < 26`.
- `strict_single_boxed 56 >= 20`.
- Do not submit v53 under the current conservative gate.

Interpretation:
- v53 is the best local validation result so far and materially beats v51 (`16/61`) and v52 (`10/61`), so the v51-replay-plus-local-repair idea is directionally useful.
- The targeted fixes worked:
  - `bit_manipulation` improved from `0/8` to `3/8`.
  - `equation_numeric_deduce` improved from `1/8` to `4/8`.
  - `gravity` improved from `0/8` or `1/8` to `2/8`.
  - `unit_conversion` mostly recovered from v52 (`1/8`) to `6/8`, though still below v51 (`7/8`).
- Remaining gap to the conservative gate is only 3 validation examples, but correctness is still concentrated in deterministic families; hidden/public transfer is not guaranteed.

Next action:
- Prepare a v54 only if it can target the remaining three-example gap without destroying v53 gains.
- Highest ROI candidates:
  - replay v51 unit conversion more exactly, because v53 lost one example versus v51
  - improve gravity coefficient/format using a train-set evaluated rule instead of a single largest-time heuristic
  - improve equation_numeric by canonicalizing final reversal/leading-zero behavior
- Avoid spending more on generic cipher/cryptarithm text imitation unless a stronger symbolic solver objective is added.

## v54 fixed-validation precision prepared (2026-06-01 CST)

Purpose:
- Make the next local result comparable to v53 by using the same 61 validation IDs from `outputs/kaggle/nemotron-rule-distill-v30-v9-v53-checks.json`.
- Target the remaining near-gate gap without broad target-style churn:
  - `bit_manipulation`: add compact query-bit and per-bit application lines after selected rules
  - `unit_conversion`: list example factors and use ASCII least-squares factor from all examples
  - `gravity`: list k-values and use ASCII least-squares k from all observations
  - keep v53/v51 concrete style for equation/numeral/cipher/cryptarithm

Prepared v54:
- Corpus builder: `scripts/build_v54_fixedval_precision_corpus.py`.
- Corpus: `outputs/bronze_corpus/v54_fixedval_precision_corpus.jsonl`.
- Summary: `outputs/bronze_corpus/v54_fixedval_precision_corpus_summary.md`.
- Rows: 2403.
- Completion lengths:
  - p50: 293 chars
  - p90: 405 chars
  - p99: 536 chars
  - bad_format: 0
- Category balance:
  - `bit_manipulation`: 520
  - `cipher`: 260
  - `cryptarithm_deduce`: 54
  - `cryptarithm_guess`: 11
  - `equation_numeric_deduce`: 520
  - `equation_numeric_guess`: 18
  - `gravity`: 520
  - `numeral`: 80
  - `unit_conversion`: 420
- Notebook: `kaggle_kernel_v54_fixedval_precision_masked_v30/`.
- Run label: `v54-fixedval-precision-masked-r16-260steps`.
- Settings:
  - rank16
  - max sequence length 1024
  - 260 train steps
  - LR `6e-5`
  - masked completion labels
  - validation max-new-tokens 256
- Fixed validation:
  - 61 fixed validation IDs from v53
  - all 61 are present in the embedded corpus
  - expected train rows after fixed split: 2342
- Push helper: `scripts/push_v54_when_quota_available.ps1`.

Local preflight:
- Notebook code cells compile.
- Embedded corpus decompresses to 2403 rows.
- Embedded run label is `v54-fixedval-precision-masked-r16-260steps`.
- Embedded corpus `bad_format=0`.
- Fixed validation IDs missing from embedded corpus: 0.

Execution policy:
- Push v54 next if Kaggle GPU quota accepts it.
- Compare primarily against v53 on the same 61 validation examples:
  - v53 same-split reference: `fixed_correct=23`, `strict_single_boxed=56`
  - v54 submit gate remains `fixed_correct>=26`, `strict_single_boxed>=20`
- Do not submit if v54 does not clear the fixed-split gate.

Push:
- Pushed to `guozhaojie/nemotron-rule-distill-v30`.
- Result: `Kernel version 10 successfully pushed`.
- Status immediately after push: `KernelWorkerStatus.RUNNING`.

## v54 completed: fixed-split precision attempt regressed (2026-06-01 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 10.
- Status: `COMPLETE`.
- Run label: `v54-fixedval-precision-masked-r16-260steps`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v54_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v10-v54-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v10-v54-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v10-v54-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 1533.16 MB`

Validation:
- `total=61`
- `fixed_boxed=55`
- `fixed_final_box_line=55`
- `strict_single_boxed=55`
- `fixed_correct=16`

By family:
- `bit_manipulation`: `0/8` correct, `7/8` boxed
- `cipher`: `2/8` correct, `8/8` boxed
- `cryptarithm_deduce`: `0/8` correct, `4/8` boxed
- `cryptarithm_guess`: `0/2` correct, `2/2` boxed
- `equation_numeric_deduce`: `1/8` correct, `7/8` boxed
- `equation_numeric_guess`: `0/3` correct, `3/3` boxed
- `gravity`: `0/8` correct, `8/8` boxed
- `numeral`: `8/8` correct, `8/8` boxed
- `unit_conversion`: `5/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 16 < 26`.
- `strict_single_boxed 55 >= 20`.
- Do not submit v54.

Comparison to v53 fixed-split reference:
- v53: `fixed_correct=23`, `strict_single_boxed=56`.
- v54: `fixed_correct=16`, `strict_single_boxed=55`.
- The precision/fixed-val attempt regressed by 7 correctness points on the same 61 validation IDs.

Interpretation:
- v54 confirms the least-squares precision target is harmful for this model/output regime despite better train-set formula accuracy on paper.
- The added bit application lines also hurt `bit_manipulation` (`3/8` in v53 -> `0/8` in v54), likely because the model learned plausible but wrong selected rules and then confidently applied them.
- Keep v53 as the best current local candidate; do not replace it with v54.
- Next useful route should either:
  - revert to v53 targets and make only very small edits, or
  - pivot away from more SFT target shaping toward a stronger symbolic/inference-compatible solver route.

## v55 v53-replay rank32 fixed-val prepared (2026-06-01 CST)

Purpose:
- Test the capacity/optimization hypothesis without changing the v53 completion style.
- v54 showed that target rewrites can destroy v53 gains, so v55 reuses the v53 hybrid replay corpus exactly and only changes training parameters.

Prepared v55:
- Corpus: `outputs/bronze_corpus/v53_hybrid_replay_corpus.jsonl`.
- Notebook: `kaggle_kernel_v55_v53_replay_r32_fixedval_v30/`.
- Run label: `v55-v53-replay-r32-fixedval-260steps`.
- Settings:
  - rank32 LoRA (competition limit)
  - max sequence length 1024
  - 260 train steps
  - LR `4e-5`
  - masked completion labels
  - validation max-new-tokens 192
- Fixed validation:
  - same 61 validation IDs as v53
  - all 61 are present in the embedded v53 corpus
  - expected train rows after fixed split: 1802
- Push helper: `scripts/push_v55_when_quota_available.ps1`.

Local preflight:
- Notebook code cells compile.
- Embedded corpus decompresses to 1863 rows.
- Embedded run label is `v55-v53-replay-r32-fixedval-260steps`.
- Embedded corpus `bad_format=0`.
- Fixed validation IDs missing from embedded corpus: 0.

Execution policy:
- Push v55 next if Kaggle GPU quota accepts it.
- Compare against v53 on the same 61 validation examples:
  - v53 fixed-split reference: `fixed_correct=23`, `strict_single_boxed=56`
  - submit gate remains `fixed_correct>=26`, `strict_single_boxed>=20`
- Do not submit if v55 does not clear the fixed-split gate.

Push:
- Pushed to `guozhaojie/nemotron-rule-distill-v30`.
- Result: `Kernel version 11 successfully pushed`.
- Status immediately after push: `KernelWorkerStatus.RUNNING`.

## v55 completed: rank32 capacity test tied v53, still blocked (2026-06-02 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 11.
- Status: `COMPLETE`.
- Run label: `v55-v53-replay-r32-fixedval-260steps`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v55_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v11-v55-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v11-v55-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v11-v55-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 3058.28 MB`

Validation:
- `total=61`
- `fixed_boxed=55`
- `fixed_final_box_line=55`
- `strict_single_boxed=55`
- `fixed_correct=23`

By family:
- `bit_manipulation`: `3/8` correct, `8/8` boxed
- `cipher`: `1/8` correct, `8/8` boxed
- `cryptarithm_deduce`: `0/8` correct, `3/8` boxed
- `cryptarithm_guess`: `0/2` correct, `1/2` boxed
- `equation_numeric_deduce`: `5/8` correct, `8/8` boxed
- `equation_numeric_guess`: `0/3` correct, `3/3` boxed
- `gravity`: `0/8` correct, `8/8` boxed
- `numeral`: `8/8` correct, `8/8` boxed
- `unit_conversion`: `6/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 23 < 26`.
- `strict_single_boxed 55 >= 20`.
- Do not submit v55.

Comparison to v53 fixed-split reference:
- v53: `fixed_correct=23`, `strict_single_boxed=56`, rank16 artifact about 1.53 GB.
- v55: `fixed_correct=23`, `strict_single_boxed=55`, rank32 artifact about 3.06 GB.
- Rank32 improved some equation/numeral behavior but lost all v53 gravity correctness, so the net result tied v53 and produced a much larger adapter.

Interpretation:
- Capacity alone is not the missing 3 examples.
- v53 remains the best current local candidate; v55 should not replace it.
- The next useful work should stop broad SFT tuning and focus on either:
  - targeted same-split ensemble-style target construction that preserves v53 gravity/unit behavior while adding only equation gains, or
  - a stronger synthetic solver-distill route for controllable deterministic families.

## v53 official submission queued (2026-06-02 CST)

Reason:
- User requested submitting v53 first to preserve a stronger score before continuing research.
- v53 remains the best local candidate after v54/v55 failed to improve on the same fixed validation split.

Submission:
- Command used:
  - `kaggle competitions submit nvidia-nemotron-model-reasoning-challenge -k guozhaojie/nemotron-rule-distill-v30 -v 9 -f submission.zip -m "v53 official hybrid replay solver-distill fixed_correct23"`
- Submitted kernel/version:
  - kernel: `guozhaojie/nemotron-rule-distill-v30`
  - version: 9
  - run label: `v53-hybrid-replay-masked-r16-220steps`
- Submission ref:
  - `53271130`
- Initial status:
  - `SubmissionStatus.PENDING`

Important:
- This intentionally submits v53, not the latest kernel output v55.
- Do not confuse the current kernel's latest version 11 with the submitted version 9.
- Wait for public score before judging transfer.

Official public result:
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.51`.
- Previous official v23 public score: `0.54`.
- Delta: `-0.03`.

Interpretation:
- v53 local improvement did not transfer to public leaderboard.
- The current official best remains v23 (`0.54`), not v53.
- This confirms the validation-to-public gap is severe; future work must not rely on the 61-example local validation score alone.

## v56 prepared: v24-style low-intrusion masked format adapter (2026-06-02 CST)

Reason:
- v53/v55 local gains did not transfer to public; v53 scored `0.51` vs v23 `0.54`.
- Next experiment should protect base-model reasoning instead of adding more solver-distill pressure.
- v56 tests a conservative format-only direction closer to v23/v24:
  - v24 balanced answer-only corpus style.
  - completion-only masked loss.
  - rank8 LoRA, low LR, short training.
  - fixed 61 validation split for comparability with v53/v55.

Prepared files:
- Notebook: `kaggle_kernel_v56_v24_masked_lowintrusion_v30/nemotron-lora-smoke-training.ipynb`.
- Metadata: `kaggle_kernel_v56_v24_masked_lowintrusion_v30/kernel-metadata.json`.
- Push helper: `scripts/push_v56_when_quota_available.ps1`.
- Local preflight summary: `outputs/kaggle/v56_preflight_summary.json`.

Settings:
- Run label: `v56-v24-masked-lowintrusion-r8-80steps-fixed61`.
- Train rows: `595`.
- Validation rows: `61`.
- LoRA rank: `8`.
- LoRA alpha: `16`.
- Max sequence length: `1024`.
- Max steps: `80`.
- LR: `2e-5`.
- Generation max-new-tokens: `96`.
- Target format: exactly one completion line, `\boxed{official_answer}`.

Data checks:
- Source train corpus: v24 balanced answer-only rows.
- Fixed validation source: `external/tonghuikang-nemotron/train.csv`, using the same 61 IDs as v53/v55.
- Dropped 5 v24 train rows that overlapped fixed validation:
  - `0fcf912a`, `1b5cab20`, `28e3bbd3`, `d0b1e41a`, `d63c1fb0`.
- Train/validation ID overlap after filtering: `0`.
- Bad completion format:
  - train: `0`
  - validation: `0`

Family counts:
- Train:
  - `bit_manipulation`: `99`
  - `cipher`: `99`
  - `equation`: `97`
  - `gravity`: `100`
  - `numeral`: `100`
  - `unit_conversion`: `100`
- Validation:
  - `bit_manipulation`: `8`
  - `cipher`: `8`
  - `equation`: `21`
  - `gravity`: `8`
  - `numeral`: `8`
  - `unit_conversion`: `8`

Local preflight:
- Notebook code cells parse successfully.
- Metadata points to `guozhaojie/nemotron-rule-distill-v30`.
- Embedded run label is `v56-v24-masked-lowintrusion-r8-80steps-fixed61`.

Execution policy:
- Push/run v56 when Kaggle GPU quota accepts it.
- Download only lightweight logs first.
- Parse with:
  - `scripts/summarize_kaggle_kernel_log.py`
  - `scripts/extract_validation_checks_from_kaggle_log.py`
- Do not download the adapter or submit from local validation alone.
- Treat v56 primarily as a public-transfer strategy test candidate; compare against v23 public `0.54` and v53 public `0.51`.

Push:
- Command used:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v56_when_quota_available.ps1`
- Result:
  - `Kernel version 12 successfully pushed`.
- Kernel:
  - `guozhaojie/nemotron-rule-distill-v30`.
- Status immediately after push:
  - `KernelWorkerStatus.RUNNING`.
- Immediate log probe:
  - `kaggle kernels logs guozhaojie/nemotron-rule-distill-v30` returned no log text yet.

## v56 completed: low-intrusion rank8 underfit, do not submit (2026-06-02 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 12.
- Status: `COMPLETE`.
- Run label: `v56-v24-masked-lowintrusion-r8-80steps-fixed61`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v56_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v12-v56-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v12-v56-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v12-v56-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 719.45 MB`

Validation:
- `total=61`
- `fixed_boxed=4`
- `fixed_final_box_line=1`
- `strict_single_boxed=1`
- `fixed_correct=1`

By family:
- `bit_manipulation`: `0/8` correct, `0/8` boxed
- `cipher`: `0/8` correct, `0/8` boxed
- `equation`: `0/21` correct, `3/21` boxed
- `gravity`: `0/8` correct, `0/8` boxed
- `numeral`: `1/8` correct, `1/8` boxed
- `unit_conversion`: `0/8` correct, `0/8` boxed

Gate:
- BLOCK.
- `fixed_correct 1 < 23`.
- `strict_single_boxed 1 < 20`.
- Do not submit v56.
- Do not download the adapter.

Interpretation:
- The low-intrusion rank8/80-step masked answer-only adapter underfit the output protocol.
- Generations mostly reverted to long base-model reasoning and did not reach a final boxed answer within 96 tokens.
- This confirms that simply lowering LoRA capacity/training pressure is not enough; it protects base reasoning too much to fix the required final-answer format.
- Future public-transfer candidates should not go this weak. A better next test would keep the base-protecting idea but increase format pressure, for example rank16 with more steps or a two-stage target that teaches immediate final boxing without broad solver-distill rewrites.

## v57 prepared: v24 masked format-pressure test (2026-06-02 CST)

Reason:
- v56 underfit the output protocol (`fixed_correct=1`, `strict_single_boxed=1`).
- v53/v55 proved solver-distill can fix local format/correctness but failed public transfer.
- v57 keeps the v56 base-protecting data strategy but increases format pressure:
  - same filtered v24 answer-only corpus
  - same fixed 61 validation IDs
  - completion-only masked loss
  - rank16 instead of rank8
  - 160 steps instead of 80
  - LR `5e-5` instead of `2e-5`

Prepared files:
- Notebook: `kaggle_kernel_v57_v24_masked_formatpressure_v30/nemotron-lora-smoke-training.ipynb`.
- Metadata: `kaggle_kernel_v57_v24_masked_formatpressure_v30/kernel-metadata.json`.
- Push helper: `scripts/push_v57_when_quota_available.ps1`.
- Local preflight summary: `outputs/kaggle/v57_preflight_summary.json`.

Settings:
- Run label: `v57-v24-masked-formatpressure-r16-160steps-fixed61`.
- Train rows: `595`.
- Validation rows: `61`.
- LoRA rank: `16`.
- LoRA alpha: `32`.
- Max sequence length: `1024`.
- Max steps: `160`.
- LR: `5e-5`.
- Generation max-new-tokens: `64`.

Local preflight:
- Notebook code cells parse successfully.
- Train/validation ID overlap: `0`.
- Bad completion format:
  - train: `0`
  - validation: `0`

Execution policy:
- Push/run v57 when Kaggle accepts it.
- Download only lightweight logs first.
- Do not download the adapter or submit automatically.
- Compare primarily against:
  - v56: `fixed_correct=1`, `strict_single_boxed=1`
  - v53: `fixed_correct=23`, `strict_single_boxed=56`, public `0.51`
  - v23: public `0.54`

Push:
- Command used:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v57_when_quota_available.ps1`
- Result:
  - `Kernel version 13 successfully pushed`.
- Kernel:
  - `guozhaojie/nemotron-rule-distill-v30`.
- Status immediately after push:
  - `KernelWorkerStatus.RUNNING`.

## v57 completed: masked format-pressure fixed format but lost correctness (2026-06-03 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 13.
- Status: `COMPLETE`.
- Run label: `v57-v24-masked-formatpressure-r16-160steps-fixed61`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v57_output_probe/nemotron-rule-distill-v30.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v13-v57-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v13-v57-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v13-v57-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 1463.14 MB`

Validation:
- `total=61`
- `fixed_boxed=60`
- `fixed_final_box_line=60`
- `strict_single_boxed=60`
- `fixed_correct=17`

By family:
- `bit_manipulation`: `3/8` correct, `8/8` boxed
- `cipher`: `1/8` correct, `8/8` boxed
- `equation`: `3/21` correct, `20/21` boxed
- `gravity`: `0/8` correct, `8/8` boxed
- `numeral`: `8/8` correct, `8/8` boxed
- `unit_conversion`: `2/8` correct, `8/8` boxed

Gate:
- BLOCK.
- `fixed_correct 17 < 23`.
- `strict_single_boxed 60 >= 20`.
- Do not submit v57.
- Do not download the adapter.

Interpretation:
- Rank16/160-step masked answer-only training solved the immediate boxed-output protocol, but it still reduced local correctness versus v53/v55 (`23/61`).
- The masked route is no longer primarily a format problem; it is a reasoning-transfer problem.
- Because v53 already scored worse publicly despite tying the best local fixed-61 result, v57 has no strategic submission value.
- Next test should pivot back toward the v23-style full-text format-first recipe, which is exactly the purpose of prepared v58.

## v58 prepared: v24 full-text format-first fallback (2026-06-02 CST)

Reason:
- v57 is running, but v56 showed masked completion-only may be too weak for immediate boxed emission.
- v58 is prepared, not pushed, as a fallback that is closer to the v23/v24 public-transfer style:
  - filtered v24 answer-only corpus
  - fixed 61 validation IDs
  - full-text `SFTTrainer` loss instead of masked completion-only loss
  - rank32/alpha64
  - 120 steps
  - LR `5e-5`
- This is more intrusive than v57 but closer to the official best v23-style route.

Prepared files:
- Notebook: `kaggle_kernel_v58_v24_fulltext_formatfirst_v30/nemotron-lora-smoke-training.ipynb`.
- Metadata: `kaggle_kernel_v58_v24_fulltext_formatfirst_v30/kernel-metadata.json`.
- Push helper: `scripts/push_v58_when_quota_available.ps1`.
- Local preflight summary: `outputs/kaggle/v58_preflight_summary.json`.

Settings:
- Run label: `v58-v24-fulltext-formatfirst-r32-120steps-fixed61`.
- Train rows: `595`.
- Validation rows: `61`.
- LoRA rank: `32`.
- LoRA alpha: `64`.
- Max sequence length: `1024`.
- Max steps: `120`.
- LR: `5e-5`.
- Generation max-new-tokens: `64`.

Local preflight:
- Notebook code cells parse successfully.
- Uses `SFTTrainer`: `true`.
- Uses masked collator: `false`.
- Train/validation ID overlap: `0`.
- Bad completion format:
  - train: `0`
  - validation: `0`

Execution policy:
- Do not push v58 while v57 is still running.
- If v57 remains below v53 and especially if boxed emission is still weak, v58 is the next available experiment to test whether full-text format-first SFT transfers better than masked answer-only SFT.
- Do not submit automatically.

Push:
- Command used:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v58_when_quota_available.ps1`
- Result:
  - `Kernel version 14 successfully pushed`.
- Kernel:
  - `guozhaojie/nemotron-rule-distill-v30`.
- Status immediately after push:
  - `KernelWorkerStatus.RUNNING`.
- Immediate log probe:
  - `kaggle kernels logs guozhaojie/nemotron-rule-distill-v30` returned no log text yet.

## v58 completed: full-text short fallback collapsed, do not submit (2026-06-03 CST)

Result:
- Kernel: `guozhaojie/nemotron-rule-distill-v30`.
- Version: 14.
- Status: `COMPLETE`.
- Run label: `v58-v24-fulltext-formatfirst-r32-120steps-fixed61`.
- Lightweight log captured from `kaggle kernels logs`:
  - `outputs/kaggle/v58_output_probe/nemotron-rule-distill-v30.log`
  - Raw decoded log: `outputs/kaggle/v58_output_probe/nemotron-rule-distill-v30.raw.log`
- Summary:
  - `outputs/kaggle/nemotron-rule-distill-v30-v14-v58-summary.json`
- Checks:
  - `outputs/kaggle/nemotron-rule-distill-v30-v14-v58-checks.json`
  - `outputs/kaggle/nemotron-rule-distill-v30-v14-v58-checks-summary.json`
- Artifact creation in log:
  - `/kaggle/working/submission.zip 2939.23 MB`

Validation:
- `total=61`
- `fixed_boxed=1`
- `fixed_final_box_line=0`
- `strict_single_boxed=0`
- `fixed_correct=0`

By family:
- `bit_manipulation`: `0/8` correct, `0/8` boxed
- `cipher`: `0/8` correct, `0/8` boxed
- `equation`: `0/21` correct, `1/21` boxed
- `gravity`: `0/8` correct, `0/8` boxed
- `numeral`: `0/8` correct, `0/8` boxed
- `unit_conversion`: `0/8` correct, `0/8` boxed

Gate:
- BLOCK.
- `fixed_correct 0 < 23`.
- `strict_single_boxed 0 < 20`.
- Do not submit v58.
- Do not download or use the large adapter.

Interpretation:
- The short v24 full-text SFT fallback did not preserve the required output protocol and collapsed on the fixed 61 validation slice.
- This strengthens the conclusion that our incremental v23/v24/v5x LoRA tuning path is not enough for medal-range performance.
- The current public leaderboard distribution requires a method-level pivot: our best public `0.54` is rank about `3333/3871`, while public Top 10% is about `0.86`.

## Public pivot candidate: huikang LB 0.85 end-to-end finetuning (2026-06-03 CST)

Source found:
- Kaggle notebook: `huikang/end-to-end-finetuning-for-lb-0-85`.
- Local pull:
  - `research/public_baselines/huikang_lb085/end-to-end-finetuning-for-lb-0-85.ipynb`
  - `research/public_baselines/huikang_lb085/kernel-metadata.json`
  - extracted code: `research/public_baselines/huikang_lb085/extracted_code.py`
- Public metadata:
  - title: `End-to-end finetuning for LB 0.85`
  - machine: `NvidiaRtxPro6000`
  - competition source: `nvidia-nemotron-model-reasoning-challenge`
  - model source: `metric/nemotron-3-nano-30b-a3b-bf16/Transformers/default/1`
  - dataset sources:
    - `huikang/huikang-nemotron-repository-snapshot`
    - `mayukh18/nemotron-packages`
    - `llkh0a/rtx-wheels`

Key differences from our v5x route:
- Long context: `MAX_SEQ_LEN=8192` instead of our 1024-ish short training.
- More training: `NUM_STEPS=1000`, batch size `32`, micro batch `4`.
- Larger/custom token-level objective:
  - loads pre-tokenized examples with `tokens`, `targets`, and per-token `weights`.
  - uses weighted per-token loss rather than ordinary SFT text loss.
  - patches forward with `cut_cross_entropy.linear_cross_entropy` to avoid full logits materialization.
- Wider target modules:
  - `q_proj`, `k_proj`, `v_proj`, `o_proj`, `up_proj`, `down_proj`, `in_proj`, `out_proj`, and manually added `lm_head`.
- Nemotron/MoE-specific engineering:
  - patches Mamba fast path.
  - casts LoRA params to fp32 while base stays bf16.
  - manually adds LoRA to `lm_head` because Unsloth drops it for MoE.
  - ties selected MoE expert LoRA sides in a Tinker-style pattern, then saves ordinary untied adapter weights.
- Data route is not just train.csv SFT:
  - uses the public `huikang-nemotron-repository-snapshot` token corpus and training-order/logprob files.

Strategic conclusion:
- This is the first credible public route found that explains the `0.85+` leaderboard cluster.
- Reproducing this public notebook is a legitimate pivot candidate.
- Spending money can make sense only for compliant compute/reproduction, for example Modal or paid GPU time on RTX PRO 6000-class hardware.
- Do not buy private answers, leaked labels, private team artifacts, or anything that bypasses the competition rules.
- Next experiment should be a faithful public-baseline reproduction or near-faithful ablation, not another small v23/v24 LoRA tweak.

## v59 pushed: faithful huikang LB 0.85 public baseline reproduction (2026-06-04 CST)

Reason:
- User asked to start reproducing the public `0.85+` route with cost control.
- Cost-control decision:
  - Start with Kaggle free quota first.
  - Do not pay for Modal/paid GPU unless the faithful Kaggle reproduction fails due quota/runtime/machine constraints.
  - Do not buy private solutions or private artifacts.

Prepared files:
- Kernel directory:
  - `kaggle_kernel_v59_huikang_lb085_repro`
- Notebook:
  - `kaggle_kernel_v59_huikang_lb085_repro/nemotron-huikang-lb085-repro.ipynb`
- Metadata:
  - `kaggle_kernel_v59_huikang_lb085_repro/kernel-metadata.json`
- Push helper:
  - `scripts/push_v59_huikang_repro_when_quota_available.ps1`
- Preflight summary:
  - `outputs/kaggle/v59_huikang_repro_preflight_summary.json`

Faithfulness:
- Notebook is a byte-for-byte copy of:
  - `research/public_baselines/huikang_lb085/end-to-end-finetuning-for-lb-0-85.ipynb`
- SHA-256:
  - `639dd61111e8d5397afdf093ae3ddec0a0ad964726b244b89a38cbda6b149d6d`
- Only the Kaggle kernel metadata was changed to use our private kernel slug:
  - `guozhaojie/nemotron-huikang-lb085-repro-v59`

Preflight:
- PASS.
- `MAX_SEQ_LEN=8192`
- `NUM_STEPS=1000`
- `BATCH_SIZE=32`
- `MICRO_BATCH_SIZE=4`
- `LORA_RANK=32`
- `LORA_ALPHA=32`
- `LEARNING_RATE=2e-4`
- `RESET_WEIGHTS=True`
- `MOE_TIE_WEIGHTS=True`
- `ORIGINAL_PROBLEMS_ONLY=False`
- `SHUFFLE_DATASET=False`
- Detected weighted token loss with `cut_cross_entropy.linear_cross_entropy`.
- Detected manual `lm_head` LoRA patch.
- Detected MoE expert LoRA tying.
- Detected `submission.zip` packaging.
- No automatic competition submit detected.

Public input sources:
- `huikang/huikang-nemotron-repository-snapshot`
- `mayukh18/nemotron-packages`
- `llkh0a/rtx-wheels`
- `metric/nemotron-3-nano-30b-a3b-bf16/Transformers/default/1`

Push:
- Initial push attempt hit a Windows/Kaggle CLI encoding issue:
  - `'gbk' codec can't decode byte 0x8b...`
- Fix:
  - updated push helper to set `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8`.
- Result:
  - `Kernel version 1 successfully pushed`.
- Kernel:
  - `guozhaojie/nemotron-huikang-lb085-repro-v59`
- Status after push:
  - `KernelWorkerStatus.RUNNING`.
- Early log probe:
  - `kaggle kernels logs guozhaojie/nemotron-huikang-lb085-repro-v59` returned no log text yet.

Execution policy:
- This notebook does not include our fixed-61 validation harness; it is a faithful public-baseline reproduction.
- When complete, first inspect status, logs, and output file list only.
- Do not download the large `submission.zip` automatically.
- Do not submit automatically.
- If the run fails due Kaggle quota/runtime/resource limits, evaluate a cost-capped Modal/paid-GPU reproduction before spending money.

## v59 completed: faithful huikang LB 0.85 reproduction produced submission.zip (2026-06-04 CST)

Result:
- Kernel: `guozhaojie/nemotron-huikang-lb085-repro-v59`.
- Version: 1.
- Status: `COMPLETE`.
- Lightweight log captured:
  - `outputs/kaggle/v59_huikang_repro_output_probe/nemotron-huikang-lb085-repro-v59.log`
  - decoded raw log: `outputs/kaggle/v59_huikang_repro_output_probe/nemotron-huikang-lb085-repro-v59.raw.log`
- Log summary:
  - `outputs/kaggle/v59_huikang_repro_output_probe/v59_log_summary.json`
- File listing:
  - `outputs/kaggle/v59_huikang_repro_output_probe/nemotron-huikang-lb085-repro-v59.files.txt`

Training evidence:
- GPU: `NVIDIA RTX PRO 6000 Blackwell Server Edition, sm_120`.
- VRAM: `102.0 GB`.
- Loaded `7830` examples, `27,842,873` tokens, `26,568,807` unmasked tokens.
- Model: `888,154,112` trainable / `32,466,091,456` total parameters.
- MoE tying: `5888` params identified for tying.
- Requested `NUM_STEPS=1000`, but the public corpus has `7830` examples and `BATCH_SIZE=32`, so training clamped to `244` steps.
- Final step:
  - `step 244/244`
  - `loss:mean=0.007994`
  - `grad_norm=0.3106`
  - `lr=8.20e-07`
- Peak VRAM: `87.9 GB`.
- Log confirms:
  - `Wrote submission.zip`
  - `Training complete.`

Output files:
- `README.md`
- `submission.zip`

Interpretation:
- The faithful public baseline reproduction ran successfully on Kaggle free quota; no paid compute was needed.
- Because this notebook has no fixed-61 validation harness, there is no local validation score from the run.
- This is a public `LB 0.85` reproduction artifact candidate, but it still needs artifact inspection and an explicit user decision before any official submission.
- Do not download `submission.zip` automatically.
- Do not submit automatically.

## v59 official submission pending (2026-06-05 CST)

Decision:
- User explicitly approved submitting v59.

Submission:
- Command script:
  - `scripts/submit_v59_huikang_repro_official.ps1`
- Competition:
  - `nvidia-nemotron-model-reasoning-challenge`
- Kernel:
  - `guozhaojie/nemotron-huikang-lb085-repro-v59`
- Kernel version:
  - `1`
- Output file:
  - `submission.zip`
- Description:
  - `v59 official faithful huikang LB0.85 public baseline repro`
- Submission ref:
  - `53376847`
- Status immediately after submission:
  - `SubmissionStatus.PENDING`
- Public score:
  - pending

Comparison target:
- Current official best before v59 remains v23:
  - public score `0.54`
  - ref `52492096`
- v53 remains worse:
  - public score `0.51`
  - ref `53271130`

Next action:
- Monitor ref `53376847` until scoring completes.
- Record public score and leaderboard impact when complete.

Official public result:
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.67`.
- Previous official best v23 public score: `0.54`.
- Delta vs v23: `+0.13`.
- Delta vs v53 public score `0.51`: `+0.16`.

Interpretation:
- v59 is now the best official submission for this account.
- The public LB0.85 reproduction did not reproduce the claimed `0.85` score exactly, but it produced a clear step-change over the previous `0.54` best.
- The result validates the pivot away from small v5x LoRA tweaks toward the public end-to-end token-level training route.
- Next work should focus on why faithful v59 lands at `0.67` instead of `0.85`, not on returning to the old short-context SFT route.

Leaderboard snapshot after v59 (2026-06-06 CST):
- Latest downloaded leaderboard:
  - `outputs/kaggle/leaderboard_probe_latest/nvidia-nemotron-model-reasoning-challenge.zip`
- Parsed snapshot:
  - `outputs/kaggle/leaderboard_probe_latest/v59_rank_snapshot.json`
- Total teams: `3954`.
- Top public score: `0.89`.
- `guozhaojie` rank: `2488`.
- `guozhaojie` public score: `0.67`.
- Score `0.67` rank band:
  - starts at rank `2454`
  - ends at rank `2516`
  - `63` teams tied at `0.67`
- Approximate public Top 10% / medal-relevant score line:
  - rank `396`
  - score `0.86`
- Public Top 40% score line:
  - rank `1582`
  - score `0.85`

Implication:
- v59 moved the account from the old `0.54` cluster to a materially better `0.67`, but it is still far below the `0.85-0.86` dense frontier.
- The next useful question is not whether public token-level end-to-end finetuning works; it does.
- The next useful question is why this faithful Kaggle reproduction underperforms the advertised `LB 0.85`, with likely suspects including source notebook version drift, public/private kernel-output mismatch, missing predecessor adapter path, or hidden differences in the author's actual submitted artifact.

## Public 0.86 replay route research: Mohamed baseline is the next best v60 candidate (2026-06-06 CST)

Reason:
- User asked to research the next realistic route after v59 improved to `0.67` but remained far from medal range.
- The current goal is to identify one high-leverage next experiment, not to return to incremental v23/v5x short-context LoRA tweaks.

Official status re-check:
- `kaggle competitions submissions nvidia-nemotron-model-reasoning-challenge --page-size 10` confirms:
  - v59 ref `53376847`: `SubmissionStatus.COMPLETE`, public `0.67`.
  - v53 ref `53271130`: public `0.51`.
  - v23 ref `52492096`: public `0.54`.

Leaderboard re-check:
- Latest downloaded leaderboard:
  - `outputs/kaggle/leaderboard_probe_latest/nvidia-nemotron-model-reasoning-challenge.zip`
- Parsed snapshot:
  - `outputs/kaggle/leaderboard_probe_latest/latest_rank_snapshot.json`
- Note: the CSV includes one anomalous rank-0 row named `submission.zip`; ignore rows with `Rank <= 0` for rank/score-line calculations.
- Valid ranked teams: `3955`.
- Top public score: `0.89`.
- `guozhaojie` rank: `2489`.
- `guozhaojie` public score: `0.67`.
- Score `0.67` tie band:
  - starts at rank `2455`
  - ends at rank `2517`
  - `63` teams tied at `0.67`
- Approximate public score lines:
  - Top 10%: rank `395`, score `0.86`
  - Top 20%: rank `791`, score `0.86`
  - Top 30%: rank `1186`, score `0.86`
  - Top 40%: rank `1582`, score `0.85`
  - Top 50%: rank `1977`, score `0.84`

Structured research artifacts:
- Public baseline feature summary:
  - `outputs/kaggle/public_baseline_structured_research/baseline_feature_summary.json`
- v59 vs Mohamed replay log comparison:
  - `outputs/kaggle/public_baseline_structured_research/v59_vs_mohamed_replay_log_compare.json`
  - compact version: `outputs/kaggle/public_baseline_structured_research/v59_vs_mohamed_replay_compact.json`
- Mohamed public lightweight output probe:
  - `outputs/kaggle/public_replay_086_light_probe/nemotron-replay-data-0-86.log`
  - `outputs/kaggle/public_replay_086_light_probe/README.md`
  - `outputs/kaggle/public_replay_086_light_probe/replay_math_tokenized.jsonl`
- The lightweight probe intentionally used `kaggle kernels output --file-pattern '^(README\.md|replay_math_tokenized\.jsonl)$'` and did not download the large `submission.zip`.

Key public baseline studied:
- Kaggle notebook:
  - `mohamedamr992/nemotron-replay-data-0-86`
  - title: `Nemotron+Replay_Data 0.86`
- Metadata:
  - competition source: `nvidia-nemotron-model-reasoning-challenge`
  - machine: `NvidiaRtxPro6000`
  - model source: `metric/nemotron-3-nano-30b-a3b-bf16/Transformers/default/1`
  - datasets:
    - `huikang/huikang-nemotron-repository-snapshot`
    - `mayukh18/nemotron-packages`
    - `mohamedamr992/replay-math`
    - `llkh0a/rtx-wheels`

Mohamed public log evidence:
- GPU: `NVIDIA RTX PRO 6000 Blackwell Server Edition, sm_120`.
- Base target corpus: same as v59:
  - `7830` examples
  - `27,842,873` tokens
  - `26,568,807` unmasked tokens
- Replay preprocessing:
  - replay source rows: `17,570`
  - replay examples kept: `323`
  - total replay tokens in downloaded tokenized file: `2,042,567`
  - trainable replay answer tokens: `2,004,570`
  - min/max replay tokenized length: `409` / `8192`
- Mixed training corpus:
  - original target examples: `7830`
  - replay math examples: `323`
  - total examples after replay: `8153`
- Training:
  - `NUM_STEPS=1000` requested, clamped to `254` because `8153 // 32 = 254`.
  - batch size `32`, micro batch size `4`.
  - LR `3.5e-4`.
  - first step loss `0.430411`.
  - final step `254/254`: loss `0.001363`, grad norm `0.0140`, LR `1.38e-06`.
  - peak VRAM `96.8 GB`.
  - log confirms `Wrote submission.zip` and `Training complete.`

Direct v59 vs Mohamed comparison:
- v59:
  - Huikang token-level route.
  - `RESET_WEIGHTS=True`.
  - no replay math.
  - LR `2e-4`.
  - `7830` examples.
  - clamped to `244` steps.
  - peak VRAM `87.9 GB`.
  - official public score `0.67`.
- Mohamed:
  - Same Huikang token-level/cut-CE/MoE-tie/lm-head route.
  - `RESET_WEIGHTS=True`.
  - adds `323` long replay math examples.
  - LR `3.5e-4`.
  - `8153` mixed examples.
  - clamped to `254` steps.
  - peak VRAM `96.8 GB`.
  - public title claims `0.86`.

Root-cause hypothesis for v59 underperformance:
- Most likely: v59 was a fresh LoRA trained only on the Huikang repository-snapshot token corpus, which appears sufficient for a step-change from `0.54` to `0.67` but not for the dense `0.85-0.86` frontier.
- The advertised Huikang `LB 0.85` may correspond to the author's released output artifact or another state of their adapter lineage, not a robustly reproducible fresh run from the public notebook defaults.
- Evidence supporting this:
  - Local public `huikang_lb085/output/submission.zip` is a valid large LoRA artifact:
    - zip size `1,373,378,537` bytes
    - uncompressed `adapter_model.safetensors` size `4,259,063,848` bytes
    - SHA-256 `460db48efeec175bb793630fbba8a99052ba8fe7543b944f804057e237a075c4`
    - LoRA rank `32`
    - target modules include `lm_head`
  - Our byte-for-byte notebook rerun produced a valid submission and improved public score, but landed at `0.67`.
  - Other high-score public notebooks commonly either package released adapters or add extra data/training ingredients beyond the v59 fresh-run defaults.

Strategic classification:
- Best next training candidate:
  - v60 faithful reproduction of `mohamedamr992/nemotron-replay-data-0-86`.
  - Rationale: closest to v59 while adding one clear, logged, public ingredient: long replay-math data plus higher LR.
  - Expected Kaggle runtime: similar to Mohamed public log, about `3.8` hours wall-clock, with peak VRAM near `96.8 GB`.
  - Risk: close to RTX PRO 6000 memory ceiling; a small runtime/package variation could OOM.
- Useful but strategically different:
  - Directly submit or package a public output artifact such as Huikang's original `output/submission.zip`.
  - This may be rule-legal if the competition permits public notebook outputs as inputs, but it answers a different question from reproducible training and needs explicit user approval before any submission.
- Lower-priority training routes:
  - `dgxchen/training-with-unsloth-to-achieve-0-85-lb`: SFT/CoT route with optional pretrained adapter packaging; useful as backup, but less directly comparable to v59.
  - `pkuszboi/0-85-lb-training-with-muon`: Muon/SFT route; extracted for later study, but currently less clean than Mohamed as the immediate v60.

Cost-control recommendation:
- Do not pay yet.
- Try v60 Mohamed replay reproduction on Kaggle free GPU first, because the public notebook has already run successfully on `NvidiaRtxPro6000` and the only extra downloaded output needed for diagnosis is lightweight.
- Consider paid RTX PRO 6000-class compute only if Kaggle quota blocks the run or repeated Kaggle runtime/OOM failures prevent reproduction.

Execution policy for v60:
- Prepare a private faithful-copy kernel from `research/public_baselines/mohamed_replay_086/nemotron-replay-data-0-86.ipynb`.
- Metadata should point to a new private slug, for example `guozhaojie/nemotron-mohamed-replay-086-repro-v60`.
- Keep source datasets exactly as public metadata:
  - `huikang/huikang-nemotron-repository-snapshot`
  - `mayukh18/nemotron-packages`
  - `mohamedamr992/replay-math`
  - `llkh0a/rtx-wheels`
  - official base model
- Do not download the large `submission.zip` or submit automatically.
- First inspect logs and file listing.
- If complete, compare logs against the public Mohamed log:
  - replay examples kept `323`
  - trainable replay answer tokens about `2,004,570`
  - total mixed examples `8153`
  - training steps `254`
  - peak VRAM near `96.8 GB`
  - `Wrote submission.zip`
- Ask for explicit user approval before any official submission.

## v60 prepared: Mohamed replay 0.86 faithful reproduction, push blocked by weekly GPU quota (2026-06-06 CST)

Reason:
- v59 proved the public token-level route is directionally right but only reached public `0.67`.
- The most directly comparable public `0.86` candidate is `mohamedamr992/nemotron-replay-data-0-86`, which adds long replay-math data and uses LR `3.5e-4`.

Prepared files:
- Kernel directory:
  - `kaggle_kernel_v60_mohamed_replay_086_repro`
- Notebook:
  - `kaggle_kernel_v60_mohamed_replay_086_repro/nemotron-replay-data-0-86.ipynb`
- Metadata:
  - `kaggle_kernel_v60_mohamed_replay_086_repro/kernel-metadata.json`
- Push helper:
  - `scripts/push_v60_mohamed_replay_repro_when_quota_available.ps1`
- Preflight summary:
  - `outputs/kaggle/v60_mohamed_replay_repro_preflight_summary.json`
- Preflight checks:
  - `outputs/kaggle/v60_mohamed_replay_repro_preflight_checks.json`

Faithfulness:
- Notebook is a byte-for-byte copy of:
  - `research/public_baselines/mohamed_replay_086/nemotron-replay-data-0-86.ipynb`
- SHA-256:
  - `c522298245654832fe496eab2eee9f3dd21630b90c0667d9ec3afe789d8a5403`
- Only Kaggle metadata was changed to our private kernel slug:
  - `guozhaojie/nemotron-mohamed-replay-086-repro-v60`

Preflight:
- PASS.
- Metadata:
  - `is_private=true`
  - `enable_gpu=true`
  - title adjusted to `Nemotron Mohamed Replay 086 Repro v60` so the clean slug matches `nemotron-mohamed-replay-086-repro-v60`
  - `machine_shape=NvidiaRtxPro6000`
  - competition source: `nvidia-nemotron-model-reasoning-challenge`
  - model source: `metric/nemotron-3-nano-30b-a3b-bf16/Transformers/default/1`
  - datasets:
    - `huikang/huikang-nemotron-repository-snapshot`
    - `mayukh18/nemotron-packages`
    - `mohamedamr992/replay-math`
    - `llkh0a/rtx-wheels`
- Notebook checks:
  - no automatic competition submit detected
  - writes `submission.zip`
  - contains replay dataset path
  - `LEARNING_RATE = 3.5e-4`
  - `RESET_WEIGHTS=True`
  - `TARGET_REPLAY_ANSWER_TOKENS = 2_000_000`
  - uses `cut_cross_entropy.linear_cross_entropy`
  - uses `MOE_TIE_WEIGHTS=True`
  - includes `lm_head`

Push attempt:
- Command used:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v60_mohamed_replay_repro_when_quota_available.ps1`
- Result:
  - blocked by Kaggle weekly GPU quota:
    - `Maximum weekly GPU quota of 30.00 hours reached.`
- No run started.
- No artifact downloaded.
- No submission made.

Next action when quota recovers:
- Re-run:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v60_mohamed_replay_repro_when_quota_available.ps1`
- After successful push, monitor:
  - `kaggle kernels status guozhaojie/nemotron-mohamed-replay-086-repro-v60`
  - `kaggle kernels logs guozhaojie/nemotron-mohamed-replay-086-repro-v60`
- On completion, first capture only logs and file listing.
- Do not download the large `submission.zip` or submit without explicit user approval.

## v60 pushed: Mohamed replay 0.86 faithful reproduction started/pending on Kaggle (2026-06-07 CST)

Push:
- Quota recovered enough for push.
- Command used:
  - `powershell -ExecutionPolicy Bypass -File scripts/push_v60_mohamed_replay_repro_when_quota_available.ps1`
- Result:
  - `Kernel version 1 successfully pushed`.
- Kernel URL:
  - `https://www.kaggle.com/code/guozhaojie/nemotron-mohamed-replay-086-repro-v60`

Immediate Kaggle API state:
- `kaggle kernels pull guozhaojie/nemotron-mohamed-replay-086-repro-v60 -p outputs\kaggle\v60_pull_probe -m` succeeded, confirming the private kernel exists.
- `kaggle kernels list --mine --page-size 100 -v` shows:
  - `guozhaojie/nemotron-mohamed-replay-086-repro-v60`
  - title `Nemotron Mohamed Replay 086 Repro v60`
  - last update `2026-06-06 16:27:49.103000` UTC
- `kaggle kernels status` returned Kaggle `500 Internal Server Error` immediately after push.
- `kaggle kernels logs` returned empty immediately after push.

Monitoring policy:
- Treat the kernel as pushed but not yet log-confirmed.
- Continue polling status/logs.
- Expected successful run evidence should match the public Mohamed log:
  - replay examples kept `323`
  - trainable replay answer tokens about `2,004,570`
  - total mixed examples `8153`
  - training steps `254`
  - peak VRAM near `96.8 GB`
  - `Wrote submission.zip`
- Do not download large `submission.zip`.
- Do not submit without explicit user approval.

## v60 completed: faithful Mohamed replay reproduction matches public 0.86 log signatures (2026-06-08 CST)

Result:
- Kernel:
  - `guozhaojie/nemotron-mohamed-replay-086-repro-v60`
- Version:
  - `1`
- Status:
  - `kaggle kernels status` still returns Kaggle `500 Internal Server Error`, but logs and file listing confirm completion.
- Lightweight log captured:
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/nemotron-mohamed-replay-086-repro-v60.log`
- File listing captured:
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/nemotron-mohamed-replay-086-repro-v60.files.txt`
- Lightweight output captured:
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/README.md`
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/replay_math_tokenized.jsonl`
- Log summary:
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/v60_log_summary.json`
- Submit decision:
  - `outputs/kaggle/v60_mohamed_replay_repro_output_probe/v60_submit_decision.json`

Output files on Kaggle:
- `README.md`
- `replay_math_tokenized.jsonl`
- `submission.zip`

Training evidence:
- GPU:
  - `NVIDIA RTX PRO 6000 Blackwell Server Edition, sm_120`
- Replay source rows:
  - `17,570`
- Replay preprocessing:
  - replay examples kept: `323`
  - trainable replay answer tokens: `2,004,570`
  - v60 `replay_math_tokenized.jsonl` size: `18,716,314` bytes
  - v60 `replay_math_tokenized.jsonl` SHA-256: `4bd68d54d2feeaa7b1a0e1c8f3acb716287f0d01e09127d9e7559bb0d2a07f49`
  - public Mohamed probe replay file SHA-256: same (`4bd68d54d2feeaa7b1a0e1c8f3acb716287f0d01e09127d9e7559bb0d2a07f49`)
- Base target corpus:
  - `7830` examples
  - `27,842,873` tokens
  - `26,568,807` unmasked tokens
- Mixed corpus:
  - original target examples: `7830`
  - replay math examples: `323`
  - total examples after replay: `8153`
- Training:
  - `254` steps
  - batch size `32`
  - micro batch size `4`
  - LR `0.00035`
  - final step `254/254`: loss `0.001310`, grad norm `0.0241`, LR `1.38e-06`
  - peak VRAM `96.8 GB`
- Log confirms:
  - `Training complete. Peak VRAM: 96.8 GB`
  - `Wrote submission.zip`
  - `Training complete.`

Reference comparison:
- All public Mohamed reference checks passed:
  - `total_rows=17570`
  - `replay_kept=323`
  - `trainable_replay_answer_tokens=2004570`
  - `loaded_examples=7830`
  - `original_target_examples=7830`
  - `replay_math_examples=323`
  - `total_after_replay=8153`
  - `training.steps=254`
  - `peak_vram=96.8`
  - final logged step is `254/254`
  - `Wrote submission.zip`

Submission decision:
- Strongest current candidate to beat v59 public `0.67`.
- This is a faithful reproduction of the public Mohamed replay `0.86` route and matches the public run's log signatures.
- Still no guarantee of public score because v59 also underperformed its public title, but v60 is materially closer to a known `0.86` public route than v59.
- Do not download the large `submission.zip` unless required by Kaggle submission mechanics.
- Do not submit without explicit user approval.

## v60 official submission pending (2026-06-08 CST)

Decision:
- User explicitly approved submitting v60.

Submission:
- Command script:
  - `scripts/submit_v60_mohamed_replay_repro_official.ps1`
- Competition:
  - `nvidia-nemotron-model-reasoning-challenge`
- Kernel:
  - `guozhaojie/nemotron-mohamed-replay-086-repro-v60`
- Kernel version:
  - `1`
- Output file:
  - `submission.zip`
- Description:
  - `v60 official faithful Mohamed replay 0.86 public baseline repro`
- Submission ref:
  - `53479353`
- Status immediately after submission:
  - `SubmissionStatus.PENDING`
- Public score:
  - pending

Comparison target:
- Current official best before v60:
  - v59 public score `0.67`
  - ref `53376847`
- Previous:
  - v23 public score `0.54`
  - v53 public score `0.51`

Next action:
- Monitor ref `53479353` until scoring completes.
- Record public score and leaderboard impact when complete.

Official public result:
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.84`.
- Previous official best v59 public score: `0.67`.
- Delta vs v59: `+0.17`.
- Delta vs v23 public score `0.54`: `+0.30`.

Leaderboard snapshot after v60 (2026-06-09 CST):
- Latest downloaded leaderboard:
  - `outputs/kaggle/leaderboard_probe_latest/nvidia-nemotron-model-reasoning-challenge.zip`
- Parsed snapshot:
  - `outputs/kaggle/leaderboard_probe_latest/v60_rank_snapshot.json`
  - `outputs/kaggle/leaderboard_probe_latest/latest_rank_snapshot.json`
- Valid ranked teams: `4075`.
- Top public score: `0.89`.
- `guozhaojie` rank: `2080`.
- `guozhaojie` public score: `0.84`.
- Score `0.84` rank band:
  - starts at rank `1959`
  - ends at rank `2209`
  - `251` teams tied at `0.84`
- Public score bands:
  - score `0.86`: ranks `24` through `1453`, `1430` teams
  - score `0.85`: ranks `1454` through `1958`, `505` teams
  - score `0.84`: ranks `1959` through `2209`, `251` teams
- Approximate public percentile lines:
  - Top 10%: rank `407`, score `0.86`
  - Top 20%: rank `815`, score `0.86`
  - Top 30%: rank `1222`, score `0.86`
  - Top 40%: rank `1630`, score `0.85`
  - Top 50%: rank `2037`, score `0.84`

Interpretation:
- v60 confirms that the public Mohamed replay route transferred much better than v59 and is now the official best.
- It still lands below the dense `0.85-0.86` frontier. Public bronze/top-10%-style territory appears to require at least `0.86` on the current public leaderboard.
- The remaining useful work should focus on finding or reproducing a route that moves from `0.84` to `0.86`, not on small local-only tweaks.


## v61 completed: public Kienngx Tinker adapter artifact packaged successfully (2026-06-09 08:41 CST)

Route:
- Public artifact path: `kienngx/nemotron-nano-30b-trained/Triton/tinker-adapter/1`.
- Public guide reproduced from: `afr1ste/nemotron-0-86-tinker-adapter-guide`.
- Private kernel: `guozhaojie/nemotron-kienngx-tinker-adapter-v61`.
- Kernel version: `1`.
- This route performs no SFT/training; it packages an already-converted public Tinker adapter artifact into the required LoRA `submission.zip` format.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v61_kienngx_tinker_adapter_repro_output_probe/nemotron-kienngx-tinker-adapter-v61.log`.
- File listing: `outputs/kaggle/v61_kienngx_tinker_adapter_repro_output_probe/nemotron-kienngx-tinker-adapter-v61.files.txt`.
- Submit decision JSON: `outputs/kaggle/v61_kienngx_tinker_adapter_repro_output_probe/v61_submit_decision.json`.

Validation evidence from log:
- Selected adapter dir: `/kaggle/input/models/kienngx/nemotron-nano-30b-trained/triton/tinker-adapter/1`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, `lora_dropout=0.0`, `task_type=CAUSAL_LM`.
- Target modules include `down_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`.
- Tensor count: `12010`.
- Adapter size: `3.31 GiB`.
- `submission.zip` size: `3.046 GiB`.
- Zip root files: `adapter_config.json`, `adapter_model.safetensors`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Recommended asking user approval and submitting v61 as the next official probe.
- Rationale: v60 public Mohamed replay route scored `0.84`; current public leaderboard top-10%/medal-like line is around `0.86`. v61 is the cleanest available public artifact/adapter path toward the dense `0.86` band and avoids further small SFT guessing.
- Do not download the large `submission.zip` unless required by Kaggle mechanics.
- Prepared submit script: `scripts/submit_v61_kienngx_tinker_adapter_official.ps1`.

## v61 official submission pending (2026-06-09 08:50 CST)

Decision:
- User explicitly approved submitting v61 after reviewing the completed public Kienngx Tinker adapter artifact package.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-kienngx-tinker-adapter-v61`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v61 official public Kienngx Tinker adapter artifact repro`.
- Submission ref: `53490698`.
- Status after repeated checks: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v61: v60 public score `0.84`, rank snapshot `2080 / 4075`.
- Current important score band: `0.86` ranks `24-1453`; public top-10%-style line is around `0.86`.

Next action:
- Monitor ref `53490698` until scoring completes.
- Record public score and leaderboard impact when complete.

## v61 official result: Kienngx Tinker adapter artifact improved to 0.85 (2026-06-09 CST)

Official result:
- Submission ref: `53490698`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.85`.
- Previous best: v60 public score `0.84`.
- Delta vs v60: `+0.01`.
- Delta vs v59: `+0.18`.
- Delta vs v23: `+0.31`.

Leaderboard snapshot after v61:
- Snapshot: `outputs/kaggle/leaderboard_probe_current/v61_rank_snapshot.json`.
- Valid ranked teams: `4080`.
- Rank: `1778 / 4080`.
- Score band `0.85`: ranks `1461-1965`, `505` teams.
- Score band `0.86`: ranks `24-1460`, `1437` teams.
- Top-10%-style line remains around `0.86`.

Interpretation:
- The public Tinker artifact route is directionally correct and improved the official best from `0.84` to `0.85`.
- It still misses the dense `0.86` band by `0.01`; repeating simple Tinker packaging variants is unlikely to move materially.

Next high-priority direction:
- Candidate: `kuangyicheng/nemotron-087-training`.
- Why: public notebook starts from the Kienngx Tinker adapter and performs a conservative 28-step continuation (`LEARNING_RATE=1.4e-6`, `POST_TRAIN_DELTA_SCALE=0.48`, `IN_PROJ_ONLY=True`, `ORIGINAL_PROBLEMS_ONLY=True`).
- Public log evidence: `Training complete. Peak VRAM: 71.9 GB`, `Wrote submission.zip`, `Submission validation OK: root files only, rank=32, alpha=32`.
- Cost/risk: consumes one RTX PRO 6000 Kaggle GPU run, about 24 minutes in public log. This is a better use of quota than more small local SFT guesses because it is a public strong continuation route from our current best adapter family.

## v62 completed: Mirza public 0.86 adapter artifact relay validated (2026-06-09 CST)

Route:
- Public source notebook: `mirzayasirabdullah07/best-nvidia-nemotron-0-86`.
- Private relay kernel: `guozhaojie/nemotron-mirza-artifact-relay-v62`.
- Successful kernel version: `2`.
- This route does not train and does not download the large artifact locally; it uses the public notebook output as a Kaggle kernel source and copies `submission.zip` inside Kaggle.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v62_mirza_public_artifact_relay_output_probe/nemotron-mirza-artifact-relay-v62.log`.
- File listing: `outputs/kaggle/v62_mirza_public_artifact_relay_output_probe/nemotron-mirza-artifact-relay-v62.files.txt`.
- Submit decision JSON: `outputs/kaggle/v62_mirza_public_artifact_relay_output_probe/v62_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/mirzayasirabdullah07/best-nvidia-nemotron-0-86/submission.zip`.
- Source zip bytes: `3824587714`.
- Zip root files: `adapter_config.json`, `adapter_model.safetensors`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, `lora_dropout=0.0`, `task_type=CAUSAL_LM`.
- Target modules include `up_proj`, `in_proj`, `gate_proj`, `out_proj`, `k_proj`, `o_proj`, `v_proj`, `q_proj`, `lm_head`, `down_proj`.
- Adapter model size: `3.967 GiB`.
- Zip size: `3.562 GiB`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Recommend asking user approval and submitting v62 next.
- Rationale: v61 already measured Kienngx Tinker at `0.85`; v62 is a distinct public artifact from a notebook titled `0.86`, with a different adapter shape/config (`lora_alpha=64`, includes `gate_proj`, larger adapter). This is the best low-cost chance to move from `0.85` into the `0.86` band before spending GPU on continuation training.
- Prepared but not run without approval: `scripts/submit_v62_mirza_public_artifact_relay_official.ps1`.

## v62 official submission pending (2026-06-10 CST)

Decision:
- User explicitly approved submitting v62 after reviewing the validated public Mirza artifact relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-mirza-artifact-relay-v62`.
- Kernel version: `2`.
- Output file: `submission.zip`.
- Description: `v62 official public Mirza adapter artifact relay`.
- Submission ref: `53510385`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v62: v61 public score `0.85`, rank `1778 / 4080`.
- Key next score band: `0.86`, ranks `24-1460` in the latest snapshot.

Next action:
- Monitor ref `53510385` until scoring completes.
- Record public score and leaderboard impact when complete.

## v62 official result: Mirza public artifact reached 0.86 (2026-06-10 CST)

Official result:
- Submission ref: `53510385`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.
- Previous official best: v61 public score `0.85`.
- Delta vs v61: `+0.01`.
- Delta vs v60: `+0.02`.
- Delta vs v23: `+0.32`.

Leaderboard snapshot after v62:
- Snapshot: `outputs/kaggle/leaderboard_probe_after_v62/v62_rank_snapshot.json`.
- Valid ranked teams: `4118`.
- Rank: `453 / 4118`.
- Score band `0.86`: ranks `28-1486`, `1459` teams.
- Score band `0.87`: ranks `5-27`, `23` teams.
- Top-10%-style line: rank `412`, score `0.86`.

Interpretation:
- v62 successfully moved the team into the key `0.86` public score band.
- Current rank `453` is just outside the top-10%-style line by about `41` ranks in the latest public snapshot.
- Because the `0.86` band is very dense and tie handling/final private scoring can shift placement, this is a real medal-contending public score but not a locked result.

Next high-priority direction:
- Preserve v62 as the current official best.
- If using more quota/submissions, prioritize a public strong continuation route such as `kuangyicheng/nemotron-087-training` over simple adapter repackaging, because simple public artifact routing has now reached the known `0.86` plateau.

## v63 completed: Kuang public 0.87 training output relay validated (2026-06-10 CST)

Route:
- Public source notebook: `kuangyicheng/nemotron-087-training`.
- Private relay kernel: `guozhaojie/nemotron-kuang-087-relay-v63`.
- Successful kernel version: `2`.
- This route does not spend GPU and does not download the large artifact locally; it uses the public notebook output as a Kaggle kernel source and copies `submission.zip` inside Kaggle.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v63_kuang_087_public_output_relay_probe/nemotron-kuang-087-relay-v63.log`.
- File listing: `outputs/kaggle/v63_kuang_087_public_output_relay_probe/nemotron-kuang-087-relay-v63.files.txt`.
- Submit decision JSON: `outputs/kaggle/v63_kuang_087_public_output_relay_probe/v63_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/kuangyicheng/nemotron-087-training/submission.zip`.
- Source zip bytes: `1373362678`.
- Zip root files: `adapter_model.safetensors`, `adapter_config.json`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, `lora_dropout=0.0`, `task_type=CAUSAL_LM`.
- Target modules include `out_proj`, `down_proj`, `v_proj`, `q_proj`, `up_proj`, `in_proj`, `lm_head`, `o_proj`, `k_proj`.
- Adapter model uncompressed size: `3.967 GiB`.
- Zip compressed size: `1.279 GiB`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Recommend asking user approval and submitting v63 next.
- Rationale: v62 is the current best at `0.86` and rank `453 / 4118`; v63 relays a public notebook titled/tracked as `0.87` continuation training and is a distinct output from the Kienngx Tinker and Mirza artifact routes.
- Prepared but not run without approval: `scripts/submit_v63_kuang_087_public_output_relay_official.ps1`.

## v64 prepared: faithful Kuang 0.87 training rerun standby (2026-06-10 CST)

Prepared only; not pushed or run:
- Private kernel directory: `kaggle_kernel_v64_kuang_087_training_repro`.
- Private kernel id: `guozhaojie/nemotron-kuang-087-training-v64`.
- Source notebook: `research/public_baselines/kuangyicheng_087_training/nemotron-087-training.ipynb`.
- Push script: `scripts/push_v64_kuang_087_training_repro.ps1`.

Purpose:
- Faithful private rerun of `kuangyicheng/nemotron-087-training` if v63 public output relay does not improve enough or if we need our own private generated artifact.

Important:
- Do not run v64 without explicit user approval because pushing the kernel starts a GPU run on `NvidiaRtxPro6000`.
- Public reference log suggests about 24 minutes and peak VRAM about `71.9 GB`.

## v63 official submission pending (2026-06-10 CST)

Decision:
- User explicitly approved submitting v63 after reviewing the validated public Kuang 0.87 training output relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-kuang-087-relay-v63`.
- Kernel version: `2`.
- Output file: `submission.zip`.
- Description: `v63 official public Kuang 087 training output relay`.
- Submission ref: `53518679`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v63: v62 public score `0.86`, rank `453 / 4118`.
- v64 faithful rerun remains prepared but not pushed or run, because it consumes GPU quota.

Next action:
- Monitor ref `53518679` until scoring completes.
- Record public score and leaderboard impact when complete.

## v63 official result: Kuang public output relay underperformed at 0.84 (2026-06-10 CST)

Official result:
- Submission ref: `53518679`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.84`.
- Current official best remains v62 public score `0.86`.
- Delta vs v62: `-0.02`.
- Delta vs v61: `-0.01`.
- Same public score as v60: `0.84`.

Interpretation:
- The public `kuangyicheng/nemotron-087-training` output relay did not transfer as advertised; the direct public output scored `0.84` for our official submission.
- Do not submit or prefer v63 over v62.
- Because v63 relayed the public output exactly, the expected value of running v64 faithful rerun is lower than before; v64 may still produce a different stochastic artifact but should be treated as a GPU-costly speculative rerun, not a clear next best.

Next action:
- Preserve v62 as current best (`0.86`).
- Reassess next candidates before spending GPU on v64.

## v65 completed: Hammad 0.87 SVD clean relay validated (2026-06-10 CST)

Route:
- Public source notebook: `hammadfarooq470/agi-for-medal-0-87`.
- Related public relay notebook: `cocoaai/nvidia-nemotron-huikang-0-87-svd-submit`.
- Private clean relay kernel: `guozhaojie/nemotron-hammad-087-svd-clean-relay-v65`.
- Kernel version: `1`.
- This route does not train and does not download the large artifact locally. It mounts the public Hammad output and repackages only the required root files into a clean `submission.zip`.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v65_hammad_087_svd_clean_relay_probe/nemotron-hammad-087-svd-clean-relay-v65.log`.
- File listing: `outputs/kaggle/v65_hammad_087_svd_clean_relay_probe/nemotron-hammad-087-svd-clean-relay-v65.files.txt`.
- Submit decision JSON: `outputs/kaggle/v65_hammad_087_svd_clean_relay_probe/v65_submit_decision.json`.

Validation evidence from log:
- Selected source adapter dir: `/kaggle/input/notebooks/hammadfarooq470/agi-for-medal-0-87/adapter_candidates/block_topk_floor4_model`.
- Source adapter model bytes: `3,548,166,840`.
- Source adapter config bytes: `904`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output zip bytes: `3,269,556,838`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules include `down_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Recommend asking user approval and submitting v65 next.
- Rationale: v62 remains the current official best at `0.86`; v65 is a distinct Huikang-v20 SVD/block-topk route advertised publicly as `0.87`, with a clean validated relay and no GPU cost. It is more strategically meaningful than another small private SFT guess.
- Risk: public title is not proof; v63 showed a public `0.87`-labeled route can score only `0.84` officially. v65 should be treated as a high-value public-probe submission, not guaranteed improvement.
- Prepared but not run without explicit approval: `scripts/submit_v65_hammad_087_svd_clean_relay_official.ps1`.

## Public candidate search after v65 (2026-06-10 CST)

High-priority candidates found:
- `biohack44/nemotron-v62-d3-sparse-trust-finisher-attack`: public GPU finisher route, starts from Kienngx Tinker adapter, runs 14 SFT steps plus sparse-trust blend, log says `READY TO SUBMIT`, output size about `3.05 GiB`. Interesting but unproven against v62; consider relay/official probe only after v65 decision.
- `paritoshtripathi5/nvidia-nemotron-svd`: CPU SVD denoise of Kienngx public submission, output `submission.zip`; code uses `keep_ratio=0.01`, which is very aggressive and may degrade, so lower priority.
- `dedquoc/nvidia-nmrc-low-rank-svd-lora-adapter-fusion`: Huikang adapter conversion via `tinker_cookbook.weights.build_lora_adapter` with patched SVD compression; likely related to Hammad/SVD family but lower priority than v65 because v65 is cleaner and explicitly advertised as 0.87.
- `lopure/lora-adapter-ensembling-experiments`: multi-adapter TIES/SVD experiment with `ties_submission.zip`; code is complex and log lacks clear submission validation, so keep as later research.

Low-priority / not currently recommended:
- `wethepeople918/nemotronallspark`: recent/high-vote notebook, but pulled log fails in offline/HF fallback path and no clear `submission.zip` evidence in the first file page.
- `ayomide2000/finding-nemo`: log fails with missing `/kaggle/working/adapter_model.safetensors`; do not prioritize.
- `bbobwayne/nemotron-tier-2-unsloth-lora-r-32`: very long GPU training route; not a short-turn public artifact relay. Keep only as background.

## v66 pushed: Biohack D3 sparse clean relay pending (2026-06-10 CST)

Prepared/pushed private relay:
- Private clean relay kernel: `guozhaojie/nemotron-biohack-d3-sparse-clean-relay-v66`.
- Kernel version: `1`.
- Public source notebook: `biohack44/nemotron-v62-d3-sparse-trust-finisher-attack`.
- Purpose: validate the public Biohack D3 Sparse-Trust Finisher output as a clean root-only `submission.zip` without downloading the large adapter locally.
- This relay uses no GPU and makes no official submission.

Initial status:
- Push succeeded after one Kaggle API SSL EOF retry.
- First status: `KernelWorkerStatus.RUNNING`.
- Initial logs/files were empty while the relay was starting or repackaging the large adapter.

Decision policy:
- Do not submit v66 without explicit user approval.
- v65 remains the higher-priority next official probe unless v66 validates and we decide the sparse finisher has a better expected value than the Hammad 0.87 SVD route.

## v66 completed: Biohack D3 sparse clean relay validated (2026-06-10 CST)

Route:
- Public source notebook: `biohack44/nemotron-v62-d3-sparse-trust-finisher-attack`.
- Private clean relay kernel: `guozhaojie/nemotron-biohack-d3-sparse-clean-relay-v66`.
- Kernel version: `1`.
- This route does not train and does not download the large artifact locally. It mounts the public Biohack output and repackages only the required root files into a clean `submission.zip`.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v66_biohack_d3_sparse_clean_relay_probe/nemotron-biohack-d3-sparse-clean-relay-v66.log`.
- File listing: `outputs/kaggle/v66_biohack_d3_sparse_clean_relay_probe/nemotron-biohack-d3-sparse-clean-relay-v66.files.txt`.
- Submit decision JSON: `outputs/kaggle/v66_biohack_d3_sparse_clean_relay_probe/v66_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/biohack44/nemotron-v62-d3-sparse-trust-finisher-attack/submission.zip`.
- Source zip bytes: `3,275,891,371`.
- Source zip already has only `adapter_config.json`, `adapter_model.safetensors`.
- Extracted adapter model bytes: `3,554,384,888`.
- Extracted adapter config bytes: `2,315`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output zip bytes: `3,286,074,885`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules include `down_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Treat v66 as the second official-probe candidate after v65, not the first.
- Rationale: Biohack v66 is distinct from v65 and includes a sparse finisher on top of Kienngx Tinker, but it starts from the already measured Kienngx family (`v61=0.85`) and has no public score claim as direct as Hammad/Cocoa `0.87`.
- Risk: It may overfit public/train families or degrade v62's stronger Mirza adapter; submit only if we want a second exploratory official probe after v65.
- Prepared but not run without explicit approval: `scripts/submit_v66_biohack_d3_sparse_clean_relay_official.ps1`.

## v65 official submission pending (2026-06-10 CST)

Decision:
- User explicitly approved submitting v65 after reviewing the validated Hammad 0.87 SVD clean relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-hammad-087-svd-clean-relay-v65`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v65 official public Hammad 087 SVD clean relay`.
- Submission ref: `53536595`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v65 remains v62 public score `0.86`.
- v66 Biohack clean relay is validated but not submitted; hold it as the next exploratory candidate until v65 score is known.

Next action:
- Monitor ref `53536595` until scoring completes.
- Record public score and leaderboard impact when complete.

## v65 official result: Hammad 0.87 SVD clean relay scored 0.85 (2026-06-10 CST)

Official result:
- Submission ref: `53536595`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.85`.
- Current official best remains v62 public score `0.86`.
- Delta vs v62: `-0.01`.
- Same public score as v61 Kienngx Tinker: `0.85`.
- Better than v63 Kuang public output relay: `+0.01`.

Interpretation:
- The Hammad/Cocoa public `0.87` SVD route did not transfer to our official submission as 0.87; it landed at the `0.85` band.
- This confirms again that public notebook titles/claims are unreliable without official submission evidence.
- Preserve v62 as the current best official submission (`0.86`).

Next action:
- Do not prefer v65 over v62.
- v66 Biohack D3 sparse clean relay remains validated and unsubmitted as a second exploratory candidate, but it starts from the Kienngx family and should be treated as risky.

## Current leaderboard and v67 Habanwer ATLAS relay status (2026-06-11 CST)

Leaderboard snapshot:
- Snapshot: `outputs/kaggle/leaderboard_probe_20260611_now/latest_rank_snapshot.json`.
- Valid ranked teams: `4164`.
- Current official best remains v62 public score `0.86`.
- Current rank: `457 / 4164`.
- Top-10%-style line: rank `417`, score `0.86`.
- Gap to top-10%-style line: about `40` ranks.
- Score band `0.86`: ranks `34-1523`, `1490` teams.
- Score band `0.87`: ranks `5-33`, `29` teams.

Interpretation:
- v62 is medal-contending but not medal-safe because the `0.86` band is extremely dense.
- A true `0.87` artifact would likely move the team into a much safer medal zone; another `0.85`/`0.84` public-title route will not help.

v67 candidate:
- Public source notebook: `habanwer/nemotron-atlas`.
- Private clean relay kernel: `guozhaojie/nemotron-habanwer-atlas-clean-relay-v67`.
- Prepared files:
  - `kaggle_kernel_v67_habanwer_atlas_clean_relay/`.
  - `scripts/push_v67_habanwer_atlas_clean_relay.ps1`.
  - `scripts/submit_v67_habanwer_atlas_clean_relay_official.ps1`.
- This route does not train and does not download the large artifact locally. It mounts the public Habanwer ATLAS output and repackages only root `adapter_config.json` and `adapter_model.safetensors`.

v67 version 1:
- Status: `KernelWorkerStatus.ERROR`.
- Failure reason: relay validation was too strict about `base_model_name_or_path`.
- Source config used `/kaggle/input/models/metric/nemotron-3-nano-30b-a3b-bf16/transformers/default/1`, which is the Kaggle local path for the same Nemotron base, while the relay originally required exact `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Source zip evidence before failure:
  - Selected source zip: `/kaggle/input/notebooks/habanwer/nemotron-atlas/submission.zip`.
  - Source zip bytes: `3,261,412,604`.
  - Source zip entries: `adapter_config.json`, `adapter_model.safetensors`.
  - Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, target modules include ATLAS regex with attention/Mamba/shared/routed expert projections.

v67 version 2:
- Patch: relaxed base-model validation to accept the canonical Nemotron name and Kaggle local model paths containing `metric/nemotron-3-nano-30b-a3b-bf16` / `nemotron-3-nano-30b-a3b-bf16`.
- Push result: kernel version `2` successfully pushed.
- Current status at last check: `KernelWorkerStatus.RUNNING`.
- Logs/files are still empty while the kernel is processing the large zip.
- Do not submit v67 officially unless version 2 completes cleanly and the user explicitly approves.

Next action:
- Continue monitoring v67 version 2 until it is `COMPLETE` or `ERROR`.
- If complete, capture lightweight logs and file listing, verify root-only zip/config, then decide whether it is worth official submission compared with v62 `0.86` and validated-but-unsubmitted v66.

## v67 completed: Habanwer ATLAS clean relay validated (2026-06-11 CST)

Route:
- Public source notebook: `habanwer/nemotron-atlas`.
- Private clean relay kernel: `guozhaojie/nemotron-habanwer-atlas-clean-relay-v67`.
- Successful kernel version: `2`.
- This route does not train and does not download the large artifact locally. It mounts the public Habanwer ATLAS output and repackages only the required root files into a clean `submission.zip`.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v67_habanwer_atlas_clean_relay_probe/nemotron-habanwer-atlas-clean-relay-v67.log`.
- File listing: `outputs/kaggle/v67_habanwer_atlas_clean_relay_probe/nemotron-habanwer-atlas-clean-relay-v67.files.txt`.
- Submit decision JSON: `outputs/kaggle/v67_habanwer_atlas_clean_relay_probe/v67_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/habanwer/nemotron-atlas/submission.zip`.
- Source zip bytes: `3,261,412,604`.
- Source zip entries: `adapter_config.json`, `adapter_model.safetensors`.
- Extracted adapter model bytes: `3,537,299,144`.
- Extracted adapter config bytes: `1,171`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output zip bytes: `3,272,049,536`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, base model path `/kaggle/input/models/metric/nemotron-3-nano-30b-a3b-bf16/transformers/default/1`.
- Target modules are ATLAS regex covering attention/Mamba/shared/routed expert projections: `in_proj`, `out_proj`, `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`, `shared_experts`, and routed `experts` projections.
- Log confirms: `Ready for Kaggle submission.`

Fix applied:
- v67 version 1 failed because the relay required exact base string `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- v67 version 2 relaxed validation to accept the canonical Nemotron name and Kaggle local model paths containing `metric/nemotron-3-nano-30b-a3b-bf16` / `nemotron-3-nano-30b-a3b-bf16`.
- Official submit script was updated to use kernel version `2`: `scripts/submit_v67_habanwer_atlas_clean_relay_official.ps1`.

Submission recommendation:
- Recommend official submission if the user approves an exploratory high-value probe.
- Rationale: v62 remains current best at public `0.86`, but the team is only about `40` ranks outside the top-10%-style line and needs a true `0.87` or favorable tie/private shift. v67 is a distinct ATLAS-trained route with a real 3.1h GPU public training log and validated 3.27GB root-only adapter package, so it is a better late-stage probe than another small SFT guess.
- Risk: v63 and v65 showed that public `0.87`-style routes can underperform (`0.84`/`0.85`), so v67 is not guaranteed to beat v62. Do not submit without explicit user approval.

Next action:
- If user approves, run `scripts/submit_v67_habanwer_atlas_clean_relay_official.ps1` and monitor the new submission ref until public score completes.
- If user does not approve yet, keep v67 as validated standby and continue looking for another independent `0.87+` artifact.

## v68 completed: VNG Refine nested clean relay validated (2026-06-11 CST)

Route:
- Public source notebook: `vngnguynhuy/refine`.
- Private clean relay kernel: `guozhaojie/nemotron-vng-refine-clean-relay-v68`.
- Successful kernel version: `1`.
- This route does not train and does not download the large artifact locally. It fixes the public notebook's nested `submission.zip` layout by extracting the adapter files and repackaging them at the zip root.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v68_vng_refine_clean_relay_probe/nemotron-vng-refine-clean-relay-v68.log`.
- File listing: `outputs/kaggle/v68_vng_refine_clean_relay_probe/nemotron-vng-refine-clean-relay-v68.files.txt`.
- Submit decision JSON: `outputs/kaggle/v68_vng_refine_clean_relay_probe/v68_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/vngnguynhuy/refine/submission.zip`.
- Source zip bytes: `3,268,303,412`.
- Source zip entries were nested under `kaggle/working/nemotron-adapter-ready-to-submit/`.
- Selected nested adapter prefix: `kaggle/working/nemotron-adapter-ready-to-submit/`.
- Extracted adapter model bytes: `3,554,384,888`.
- Extracted adapter config bytes: `581`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output zip bytes: `3,280,489,218`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules include `down_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`.
- Log confirms: `Ready for Kaggle submission.`

Submission recommendation:
- Keep v68 as a validated exploratory backup, but lower priority than v67.
- Rationale: v68 fixes a real packaging defect in a public high-vote route, so it might score differently from the raw public notebook output. However, it appears close to the SVD/finisher family that has already underperformed in v65 (`0.85`) and may not beat v62 (`0.86`).
- Do not submit without explicit user approval.

## v69 completed: Mirza competition clean relay validated but likely duplicate of v62 (2026-06-11 CST)

Route:
- Public source notebook: `mirzayasirabdullah07/nvidia-nemotron-competition`.
- Private clean relay kernel: `guozhaojie/nemotron-mirza-competition-clean-relay-v69`.
- Successful kernel version: `1`.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v69_mirza_competition_clean_relay_probe/nemotron-mirza-competition-clean-relay-v69.log`.
- File listing: `outputs/kaggle/v69_mirza_competition_clean_relay_probe/nemotron-mirza-competition-clean-relay-v69.files.txt`.
- Submit decision JSON: `outputs/kaggle/v69_mirza_competition_clean_relay_probe/v69_submit_decision.json`.

Validation evidence from log:
- Selected source zip: `/kaggle/input/notebooks/mirzayasirabdullah07/nvidia-nemotron-competition/submission.zip`.
- Source zip bytes: `3,824,587,714`.
- Source zip entries: `adapter_config.json`, `adapter_model.safetensors`.
- Extracted adapter model bytes: `4,259,063,856`.
- Extracted adapter config bytes: `1,323`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output zip bytes: `3,840,972,555`.
- Config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules include `up_proj`, `in_proj`, `gate_proj`, `out_proj`, `k_proj`, `o_proj`, `v_proj`, `q_proj`, `lm_head`, `down_proj`.
- Log confirms: `Ready for Kaggle submission.`

Duplicate assessment:
- v69 source zip bytes exactly match v62 source zip bytes: `3,824,587,714`.
- v69 config shape also matches v62: `r=32`, `lora_alpha=64`, includes `gate_proj`, large 4.259GB adapter.
- Therefore v69 is almost certainly the same Mirza artifact as current best v62 (`0.86`) through a different public notebook wrapper.

Submission recommendation:
- Do not submit v69 unless a later binary diff proves it differs from v62.
- Expected value is low because it likely reproduces v62 and wastes an official submission.

Current late-stage submission priority after v68/v69 validation:
1. v67 Habanwer ATLAS clean relay: highest-value non-duplicate exploratory probe.
2. v68 VNG Refine clean relay: validated backup, but likely SVD/finisher-family risk.
3. v66 Biohack D3 sparse clean relay: validated backup, but likely Kienngx-family risk.
4. v69 Mirza competition clean relay: do not submit, likely duplicate of v62.

## v67 official submission pending (2026-06-11 CST)

Decision:
- User explicitly approved submitting v67 after reviewing the validated Habanwer ATLAS clean relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-habanwer-atlas-clean-relay-v67`.
- Kernel version: `2`.
- Output file: `submission.zip`.
- Description: `v67 official public Habanwer ATLAS clean relay`.
- Submission ref: `53572937`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v67 remains v62 public score `0.86`.
- Latest known rank snapshot before v67: `457 / 4164`, about `40` ranks outside the top-10%-style line.

Next action:
- Monitor ref `53572937` until scoring completes.
- Record public score and decide whether v68 is worth the next official probe.

## v67 score monitoring note (2026-06-11 CST)

Submission ref `53572937` was successfully created for `v67 official public Habanwer ATLAS clean relay`.

Monitoring status:
- Initial post-submit listing confirmed `SubmissionStatus.PENDING`.
- A follow-up check after ~90 seconds still showed `SubmissionStatus.PENDING`.
- Later `kaggle competitions submissions` checks hit repeated Kaggle API SSL EOF errors, so the public score could not be refreshed in this turn.
- This is an API/network polling issue, not evidence of a failed submission.

Current action policy:
- Preserve v62 (`0.86`) as the current official best until v67 completes.
- Do not submit v68 or v66 before v67 score is known unless the user explicitly approves a parallel exploratory submission.

## v67 score monitoring note (2026-06-12 CST)

Submission ref `53572937` remains in `SubmissionStatus.PENDING` on the latest successful Kaggle CLI checks.

Latest observed official submissions:
- v67 `53572937`: pending, no public score yet.
- v65 `53536595`: complete, public `0.85`.
- v63 `53518679`: complete, public `0.84`.
- v62 `53510385`: complete, public `0.86` and remains current official best until v67 completes.

Action policy:
- Continue monitoring v67 until complete.
- Do not submit v68 while v67 is pending unless the user explicitly approves a parallel exploratory submission.
- If v67 completes below or equal to v62, v68 remains the next validated backup candidate.

## v68 official submission pending (2026-06-12 CST)

Decision:
- User explicitly approved a parallel exploratory v68 submission while v67 is still pending.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-vng-refine-clean-relay-v68`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v68 official public VNG Refine clean relay`.
- Submission ref: `53574724`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Concurrent pending submissions:
- v67 `53572937`: `SubmissionStatus.PENDING`.
- v68 `53574724`: `SubmissionStatus.PENDING`.

Comparison target:
- Current official best before v67/v68 remains v62 public score `0.86`.

Next action:
- Monitor refs `53572937` and `53574724` until scoring completes.
- If neither beats v62, consider v66 only as a final low-probability backup; do not submit v69 because it is likely a duplicate of v62.

## v67/v68 parallel score monitoring note (2026-06-12 CST)

Latest successful Kaggle CLI check after v68 submission:
- v68 `53574724`: `SubmissionStatus.PENDING`, no public score yet.
- v67 `53572937`: `SubmissionStatus.PENDING`, no public score yet.
- v65 `53536595`: complete, public `0.85`.
- v62 `53510385`: complete, public `0.86`, remains current official best until v67/v68 complete.

Interpretation:
- Both late-stage exploratory submissions have been accepted and are waiting in the official scoring queue.
- No failure signal is present.
- Do not submit v66 while v67/v68 are pending unless the user explicitly chooses a final low-probability backup probe.

## v67/v68 official results (2026-06-12 CST)

Official results:
- v67 ref `53572937`, `v67 official public Habanwer ATLAS clean relay`: `SubmissionStatus.COMPLETE`, public score `0.62`.
- v68 ref `53574724`, `v68 official public VNG Refine clean relay`: `SubmissionStatus.COMPLETE`, public score `0.86`.

Comparison:
- v67 underperformed severely and should not be selected over v62.
- v68 tied the current best v62 public score `0.86` but did not improve to `0.87`.
- Current official best remains public `0.86`, represented by v62 and now also matched by v68.

Interpretation:
- The Habanwer ATLAS route did not transfer to official scoring.
- The VNG Refine packaging fix was valid and recovered to the `0.86` band, but it did not break the bronze-safe `0.87` threshold.
- Next remaining validated backup is v66 Biohack D3 sparse clean relay, but it should be treated as a final low-probability exploratory probe because it is likely related to the Kienngx/SVD/finisher family.

Next action:
- Refresh the public leaderboard rank after v68.
- Do not submit v66 unless the user explicitly approves `submit v66` / `提交 v66`.

## Leaderboard snapshot after v68 result (2026-06-12 CST)

Snapshot:
- Snapshot: `outputs/kaggle/leaderboard_probe_20260612_after_v68/latest_rank_snapshot.json`.
- Source CSV timestamp: `2026-06-12T04:52:21`.
- Valid ranked teams: `4207`.
- Current public score: `0.86`.
- Current rank: `459 / 4207`.
- Top-10%-style line: rank `421`, score `0.86`.
- Gap to top-10%-style line: about `38` ranks.
- Score band `0.86`: ranks `45-1549`, `1505` teams.
- Score band `0.87`: ranks `5-44`, `40` teams.
- Score band `0.88`: ranks `2-4`, `3` teams.
- Score band `0.90`: rank `1`.

Interpretation:
- v68 tying `0.86` keeps the team in the dense medal-contending band but does not make bronze safe.
- The public top-10%-style cutoff still lies inside the same `0.86` tie band; current rank is only about `38` places below that cutoff.
- A true `0.87` remains the most reliable path to bronze. Without `0.87`, bronze depends on tie ordering and final private leaderboard shakeout.

Next remaining validated official probe:
- v66 Biohack D3 sparse clean relay: validated, unsubmitted, but expected value is lower than v67/v68 because it appears close to already-tested Kienngx/SVD/finisher routes.
- Submit v66 only if the user explicitly approves a final exploratory official probe.

## v66 official submission pending (2026-06-12 CST)

Decision:
- User explicitly approved submitting v66 as the final validated exploratory probe after v67 and v68 completed.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-biohack-d3-sparse-clean-relay-v66`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v66 official public Biohack D3 sparse clean relay`.
- Submission ref: `53589561`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v66 remains public `0.86` from v62 and v68.
- v67 Habanwer ATLAS scored `0.62`; v68 VNG Refine tied best at `0.86`.

Next action:
- Monitor ref `53589561` until scoring completes.
- Start a route-level retro of public artifacts and design a self-owned late-stage leaderboard route.

## v70 adapter audit started for self-owned merge route (2026-06-12 CST)

Purpose:
- Support the self-owned `0.86 -> 0.87` push route by auditing v62, v68, and v66 adapter artifacts on Kaggle without downloading multi-GB files locally.

Kernel:
- Private audit kernel: `guozhaojie/nemotron-adapter-audit-v70`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v70_adapter_audit_v62_v68_v66`.
- Push script: `scripts/push_v70_adapter_audit_v62_v68_v66.ps1`.
- Uses no GPU.

Mounted sources:
- `guozhaojie/nemotron-mirza-artifact-relay-v62`.
- `guozhaojie/nemotron-vng-refine-clean-relay-v68`.
- `guozhaojie/nemotron-biohack-d3-sparse-clean-relay-v66`.

Intended outputs:
- `adapter_audit_v70.json`.
- `adapter_audit_v70.md`.

Checks:
- submission zip SHA-256 and byte size.
- extracted adapter_model SHA-256 and byte size.
- adapter_config SHA-256 and key fields.
- safetensors tensor keys, shapes, dtypes, and module suffix counts.
- pairwise overlap among v62/v68/v66.

Current status at latest check:
- `KernelWorkerStatus.RUNNING`.
- No output files yet; likely hashing/extracting multiple 3GB+ artifacts.

Why this matters:
- If v66 and v68 share the exact adapter hash, v66 is effectively redundant with v68.
- If v62 and v68 have enough compatible tensor overlap, the next self-owned route is a conservative v62-preserving adapter merge rather than another blind SFT.

## v66 official result and v70 adapter audit result (2026-06-12 CST)

v66 official result:
- Submission ref: `53589561`.
- Description: `v66 official public Biohack D3 sparse clean relay`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.84`.
- Current official best remains `0.86` from v62/v68.

Interpretation:
- v66 underperformed and should not be selected over v62/v68.
- This confirms the Biohack sparse finisher did not provide a useful late-stage improvement.

v70 adapter audit result:
- Kernel: `guozhaojie/nemotron-adapter-audit-v70`.
- Version: `1`.
- Status: `KernelWorkerStatus.COMPLETE`.
- Intended outputs written in Kaggle working dir:
  - `adapter_audit_v70.json`.
  - `adapter_audit_v70.md`.
- Do not bulk-download the full kernel output without filtering, because the working dir also contains extracted multi-GB adapter files.

Key v70 evidence from logs:
- v62 Mirza:
  - zip bytes: `3,824,587,714`.
  - adapter bytes: `4,259,063,856`.
  - adapter sha256 prefix: `bc0283d0935afe4d`.
  - `r=32`, `lora_alpha=64`.
  - tensor count: `12,011`.
- v68 VNG Refine:
  - zip bytes: `3,280,489,218`.
  - adapter bytes: `3,554,384,888`.
  - adapter sha256 prefix: `f6c2e5b36638f2d1`.
  - `r=32`, `lora_alpha=32`.
  - tensor count: `12,010`.
- v66 Biohack:
  - zip bytes: `3,286,074,885`.
  - adapter bytes: `3,554,384,888`.
  - adapter sha256 prefix: `9bfb947a7f4c6414`.
  - `r=32`, `lora_alpha=32`.
  - tensor count: `12,010`.

Important conclusions:
- v66 and v68 have identical adapter byte size but different adapter hashes, so they are not byte-identical.
- v66 still scored worse (`0.84`) than v68 (`0.86`), so config/weights differ in a harmful way despite matching size.
- v62 remains the strongest anchor: alpha64, larger adapter, one extra tensor, official `0.86`.
- v68 is the best secondary anchor: official `0.86`, different hash/shape family from v62, alpha32.

Self-owned route implication:
- Do not use v66 as merge donor unless a later tensor-level diff finds a specific useful subset.
- Next best self-owned route remains a conservative v62-preserving merge/delta audit with v68, not more public relays and not broad SFT.

## v70 normalized key-overlap follow-up (2026-06-12 CST)

Local analysis of `outputs/kaggle/v70_adapter_audit_v62_v68_v66/adapter_audit_v70.json`:

Raw key overlap:
- v62 vs v68: only `2` common tensor keys due namespace mismatch.
- v68 vs v66: `12,010 / 12,010` common tensor keys.

Normalized key mapping:
- Map v62 prefix `base_model.model.backbone.layers.` to v68/v66 prefix `base_model.model.model.layers.`.

After normalization:
- v62 vs v68:
  - normalized common keys: `12,010`.
  - same-shape common keys: `12,010`.
  - v62-only keys: `1` (`base_model.model.lm_head.base_layer.weight`).
  - v68-only keys: `0`.
- v62 vs v66:
  - normalized common keys: `12,010`.
  - same-shape common keys: `12,010`.
  - v62-only keys: `1` (`base_model.model.lm_head.base_layer.weight`).
  - v66-only keys: `0`.
- v68 vs v66:
  - common keys: `12,010`.
  - same-shape common keys: `12,010`.

Implication:
- A v62-preserving merge with v68 is technically feasible after key normalization.
- The safest merge should keep v62 config/key naming/output layout and map v68 tensor values into v62 tensor names.
- Keep the v62-only `lm_head.base_layer.weight` untouched.
- Because LoRA A/B weights compose nonlinearly (`B @ A`) and v62 has `alpha=64` while v68 has `alpha=32`, any merge must be conservative.

Candidate self-owned merge family:
- Start from v62.
- For common normalized keys, create interpolated tensors:
  - `merged = (1 - lambda) * v62 + lambda * scale * v68_mapped`.
- Candidate scale options:
  - `scale=1.0` for raw tensor interpolation.
  - `scale=sqrt(64/32)=sqrt(2)` if preserving v62 `alpha=64` while trying to normalize v68 effective LoRA magnitude.
- Candidate lambda should be small: `0.02`, `0.05`, `0.10`.

Risk:
- Direct LoRA tensor interpolation can break low-rank bases even if tensor shapes match.
- The first official probe should be extremely conservative, e.g. `lambda=0.02` or `0.05`, not a large blend.

## v71 self-owned v62-v68 merge lambda 0.02 started (2026-06-12 CST)

Purpose:
- First self-owned leaderboard-push artifact after public-route retro.
- Conservative v62-preserving merge with a small v68 contribution.

Kernel:
- Private kernel: `guozhaojie/nemotron-v62-v68-merge-lam002-v71`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v71_v62_v68_merge_lam002`.
- Push script: `scripts/push_v71_v62_v68_merge_lam002.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v71_v62_v68_merge_lam002_official.ps1`.

Merge strategy:
- Use v62 Mirza as anchor and preserve v62 config/key naming.
- Normalize v68 keys from `base_model.model.model.layers.` to v62's `base_model.model.backbone.layers.` equivalent through reverse lookup.
- For same-shape common tensors: `merged = 0.98 * v62 + 0.02 * v68`.
- Keep v62-only `base_model.model.lm_head.base_layer.weight` untouched.
- No training, no GPU.

Decision policy:
- Do not submit v71 officially unless the kernel completes cleanly and the user explicitly approves.

## v71 completed: first self-owned v62-v68 merge candidate validated (2026-06-12 CST)

Route:
- Self-owned merge route after public-route retro.
- Private kernel: `guozhaojie/nemotron-v62-v68-merge-lam002-v71`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v71_v62_v68_merge_lam002`.
- No training and no GPU.

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v71_v62_v68_merge_lam002_probe/nemotron-v62-v68-merge-lam002-v71.log`.
- File listing: `outputs/kaggle/v71_v62_v68_merge_lam002_probe/nemotron-v62-v68-merge-lam002-v71.files.txt`.
- Merge stats: `outputs/kaggle/v71_v62_v68_merge_lam002_probe/merged_v71_lam002/merge_stats_v71.json`.
- Submit decision JSON: `outputs/kaggle/v71_v62_v68_merge_lam002_probe/v71_submit_decision.json`.

Merge strategy:
- Anchor: v62 Mirza public artifact, official public `0.86`.
- Donor: v68 VNG Refine clean relay, official public `0.86`.
- Key normalization: map v62 `base_model.model.backbone.layers.` to v68 `base_model.model.model.layers.`.
- Tensor interpolation for common keys:
  - `merged = 0.98 * v62 + 0.02 * v68`.
- Keep v62-only key untouched:
  - `base_model.model.lm_head.base_layer.weight`.
- Preserve v62 config and output layout.

Validation evidence from log:
- v62 source zip bytes: `3,824,587,714`.
- v68 source zip bytes: `3,280,489,218`.
- Merged keys: `12,010`.
- Kept v62-only keys: `1`.
- Shape mismatch count: `0`.
- Missing v68 count: `1` (`base_model.model.lm_head.base_layer.weight`).
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors` only.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output adapter model bytes: `4,259,063,824`.
- Output zip bytes: `3,854,539,410`.
- Log confirms: `Ready for Kaggle submission.`

Risk assessment:
- This is a real self-owned candidate, not a public relay.
- It is very conservative (`lambda=0.02`) and preserves v62 config, but direct LoRA A/B interpolation can still degrade because the effective update is nonlinear (`B @ A`).
- Expected downside: score below `0.86`.
- Expected upside: small chance to move forward within the `0.86` tie band or, less likely, reach `0.87`.

Decision policy:
- Prepared submit script: `scripts/submit_v71_v62_v68_merge_lam002_official.ps1`.
- Do not submit without explicit user approval.

## v71 official submission pending (2026-06-12 CST)

Decision:
- User explicitly approved submitting v71 after reviewing the self-owned v62-v68 merge candidate.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v62-v68-merge-lam002-v71`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v71 official self-owned v62-v68 merge lam002`.
- Submission ref: `53602734`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v71 remains public `0.86` from v62/v68.
- v71 is the first self-owned candidate, not a public relay.

Next action:
- Monitor ref `53602734` until scoring completes.

## v71 score monitoring note (2026-06-12 CST)

Submission ref `53602734` remains in `SubmissionStatus.PENDING` after repeated successful Kaggle CLI checks.

Latest observed official submissions:
- v71 `53602734`: pending, no public score yet.
- v66 `53589561`: complete, public `0.84`.
- v68 `53574724`: complete, public `0.86`.
- v67 `53572937`: complete, public `0.62`.
- v62 `53510385`: complete, public `0.86` and remains current best until v71 completes.

Action policy:
- Continue monitoring v71 until complete.
- Do not submit another self-owned merge candidate before v71 score is known unless user explicitly approves a more aggressive parallel strategy.
- If v71 scores below `0.86`, next safer variant would be lower lambda (`0.005` or `0.01`) or selective merge excluding `lm_head` and/or high-risk expert tensors.

## v71 official result and leaderboard snapshot (2026-06-13 CST)

Submission:
- Ref: `53602734`.
- Description: `v71 official self-owned v62-v68 merge lam002`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Interpretation:
- v71 did not improve over the current best public `0.86`, but it also did not regress.
- Current tied best remains v62/v68/v71 at public `0.86`.
- The conservative self-owned merge route is viable for preserving a strong baseline, but raw LoRA tensor interpolation at `lambda=0.02` was not enough to reach `0.87`.

Leaderboard snapshot:
- Downloaded file: `outputs/kaggle/leaderboard_probe_20260613_v71/nvidia-nemotron-model-reasoning-challenge-publicleaderboard-2026-06-13T04_19_44.csv`.
- Rows: `4237`.
- Team `guozhaojie`: rank `465`, score `0.86`, submission count `12`.
- Approximate top 10 percent line: rank `424`.
- Gap to top 10 percent line: about `41` ranks.
- Score bands: `0.87` ranks `6-48` (`43` teams), `0.86` ranks `49-1578` (`1530` teams).

Next action:
- To materially improve medal odds, we still need a true `0.87` candidate or a final/private shakeout favorable enough to overcome the current public top-10-percent gap.
- Next self-owned candidates should avoid broad raw interpolation and instead test more selective, low-risk merges: lower lambda (`0.005` or `0.01`) and/or selective tensor families that preserve the v62 answer behavior.

## v72 selective effective-delta SVD merge started (2026-06-13 CST)

Purpose:
- Next self-owned attempt after v71 preserved public `0.86` but did not improve.
- Move from raw LoRA tensor interpolation to a more LoRA-correct effective delta merge.

Rationale:
- v71 proved broad raw tensor interpolation at `lambda=0.02` can preserve v62 behavior, but did not reach `0.87`.
- Public adapter ensembling/SVD notebooks use the same lower-level idea: combine effective LoRA deltas (`B @ A`) and recompress to rank `32`.
- Our official history shows training-heavy routes are fragile, while public artifact relays plateau around `0.84-0.86`.

Kernel:
- Private kernel: `guozhaojie/nemotron-v62-v68-selective-delta-svd-v72`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v72_v62_v68_selective_delta_svd`.
- Push script: `scripts/push_v72_v62_v68_selective_delta_svd.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v72_v62_v68_selective_delta_svd_official.ps1`.

Merge strategy:
- Anchor: v62 Mirza public artifact, official public `0.86`.
- Donor: v68 VNG Refine clean relay, official public `0.86`.
- Preserve v62 config, output layout, and all unselected tensors.
- For selected shared projection LoRA pairs only:
  - Selected modules: `in_proj`, `out_proj`, `q_proj`, `k_proj`, `v_proj`, `o_proj`.
  - Exclude expert MLP tensors and `lm_head`.
  - Compute a weighted effective delta in LoRA space and recompress to rank `32` with a QR/SVD trick.
  - Current lambda: `0.10`.
- No SFT, no GPU.

Decision policy:
- Do not submit v72 officially unless the kernel completes cleanly and the user explicitly approves.
- If v72 fails due runtime/memory, fallback is v73: narrower selective raw merge over the same projection-family tensors, or a lower-lambda (`0.005/0.01`) v62-preserving raw merge.

Current status:
- Pushed successfully after removing UTF-8 BOM from `kernel-metadata.json`.
- Status after push: `KernelWorkerStatus.RUNNING`.
- Logs were not available during early container startup.

## v72 completed: selective effective-delta SVD candidate validated (2026-06-13 CST)

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v72_selective_delta_svd_probe/nemotron-v62-v68-selective-delta-svd-v72.log`.
- Plain parsed log: `outputs/kaggle/v72_selective_delta_svd_probe/plain_log.txt`.
- File listing: `outputs/kaggle/v72_selective_delta_svd_probe/nemotron-v62-v68-selective-delta-svd-v72.files.txt`.
- Submit decision JSON: `outputs/kaggle/v72_selective_delta_svd_probe/v72_submit_decision.json`.

Validation evidence from log:
- v62 source zip bytes: `3,824,587,714`.
- v62 source adapter bytes: `4,259,063,856`.
- v68 source zip bytes: `3,280,489,218`.
- v68 source adapter bytes: `3,554,384,888`.
- Effective delta coefficients under preserved v62 `alpha=64`: `coef62=0.9`, `coef68=0.05`.
- Selected LoRA pairs: `70`.
- Replaced tensors: `140`.
- Kept v62 tensors: `11,871`.
- Skipped pairs: `0`.
- Module pair counts: `in_proj=23`, `out_proj=23`, `k_proj=6`, `o_proj=6`, `q_proj=6`, `v_proj=6`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output adapter model bytes: `4,259,063,824`.
- Output zip bytes: `3,853,498,866`.
- Elapsed time: `425.08` seconds.
- Log confirms: `Ready for Kaggle submission review; do not submit officially without user approval.`

Risk assessment:
- This is a genuine self-owned candidate and more LoRA-correct than v71 raw tensor interpolation.
- It is still conservative because only `140 / 12,011` tensors changed and expert MLP plus `lm_head` stayed anchored to v62.
- Upside: better chance than lower-lambda raw merge to move within or above the `0.86` band.
- Downside: the `coef68=0.05` effective delta may still be too small for a public score change; official result may tie `0.86` or regress.

Decision policy:
- Prepared submit script: `scripts/submit_v72_v62_v68_selective_delta_svd_official.ps1`.
- Do not submit without explicit user approval.

## v72 official submission pending (2026-06-13 CST)

Decision:
- User explicitly approved submitting v72 after reviewing the selective effective-delta SVD candidate.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v62-v68-selective-delta-svd-v72`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v72 official self-owned v62-v68 selective delta-svd`.
- Submission ref: `53632977`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v72 remains public `0.86` from v62/v68/v71.
- A true public `0.87` would materially improve bronze odds; another `0.86` may still help only through tie ordering/final-private shakeout.

Next action:
- Monitor ref `53632977` until scoring completes.

## v72 official result (2026-06-13 CST)

Submission:
- Ref: `53632977`.
- Description: `v72 official self-owned v62-v68 selective delta-svd`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Interpretation:
- v72 tied the current best public score from v62/v68/v71.
- The selective effective-delta SVD route preserved the strong v62 baseline, but did not reach `0.87`.
- This is still useful evidence: changing only shared projection tensors in a mathematically cleaner way is safe enough to avoid regression, but the magnitude/scope was not enough for a public score increase.

Comparison:
- Current best remains public `0.86`.
- A true `0.87` candidate is still needed for materially safer bronze odds.

## v74 projection plus lm_head effective-delta SVD lambda 0.25 started (2026-06-14 CST)

Purpose:
- Next self-owned attempt after v71-v73 all tied public `0.86`.
- Add a more behavior-visible change while keeping v62 as the anchor.

Rationale:
- Projection-only delta-SVD is safe but appears insufficient to break the `0.86` plateau.
- Public and local evidence suggest `lm_head` participates in strong adapters, but replacing the whole `lm_head.base_layer.weight` is high risk.
- v74 therefore merges only `lm_head` LoRA A/B in effective delta space and preserves v62's `lm_head.base_layer.weight`.

Kernel:
- Private kernel: `guozhaojie/nemotron-v74-projection-lmhead-dsvd-lam025`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v74_v62_v68_projection_lmhead_delta_svd_lam025`.
- Push script: `scripts/push_v74_v62_v68_projection_lmhead_dsvd_lam025.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v74_v62_v68_projection_lmhead_dsvd_lam025_official.ps1`.

Merge strategy:
- Anchor: v62 Mirza public artifact, official public `0.86`.
- Donor: v68 VNG Refine clean relay, official public `0.86`.
- Selected modules: `in_proj`, `out_proj`, `q_proj`, `k_proj`, `v_proj`, `o_proj`, `lm_head`.
- Exclude routed expert MLP tensors.
- Preserve v62-only `base_model.model.lm_head.base_layer.weight` because it is not a LoRA A/B pair.
- Compute effective LoRA delta merge in `B @ A` space and recompress to rank `32`.
- Lambda: `0.25`.
- No SFT, no GPU.

Current status:
- Kernel version `1` pushed successfully.
- Status after push: `KernelWorkerStatus.RUNNING`.

Decision policy:
- Do not submit v74 officially unless the kernel completes cleanly and the user explicitly approves.

## v74 completed: projection plus lm_head effective-delta SVD candidate validated (2026-06-14 CST)

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v74_projection_lmhead_dsvd_lam025_probe/nemotron-v74-projection-lmhead-dsvd-lam025.log`.
- Plain parsed log: `outputs/kaggle/v74_projection_lmhead_dsvd_lam025_probe/plain_log.txt`.
- File listing: `outputs/kaggle/v74_projection_lmhead_dsvd_lam025_probe/nemotron-v74-projection-lmhead-dsvd-lam025.files.txt`.
- Submit decision JSON: `outputs/kaggle/v74_projection_lmhead_dsvd_lam025_probe/v74_submit_decision.json`.

Validation evidence from log:
- v62 source zip bytes: `3,824,587,714`.
- v62 source adapter bytes: `4,259,063,856`.
- v68 source zip bytes: `3,280,489,218`.
- v68 source adapter bytes: `3,554,384,888`.
- Effective delta coefficients under preserved v62 `alpha=64`: `coef62=0.75`, `coef68=0.125`.
- Selected LoRA pairs: `71`.
- Replaced tensors: `142`.
- Kept v62 tensors: `11,869`.
- Skipped pairs: `0`.
- Module pair counts: `in_proj=23`, `out_proj=23`, `k_proj=6`, `o_proj=6`, `q_proj=6`, `v_proj=6`, `lm_head=1`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output adapter model bytes: `4,259,063,824`.
- Output zip bytes: `3,853,549,306`.
- Elapsed time: `433.81` seconds.
- Log confirms: `Ready for Kaggle submission review; do not submit officially without user approval.`

Risk assessment:
- v74 adds only one extra LoRA pair versus v73: `lm_head`.
- It preserves v62's `lm_head.base_layer.weight`, so the highest-risk full head replacement is avoided.
- Because `lm_head` directly affects answer token distribution, this candidate has more chance than v73 to change the public score, but also a higher chance to regress.

Decision policy:
- Prepared submit script: `scripts/submit_v74_v62_v68_projection_lmhead_dsvd_lam025_official.ps1`.
- Do not submit without explicit user approval.

## v74 official submission pending (2026-06-14 CST)

Decision:
- User explicitly approved submitting v74 after reviewing the projection plus `lm_head` effective-delta SVD candidate.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v74-projection-lmhead-dsvd-lam025`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v74 official self-owned v62-v68 projection lmhead dsvd lam025`.
- Submission ref: `53659084`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v74 remains public `0.86` from v62/v68/v71/v72/v73.
- v74 is higher risk than v73 because it changes `lm_head` LoRA A/B, but it may also be more likely to alter final answer token distribution.

Next action:
- Monitor ref `53659084` until scoring completes.

Next action:
- Consider a slightly broader v73 if official attempts remain available: either increase the selective effective-delta scope to include some non-expert MLP-compatible tensors, or run a second selective merge with a stronger effective v68 contribution.

## Leaderboard snapshot after v72 (2026-06-13 CST)

Snapshot:
- Downloaded file: `outputs/kaggle/leaderboard_probe_20260613_after_v72/nvidia-nemotron-model-reasoning-challenge-publicleaderboard-2026-06-13T14_02_02.csv`.
- Rows: `4249`.
- Team `guozhaojie`: rank `469`, score `0.86`, submission count `13`.
- Approximate top 10 percent line: rank `425`.
- Gap to top 10 percent line: about `44` ranks.
- Score bands: `0.88` ranks `2-5` (`4` teams), `0.87` ranks `6-55` (`50` teams), `0.86` ranks `56-1585` (`1530` teams).

Interpretation:
- Current public `0.86` is not safely in the likely bronze band.
- The direct path to safer bronze remains a true public `0.87`.

## v73 projection effective-delta SVD lambda 0.25 started (2026-06-13 CST)

Purpose:
- Next self-owned attempt after v72 tied public `0.86`.
- Increase the effective v68 contribution while preserving v62 as the anchor.

Rationale:
- v72 changed only `70` shared projection LoRA pairs and used an effective v68 coefficient of `0.05`; it was safe but did not move the public score.
- Directly expanding into `up_proj/down_proj` would mostly touch routed expert tensors, which is much riskier and much slower.
- v73 keeps the same controlled shared projection scope as v72, but raises lambda from `0.10` to `0.25`.

Kernel:
- Private kernel: `guozhaojie/nemotron-v73-projection-delta-svd-lam025`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v73_v62_v68_projection_delta_svd_lam025`.
- Push script: `scripts/push_v73_v62_v68_projection_delta_svd_lam025.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v73_v62_v68_projection_delta_svd_lam025_official.ps1`.

Merge strategy:
- Anchor: v62 Mirza public artifact, official public `0.86`.
- Donor: v68 VNG Refine clean relay, official public `0.86`.
- Selected modules remain `in_proj`, `out_proj`, `q_proj`, `k_proj`, `v_proj`, `o_proj`.
- Exclude expert MLP tensors and `lm_head`.
- Compute effective LoRA delta merge in `B @ A` space and recompress to rank `32`.
- Lambda: `0.25`.
- With preserved v62 `alpha=64`, expected unscaled coefficients are approximately `coef62=0.75`, `coef68=0.125`.
- No SFT, no GPU.

Current status:
- Initial push attempts hit transient Kaggle API SSL EOF errors.
- Push eventually succeeded after shortening/fixing the kernel slug to Kaggle's actual title-derived slug.
- Status after push: `KernelWorkerStatus.RUNNING`.

Decision policy:
- Do not submit v73 officially unless the kernel completes cleanly and the user explicitly approves.

## v73 completed: projection effective-delta SVD lambda 0.25 candidate validated (2026-06-13 CST)

Run result:
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v73_projection_delta_svd_lam025_probe/nemotron-v73-projection-delta-svd-lam025.log`.
- Plain parsed log: `outputs/kaggle/v73_projection_delta_svd_lam025_probe/plain_log.txt`.
- File listing: `outputs/kaggle/v73_projection_delta_svd_lam025_probe/nemotron-v73-projection-delta-svd-lam025.files.txt`.
- Submit decision JSON: `outputs/kaggle/v73_projection_delta_svd_lam025_probe/v73_submit_decision.json`.

Validation evidence from log:
- v62 source zip bytes: `3,824,587,714`.
- v62 source adapter bytes: `4,259,063,856`.
- v68 source zip bytes: `3,280,489,218`.
- v68 source adapter bytes: `3,554,384,888`.
- Effective delta coefficients under preserved v62 `alpha=64`: `coef62=0.75`, `coef68=0.125`.
- Selected LoRA pairs: `70`.
- Replaced tensors: `140`.
- Kept v62 tensors: `11,871`.
- Skipped pairs: `0`.
- Module pair counts: `in_proj=23`, `out_proj=23`, `k_proj=6`, `o_proj=6`, `q_proj=6`, `v_proj=6`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output adapter model bytes: `4,259,063,824`.
- Output zip bytes: `3,853,502,351`.
- Elapsed time: `501.15` seconds.
- Log confirms: `Ready for Kaggle submission review; do not submit officially without user approval.`

Risk assessment:
- v73 is the same controlled projection-only merge family as v72, but with stronger v68 contribution.
- This is more likely than v72 to change official score, but also has higher regression risk.
- It still avoids the highest-risk areas: `lm_head` and routed expert MLP tensors.

Decision policy:
- Prepared submit script: `scripts/submit_v73_v62_v68_projection_delta_svd_lam025_official.ps1`.
- Do not submit without explicit user approval.

## Leaderboard snapshot before v73 decision (2026-06-14 CST)

Snapshot:
- Downloaded file: `outputs/kaggle/leaderboard_probe_20260614_latest/nvidia-nemotron-model-reasoning-challenge-publicleaderboard-2026-06-14T01_01_19.csv`.
- Rows: `4260`.
- Team `guozhaojie`: rank `469`, score `0.86`, submission count `13`.
- Approximate top 10 percent line: rank `426`.
- Gap to top 10 percent line: about `43` ranks.
- Score bands: `0.88` ranks `2-6` (`5` teams), `0.87` ranks `7-55` (`49` teams), `0.86` ranks `56-1601` (`1546` teams).

Interpretation:
- Current public `0.86` remains outside the approximate top 10 percent line.
- v73 is the next prepared self-owned candidate; it has higher upside than v72 but also higher regression risk.

## v73 official submission pending (2026-06-14 CST)

Decision:
- User explicitly approved submitting v73 after reviewing the projection effective-delta SVD lambda `0.25` candidate.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v73-projection-delta-svd-lam025`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v73 official self-owned v62-v68 projection delta-svd lam025`.
- Submission ref: `53654923`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v73 remains public `0.86` from v62/v68/v71/v72.
- v73 has higher upside than v72 because the effective v68 coefficient is stronger, but it also has higher regression risk.

Next action:
- Monitor ref `53654923` until scoring completes.

## v73 official result (2026-06-14 CST)

Submission:
- Ref: `53654923`.
- Description: `v73 official self-owned v62-v68 projection delta-svd lam025`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Interpretation:
- v73 tied the current best public score from v62/v68/v71/v72.
- Increasing the projection-only effective v68 contribution from v72's `coef68=0.05` to v73's `coef68=0.125` still preserved the v62 baseline but did not reach `0.87`.
- This suggests the shared projection-only delta-SVD family is safe but likely insufficient by itself to break the public `0.86` plateau.

Comparison:
- Current best remains public `0.86`.
- A true `0.87` candidate is still needed for materially safer bronze odds.

## v74 official result (2026-06-14 CST)

Submission:
- Ref: `53659084`.
- Description: `v74 official self-owned v62-v68 projection lmhead dsvd lam025`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Interpretation:
- v74 tied the current best public score from v62/v68/v71/v72/v73.
- Adding the `lm_head` LoRA pair to the projection-family effective-delta SVD merge preserved the strong v62 behavior but still did not reach `0.87`.
- The result confirms that projection plus `lm_head` delta-SVD is safe enough to avoid regression, but it remains inside the same dense `0.86` public band.

Comparison:
- Current best remains public `0.86`.
- A true `0.87` candidate is still needed for materially safer bronze odds.

## Leaderboard snapshot after v74 (2026-06-14 CST)

Snapshot:
- Downloaded zip: `outputs/kaggle/leaderboard_probe_20260614_after_v74/nvidia-nemotron-model-reasoning-challenge.zip`.
- Snapshot JSON: `outputs/kaggle/leaderboard_probe_20260614_after_v74/latest_rank_snapshot.json`.
- CSV inside zip: `nvidia-nemotron-model-reasoning-challenge-publicleaderboard-2026-06-14T08:35:17.csv`.
- Team `guozhaojie`: rank `470`, score `0.86`, submission count `15`.
- Total teams: `4272`.
- Approximate top 10 percent line: rank `427`.
- Gap to top 10 percent line: about `43` ranks.
- Delta versus previous recorded rank `469`: `-1` rank.
- Score bands: `0.90` rank `1` (`1` team), `0.88` ranks `2-6` (`5` teams), `0.87` ranks `7-59` (`53` teams), `0.86` ranks `60-1611` (`1552` teams).

Interpretation:
- v74 did not improve leaderboard placement; the public score remains `0.86`.
- The one-rank slip appears to be normal leaderboard churn/tie-band movement while total teams increased from `4260` to `4272`.
- Bronze/top-10%-style odds are essentially unchanged: still close, still not safe, and still likely requires a true `0.87` for material safety.

## v75 MLP-lite effective-delta SVD lambda 0.15 started (2026-06-14 CST)

Purpose:
- Next self-owned attempt after v72-v74 preserved public `0.86` but did not reach `0.87`.
- Add more behavior-relevant non-routed MLP LoRA pairs while keeping v62 as the anchor.

Kernel:
- Private kernel: `guozhaojie/nemotron-v75-mlp-lite-dsvd-lam015`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v75_v62_v68_mlp_lite_delta_svd_lam015`.
- Push script: `scripts/push_v75_v62_v68_mlp_lite_dsvd_lam015.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v75_v62_v68_mlp_lite_dsvd_lam015_official.ps1`.

Design:
- Anchor: v62 Mirza public artifact, official public `0.86`.
- Donor: v68 VNG Refine clean relay, official public `0.86`.
- Preserve v62 config, output layout, and all unselected tensors.
- Selected modules: `in_proj`, `out_proj`, `q_proj`, `k_proj`, `v_proj`, `o_proj`, `lm_head`, `up_proj`, `down_proj`.
- Exclude routed expert tensors via `.experts.` guard.
- Do not select `gate_proj` because v68 does not expose a compatible `gate_proj` donor.
- Lambda: `0.15`.
- With preserved v62 `alpha=64`, expected unscaled effective coefficients are approximately `coef62=0.85`, `coef68=0.075`.
- No training and no GPU.

Rationale:
- v72-v74 showed projection-only and projection-plus-`lm_head` effective-delta SVD are safe enough to preserve `0.86`, but insufficient to break the plateau.
- v75 takes a controlled step into shared/non-routed MLP (`up_proj`, `down_proj`), which is more likely to affect reasoning behavior than attention projection deltas alone.
- The lower lambda versus v73/v74 reduces regression risk while the wider tensor scope increases upside.

Current status:
- Push succeeded.
- Latest status immediately after push: `KernelWorkerStatus.RUNNING`.
- Initial logs/files were empty while the kernel started processing large source zips.

Decision policy:
- Do not submit v75 officially unless the kernel completes cleanly and the user explicitly approves after reviewing validation logs/files.

## v75 completed: MLP-lite effective-delta SVD candidate validated (2026-06-14 CST)

Run result:
- Private kernel: `guozhaojie/nemotron-v75-mlp-lite-dsvd-lam015`.
- Kernel version: `1`.
- Status: `KernelWorkerStatus.COMPLETE`.
- Log: `outputs/kaggle/v75_mlp_lite_dsvd_lam015_probe/nemotron-v75-mlp-lite-dsvd-lam015.log`.
- File listing: `outputs/kaggle/v75_mlp_lite_dsvd_lam015_probe/nemotron-v75-mlp-lite-dsvd-lam015.files.txt`.

Validation evidence from log:
- v62 source zip bytes: `3,824,587,714`.
- v62 source adapter bytes: `4,259,063,856`.
- v68 source zip bytes: `3,280,489,218`.
- v68 source adapter bytes: `3,554,384,888`.
- Effective delta coefficients under preserved v62 `alpha=64`: `coef62=0.85`, `coef68=0.075`.
- Candidate selected bases: `117`.
- Selected LoRA pairs: `117`.
- Replaced tensors: `234`.
- Kept v62 tensors: `11,777`.
- Skipped pairs: `0`.
- Module pair counts: `in_proj=23`, `out_proj=23`, `down_proj=23`, `up_proj=23`, `k_proj=6`, `o_proj=6`, `q_proj=6`, `v_proj=6`, `lm_head=1`.
- Output zip root entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output adapter model bytes: `4,259,063,824`.
- Output zip bytes: `3,853,841,077`.
- Elapsed time: `481.32` seconds.
- Log confirms: `Ready for Kaggle submission review; do not submit officially without user approval.`

Risk assessment:
- v75 is the first self-owned merge after v74 that expands into shared/non-routed MLP (`up_proj`, `down_proj`).
- It is more behavior-relevant than projection-only and projection-plus-`lm_head` variants, so it has more upside.
- It also has higher regression risk because it modifies `234` tensors versus v74's `142`, but the lower effective v68 coefficient (`0.075`) and v62-preserved config reduce the downside.

Decision policy:
- Prepared submit script: `scripts/submit_v75_v62_v68_mlp_lite_dsvd_lam015_official.ps1`.
- Do not submit without explicit user approval.

## v75 official submission pending (2026-06-14 CST)

Decision:
- User explicitly approved submitting v75 after reviewing the MLP-lite effective-delta SVD candidate.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v75-mlp-lite-dsvd-lam015`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v75 official self-owned v62-v68 mlp-lite dsvd lam015`.
- Submission ref: `53672249`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Comparison target:
- Current official best before v75 remains public `0.86` from v62/v68/v71/v72/v73/v74.
- v75 has higher upside than v74 because it modifies non-routed shared MLP LoRA pairs (`up_proj`, `down_proj`) in addition to projection and `lm_head` pairs.
- v75 also has higher regression risk because it replaces `234` tensors versus v74's `142`, though the effective v68 coefficient is lower (`0.075`).

Next action:
- Monitor ref `53672249` until scoring completes.
- If v75 reaches `0.87`, refresh leaderboard rank immediately.
- If v75 ties or regresses, preserve the existing `0.86` submissions as best official results.

## v75 official result (2026-06-14 CST)

Submission:
- Ref: `53672249`.
- Description: `v75 official self-owned v62-v68 mlp-lite dsvd lam015`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Interpretation:
- v75 tied the current best public score from v62/v68/v71/v72/v73/v74.
- Expanding effective-delta SVD into shared/non-routed MLP (`up_proj`, `down_proj`) preserved the strong v62 baseline, but still did not reach `0.87`.
- This suggests the v62-v68 SVD merge family is robust enough to avoid regression across wider scopes, but may not contain enough complementary signal to break the public `0.86` plateau by itself.

Comparison:
- Current best remains public `0.86`.
- A true `0.87` candidate is still needed for materially safer bronze odds.

## v76 Huikang v20 direct adapter convert/audit started (2026-06-14 CST)

Purpose:
- Pivot away from the v62-v68 SVD merge family after v71-v75 all tied public `0.86`.
- Test the strongest external evidence source found in late-stage research: Huikang's public `nemotron-adapter` model artifact associated with the Progress Prize winning repository/notebook pipeline.

Kernel:
- Private kernel: `guozhaojie/nemotron-v76-huikang-v20-direct-convert`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v76_huikang_v20_direct_convert_audit`.
- Push script: `scripts/push_v76_huikang_v20_direct_convert.ps1`.
- Prepared official submit script, not auto-run: `scripts/submit_v76_huikang_v20_direct_convert_official.ps1`.

Sources:
- Huikang public model source: `huikang/nemotron-adapter/Transformers/default/20`.
- Reference source for stable official config/shape: `guozhaojie/nemotron-mirza-artifact-relay-v62`.

Design:
- No training and no GPU.
- Auto-detect Huikang adapter files inside `/kaggle/input/models/huikang/nemotron-adapter/transformers/default/20`.
- If the adapter already has submission-like LoRA keys, normalize `model` to `backbone` and repackage.
- If it has Tinker/training-style keys, apply the public Huikang conversion logic:
  - rename `base_model.model.model` to `base_model.model.backbone`;
  - unfuse expert `w1`/`w2` tensors into per-expert `up_proj`/`down_proj`;
  - merge Mamba `gate_proj + x_proj` into `in_proj` by rank-32 SVD;
  - use v62 config as the official output config.
- Output root-only `submission.zip` with `adapter_config.json` and `adapter_model.safetensors`.

Current status:
- First push failed because `kernel-metadata.json` had a UTF-8 BOM; metadata was rewritten without BOM.
- Second push succeeded.
- Latest status immediately after push: `KernelWorkerStatus.RUNNING`.
- Initial logs/files were empty while the kernel started processing source artifacts.

Decision policy:
- Do not submit v76 officially unless the kernel completes cleanly, produces a valid root-only zip, and the user explicitly approves after reviewing the result.

## v76 Huikang v20 direct adapter convert/audit result (2026-06-14 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v76-huikang-v20-direct-convert`.
- Kernel version: `1`.
- Status: `KernelWorkerStatus.ERROR`.
- Lightweight log saved at `outputs/kaggle/v76_huikang_v20_direct_convert_probe/nemotron-v76-huikang-v20-direct-convert.log`.

Failure:
- The notebook printed `Huikang adapter dir candidates:` with no candidates.
- It then raised `FileNotFoundError: No Huikang adapter dir found` inside `find_huikang_adapter_dir()`.
- `kaggle kernels files` returned no useful output files after the failure.

Interpretation:
- This does not yet invalidate Huikang v20 as a candidate.
- The failure happened before any adapter conversion/audit, because path discovery was too strict and required a Kaggle-mounted path pattern that was not present at runtime.

Next action:
- Push a v76 path-discovery fix or a v77 probe that lists `/kaggle/input` broadly, searches by `adapter_config.json`, `adapter_model.safetensors`, `*.safetensors`, and config-like files, and chooses candidates by file evidence rather than by `huikang/nemotron-adapter` path text.
- Do not submit an official entry until a clean root-only `submission.zip` is produced and reviewed.

## v76 Huikang v20 path-discovery fix pushed (2026-06-14 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v76-huikang-v20-direct-convert`.
- Kernel version: `2`.
- Push result: `Kernel version 2 successfully pushed`.

Fix:
- Replaced strict Huikang path matching with broad `/kaggle/input` diagnostics.
- The notebook now prints top-level mounted inputs, interesting `.json`/`.safetensors`/`.zip` files, and adapter candidates scored by file evidence.
- Candidate selection now searches for `adapter_config.json`, `adapter_model.safetensors`, and any `*.safetensors`, while deprioritizing v62/Mirza/reference paths.

External evidence:
- Kaggle CLI can list Huikang v20 files under `huikang/nemotron-adapter/Transformers/default/20`.
- v20 contains `adapter_config.json` and `adapter_model.safetensors` with model bytes `1544348352`.

Current status:
- Immediate status poll hit a transient Kaggle API SSL EOF.
- Early log pull returned no content yet.

Next action:
- Monitor v76 version `2`.
- If it completes, capture lightweight logs/files, verify root-only `submission.zip`, and only then ask for explicit approval before any official submission.

## v77 Huikang v27 direct adapter convert/audit started (2026-06-14 CST)

Purpose:
- Run the same path-fixed direct-convert/audit route on Huikang `default/27`, because Kaggle CLI shows it is a later public version with the same expected adapter file layout as v20.
- This is a parallel private audit, not an official submission.

Kernel:
- Private kernel: `guozhaojie/nemotron-v77-huikang-v27-direct-convert`.
- Kernel version: `1`.
- Kernel directory: `kaggle_kernel_v77_huikang_v27_direct_convert_audit`.
- Push script: `scripts/push_v77_huikang_v27_direct_convert.ps1`.
- Push result: `Kernel version 1 successfully pushed`.

Source:
- Huikang public model source: `huikang/nemotron-adapter/Transformers/default/27`.
- Reference source for stable official config/shape: `guozhaojie/nemotron-mirza-artifact-relay-v62`.

Decision policy:
- Do not submit v77 officially unless the kernel completes cleanly, produces a valid root-only `submission.zip`, and the user explicitly approves after reviewing the result.

## Process guardrail added after v76 path failure (2026-06-14 CST)

Issue:
- v76 version `1` failed from a low-level process bug: source path discovery assumed the mounted Kaggle path would contain specific text, and the notebook did not print enough `/kaggle/input` diagnostics before failing.

Guardrail:
- Added global Codex skill `kaggle-submission-guardrails`.
- Added preflight script `C:\Users\jie13\.codex\skills\kaggle-submission-guardrails\scripts\kaggle_kernel_preflight.py`.
- Added project note `docs/KAGGLE_SUBMISSION_GUARDRAILS.md`.

Verification:
- Skill validation passed with `quick_validate.py`.
- Preflight passed on v76 pathfix kernel directory and verified Huikang v20 remote files `adapter_config.json` and `adapter_model.safetensors`.
- Preflight passed on v77 kernel directory and verified Huikang v27 remote files `adapter_config.json` and `adapter_model.safetensors`.

Rule going forward:
- Before future Kaggle kernel pushes/submissions, run the guardrail preflight and record the evidence if the run affects official scoring or late-stage medal strategy.

## v76 Huikang v20 path-discovery fix result (2026-06-14 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v76-huikang-v20-direct-convert`.
- Kernel version: `2`.
- Status: `KernelWorkerStatus.ERROR`.
- Lightweight log saved at `outputs/kaggle/v76_huikang_v20_direct_convert_probe/nemotron-v76-huikang-v20-direct-convert-v2.log`.

Evidence:
- Runtime `/kaggle/input` existed but only had:
- `/kaggle/input/competitions`;
- `/kaggle/input/notebooks`;
- v62 notebook source with `submission.zip`.
- No `/kaggle/input/models` directory and no Huikang `adapter_model.safetensors` candidate appeared at runtime.
- Failure: `FileNotFoundError: No adapter/model safetensors candidates found under /kaggle/input`.

Interpretation:
- v76 v2 fixed the earlier bad path-filtering error and produced the missing runtime diagnostics.
- The new blocker is source mounting: Kaggle CLI can list Huikang v20 model files, but this private CPU/no-GPU kernel did not mount the `model_sources` artifact into runtime.
- Conversion logic still has not been tested.

Guardrail update:
- Updated `kaggle-submission-guardrails` to distinguish CLI source visibility from runtime mount evidence.
- Future model-source kernels must prove runtime model mount before conversion/submission decisions.

Next action:
- Let v77 finish or fail to see whether Huikang v27 mounts differently.
- If v77 has the same missing model mount, the next fix should use a kernel configuration closer to Huikang's public notebook metadata or relay through an available notebook/kernel source rather than assuming `model_sources` will mount in the current private CPU kernel shape.

## v77 Huikang v27 direct adapter convert/audit result (2026-06-14 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v77-huikang-v27-direct-convert`.
- Kernel version: `1`.
- Status: `KernelWorkerStatus.COMPLETE`.
- Lightweight log saved at `outputs/kaggle/v77_huikang_v27_direct_convert_probe/nemotron-v77-huikang-v27-direct-convert.log`.
- File listing saved at `outputs/kaggle/v77_huikang_v27_direct_convert_probe/nemotron-v77-huikang-v27-direct-convert.files.txt`.

Runtime source evidence:
- `/kaggle/input/models` was mounted.
- Chosen Huikang source path: `/kaggle/input/models/huikang/nemotron-adapter/transformers/default/27`.
- Source files included `README.md`, `adapter_config.json`, `adapter_model.safetensors`, and `checkpoint_complete`.
- Huikang source model bytes: `1544348352`.
- v62 reference zip path: `/kaggle/input/notebooks/guozhaojie/nemotron-mirza-artifact-relay-v62/submission.zip`.
- v62 reference model bytes: `4259063856`.

Conversion evidence:
- Source config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, `target_modules=all-linear`.
- Source tensor count: `418`.
- Source LoRA base count: `209`.
- Source module suffix counts included `gate_proj=46`, `out_proj=46`, `x_proj=46`, `w1=46`, `w2=46`, `w3=46`, `down_proj=46`, `up_proj=46`, `k/o/q/v_proj=12 each`, `lm_head=2`.
- Detected mode: `trained_adapter_conversion`.
- Output tensor count: `12010`.
- Direct pairs: `94`.
- Expert unfused pairs: `5888`.
- Mamba merged layers: `23`.
- Skipped count: `23`, all shown examples were `empty_w3`.
- SVD kept min/mean: `0.7066424427` / `0.7320138715`.

Shape audit:
- v62 tensor count: `12011`.
- Same-shape keys with v62: `12008`.
- Missing vs v62: `3`.
- Extra vs v62: `2`.
- Main mismatch is around `lm_head`: v62 has `base_model.model.lm_head.*`, output has `base_model.model.backbone.lm_head.*`.

Output evidence:
- Output zip entries: `['adapter_config.json', 'adapter_model.safetensors']`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=64`, official base model path `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output target modules: `up_proj`, `in_proj`, `gate_proj`, `out_proj`, `k_proj`, `o_proj`, `v_proj`, `q_proj`, `lm_head`, `down_proj`.
- Output model bytes: `3554420648`.
- Output zip bytes: `3272714790`.
- Elapsed seconds: `302.38`.

Interpretation:
- v77 is the first successful Huikang direct-convert audit in this branch.
- It is stronger evidence than v76 because the runtime actually mounted the model source and produced a root-only zip.
- Risk: the shape audit still shows a small `lm_head` key namespace mismatch versus v62. This may be acceptable if the official evaluator expects the output config/key convention, but it is not risk-free.

Decision policy:
- Do not submit v77 officially unless the user explicitly approves.
- If approved, submit `submission.zip` from kernel `guozhaojie/nemotron-v77-huikang-v27-direct-convert` version `1` with a clear description such as `v77 official Huikang v27 direct convert audit`.

## v77 official submission pending (2026-06-15 CST)

Decision:
- User explicitly approved official submission after reviewing v77 direct-convert evidence.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v77-huikang-v27-direct-convert`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v77 official Huikang v27 direct convert`.
- Submission ref: `53680134`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Pre-submit guardrail evidence:
- `kaggle-submission-guardrails` preflight passed.
- Kernel status was `KernelWorkerStatus.COMPLETE`.
- Runtime logs confirmed Huikang v27 mounted under `/kaggle/input/models/huikang/nemotron-adapter/transformers/default/27`.
- Runtime logs confirmed output zip entries `adapter_config.json` and `adapter_model.safetensors`.
- Output model bytes: `3554420648`.
- Output zip bytes: `3272714790`.

Comparison target:
- Current official best before v77 remains public `0.86` from v62/v68/v71/v72/v73/v74/v75.
- v77 is a genuinely new Huikang v27 direct-convert route, not another v62-v68 merge.

Risk:
- Shape audit showed `missing_vs_v62_count=3` and `extra_vs_v62_count=2`, mainly around `lm_head` key namespace.
- This is acceptable for an approved late-stage medal push, but the score may tie or regress.

Next action:
- Monitor submission ref `53680134` until scoring completes.
- If it reaches `0.87`, refresh leaderboard/rank immediately.
- If it ties or regresses, preserve existing public `0.86` as current best and continue searching for a complementary artifact route.

## v77 official result (2026-06-15 CST)

Submission:
- Ref: `53680134`.
- Description: `v77 official Huikang v27 direct convert`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.51`.

Comparison:
- v77 regressed far below current best public `0.86`.
- Current best remains public `0.86` from v62/v68/v71/v72/v73/v74/v75.

Interpretation:
- The Huikang v27 direct conversion produced a structurally valid zip, but the key/config conversion is not evaluator-compatible enough for leaderboard performance.
- The earlier `lm_head` namespace mismatch and conversion uncertainty were real risks.
- Do not continue direct Huikang conversion without first fixing key compatibility against a known-scoring Huikang public output or rerunning the exact public notebook path.

Next action:
- Preserve `0.86` submissions as best official result.
- Focus final sprint only on routes with credible public `0.87+` artifact evidence or exact-output relay candidates, not more speculative conversion.

## v78/v79 official results: 3-way DSVD variants tied 0.86 (2026-06-15 CST)

Submissions:
- v78 ref `53699576`: `v78 official 3way DSVD v62+v68+v66`, `SubmissionStatus.COMPLETE`, public score `0.86`.
- v79 ref `53699591`: `v79 official 3way DSVD v62+v68+v65`, `SubmissionStatus.COMPLETE`, public score `0.86`.

Evidence:
- Kaggle submissions CLI on 2026-06-15 CST showed both v78 and v79 complete with public score `0.86`.
- Lightweight logs/files saved under `outputs/kaggle/v78_v79_final_status/`.
- v78 log: output entries `adapter_config.json`, `adapter_model.safetensors`; output model bytes `4259063824`; output zip bytes `3853488853`.
- v79 log: output entries `adapter_config.json`, `adapter_model.safetensors`; output model bytes `4259063824`; output zip bytes `3853372408`.

Interpretation:
- Both 3-way DSVD variants preserved the current best `0.86` but did not break the `0.87` line.
- This reinforces that v62/v68/v65/v66 adapter arithmetic is a plateau-preserving family, not a reliable bronze-safe breakthrough.

Next action:
- Preserve existing `0.86` submissions as the best official result.
- For the final sprint, only pursue genuinely new public artifact/adapter routes or exact-output relays with credible evidence beyond the already-tested v62/v68/SVD family.

## v80/v81 final-sprint KeithTyser 0.86 anchor audit started (2026-06-15 CST)

Rationale:
- Public model source `keithtyser/nemotron-086-adapters-20260605` exposes six real rank-32 Nemotron 0.86-class LoRA adapter anchors, each with `adapter_model.safetensors` around `3554384888` bytes.
- This is not a proven `0.87` route, but it is a distinct public adapter-anchor pool discovered late in the sprint.
- The highest-priority candidate is `public_hk_to_kn_lm_head_lam1p0`, because it appears to address the Huikang-to-Kienngx key/config compatibility problem that caused v77 to collapse to `0.51`.

Runs:
- v80 private kernel: `guozhaojie/nemotron-v80-keithtyser-086-anchor-audit`, version `2`; six-source audit, CPU/no internet, not an official submission.
- v81 private kernel: `guozhaojie/nemotron-v81-keithtyser-hk-to-kn-lmhead`, version `1`; single-source relay/audit for `public_hk_to_kn_lm_head_lam1p0`, CPU/no internet, not an official submission.

Guardrail evidence:
- `kaggle-submission-guardrails` preflight passed for both v80 and v81.
- Remote model source file listings confirmed `adapter_config.json`, `adapter_model.safetensors`, and metadata JSON files are visible before push.
- Official submission remains blocked unless a kernel completes cleanly, logs prove runtime mount/output zip integrity, and the user explicitly approves.

## v81 completed: KeithTyser HK-to-KN lm_head 0.86-class relay ready but not submitted (2026-06-15 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v81-keithtyser-hk-to-kn-lmhead`.
- Kernel version: `1`.
- Status: `KernelWorkerStatus.COMPLETE`.
- Lightweight logs/files saved under `outputs/kaggle/v81_keithtyser_hk_to_kn_lmhead_probe/`.

Runtime source evidence:
- `/kaggle/input/models` mounted successfully.
- Selected source dir: `/kaggle/input/models/keithtyser/nemotron-086-adapters-20260605/transformers/public_hk_to_kn_lm_head_lam1p0/1`.
- Source `adapter_model.safetensors` bytes: `3554384888`.
- Source partial sha256 head+tail 16MB: `72183cc3220d59cb74dc36367897197e4ff17d69919d51d7cdddcde13c57e1aa`.
- Metadata `source_note`: `Canonical merged 0.86-class public adapter.`
- Merge metadata: anchor `huikang_default20_ready`, other `kienngx_tinker_adapter_v1_ready`, group `lm_head`, changed tensors `2`, lambda `1.0`, method `direct_tensor_interpolation`.

Output evidence:
- Output zip entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output config: `peft_type=LORA`, `r=32`, `lora_alpha=32`, base model `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules: `down_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`.
- Output zip bytes: `3280491955`.
- Elapsed seconds: `199.19`.

Leaderboard context:
- Fresh leaderboard snapshot at `outputs/kaggle/leaderboard_download_20260615_2015/`:
- total teams `4317`;
- `guozhaojie` rank `474`, public score `0.86`, submission count `19`;
- approximate top 10% rank `432`, also score `0.86`;
- score band `0.87`: ranks `7-65`, `59` teams;
- score band `0.86`: ranks `66-1666`, `1601` teams.

Decision:
- v81 is submission-ready structurally, but its own metadata says `0.86-class`, not `0.87`.
- Expected outcome if submitted: likely `0.86`; possible downside `0.85`/worse if this anchor is less compatible than v62/v68; small upside if it transfers unusually well or helps final/private behavior.
- Do not submit v81 officially unless the user explicitly approves this late-stage low-to-medium expected value gamble.

Prepared script:
- `scripts/submit_v81_keithtyser_hk_to_kn_lmhead_official.ps1`

## v82 official submission pending: Svanik engine ensemble normalized relay (2026-06-15 CST)

Decision:
- User explicitly approved official submission for the v82 Svanik engine ensemble relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v82-svanik-engine-ensemble-relay`.
- Kernel version: `2`.
- Output file: `submission.zip`.
- Description: `v82 official Svanik engine ensemble normalized relay`.
- Submission ref: `53710861`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Pre-submit guardrail evidence:
- Kernel files listing confirmed `submission.zip` exists.
- Lightweight probe logs/files are saved under `outputs/kaggle/v82_svanik_engine_ensemble_probe/`.
- Output config base path was normalized to `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Target modules include `down_proj`, `gate_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`, and `x_proj`.
- Output zip bytes from runtime evidence: `3370487743`.

Comparison target:
- Current official best before v82 remains public `0.86` from v62/v68/v71/v72/v73/v74/v75/v78/v79.
- Latest leaderboard snapshot before v82: team rank `474/4317`, public score `0.86`; approximate top-10% rank `432`, also inside the `0.86` band.

Next action:
- Monitor ref `53710861` until complete.
- If it reaches `0.87`, refresh leaderboard immediately.
- If it ties `0.86` or regresses, preserve existing `0.86` submissions as best official result.

## v82 official result: Svanik engine ensemble normalized relay errored (2026-06-15 CST)

Submission:
- Ref: `53710861`.
- Description: `v82 official Svanik engine ensemble normalized relay`.
- Status: `SubmissionStatus.ERROR`.
- Public score: none.

Evidence:
- Kaggle submissions CLI on 2026-06-15 21:50 CST showed ref `53710861` in `SubmissionStatus.ERROR`.
- Kernel output was structurally present, but official scoring did not accept the submitted artifact.

Interpretation:
- Do not resubmit v82 unchanged.
- Most likely failure mode is packaging-level compatibility rather than leaderboard quality: v82 rewrote the public 3.6GB adapter into a normalized zip whose official scorer rejected.
- The intended fix is v83, which streams the public source zip into a root-only normalized `ZIP_STORED` output without extracting/recompressing the large safetensors file.

Current best:
- Preserve public `0.86` from v62/v68/v71/v72/v73/v74/v75/v78/v79.

## v83 completed: Svanik stream relay ready for approval (2026-06-15 CST)

Kernel:
- Private kernel: `guozhaojie/nemotron-v83-svanik-stream-relay`.
- Latest run completed at `2026-06-15 12:36:58 UTC`.
- Lightweight logs/files saved under `outputs/kaggle/v83_svanik_stream_relay_probe/`.

Runtime evidence:
- Source zip selected from public kernel source `svanikkolli/nemotron-engine-ensembler`.
- Source model entry size: `3611499192` bytes.
- Source model head16MB sha256: `5304e6d88fbd3d7055a5f277f653ffd4124598b3285065b168af92b112da6bbc`.
- Config base path normalized from `/kaggle/input/models/metric/nemotron-3-nano-30b-a3b-bf16/transformers/default/1` to `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
- Output zip entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output uncompressed sizes: `adapter_config.json=1132`, `adapter_model.safetensors=3611499192`.
- Output zip bytes: `3611500702`.
- Target modules include `down_proj`, `gate_proj`, `in_proj`, `k_proj`, `lm_head`, `o_proj`, `out_proj`, `q_proj`, `up_proj`, `v_proj`, and `x_proj`.

Decision:
- v83 is the safer replacement for v82 because it preserves the public source adapter bytes and only normalizes config while writing a root-only stored zip.
- It is still a late-stage public artifact gamble: upside is a possible `0.87`/tie-order/private-shift improvement; downside is another scoring error or score below current best.
- Do not submit v83 officially unless the user explicitly approves.

Prepared next action:
- If approved, submit `submission.zip` from kernel `guozhaojie/nemotron-v83-svanik-stream-relay`, latest completed version, with description `v83 official Svanik stream relay`.

## v83 official submission pending (2026-06-15 CST)

Decision:
- User explicitly approved official submission after reviewing v82 `ERROR` and v83 stream-relay evidence.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v83-svanik-stream-relay`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v83 official Svanik stream relay`.
- Submission ref: `53713109`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Pre-submit guardrail evidence:
- `kaggle kernels files` confirmed `submission.zip` exists for v83.
- Recent submissions list showed no prior v83 official submission.
- v83 runtime logs confirmed root-only output entries `adapter_config.json` and `adapter_model.safetensors`.
- v83 output preserved source adapter size `3611499192` bytes and normalized the base model path to `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.

Comparison target:
- Current official best remains public `0.86`.
- v82 ref `53710861` errored, so v83 is the corrected Svanik stream-relay attempt.

Next action:
- Monitor ref `53713109` until complete.
- If score is `0.87`, refresh leaderboard immediately.
- If it errors, ties `0.86`, or regresses, preserve existing `0.86` submissions as best official result.

## v83 official result: Svanik stream relay errored (2026-06-15 CST)

Submission:
- Ref: `53713109`.
- Description: `v83 official Svanik stream relay`.
- Status: `SubmissionStatus.ERROR`.
- Public score: none.

Evidence:
- Kaggle submissions CLI on 2026-06-15 22:19 CST showed ref `53713109` in `SubmissionStatus.ERROR`.
- v82 and v83 both errored despite different Svanik packaging strategies.

Interpretation:
- Stop the Svanik engine-ensemble relay family. The public artifact may not be official-scorer compatible for this competition path, even when the local output is root-only and config-normalized.
- Do not resubmit v82/v83 unchanged.
- Guardrail added to local `kaggle-submission-guardrails` skill: `SubmissionStatus.ERROR` with blank `publicScore` is now treated as scorer load/validation failure; stop unchanged resubmission, compare against known-scoring artifacts, and stop a public artifact family after repeated scorer errors.

Fallback candidate:
- The cleanest remaining low-cost option is the already completed KeithTyser v81 relay:
  - Kernel `guozhaojie/nemotron-v81-keithtyser-hk-to-kn-lmhead`, version `1`.
  - Output root-only `submission.zip`.
  - Adapter size `3554384888` bytes.
  - Metadata labels it as a canonical merged `0.86-class` public adapter.
- Expected value is lower than a true `0.87` route, but it is structurally cleaner than Svanik and may still help hidden precision/private shakeout.

## Leaderboard tie-band diagnostic: why public 0.86 ranks differ widely (2026-06-15 CST)

Fresh leaderboard snapshot:
- Download path: `outputs/kaggle/leaderboard_download_20260615_2158/`.
- CSV timestamp: `2026-06-15T13:58:43`.
- Total teams: `4325`.
- Team `guozhaojie`: rank `474`, public score `0.86`, submission count `19`, latest best-row timestamp shown as `2026-06-15 06:43:56`.
- Approximate top-10% cutoff: rank `433`, also public score `0.86`.

Score bands:
- `0.91`: rank `1`, count `1`.
- `0.88`: ranks `2-6`, count `5`.
- `0.87`: ranks `7-65`, count `59`.
- `0.86`: ranks `66-1670`, count `1605`.
- `0.85`: ranks `1671-2200`, count `530`.
- `0.84`: ranks `2201-2439`, count `239`.

Interpretation:
- The displayed public score is not enough to infer exact placement. A visible `0.86` covers a very large rank interval.
- The rank ordering inside the visible `0.86` band is likely determined by hidden score precision and/or Kaggle tie-breaking such as when the best score was first achieved; the downloaded CSV exposes only the displayed `0.86`, not the exact internal ordering signal.
- Our current position is `409/1605` within the visible `0.86` band, about `41` ranks behind the approximate top-10% cutoff.

Final-sprint implication:
- Repeating artifacts that merely tie visible `0.86` may still move rank only if they improve hidden precision/tie ordering, but this is hard to observe.
- A visible `0.87` remains the clean medal-safe public target.
- If no credible `0.87` route remains, the best fallback is to submit differentiated `0.86` candidates that may shift private leaderboard behavior, while preserving known stable `0.86` submissions.

## v84 completed: Ayomide rank-309 public artifact relay ready for approval (2026-06-15 CST)

Rationale:
- User asked for directions that could plausibly move the team from rank `474` into the top `400`.
- Latest public leaderboard snapshot showed `Ayomide2000` at rank `309`, public score `0.86`, with team member username `ayomide2000`.
- This is stronger evidence than a generic `0.86-class` artifact because it is already positioned well inside the visible `0.86` tie band.

Public prior-art scan:
- `ayomide2000/finding-nemo`: author rank `309`, visible public score `0.86`, kernel source output files visible.
- `debatreyabiswas/nemotroncomp-best0-86-solution-nvidia-under-5min`: author rank `410`, visible public score `0.86`, useful backup but less attractive than Ayomide for a top-400 move.
- `evgendvorkin/nemotron-3-nano-lora-adapter-submission`: author rank `529`, lower priority than current team rank `474`.
- `lopure/lora-adapter-ensembling-experiments`: author rank `1189`, not useful for this objective.

Kernel:
- Private kernel: `guozhaojie/nemotron-v84-ayomide309-artifact-relay`.
- Kernel version: `1`.
- Status: `KernelWorkerStatus.COMPLETE`.
- Source: public kernel output `ayomide2000/finding-nemo`.

Runtime source evidence:
- Source candidate dir: `/kaggle/input/notebooks/ayomide2000/finding-nemo`.
- Source files:
  - `adapter_config.json`: `580` bytes.
  - `adapter_model.safetensors`: `3554384888` bytes.
  - `converted_adapter_model.safetensors`: `3554420624` bytes.
  - `submission.zip`: `3270301847` bytes.
- Source `submission.zip` entries:
  - `adapter_config.json`, uncompressed `580`, compressed `293`.
  - `adapter_model.safetensors`, uncompressed `3554420624`, compressed `3270301176`.
- Selected model file: `converted_adapter_model.safetensors`.
- Selected model partial sha256 head+tail16MB: `c49d188fbcc994d008873d437a6a6a23fc1e3e78dd25d69445b301bdd8362c8c`.

Output evidence:
- Output zip entries: `adapter_config.json`, `adapter_model.safetensors`.
- Output uncompressed sizes: `adapter_config.json=580`, `adapter_model.safetensors=3554420624`.
- Output zip bytes: `3554421582`.
- Config summary:
  - `peft_type=LORA`.
  - `r=32`.
  - `lora_alpha=32`.
  - `base_model_name_or_path=nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`.
  - `inference_mode=true`.
  - target modules: `k_proj`, `o_proj`, `in_proj`, `q_proj`, `up_proj`, `v_proj`, `down_proj`, `out_proj`, `lm_head`.

Risk:
- Ayomide's current public kernel status is `KernelWorkerStatus.ERROR`, but its successful output artifacts remain visible and the author's leaderboard row is strong.
- v84 uses artifact relay, not notebook rerun. This avoids the failing notebook cell and preserves the exposed successful adapter content.

Decision:
- v84 is currently the strongest candidate for a top-400 push because it mirrors an artifact family whose public owner is rank `309` within the `0.86` band.
- It is not a visible `0.87` route, so it cannot guarantee medal safety, but it is more directly aligned with the rank objective than v81.
- Do not official-submit without explicit user approval.

## v84 official submission pending (2026-06-15 CST)

Decision:
- User explicitly approved official submission for the Ayomide rank-309 public artifact relay.

Submission:
- Competition: `nvidia-nemotron-model-reasoning-challenge`.
- Kernel: `guozhaojie/nemotron-v84-ayomide309-artifact-relay`.
- Kernel version: `1`.
- Output file: `submission.zip`.
- Description: `v84 official Ayomide rank309 artifact relay`.
- Submission ref: `53714795`.
- Status immediately after submission: `SubmissionStatus.PENDING`.
- Public score: pending.

Pre-submit guardrail evidence:
- `kaggle-submission-guardrails` preflight passed with no warnings.
- `kaggle kernels files` confirmed v84 `submission.zip` exists.
- Recent submissions list showed no prior v84 official submission.
- Runtime logs confirmed source artifact from `ayomide2000/finding-nemo` and root-only output entries `adapter_config.json` and `adapter_model.safetensors`.

Comparison target:
- Current official best before v84 remains public `0.86`.
- Rank objective: improve from rank `474` toward top `400`; public prior-art owner Ayomide2000 is rank `309` with visible public score `0.86`.

Next action:
- Monitor ref `53714795` until complete.
- If it completes at `0.86`, refresh leaderboard to see whether hidden/tie ordering moved rank.
- If it errors, apply the `SubmissionStatus.ERROR` guardrail and avoid unchanged resubmission.

## v84 official result: Ayomide rank-309 artifact relay tied 0.86 but did not improve rank (2026-06-16 CST)

Submission:
- Ref: `53714795`.
- Description: `v84 official Ayomide rank309 artifact relay`.
- Status: `SubmissionStatus.COMPLETE`.
- Public score: `0.86`.

Leaderboard refresh:
- Download path: `outputs/kaggle/leaderboard_download_20260616_0000_after_v84/`.
- CSV timestamp: `2026-06-15T16:00:53`.
- Total teams: `4330`.
- Team `guozhaojie`: rank `475`, public score `0.86`, submission count `20`, latest best-row timestamp `2026-06-15 14:50:31`.
- Previous reference rank before v84: `474`.
- Rank delta: `-1` place; no movement toward top `400`.

Score bands after v84:
- `0.91`: rank `1`, count `1`.
- `0.89`: rank `2`, count `1`.
- `0.88`: ranks `3-6`, count `4`.
- `0.87`: ranks `7-66`, count `60`.
- `0.86`: ranks `67-1675`, count `1609`.
- `0.85`: ranks `1676-2205`, count `530`.

Interpretation:
- v84 reproduced the visible `0.86` score but did not improve hidden/tie ordering; it slightly worsened public rank because the leaderboard grew and/or other teams moved.
- The Ayomide artifact relay did not transfer the source owner's rank-309 ordering advantage to our account.
- Stop spending final submissions on additional `0.86` artifact relays unless there is a concrete new signal beyond visible score and source-owner rank.

Next action:
- Pivot back to a visible `0.87` training route for any further work, especially a faithful reproduction of a public `nemotron-087-training` style route, rather than more `0.86` relay variants.

## Competition ended: final public snapshot and handoff (2026-06-16 CST)

Final public snapshot checked after the deadline:
- Download path: `outputs/kaggle/leaderboard_download_20260616_0002_final_public/`.
- CSV timestamp: `2026-06-15T16:03:02`.
- Total teams: `4330`.
- Team `guozhaojie`: rank `475`, public score `0.86`, submission count `20`, latest best-row timestamp `2026-06-15 14:50:31`.
- Rank `400` also had visible public score `0.86`.

Final submitted state:
- Final latest submission: v84 ref `53714795`, `SubmissionStatus.COMPLETE`, public score `0.86`.
- Current best visible public score remains `0.86`.
- v84 did not improve rank from the pre-v84 reference rank `474`; final checked public rank is `475`.

Conclusion:
- The late artifact-relay sprint successfully preserved the `0.86` score but did not move hidden/tie ordering enough for top `400`.
- Further `0.86` artifact relays should be considered exhausted unless a future postmortem reveals a concrete structural signal.
- Any post-competition technical writeup should focus on the plateau: public artifact relays can reach `0.86`, but medal-safe progress likely required an earlier faithful `0.87` training route or a stronger validation proxy for hidden/tie precision.

## Final retro and next-competition playbook created (2026-06-16 CST)

Artifacts:
- `docs/NEMOTRON_FINAL_RETRO_20260616.md`
- `docs/NEXT_KAGGLE_PLAYBOOK.md`
- Local Codex skill: `C:\Users\jie13\.codex\skills\kaggle-competition-playbook`

Corrected medal-rule note:
- For 1000+ team Kaggle competition medals, bronze is top `10%`, silver is top `5%`, and gold is top `10 + 0.2%`.
- At `4330` final checked public rows, the approximate public bronze cutoff is rank `433`.
- Team `guozhaojie` final checked public rank `475` is about `42` public ranks outside the bronze cutoff, pending any private/final shake-up.

Reusable lesson:
- The next Kaggle run should start with rule/medal math, public prior-art reproduction, validation calibration, submission-budget tracking, and plateau stop rules before heavy self-owned training.
