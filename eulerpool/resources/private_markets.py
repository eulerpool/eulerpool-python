from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class PrivateMarkets(SyncResource):
    def companies(self, **params: Any) -> Any:
        """Private Companies"""
        return self._get("/private-markets/companies", params)
    def funding(self, company: str, **params: Any) -> Any:
        """Funding Rounds"""
        return self._get(f"/private-markets/funding/{quote(str(company))}", params)


class AsyncPrivateMarkets(AsyncResource):
    async def companies(self, **params: Any) -> Any:
        """Private Companies"""
        return await self._get("/private-markets/companies", params)
    async def funding(self, company: str, **params: Any) -> Any:
        """Funding Rounds"""
        return await self._get(f"/private-markets/funding/{quote(str(company))}", params)
