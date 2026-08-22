from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Screener(SyncResource):
    def screen(self, body: Any = None) -> Any:
        return self._post("/screener/screen", body)

    def universe(self) -> Any:
        return self._get("/screener/universe")

    def search(self, query: str) -> Any:
        return self._get(f"/screener/search/{quote(query)}")

    def metadata(self) -> Any:
        return self._get("/screener/metadata")


class AsyncScreener(AsyncResource):
    async def screen(self, body: Any = None) -> Any:
        return await self._post("/screener/screen", body)

    async def universe(self) -> Any:
        return await self._get("/screener/universe")

    async def search(self, query: str) -> Any:
        return await self._get(f"/screener/search/{quote(query)}")

    async def metadata(self) -> Any:
        return await self._get("/screener/metadata")
