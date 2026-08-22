from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Index(SyncResource):
    def constituents(self, index_id: str) -> Any:
        return self._get(f"/index/constituents/{quote(index_id)}")


class AsyncIndex(AsyncResource):
    async def constituents(self, index_id: str) -> Any:
        return await self._get(f"/index/constituents/{quote(index_id)}")
