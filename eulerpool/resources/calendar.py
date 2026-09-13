from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Calendar(SyncResource):
    def dividends(self, year: str, **params: Any) -> Any:
        """Dividend Calendar"""
        return self._get(f"/calendar/dividends/{quote(str(year))}", params)
    def dividends_forward(self, **params: Any) -> Any:
        """Forward Dividend Calendar"""
        return self._get("/calendar/dividends-forward", params)
    def earnings(self, date: str, **params: Any) -> Any:
        """Earnings Calendar (Weekly)"""
        return self._get(f"/calendar/earnings/{quote(str(date))}", params)
    def earnings_by_symbol(self, symbol: str, **params: Any) -> Any:
        """Earnings Calendar by Symbol"""
        return self._get(f"/calendar/earnings-by-symbol/{quote(str(symbol))}", params)
    def earnings_surprises(self, symbol: str, **params: Any) -> Any:
        """Earnings Surprises"""
        return self._get(f"/calendar/earnings-surprises/{quote(str(symbol))}", params)
    def economic_calendar(self, **params: Any) -> Any:
        """Economic Calendar"""
        return self._get("/calendar/economic-calendar", params)
    def economic_calendar_history(self, **params: Any) -> Any:
        """Economic Calendar History"""
        return self._get("/calendar/economic-calendar/history", params)
    def ipo(self, **params: Any) -> Any:
        """IPO Calendar"""
        return self._get("/calendar/ipo", params)
    def ipo_pipeline(self, **params: Any) -> Any:
        """IPO Pipeline"""
        return self._get("/calendar/ipo-pipeline", params)
    def ma_deals(self, **params: Any) -> Any:
        """M&A Deal Tracker"""
        return self._get("/calendar/ma-deals", params)
    def spac(self, **params: Any) -> Any:
        """SPAC Tracker"""
        return self._get("/calendar/spac", params)


class AsyncCalendar(AsyncResource):
    async def dividends(self, year: str, **params: Any) -> Any:
        """Dividend Calendar"""
        return await self._get(f"/calendar/dividends/{quote(str(year))}", params)
    async def dividends_forward(self, **params: Any) -> Any:
        """Forward Dividend Calendar"""
        return await self._get("/calendar/dividends-forward", params)
    async def earnings(self, date: str, **params: Any) -> Any:
        """Earnings Calendar (Weekly)"""
        return await self._get(f"/calendar/earnings/{quote(str(date))}", params)
    async def earnings_by_symbol(self, symbol: str, **params: Any) -> Any:
        """Earnings Calendar by Symbol"""
        return await self._get(f"/calendar/earnings-by-symbol/{quote(str(symbol))}", params)
    async def earnings_surprises(self, symbol: str, **params: Any) -> Any:
        """Earnings Surprises"""
        return await self._get(f"/calendar/earnings-surprises/{quote(str(symbol))}", params)
    async def economic_calendar(self, **params: Any) -> Any:
        """Economic Calendar"""
        return await self._get("/calendar/economic-calendar", params)
    async def economic_calendar_history(self, **params: Any) -> Any:
        """Economic Calendar History"""
        return await self._get("/calendar/economic-calendar/history", params)
    async def ipo(self, **params: Any) -> Any:
        """IPO Calendar"""
        return await self._get("/calendar/ipo", params)
    async def ipo_pipeline(self, **params: Any) -> Any:
        """IPO Pipeline"""
        return await self._get("/calendar/ipo-pipeline", params)
    async def ma_deals(self, **params: Any) -> Any:
        """M&A Deal Tracker"""
        return await self._get("/calendar/ma-deals", params)
    async def spac(self, **params: Any) -> Any:
        """SPAC Tracker"""
        return await self._get("/calendar/spac", params)
