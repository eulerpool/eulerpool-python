from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class RiskModels(SyncResource):
    def covariance(self, **params: Any) -> Any:
        """Factor Covariance Matrix"""
        return self._get("/risk-models/covariance", params)
    def exposure(self, identifier: str, **params: Any) -> Any:
        """Factor Exposure"""
        return self._get(f"/risk-models/exposure/{quote(str(identifier))}", params)
    def factor_returns(self, **params: Any) -> Any:
        """Factor Returns"""
        return self._get("/risk-models/factor-returns", params)
    def factors(self, **params: Any) -> Any:
        """Available Risk Factors"""
        return self._get("/risk-models/factors", params)
    def portfolio_risk(self, body: Any = None, **params: Any) -> Any:
        """Portfolio Risk Decomposition"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/risk-models/portfolio-risk", body, params)


class AsyncRiskModels(AsyncResource):
    async def covariance(self, **params: Any) -> Any:
        """Factor Covariance Matrix"""
        return await self._get("/risk-models/covariance", params)
    async def exposure(self, identifier: str, **params: Any) -> Any:
        """Factor Exposure"""
        return await self._get(f"/risk-models/exposure/{quote(str(identifier))}", params)
    async def factor_returns(self, **params: Any) -> Any:
        """Factor Returns"""
        return await self._get("/risk-models/factor-returns", params)
    async def factors(self, **params: Any) -> Any:
        """Available Risk Factors"""
        return await self._get("/risk-models/factors", params)
    async def portfolio_risk(self, body: Any = None, **params: Any) -> Any:
        """Portfolio Risk Decomposition"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/risk-models/portfolio-risk", body, params)
