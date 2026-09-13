from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Forex(SyncResource):
    def list(self, **params: Any) -> Any:
        """Forex List API"""
        return self._get("/forex/list", params)
    def rates(self, basecurrency: str, **params: Any) -> Any:
        """Forex Rates API"""
        return self._get(f"/forex/rates/{quote(str(basecurrency))}", params)


class AsyncForex(AsyncResource):
    async def list(self, **params: Any) -> Any:
        """Forex List API"""
        return await self._get("/forex/list", params)
    async def rates(self, basecurrency: str, **params: Any) -> Any:
        """Forex Rates API"""
        return await self._get(f"/forex/rates/{quote(str(basecurrency))}", params)
