# Python Recipe: Quote Coverage Audit

Use this recipe when you want a quick contract-level check on quote coverage and spread quality before trusting an options backtest.

## Prerequisites

- Python 3.9+
- `pip install cutemarkets`
- Expert-plan access for historical options quotes
- `CUTEMARKETS_API_KEY=cm_...`

## Run

```bash
python quote_coverage_audit.py
```

## Related Docs

- [Quotes](https://cutemarkets.com/docs/quotes)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
