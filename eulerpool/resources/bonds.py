from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Bonds(SyncResource):
    def profile(self, isin: str) -> Any:
        return self._get(f"/bonds/profile/{quote(isin)}")

    def prices(self, isin: str) -> Any:
        return self._get(f"/bonds/prices/{quote(isin)}")

    def yield_curve(self) -> Any:
        return self._get("/bonds/yield-curve")

    def list(self) -> Any:
        return self._get("/bonds/list")

    def ticks(self, identifier: str) -> Any:
        return self._get(f"/bonds/ticks/{quote(identifier)}")


class AsyncBonds(AsyncResource):
    async def profile(self, isin: str) -> Any:
        return await self._get(f"/bonds/profile/{quote(isin)}")

    async def prices(self, isin: str) -> Any:
        return await self._get(f"/bonds/prices/{quote(isin)}")

    async def yield_curve(self) -> Any:
        return await self._get("/bonds/yield-curve")

    async def list(self) -> Any:
        return await self._get("/bonds/list")

    async def ticks(self, identifier: str) -> Any:
        return await self._get(f"/bonds/ticks/{quote(identifier)}")
