from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class MutualFund(SyncResource):
    def countries(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Countries"""
        return self._get(f"/mutual-fund/countries/{quote(str(symbol))}", params)
    def disclosure(self, symbol: str, **params: Any) -> Any:
        """Fund Disclosure (Quarterly)"""
        return self._get(f"/mutual-fund/disclosure/{quote(str(symbol))}", params)
    def holdings(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Holdings"""
        return self._get(f"/mutual-fund/holdings/{quote(str(symbol))}", params)
    def profile(self, identifier: str, **params: Any) -> Any:
        """Mutual Fund Profile"""
        return self._get(f"/mutual-fund/profile/{quote(str(identifier))}", params)
    def sectors(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Sectors"""
        return self._get(f"/mutual-fund/sectors/{quote(str(symbol))}", params)


class AsyncMutualFund(AsyncResource):
    async def countries(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Countries"""
        return await self._get(f"/mutual-fund/countries/{quote(str(symbol))}", params)
    async def disclosure(self, symbol: str, **params: Any) -> Any:
        """Fund Disclosure (Quarterly)"""
        return await self._get(f"/mutual-fund/disclosure/{quote(str(symbol))}", params)
    async def holdings(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Holdings"""
        return await self._get(f"/mutual-fund/holdings/{quote(str(symbol))}", params)
    async def profile(self, identifier: str, **params: Any) -> Any:
        """Mutual Fund Profile"""
        return await self._get(f"/mutual-fund/profile/{quote(str(identifier))}", params)
    async def sectors(self, symbol: str, **params: Any) -> Any:
        """Mutual Fund Sectors"""
        return await self._get(f"/mutual-fund/sectors/{quote(str(symbol))}", params)
