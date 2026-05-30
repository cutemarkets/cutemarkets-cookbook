from __future__ import annotations

import os
from typing import Any, Iterable, Optional

from cutemarkets import CuteMarkets


def _get(value: Any, key: str) -> Any:
    if isinstance(value, dict):
        return value.get(key)
    return getattr(value, key, None)


def _number(container: Any, key: str) -> Optional[float]:
    value = _get(container, key)
    if value is None:
        return None
    return float(value)


def _rows(value: Any) -> Iterable[Any]:
    return _get(value, "tickers") or _get(value, "results") or []


def main() -> None:
    client = CuteMarkets(stocks_api_key=os.environ.get("CUTEMARKETS_STOCKS_API_KEY"))
    tickers = [
        item.strip().upper()
        for item in os.environ.get("CUTEMARKETS_STOCKS", "AAPL,MSFT,NVDA").split(",")
        if item.strip()
    ]

    try:
        snapshots = client.stocks.snapshots.all(tickers=",".join(tickers))
        print("ticker,last_trade,previous_close,change_pct")
        for snapshot in _rows(snapshots):
            last_trade = _number(_get(snapshot, "last_trade") or _get(snapshot, "lastTrade"), "price")
            previous_close = _number(_get(snapshot, "prev_day") or _get(snapshot, "prevDay"), "close")
            change_pct = (
                ((last_trade - previous_close) / previous_close) * 100.0
                if last_trade is not None and previous_close not in (None, 0.0)
                else None
            )
            print(f"{_get(snapshot, 'ticker')},{last_trade},{previous_close},{change_pct}")

        bars = client.stocks.aggs.range(tickers[0], 1, "day", "2026-01-01", "2026-01-31")
        print(f"daily_bars_loaded={len(_get(bars, 'results') or [])}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
