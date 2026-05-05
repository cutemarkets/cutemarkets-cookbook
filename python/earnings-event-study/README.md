# Python Recipe: Earnings Event Study

Use this recipe when you want a simple event-study row for one earnings date: first post-event expiry, ATM call/put pair, and implied move from the listed straddle.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python earnings_event_study.py
```

## Related Docs

- [Expirations](https://cutemarkets.com/docs/expirations)
- [Options chain](https://cutemarkets.com/docs/option-chain)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
