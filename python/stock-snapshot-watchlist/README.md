# Python Recipe: Stock Snapshot Watchlist

Use this recipe when you want a small watchlist script that pulls current stock snapshots and a short daily-bar window.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_STOCKS_API_KEY=cm_...` or `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python stock_snapshot_watchlist.py
```

Optional:

```bash
CUTEMARKETS_STOCKS=AAPL,MSFT,NVDA python stock_snapshot_watchlist.py
```

## Related Docs

- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
- [CuteMarkets docs](https://cutemarkets.com/docs)
