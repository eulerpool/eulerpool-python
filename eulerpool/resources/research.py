from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Research(SyncResource):
    def recommendations(self, ticker: str) -> Any:
        return self._get(f"/research/recommendations/{quote(ticker)}")

    def news(self, ticker: str) -> Any:
        return self._get(f"/research/news/{quote(ticker)}")

    def press_releases(self, ticker: str) -> Any:
        return self._get(f"/research/press-releases/{quote(ticker)}")


class AsyncResearch(AsyncResource):
    async def recommendations(self, ticker: str) -> Any:
        return await self._get(f"/research/recommendations/{quote(ticker)}")

    async def news(self, ticker: str) -> Any:
        return await self._get(f"/research/news/{quote(ticker)}")

    async def press_releases(self, ticker: str) -> Any:
        return await self._get(f"/research/press-releases/{quote(ticker)}")
