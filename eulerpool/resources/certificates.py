from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Certificates(SyncResource):
    def profile(self, isin: str) -> Any:
        return self._get(f"/certificates/profile/{quote(isin)}")

    def list(self) -> Any:
        return self._get("/certificates/list")

    def quotes(self, isin: str) -> Any:
        return self._get(f"/certificates/quotes/{quote(isin)}")


class AsyncCertificates(AsyncResource):
    async def profile(self, isin: str) -> Any:
        return await self._get(f"/certificates/profile/{quote(isin)}")

    async def list(self) -> Any:
        return await self._get("/certificates/list")

    async def quotes(self, isin: str) -> Any:
        return await self._get(f"/certificates/quotes/{quote(isin)}")
