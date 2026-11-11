# Sample responses

Real `200` responses for four Stocktwits API endpoints, taken on 3 November 2026 during US
market hours (so the newest price bar and sentiment day are still in progress). The trending
list is cut to its first three symbols, and each symbol's `BusinessDescription` is removed
because it can name founders and officers. There are no messages or account data in these
files. Field names and values are otherwise unchanged. File names follow the endpoint path.

| File | Request |
|---|---|
| `trending-symbols.json` | `GET /trending-symbols?region=US&asset_class=equities&limit=10` |
| `sentiment.json` | `GET /sentiment?symbol=AAPL` |
| `sentiment-daily.json` | `GET /sentiment-daily?symbol=AAPL` |
| `price-chart.json` | `GET /price-chart?symbol=AAPL&range=3M` |

They are useful for writing parsers and tests before you subscribe. Sentiment and prices
change by the minute, so do not hard-code these values.
