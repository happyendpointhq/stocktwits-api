// Stocktwits API quickstart. Node 18+ (built-in fetch), no dependencies.
//   RAPIDAPI_KEY=... node quickstart.mjs AAPL

const HOST = 'stocktwits5.p.rapidapi.com';

async function get(path, params = {}) {
  const url = new URL(`https://${HOST}${path}`);
  for (const [key, value] of Object.entries(params)) {
    if (value != null) url.searchParams.set(key, value);
  }
  const res = await fetch(url, {
    headers: { 'x-rapidapi-host': HOST, 'x-rapidapi-key': process.env.RAPIDAPI_KEY },
  });
  if (!res.ok) throw new Error(`Stocktwits API ${res.status}: ${await res.text()}`);
  return (await res.json()).data;
}

const symbol = (process.argv[2] ?? 'AAPL').toUpperCase();

// Daily bullish and bearish shares, newest first (the rows sit in data.data).
const { data: days } = await get('/sentiment-daily', { symbol });
console.log(`${symbol}: bullish share over the last ${days.length} days`);
for (const day of days.slice(0, 10)) {
  console.log(`${day.timestamp}  ${day.bullish.toFixed(1).padStart(5)}% bullish  ${'#'.repeat(Math.round(day.bullish / 4))}`);
}
