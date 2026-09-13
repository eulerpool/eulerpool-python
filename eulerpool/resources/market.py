from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Market(SyncResource):
    def analytics_52week(self, ticker: str, **params: Any) -> Any:
        """52-Week Analytics"""
        return self._get(f"/market/analytics/52week/{quote(str(ticker))}", params)
    def analytics_correlation(self, **params: Any) -> Any:
        """Stock Correlation"""
        return self._get("/market/analytics/correlation", params)
    def analytics_fx_returns(self, identifier: str, **params: Any) -> Any:
        """Currency-Adjusted Returns"""
        return self._get(f"/market/analytics/fx-returns/{quote(str(identifier))}", params)
    def analytics_risk(self, identifier: str, **params: Any) -> Any:
        """Risk & Return Analytics"""
        return self._get(f"/market/analytics/risk/{quote(str(identifier))}", params)
    def breadth(self, **params: Any) -> Any:
        """Market Breadth"""
        return self._get("/market/breadth", params)
    def cboe_indices(self, **params: Any) -> Any:
        """CBOE Indices"""
        return self._get("/market/cboe/indices", params)
    def dark_pool(self, ticker: str, **params: Any) -> Any:
        """Dark Pool Volume"""
        return self._get(f"/market/dark-pool/{quote(str(ticker))}", params)
    def etf_flows(self, ticker: str, **params: Any) -> Any:
        """ETF Fund Flows"""
        return self._get(f"/market/etf-flows/{quote(str(ticker))}", params)
    def exchanges(self, **params: Any) -> Any:
        """Exchanges"""
        return self._get("/market/exchanges", params)
    def fx(self, from_: str, to: str, **params: Any) -> Any:
        """FX Rate Series"""
        return self._get(f"/market/fx/{quote(str(from_))}/{quote(str(to))}", params)
    def holidays(self, exchange: Optional[str] = None, **params: Any) -> Any:
        """Holidays by Exchange"""
        if exchange is not None:
            return self._get(f"/market/holidays/{quote(str(exchange))}", params)
        return self._get("/market/holidays", params)
    def indicators(self, **params: Any) -> Any:
        """Market Indicators"""
        return self._get("/market/indicators", params)
    def l2(self, ticker: str, **params: Any) -> Any:
        """Level 2 Order Book"""
        return self._get(f"/market/l2/{quote(str(ticker))}", params)
    def last_quote(self, ticker: str, **params: Any) -> Any:
        """Last Quote"""
        return self._get(f"/market/last-quote/{quote(str(ticker))}", params)
    def last_trade(self, ticker: str, **params: Any) -> Any:
        """Last Trade"""
        return self._get(f"/market/last-trade/{quote(str(ticker))}", params)
    def market_status(self, **params: Any) -> Any:
        """Market Status"""
        return self._get("/market/market-status", params)
    def most_shorted(self, **params: Any) -> Any:
        """Most Shorted Stocks"""
        return self._get("/market/most-shorted", params)
    def options(self, ticker: str, **params: Any) -> Any:
        """Options Chain"""
        return self._get(f"/market/options/{quote(str(ticker))}", params)
    def options_flow(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """Options Flow by Ticker"""
        if ticker is not None:
            return self._get(f"/market/options-flow/{quote(str(ticker))}", params)
        return self._get("/market/options-flow", params)
    def quotes_bulk(self, body: Any = None, **params: Any) -> Any:
        """Bulk Quotes"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        if isinstance(body, (list, tuple)):
            body = {"isins": list(body)}
        return self._post("/market/quotes/bulk", body, params)
    def quotes_exchanges(self, identifier: str, **params: Any) -> Any:
        """Multi-Exchange Quotes"""
        return self._get(f"/market/quotes/exchanges/{quote(str(identifier))}", params)
    def quotes_intraday(self, identifier: str, **params: Any) -> Any:
        """Intraday Quotes"""
        return self._get(f"/market/quotes/intraday/{quote(str(identifier))}", params)
    def quotes_latest(self, stocks: Any = None, **params: Any) -> Any:
        """Latest Quotes. Pass tickers to limit the response, e.g. quotes_latest(["AAPL", "MSFT"])."""
        if isinstance(stocks, dict):
            params = {**stocks, **params}
        elif stocks is not None:
            if isinstance(stocks, (list, tuple)):
                stocks = ",".join(str(s) for s in stocks)
            params = {"stocks": stocks, **params}
        return self._get("/market/quotes/latest", params)
    def risk_metrics(self, ticker: str, **params: Any) -> Any:
        """Precomputed Risk Metrics"""
        return self._get(f"/market/risk-metrics/{quote(str(ticker))}", params)
    def sector_performance(self, **params: Any) -> Any:
        """Sector Performance"""
        return self._get("/market/sector-performance", params)
    def top_movers(self, **params: Any) -> Any:
        """Top Gainers & Losers"""
        return self._get("/market/top-movers", params)
    def unusual_move(self, **params: Any) -> Any:
        """Unusual Price Moves"""
        return self._get("/market/unusual-move", params)
    def vix_term_structure(self, **params: Any) -> Any:
        """VIX Term Structure"""
        return self._get("/market/vix/term-structure", params)


class AsyncMarket(AsyncResource):
    async def analytics_52week(self, ticker: str, **params: Any) -> Any:
        """52-Week Analytics"""
        return await self._get(f"/market/analytics/52week/{quote(str(ticker))}", params)
    async def analytics_correlation(self, **params: Any) -> Any:
        """Stock Correlation"""
        return await self._get("/market/analytics/correlation", params)
    async def analytics_fx_returns(self, identifier: str, **params: Any) -> Any:
        """Currency-Adjusted Returns"""
        return await self._get(f"/market/analytics/fx-returns/{quote(str(identifier))}", params)
    async def analytics_risk(self, identifier: str, **params: Any) -> Any:
        """Risk & Return Analytics"""
        return await self._get(f"/market/analytics/risk/{quote(str(identifier))}", params)
    async def breadth(self, **params: Any) -> Any:
        """Market Breadth"""
        return await self._get("/market/breadth", params)
    async def cboe_indices(self, **params: Any) -> Any:
        """CBOE Indices"""
        return await self._get("/market/cboe/indices", params)
    async def dark_pool(self, ticker: str, **params: Any) -> Any:
        """Dark Pool Volume"""
        return await self._get(f"/market/dark-pool/{quote(str(ticker))}", params)
    async def etf_flows(self, ticker: str, **params: Any) -> Any:
        """ETF Fund Flows"""
        return await self._get(f"/market/etf-flows/{quote(str(ticker))}", params)
    async def exchanges(self, **params: Any) -> Any:
        """Exchanges"""
        return await self._get("/market/exchanges", params)
    async def fx(self, from_: str, to: str, **params: Any) -> Any:
        """FX Rate Series"""
        return await self._get(f"/market/fx/{quote(str(from_))}/{quote(str(to))}", params)
    async def holidays(self, exchange: Optional[str] = None, **params: Any) -> Any:
        """Holidays by Exchange"""
        if exchange is not None:
            return await self._get(f"/market/holidays/{quote(str(exchange))}", params)
        return await self._get("/market/holidays", params)
    async def indicators(self, **params: Any) -> Any:
        """Market Indicators"""
        return await self._get("/market/indicators", params)
    async def l2(self, ticker: str, **params: Any) -> Any:
        """Level 2 Order Book"""
        return await self._get(f"/market/l2/{quote(str(ticker))}", params)
    async def last_quote(self, ticker: str, **params: Any) -> Any:
        """Last Quote"""
        return await self._get(f"/market/last-quote/{quote(str(ticker))}", params)
    async def last_trade(self, ticker: str, **params: Any) -> Any:
        """Last Trade"""
        return await self._get(f"/market/last-trade/{quote(str(ticker))}", params)
    async def market_status(self, **params: Any) -> Any:
        """Market Status"""
        return await self._get("/market/market-status", params)
    async def most_shorted(self, **params: Any) -> Any:
        """Most Shorted Stocks"""
        return await self._get("/market/most-shorted", params)
    async def options(self, ticker: str, **params: Any) -> Any:
        """Options Chain"""
        return await self._get(f"/market/options/{quote(str(ticker))}", params)
    async def options_flow(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """Options Flow by Ticker"""
        if ticker is not None:
            return await self._get(f"/market/options-flow/{quote(str(ticker))}", params)
        return await self._get("/market/options-flow", params)
    async def quotes_bulk(self, body: Any = None, **params: Any) -> Any:
        """Bulk Quotes"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        if isinstance(body, (list, tuple)):
            body = {"isins": list(body)}
        return await self._post("/market/quotes/bulk", body, params)
    async def quotes_exchanges(self, identifier: str, **params: Any) -> Any:
        """Multi-Exchange Quotes"""
        return await self._get(f"/market/quotes/exchanges/{quote(str(identifier))}", params)
    async def quotes_intraday(self, identifier: str, **params: Any) -> Any:
        """Intraday Quotes"""
        return await self._get(f"/market/quotes/intraday/{quote(str(identifier))}", params)
    async def quotes_latest(self, stocks: Any = None, **params: Any) -> Any:
        """Latest Quotes. Pass tickers to limit the response, e.g. quotes_latest(["AAPL", "MSFT"])."""
        if isinstance(stocks, dict):
            params = {**stocks, **params}
        elif stocks is not None:
            if isinstance(stocks, (list, tuple)):
                stocks = ",".join(str(s) for s in stocks)
            params = {"stocks": stocks, **params}
        return await self._get("/market/quotes/latest", params)
    async def risk_metrics(self, ticker: str, **params: Any) -> Any:
        """Precomputed Risk Metrics"""
        return await self._get(f"/market/risk-metrics/{quote(str(ticker))}", params)
    async def sector_performance(self, **params: Any) -> Any:
        """Sector Performance"""
        return await self._get("/market/sector-performance", params)
    async def top_movers(self, **params: Any) -> Any:
        """Top Gainers & Losers"""
        return await self._get("/market/top-movers", params)
    async def unusual_move(self, **params: Any) -> Any:
        """Unusual Price Moves"""
        return await self._get("/market/unusual-move", params)
    async def vix_term_structure(self, **params: Any) -> Any:
        """VIX Term Structure"""
        return await self._get("/market/vix/term-structure", params)
