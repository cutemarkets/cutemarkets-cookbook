# TypeScript Recipe: Minimal Paper Trading Loop

Use this recipe when you want a small Node loop that finds or creates a paper account, checks a stock snapshot, submits one simulated stock order, and prints positions.

## Prerequisites

- Node 18+
- `CUTEMARKETS_PAPER_API_KEY=cm_...` or `CUTEMARKETS_API_KEY=cm_...`
- `CUTEMARKETS_STOCKS_API_KEY=cm_...` if your stocks and paper keys are separate
- `npm install` from the cookbook root

## Run

```bash
npm run ts:paper-trading-agent-loop
```

This recipe is deliberately minimal. It is not a production bot and does not include scheduling, reconciliation, or portfolio-level risk controls.

## Related Docs

- [TypeScript SDK](https://github.com/cutemarkets/cutemarkets-typescript)
- [CuteMarkets docs](https://cutemarkets.com/docs)
