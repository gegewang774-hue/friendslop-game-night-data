# Friendslop Game Night Data

A small, source-traceable catalog and command-line filter for choosing a multiplayer game night. The catalog transcribes recommendations and player-count claims from three public guides; it is a dated editorial snapshot, not a live store feed or a claim of hands-on playtesting.

The underlying group-fit questions come from the [BestFriendslopGames guide to friendslop](https://bestfriendslopgames.com/what-is-friendslop/).

## Files

- `data/game_guide_catalog.csv` — one row per game-guide appearance, with the guide URL, official Steam listing, stated player cap where available, and the guide's check date where stated. A game can appear in more than one guide.
- `docs/selection_rules.md` — the site's editorial tests expressed as reusable questions, with limits on what they can establish.
- `tools/find_games.py` — a standard-library-only filter for guide category and minimum group size. It does not score or rank games.

## Use

```sh
python tools/find_games.py --guide five-player --min-players 5
python tools/find_games.py --guide free
python tools/find_games.py --guide non-horror --min-players 8
```

Blank player caps mean the cited guide did not supply a usable cap for that row. The tool keeps those rows separate as `CAP NOT VERIFIED` when a minimum is requested. A maximum-player figure may apply only to the mode named in `cap_basis`; read that column and recheck the official listing before inviting or buying for a group.

## Provenance and limitations

Each CSV row points to its source guide and an official Steam listing. The `site_checked_date` field copies dates explicitly stated on the source guide; an empty field means that guide did not state a check date. The CSV is a transcription of published claims, with light normalization of game names and guide categories. It contains no playtime, performance, review, or experimental data. Store details can change. The selection rules are editorial heuristics, not validated measures of game quality.
