from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Crypto(SyncResource):
    def list(self, start: int, end: int) -> Any:
        return self._get(f"/crypto/list/{start}/{end}")

    def profile(self, symbol: str) -> Any:
        return self._get(f"/crypto/profile/{quote(symbol)}")

    def quotes(self, identifier: str) -> Any:
        return self._get(f"/crypto/quotes/{quote(identifier)}")


class AsyncCrypto(AsyncResource):
    async def list(self, start: int, end: int) -> Any:
        return await self._get(f"/crypto/list/{start}/{end}")

    async def profile(self, symbol: str) -> Any:
        return await self._get(f"/crypto/profile/{quote(symbol)}")

    async def quotes(self, identifier: str) -> Any:
        return await self._get(f"/crypto/quotes/{quote(identifier)}")
