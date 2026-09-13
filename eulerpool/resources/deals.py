from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Deals(SyncResource):
    def ma(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """M&A Deals by Ticker"""
        if ticker is not None:
            return self._get(f"/deals/ma/{quote(str(ticker))}", params)
        return self._get("/deals/ma", params)
    def ma_stats_monthly(self, **params: Any) -> Any:
        """M&A Monthly Activity"""
        return self._get("/deals/ma/stats/monthly", params)


class AsyncDeals(AsyncResource):
    async def ma(self, ticker: Optional[str] = None, **params: Any) -> Any:
        """M&A Deals by Ticker"""
        if ticker is not None:
            return await self._get(f"/deals/ma/{quote(str(ticker))}", params)
        return await self._get("/deals/ma", params)
    async def ma_stats_monthly(self, **params: Any) -> Any:
        """M&A Monthly Activity"""
        return await self._get("/deals/ma/stats/monthly", params)
