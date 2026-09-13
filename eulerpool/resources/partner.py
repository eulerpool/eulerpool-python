from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Partner(SyncResource):
    def alleaktien_fundamentals(self, **params: Any) -> Any:
        """AlleAktien Fundamentals"""
        return self._get("/partner/alleaktien/fundamentals", params)


class AsyncPartner(AsyncResource):
    async def alleaktien_fundamentals(self, **params: Any) -> Any:
        """AlleAktien Fundamentals"""
        return await self._get("/partner/alleaktien/fundamentals", params)
