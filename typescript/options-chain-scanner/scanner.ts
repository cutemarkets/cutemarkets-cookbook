const apiKey = process.env.CUTEMARKETS_API_KEY;
if (!apiKey) {
  throw new Error("Set CUTEMARKETS_API_KEY=cm_... before running this recipe.");
}

const baseUrl = process.env.CUTEMARKETS_BASE_URL ?? "https://api.cutemarkets.com";
const ticker = process.env.CUTEMARKETS_UNDERLYING ?? "SPY";

type ChainRow = {
  open_interest?: number;
  implied_volatility?: number;
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
};

function spreadPct(contract: ChainRow): number | null {
  const bid = contract.last_quote?.bid;
  const ask = contract.last_quote?.ask;
  if (bid === undefined || ask === undefined) {
    return null;
  }
  const mid = (bid + ask) / 2;
  if (mid <= 0) {
    return null;
  }
  return (ask - bid) / mid;
}

const url = new URL(`${baseUrl.replace(/\/+$/, "")}/v1/options/chain/${encodeURIComponent(ticker)}/`);
url.searchParams.set("contract_type", "call");
url.searchParams.set("limit", "100");

const response = await fetch(url, {
  headers: {
    Accept: "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
});
if (!response.ok) {
  throw new Error(`CuteMarkets chain request failed with ${response.status}`);
}

const payload = (await response.json()) as { results?: ChainRow[] };
const ranked = (payload.results ?? [])
  .filter((contract) => {
    const spread = spreadPct(contract);
    return spread !== null && spread <= 0.2 && (contract.open_interest ?? 0) >= 100;
  })
  .sort((left, right) => (right.open_interest ?? 0) - (left.open_interest ?? 0))
  .slice(0, 10);

for (const contract of ranked) {
  console.log(
    contract.details?.ticker,
    contract.details?.expiration_date,
    contract.details?.strike_price,
    `oi=${contract.open_interest}`,
    `iv=${contract.implied_volatility}`,
  );
}
