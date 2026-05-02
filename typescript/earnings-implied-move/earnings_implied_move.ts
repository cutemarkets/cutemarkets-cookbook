const apiKey = process.env.CUTEMARKETS_API_KEY;
if (!apiKey) {
  throw new Error("Set CUTEMARKETS_API_KEY=cm_... before running this recipe.");
}

const baseUrl = process.env.CUTEMARKETS_BASE_URL ?? "https://api.cutemarkets.com";
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

async function requestJson<T>(path: string, params: Record<string, string> = {}): Promise<T> {
  const url = new URL(`${baseUrl.replace(/\/+$/, "")}${path}`);
  for (const [key, value] of Object.entries(params)) {
    url.searchParams.set(key, value);
  }
  const response = await fetch(url, {
    headers: {
      Accept: "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
  });
  if (!response.ok) {
    throw new Error(`CuteMarkets request failed with ${response.status} for ${url.pathname}`);
  }
  return (await response.json()) as T;
}

const expirations = await requestJson<ExpirationsPayload>(`/v1/tickers/expirations/${encodeURIComponent(underlying)}/`);
const expiry = (expirations.results ?? []).find((value) => value >= eventDate);
if (!expiry) {
  throw new Error(`No expiry found on or after ${eventDate}`);
}

const chain = await requestJson<{ results?: ChainRow[] }>(`/v1/options/chain/${encodeURIComponent(underlying)}/`, {
  expiration_date: expiry,
  limit: "250",
});
const rows = chain.results ?? [];
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
