import argparse
import json
import sys
from pathlib import Path


def _fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)

def _read_text_with_bom(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xff\xfe"):
        return data.decode("utf-16le").lstrip("\ufeff")
    if data.startswith(b"\xfe\xff"):
        return data.decode("utf-16be").lstrip("\ufeff")
    if data.startswith(b"\xef\xbb\xbf"):
        return data.decode("utf-8-sig").lstrip("\ufeff")
    return data.decode("utf-8").lstrip("\ufeff")


def _load_summary(path: Path) -> dict:
    if not path.exists():
        _fail(f"Summary file not found: {path}")
    try:
        return json.loads(_read_text_with_bom(path))
    except json.JSONDecodeError as e:
        _fail(f"Failed to parse summary JSON: {e}")
    except UnicodeDecodeError as e:
        _fail(f"Failed to decode summary file as UTF-8/UTF-16: {e}")


def _main() -> int:
    ap = argparse.ArgumentParser(description="Nemotron submission gate based on validation metrics")
    ap.add_argument("summary_json", help="JSON output from summarize_kaggle_kernel_log.py --json")
    ap.add_argument("--min-fixed-correct", type=int, default=26, help="Minimum fixed_correct to allow submit")
    ap.add_argument(
        "--min-strict-single-boxed",
        type=int,
        default=20,
        help="Minimum strict_single_boxed to allow submit",
    )
    args = ap.parse_args()

    summary = _load_summary(Path(args.summary_json).expanduser().resolve())
    fixed_correct = int(summary.get("fixed_correct", 0))
    strict_single_boxed = int(summary.get("strict_single_boxed", 0))
    fixed_final_box_line = int(summary.get("fixed_final_box_line", 0))
    run_label = summary.get("run_label", "")

    reasons = []
    if fixed_correct < args.min_fixed_correct:
        reasons.append(
            f"fixed_correct {fixed_correct} < min_fixed_correct {args.min_fixed_correct}"
        )
    if strict_single_boxed < args.min_strict_single_boxed:
        reasons.append(
            f"strict_single_boxed {strict_single_boxed} < min_strict_single_boxed {args.min_strict_single_boxed}"
        )
    if fixed_final_box_line < strict_single_boxed:
        reasons.append(
            "fixed_final_box_line is unexpectedly lower than strict_single_boxed; check evaluator consistency"
        )

    print("submission_gate")
    print(f"- run_label: {run_label}")
    print(f"- fixed_correct: {fixed_correct}")
    print(f"- strict_single_boxed: {strict_single_boxed}")
    print(f"- fixed_final_box_line: {fixed_final_box_line}")
    print(f"- threshold.min_fixed_correct: {args.min_fixed_correct}")
    print(f"- threshold.min_strict_single_boxed: {args.min_strict_single_boxed}")

    if reasons:
        print("- decision: BLOCK")
        print("- reasons:")
        for r in reasons:
            print(f"  - {r}")
        return 1

    print("- decision: ALLOW")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
