# Stocktwits API and Scraper

The Stocktwits API returns data from Stocktwits, the social network for traders and
investors, as JSON: bullish and bearish sentiment for any stock or crypto symbol (live, daily
and as a chart back to 2018), message volume, trending symbols and rankings, message streams
by symbol and topic, real-time quotes and price charts, fundamentals, watcher counts,
financial news, earnings calendars, earnings call transcripts and polls. It is a REST API, so
you get Stocktwits sentiment in your own code without building and maintaining a Stocktwits
scraper.

Built and maintained by [Happy Endpoint](https://happyendpoint.com/library/stocktwits-api?utm_source=github&utm_medium=readme&utm_campaign=stocktwits-api).

- Subscribe and test every endpoint on RapidAPI: https://rapidapi.com/happyendpoint/api/stocktwits5
- Product page: https://happyendpoint.com/library/stocktwits-api?utm_source=github&utm_medium=readme&utm_campaign=stocktwits-api

---

## At a glance

| | |
|---|---|
| Base URL | `https://stocktwits5.p.rapidapi.com` |
| Auth | `x-rapidapi-key` and `x-rapidapi-host` headers |
| Endpoints | 56, all `GET` |
| Coverage | US and Indian equities, ETFs, indices, futures, crypto (`BTC.X`), forex and private companies (`.P`) |
| Sentiment | Live with 15-minute and 24-hour change, daily bullish and bearish shares for about 61 days, charts from 5-minute to daily points |
| Batch calls | Quotes, sparklines, fundamentals and symbol lookups take up to 100 symbols |
| Format | JSON, every response wrapped in `{"success": true, "data": {...}}` |

---

## What data you get

**Sentiment**
- A symbol's sentiment score and message volume now, over 15 minutes and 24 hours, with labels
- The daily bullish and bearish split of a symbol's messages
- Sentiment and message volume charts, and the market-wide Stocktwits Sentiment Index for the US, India and crypto

**Trending and rankings**
- Trending symbols with a trending score and an AI summary of why
- Most active, most bullish, most bearish, top gainers, top losers and most new watchers
- Popular messages and trending topics per symbol

**Market data and fundamentals**
- Real-time quotes, OHLCV price charts from one day to five years, sparklines and market-cap charts
- Fundamentals, EPS against estimates, watcher counts and growth, crypto profiles and private-company funding rounds

**Messages, news and earnings**
- Message streams by symbol, topic or site-wide feed, filtered by bullish or bearish tag, and full-text message search
- Newsroom feeds and symbol news, earnings calendars for the US and India, earnings calls and full transcripts
- Polls, market holidays and trading sessions

---

## Quick start

### 1. Get an API key

Subscribe on [RapidAPI](https://rapidapi.com/happyendpoint/api/stocktwits5). Current plans are listed there. Copy `.env.example` to `.env` and paste your key.

### 2. Make a request

```bash
curl "https://stocktwits5.p.rapidapi.com/sentiment-daily?symbol=AAPL" \
  -H "x-rapidapi-host: stocktwits5.p.rapidapi.com" \
  -H "x-rapidapi-key: YOUR_RAPIDAPI_KEY"
```

### Python

```bash
pip install -r requirements.txt
cd examples/python
python quickstart.py
```

```python
from client import get

days = get("/sentiment-daily", symbol="AAPL")["data"]
for day in days[:5]:
    print(day["timestamp"], day["bullish"], day["bearish"])
```

### JavaScript

```bash
RAPIDAPI_KEY=your_key node examples/javascript/quickstart.mjs AAPL
```

---

## Example response

`GET /sentiment-daily?symbol=AAPL`, trimmed to three days. More responses are in
[`samples/`](samples/).

```json
{
  "success": true,
  "data": {
    "data": [
      { "bullish": 45.85, "bearish": 54.15, "timestamp": "2026-11-03" },
      { "bullish": 40.85, "bearish": 59.15, "timestamp": "2026-11-02" },
      { "bullish": 38.07, "bearish": 61.93, "timestamp": "2026-11-01" }
    ]
  }
}
```

---

## Endpoints

Base URL: `https://stocktwits5.p.rapidapi.com`

### Search and symbols

| Endpoint | Returns |
|---|---|
| `GET /search` | Stocks, ETFs, indices, futures, crypto, private companies and forex by ticker or name |
| `GET /lookup-symbols` | Name, logo, market cap and page link for up to 100 symbols |
| `GET /symbol` | A symbol's page: price, watchers, trending topics, AI summary and poll |
| `GET /symbol-by-url` | The same from a stocktwits.com symbol link |
| `GET /symbol-announcements` | Announcements pinned to a symbol's page |
| `GET /fundamentals` | Valuation, profitability, balance sheet, dividends, beta and 52-week range |
| `GET /fundamentals-batch` | Fundamentals for up to 100 symbols |
| `GET /eps-facts` | Reported EPS and revenue against estimates, and the next earnings date |
| `GET /watcher-stats` | Watcher count and its 1, 7 and 30-day growth |
| `GET /funding-rounds` | A private company's funding rounds and valuations |
| `GET /crypto-data` | A crypto asset's prices, supply, market cap and recent daily history |

### Market data

| Endpoint | Returns |
|---|---|
| `GET /quote` | A real-time quote, optionally with fundamentals or futures |
| `GET /quotes` | Real-time quotes for up to 100 symbols |
| `GET /price-chart` | OHLCV bars from `1D` to `5Y` |
| `GET /sparklines` | Intraday close sparklines for up to 100 symbols |
| `GET /market-cap-chart` | Market-cap history of a crypto asset or private company |

### Sentiment

| Endpoint | Returns |
|---|---|
| `GET /sentiment` | Sentiment and message volume now, 15-minute and 24-hour change, per-window summaries |
| `GET /sentiment-chart` | Sentiment and message volume history, 5-minute to daily points since 2018 |
| `GET /sentiment-daily` | Daily bullish and bearish percentages for about 61 days |
| `GET /market-sentiment-index` | The market-wide Stocktwits Sentiment Index with benchmark prices |

### Trending and rankings

| Endpoint | Returns |
|---|---|
| `GET /trending-symbols` | Symbols trending now, ranked, with an AI summary |
| `GET /symbol-rankings` | Most active, most bullish, most bearish, top gainers and losers, most new watchers |
| `GET /popular-messages` | The most popular messages across symbols |
| `GET /symbol-popular-messages` | One symbol's most popular messages |
| `GET /trending-topic` | One "why it's trending" topic and the messages behind it |

### Messages

| Endpoint | Returns |
|---|---|
| `GET /symbol-stream` | A symbol's message stream, filterable by bullish or bearish tag and content |
| `GET /topic-stream` | Messages about one topic word across symbols |
| `GET /global-stream` | Site-wide trending, suggested or chart streams |
| `GET /cmt-stream` | The CMT technical analysis community stream |
| `GET /message`, `/message-by-url`, `/message-thread`, `/message-conversation` | One message, its replies and its conversation |
| `GET /article-messages` | Posts that share one news article |
| `GET /search-messages` | Full-text message search back to 2008 |
| `GET /user-stream`, `/user-liked-messages` | Messages by or liked by one account |

### News and earnings

| Endpoint | Returns |
|---|---|
| `GET /news-feed` | Newsroom feeds: trending, Stocktwits originals, stocks, crypto, press releases, indices |
| `GET /symbol-news` | News and videos about one or more symbols |
| `GET /news-articles` | News from one outlet or writer |
| `GET /news-article`, `/news-article-by-url` | One article by id or link |
| `GET /earnings-calendar` | Who reports on which day, for the US and India |
| `GET /earnings-call` | Estimates against actuals, AI summary and audio links for one call |
| `GET /earnings-call-transcript` | The full transcript with speakers and timings |

### Accounts, calendar and polls

| Endpoint | Returns |
|---|---|
| `GET /user`, `/user-by-url`, `/user-followers`, `/user-following`, `/user-watchlist`, `/suggested-users` | Public account data (not used in this repo's examples) |
| `GET /market-calendar` | Market holidays and the next session for the US, India and crypto |
| `GET /prediction-hours` | The sessions next-day, next-week and next-month predictions target |
| `GET /polls`, `/poll` | Polls with choices, vote shares and winner |
| `GET /status` | Service health |

---

## Things to know about the data

These come from running the examples against the API on 3 and 4 November 2026 (US market
hours), on AAPL, TSLA and the trending list.

- **The response nests `data` twice** on `/sentiment` and `/sentiment-daily`: the rows sit in
  `data.data`.
- **Daily sentiment includes weekends.** 61 calendar days of AAPL gave 41 trading days once
  joined to prices. Join on the date, not the row position.
- **Daily rows are newest first; price bars are oldest first.**
- **The last price bar can be the live session.** During market hours the newest daily bar is
  the session in progress (AAPL showed a -2.47% "day" before the close).
  `client.daily_closes()` drops bars that have not ended.
- **A daily bar's date is its `end_time`.** Bars run from 23:59:59 on the previous day to
  23:59:59 on the trading day, in New York time with the offset in the string.
- **`label` and `labelNormalized` disagree.** AAPL read `"label": "BULLISH"` next to
  `"labelNormalized": "BEARISH"`: the first is the raw reading, the second compares it with
  the symbol's own history. Pick one and say which.
- **Sentiment and price do not line up the same way for every symbol.** Over the same two
  months the bullish share had a +0.25 correlation with AAPL's next-day return and -0.24 with
  TSLA's. Two months is a small sample; `sentiment_vs_price.py` prints both numbers so you can
  judge.
- **Each symbol has its own baseline.** TSLA's daily bullish share stayed between 56.5% and
  70.5%, while AAPL's ran from 37.4% to 76.3%. Compare a symbol with its own history, not
  with 50%.
- **Trending is about attention, not size.** The top trending equity had under 7,000 watchers;
  AMD, fifth, had 566,685.
- **Fundamentals carry a business description** that can name founders and officers. Drop it
  if you store or publish the rows; the samples here do.

---

## Examples in this repo

| File | What it does |
|---|---|
| [`examples/python/quickstart.py`](examples/python/quickstart.py) | Trending symbols with their scores and the AI summary, then the top symbol's sentiment now and over 24 hours |
| [`examples/python/sentiment_vs_price.py`](examples/python/sentiment_vs_price.py) | Join a symbol's daily bullish share with its daily closes: correlation with same-day and next-day returns, next-day returns after more and less bullish days, and the biggest sentiment swings, with optional CSV |
| [`examples/javascript/quickstart.mjs`](examples/javascript/quickstart.mjs) | A symbol's daily bullish share as a text bar chart in Node 18+, no dependencies |
| [`samples/`](samples/) | Real responses for four endpoints |

The examples read symbol-level aggregates only. None of them reads messages or accounts.

---

## API or your own Stocktwits scraper

A homemade Stocktwits scraper has to page message streams, rebuild sentiment from tags, keep
up with the site's changes and stay within its limits. This API returns the sentiment,
rankings, prices and news as documented JSON, so the work you keep is the analysis. If you
need a one-off export or a recurring feed rather than API calls,
[contact us](https://happyendpoint.com/contact?utm_source=github&utm_medium=readme&utm_campaign=stocktwits-api).

---

## Use it from Claude, Cursor or any MCP client

RapidAPI exposes every endpoint as an MCP tool, so an AI assistant can read Stocktwits
sentiment without code:

```json
{
  "mcpServers": {
    "stocktwits": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.rapidapi.com",
        "--header",
        "x-api-host: stocktwits5.p.rapidapi.com",
        "--header",
        "x-api-key: YOUR_RAPIDAPI_KEY"
      ]
    }
  }
}
```

| Client | Config path |
|---|---|
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` |
| Cursor | `~/.cursor/mcp.json` |
| Claude Code | `.mcp.json` in your project root |

---

## FAQ

### Is there a Stocktwits API?

Stocktwits does not offer open, self-serve access to this data. This API, built and
maintained by Happy Endpoint and independent of Stocktwits, returns its sentiment, trending
symbols, messages, quotes and news as REST and JSON.

### How do I get Stocktwits sentiment for a stock?

`/sentiment` gives the live score with 15-minute and 24-hour change, `/sentiment-daily` the
daily bullish and bearish split for about 61 days, and `/sentiment-chart` the history back to
2018.

### Does Stocktwits sentiment predict stock prices?

Not in any simple way. In the two months tested, the bullish share was mildly positively
related to AAPL's next-day return and mildly negatively to TSLA's.
[`sentiment_vs_price.py`](examples/python/sentiment_vs_price.py) measures it for any symbol.

### Can I get trending stocks from Stocktwits?

Yes. `/trending-symbols` returns the ranked list with a trending score and an AI summary, and
`/symbol-rankings` gives most active, most bullish, most bearish and top movers.

### Does it cover crypto and Indian stocks?

Yes. Crypto symbols end in `.X` (`BTC.X`), and trending, rankings, the sentiment index and the
earnings calendar take an India region or market.

### How do I use the Stocktwits API in Python?

Install `requests`, set `RAPIDAPI_KEY`, and call the endpoints with the two RapidAPI headers.
[`examples/python/client.py`](examples/python/client.py) is a short client with helpers for
daily closes and correlation.

### Is there a free Stocktwits API?

Plans, including what each one allows, are on the
[RapidAPI listing](https://rapidapi.com/happyendpoint/api/stocktwits5), where every endpoint can
also be tested in the browser.

---

## Related repos

- [morningstar-api](https://github.com/happyendpointhq/morningstar-api) - Morningstar quotes, fundamentals and research data
- [awesome-alternative-data](https://github.com/happyendpointhq/awesome-alternative-data) - alternative data sources for investment research
- [happyendpoint-python](https://github.com/happyendpointhq/happyendpoint-python) - Python SDK for Happy Endpoint APIs

---

## Disclaimer

Happy Endpoint is an independent provider. This project is **not affiliated
with, endorsed by, sponsored by, or connected to** any of the websites,
platforms, retailers, or marketplaces referenced here or reachable through the
underlying APIs.

All product names, brands, trademarks, and registered trademarks are the
property of their respective owners. Any reference to them is descriptive only,
to identify the subject matter of the data, and does not imply any association
or endorsement.

Users are responsible for ensuring their use of any data complies with
applicable laws and the terms of service of the relevant source.

Nothing in this repository is investment advice.

---

## About Happy Endpoint

[Happy Endpoint](https://happyendpoint.com) builds and maintains real-time data
APIs for property portals, retailers, and marketplaces. All APIs are available on
RapidAPI with a free tier.

- Catalogue: [happyendpoint.com/library](https://happyendpoint.com/library)
- Datasets: [happyendpoint.com/datasets](https://happyendpoint.com/datasets)
- Documentation: [docs.happyendpoint.com](https://docs.happyendpoint.com)
- Contact: hello@happyendpoint.com

## Licence

MIT. See [LICENSE](LICENSE).
