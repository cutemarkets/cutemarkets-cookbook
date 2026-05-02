# Python Recipe: Earnings Implied Move

Use this recipe when you want to estimate an implied move from the ATM straddle around an earnings date.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python earnings_implied_move.py
```

## Expected Output

```text
{'underlying': 'MSFT', 'expiry': '2026-05-01', 'spot': 412.3, 'impliedMovePct': 0.074}
```

## Related Docs

- [Options chain](https://cutemarkets.com/docs/option-chain)
- [Expirations](https://cutemarkets.com/docs/expirations)
