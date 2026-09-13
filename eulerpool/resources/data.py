from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Data(SyncResource):
    def catalog(self, **params: Any) -> Any:
        """Data catalog"""
        return self._get("/data/catalog", params)
    def health(self, **params: Any) -> Any:
        """Data health"""
        return self._get("/data/health", params)


class AsyncData(AsyncResource):
    async def catalog(self, **params: Any) -> Any:
        """Data catalog"""
        return await self._get("/data/catalog", params)
    async def health(self, **params: Any) -> Any:
        """Data health"""
        return await self._get("/data/health", params)
