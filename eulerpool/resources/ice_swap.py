from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class IceSwap(SyncResource):
    def data(self, code: str) -> Any:
        return self._get(f"/ice-swap/{quote(code)}")


class AsyncIceSwap(AsyncResource):
    async def data(self, code: str) -> Any:
        return await self._get(f"/ice-swap/{quote(code)}")
