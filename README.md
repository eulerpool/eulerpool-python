# Eulerpool SDK for Python

Official Python SDK for the [Eulerpool Financial Data API](https://eulerpool.com/developers).

## Installation

```bash
pip install eulerpool
```

## Quick Start

```python
import eulerpool

client = eulerpool.Eulerpool("YOUR_API_KEY")

# Get a company profile
profile = client.equity.profile("US0378331005")
print(profile)

# Get income statement
income = client.equity.income_statement("US0378331005")

# Get ETF holdings
holdings = client.etf.holdings("IE00B4L5Y983")

# Get forex rates
rates = client.forex.rates("EUR")

# Get macro calendar
calendar = client.macro.calendar()

client.close()
```

## Context Manager

```python
with eulerpool.Eulerpool("YOUR_API_KEY") as client:
    profile = client.equity.profile("US0378331005")
```

## Async Support

```python
import asyncio
import eulerpool

async def main():
    async with eulerpool.AsyncEulerpool("YOUR_API_KEY") as client:
        profile = await client.equity.profile("US0378331005")
        income = await client.equity.income_statement("US0378331005")
        print(profile)

asyncio.run(main())
```

## Authentication

Pass your API key when creating the client. By default, it is sent as a `?token=` query parameter. To use the `Authorization: Bearer` header instead:

```python
client = eulerpool.Eulerpool("YOUR_API_KEY", use_auth_header=True)
```

Get your free API key at [eulerpool.com/developers/register](https://eulerpool.com/developers/register).

## Configuration

```python
client = eulerpool.Eulerpool(
    "YOUR_API_KEY",
    base_url="https://api.eulerpool.com/api/1",  # default
    use_auth_header=False,                         # default: use ?token= query param
    max_retries=2,                                 # default
    timeout=30.0,                                  # default: 30s
)
```

## Available Resources

| Resource | Accessor | Endpoints |
|----------|----------|-----------|
| Equity | `client.equity` | profile, quotes, balance_sheet, income_statement, cash_flow_statement, ownership, executives, peers, supply_chain, segments, estimates, splits, dividends, dividends_by_fy, insider_trades, esg_rating, short_volume, short_interest_positions, regions, country_insider_trades, swot, discover, metrics, upgrades, overview, income_statement_quarterly, cash_flow_statement_quarterly, fundamentals_quarterly, aaqs, shares_outstanding, market_cap, candles, insider_trades_derivatives, insider_trades_eu, valuation_history, returns, growth, margins, dividend_quality, kpi, coverage, list, search |
| Equity Extended | `client.equity_extended` | aaqs, options_chain, technical_signals, basic_financials, ebitda_estimates, sec_filings, earnings_calendar, tech_indicators, price_target_history, peers, short_interest, short_volume, index_history, market_news, symbol_changes, isin_changes, financials_reported, aggregate_signals |
| ETF | `client.etf` | profile, holdings, sectors, countries, quotes, description, list |
| Macro | `client.macro` | countries, country, indicator, fred_series, fred_observations, ecb_series, ecb_observations, imf_series, imf_observations, worldbank_series, worldbank_observations, eurostat_series, eurostat_observations, search, latest_fred, latest_ecb, calendar_properties, calendar, country_risk |
| Forex | `client.forex` | list, rates |
| Bonds | `client.bonds` | profile, prices, yield_curve, list, ticks |
| Crypto | `client.crypto` | list, profile, quotes |
| Crypto Extended | `client.crypto_extended` | top_coins, market_overview, analysis, derivatives, onchain, defi, defi_protocols, defi_yields, dex_volumes, stablecoins, fear_greed_history, candles, chain_tvl, defi_fees, stablecoin_supply, bridge_volumes, funding_rates, open_interest, intraday, symbol_map |
| Market | `client.market` | quotes_latest, quotes_intraday, options, analytics_52week, indicators, fx, quotes_exchanges, analytics_fx_returns, top_movers, market_status, quotes_bulk, analytics_risk, analytics_correlation, holidays |
| Alternative | `client.alternative` | superinvestors_list, superinvestors_holdings, superinvestors_top_holdings, superinvestors_recent_activity, congress_trading, investment_themes, fear_and_greed, cot, google_trends, wikipedia_pageviews |
| Sentiment | `client.sentiment` | insider_sentiment, news_sentiment, social_sentiment, price_metrics, fund_ownership, institutional_ownership, sector_metrics |
| Research | `client.research` | recommendations, news, press_releases |
| Calendar | `client.calendar` | ipo, dividends, earnings, earnings_by_symbol, earnings_surprises |
| Screener | `client.screener` | screen, universe, search, metadata |
| Mutual Fund | `client.mutual_fund` | profile, holdings, sectors, countries |
| Commodity | `client.commodity` | profile, quotes, list |
| Institutional | `client.institutional` | profile, portfolio |
| Certificates | `client.certificates` | profile, list, quotes |
| Earning Calls | `client.earning_calls` | list, transcript |
| Index | `client.index` | constituents |
| Fair Value | `client.fair_value` | by_isin |
| AAQ | `client.aaq` | by_isin |
| News | `client.news` | feed, list, by_name, by_isin |
| Trends | `client.trends` | ticker_trends |
| ICE-SWAP | `client.ice_swap` | data |

## Error Handling

```python
from eulerpool import Eulerpool, AuthenticationError, RateLimitError

client = Eulerpool("YOUR_API_KEY")

try:
    data = client.equity.profile("US0378331005")
except AuthenticationError:
    print("Invalid API key")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
```

## Requirements

- Python >= 3.8
- httpx >= 0.24.0

## License

MIT
