from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Funds(SyncResource):
    def form_d(self, cik: Optional[str] = None, **params: Any) -> Any:
        """Form D Filings by CIK"""
        if cik is not None:
            return self._get(f"/funds/form-d/{quote(str(cik))}", params)
        return self._get("/funds/form-d", params)
    def nport(self, cik: Optional[str] = None, **params: Any) -> Any:
        """N-PORT Holdings by CIK"""
        if cik is not None:
            return self._get(f"/funds/nport/{quote(str(cik))}", params)
        return self._get("/funds/nport", params)


class AsyncFunds(AsyncResource):
    async def form_d(self, cik: Optional[str] = None, **params: Any) -> Any:
        """Form D Filings by CIK"""
        if cik is not None:
            return await self._get(f"/funds/form-d/{quote(str(cik))}", params)
        return await self._get("/funds/form-d", params)
    async def nport(self, cik: Optional[str] = None, **params: Any) -> Any:
        """N-PORT Holdings by CIK"""
        if cik is not None:
            return await self._get(f"/funds/nport/{quote(str(cik))}", params)
        return await self._get("/funds/nport", params)
