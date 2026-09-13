from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class IceSwap(SyncResource):
    def data(self, code: str, **params: Any) -> Any:
        """ICE-SWAP data api"""
        return self._get(f"/ice-swap/{quote(str(code))}", params)


class AsyncIceSwap(AsyncResource):
    async def data(self, code: str, **params: Any) -> Any:
        """ICE-SWAP data api"""
        return await self._get(f"/ice-swap/{quote(str(code))}", params)
