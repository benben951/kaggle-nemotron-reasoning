"""Extract validation_generation_checks from Kaggle streamed kernel logs.

Kaggle CLI logs can be newline-delimited JSON chunks where stdout data is split
across many lines. This helper reconstructs stdout and parses the validation
checks JSON array emitted by our notebooks.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_stream_text(path: Path) -> str:
    parts: list[str] = []
    raw = path.read_text(encoding="utf-8", errors="replace")
    for line in raw.splitlines():
        candidate = line.strip()
        if candidate.startswith(","):
            candidate = candidate[1:]
        if not candidate.startswith("{"):
            parts.append(line + "\n")
            continue
        try:
            obj = json.loads(candidate)
        except json.JSONDecodeError:
            parts.append(line + "\n")
            continue
        data = obj.get("data")
        if isinstance(data, str):
            parts.append(data)
    return "".join(parts)


def parse_json_after_marker(text: str, marker: str) -> object:
    idx = text.find(marker)
    if idx < 0:
        raise ValueError(f"marker not found: {marker}")
    s = text[idx + len(marker):]
    start = s.find("[")
    if start < 0:
        raise ValueError("JSON array start not found after marker")
    depth = 0
    in_string = False
    escape = False
    for i, ch in enumerate(s[start:], start=start):
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
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return json.loads(s[start:i + 1])
    raise ValueError("JSON array did not close")


def summarize(checks: list[dict]) -> dict:
    by_family: dict[str, list[dict]] = defaultdict(list)
    for row in checks:
        by_family[str(row.get("task_family", "unknown"))].append(row)
    family_summary = {}
    for family, rows in sorted(by_family.items()):
        family_summary[family] = {
            "total": len(rows),
            "fixed_boxed": sum(1 for r in rows if r.get("fixed_boxed")),
            "fixed_final_box_line": sum(1 for r in rows if r.get("fixed_final_box_line")),
            "fixed_correct": sum(1 for r in rows if r.get("fixed_correct")),
        }
    return {
        "total": len(checks),
        "fixed_boxed": sum(1 for r in checks if r.get("fixed_boxed")),
        "fixed_final_box_line": sum(1 for r in checks if r.get("fixed_final_box_line")),
        "fixed_correct": sum(1 for r in checks if r.get("fixed_correct")),
        "family_breakdown": family_summary,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--summary-out", type=Path)
    args = parser.parse_args()

    text = read_stream_text(args.log)
    checks = parse_json_after_marker(text, "validation_generation_checks ")
    if not isinstance(checks, list):
        raise TypeError("validation checks payload is not a list")
    summary = summarize(checks)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.summary_out:
        args.summary_out.parent.mkdir(parents=True, exist_ok=True)
        args.summary_out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
