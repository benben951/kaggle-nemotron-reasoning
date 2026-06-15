import argparse
import json
import sys
from pathlib import Path


def _fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)

def _write_utf8_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _extract_validation_json(log_text: str) -> dict:
    marker = "validation_generation_summary"
    idx = log_text.rfind(marker)
    if idx < 0:
        _fail("Could not find 'validation_generation_summary' in log")

    brace_start = log_text.find("{", idx)
    if brace_start < 0:
        _fail("Found marker but no JSON object start '{'")

    depth = 0
    in_string = False
    escape = False
    end = None
    for i in range(brace_start, len(log_text)):
        ch = log_text[i]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        _fail("Could not find matching JSON object end for validation summary")

    obj_text = log_text[brace_start:end]
    try:
        return json.loads(obj_text)
    except json.JSONDecodeError as e:
        _fail(f"Failed to parse validation summary JSON: {e}")


def _normalize_log_text(raw: str) -> str:
    lines = []
    for ln in raw.splitlines():
        s = ln.strip()
        if not s:
            continue
        try:
            item = json.loads(s.lstrip(","))
            data = item.get("data")
            if isinstance(data, str):
                lines.append(data)
            continue
        except Exception:
            pass
        lines.append(ln)
    return "".join(lines)


def _main() -> int:
    ap = argparse.ArgumentParser(description="Extract Nemotron validation metrics from Kaggle kernel log")
    ap.add_argument("log_path", help="Path to kaggle kernel .log file")
    ap.add_argument("--json", action="store_true", help="Print JSON only")
    ap.add_argument(
        "--out",
        help="Optional path to write JSON summary (UTF-8). Avoids PowerShell '>' UTF-16 redirection issues.",
    )
    args = ap.parse_args()

    p = Path(args.log_path).expanduser().resolve()
    if not p.exists():
        _fail(f"File not found: {p}")
    raw = p.read_text(encoding="utf-8", errors="replace")
    text = _normalize_log_text(raw)
    summary = _extract_validation_json(text)

    out = {
        "run_label": summary.get("run_label", ""),
        "total": int(summary.get("total", 0)),
        "fixed_boxed": int(summary.get("fixed_boxed", 0)),
        "fixed_loose_boxed": int(summary.get("fixed_loose_boxed", 0)),
        "fixed_final_box_line": int(summary.get("fixed_final_box_line", 0)),
        "strict_single_boxed": int(summary.get("strict_single_boxed", 0)),
        "fixed_correct": int(summary.get("fixed_correct", 0)),
        # Older notebooks used `by_family`; newer ones use `family_breakdown`.
        "family_breakdown": summary.get("family_breakdown") or summary.get("by_family") or {},
    }

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        _write_utf8_json(out_path, out)

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    print("validation_summary")
    for k in [
        "run_label",
        "total",
        "fixed_boxed",
        "fixed_final_box_line",
        "strict_single_boxed",
        "fixed_correct",
    ]:
        print(f"- {k}: {out[k]}")
    print("- family_breakdown:")
    print(json.dumps(out["family_breakdown"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
