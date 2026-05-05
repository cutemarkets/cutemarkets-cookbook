from __future__ import annotations

import os
from statistics import median

from cutemarkets import CuteMarkets
from cutemarkets.errors import ForbiddenError


def main() -> None:
    client = CuteMarkets(api_key=os.environ.get("CUTEMARKETS_API_KEY"))
    option_ticker = os.environ.get("CUTEMARKETS_OPTION_TICKER", "O:SPY260417C00580000")
    try:
        page = client.options.quotes.list(option_ticker, limit=100)
    except ForbiddenError as exc:
        raise SystemExit(f"Quotes unavailable on this plan: {exc.message}") from exc

    mids = []
    spreads = []
    for quote in page.results:
        if quote.bid_price is None or quote.ask_price is None:
            continue
        mid = (quote.bid_price + quote.ask_price) / 2.0
        if mid <= 0:
            continue
        mids.append(mid)
        spreads.append((quote.ask_price - quote.bid_price) / mid)

    payload = {
        "optionTicker": option_ticker,
        "observations": len(page.results),
        "usableObservations": len(spreads),
        "medianMid": median(mids) if mids else 0.0,
        "medianSpreadPct": median(spreads) if spreads else 0.0,
        "usableUnder10Pct": sum(1 for spread in spreads if spread <= 0.10),
    }
    print(payload)
    client.close()


if __name__ == "__main__":
    main()
