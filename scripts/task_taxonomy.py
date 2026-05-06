from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def classify_prompt(prompt: str) -> str:
    text = prompt.lower()
    if "8-bit binary" in text or "bit manipulation" in text:
        return "bit_manipulation"
    if "decrypt" in text or "encryption" in text:
        return "text_cipher"
    if "alice's wonderland" in text:
        return "alice_reasoning_other"
    if "grid" in text or "matrix" in text:
        return "grid_or_matrix"
    if "calculate" in text or "determine" in text:
        return "symbolic_reasoning"
    return "unknown"


def main() -> None:
    train = pd.read_csv(RAW / "train.csv")
    train["task_family"] = train["prompt"].map(classify_prompt)
    counts = train["task_family"].value_counts().rename_axis("task_family").reset_index(name="count")
    print(counts.to_string(index=False))

    out = ROOT / "docs" / "task_family_counts.csv"
    counts.to_csv(out, index=False)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
