from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class FairValue(SyncResource):
    def by_isin(self, identifier: str, **params: Any) -> Any:
        """Fair Value"""
        return self._get(f"/fair-value/by-isin/{quote(str(identifier))}", params)


class AsyncFairValue(AsyncResource):
    async def by_isin(self, identifier: str, **params: Any) -> Any:
        """Fair Value"""
        return await self._get(f"/fair-value/by-isin/{quote(str(identifier))}", params)
