# Kaggle Submission Guardrails

This project treats Kaggle process mistakes as bugs, not as memory issues.

## v76 Lesson

Symptom:
- v76 kernel version 1 failed with `FileNotFoundError: No Huikang adapter dir found`.

Root cause:
- Runtime discovery assumed source paths would contain specific text such as `huikang` and `nemotron-adapter`.
- The notebook did not first print broad `/kaggle/input` diagnostics, so the failure was harder to debug than necessary.

Guardrail added:
- Created global Codex skill: `C:\Users\jie13\.codex\skills\kaggle-submission-guardrails\SKILL.md`.
- Created preflight script: `C:\Users\jie13\.codex\skills\kaggle-submission-guardrails\scripts\kaggle_kernel_preflight.py`.
- v76/v77 preflight now verifies:
- no UTF-8 BOM in `kernel-metadata.json`;
- metadata JSON parses;
- `code_file` exists;
- notebook code parses;
- versioned Kaggle model source files are visible via Kaggle CLI;
- expected `adapter_config.json` and `adapter_model.safetensors` are present.

Second lesson from v76 version 2:
- Kaggle CLI source visibility is necessary but not sufficient.
- v76 v2 proved Huikang v20 files were visible via CLI, but runtime `/kaggle/input` still contained only competition and notebook sources, with no model mount.
- Future kernels must print runtime source evidence before conversion: top-level `/kaggle/input`, candidate files, chosen source path, and output zip entries.

## Required Commands Before Future Pushes

For v76/v77-style adapter kernels:

```powershell
python C:\Users\jie13\.codex\skills\kaggle-submission-guardrails\scripts\kaggle_kernel_preflight.py <kernel_dir> --check-remote --expect-model-file adapter_config.json --expect-model-file adapter_model.safetensors
```

After push:

```powershell
kaggle kernels status <owner>/<kernel>
kaggle kernels logs <owner>/<kernel>
kaggle kernels files <owner>/<kernel>
```

## Submission Rule

Do not submit officially until:

- the exact kernel version is known;
- `kaggle kernels files` shows the expected output artifact;
- lightweight logs confirm source path and conversion/output evidence;
- the user explicitly approves the official submission.

## Final Nemotron Lessons

Final-state process lessons from the 2026-06-16 retro:

- Compute Kaggle competition medal cutoffs on day 0. For 1000+ team Kaggle competition medals, bronze is top `10%`, silver is top `5%`, and gold is top `10 + 0.2%`; do not use the incorrect `10/20/30%` table.
- Treat a wide rounded-score band as a plateau risk. In Nemotron, public `0.86` covered ranks `67-1675`, so repeated visible `0.86` submissions did not guarantee medal movement.
- Stop a same-family route after repeated `SubmissionStatus.ERROR` with blank public score; this means scorer load/validation failure, not a low model score.
- Do not rely on public notebook titles such as `0.87` unless the exact artifact transfer is proven by an official submission.
- Source-owner rank inside the same rounded score band is not enough evidence that an artifact relay will transfer tie ordering.
- Every process failure must produce a symptom/root-cause/guardrail entry in `docs/EXPERIMENTS.md` or a reusable skill.
