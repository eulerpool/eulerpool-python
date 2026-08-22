from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class MutualFund(SyncResource):
    def profile(self, isin: str) -> Any:
        return self._get(f"/mutual-fund/profile/{quote(isin)}")

    def holdings(self, symbol: str) -> Any:
        return self._get(f"/mutual-fund/holdings/{quote(symbol)}")

    def sectors(self, symbol: str) -> Any:
        return self._get(f"/mutual-fund/sectors/{quote(symbol)}")

    def countries(self, symbol: str) -> Any:
        return self._get(f"/mutual-fund/countries/{quote(symbol)}")


class AsyncMutualFund(AsyncResource):
    async def profile(self, isin: str) -> Any:
        return await self._get(f"/mutual-fund/profile/{quote(isin)}")

    async def holdings(self, symbol: str) -> Any:
        return await self._get(f"/mutual-fund/holdings/{quote(symbol)}")

    async def sectors(self, symbol: str) -> Any:
        return await self._get(f"/mutual-fund/sectors/{quote(symbol)}")

    async def countries(self, symbol: str) -> Any:
        return await self._get(f"/mutual-fund/countries/{quote(symbol)}")
