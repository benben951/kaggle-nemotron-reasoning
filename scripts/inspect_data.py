from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def main() -> None:
    train = pd.read_csv(RAW / "train.csv")
    test = pd.read_csv(RAW / "test.csv")

    print("train shape:", train.shape)
    print("test shape:", test.shape)
    print("train columns:", list(train.columns))
    print("test columns:", list(test.columns))
    print("missing train:")
    print(train.isna().sum())
    print("missing test:")
    print(test.isna().sum())

    overlap = set(test["id"]).intersection(set(train["id"]))
    print("test/train id overlap:", len(overlap), sorted(overlap)[:10])

    print("\nSample train rows:")
    print(train.head(3).to_string(index=False))


if __name__ == "__main__":
    main()
