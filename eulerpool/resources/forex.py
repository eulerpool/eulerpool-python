from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Forex(SyncResource):
    def list(self) -> Any:
        return self._get("/forex/list")

    def rates(self, base_currency: str) -> Any:
        return self._get(f"/forex/rates/{quote(base_currency)}")


class AsyncForex(AsyncResource):
    async def list(self) -> Any:
        return await self._get("/forex/list")

    async def rates(self, base_currency: str) -> Any:
        return await self._get(f"/forex/rates/{quote(base_currency)}")
