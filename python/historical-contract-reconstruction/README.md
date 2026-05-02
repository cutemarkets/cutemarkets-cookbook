# Python Recipe: Historical Contract Reconstruction

Use this recipe when you need to rebuild the contract universe as it existed on a historical date.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python historical_contracts_as_of.py
```

## Expected Output

```text
[contracts.list] MSFT as_of=2026-01-15 count=5
O:MSFT260220C00400000 call 2026-02-20 400.0
```

## Related Docs

- [Contracts](https://cutemarkets.com/docs/contracts)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
