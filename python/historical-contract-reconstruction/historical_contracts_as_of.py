from __future__ import annotations

import os

from cutemarkets import CuteMarkets


def main() -> None:
    client = CuteMarkets(api_key=os.environ.get("CUTEMARKETS_API_KEY"))
    as_of = os.environ.get("CUTEMARKETS_AS_OF", "2026-01-15")
    page = client.options.contracts.list(
        underlying_ticker=os.environ.get("CUTEMARKETS_UNDERLYING", "MSFT"),
        as_of=as_of,
        expiration_date_gte="2026-01-22",
        expiration_date_lte="2026-03-01",
        limit=5,
    )
    print(f"[contracts.list] MSFT as_of={as_of} count={len(page.results)}")
    for contract in page.results:
        print(contract.ticker, contract.contract_type, contract.expiration_date, contract.strike_price)
    client.close()


if __name__ == "__main__":
    main()
