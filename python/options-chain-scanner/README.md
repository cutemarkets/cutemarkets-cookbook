# Python Recipe: Options Chain Scanner

Use this recipe when you want a simple chain scanner that filters on spread and open interest instead of printing the raw chain.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python scanner.py
```

## Expected Output

```text
[chain] ticker=SPY contracts=100 ranked=10
O:SPY260417C00580000 2026-04-17 580.0 oi=21432 iv=0.221
```

## Related Docs

- [Options chain](https://cutemarkets.com/docs/option-chain)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
