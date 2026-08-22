from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Commodity(SyncResource):
    def profile(self, ticker: str) -> Any:
        return self._get(f"/commodity/profile/{quote(ticker)}")

    def quotes(self, ticker: str) -> Any:
        return self._get(f"/commodity/quotes/{quote(ticker)}")

    def list(self) -> Any:
        return self._get("/commodity/list")


class AsyncCommodity(AsyncResource):
    async def profile(self, ticker: str) -> Any:
        return await self._get(f"/commodity/profile/{quote(ticker)}")

    async def quotes(self, ticker: str) -> Any:
        return await self._get(f"/commodity/quotes/{quote(ticker)}")

    async def list(self) -> Any:
        return await self._get("/commodity/list")
