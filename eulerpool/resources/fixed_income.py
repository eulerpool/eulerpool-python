from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class FixedIncome(SyncResource):
    def analytics(self, body: Any = None, **params: Any) -> Any:
        """Bond Analytics"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/fixed-income/analytics", body, params)
    def curve_forward(self, **params: Any) -> Any:
        """Forward Curve"""
        return self._get("/fixed-income/curve/forward", params)
    def curve_spot(self, **params: Any) -> Any:
        """Spot Curve"""
        return self._get("/fixed-income/curve/spot", params)
    def default_probabilities(self, **params: Any) -> Any:
        """Implied Default Probabilities"""
        return self._get("/fixed-income/default-probabilities", params)


class AsyncFixedIncome(AsyncResource):
    async def analytics(self, body: Any = None, **params: Any) -> Any:
        """Bond Analytics"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/fixed-income/analytics", body, params)
    async def curve_forward(self, **params: Any) -> Any:
        """Forward Curve"""
        return await self._get("/fixed-income/curve/forward", params)
    async def curve_spot(self, **params: Any) -> Any:
        """Spot Curve"""
        return await self._get("/fixed-income/curve/spot", params)
    async def default_probabilities(self, **params: Any) -> Any:
        """Implied Default Probabilities"""
        return await self._get("/fixed-income/default-probabilities", params)
