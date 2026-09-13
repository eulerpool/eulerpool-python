from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Shipping(SyncResource):
    def cargoes(self, **params: Any) -> Any:
        """Cargo Movements"""
        return self._get("/shipping/cargoes", params)
    def ports(self, **params: Any) -> Any:
        """Ports"""
        return self._get("/shipping/ports", params)
    def ports_activity(self, id: str, **params: Any) -> Any:
        """Port Activity"""
        return self._get(f"/shipping/ports/{quote(str(id))}/activity", params)
    def positions(self, **params: Any) -> Any:
        """Current Positions"""
        return self._get("/shipping/positions", params)
    def vessels(self, imo: Optional[str] = None, **params: Any) -> Any:
        """Vessel Details"""
        if imo is not None:
            return self._get(f"/shipping/vessels/{quote(str(imo))}", params)
        return self._get("/shipping/vessels", params)
    def vessels_track(self, imo: str, **params: Any) -> Any:
        """Vessel Track"""
        return self._get(f"/shipping/vessels/{quote(str(imo))}/track", params)
    def voyages(self, **params: Any) -> Any:
        """Active Voyages"""
        return self._get("/shipping/voyages", params)


class AsyncShipping(AsyncResource):
    async def cargoes(self, **params: Any) -> Any:
        """Cargo Movements"""
        return await self._get("/shipping/cargoes", params)
    async def ports(self, **params: Any) -> Any:
        """Ports"""
        return await self._get("/shipping/ports", params)
    async def ports_activity(self, id: str, **params: Any) -> Any:
        """Port Activity"""
        return await self._get(f"/shipping/ports/{quote(str(id))}/activity", params)
    async def positions(self, **params: Any) -> Any:
        """Current Positions"""
        return await self._get("/shipping/positions", params)
    async def vessels(self, imo: Optional[str] = None, **params: Any) -> Any:
        """Vessel Details"""
        if imo is not None:
            return await self._get(f"/shipping/vessels/{quote(str(imo))}", params)
        return await self._get("/shipping/vessels", params)
    async def vessels_track(self, imo: str, **params: Any) -> Any:
        """Vessel Track"""
        return await self._get(f"/shipping/vessels/{quote(str(imo))}/track", params)
    async def voyages(self, **params: Any) -> Any:
        """Active Voyages"""
        return await self._get("/shipping/voyages", params)
