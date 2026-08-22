from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class News(SyncResource):
    def feed(self, *, language: Optional[str] = None, type: Optional[str] = None) -> Any:
        params = {}
        if language is not None:
            params["language"] = language
        if type is not None:
            params["type"] = type
        return self._get("/eulerpool-news/feed.xml", params or None)

    def list(self, start: int, end: int) -> Any:
        return self._get(f"/eulerpool-news/news/{start}/{end}")

    def by_name(self, name: str) -> Any:
        return self._get(f"/eulerpool-news/by-name/{quote(name)}")

    def by_isin(self, identifier: str) -> Any:
        return self._get(f"/eulerpool-news/by-isin/{quote(identifier)}")


class AsyncNews(AsyncResource):
    async def feed(self, *, language: Optional[str] = None, type: Optional[str] = None) -> Any:
        params = {}
        if language is not None:
            params["language"] = language
        if type is not None:
            params["type"] = type
        return await self._get("/eulerpool-news/feed.xml", params or None)

    async def list(self, start: int, end: int) -> Any:
        return await self._get(f"/eulerpool-news/news/{start}/{end}")

    async def by_name(self, name: str) -> Any:
        return await self._get(f"/eulerpool-news/by-name/{quote(name)}")

    async def by_isin(self, identifier: str) -> Any:
        return await self._get(f"/eulerpool-news/by-isin/{quote(identifier)}")
