from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Trends(SyncResource):
    def ticker_trends(self, symbol: str, **params: Any) -> Any:
        """Ticker and Trends API"""
        return self._get(f"/trends/ticker-trends/{quote(str(symbol))}", params)


class AsyncTrends(AsyncResource):
    async def ticker_trends(self, symbol: str, **params: Any) -> Any:
        """Ticker and Trends API"""
        return await self._get(f"/trends/ticker-trends/{quote(str(symbol))}", params)
