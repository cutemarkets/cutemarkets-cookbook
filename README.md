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

## TypeScript Recipes

- [options-chain-scanner](typescript/options-chain-scanner/README.md)
- [earnings-implied-move](typescript/earnings-implied-move/README.md)

TypeScript recipes in this repo are intentionally self-contained so they can run before the TypeScript SDK is published. Once `cutemarkets-typescript` is live on npm, use the SDK for typed production integrations and keep the cookbook for small task-focused recipes.

## How To Use This Repo

1. Pick the workflow you need.
2. Read the recipe README for prerequisites and expected output.
3. Copy the script into your own project or keep it as a starting point.
4. Follow the linked docs page when you need endpoint-level detail.

The cookbook is meant to deliver value first. If you need fuller typing, pagination helpers, or more endpoints, move from the recipe to the SDK repo rather than rebuilding the API surface yourself.
