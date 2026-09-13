from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Patents(SyncResource):
    def list(self, ticker: str, **params: Any) -> Any:
        """Company Patents API"""
        return self._get(f"/patents/list/{quote(str(ticker))}", params)
    def stats(self, ticker: str, **params: Any) -> Any:
        """Patent Statistics API"""
        return self._get(f"/patents/stats/{quote(str(ticker))}", params)


class AsyncPatents(AsyncResource):
    async def list(self, ticker: str, **params: Any) -> Any:
        """Company Patents API"""
        return await self._get(f"/patents/list/{quote(str(ticker))}", params)
    async def stats(self, ticker: str, **params: Any) -> Any:
        """Patent Statistics API"""
        return await self._get(f"/patents/stats/{quote(str(ticker))}", params)
