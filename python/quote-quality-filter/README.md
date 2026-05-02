# Python Recipe: Quote Quality Filter

Use this recipe when you need a fast sanity check on quote spread quality before trusting a backtest or scanner.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- Expert-plan access for historical options quotes
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python quote_quality_filter.py
```

## Expected Output

```text
{'medianMid': 1.14, 'medianSpreadPct': 0.043, 'usableUnder10Pct': 42}
```

## Related Docs

- [Quotes](https://cutemarkets.com/docs/quotes)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
