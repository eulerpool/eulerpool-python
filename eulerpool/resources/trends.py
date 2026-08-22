from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Trends(SyncResource):
    def ticker_trends(self, symbol: str) -> Any:
        return self._get(f"/trends/ticker-trends/{quote(symbol)}")


class AsyncTrends(AsyncResource):
    async def ticker_trends(self, symbol: str) -> Any:
        return await self._get(f"/trends/ticker-trends/{quote(symbol)}")
