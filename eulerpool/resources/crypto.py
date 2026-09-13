from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Crypto(SyncResource):
    def list(self, start: str, end: str, **params: Any) -> Any:
        """Crypto List (Paginated) API"""
        return self._get(f"/crypto/list/{quote(str(start))}/{quote(str(end))}", params)
    def profile(self, symbol: str, **params: Any) -> Any:
        """Crypto Profile API"""
        return self._get(f"/crypto/profile/{quote(str(symbol))}", params)
    def quotes(self, identifier: str, **params: Any) -> Any:
        """Crypto Quotes API"""
        return self._get(f"/crypto/quotes/{quote(str(identifier))}", params)


class AsyncCrypto(AsyncResource):
    async def list(self, start: str, end: str, **params: Any) -> Any:
        """Crypto List (Paginated) API"""
        return await self._get(f"/crypto/list/{quote(str(start))}/{quote(str(end))}", params)
    async def profile(self, symbol: str, **params: Any) -> Any:
        """Crypto Profile API"""
        return await self._get(f"/crypto/profile/{quote(str(symbol))}", params)
    async def quotes(self, identifier: str, **params: Any) -> Any:
        """Crypto Quotes API"""
        return await self._get(f"/crypto/quotes/{quote(str(identifier))}", params)
