from __future__ import annotations

import os
from typing import Optional

from cutemarkets import CuteMarkets


def midpoint(contract) -> Optional[float]:
    quote = contract.last_quote
    if quote is None or quote.bid is None or quote.ask is None:
        return None
    return (quote.bid + quote.ask) / 2.0


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
    implied_move = midpoint(call) + midpoint(put)
    print(
        {
            "underlying": underlying,
            "expiry": expiry,
            "spot": spot,
            "impliedMovePct": implied_move / spot,
        }
    )
    client.close()


if __name__ == "__main__":
    main()
