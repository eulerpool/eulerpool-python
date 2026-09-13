from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Analytics(SyncResource):
    def cftc_tff(self, market_code: Optional[str] = None, **params: Any) -> Any:
        """CFTC TFF Report"""
        if market_code is not None:
            return self._get(f"/analytics/cftc/tff/{quote(str(market_code))}", params)
        return self._get("/analytics/cftc/tff", params)
    def corporate_events(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """Corporate Events"""
        if ticker is not None:
            return self._get(f"/analytics/corporate-events/{quote(str(ticker))}", params)
        return self._get("/analytics/corporate-events", params)
    def earnings_calendar(self, **params: Any) -> Any:
        """Earnings Calendar"""
        return self._get("/analytics/earnings-calendar", params)
    def fama_french(self, **params: Any) -> Any:
        """Fama-French Factors"""
        return self._get("/analytics/fama-french", params)
    def options_volume(self, **params: Any) -> Any:
        """Options Volume"""
        return self._get("/analytics/options-volume", params)


class AsyncAnalytics(AsyncResource):
    async def cftc_tff(self, market_code: Optional[str] = None, **params: Any) -> Any:
        """CFTC TFF Report"""
        if market_code is not None:
            return await self._get(f"/analytics/cftc/tff/{quote(str(market_code))}", params)
        return await self._get("/analytics/cftc/tff", params)
    async def corporate_events(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """Corporate Events"""
        if ticker is not None:
            return await self._get(f"/analytics/corporate-events/{quote(str(ticker))}", params)
        return await self._get("/analytics/corporate-events", params)
    async def earnings_calendar(self, **params: Any) -> Any:
        """Earnings Calendar"""
        return await self._get("/analytics/earnings-calendar", params)
    async def fama_french(self, **params: Any) -> Any:
        """Fama-French Factors"""
        return await self._get("/analytics/fama-french", params)
    async def options_volume(self, **params: Any) -> Any:
        """Options Volume"""
        return await self._get("/analytics/options-volume", params)
