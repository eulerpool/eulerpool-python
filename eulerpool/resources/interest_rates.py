from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class InterestRates(SyncResource):
    def rates(self, series_id: Optional[str] = None, **params: Any) -> Any:
        """FRED interest rate history"""
        if series_id is not None:
            return self._get(f"/interest-rates/rates/{quote(str(series_id))}", params)
        return self._get("/interest-rates/rates", params)
    def spreads(self, **params: Any) -> Any:
        """US Treasury spreads (latest)"""
        return self._get("/interest-rates/spreads", params)
    def yield_curve(self, **params: Any) -> Any:
        """US Treasury yield curve (latest)"""
        return self._get("/interest-rates/yield-curve", params)


class AsyncInterestRates(AsyncResource):
    async def rates(self, series_id: Optional[str] = None, **params: Any) -> Any:
        """FRED interest rate history"""
        if series_id is not None:
            return await self._get(f"/interest-rates/rates/{quote(str(series_id))}", params)
        return await self._get("/interest-rates/rates", params)
    async def spreads(self, **params: Any) -> Any:
        """US Treasury spreads (latest)"""
        return await self._get("/interest-rates/spreads", params)
    async def yield_curve(self, **params: Any) -> Any:
        """US Treasury yield curve (latest)"""
        return await self._get("/interest-rates/yield-curve", params)
