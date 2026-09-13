from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Bonds(SyncResource):
    def list(self, **params: Any) -> Any:
        """Bond List / Search API"""
        return self._get("/bonds/list", params)
    def prices(self, identifier: str, **params: Any) -> Any:
        return self._get(f"/bonds/prices/{quote(str(identifier))}", params)
    def profile(self, identifier: str, **params: Any) -> Any:
        return self._get(f"/bonds/profile/{quote(str(identifier))}", params)
    def ticks(self, identifier: str, **params: Any) -> Any:
        return self._get(f"/bonds/ticks/{quote(str(identifier))}", params)
    def yield_curve(self, **params: Any) -> Any:
        """Government Bond Yield Curve API"""
        return self._get("/bonds/yield-curve", params)


class AsyncBonds(AsyncResource):
    async def list(self, **params: Any) -> Any:
        """Bond List / Search API"""
        return await self._get("/bonds/list", params)
    async def prices(self, identifier: str, **params: Any) -> Any:
        return await self._get(f"/bonds/prices/{quote(str(identifier))}", params)
    async def profile(self, identifier: str, **params: Any) -> Any:
        return await self._get(f"/bonds/profile/{quote(str(identifier))}", params)
    async def ticks(self, identifier: str, **params: Any) -> Any:
        return await self._get(f"/bonds/ticks/{quote(str(identifier))}", params)
    async def yield_curve(self, **params: Any) -> Any:
        """Government Bond Yield Curve API"""
        return await self._get("/bonds/yield-curve", params)
