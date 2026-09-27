#!/usr/bin/env python3
"""Filter the site's dated game-guide catalog without external packages."""

import argparse
import csv
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "data" / "game_guide_catalog.csv"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", choices=("five-player", "free", "non-horror"))
    parser.add_argument("--min-players", type=int, default=0)
    args = parser.parse_args()
    if args.min_players < 0:
        parser.error("--min-players must be zero or greater")

    with CATALOG.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    for row in rows:
        if args.guide and row["guide"] != args.guide:
            continue
        cap_text = row["official_player_cap"]
        if args.min_players and not cap_text:
            status = "CAP NOT VERIFIED"
        elif args.min_players and int(cap_text) < args.min_players:
            continue
        else:
            status = "listed"
        print(f'{row["game"]} | {row["guide"]} | cap: {cap_text or "unknown"} | {status}')
        print(f'  mode: {row["cap_basis"]}')
        print(f'  source: {row["site_source_url"]}')


if __name__ == "__main__":
    main()
