from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class EquityExtended(SyncResource):
    def aaqs(self, isin: str) -> Any:
        return self._get(f"/equity-extended/aaqs/{quote(isin)}")

    def options_chain(self, isin: str) -> Any:
        return self._get(f"/equity-extended/options-chain/{quote(isin)}")

    def technical_signals(self, isin: str) -> Any:
        return self._get(f"/equity-extended/technical-signals/{quote(isin)}")

    def basic_financials(self, isin: str) -> Any:
        return self._get(f"/equity-extended/basic-financials/{quote(isin)}")

    def ebitda_estimates(self, isin: str) -> Any:
        return self._get(f"/equity-extended/ebitda-estimates/{quote(isin)}")

    def sec_filings(self, isin: str) -> Any:
        return self._get(f"/equity-extended/sec-filings/{quote(isin)}")

    def earnings_calendar(self, isin: str) -> Any:
        return self._get(f"/equity-extended/earnings-calendar/{quote(isin)}")

    def tech_indicators(self, isin: str) -> Any:
        return self._get(f"/equity-extended/tech-indicators/{quote(isin)}")

    def price_target_history(self, isin: str) -> Any:
        return self._get(f"/equity-extended/price-target-history/{quote(isin)}")

    def peers(self, isin: str) -> Any:
        return self._get(f"/equity-extended/peers/{quote(isin)}")

    def short_interest(self, isin: str) -> Any:
        return self._get(f"/equity-extended/short-interest/{quote(isin)}")

    def short_volume(self, isin: str) -> Any:
        return self._get(f"/equity-extended/short-volume/{quote(isin)}")

    def index_history(self, symbol: str) -> Any:
        return self._get(f"/equity-extended/index-history/{quote(symbol)}")

    def market_news(self) -> Any:
        return self._get("/equity-extended/market-news")

    def symbol_changes(self) -> Any:
        return self._get("/equity-extended/symbol-changes")

    def isin_changes(self) -> Any:
        return self._get("/equity-extended/isin-changes")

    def financials_reported(self, isin: str) -> Any:
        return self._get(f"/equity-extended/financials-reported/{quote(isin)}")

    def aggregate_signals(self, isin: str) -> Any:
        return self._get(f"/equity-extended/aggregate-signals/{quote(isin)}")


class AsyncEquityExtended(AsyncResource):
    async def aaqs(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/aaqs/{quote(isin)}")

    async def options_chain(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/options-chain/{quote(isin)}")

    async def technical_signals(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/technical-signals/{quote(isin)}")

    async def basic_financials(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/basic-financials/{quote(isin)}")

    async def ebitda_estimates(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/ebitda-estimates/{quote(isin)}")

    async def sec_filings(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/sec-filings/{quote(isin)}")

    async def earnings_calendar(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/earnings-calendar/{quote(isin)}")

    async def tech_indicators(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/tech-indicators/{quote(isin)}")

    async def price_target_history(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/price-target-history/{quote(isin)}")

    async def peers(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/peers/{quote(isin)}")

    async def short_interest(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/short-interest/{quote(isin)}")

    async def short_volume(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/short-volume/{quote(isin)}")

    async def index_history(self, symbol: str) -> Any:
        return await self._get(f"/equity-extended/index-history/{quote(symbol)}")

    async def market_news(self) -> Any:
        return await self._get("/equity-extended/market-news")

    async def symbol_changes(self) -> Any:
        return await self._get("/equity-extended/symbol-changes")

    async def isin_changes(self) -> Any:
        return await self._get("/equity-extended/isin-changes")

    async def financials_reported(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/financials-reported/{quote(isin)}")

    async def aggregate_signals(self, isin: str) -> Any:
        return await self._get(f"/equity-extended/aggregate-signals/{quote(isin)}")
