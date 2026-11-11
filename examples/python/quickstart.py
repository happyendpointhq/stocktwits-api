"""The symbols trending on Stocktwits right now, then the sentiment reading of the first one.

    python quickstart.py
    python quickstart.py crypto
"""

import sys

from client import get

asset_class = sys.argv[1] if len(sys.argv) > 1 else "equities"

trending = get("/trending-symbols", region="US", asset_class=asset_class, limit=10)
print(f"Trending on Stocktwits ({asset_class})\n")
for s in trending["symbols"]:
    print(f"{s['rank']:>2}. {s['symbol']:<8} {s['title'][:40]:<40} score {s['trending_score']:>6.2f}  "
          f"{s['watchlist_count']:>9,} watchers")

top = trending["symbols"][0]
if top["trends"].get("summary"):
    print(f"\nWhy {top['symbol']} is trending: {top['trends']['summary']}")

reading = get("/sentiment", symbol=top["symbol"])["data"]
print(f"\n{top['symbol']} sentiment")
for window in ("now", "24h"):
    s, v = reading["sentiment"][window], reading["messageVolume"][window]
    # `label` and `labelNormalized` can disagree (BULLISH next to BEARISH): label is the raw
    # reading, labelNormalized compares it with the symbol's own history.
    print(f"  {window:<4} sentiment {s['value']:+.3f} ({s['label']}, {s['labelNormalized']} for this symbol)  "
          f"message volume {v['value']:,} ({v['label']})")
