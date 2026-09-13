from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Nft(SyncResource):
    def list(self, **params: Any) -> Any:
        """NFT Collections List API"""
        return self._get("/nft/list", params)
    def market_chart(self, id: str, **params: Any) -> Any:
        """NFT Collection Price History"""
        return self._get(f"/nft/market-chart/{quote(str(id))}", params)
    def markets(self, **params: Any) -> Any:
        """NFT Markets Ranking"""
        return self._get("/nft/markets", params)
    def profile(self, id: str, **params: Any) -> Any:
        """NFT Collection Profile API"""
        return self._get(f"/nft/profile/{quote(str(id))}", params)
    def search(self, query: str, **params: Any) -> Any:
        """NFT Collection Search API"""
        return self._get(f"/nft/search/{quote(str(query))}", params)


class AsyncNft(AsyncResource):
    async def list(self, **params: Any) -> Any:
        """NFT Collections List API"""
        return await self._get("/nft/list", params)
    async def market_chart(self, id: str, **params: Any) -> Any:
        """NFT Collection Price History"""
        return await self._get(f"/nft/market-chart/{quote(str(id))}", params)
    async def markets(self, **params: Any) -> Any:
        """NFT Markets Ranking"""
        return await self._get("/nft/markets", params)
    async def profile(self, id: str, **params: Any) -> Any:
        """NFT Collection Profile API"""
        return await self._get(f"/nft/profile/{quote(str(id))}", params)
    async def search(self, query: str, **params: Any) -> Any:
        """NFT Collection Search API"""
        return await self._get(f"/nft/search/{quote(str(query))}", params)
