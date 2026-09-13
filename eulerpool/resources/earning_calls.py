from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class EarningCalls(SyncResource):
    def list(self, ticker: str, **params: Any) -> Any:
        """List earning call transcripts by ticker"""
        return self._get(f"/earning-calls/list/{quote(str(ticker))}", params)
    def transcript(self, id: str, **params: Any) -> Any:
        """Get earning call transcript by ID"""
        return self._get(f"/earning-calls/transcript/{quote(str(id))}", params)


class AsyncEarningCalls(AsyncResource):
    async def list(self, ticker: str, **params: Any) -> Any:
        """List earning call transcripts by ticker"""
        return await self._get(f"/earning-calls/list/{quote(str(ticker))}", params)
    async def transcript(self, id: str, **params: Any) -> Any:
        """Get earning call transcript by ID"""
        return await self._get(f"/earning-calls/transcript/{quote(str(id))}", params)
