from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Etf(SyncResource):
    def profile(self, isin: str) -> Any:
        return self._get(f"/etf/profile/{quote(isin)}")

    def holdings(self, isin: str) -> Any:
        return self._get(f"/etf/holdings/{quote(isin)}")

    def sectors(self, isin: str) -> Any:
        return self._get(f"/etf/sectors/{quote(isin)}")

    def countries(self, isin: str) -> Any:
        return self._get(f"/etf/countries/{quote(isin)}")

    def quotes(self, isin: str) -> Any:
        return self._get(f"/etf/quotes/{quote(isin)}")

    def description(self, isin: str) -> Any:
        return self._get(f"/etf/description/{quote(isin)}")

    def list(self, start: int, end: int) -> Any:
        return self._get(f"/etf/list/{start}/{end}")


class AsyncEtf(AsyncResource):
    async def profile(self, isin: str) -> Any:
        return await self._get(f"/etf/profile/{quote(isin)}")

    async def holdings(self, isin: str) -> Any:
        return await self._get(f"/etf/holdings/{quote(isin)}")

    async def sectors(self, isin: str) -> Any:
        return await self._get(f"/etf/sectors/{quote(isin)}")

    async def countries(self, isin: str) -> Any:
        return await self._get(f"/etf/countries/{quote(isin)}")

    async def quotes(self, isin: str) -> Any:
        return await self._get(f"/etf/quotes/{quote(isin)}")

    async def description(self, isin: str) -> Any:
        return await self._get(f"/etf/description/{quote(isin)}")

    async def list(self, start: int, end: int) -> Any:
        return await self._get(f"/etf/list/{start}/{end}")
