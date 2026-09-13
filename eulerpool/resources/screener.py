from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Screener(SyncResource):
    def metadata(self, **params: Any) -> Any:
        """Screener Metadata"""
        return self._get("/screener/metadata", params)
    def screen(self, body: Any = None, **params: Any) -> Any:
        """Stock Screener"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/screener/screen", body, params)
    def search(self, query: str, **params: Any) -> Any:
        """Symbol Search"""
        return self._get(f"/screener/search/{quote(str(query))}", params)
    def universe(self, **params: Any) -> Any:
        """Screener Universe"""
        return self._get("/screener/universe", params)


class AsyncScreener(AsyncResource):
    async def metadata(self, **params: Any) -> Any:
        """Screener Metadata"""
        return await self._get("/screener/metadata", params)
    async def screen(self, body: Any = None, **params: Any) -> Any:
        """Stock Screener"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/screener/screen", body, params)
    async def search(self, query: str, **params: Any) -> Any:
        """Symbol Search"""
        return await self._get(f"/screener/search/{quote(str(query))}", params)
    async def universe(self, **params: Any) -> Any:
        """Screener Universe"""
        return await self._get("/screener/universe", params)
