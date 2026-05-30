import { CuteMarketsClient } from "cutemarkets-typescript";

const client = new CuteMarketsClient({
  stocksApiKey: process.env.CUTEMARKETS_STOCKS_API_KEY,
  paperApiKey: process.env.CUTEMARKETS_PAPER_API_KEY,
});

const accountName = process.env.CUTEMARKETS_PAPER_ACCOUNT_NAME ?? "cookbook-paper-loop";
const symbol = (process.env.CUTEMARKETS_PAPER_SYMBOL ?? "AAPL").toUpperCase();

const accounts = await client.paper.accounts.list({ limit: 100 });
let account = accounts.results.find((item) => item.name === accountName);

if (!account?.id) {
  const created = await client.paper.accounts.create({
    name: accountName,
    initial_cash: 100000,
  });
  account = created.account;
}

if (!account?.id) {
  throw new Error("Paper account did not include an id.");
}

const snapshot = await client.stocks.snapshot(symbol);
const lastTrade = snapshot.last_trade ?? snapshot.lastTrade;
console.log({ account: account.id, symbol, lastTrade });

const order = await client.paper.orders.submit(account.id, {
  symbol,
  qty: 1,
  side: "buy",
  type: "market",
  time_in_force: "day",
  client_order_id: `cookbook-${symbol.toLowerCase()}-${Date.now()}`,
});

const positions = await client.paper.positions(account.id);
console.log({ orderId: order.id, positions: positions.results.length });
