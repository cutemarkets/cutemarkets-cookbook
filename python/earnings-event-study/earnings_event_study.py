from __future__ import annotations

import os
from typing import Optional

from cutemarkets import CuteMarkets


def midpoint(bid: Optional[float], ask: Optional[float]) -> Optional[float]:
    if bid is None or ask is None:
        return None
    mid = (bid + ask) / 2.0
    return mid if mid > 0 else None


def main() -> None:
    client = CuteMarkets(api_key=os.environ.get("CUTEMARKETS_API_KEY"))
    underlying = os.environ.get("CUTEMARKETS_UNDERLYING", "MSFT")
    event_date = os.environ.get("CUTEMARKETS_EVENT_DATE", "2026-04-29")
    expirations = client.tickers.expirations(underlying).results
    expiry = next(value for value in expirations if value >= event_date)
    chain = client.options.chain(underlying, expiration_date=expiry, limit=250)
    spot = float(chain.results[0].underlying_asset.price)
    ranked = sorted(
        [contract for contract in chain.results if contract.details and contract.details.strike_price is not None],
        key=lambda contract: abs(float(contract.details.strike_price) - spot),
    )
    call = next(contract for contract in ranked if contract.details.contract_type == "call")
    put = next(
        contract
        for contract in ranked
        if contract.details.contract_type == "put"
        and contract.details.strike_price == call.details.strike_price
    )
    call_mid = midpoint(call.last_quote.bid if call.last_quote else None, call.last_quote.ask if call.last_quote else None)
    put_mid = midpoint(put.last_quote.bid if put.last_quote else None, put.last_quote.ask if put.last_quote else None)
    if call_mid is None or put_mid is None:
        raise SystemExit("ATM pair did not contain a complete bid/ask.")
    straddle_mid = call_mid + put_mid
    print(
        {
            "underlying": underlying,
            "eventDate": event_date,
            "expiry": expiry,
            "spot": spot,
            "callTicker": call.details.ticker,
            "putTicker": put.details.ticker,
            "impliedMoveAbs": straddle_mid,
            "impliedMovePct": straddle_mid / spot,
        }
    )
    client.close()


if __name__ == "__main__":
    main()
