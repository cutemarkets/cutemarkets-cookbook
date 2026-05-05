import { CuteMarketsClient } from "cutemarkets-typescript";

const underlying = process.env.CUTEMARKETS_UNDERLYING ?? "MSFT";
const eventDate = process.env.CUTEMARKETS_EVENT_DATE ?? "2026-04-29";

type ExpirationsPayload = {
  results?: string[];
};

type ChainRow = {
  details?: {
    ticker?: string;
    expiration_date?: string;
    strike_price?: number;
    contract_type?: string;
  };
  last_quote?: {
    bid?: number;
    ask?: number;
  };
  underlying_asset?: {
    price?: number;
  };
};

function midpoint(contract: ChainRow): number | null {
  const bid = contract.last_quote?.bid;
  const ask = contract.last_quote?.ask;
  if (bid === undefined || ask === undefined) {
    return null;
  }
  const mid = (bid + ask) / 2;
  return mid > 0 ? mid : null;
}

const client = new CuteMarketsClient({
  apiKey: process.env.CUTEMARKETS_API_KEY,
});
const expirations = (await client.tickers.expirations(underlying)) as ExpirationsPayload;
const expiry = (expirations.results ?? []).find((value) => value >= eventDate);
if (!expiry) {
  throw new Error(`No expiry found on or after ${eventDate}`);
}

const chain = await client.options.chain(underlying, {
  expiration_date: expiry,
  limit: 250,
});
const rows = (chain.results ?? []) as ChainRow[];
const spot = rows[0]?.underlying_asset?.price;
if (!spot) {
  throw new Error("Missing underlying spot price.");
}

const ranked = [...rows]
  .filter((contract) => contract.details?.strike_price !== undefined)
  .sort(
    (left, right) =>
      Math.abs((left.details?.strike_price ?? 0) - spot) -
      Math.abs((right.details?.strike_price ?? 0) - spot),
  );

const call = ranked.find((contract) => contract.details?.contract_type === "call");
const put = ranked.find(
  (contract) =>
    contract.details?.contract_type === "put" &&
    contract.details?.strike_price === call?.details?.strike_price,
);
if (!call || !put) {
  throw new Error("Could not identify ATM call/put pair.");
}

const callMid = midpoint(call);
const putMid = midpoint(put);
if (callMid === null || putMid === null) {
  throw new Error("ATM pair did not contain a complete bid/ask.");
}

const straddleMid = callMid + putMid;
console.log({ underlying, eventDate, expiry, spot, impliedMovePct: straddleMid / spot });
