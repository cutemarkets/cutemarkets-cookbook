from __future__ import annotations

import os
import time
from typing import Any, Optional

from cutemarkets import CuteMarkets


def _get(value: Any, key: str) -> Any:
    if isinstance(value, dict):
        return value.get(key)
    return getattr(value, key, None)


def _find_account(client: CuteMarkets, name: str) -> Optional[Any]:
    page = client.paper.accounts.list(limit=100)
    for account in _get(page, "results") or []:
        if _get(account, "name") == name:
            return account
    return None


def main() -> None:
    client = CuteMarkets(paper_api_key=os.environ.get("CUTEMARKETS_PAPER_API_KEY"))
    account_name = os.environ.get("CUTEMARKETS_PAPER_ACCOUNT_NAME", "cookbook-paper-loop")
    symbol = os.environ.get("CUTEMARKETS_PAPER_SYMBOL", "AAPL").upper()

    try:
        account = _find_account(client, account_name)
        if account is None:
            created = client.paper.accounts.create(name=account_name, initial_cash=100000)
            account = _get(created, "account")
        account_id = _get(account, "id")
        if not account_id:
            raise RuntimeError("Paper account did not include an id.")

        snapshot = client.stocks.snapshot(symbol)
        last_trade = _get(_get(snapshot, "last_trade") or _get(snapshot, "lastTrade"), "price")
        print({"account": account_id, "symbol": symbol, "last_trade": last_trade})

        order = client.paper.orders.submit(
            account_id,
            symbol=symbol,
            qty=1,
            side="buy",
            type="market",
            time_in_force="day",
            client_order_id=f"cookbook-{symbol.lower()}-{int(time.time())}",
        )
        positions = client.paper.positions(account_id)
        print({"order_id": _get(order, "id"), "positions": len(_get(positions, "results") or [])})
    finally:
        client.close()


if __name__ == "__main__":
    main()
