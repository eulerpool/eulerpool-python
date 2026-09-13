from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class News(SyncResource):
    def feed(self, **params: Any) -> Any:
        """News Feed RSS XML"""
        return self._get("/news/feed.xml", params)


class AsyncNews(AsyncResource):
    async def feed(self, **params: Any) -> Any:
        """News Feed RSS XML"""
        return await self._get("/news/feed.xml", params)
