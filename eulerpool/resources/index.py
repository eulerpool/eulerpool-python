from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Index(SyncResource):
    def basket(self, body: Any = None, **params: Any) -> Any:
        """Custom Basket Builder"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/index/basket", body, params)
    def constituents(self, id: str, **params: Any) -> Any:
        """Index Constituents"""
        return self._get(f"/index/constituents/{quote(str(id))}", params)


class AsyncIndex(AsyncResource):
    async def basket(self, body: Any = None, **params: Any) -> Any:
        """Custom Basket Builder"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/index/basket", body, params)
    async def constituents(self, id: str, **params: Any) -> Any:
        """Index Constituents"""
        return await self._get(f"/index/constituents/{quote(str(id))}", params)
