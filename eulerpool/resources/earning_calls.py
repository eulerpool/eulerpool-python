from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class EarningCalls(SyncResource):
    def list(self, ticker: str) -> Any:
        return self._get(f"/earning-calls/list/{quote(ticker)}")

    def transcript(self, call_id: str) -> Any:
        return self._get(f"/earning-calls/transcript/{quote(call_id)}")


class AsyncEarningCalls(AsyncResource):
    async def list(self, ticker: str) -> Any:
        return await self._get(f"/earning-calls/list/{quote(ticker)}")

    async def transcript(self, call_id: str) -> Any:
        return await self._get(f"/earning-calls/transcript/{quote(call_id)}")
