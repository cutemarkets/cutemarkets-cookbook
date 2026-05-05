# Recipes for Using CuteMarkets Options Data in Python and TypeScript

`cutemarkets-cookbook` is a jobs-to-be-done repository. It does not duplicate the SDKs. Instead, it organizes runnable recipes around the workflows developers actually want to solve with options data.

Quick links:

- [Get API key](https://cutemarkets.com/signup)
- [Read docs](https://cutemarkets.com/docs)
- [Python SDK](https://github.com/cutemarkets/cutemarkets-python)
- [TypeScript SDK](https://github.com/cutemarkets/cutemarkets-typescript)

## Python Recipes

- [options-chain-scanner](python/options-chain-scanner/README.md)
- [historical-contract-reconstruction](python/historical-contract-reconstruction/README.md)
- [earnings-implied-move](python/earnings-implied-move/README.md)
- [quote-quality-filter](python/quote-quality-filter/README.md)
- [quote-coverage-audit](python/quote-coverage-audit/README.md)
- [earnings-event-study](python/earnings-event-study/README.md)

## TypeScript Recipes

- [options-chain-scanner](typescript/options-chain-scanner/README.md)
- [earnings-implied-move](typescript/earnings-implied-move/README.md)

TypeScript recipes now use the published `cutemarkets-typescript` SDK directly. The cookbook stays focused on small workflow-level tasks, while the SDK remains the right place for typed production integrations.

## How To Use This Repo

1. Pick the workflow you need.
2. Read the recipe README for prerequisites and expected output.
3. Copy the script into your own project or keep it as a starting point.
4. Follow the linked docs page when you need endpoint-level detail.

The cookbook is meant to deliver value first. If you need fuller typing, pagination helpers, or more endpoints, move from the recipe to the SDK repo rather than rebuilding the API surface yourself.

## Validation

- `npm test` checks the TypeScript recipes with `tsc` and the Python recipes with a syntax/import harness.
- [recipes.manifest.json](recipes.manifest.json) is the machine-readable recipe index for future automation.
