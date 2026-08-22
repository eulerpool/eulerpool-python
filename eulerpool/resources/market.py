from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Market(SyncResource):
    def quotes_latest(self, stocks: str | list | None = None) -> Any:
        """Latest quotes. Pass tickers to limit the response, e.g. quotes_latest(["AAPL", "MSFT"])."""
        value = ",".join(stocks) if isinstance(stocks, (list, tuple)) else stocks
        return self._get("/market/quotes/latest", {"stocks": value} if value else None)

    def quotes_intraday(self, isin: str) -> Any:
        return self._get(f"/market/quotes/intraday/{quote(isin)}")

    def options(self, ticker: str) -> Any:
        return self._get(f"/market/options/{quote(ticker)}")

    def analytics_52week(self, ticker: str) -> Any:
        return self._get(f"/market/analytics/52week/{quote(ticker)}")

    def indicators(self) -> Any:
        return self._get("/market/indicators")

    def fx(self, from_currency: str, to_currency: str) -> Any:
        return self._get(f"/market/fx/{quote(from_currency)}/{quote(to_currency)}")

    def quotes_exchanges(self, isin: str) -> Any:
        return self._get(f"/market/quotes/exchanges/{quote(isin)}")

    def analytics_fx_returns(self, isin: str) -> Any:
        return self._get(f"/market/analytics/fx-returns/{quote(isin)}")

    def top_movers(self) -> Any:
        return self._get("/market/top-movers")

    def market_status(self) -> Any:
        return self._get("/market/market-status")

    def quotes_bulk(self, isins: list) -> Any:
        return self._post("/market/quotes/bulk", {"isins": isins})

    def analytics_risk(self, identifier: str) -> Any:
        return self._get(f"/market/analytics/risk/{quote(identifier)}")

    def analytics_correlation(self, *, isin1: str | None = None, isin2: str | None = None, range: str | None = None) -> Any:
        params = {}
        if isin1 is not None:
            params["isin1"] = isin1
        if isin2 is not None:
            params["isin2"] = isin2
        if range is not None:
            params["range"] = range
        return self._get("/market/analytics/correlation", params or None)

    def holidays(self) -> Any:
        return self._get("/market/holidays")


class AsyncMarket(AsyncResource):
    async def quotes_latest(self, stocks: str | list | None = None) -> Any:
        """Latest quotes. Pass tickers to limit the response, e.g. quotes_latest(["AAPL", "MSFT"])."""
        value = ",".join(stocks) if isinstance(stocks, (list, tuple)) else stocks
        return await self._get("/market/quotes/latest", {"stocks": value} if value else None)

    async def quotes_intraday(self, isin: str) -> Any:
        return await self._get(f"/market/quotes/intraday/{quote(isin)}")

    async def options(self, ticker: str) -> Any:
        return await self._get(f"/market/options/{quote(ticker)}")

    async def analytics_52week(self, ticker: str) -> Any:
        return await self._get(f"/market/analytics/52week/{quote(ticker)}")

    async def indicators(self) -> Any:
        return await self._get("/market/indicators")

    async def fx(self, from_currency: str, to_currency: str) -> Any:
        return await self._get(f"/market/fx/{quote(from_currency)}/{quote(to_currency)}")

    async def quotes_exchanges(self, isin: str) -> Any:
        return await self._get(f"/market/quotes/exchanges/{quote(isin)}")

    async def analytics_fx_returns(self, isin: str) -> Any:
        return await self._get(f"/market/analytics/fx-returns/{quote(isin)}")

    async def top_movers(self) -> Any:
        return await self._get("/market/top-movers")

    async def market_status(self) -> Any:
        return await self._get("/market/market-status")

    async def quotes_bulk(self, isins: list) -> Any:
        return await self._post("/market/quotes/bulk", {"isins": isins})

    async def analytics_risk(self, identifier: str) -> Any:
        return await self._get(f"/market/analytics/risk/{quote(identifier)}")

    async def analytics_correlation(self, *, isin1: str | None = None, isin2: str | None = None, range: str | None = None) -> Any:
        params = {}
        if isin1 is not None:
            params["isin1"] = isin1
        if isin2 is not None:
            params["isin2"] = isin2
        if range is not None:
            params["range"] = range
        return await self._get("/market/analytics/correlation", params or None)

    async def holidays(self) -> Any:
        return await self._get("/market/holidays")
