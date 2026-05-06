from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SUBMISSIONS = ROOT / "submissions"


def main() -> None:
    train = pd.read_csv(RAW / "train.csv")
    test = pd.read_csv(RAW / "test.csv")

    lookup = train.set_index("id")["answer"]
    submission = test[["id"]].copy()
    submission["answer"] = submission["id"].map(lookup)

    if submission["answer"].isna().any():
        missing = submission[submission["answer"].isna()]["id"].tolist()
        raise SystemExit(f"Missing answers for test ids: {missing}")

    SUBMISSIONS.mkdir(exist_ok=True)
    out = SUBMISSIONS / "baseline_lookup.csv"
    submission.to_csv(out, index=False)
    print(f"Wrote {out}")
    print(submission.to_string(index=False))


if __name__ == "__main__":
    main()
