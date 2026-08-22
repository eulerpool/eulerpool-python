from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Institutional(SyncResource):
    def profile(self, cik: str) -> Any:
        return self._get(f"/institutional/profile/{quote(cik)}")

    def portfolio(self, cik: str) -> Any:
        return self._get(f"/institutional/portfolio/{quote(cik)}")


class AsyncInstitutional(AsyncResource):
    async def profile(self, cik: str) -> Any:
        return await self._get(f"/institutional/profile/{quote(cik)}")

    async def portfolio(self, cik: str) -> Any:
        return await self._get(f"/institutional/portfolio/{quote(cik)}")
