from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Dex(SyncResource):
    def categories(self, **params: Any) -> Any:
        """Onchain Token Categories"""
        return self._get("/dex/categories", params)
    def dexes(self, network: str, **params: Any) -> Any:
        """DEXes on a Network"""
        return self._get(f"/dex/dexes/{quote(str(network))}", params)
    def networks(self, **params: Any) -> Any:
        """Onchain DEX Networks"""
        return self._get("/dex/networks", params)
    def new_pools(self, **params: Any) -> Any:
        """Newly Created DEX Pools"""
        return self._get("/dex/new-pools", params)
    def pool_ohlcv(self, network: str, address: str, **params: Any) -> Any:
        """DEX Pool OHLCV"""
        return self._get(f"/dex/pool-ohlcv/{quote(str(network))}/{quote(str(address))}", params)
    def pools(self, network: str, **params: Any) -> Any:
        """Top DEX Pools by Network"""
        return self._get(f"/dex/pools/{quote(str(network))}", params)
    def trending_pools(self, **params: Any) -> Any:
        """Trending DEX Pools"""
        return self._get("/dex/trending-pools", params)


class AsyncDex(AsyncResource):
    async def categories(self, **params: Any) -> Any:
        """Onchain Token Categories"""
        return await self._get("/dex/categories", params)
    async def dexes(self, network: str, **params: Any) -> Any:
        """DEXes on a Network"""
        return await self._get(f"/dex/dexes/{quote(str(network))}", params)
    async def networks(self, **params: Any) -> Any:
        """Onchain DEX Networks"""
        return await self._get("/dex/networks", params)
    async def new_pools(self, **params: Any) -> Any:
        """Newly Created DEX Pools"""
        return await self._get("/dex/new-pools", params)
    async def pool_ohlcv(self, network: str, address: str, **params: Any) -> Any:
        """DEX Pool OHLCV"""
        return await self._get(f"/dex/pool-ohlcv/{quote(str(network))}/{quote(str(address))}", params)
    async def pools(self, network: str, **params: Any) -> Any:
        """Top DEX Pools by Network"""
        return await self._get(f"/dex/pools/{quote(str(network))}", params)
    async def trending_pools(self, **params: Any) -> Any:
        """Trending DEX Pools"""
        return await self._get("/dex/trending-pools", params)
