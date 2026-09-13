from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class EconomicForecasts(SyncResource):
    def get(self, country: str, indicator: Optional[str] = None, **params: Any) -> Any:
        """Country Indicator Forecast"""
        if indicator is not None:
            return self._get(f"/economic-forecasts/{quote(str(country))}/{quote(str(indicator))}", params)
        return self._get(f"/economic-forecasts/{quote(str(country))}", params)
    def indicators(self, **params: Any) -> Any:
        """Forecast Indicators"""
        return self._get("/economic-forecasts/indicators", params)


class AsyncEconomicForecasts(AsyncResource):
    async def get(self, country: str, indicator: Optional[str] = None, **params: Any) -> Any:
        """Country Indicator Forecast"""
        if indicator is not None:
            return await self._get(f"/economic-forecasts/{quote(str(country))}/{quote(str(indicator))}", params)
        return await self._get(f"/economic-forecasts/{quote(str(country))}", params)
    async def indicators(self, **params: Any) -> Any:
        """Forecast Indicators"""
        return await self._get("/economic-forecasts/indicators", params)
