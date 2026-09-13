from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Aaq(SyncResource):
    def by_isin(self, identifier: str, **params: Any) -> Any:
        """AAQS Score"""
        return self._get(f"/aaqs/by-isin/{quote(str(identifier))}", params)


class AsyncAaq(AsyncResource):
    async def by_isin(self, identifier: str, **params: Any) -> Any:
        """AAQS Score"""
        return await self._get(f"/aaqs/by-isin/{quote(str(identifier))}", params)
