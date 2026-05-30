# Python Recipe: Minimal Paper Trading Loop

Use this recipe when you want a small local loop that finds or creates a paper account, checks a stock snapshot, submits one simulated stock order, and prints positions.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_PAPER_API_KEY=cm_...` or `CUTEMARKETS_API_KEY=cm_...`
- `CUTEMARKETS_STOCKS_API_KEY=cm_...` if your stocks and paper keys are separate

## Run

```bash
python paper_trading_agent_loop.py
```

Optional:

```bash
CUTEMARKETS_PAPER_SYMBOL=MSFT python paper_trading_agent_loop.py
```

This recipe is deliberately minimal. It is not a production bot and does not include scheduling, reconciliation, or portfolio-level risk controls.

## Related Docs

- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
- [CuteMarkets docs](https://cutemarkets.com/docs)
