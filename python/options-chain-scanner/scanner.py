from __future__ import annotations

import os
from typing import Optional

from cutemarkets import CuteMarkets


def spread_pct(contract) -> Optional[float]:
    quote = contract.last_quote
    if quote is None or quote.bid is None or quote.ask is None:
        return None
    mid = (quote.bid + quote.ask) / 2.0
    if mid <= 0:
        return None
    return (quote.ask - quote.bid) / mid


def main() -> None:
    client = CuteMarkets(api_key=os.environ.get("CUTEMARKETS_API_KEY"))
    ticker = os.environ.get("CUTEMARKETS_UNDERLYING", "SPY")
    chain = client.options.chain(ticker, contract_type="call", limit=100)
    ranked = [
        contract
        for contract in chain.results
        if spread_pct(contract) is not None
        and spread_pct(contract) <= 0.2
        and (contract.open_interest or 0) >= 100
    ]
    ranked.sort(key=lambda contract: float(contract.open_interest or 0.0), reverse=True)
    print(f"[chain] ticker={ticker} contracts={len(chain.results)} ranked={len(ranked[:10])}")
    for contract in ranked[:10]:
        print(
            contract.details.ticker,
            contract.details.expiration_date,
            contract.details.strike_price,
            f"oi={contract.open_interest}",
            f"iv={contract.implied_volatility}",
        )
    client.close()


if __name__ == "__main__":
    main()
