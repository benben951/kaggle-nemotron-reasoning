#!/usr/bin/env python3
"""Compute Kaggle competition medal cutoff ranks from team count.

This implements the Kaggle competition-medal progression table:
- 0-99 teams: bronze top 40%, silver top 20%, gold top 10%.
- 100-249 teams: bronze top 40%, silver top 20%, gold top 10.
- 250-999 teams: bronze top 100, silver top 50, gold top 10 + 0.2%.
- 1000+ teams: bronze top 10%, silver top 5%, gold top 10 + 0.2%.

Percentage calculations are rounded down.
"""

from __future__ import annotations

import argparse
import math


def gold_top_10_plus_02_percent(team_count: int) -> int:
    # Kaggle describes this as one extra gold for every 500 teams.
    return 10 + team_count // 500


def cutoffs(team_count: int) -> dict[str, int]:
    if team_count < 0:
        raise ValueError("team_count must be non-negative")

    if team_count < 100:
        return {
            "gold": math.floor(team_count * 0.10),
            "silver": math.floor(team_count * 0.20),
            "bronze": math.floor(team_count * 0.40),
        }
    if team_count < 250:
        return {
            "gold": min(10, team_count),
            "silver": math.floor(team_count * 0.20),
            "bronze": math.floor(team_count * 0.40),
        }
    if team_count < 1000:
        return {
            "gold": min(gold_top_10_plus_02_percent(team_count), team_count),
            "silver": min(50, team_count),
            "bronze": min(100, team_count),
        }
    return {
        "gold": min(gold_top_10_plus_02_percent(team_count), team_count),
        "silver": math.floor(team_count * 0.05),
        "bronze": math.floor(team_count * 0.10),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("team_count", type=int, help="Number of leaderboard teams")
    parser.add_argument("--rank", type=int, help="Optional team rank to classify")
    args = parser.parse_args()

    result = cutoffs(args.team_count)

    print(f"teams: {args.team_count}")
    print(f"gold_cutoff_rank: {result['gold']}")
    print(f"silver_cutoff_rank: {result['silver']}")
    print(f"bronze_cutoff_rank: {result['bronze']}")

    if args.rank is not None:
        pct = args.rank / args.team_count * 100 if args.team_count else float("inf")
        if args.rank <= result["gold"]:
            medal = "gold"
        elif args.rank <= result["silver"]:
            medal = "silver"
        elif args.rank <= result["bronze"]:
            medal = "bronze"
        else:
            medal = "none"
        print(f"rank: {args.rank}")
        print(f"rank_percent: {pct:.2f}%")
        print(f"public_medal_band: {medal}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
