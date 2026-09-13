from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Derivatives(SyncResource):
    def options_flow(self, identifier: str, **params: Any) -> Any:
        """Options Flow"""
        return self._get(f"/derivatives/options/flow/{quote(str(identifier))}", params)
    def options_greeks(self, identifier: str, **params: Any) -> Any:
        """Options Greeks"""
        return self._get(f"/derivatives/options/greeks/{quote(str(identifier))}", params)
    def options_iv_surface(self, identifier: str, **params: Any) -> Any:
        """IV Surface"""
        return self._get(f"/derivatives/options/iv-surface/{quote(str(identifier))}", params)
    def options_price(self, body: Any = None, **params: Any) -> Any:
        """Price Option"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/derivatives/options/price", body, params)
    def options_strategy(self, body: Any = None, **params: Any) -> Any:
        """Strategy Analysis"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/derivatives/options/strategy", body, params)
    def options_unusual_activity(self, **params: Any) -> Any:
        """Unusual Options Activity"""
        return self._get("/derivatives/options/unusual-activity", params)


class AsyncDerivatives(AsyncResource):
    async def options_flow(self, identifier: str, **params: Any) -> Any:
        """Options Flow"""
        return await self._get(f"/derivatives/options/flow/{quote(str(identifier))}", params)
    async def options_greeks(self, identifier: str, **params: Any) -> Any:
        """Options Greeks"""
        return await self._get(f"/derivatives/options/greeks/{quote(str(identifier))}", params)
    async def options_iv_surface(self, identifier: str, **params: Any) -> Any:
        """IV Surface"""
        return await self._get(f"/derivatives/options/iv-surface/{quote(str(identifier))}", params)
    async def options_price(self, body: Any = None, **params: Any) -> Any:
        """Price Option"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/derivatives/options/price", body, params)
    async def options_strategy(self, body: Any = None, **params: Any) -> Any:
        """Strategy Analysis"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/derivatives/options/strategy", body, params)
    async def options_unusual_activity(self, **params: Any) -> Any:
        """Unusual Options Activity"""
        return await self._get("/derivatives/options/unusual-activity", params)
