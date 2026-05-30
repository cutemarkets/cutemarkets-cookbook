import { CuteMarketsClient } from "cutemarkets-typescript";

const client = new CuteMarketsClient({
  stocksApiKey: process.env.CUTEMARKETS_STOCKS_API_KEY,
});

const tickers = (process.env.CUTEMARKETS_STOCKS ?? "AAPL,MSFT,NVDA")
  .split(",")
  .map((ticker) => ticker.trim().toUpperCase())
  .filter(Boolean);

function numberField(container: unknown, key: string): number | undefined {
  if (typeof container !== "object" || container === null) {
    return undefined;
  }
  const value = (container as Record<string, unknown>)[key];
  return typeof value === "number" ? value : undefined;
}

const snapshots = await client.stocks.snapshots.all({ tickers: tickers.join(",") });
const rows = snapshots.tickers ?? (Array.isArray(snapshots.results) ? snapshots.results : []);

console.log("ticker,last_trade,previous_close,change_pct");
for (const snapshot of rows) {
  const lastTrade = numberField(snapshot.last_trade ?? snapshot.lastTrade, "price");
  const previousClose = numberField(snapshot.prev_day ?? snapshot.prevDay, "close");
  const changePct =
    lastTrade !== undefined && previousClose !== undefined && previousClose !== 0
      ? ((lastTrade - previousClose) / previousClose) * 100
      : null;
  console.log(`${snapshot.ticker},${lastTrade},${previousClose},${changePct}`);
}

const bars = await client.stocks.aggs.range(tickers[0] ?? "AAPL", 1, "day", "2026-01-01", "2026-01-31");
console.log(`daily_bars_loaded=${bars.results?.length ?? 0}`);
