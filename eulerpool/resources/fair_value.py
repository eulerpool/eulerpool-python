from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class FairValue(SyncResource):
    def by_isin(self, isin: str) -> Any:
        return self._get(f"/fair-value/by-isin/{quote(isin)}")


class AsyncFairValue(AsyncResource):
    async def by_isin(self, isin: str) -> Any:
        return await self._get(f"/fair-value/by-isin/{quote(isin)}")
