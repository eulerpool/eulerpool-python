from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Certificates(SyncResource):
    def list(self, **params: Any) -> Any:
        """Certificate List API"""
        return self._get("/certificates/list", params)
    def profile(self, identifier: str, **params: Any) -> Any:
        """Certificate Profile API"""
        return self._get(f"/certificates/profile/{quote(str(identifier))}", params)
    def quotes(self, identifier: str, **params: Any) -> Any:
        """Certificate Quotes API"""
        return self._get(f"/certificates/quotes/{quote(str(identifier))}", params)


class AsyncCertificates(AsyncResource):
    async def list(self, **params: Any) -> Any:
        """Certificate List API"""
        return await self._get("/certificates/list", params)
    async def profile(self, identifier: str, **params: Any) -> Any:
        """Certificate Profile API"""
        return await self._get(f"/certificates/profile/{quote(str(identifier))}", params)
    async def quotes(self, identifier: str, **params: Any) -> Any:
        """Certificate Quotes API"""
        return await self._get(f"/certificates/quotes/{quote(str(identifier))}", params)
