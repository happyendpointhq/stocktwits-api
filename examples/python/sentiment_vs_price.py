"""Does Stocktwits sentiment move with the price, or ahead of it? Joins a symbol's daily
bullish share (last ~61 days) with its daily closes and measures both.

    python sentiment_vs_price.py AAPL
    python sentiment_vs_price.py TSLA --csv tsla.csv

Two calls per symbol. Two months of data is a small sample: treat the result as a
description of this window, not as a trading signal.
"""

import argparse
import csv
from statistics import mean, median

from client import correlation, daily_closes, get

parser = argparse.ArgumentParser()
parser.add_argument("symbol")
parser.add_argument("--csv", help="also write the joined daily rows to this file")
args = parser.parse_args()
symbol = args.symbol.upper()

sentiment = get("/sentiment-daily", symbol=symbol)["data"]  # newest first, weekends included
closes = daily_closes(get("/price-chart", symbol=symbol, range="3M"))

days = sorted(closes)
rows = []
bullish = {row["timestamp"]: row["bullish"] for row in sentiment}
for i in range(1, len(days)):
    day = days[i]
    if day not in bullish:
        continue
    ret = closes[day] / closes[days[i - 1]] - 1
    nxt = closes[days[i + 1]] / closes[day] - 1 if i + 1 < len(days) else None
    rows.append({"date": day, "bullish_pct": bullish[day], "close": closes[day],
                 "return": ret, "next_day_return": nxt})

if len(rows) < 10:
    raise SystemExit(f"{symbol}: only {len(rows)} trading days with both sentiment and price")

print(f"{symbol}: {len(rows)} trading days, {rows[0]['date']} to {rows[-1]['date']}")
print(f"  bullish share: median {median(r['bullish_pct'] for r in rows):.1f}%, "
      f"range {min(r['bullish_pct'] for r in rows):.1f}% to {max(r['bullish_pct'] for r in rows):.1f}%")

same = correlation([r["bullish_pct"] for r in rows], [r["return"] for r in rows])
paired = [r for r in rows if r["next_day_return"] is not None]
ahead = correlation([r["bullish_pct"] for r in paired], [r["next_day_return"] for r in paired])
print(f"  correlation with the same day's return: {same:+.2f}" if same is not None else "  same day: n/a")
print(f"  correlation with the next day's return: {ahead:+.2f}" if ahead is not None else "  next day: n/a")

cut = median(r["bullish_pct"] for r in paired)
high = [r["next_day_return"] for r in paired if r["bullish_pct"] > cut]
low = [r["next_day_return"] for r in paired if r["bullish_pct"] <= cut]
if high and low:
    print(f"  next-day return after more bullish days: {mean(high):+.2%} ({len(high)} days); "
          f"after less bullish days: {mean(low):+.2%} ({len(low)} days)")

swings = sorted(zip(rows, rows[1:]), key=lambda p: -abs(p[1]["bullish_pct"] - p[0]["bullish_pct"]))[:5]
print("  biggest changes in bullish share from one trading day to the next:")
for before, after in swings:
    print(f"    {after['date']}  {before['bullish_pct']:.1f}% -> {after['bullish_pct']:.1f}%  "
          f"price {after['return']:+.2%} that day")

if args.csv:
    with open(args.csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {len(rows)} rows to {args.csv}")
